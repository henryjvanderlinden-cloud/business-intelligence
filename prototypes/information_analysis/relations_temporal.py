"""Round 2, item 03 per relation (analysis/README.md section 9): does the relation hold as of a time?

For every relation folder that relations.py wrote, one more evidence file: the child row's date (its business date,
the header's date for document lines, otherwise its ValidFrom or LastEditedWhen), and
  - for a system-versioned parent, which version of the parent row was current at the end of that date: none yet,
    the current one, or an earlier one; and, for an earlier one, which attributes differ from the current version;
  - for a parent with a business date of its own, the order of the two dates and the days between them.
Counts only.

    python prototypes/information_analysis/relations_temporal.py
"""
import bisect
import collections
import csv
import datetime
import gzip
import inspect
import json
import os
import statistics
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from evidence_orders import blob, sha, now  # noqa: E402
from relations import write_evidence, load_catalogues  # noqa: E402
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import ia_lib as ia  # noqa: E402

SCRIPT = "prototypes/information_analysis/relations_temporal.py"
RAW = os.path.join(ROOT, "data", "raw", "wwi")
DAY = "2016-06-01"
REL_DIR = os.path.join(ROOT, "analysis", "wwi", "across", "relations")
csv.field_size_limit(1 << 30)
# business dates of event tables (round 1's date columns)
DATE_COLS = {"Sales.Orders": "OrderDate", "Sales.Invoices": "InvoiceDate", "Sales.CustomerTransactions": "TransactionDate",
             "Purchasing.SupplierTransactions": "TransactionDate", "Warehouse.StockItemTransactions": "TransactionOccurredWhen",
             "Purchasing.PurchaseOrders": "OrderDate", "Sales.SpecialDeals": "StartDate"}
# document lines take the header's date: (line column, header table, header key)
HEADER_DATE = {"Sales.InvoiceLines": ("InvoiceID", "Sales.Invoices", "InvoiceID"),
               "Sales.OrderLines": ("OrderID", "Sales.Orders", "OrderID"),
               "Purchasing.PurchaseOrderLines": ("PurchaseOrderID", "Purchasing.PurchaseOrders", "PurchaseOrderID")}
PERIOD = {"ValidFrom", "ValidTo", "LastEditedBy", "LastEditedWhen"}
_cache = {}


def table(name):
    if name not in _cache:
        with gzip.open(os.path.join(RAW, DAY, name + ".csv.gz"), "rt", encoding="utf-8", newline="") as f:
            r = csv.reader(f)
            head = next(r)
            _cache[name] = (head, list(r))
    return _cache[name]


def col(name, c):
    head, rows = table(name)
    i = head.index(c)
    return [r[i] for r in rows]


def child_dates(child):
    """The date each child row is about, and the name of the column it comes from."""
    head, _ = table(child)
    if child in DATE_COLS:
        return col(child, DATE_COLS[child]), DATE_COLS[child]
    if child in HEADER_DATE:
        lc, ht, hk = HEADER_DATE[child]
        d = dict(zip(col(ht, hk), col(ht, DATE_COLS[ht])))
        return [d.get(v, "") for v in col(child, lc)], "%s.%s via %s" % (ht, DATE_COLS[ht], lc)
    for c in ("ValidFrom", "LastEditedWhen"):
        if c in head:
            return col(child, c), c
    return None, None


def end_of_day(d):
    return d if "T" in d else d + "T23:59:59.9999999"


def versions(parent, pcol):
    """Per parent key, its versions sorted by ValidFrom: (ValidFrom, attributes), current version last."""
    head, rows = table(parent)
    hhead, hrows = table(parent + "_Archive")
    attrs = [c for c in head if c not in PERIOD]
    out = collections.defaultdict(list)
    for h, rs, cur in ((hhead, hrows, False), (head, rows, True)):
        ix = {c: h.index(c) for c in h}
        for r in rs:
            out[r[ix[pcol]]].append((r[ix["ValidFrom"]], r[ix["ValidTo"]], tuple(r[ix[c]] for c in attrs), cur))
    for k in out:
        out[k].sort()
    return out, attrs


