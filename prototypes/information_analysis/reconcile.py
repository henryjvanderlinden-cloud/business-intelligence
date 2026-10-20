"""Round 2 reconciliations (item 16 across tables; ADR-0019, analysis/README.md section 9).

Each function compares what two or more tables say about the same thing and returns counts only. main() writes one
evidence file per reconciliation into analysis/wwi/across/reconciliations/<slug>/evidence/ and the item file
16_reconciliation.md, with mechanical claims from the counts plus the agent's readings from a notes module.

    python prototypes/information_analysis/reconcile.py <notes module>
"""
import collections
import csv
import datetime
import gzip
import hashlib
import importlib.util
import inspect
import json
import os
import sys
from decimal import Decimal as D, ROUND_HALF_UP

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from evidence_orders import blob, sha, now  # noqa: E402
from relations import write_evidence  # noqa: E402
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import ia_lib as ia  # noqa: E402

SCRIPT = "prototypes/information_analysis/reconcile.py"
RAW = os.path.join(ROOT, "data", "raw", "wwi")
DAY, PREV = os.environ.get("IA_DAY", "2016-06-01"), os.environ.get("IA_PREV", "2016-05-31")   # recheck.py sets them
OUT = os.path.join(ROOT, "analysis", "wwi", "across", "reconciliations")
csv.field_size_limit(1 << 30)
_cache = {}


def rows(table, day=DAY):
    if (table, day) not in _cache:
        with gzip.open(os.path.join(RAW, day, table + ".csv.gz"), "rt", encoding="utf-8", newline="") as f:
            _cache[(table, day)] = list(csv.DictReader(f))
    return _cache[(table, day)]


def cmp(a, b):
    return "equal to" if a == b else "greater than" if a > b else "less than"


def invoice_lines_vs_stock_issues():
    """Each stock issue against the invoice line it belongs to (InvoiceID, StockItemID): quantity and date."""
    lines = {(r["InvoiceID"], r["StockItemID"]): r for r in rows("Sales.InvoiceLines")}
    inv = {r["InvoiceID"]: r["InvoiceDate"][:10] for r in rows("Sales.Invoices")}
    qty, date, kinds, per_key = collections.Counter(), collections.Counter(), collections.Counter(), collections.Counter()
    for s in rows("Warehouse.StockItemTransactions"):
        if not s["InvoiceID"]:
            continue
        kinds[s["TransactionTypeID"]] += 1
        per_key[(s["InvoiceID"], s["StockItemID"])] += 1
        line = lines.get((s["InvoiceID"], s["StockItemID"]))
        if line is None:
            qty["no line"] += 1
            continue
        q, lq = D(s["Quantity"]), D(line["Quantity"])
        qty["movement = -line quantity" if q == -lq else "movement = line quantity" if q == lq else "other"] += 1
        date["movement date " + cmp(s["TransactionOccurredWhen"][:10], inv[s["InvoiceID"]]) + " invoice date"] += 1
    line_rows = len(rows("Sales.InvoiceLines"))
    return {"movements_with_invoice": sum(kinds.values()), "by_transaction_type": dict(kinds), "quantity": dict(qty),
            "date_against_invoice_date": dict(date), "invoice_line_rows": line_rows, "distinct_line_keys": len(lines),
            "line_keys_with_more_than_one_movement": sum(1 for k, v in per_key.items() if v > 1),
            "lines_without_movement": sum(1 for k in lines if k not in per_key)}


