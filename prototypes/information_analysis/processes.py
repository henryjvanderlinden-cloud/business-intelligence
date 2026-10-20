"""Round 2, item 24 (analysis/README.md section 9): the business processes the tables record, as the data shows them.

Each function follows one process through its tables and returns, per step, how many rows reach it and the days
between steps (counts and distributions only). main() writes the evidence to analysis/wwi/across/processes/<slug>/
evidence/ and the item file 24_processes.md, with mechanical claims from the counts and the agent's readings from a
notes module. As-is only (ADR-0020).

    python prototypes/information_analysis/processes.py <notes module>
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
import statistics
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from evidence_orders import blob, sha, now  # noqa: E402
from relations import write_evidence  # noqa: E402
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import ia_lib as ia  # noqa: E402

SCRIPT = "prototypes/information_analysis/processes.py"
RAW = os.path.join(ROOT, "data", "raw", "wwi")
DAY = os.environ.get("IA_DAY", "2016-06-01")   # recheck.py sets it
OUT = os.path.join(ROOT, "analysis", "wwi", "across", "processes")
csv.field_size_limit(1 << 30)
_cache = {}


def rows(table):
    if table not in _cache:
        with gzip.open(os.path.join(RAW, DAY, table + ".csv.gz"), "rt", encoding="utf-8", newline="") as f:
            _cache[table] = list(csv.DictReader(f))
    return _cache[table]


def days(a, b):
    return (datetime.date.fromisoformat(b[:10]) - datetime.date.fromisoformat(a[:10])).days


def dist(v):
    if not v:
        return {"rows": 0}
    v = sorted(v)
    return {"rows": len(v), "min": v[0], "median": statistics.median(v), "max": v[-1],
            "most_common": collections.Counter(v).most_common(4)}


def order_to_cash():
    """Order, picking, invoice, delivery, stock issue, ledger entry, payment: rows reaching each step, days between."""
    orders = rows("Sales.Orders")
    inv_by_order = {i["OrderID"]: i for i in rows("Sales.Invoices")}
    backorders = {o["BackorderOrderID"] for o in orders if o["BackorderOrderID"]}
    issues = collections.Counter(s["InvoiceID"] for s in rows("Warehouse.StockItemTransactions") if s["InvoiceID"])
    ledger = {t["InvoiceID"]: t for t in rows("Sales.CustomerTransactions") if t["InvoiceID"]}
    steps = collections.Counter()
    lag = collections.defaultdict(list)
    for o in orders:
        steps["1 order"] += 1
        if o["BackorderOrderID"]:
            steps["1a order split: has a backorder"] += 1
        if o["OrderID"] in backorders:
            steps["1b order is a backorder"] += 1
        if o["PickingCompletedWhen"]:
            steps["2 picked"] += 1
            lag["order to picking completed"].append(days(o["OrderDate"], o["PickingCompletedWhen"]))
        i = inv_by_order.get(o["OrderID"])
        if not i:
            continue
        steps["3 invoiced"] += 1
        lag["order to invoice"].append(days(o["OrderDate"], i["InvoiceDate"]))
        if o["PickingCompletedWhen"]:
            lag["picking completed to invoice"].append(days(o["PickingCompletedWhen"], i["InvoiceDate"]))
        if i["ConfirmedDeliveryTime"]:
            steps["4 delivery confirmed"] += 1
            lag["invoice to delivery confirmed"].append(days(i["InvoiceDate"], i["ConfirmedDeliveryTime"]))
        if issues.get(i["InvoiceID"]):
            steps["5 stock issued"] += 1
        t = ledger.get(i["InvoiceID"])
        if t:
            steps["6 booked in the customer ledger"] += 1
            if t["FinalizationDate"]:
                steps["7 paid (entry finalized)"] += 1
                lag["invoice to payment"].append(days(i["InvoiceDate"], t["FinalizationDate"]))
    return {"steps": dict(sorted(steps.items())), "days": {k: dist(v) for k, v in sorted(lag.items())},
            "orders_picked_without_invoice": sum(1 for o in orders if o["PickingCompletedWhen"] and o["OrderID"] not in inv_by_order)}


def procure_to_pay():
    """Purchase order, receipt (stock movement and line), supplier invoice, payment: rows reaching each step, days."""
    pos = rows("Purchasing.PurchaseOrders")
    receipts = collections.defaultdict(list)
    for s in rows("Warehouse.StockItemTransactions"):
        if s["PurchaseOrderID"]:
            receipts[s["PurchaseOrderID"]].append(s["TransactionOccurredWhen"])
    lines = collections.defaultdict(list)
    for l in rows("Purchasing.PurchaseOrderLines"):
        lines[l["PurchaseOrderID"]].append(l)
    inv = {t["PurchaseOrderID"]: t for t in rows("Purchasing.SupplierTransactions") if t["PurchaseOrderID"]}
    steps, lag = collections.Counter(), collections.defaultdict(list)
    for p in pos:
        steps["1 purchase order"] += 1
        lag["order to expected delivery"].append(days(p["OrderDate"], p["ExpectedDeliveryDate"]))
        if p["IsOrderFinalized"] == "1":
            steps["1a order finalized"] += 1
        if receipts.get(p["PurchaseOrderID"]):
            steps["2 received (stock movement)"] += 1
            first = min(receipts[p["PurchaseOrderID"]])
            lag["order to first receipt"].append(days(p["OrderDate"], first))
            lag["expected delivery to first receipt"].append(days(p["ExpectedDeliveryDate"], first))
        ls = lines.get(p["PurchaseOrderID"], [])
        if ls and all(l["IsOrderLineFinalized"] == "1" for l in ls):
            steps["2a every line finalized"] += 1
        if ls and all(l["ReceivedOuters"] == l["OrderedOuters"] for l in ls):
            steps["2b every line received in full (ReceivedOuters = OrderedOuters)"] += 1
        for l in ls:
            steps["lines"] += 1
            if receipts.get(p["PurchaseOrderID"]) and l["ReceivedOuters"] != l["OrderedOuters"]:
                steps["lines of received orders with ReceivedOuters different from OrderedOuters"] += 1
        t = inv.get(p["PurchaseOrderID"])
        if t:
            steps["3 supplier invoice"] += 1
            lag["order to supplier invoice"].append(days(p["OrderDate"], t["TransactionDate"]))
            if receipts.get(p["PurchaseOrderID"]):
                lag["first receipt to supplier invoice"].append(days(min(receipts[p["PurchaseOrderID"]]), t["TransactionDate"]))
            if t["FinalizationDate"]:
                steps["4 paid (invoice finalized)"] += 1
                lag["supplier invoice to payment"].append(days(t["TransactionDate"], t["FinalizationDate"]))
    return {"steps": dict(sorted(steps.items())), "days": {k: dist(v) for k, v in sorted(lag.items())}}


def stocktake():
    """Stock adjustments at stocktake: when they occur, how many items, and the holdings' stocktake columns."""
    adj = [s for s in rows("Warehouse.StockItemTransactions") if s["TransactionTypeID"] == "12"]
    when = collections.Counter(s["TransactionOccurredWhen"][:10] for s in adj)
    items_per_date = collections.defaultdict(set)
    for s in adj:
        items_per_date[s["TransactionOccurredWhen"][:10]].add(s["StockItemID"])
    h = rows("Warehouse.StockItemHoldings")
    return {"adjustments": len(adj), "dates": dict(sorted(when.items())), "items_adjusted": len({s["StockItemID"] for s in adj}),
            "distinct_items_per_date": {d: len(v) for d, v in sorted(items_per_date.items())},
            "adjustment_sign": dict(collections.Counter("positive" if float(s["Quantity"]) > 0 else "negative" if float(s["Quantity"]) < 0 else "zero" for s in adj)),
            "holdings": len(h), "holdings_LastStocktakeQuantity_filled": sum(1 for r in h if r["LastStocktakeQuantity"] != "")}


