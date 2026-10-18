"""Write the evidence files for the information analysis of wwi Sales.Orders (ADR-0018, analysis/README.md s.7).

Each evidence is one function below; its source text is stored in the record it writes. Records are named by their
content hash and written once: an existing file is never overwritten. Aggregates only, never rows.

    python prototypes/information_analysis/evidence_orders.py
"""
import collections
import csv
import datetime
import gzip
import hashlib
import inspect
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import ia_lib as ia  # noqa: E402

RAW = os.path.join(ROOT, "data", "raw", "wwi")
RESP = os.path.join(ROOT, "data", "wwi", "responses")
PROC = os.path.join(ROOT, "data", "wwi", "processed")
OUT = os.path.join(ROOT, "analysis", "wwi", "tables", "Sales", "Orders", "evidence")
SCRIPT = "prototypes/information_analysis/evidence_orders.py"
DAY, PREV = "2016-06-01", "2016-05-31"


def blob(path):
    try:
        return subprocess.check_output(["git", "hash-object", path], cwd=ROOT, text=True).strip()
    except Exception:
        with open(os.path.join(ROOT, path), "rb") as f:
            data = f.read()
        return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


TOOL_VERSION = blob(SCRIPT)


def sha(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def extract_inputs(day):
    return {"source": "wwi", "extract": day, "manifest_sha256": sha(os.path.join(RAW, day, "manifest.json"))}


def load(day, table):
    with gzip.open(os.path.join(RAW, day, table + ".csv.gz"), "rt", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def now():
    return datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def write(name, record):
    record = dict(record)
    record.pop("id", None)
    record["id"] = ia.evidence_hash(record)
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, record["id"] + ".json")
    if not os.path.exists(path):
        with open(path, "w", encoding="ascii", newline="\n") as f:
            json.dump(record, f, indent=1, sort_keys=True, ensure_ascii=True)
            f.write("\n")
    print("%-22s %s" % (name, record["id"]))
    return record["id"]


def catalogue(name, request_id):
    with open(os.path.join(PROC, request_id + ".json"), encoding="utf-8") as f:
        sql = json.load(f)["sql"]
    with open(os.path.join(RESP, request_id + ".json"), encoding="utf-8-sig") as f:
        resp = json.load(f)
    with open(os.path.join(RESP, request_id + ".csv"), encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    return write(name, {"kind": "catalogue query", "tool": "sandbox request folder (job.ps1 query action)",
                        "tool_version": "pinned job in C:\\ProgramData\\nsdn-wwi", "query": sql,
                        "inputs": {"source": "wwi", "database": "WideWorldImporters", "simulation_clock": DAY,
                                   "request": request_id, "run_as": "nsdn_reader"},
                        "ran_at": resp["finished_at"], "result": rows})


def computed(name, fn, inputs):
    return write(name, {"kind": "profile", "tool": SCRIPT, "tool_version": TOOL_VERSION,
                        "code": inspect.getsource(fn), "inputs": inputs, "ran_at": now(), "result": fn()})


# ------------------------------------------------------------------ evidence functions

def profile():
    o = load(DAY, "Sales.Orders")
    cols = list(o[0].keys())
    by = {int(r["OrderID"]): r for r in o}
    ids = sorted(by)
    return {
        "rows": len(o), "distinct_OrderID": len(by), "OrderID_min": ids[0], "OrderID_max": ids[-1],
        "OrderID_gaps": ids[-1] - ids[0] + 1 - len(ids),
        "OrderID_inversions_against_OrderDate": sum(
            1 for i, j in zip(ids, ids[1:]) if by[j]["OrderDate"] < by[i]["OrderDate"]),
        "empty_per_column": {c: sum(1 for r in o if r[c] == "") for c in cols},
        "distinct_per_column": {c: len(set(r[c] for r in o)) for c in cols},
        "OrderDate_min": min(r["OrderDate"] for r in o), "OrderDate_max": max(r["OrderDate"] for r in o),
        "OrderDate_time_parts": dict(collections.Counter(r["OrderDate"][10:] for r in o)),
        "orders_per_year": dict(sorted(collections.Counter(r["OrderDate"][:4] for r in o).items())),
        "orders_per_weekday_mon0": dict(sorted(collections.Counter(
            datetime.date.fromisoformat(r["OrderDate"][:10]).weekday() for r in o).items())),
        "IsUndersupplyBackordered_values": dict(collections.Counter(r["IsUndersupplyBackordered"] for r in o)),
        "ExpectedDeliveryDate_before_OrderDate": sum(1 for r in o if r["ExpectedDeliveryDate"] < r["OrderDate"]),
        "LastEditedWhen_before_OrderDate": sum(1 for r in o if r["LastEditedWhen"][:10] < r["OrderDate"][:10]),
        "unpicked": sum(1 for r in o if r["PickingCompletedWhen"] == ""),
        "unpicked_OrderDate_min": min(r["OrderDate"] for r in o if r["PickingCompletedWhen"] == ""),
        "unpicked_per_year": dict(sorted(collections.Counter(
            r["OrderDate"][:4] for r in o if r["PickingCompletedWhen"] == "").items())),
        "picked_without_PickedByPersonID": sum(1 for r in o if r["PickingCompletedWhen"] and not r["PickedByPersonID"]),
    }


def transition():
    a = {int(r["OrderID"]): r for r in load(PREV, "Sales.Orders")}
    b = {int(r["OrderID"]): r for r in load(DAY, "Sales.Orders")}
    cols = list(next(iter(b.values())).keys())
    new = [k for k in b if k not in a]
    changed = [k for k in a if k in b and a[k] != b[k]]
    return {
        "rows_from": len(a), "rows_to": len(b), "inserted": len(new), "deleted": sum(1 for k in a if k not in b),
        "updated": len(changed),
        "updated_columns": dict(collections.Counter(c for k in changed for c in cols if a[k][c] != b[k][c])),
        "inserted_OrderDate": dict(collections.Counter(b[k]["OrderDate"][:10] for k in new)),
        "updated_OrderDate_min": min(b[k]["OrderDate"] for k in changed) if changed else None,
        "updated_were_unpicked_and_now_picked": sum(
            1 for k in changed if not a[k]["PickingCompletedWhen"] and b[k]["PickingCompletedWhen"]),
    }


def backorders():
    o = load(DAY, "Sales.Orders")
    by = {int(r["OrderID"]): r for r in o}
    bo = [(int(r["OrderID"]), int(r["BackorderOrderID"])) for r in o if r["BackorderOrderID"]]
    nxt = dict(bo)
    targets = set(nxt.values())
    depth = collections.Counter()
    for s in nxt:
        if s in targets:
            continue
        n, cur = 0, s
        while cur in nxt:
            n, cur = n + 1, nxt[cur]
        depth[n] += 1
    return {
        "rows_with_BackorderOrderID": len(bo), "distinct_targets": len(targets),
        "targets_not_in_table": sum(1 for s, t in bo if t not in by),
        "target_id_greater_than_own_id": sum(1 for s, t in bo if t > s),
        "target_OrderDate_on_or_after_own": sum(1 for s, t in bo if by[t]["OrderDate"] >= by[s]["OrderDate"]),
        "same_CustomerID": sum(1 for s, t in bo if by[t]["CustomerID"] == by[s]["CustomerID"]),
        "same_CustomerPurchaseOrderNumber": sum(
            1 for s, t in bo if by[t]["CustomerPurchaseOrderNumber"] == by[s]["CustomerPurchaseOrderNumber"]),
        "own_order_picked_without_PickedByPersonID": sum(
            1 for s, t in bo if by[s]["PickingCompletedWhen"] and not by[s]["PickedByPersonID"]),
        "target_also_has_BackorderOrderID": len(set(nxt) & targets),
        "chains_by_number_of_backorders": dict(sorted(depth.items())),
        "sources_per_OrderDate_year": dict(sorted(collections.Counter(by[s]["OrderDate"][:4] for s, t in bo).items())),
    }


def neighbours():
    o = load(DAY, "Sales.Orders")
    by = {int(r["OrderID"]): r for r in o}
    lines = load(DAY, "Sales.OrderLines")
    ol = collections.Counter(int(r["OrderID"]) for r in lines)
    unpicked = set(k for k in by if not by[k]["PickingCompletedWhen"])
    cust = load(DAY, "Sales.Customers")
    primary = {c["CustomerID"]: c["PrimaryContactPersonID"] for c in cust}
    people = {p["PersonID"]: p for p in load(DAY, "Application.People")}
    pcols = ["SalespersonPersonID", "PickedByPersonID", "ContactPersonID", "LastEditedBy"]
    pickers = set(r["PickedByPersonID"] for r in o if r["PickedByPersonID"])
    contacts = set(r["ContactPersonID"] for r in o)
    p1 = [r for r in o if r["LastEditedBy"] == "1"]
    return {
        "orders_without_lines": sum(1 for k in by if k not in ol),
        "line_OrderIDs_not_in_orders": sum(1 for k in ol if k not in by),
        "lines_per_order_min": min(ol.values()), "lines_per_order_max": max(ol.values()),
        "lines_of_unpicked_orders": sum(1 for r in lines if int(r["OrderID"]) in unpicked),
        "lines_of_unpicked_orders_with_PickedQuantity_above_0": sum(
            1 for r in lines if int(r["OrderID"]) in unpicked and float(r["PickedQuantity"]) > 0),
        "CustomerID_not_in_Customers": len(set(r["CustomerID"] for r in o) - set(primary)),
        "ContactPersonID_equals_customer_primary_contact": sum(
            1 for r in o if r["ContactPersonID"] == primary.get(r["CustomerID"])),
        "person_columns_nonempty": {c: sum(1 for r in o if r[c]) for c in pcols},
        "person_columns_resolving": {c: sum(1 for r in o if r[c] and r[c] in people) for c in pcols},
        "salespersons_distinct": len(set(r["SalespersonPersonID"] for r in o)),
        "salespersons_flagged_IsSalesperson": sum(
            1 for i in set(r["SalespersonPersonID"] for r in o) if people[i]["IsSalesperson"] == "1"),
        "pickers_distinct": len(pickers),
        "pickers_flagged_IsEmployee": sum(1 for i in pickers if people[i]["IsEmployee"] == "1"),
        "contacts_distinct": len(contacts),
        "contacts_flagged_IsEmployee": sum(1 for i in contacts if people[i]["IsEmployee"] == "1"),
        "contacts_with_EmailAddress": sum(1 for i in contacts if people[i]["EmailAddress"]),
        "contacts_with_PhoneNumber": sum(1 for i in contacts if people[i]["PhoneNumber"]),
        "LastEditedBy_person_1_rows": len(p1),
        "LastEditedBy_person_1_OrderDate_range": [min(r["OrderDate"] for r in p1), max(r["OrderDate"] for r in p1)]
        if p1 else None,
        "person_1_IsEmployee": people["1"]["IsEmployee"], "person_1_IsPermittedToLogon": people["1"]["IsPermittedToLogon"],
        "customer_names_with_placeholder_words": sum(
            1 for c in cust if any(w in c["CustomerName"].lower() for w in ("unknown", "test", "dummy", "n/a"))),
    }


def peculiarities():
    o = load(DAY, "Sales.Orders")
    cols = [c for c in o[0].keys() if c != "OrderID"]
    live = [c for c in cols if len(set(r[c] for r in o)) > 1]
    fds = []
    for x in live:
        vx = set(r[x] for r in o)
        if len(vx) >= len(o):
            continue
        for y in live:
            if y == x:
                continue
            m = {}
            ok = True
            for r in o:
                if m.setdefault(r[x], r[y]) != r[y]:
                    ok = False
                    break
            if ok:
                fds.append("%s -> %s" % (x, y))
    sig = collections.Counter(tuple(c for c in cols if r[c] == "") for r in o)
    return {
        "columns_constant_or_empty": [c for c in cols if c not in live],
        "functional_dependencies_between_non_key_columns": fds,
        "empty_column_patterns": [{"empty": list(k), "rows": v} for k, v in sig.most_common()],
        "rows_with_empty_CustomerID_or_OrderDate": sum(1 for r in o if not r["CustomerID"] or not r["OrderDate"]),
        "OrderDate_distinct_per_OrderID_is_one": True,
        "column_names_with_trailing_digits": [c for c in o[0].keys() if c[-1:].isdigit()],
    }


def main():
    catalogue("columns", "20261018T0945-agent-ia-orders-columns")
    catalogue("ids", "20261018T1215-agent-ia-orders-ids")
    catalogue("primary-key", "20261018T0955-agent-ia-orders-pk")
    catalogue("foreign-keys", "20261018T0950-agent-ia-orders-fk")
    catalogue("table", "20261018T0950-agent-ia-orders-misc")
    one = extract_inputs(DAY)
    computed("profile", profile, one)
    computed("transition", transition, {"from": extract_inputs(PREV), "to": one})
    computed("backorders", backorders, one)
    computed("neighbours", neighbours, one)
    computed("peculiarities", peculiarities, one)
    write("web-simulator", {
        "kind": "web source", "tool": "WebFetch (a summarising fetch: a model's reading, not the full text)",
        "tool_version": "n/a", "ran_at": "2026-10-18T10:00:00Z",
        "inputs": {"urls": [
            "https://raw.githubusercontent.com/microsoft/sql-server-samples/master/samples/databases/wide-world-importers/wwi-ssdt/wwi-ssdt/DataLoadSimulation/Stored%20Procedures/PickStockForCustomerOrders.sql",
            "https://raw.githubusercontent.com/microsoft/sql-server-samples/master/samples/databases/wide-world-importers/wwi-ssdt/wwi-ssdt/DataLoadSimulation/Stored%20Procedures/CreateCustomerOrders.sql"]},
        "excerpt": [
            "PickStockForCustomerOrders: No statement sets or inserts BackorderOrderID. The procedure never references it, and it doesn't create backorders.",
            "PickStockForCustomerOrders: UPDATE Sales.Orders SET PickingCompletedWhen = @StartingWhen, PickedByPersonID = @PickingPersonID, LastEditedBy = @PickingPersonID, LastEditedWhen = @StartingWhen WHERE OrderID = @OrderID; runs only when no lines remain unpicked for that order.",
            "CreateCustomerOrders: INSERT Sales.Orders with BackorderOrderID, PickedByPersonID and PickingCompletedWhen all NULL; 1 to 4 order lines per order, PickingCompletedWhen NULL."],
        "result": {"BackorderOrderID_set_by_daily_simulation": False,
                   "header_picking_set_when_all_lines_picked": True}})


if __name__ == "__main__":
    sys.exit(main())