def ledger_invoices_vs_invoice_lines():
    """Each customer-ledger invoice entry against the sum of its invoice lines: amounts, tax and date."""
    agg = collections.defaultdict(lambda: [D(0), D(0), D(0), 0])
    for l in rows("Sales.InvoiceLines"):
        a = agg[l["InvoiceID"]]
        a[0] += D(l["Quantity"]) * D(l["UnitPrice"])
        a[1] += D(l["TaxAmount"])
        a[2] += D(l["ExtendedPrice"])
        a[3] += D(l["ExtendedPrice"]) == D(l["Quantity"]) * D(l["UnitPrice"]) + D(l["TaxAmount"])
    inv = {r["InvoiceID"]: r["InvoiceDate"][:10] for r in rows("Sales.Invoices")}
    out = collections.Counter()
    n = 0
    for t in rows("Sales.CustomerTransactions"):
        if not t["InvoiceID"]:
            continue
        n += 1
        a = agg[t["InvoiceID"]]
        out["AmountExcludingTax " + cmp(D(t["AmountExcludingTax"]), a[0]) + " sum of Quantity x UnitPrice"] += 1
        out["TaxAmount " + cmp(D(t["TaxAmount"]), a[1]) + " sum of line TaxAmount"] += 1
        out["TransactionAmount " + cmp(D(t["TransactionAmount"]), a[2]) + " sum of ExtendedPrice"] += 1
        out["TransactionDate " + cmp(t["TransactionDate"][:10], inv[t["InvoiceID"]]) + " InvoiceDate"] += 1
    lines = sum(1 for _ in rows("Sales.InvoiceLines"))
    return {"invoice_entries": n, "comparisons": dict(sorted(out.items())), "invoice_lines": lines,
            "lines_where_ExtendedPrice_is_Quantity_x_UnitPrice_plus_TaxAmount": sum(a[3] for a in agg.values())}


def payments_vs_invoices(table, party, invoice_type, payment_type):
    """Ledger payments against the same party's invoice entries finalized on the payment's date: whether the payment
    equals their total, how many invoices it settles, and how long after its date an invoice is finalized."""
    t = rows(table)
    invs = [r for r in t if r["TransactionTypeID"] == invoice_type]
    pays = [r for r in t if r["TransactionTypeID"] == payment_type]
    fin_sum, fin_n = collections.defaultdict(lambda: D(0)), collections.Counter()
    for r in invs:
        if r["FinalizationDate"]:
            k = (r[party], r["FinalizationDate"][:10])
            fin_sum[k] += D(r["TransactionAmount"])
            fin_n[k] += 1
    pay_keys = collections.Counter((p[party], p["TransactionDate"][:10]) for p in pays)
    match, per_payment = collections.Counter(), collections.Counter()
    for p in pays:
        k = (p[party], p["TransactionDate"][:10])
        match["payment = -(invoices finalized that day)" if fin_sum.get(k) == -D(p["TransactionAmount"]) else
              "no invoice finalized that day" if k not in fin_sum else "amounts differ"] += 1
        per_payment[fin_n.get(k, 0)] += 1
    lag = collections.Counter((datetime.date.fromisoformat(r["FinalizationDate"][:10]) -
                               datetime.date.fromisoformat(r["TransactionDate"][:10])).days for r in invs if r["FinalizationDate"])
    state = collections.Counter("IsFinalized=%s|FinalizationDate=%s|OutstandingBalance=%s" % (
        r["IsFinalized"], "set" if r["FinalizationDate"] else "empty", "0" if D(r["OutstandingBalance"]) == 0 else
        "the full amount" if D(r["OutstandingBalance"]) == D(r["TransactionAmount"]) else "partial") for r in invs)
    pstate = collections.Counter("IsFinalized=%s|OutstandingBalance=%s" % (r["IsFinalized"], "0" if D(r["OutstandingBalance"]) == 0 else "not 0")
                                 for r in pays)
    return {"invoices": len(invs), "payments": len(pays), "payments_per_party_and_day_max": max(pay_keys.values()) if pay_keys else 0,
            "payment_against_invoices_finalized_that_day": dict(match),
            "invoices_finalized_on_the_payments_party_and_day": {str(k): v for k, v in sorted(per_payment.items())},
            "party_days_with_finalized_invoices_but_no_payment": sum(1 for k in fin_sum if k not in pay_keys),
            "days_from_invoice_to_finalization": {str(k): v for k, v in sorted(lag.items())},
            "invoice_states": dict(state), "payment_states": dict(pstate)}


def customer_payments_vs_invoices():
    return payments_vs_invoices("Sales.CustomerTransactions", "CustomerID", "1", "3")


def supplier_payments_vs_invoices():
    return payments_vs_invoices("Purchasing.SupplierTransactions", "SupplierID", "5", "7")