PROCESSES = {
    "order-to-cash": (order_to_cash, ["Sales.Orders", "Sales.Invoices", "Warehouse.StockItemTransactions", "Sales.CustomerTransactions"]),
    "procure-to-pay": (procure_to_pay, ["Purchasing.PurchaseOrders", "Purchasing.PurchaseOrderLines", "Warehouse.StockItemTransactions", "Purchasing.SupplierTransactions"]),
    "stocktake": (stocktake, ["Warehouse.StockItemTransactions", "Warehouse.StockItemHoldings"]),
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
    method = "counts by %s (blob %s); readings by %s" % (SCRIPT, base["tool_version"], notes.COMMON["written_by"])
    for slug, (fn, tables) in PROCESSES.items():
        code = inspect.getsource(fn) + "\n" + inspect.getsource(days) + "\n" + inspect.getsource(dist)
        result = fn()
        h = write_evidence(os.path.join(OUT, slug, "evidence"),
                           dict(base, code=code, inputs={"source": "wwi", "extract": DAY, "manifest_sha256": sha(os.path.join(RAW, DAY, "manifest.json")),
                                                         "tables": tables}, result=result))
        print(slug, h, json.dumps(result)[:600])
        note = notes.NOTES[slug]
        claims = [("observed", "high", True, "every new extract", t) for t in note["counts"](result)] + list(note.get("readings", []))
        conf = ia.CONFIDENCE[min(ia.CONFIDENCE.index(c[1]) for c in claims)]
        lines = ["- C%d | type=%s | status=proposed | confidence=%s | effective=%s | observed=%s | checked=%s | evidence=%s | recheck=%s | text: %s"
                 % (i, typ, cf, DAY, notes.NOW[:10], notes.NOW[:10], h if ev else "none", rc, t)
                 for i, (typ, cf, ev, rc, t) in enumerate(claims, 1)]
        front = dict(notes.COMMON, id="wwi:process:%s" % slug, subject="wwi/across/processes/%s" % slug, item="24", topic="processes",
                     tier="best-effort", summary=note["summary"], confidence=conf, claims=str(len(claims)), method=method,
                     input_schema_sha256=schema_hash(tables), recheck_when="every new extract, or a schema change of the tables followed")
        txt = ("---\n" + "\n".join("%s: %s" % (k, front[k]) for k in ia.FRONT_KEYS) + "\n---\n\n## Claims\n\n" + "\n".join(lines) +
               "\n\n## Reasoning\n\n" + note["reasoning"] + "\n\n## Uncertainties\n\n" + (note.get("uncertainties") or "None.") +
               "\n\n## For a person\n\nNone.\n")
        assert all(ord(ch) < 128 for ch in txt), slug
        with open(os.path.join(OUT, slug, "24_processes.md"), "w", encoding="ascii", newline="\n") as f:
            f.write(txt)


if __name__ == "__main__":
    main(sys.argv)
