"""Recheck the analysis against a newer extract (item 22, stability; analysis/README.md sections 5 and 6).

Runs the measuring functions of the analysis scripts - transitions, candidate keys, relations, reconciliations,
processes, point in time - once on the extract the record was written on (BASE) and once on the newer one (NEW), each
in a fresh interpreter with IA_DAY and IA_PREV set, plus follow-ups on what the earlier extract left open. Writes one
evidence file per group into analysis/wwi/_source/evidence/ holding both results; counts only.

    python prototypes/information_analysis/recheck.py <base day> <base prev> <new day> <new prev>
"""
import inspect
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from evidence_orders import blob, sha, now  # noqa: E402
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import ia_lib as ia  # noqa: E402

SCRIPT = "prototypes/information_analysis/recheck.py"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "analysis", "wwi", "_source", "evidence")
RAW = os.path.join(ROOT, "data", "raw", "wwi")

# Each probe runs in its own interpreter so that the scripts' module constants (DAY, PREV) take the extract's date.
PROBES = {
    "transitions": '''
import json, os, glob
import profile_tables as pt
out = {}
for f in sorted(glob.glob(os.path.join(pt.ROOT, "scratch", "ia_profile", "*.json"))):
    d = json.load(open(f))
    pk = [k["column_name"] for k in d["catalogue"]["keys"] if k["is_primary_key"] == "1"]
    t = os.path.basename(f)[:-5]
    if pk and d["catalogue"]["table"][0]["temporal_type_desc"] != "HISTORY_TABLE":
        out[t] = pt.transition(t, pk)
print(json.dumps(out))
''',
    "candidate_keys": '''
import json
import evidence_shared as es
print(json.dumps({t: [es.candidate_key(t, c) for c in cs] for t, cs in es.CANDIDATE_KEYS.items()}))
''',
    "relations": '''
import json
import relations as r
cats = r.load_catalogues()
out = {}
for t, d in cats.items():
    for k in d["catalogue"]["foreign_keys_out"]:
        child, parent = "%s.%s" % (k["schema_name"], k["table_name"]), "%s.%s" % (k["ref_schema"], k["ref_table"])
        p = r.relation_profile(child, k["column_name"], parent, k["ref_column"], cats[parent])
        out["%s.%s" % (child, k["column_name"])] = {x: p[x] for x in ("child_rows", "child_empty", "orphan_rows", "parents_unreferenced")} | {
            "max_children": p["children_per_referenced_parent"].get("max")}
for child, cc, parent, pc in r.COMPOSITE:
    p = r.composite_profile(child, cc, parent, pc)
    out["%s.%s" % (child, "+".join(cc))] = {x: p[x] for x in ("child_rows", "child_empty", "orphan_rows", "parents_unreferenced", "parent_combination_unique")} | {
        "max_children": p["children_per_referenced_parent"].get("max")}
routes = {
 "Sales.CustomerTransactions.CustomerID = Invoices.BillToCustomerID": ("Sales.CustomerTransactions", "CustomerID", "InvoiceID", "Sales.Invoices", "InvoiceID", "BillToCustomerID"),
 "Sales.CustomerTransactions.CustomerID = Invoices.CustomerID": ("Sales.CustomerTransactions", "CustomerID", "InvoiceID", "Sales.Invoices", "InvoiceID", "CustomerID"),
 "Warehouse.StockItemTransactions.CustomerID = Invoices.CustomerID": ("Warehouse.StockItemTransactions", "CustomerID", "InvoiceID", "Sales.Invoices", "InvoiceID", "CustomerID"),
 "Sales.Invoices.CustomerID = Orders.CustomerID": ("Sales.Invoices", "CustomerID", "OrderID", "Sales.Orders", "OrderID", "CustomerID"),
 "Sales.Invoices.BillToCustomerID = Customers.BillToCustomerID": ("Sales.Invoices", "BillToCustomerID", "CustomerID", "Sales.Customers", "CustomerID", "BillToCustomerID"),
 "Sales.Invoices.SalespersonPersonID = Orders.SalespersonPersonID": ("Sales.Invoices", "SalespersonPersonID", "OrderID", "Sales.Orders", "OrderID", "SalespersonPersonID"),
 "Sales.InvoiceLines.PackageTypeID = StockItems.UnitPackageID": ("Sales.InvoiceLines", "PackageTypeID", "StockItemID", "Warehouse.StockItems", "StockItemID", "UnitPackageID"),
 "Purchasing.PurchaseOrderLines.PackageTypeID = StockItems.OuterPackageID": ("Purchasing.PurchaseOrderLines", "PackageTypeID", "StockItemID", "Warehouse.StockItems", "StockItemID", "OuterPackageID"),
 "Purchasing.PurchaseOrders.ContactPersonID = Suppliers.PrimaryContactPersonID": ("Purchasing.PurchaseOrders", "ContactPersonID", "SupplierID", "Purchasing.Suppliers", "SupplierID", "PrimaryContactPersonID"),
 "Warehouse.StockItemTransactions.SupplierID = StockItems.SupplierID": ("Warehouse.StockItemTransactions", "SupplierID", "StockItemID", "Warehouse.StockItems", "StockItemID", "SupplierID"),
}
out["two_routes"] = {k: r.path_agreement(*v) for k, v in routes.items()}
print(json.dumps(out))
''',
    "reconciliations": '''
import json
import reconcile as rc
print(json.dumps({slug: fn() for slug, (fn, _, _) in rc.RECONCILIATIONS.items()}))
''',
    "processes": '''
import json
import processes as p
print(json.dumps({slug: fn() for slug, (fn, _) in p.PROCESSES.items()}))
''',
    "point_in_time": '''
import json
import relations_temporal as rt
from relations import load_catalogues
cats = load_catalogues()
out = {}
for child, cc, parent, pc in [("Sales.InvoiceLines", "StockItemID", "Warehouse.StockItems", "StockItemID"),
                              ("Sales.Invoices", "CustomerID", "Sales.Customers", "CustomerID"),
                              ("Sales.CustomerTransactions", "CustomerID", "Sales.Customers", "CustomerID"),
                              ("Sales.Orders", "SalespersonPersonID", "Application.People", "PersonID")]:
    out["%s.%s" % (child, cc)] = rt.as_of(child, cc, parent, pc, cats)
out["Sales.Invoices.OrderID by backorder"] = rt.order_dates_by_backorder("Sales.Invoices", "OrderID")
print(json.dumps(out))
''',
}