def supplier_invoices_vs_purchase_order_lines():
    """Each supplier invoice against its purchase order's lines at the expected price per outer."""
    agg = collections.defaultdict(lambda: [D(0), D(0), D(0)])
    for l in rows("Purchasing.PurchaseOrderLines"):
        p = D(l["ExpectedUnitPricePerOuter"])
        agg[l["PurchaseOrderID"]][0] += D(l["ReceivedOuters"]) * p
        agg[l["PurchaseOrderID"]][1] += D(l["OrderedOuters"]) * p
        agg[l["PurchaseOrderID"]][2] += (D(l["ReceivedOuters"]) * p * D("0.15")).quantize(D("0.01"), ROUND_HALF_UP)
    out = collections.Counter()
    for t in rows("Purchasing.SupplierTransactions"):
        if t["TransactionTypeID"] != "5":
            continue
        ex = D(t["AmountExcludingTax"])
        a = agg[t["PurchaseOrderID"]]
        out["AmountExcludingTax " + cmp(ex, a[0]) + " sum of ReceivedOuters x ExpectedUnitPricePerOuter"] += 1
        out["AmountExcludingTax " + cmp(ex, a[1]) + " sum of OrderedOuters x ExpectedUnitPricePerOuter"] += 1
        out["TaxAmount " + cmp(D(t["TaxAmount"]), (ex * D("0.15")).quantize(D("0.01"), ROUND_HALF_UP)) + " 15% of AmountExcludingTax, rounded half up"] += 1
        out["TaxAmount " + cmp(D(t["TaxAmount"]), a[2]) + " the sum over lines of 15% of ReceivedOuters x ExpectedUnitPricePerOuter, each rounded half up"] += 1
        out["TransactionAmount " + cmp(D(t["TransactionAmount"]), ex + D(t["TaxAmount"])) + " AmountExcludingTax + TaxAmount"] += 1
    return {"supplier_invoices": sum(1 for t in rows("Purchasing.SupplierTransactions") if t["TransactionTypeID"] == "5"),
            "comparisons": dict(sorted(out.items()))}


def stock_holdings_vs_movements():
    """QuantityOnHand against the stock movements: the level against the sum of all movements, and the change between
    the two extracts against the movements added between them."""
    h1 = {r["StockItemID"]: r for r in rows("Warehouse.StockItemHoldings")}
    h0 = {r["StockItemID"]: r for r in rows("Warehouse.StockItemHoldings", PREV)}
    total, added = collections.defaultdict(lambda: D(0)), collections.defaultdict(lambda: D(0))
    before = {r["StockItemTransactionID"]: r["Quantity"] for r in rows("Warehouse.StockItemTransactions", PREV)}
    new_types = collections.Counter()
    seen, changed = set(), 0
    for r in rows("Warehouse.StockItemTransactions"):
        total[r["StockItemID"]] += D(r["Quantity"])
        seen.add(r["StockItemTransactionID"])
        if r["StockItemTransactionID"] not in before:
            added[r["StockItemID"]] += D(r["Quantity"])
            new_types[r["TransactionTypeID"]] += 1
        elif D(before[r["StockItemTransactionID"]]) != D(r["Quantity"]):
            changed += 1
    level = collections.Counter(cmp(D(h1[i]["QuantityOnHand"]), total[i]) for i in h1)
    change = collections.Counter()
    direction = collections.Counter()
    for i in h1:
        d = D(h1[i]["QuantityOnHand"]) - D(h0[i]["QuantityOnHand"]) if i in h0 else None
        if d is None:
            change["item not in the earlier extract"] += 1
            continue
        change["change " + cmp(d, added[i]) + " movements added"] += 1
        direction["QuantityOnHand " + ("rose" if d > 0 else "fell" if d < 0 else "unchanged")] += 1
    return {"items": len(h1), "level_against_sum_of_all_movements": dict(level), "movements_added_between_extracts": dict(new_types),
            "earlier_movements_with_changed_quantity": changed, "earlier_movements_deleted": sum(1 for k in before if k not in seen),
            "change_against_movements_added": dict(change), "change_direction": dict(direction),
            "items_with_negative_QuantityOnHand": sum(1 for i in h1 if D(h1[i]["QuantityOnHand"]) < 0),
            "LastStocktakeQuantity_equals_QuantityOnHand": sum(1 for i in h1 if h1[i]["LastStocktakeQuantity"] == h1[i]["QuantityOnHand"])}


