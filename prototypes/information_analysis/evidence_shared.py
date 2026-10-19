"""Evidence on facts that one table's profile cannot show alone, written into each table it concerns.

Round 1 records these as facts about each table (here: key stability, item 6); what they mean between tables is
round 2's (ADR-0019).

    python prototypes/information_analysis/evidence_shared.py
"""
import inspect
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from profile_tables import ROOT, DAY, PREV, reader, write, blob, now, sha, RAW  # noqa: E402
import ia_lib as ia  # noqa: E402

SCRIPT = "prototypes/information_analysis/evidence_shared.py"
TRANSACTION_TABLES = {"Sales.CustomerTransactions": "CustomerTransactionID",
                      "Purchasing.SupplierTransactions": "SupplierTransactionID",
                      "Warehouse.StockItemTransactions": "StockItemTransactionID"}


def shared_transaction_numbering():
    ids = {}
    for t, col in TRANSACTION_TABLES.items():
        f, head, rows = reader(DAY, t)
        i = head.index(col)
        ids[t] = set(int(r[i]) for r in rows)
        f.close()
    names = list(ids)
    union = set().union(*ids.values())
    return {"tables": {t: {"rows": len(v), "min": min(v), "max": max(v)} for t, v in ids.items()},
            "overlap_between_tables": {"%s & %s" % (a, b): len(ids[a] & ids[b]) for i, a in enumerate(names) for b in names[i + 1:]},
            "union_rows": len(union), "union_min": min(union), "union_max": max(union),
            "numbers_unused_in_union_range": max(union) - min(union) + 1 - len(union)}


def main():
    rec = {"kind": "profile", "tool": SCRIPT, "tool_version": blob(SCRIPT), "code": inspect.getsource(shared_transaction_numbering),
           "inputs": {"source": "wwi", "extract": DAY, "manifest_sha256": sha(os.path.join(RAW, DAY, "manifest.json")),
                      "tables": sorted(TRANSACTION_TABLES)}, "ran_at": now(), "result": shared_transaction_numbering()}
    for t in TRANSACTION_TABLES:
        s, n = t.split(".")
        h = write(os.path.join(ROOT, "analysis", "wwi", "tables", ia.escape(s), ia.escape(n), "evidence"), rec)
    print(h, rec["result"]["numbers_unused_in_union_range"])


if __name__ == "__main__" and len(sys.argv) == 1:
    main()


CANDIDATE_KEYS = {"Purchasing.PurchaseOrderLines": [["PurchaseOrderID", "StockItemID"]],
                  "Sales.OrderLines": [["OrderID", "StockItemID"]],
                  "Sales.InvoiceLines": [["InvoiceID", "StockItemID"]],
                  "Sales.Invoices": [["OrderID"]],
                  "Sales.CustomerTransactions": [["InvoiceID"]],
                  "Purchasing.SupplierTransactions": [["PurchaseOrderID"]],
                  "Warehouse.StockItemTransactions": [["InvoiceID", "StockItemID"], ["PurchaseOrderID", "StockItemID"]],
                  "Warehouse.VehicleTemperatures": [["ChillerSensorNumber", "RecordedWhen"]],
                  "Warehouse.ColdRoomTemperatures": [["ColdRoomSensorNumber"]]}


def candidate_key(table, cols):
    """Is this column combination unique, among the rows where all its columns are filled?"""
    f, head, rows = reader(DAY, table)
    idx = [head.index(c) for c in cols]
    seen, dup, filled, n = set(), 0, 0, 0
    for r in rows:
        n += 1
        k = tuple(r[i] for i in idx)
        if "" in k:
            continue
        filled += 1
        if k in seen:
            dup += 1
        seen.add(k)
    f.close()
    return {"columns": cols, "rows": n, "rows_with_all_filled": filled, "distinct": len(seen), "duplicate_rows": dup}