def run(probe, day, prev):
    env = dict(os.environ, IA_DAY=day, IA_PREV=prev, PYTHONPATH=HERE)
    p = subprocess.run([sys.executable, "-c", PROBES[probe]], cwd=HERE, env=env, capture_output=True, text=True, check=True)
    return json.loads(p.stdout.strip().splitlines()[-1])


def follow_ups(base, new):
    """What the base extract left open, looked up in the new one."""
    import csv
    import gzip
    import collections
    from decimal import Decimal as D
    csv.field_size_limit(1 << 30)

    def rd(day, t):
        with gzip.open(os.path.join(RAW, day, t + ".csv.gz"), "rt", encoding="utf-8", newline="") as f:
            return list(csv.DictReader(f))
    out = {}
    # purchase-order lines not received in the base extract
    pl0 = {r["PurchaseOrderLineID"]: r for r in rd(base, "Purchasing.PurchaseOrderLines")}
    pl1 = {r["PurchaseOrderLineID"]: r for r in rd(new, "Purchasing.PurchaseOrderLines")}
    open0 = [k for k, r in pl0.items() if r["IsOrderLineFinalized"] != "1"]
    mv = collections.Counter((r["PurchaseOrderID"], r["StockItemID"]) for r in rd(new, "Warehouse.StockItemTransactions") if r["PurchaseOrderID"])
    mv0 = collections.Counter((r["PurchaseOrderID"], r["StockItemID"]) for r in rd(base, "Warehouse.StockItemTransactions") if r["PurchaseOrderID"])
    out["purchase_order_lines_open_in_base"] = {
        "lines": len(open0),
        "in_new": dict(collections.Counter(
            "finalized=%s|received %s ordered|movements in base=%d|movements in new=%d" % (
                pl1[k]["IsOrderLineFinalized"], "=" if pl1[k]["ReceivedOuters"] == pl1[k]["OrderedOuters"] else "!=",
                mv0[(pl1[k]["PurchaseOrderID"], pl1[k]["StockItemID"])], mv[(pl1[k]["PurchaseOrderID"], pl1[k]["StockItemID"])]) for k in open0)),
        "new_lines_with_ReceivedOuters_between_0_and_ordered": sum(1 for k, r in pl1.items() if 0 < D(r["ReceivedOuters"]) < D(r["OrderedOuters"]))}
    # supplier and customer invoices open in the base extract
    for t, inv_type, key in (("Purchasing.SupplierTransactions", "5", "SupplierTransactionID"), ("Sales.CustomerTransactions", "1", "CustomerTransactionID")):
        a = {r[key]: r for r in rd(base, t)}
        b = {r[key]: r for r in rd(new, t)}
        op = [k for k, r in a.items() if r["TransactionTypeID"] == inv_type and r["IsFinalized"] != "1"]
        out["%s_invoices_open_in_base" % t] = {
            "invoices": len(op),
            "in_new": dict(collections.Counter(
                "finalized=%s|outstanding=%s" % (b[k]["IsFinalized"], "0" if D(b[k]["OutstandingBalance"]) == 0 else
                                                  "full" if D(b[k]["OutstandingBalance"]) == D(b[k]["TransactionAmount"]) else "partial") for k in op if k in b)),
            "new_entries_partly_outstanding": sum(1 for r in b.values() if 0 < abs(D(r["OutstandingBalance"])) < abs(D(r["TransactionAmount"])))}
    # orders open in the base extract
    o0 = {r["OrderID"]: r for r in rd(base, "Sales.Orders")}
    o1 = {r["OrderID"]: r for r in rd(new, "Sales.Orders")}
    inv1 = {r["OrderID"] for r in rd(new, "Sales.Invoices")}
    unp = [k for k, r in o0.items() if not r["PickingCompletedWhen"]]
    out["orders_unpicked_in_base"] = {"orders": len(unp), "in_new": dict(collections.Counter(
        "picked=%s|invoiced=%s|is a backorder target=%s" % (bool(o1[k]["PickingCompletedWhen"]), k in inv1,
                                                           k in {r["BackorderOrderID"] for r in o1.values() if r["BackorderOrderID"]}) for k in unp))}
    new_orders = [r for k, r in o1.items() if k not in o0]
    out["orders_added"] = {"orders": len(new_orders), "with_backorder": sum(1 for r in new_orders if r["BackorderOrderID"]),
                           "order_dates": dict(collections.Counter(r["OrderDate"][:10] for r in new_orders))}
    # versions added to history tables
    out["history_rows_added"] = {}
    for t in ("Application.People", "Sales.Customers", "Warehouse.StockItems", "Purchasing.Suppliers"):
        h0, h1 = rd(base, t + "_Archive"), rd(new, t + "_Archive")
        if len(h1) != len(h0):
            k0 = {tuple(sorted(r.items())) for r in h0}
            added = [r for r in h1 if tuple(sorted(r.items())) not in k0]
            cur1 = {r[list(r)[0]]: r for r in rd(new, t)}
            cols = collections.Counter(c for r in added for c in r if c in cur1.get(r[list(r)[0]], {}) and
                                       c not in ("ValidFrom", "ValidTo") and r[c] != cur1[r[list(r)[0]]][c])
            out["history_rows_added"][t] = {"rows": len(added), "columns_differing_from_current": dict(cols)}
    # telemetry per day
    for t, col in (("Warehouse.ColdRoomTemperatures_Archive", "ColdRoomSensorNumber"), ("Warehouse.VehicleTemperatures", "ChillerSensorNumber")):
        b = rd(new, t)
        out["%s_rows_recorded_on_new_day" % t] = dict(collections.Counter(r[col] for r in b if r["RecordedWhen"][:10] == new))
        out["%s_rows_recorded_on_base_day" % t] = dict(collections.Counter(r[col] for r in b if r["RecordedWhen"][:10] == base))
    return out