RECONCILIATIONS = {
    "invoice-lines-vs-stock-issues": (invoice_lines_vs_stock_issues, ["Sales.InvoiceLines", "Sales.Invoices", "Warehouse.StockItemTransactions"], [DAY]),
    "ledger-invoices-vs-invoice-lines": (ledger_invoices_vs_invoice_lines, ["Sales.CustomerTransactions", "Sales.InvoiceLines", "Sales.Invoices"], [DAY]),
    "customer-payments-vs-invoices": (customer_payments_vs_invoices, ["Sales.CustomerTransactions"], [DAY]),
    "supplier-payments-vs-invoices": (supplier_payments_vs_invoices, ["Purchasing.SupplierTransactions"], [DAY]),
    "supplier-invoices-vs-purchase-order-lines": (supplier_invoices_vs_purchase_order_lines, ["Purchasing.SupplierTransactions", "Purchasing.PurchaseOrderLines"], [DAY]),
    "stock-holdings-vs-movements": (stock_holdings_vs_movements, ["Warehouse.StockItemHoldings", "Warehouse.StockItemTransactions"], [PREV, DAY]),
}


def schema_hash(tables):
    hs = []
    for t in sorted(tables):
        with gzip.open(os.path.join(RAW, DAY, t + ".csv.gz"), "rt", encoding="utf-8", newline="") as f:
            hs.append(ia.schema_hash(next(csv.reader(f))))
    return hashlib.sha256("\n".join(hs).encode("ascii")).hexdigest()


def main(argv):
    sp = importlib.util.spec_from_file_location("notes", argv[1])
    notes = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(notes)
    base = {"kind": "profile", "tool": SCRIPT, "tool_version": blob(SCRIPT), "ran_at": now()}
    method = ("counts by prototypes/information_analysis/reconcile.py (blob %s); readings by %s from those counts"
              % (base["tool_version"], notes.COMMON["written_by"]))
    for slug, (fn, tables, days) in RECONCILIATIONS.items():
        code = inspect.getsource(fn)
        if fn in (customer_payments_vs_invoices, supplier_payments_vs_invoices):
            code += "\n" + inspect.getsource(payments_vs_invoices)
        inputs = {"source": "wwi", "extracts": {d: sha(os.path.join(RAW, d, "manifest.json")) for d in days}, "tables": tables}
        result = fn()
        h = write_evidence(os.path.join(OUT, slug, "evidence"), dict(base, code=code, inputs=inputs, result=result))
        print(slug, h, json.dumps(result)[:400])
        note = notes.NOTES[slug]
        claims = [("observed", "high", ["rec"], "every new extract", t) for t in note["counts"](result)]
        claims += [c for c in note.get("readings", [])]
        conf = ia.CONFIDENCE[min(ia.CONFIDENCE.index(c[1]) for c in claims)]
        lines = []
        for i, (typ, cf, ev, recheck, text) in enumerate(claims, 1):
            lines.append("- C%d | type=%s | status=proposed | confidence=%s | effective=%s | observed=%s | checked=%s | evidence=%s | "
                         "recheck=%s | text: %s" % (i, typ, cf, DAY, notes.NOW[:10], notes.NOW[:10], h if ev else "none", recheck, text))
        front = dict(notes.COMMON, id="wwi:reconciliation:%s" % slug, subject="wwi/across/reconciliations/%s" % slug, item="16",
                     topic="reconciliation", tier="best-effort", summary=note["summary"], confidence=conf, claims=str(len(claims)),
                     method=method, input_schema_sha256=schema_hash(tables),
                     last_checked_against=DAY, recheck_when=note.get("recheck", "every new extract, or a schema change of the tables compared"))
        txt = ("---\n" + "\n".join("%s: %s" % (k, front[k]) for k in ia.FRONT_KEYS) + "\n---\n\n## Claims\n\n" + "\n".join(lines) +
               "\n\n## Reasoning\n\n" + note["reasoning"] + "\n\n## Uncertainties\n\n" + (note.get("uncertainties") or "None.") +
               "\n\n## For a person\n\nNone.\n")
        assert all(ord(ch) < 128 for ch in txt), slug
        with open(os.path.join(OUT, slug, "16_reconciliation.md"), "w", encoding="ascii", newline="\n") as f:
            f.write(txt)


if __name__ == "__main__":
    main(sys.argv)