def main_candidates():
    for t, combos in CANDIDATE_KEYS.items():
        s, n = t.split(".")
        rec = {"kind": "profile", "tool": SCRIPT, "tool_version": blob(SCRIPT), "code": inspect.getsource(candidate_key),
               "inputs": {"source": "wwi", "extract": DAY, "manifest_sha256": sha(os.path.join(RAW, DAY, "manifest.json")), "table": t},
               "ran_at": now(), "result": [candidate_key(t, c) for c in combos]}
        h = write(os.path.join(ROOT, "analysis", "wwi", "tables", ia.escape(s), ia.escape(n), "evidence"), rec)
        print(t, h, [(r["columns"], r["rows_with_all_filled"], r["distinct"], r["duplicate_rows"]) for r in rec["result"]])


if __name__ == "__main__" and len(sys.argv) > 1 and sys.argv[1] == "candidates":
    main_candidates()


def invoice_line_arithmetic():
    """Do TaxAmount and ExtendedPrice follow from Quantity, UnitPrice and TaxRate, and how is tax rounded?"""
    from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
    f, head, rows = reader(DAY, "Sales.InvoiceLines")
    i = {c: head.index(c) for c in ("Quantity", "UnitPrice", "TaxRate", "TaxAmount", "ExtendedPrice")}
    n = tax_exact = tax_half_up = tax_half_even = ext_ok = 0
    worst = Decimal(0)
    for r in rows:
        n += 1
        q, up, tr = Decimal(r[i["Quantity"]]), Decimal(r[i["UnitPrice"]]), Decimal(r[i["TaxRate"]])
        tax, ext = Decimal(r[i["TaxAmount"]]), Decimal(r[i["ExtendedPrice"]])
        raw = q * up * tr / 100
        tax_exact += raw == tax
        tax_half_up += raw.quantize(Decimal("0.01"), ROUND_HALF_UP) == tax
        tax_half_even += raw.quantize(Decimal("0.01"), ROUND_HALF_EVEN) == tax
        ext_ok += q * up + tax == ext
        worst = max(worst, abs(raw - tax))
    f.close()
    return {"rows": n, "tax_equals_quantity_x_price_x_rate_exactly": tax_exact,
            "tax_equals_it_rounded_half_up_to_cents": tax_half_up, "tax_equals_it_rounded_half_even_to_cents": tax_half_even,
            "extended_price_equals_quantity_x_price_plus_tax": ext_ok, "largest_difference_tax_vs_unrounded": str(worst)}


def main_arithmetic():
    rec = {"kind": "profile", "tool": SCRIPT, "tool_version": blob(SCRIPT), "code": inspect.getsource(invoice_line_arithmetic),
           "inputs": {"source": "wwi", "extract": DAY, "manifest_sha256": sha(os.path.join(RAW, DAY, "manifest.json")), "table": "Sales.InvoiceLines"},
           "ran_at": now(), "result": invoice_line_arithmetic()}
    print(write(os.path.join(ROOT, "analysis", "wwi", "tables", "Sales", "InvoiceLines", "evidence"), rec), rec["result"])


if __name__ == "__main__" and len(sys.argv) > 1 and sys.argv[1] == "arithmetic":
    main_arithmetic()


DOC_URL = "https://learn.microsoft.com/en-us/sql/samples/wide-world-importers-what-is?view=sql-server-ver17"
DOC_TABLES = ["Sales.Orders", "Sales.Invoices", "Sales.Customers", "Sales.CustomerCategories", "Sales.CustomerTransactions",
              "Purchasing.SupplierTransactions", "Purchasing.PurchaseOrders", "Warehouse.StockItemTransactions",
              "Warehouse.StockItemHoldings", "Warehouse.VehicleTemperatures", "Warehouse.ColdRoomTemperatures", "Warehouse.StockItems"]