def as_of(child, ccol, parent, pcol, cats):
    """Which version of the parent was current at the end of the child row's date: the last version with
    ValidFrom <= t, provided t < its ValidTo; otherwise the date falls in a gap between versions."""
    dates, source = child_dates(child)
    keys = col(child, ccol)
    vs, attrs = versions(parent, pcol)
    res = collections.Counter()
    differ = collections.Counter()
    for k, d in zip(keys, dates):
        if not k or not d:
            res["no key or no date"] += 1
            continue
        t = end_of_day(d)
        v = vs.get(k, [])
        froms = [x[0] for x in v]
        i = bisect.bisect_right(froms, t) - 1
        if i < 0:
            res["no version yet at the child's date"] += 1
            continue
        if t >= v[i][1]:
            res["no version current at the child's date (a gap between versions)"] += 1
            continue
        if v[i][3]:
            res["the current version"] += 1
            continue
        res["an earlier version"] += 1
        cur = v[-1][2]
        diff = [a for a, x, y in zip(attrs, v[i][2], cur) if x != y]
        if diff:
            res["an earlier version whose attributes differ from the current"] += 1
            for a in diff:
                differ[a] += 1
        else:
            res["an earlier version with the same attributes"] += 1
    return {"child_date_column": source, "parent_version_at_end_of_child_date": dict(res),
            "attributes_that_differ_rows": dict(differ.most_common())}


def date_order(child, ccol, parent, pcol):
    """The child row's date against the parent row's own business date."""
    dates, source = child_dates(child)
    pd = dict(zip(col(parent, pcol), col(parent, DATE_COLS[parent])))
    order, lag = collections.Counter(), []
    for k, d in zip(col(child, ccol), dates):
        if not k or not d or k not in pd or not pd[k]:
            continue
        a, b = d[:10], pd[k][:10]
        order["child date " + ("before" if a < b else "same day as" if a == b else "after") + " parent date"] += 1
        lag.append((datetime.date.fromisoformat(a) - datetime.date.fromisoformat(b)).days)
    if not lag:
        return {"child_date_column": source, "parent_date_column": DATE_COLS[parent], "rows": 0}
    lag.sort()
    return {"child_date_column": source, "parent_date_column": DATE_COLS[parent], "rows": len(lag), "order": dict(order),
            "days_child_minus_parent": {"min": lag[0], "median": statistics.median(lag), "max": lag[-1],
                                        "most_common": collections.Counter(lag).most_common(5)}}


def order_dates_by_backorder(child, ccol):
    """For a relation to Sales.Orders: the child's date against the order date, split by whether the order is a
    backorder (named by another order's BackorderOrderID)."""
    targets = {v for v in col("Sales.Orders", "BackorderOrderID") if v}
    od = dict(zip(col("Sales.Orders", "OrderID"), col("Sales.Orders", "OrderDate")))
    dates, _ = child_dates(child)
    c = collections.Counter()
    for k, d in zip(col(child, ccol), dates):
        if k and d and k in od:
            c["%s|%s" % ("backorder" if k in targets else "not a backorder",
                         "child date after order date" if d[:10] > od[k][:10] else "same day or before")] += 1
    return dict(sorted(c.items()))


def main():
    cats = load_catalogues()
    base = {"kind": "profile", "tool": SCRIPT, "tool_version": blob(SCRIPT), "ran_at": now()}
    inp = {"source": "wwi", "extract": DAY, "manifest_sha256": sha(os.path.join(RAW, DAY, "manifest.json"))}
    code = "\n".join(inspect.getsource(f) for f in (child_dates, end_of_day, versions, as_of, date_order, order_dates_by_backorder))
    for name in sorted(os.listdir(REL_DIR)):
        sides = ia.parse_relation(name)
        (cs, ct, ccols), (ps, pt, pcols) = sides
        if len(ccols) != 1:
            continue
        child, parent, ccol, pcol = "%s.%s" % (cs, ct), "%s.%s" % (ps, pt), ccols[0], pcols[0]
        res = {"parent_temporal_type": cats[parent]["catalogue"]["table"][0]["temporal_type_desc"]}
        dates, source = child_dates(child)
        res["child_date_column"] = source
        if dates is None:
            res["note"] = "the child has no date column"
        else:
            if res["parent_temporal_type"] == "SYSTEM_VERSIONED_TEMPORAL_TABLE":
                res["as_of"] = as_of(child, ccol, parent, pcol, cats)
            if parent in DATE_COLS and parent != child:
                res["date_order"] = date_order(child, ccol, parent, pcol)
            elif parent in DATE_COLS and parent == child:
                res["date_order"] = date_order(child, ccol, parent, pcol)
            if parent == "Sales.Orders" and child != parent:
                res["date_order_by_backorder"] = order_dates_by_backorder(child, ccol)
        h = write_evidence(os.path.join(REL_DIR, name, "evidence"),
                           dict(base, code=code, inputs=dict(inp, child=child, child_column=ccol, parent=parent, parent_column=pcol), result=res))
        print(name, h, json.dumps(res)[:300])


if __name__ == "__main__":
    main()
