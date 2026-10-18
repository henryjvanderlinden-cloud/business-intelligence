"""Write the evidence files for the information analysis of wwi Sales.Orders (minimum items).

Aggregates only. See README.md in this folder.
"""
import collections, csv, datetime, gzip, hashlib, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RAW = os.path.join(ROOT, "data", "raw", "wwi")
RESP = os.path.join(ROOT, "data", "wwi", "responses")
REQ = os.path.join(ROOT, "data", "wwi", "processed")
OUT = os.path.join(ROOT, "analysis", "wwi", "tables", "Sales.Orders", "evidence")
CODE = "prototypes/information_analysis/evidence_orders.py"
NOW = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()


def sha(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def as_of(day):
    return {"source": "wwi", "extract": day, "manifest_sha256": sha(os.path.join(RAW, day, "manifest.json"))}


def load(day, table):
    with gzip.open(os.path.join(RAW, day, table + ".csv.gz"), "rt", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def write(eid, slug, record):
    os.makedirs(OUT, exist_ok=True)
    record = dict({"id": eid, "written_at": NOW}, **record)
    with open(os.path.join(OUT, "%s_%s.json" % (eid, slug)), "w", encoding="utf-8", newline="\n") as f:
        json.dump(record, f, indent=1, ensure_ascii=True)
        f.write("\n")


def catalogue(eid, slug, request_id):
    with open(os.path.join(REQ, request_id + ".json"), encoding="utf-8") as f:
        sql = json.load(f)["sql"]
    with open(os.path.join(RESP, request_id + ".csv"), encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    write(eid, slug, {"kind": "catalogue query", "tool": "sandbox request folder, query as nsdn_reader",
                      "request": request_id, "query": sql, "result": rows,
                      "as_of": {"source": "wwi", "database": "WideWorldImporters, live, 2026-10-18"}})


def main():
    day, prev = "2016-06-01", "2016-05-31"
    catalogue("E001", "columns", "20261018T0945-agent-ia-orders-columns")
    catalogue("E002", "primary-key", "20261018T0955-agent-ia-orders-pk")
    catalogue("E003", "foreign-keys", "20261018T0950-agent-ia-orders-fk")
    catalogue("E004", "table", "20261018T0950-agent-ia-orders-misc")

    o = load(day, "Sales.Orders")
    cols = list(o[0].keys())
    by = {int(r["OrderID"]): r for r in o}
    ids = sorted(by)
    profile = {
        "rows": len(o),
        "distinct_OrderID": len(by),
        "OrderID_min": ids[0], "OrderID_max": ids[-1],
        "OrderID_gaps": ids[-1] - ids[0] + 1 - len(ids),
        "empty_per_column": {c: sum(1 for r in o if r[c] == "") for c in cols},
        "distinct_per_column": {c: len(set(r[c] for r in o)) for c in cols},
        "OrderDate_min": min(r["OrderDate"] for r in o), "OrderDate_max": max(r["OrderDate"] for r in o),
        "OrderDate_time_parts": dict(collections.Counter(r["OrderDate"][10:] for r in o)),
        "orders_per_year": dict(sorted(collections.Counter(r["OrderDate"][:4] for r in o).items())),
        "orders_per_weekday_mon0": dict(sorted(collections.Counter(
            datetime.date.fromisoformat(r["OrderDate"][:10]).weekday() for r in o).items())),
        "IsUndersupplyBackordered_values": dict(collections.Counter(r["IsUndersupplyBackordered"] for r in o)),
        "OrderID_inversions_against_OrderDate": sum(
            1 for i, j in zip(ids, ids[1:]) if by[j]["OrderDate"] < by[i]["OrderDate"]),
        "ExpectedDeliveryDate_before_OrderDate": sum(1 for r in o if r["ExpectedDeliveryDate"] < r["OrderDate"]),
        "LastEditedWhen_before_OrderDate": sum(1 for r in o if r["LastEditedWhen"][:10] < r["OrderDate"][:10]),
        "unpicked": sum(1 for r in o if r["PickingCompletedWhen"] == ""),
        "unpicked_with_picker": sum(1 for r in o if r["PickingCompletedWhen"] == "" and r["PickedByPersonID"]),
        "picked_without_picker": sum(1 for r in o if r["PickingCompletedWhen"] and not r["PickedByPersonID"]),
        "unpicked_OrderDate_min": min(r["OrderDate"] for r in o if r["PickingCompletedWhen"] == ""),
        "unpicked_per_year": dict(sorted(collections.Counter(
            r["OrderDate"][:4] for r in o if r["PickingCompletedWhen"] == "").items())),
    }
    write("E005", "profile", {"kind": "profile", "tool": CODE, "as_of": as_of(day), "result": profile})

    a = {int(r["OrderID"]): r for r in load(prev, "Sales.Orders")}
    new = [k for k in by if k not in a]
    gone = [k for k in a if k not in by]
    changed = [k for k in a if k in by and a[k] != by[k]]
    write("E006", "transition", {"kind": "comparison of two extracts", "tool": CODE,
                                 "as_of": {"from": as_of(prev), "to": as_of(day)}, "result": {
        "rows_from": len(a), "rows_to": len(by), "inserted": len(new), "deleted": len(gone),
        "updated": len(changed),
        "updated_columns": dict(collections.Counter(c for k in changed for c in cols if a[k][c] != by[k][c])),
        "inserted_OrderDate": dict(collections.Counter(by[k]["OrderDate"][:10] for k in new)),
        "updated_OrderDate_min": min(by[k]["OrderDate"] for k in changed) if changed else None,
        "updated_kind": dict(collections.Counter(
            "picked" if not a[k]["PickingCompletedWhen"] and by[k]["PickingCompletedWhen"] else "other"
            for k in changed)),
    }})

    bo = [(int(r["OrderID"]), int(r["BackorderOrderID"])) for r in o if r["BackorderOrderID"]]
    src = set(s for s, t in bo)
    tgt = set(t for s, t in bo)
    write("E007", "backorder-direction", {"kind": "profile", "tool": CODE, "as_of": as_of(day), "result": {
        "rows_with_BackorderOrderID": len(bo),
        "distinct_targets": len(tgt),
        "targets_not_in_table": sum(1 for s, t in bo if t not in by),
        "target_id_greater_than_own_id": sum(1 for s, t in bo if t > s),
        "target_OrderDate_on_or_after_own": sum(1 for s, t in bo if by[t]["OrderDate"] >= by[s]["OrderDate"]),
        "same_CustomerID": sum(1 for s, t in bo if by[t]["CustomerID"] == by[s]["CustomerID"]),
        "same_CustomerPurchaseOrderNumber": sum(
            1 for s, t in bo if by[t]["CustomerPurchaseOrderNumber"] == by[s]["CustomerPurchaseOrderNumber"]),
        "own_order_picked": sum(1 for s, t in bo if by[s]["PickingCompletedWhen"]),
        "own_order_picked_without_PickedByPersonID": sum(
            1 for s, t in bo if by[s]["PickingCompletedWhen"] and not by[s]["PickedByPersonID"]),
        "all_picked_without_PickedByPersonID": sum(
            1 for r in o if r["PickingCompletedWhen"] and not r["PickedByPersonID"]),
        "target_also_has_BackorderOrderID": len(src & tgt),
    }})

    lines = load(day, "Sales.OrderLines")
    ol = collections.Counter(int(r["OrderID"]) for r in lines)
    unpicked = set(k for k in by if not by[k]["PickingCompletedWhen"])
    cust = load(day, "Sales.Customers")
    primary = {c["CustomerID"]: c["PrimaryContactPersonID"] for c in cust}
    people = {p["PersonID"]: p for p in load(day, "Application.People")}
    person_cols = ["SalespersonPersonID", "PickedByPersonID", "ContactPersonID", "LastEditedBy"]
    write("E008", "neighbours", {"kind": "profile", "tool": CODE, "as_of": as_of(day), "result": {
        "orders_without_lines": sum(1 for k in by if k not in ol),
        "line_OrderIDs_not_in_orders": sum(1 for k in ol if k not in by),
        "lines_per_order_min": min(ol.values()), "lines_per_order_max": max(ol.values()),
        "lines_of_unpicked_orders": sum(1 for l in lines if int(l["OrderID"]) in unpicked),
        "lines_of_unpicked_orders_with_PickedQuantity_above_0": sum(
            1 for l in lines if int(l["OrderID"]) in unpicked and float(l["PickedQuantity"]) > 0),
        "CustomerID_not_in_Customers": len(set(r["CustomerID"] for r in o) - set(primary)),
        "ContactPersonID_equals_customer_primary_contact": sum(
            1 for r in o if r["ContactPersonID"] == primary.get(r["CustomerID"])),
        "person_columns_resolving_to_People": {c: sum(1 for r in o if r[c] and r[c] in people) for c in person_cols},
        "person_columns_nonempty": {c: sum(1 for r in o if r[c]) for c in person_cols},
        "LastEditedBy_is_person_1": sum(1 for r in o if r["LastEditedBy"] == "1"),
        "person_1_IsEmployee": people["1"]["IsEmployee"], "person_1_IsPermittedToLogon": people["1"]["IsPermittedToLogon"],
        "salespersons_flagged_IsSalesperson": sum(
            1 for i in set(r["SalespersonPersonID"] for r in o) if people[i]["IsSalesperson"] == "1"),
        "salespersons_distinct": len(set(r["SalespersonPersonID"] for r in o)),
        "contacts_flagged_IsEmployee": sum(
            1 for i in set(r["ContactPersonID"] for r in o) if people[i]["IsEmployee"] == "1"),
        "contacts_distinct": len(set(r["ContactPersonID"] for r in o)),
        "pickers_distinct": len(set(r["PickedByPersonID"] for r in o if r["PickedByPersonID"])),
        "pickers_flagged_IsEmployee": sum(
            1 for i in set(r["PickedByPersonID"] for r in o if r["PickedByPersonID"]) if people[i]["IsEmployee"] == "1"),
        "customer_names_with_placeholder_words": sum(
            1 for c in cust if any(w in c["CustomerName"].lower() for w in ("unknown", "test", "dummy", "n/a"))),
        "contacts_with_EmailAddress": sum(
            1 for i in set(r["ContactPersonID"] for r in o) if people[i]["EmailAddress"]),
        "contacts_with_PhoneNumber": sum(
            1 for i in set(r["ContactPersonID"] for r in o) if people[i]["PhoneNumber"]),
    }})
    print("wrote", sorted(os.listdir(OUT)))


if __name__ == "__main__":
    sys.exit(main())