DOC_EXCERPTS = {
    "purchasing": ["WWI creates purchase orders and submits the orders to the suppliers.",
                   "Periodically, WWI pays suppliers for items that were on purchase orders. The payments often occur some time after they receive the goods."],
    "stocking": ["Suppliers send the items. WWI receives them and stocks them in their warehouse."],
    "customer_orders": ["If possible, WWI fills the customer order with stock items in the warehouse. When they don't have sufficient stock, they order the additional stock from the suppliers.",
                        "Some customers don't want to wait for items that aren't in stock. If they order, for example, five different stock items, and four are available, they want to receive the four items and backorder the remaining item. The item is then sent later in a separate shipment."],
    "invoicing": ["WWI invoices customers for the stock items, typically by converting the order to an invoice."],
    "delivery": ["WWI delivers stock items to customers either via their own delivery vans or via other couriers or freight methods."],
    "payments": ["Customers pay invoices to WWI."],
    "credit_notes": ["WWI issues credit notes when a customer doesn't receive goods for some reason, or when goods are faulty. These notes are treated as negative invoices."],
    "stocktakes": ["WWI periodically counts the on-hand quantities of stock items to ensure that the stock quantities shown as available in their system are accurate. (This process is called a stocktake.)"],
    "customers": ["WWI is a wholesaler. Its customers are mostly companies that resell to individuals. WWI sells to retail customers across the United States, including specialty stores, supermarkets, computing stores, tourist attraction shops, and some individuals.",
                  "WWI also sells to other wholesalers via a network of agents who promote the products on WWI's behalf."],
    "fiscal_year": ["The company operates with a financial year that starts on November 1."],
    "chilled": ["Now, to meet food handling requirements, they must monitor the temperature in their chiller room and any of their trucks that have chiller sections.",
                "Perishable goods are stored in refrigerated rooms. Sensor data from these rooms is ingested into the database for monitoring and analytics.",
                "Vehicles that transport goods for WWI include sensors that track their location. This location is also ingested into the database for monitoring and further analytics."],
}


def main_documentation():
    rec = {"kind": "web source", "tool": "WebFetch (a summarising fetch; the excerpts were returned as verbatim quotations, not checked against the page by hand)",
           "tool_version": "n/a", "ran_at": "2026-10-18T20:40:00Z", "inputs": {"url": DOC_URL, "title": "What is Wide World Importers (Microsoft Learn)"},
           "excerpt": DOC_EXCERPTS, "result": {"describes": "the business and its workflows; no schema, table or column documentation"}}
    for t in DOC_TABLES:
        s, n = t.split(".")
        h = write(os.path.join(ROOT, "analysis", "wwi", "tables", ia.escape(s), ia.escape(n), "evidence"), rec)
    write(os.path.join(ROOT, "analysis", "wwi", "_source", "evidence"), rec)
    print(h)


if __name__ == "__main__" and len(sys.argv) > 1 and sys.argv[1] == "documentation":
    main_documentation()


CODE_TABLES = {"TransactionTypeID": ("Application.TransactionTypes", "TransactionTypeName"),
               "PaymentMethodID": ("Application.PaymentMethods", "PaymentMethodName"),
               "DeliveryMethodID": ("Application.DeliveryMethods", "DeliveryMethodName"),
               "PackageTypeID": ("Warehouse.PackageTypes", "PackageTypeName"),
               "SupplierCategoryID": ("Purchasing.SupplierCategories", "SupplierCategoryName"),
               "CustomerCategoryID": ("Sales.CustomerCategories", "CustomerCategoryName"),
               "BuyingGroupID": ("Sales.BuyingGroups", "BuyingGroupName"),
               "StockGroupID": ("Warehouse.StockGroups", "StockGroupName")}
CODE_USERS = ["Sales.CustomerTransactions", "Purchasing.SupplierTransactions", "Warehouse.StockItemTransactions",
              "Sales.Invoices", "Sales.Customers", "Purchasing.PurchaseOrders", "Purchasing.Suppliers",
              "Sales.InvoiceLines", "Sales.OrderLines", "Purchasing.PurchaseOrderLines", "Sales.SpecialDeals",
              "Warehouse.StockItemStockGroups"]


def code_labels(table):
    """For each code column of the table, the codes used and their names in the code table."""
    f, head, rows = reader(DAY, table)
    rows = list(rows)
    f.close()
    out = {}
    for col, (ct, name_col) in CODE_TABLES.items():
        if col not in head:
            continue
        g, h2, r2 = reader(DAY, ct)
        names = {r[0]: r[h2.index(name_col)] for r in r2}
        g.close()
        i = head.index(col)
        used = {}
        for r in rows:
            used[r[i]] = used.get(r[i], 0) + 1
        out[col] = {"code_table": ct, "used": {v or "(empty)": {"rows": k, "name": names.get(v)} for v, k in sorted(used.items())},
                    "defined_but_unused": {c: n for c, n in names.items() if c not in used}}
    return out


