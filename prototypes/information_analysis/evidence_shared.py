"""Evidence on facts that one table's profile cannot show alone, written into each table it concerns.

Round 1 records these as facts about each table (here: key stability, item 6); what they mean between tables is
round 2's (ADR-0019).

    python prototypes/information_analysis/evidence_shared.py
"""
import inspect
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from profile_tables import ROOT, DAY, reader, write, blob, now, sha, RAW  # noqa: E402
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