def main(argv):
    base, base_prev, new, new_prev = argv[1:5]
    rec_base = {"kind": "profile", "tool": SCRIPT, "tool_version": blob(SCRIPT), "ran_at": now()}
    inputs = {"source": "wwi", "base_extract": base, "base_previous": base_prev, "new_extract": new, "new_previous": new_prev,
              "manifests": {d: sha(os.path.join(RAW, d, "manifest.json")) for d in sorted({base, base_prev, new, new_prev})}}
    for probe in PROBES:
        res = {"base": run(probe, base, base_prev), "new": run(probe, new, new_prev)}
        rec = dict(rec_base, code=PROBES[probe], inputs=dict(inputs, probe=probe), result=res)
        rec["id"] = ia.evidence_hash(rec)
        os.makedirs(OUT, exist_ok=True)
        with open(os.path.join(OUT, rec["id"] + ".json"), "w", encoding="ascii", newline="\n") as f:
            json.dump(rec, f, indent=1, sort_keys=True, ensure_ascii=True)
            f.write("\n")
        print(probe, rec["id"])
    rec = dict(rec_base, code=inspect.getsource(follow_ups), inputs=dict(inputs, probe="follow_ups"), result=follow_ups(base, new))
    rec["id"] = ia.evidence_hash(rec)
    with open(os.path.join(OUT, rec["id"] + ".json"), "w", encoding="ascii", newline="\n") as f:
        json.dump(rec, f, indent=1, sort_keys=True, ensure_ascii=True)
        f.write("\n")
    print("follow_ups", rec["id"])


if __name__ == "__main__":
    main(sys.argv)