def delivery_json_keys():
    """Keys inside the delivery JSON of Sales.Invoices, counted over all invoices."""
    import collections, json as js
    f, head, rows = reader(DAY, "Sales.Invoices")
    i = head.index("ReturnedDeliveryData")
    top, ev, ev_n = collections.Counter(), collections.Counter(), collections.Counter()
    status = collections.Counter()
    for r in rows:
        o = js.loads(r[i])
        top.update(o.keys())
        ev_n[len(o.get("Events", []))] += 1
        for e in o.get("Events", []):
            ev.update(e.keys())
            status[e.get("Event", "") + "/" + str(e.get("Status", ""))] += 1
    f.close()
    return {"top_level_keys": dict(top), "events_per_invoice": dict(ev_n), "event_keys": dict(ev), "event_and_status": dict(status)}


def coldroom_history():
    """The cold-room current table against its history table, and the sensors across the two extracts."""
    import collections
    out = {}
    for day in (PREV, DAY):
        f, head, rows = reader(day, "Warehouse.ColdRoomTemperatures")
        rows = list(rows)
        f.close()
        out["current_" + day] = {"ids": sorted(int(r[0]) for r in rows), "sensors": sorted(r[head.index("ColdRoomSensorNumber")] for r in rows),
                                 "recorded_when": sorted(set(r[head.index("RecordedWhen")] for r in rows))}
    f, head, rows = reader(DAY, "Warehouse.ColdRoomTemperatures_Archive")
    i = {c: head.index(c) for c in head}
    n, sensors, lo, hi, vf_eq = 0, collections.Counter(), None, None, 0
    idmin, idmax = None, None
    for r in rows:
        n += 1
        sensors[r[i["ColdRoomSensorNumber"]]] += 1
        w = r[i["RecordedWhen"]]
        lo = w if lo is None or w < lo else lo
        hi = w if hi is None or w > hi else hi
        vf_eq += r[i["ValidFrom"]][:19] == w[:19]
        k = int(r[0])
        idmin = k if idmin is None or k < idmin else idmin
        idmax = k if idmax is None or k > idmax else idmax
    f.close()
    out["history"] = {"rows": n, "rows_per_sensor": dict(sensors), "recorded_when_min": lo, "recorded_when_max": hi,
                      "valid_from_equals_recorded_when_to_the_second": vf_eq, "id_min": idmin, "id_max": idmax}
    return out


def main_more():
    base = {"kind": "profile", "tool": SCRIPT, "tool_version": blob(SCRIPT), "ran_at": now()}
    inp = {"source": "wwi", "extract": DAY, "manifest_sha256": sha(os.path.join(RAW, DAY, "manifest.json"))}
    for t in CODE_USERS:
        s, n = t.split(".")
        rec = dict(base, code=inspect.getsource(code_labels), inputs=dict(inp, table=t), result=code_labels(t))
        print(t, "labels", write(os.path.join(ROOT, "analysis", "wwi", "tables", s, n, "evidence"), rec))
    rec = dict(base, code=inspect.getsource(delivery_json_keys), inputs=dict(inp, table="Sales.Invoices"), result=delivery_json_keys())
    print("Sales.Invoices delivery_json", write(os.path.join(ROOT, "analysis", "wwi", "tables", "Sales", "Invoices", "evidence"), rec), rec["result"]["event_keys"])
    rec = dict(base, code=inspect.getsource(coldroom_history), inputs=dict(inp, previous_extract=PREV), result=coldroom_history())
    for n in ("ColdRoomTemperatures", "ColdRoomTemperatures_Archive"):
        h = write(os.path.join(ROOT, "analysis", "wwi", "tables", "Warehouse", n, "evidence"), rec)
    print("coldroom", h, json.dumps(rec["result"])[:900])


if __name__ == "__main__" and len(sys.argv) > 1 and sys.argv[1] == "more":
    import json
    main_more()
