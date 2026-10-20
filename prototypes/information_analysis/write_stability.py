"""Write analysis/wwi/_source/22_stability.md (item 22, stability) from recheck.py's evidence: what a newer extract
confirms, contradicts or settles in the record written on an earlier one. Mechanical claims from the counts; readings
from a notes module.

    python prototypes/information_analysis/write_stability.py <notes module>
"""
import importlib.util
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from evidence_orders import blob  # noqa: E402
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import ia_lib as ia  # noqa: E402

SRC = os.path.join(ROOT, "analysis", "wwi", "_source")


def n(x):
    if isinstance(x, float) and x.is_integer():
        x = int(x)
    return format(x, ",")


def load():
    ev = {}
    for f in sorted(os.listdir(os.path.join(SRC, "evidence"))):
        with open(os.path.join(SRC, "evidence", f), encoding="utf-8") as fh:
            rec = json.load(fh)
        if rec.get("tool") == "prototypes/information_analysis/recheck.py":
            p = rec["inputs"]["probe"]
            if p not in ev or rec["ran_at"] > ev[p]["ran_at"]:
                ev[p] = rec
    return ev


def mechanical(ev):
    """(probe, text) pairs: what the counts show, base extract against new."""
    out = []
    i = ev["transitions"]["inputs"]
    B, N = i["base_extract"], i["new_extract"]
    t = ev["transitions"]["result"]
    act = sorted(k for k in t["base"] if any(t[s][k].get(x) for s in ("base", "new") for x in ("inserted", "updated", "deleted")))
    same_cols = [k for k in act if sorted(t["base"][k]["updated_columns"]) == sorted(t["new"][k]["updated_columns"])]
    diff_cols = [k for k in act if k not in same_cols]
    both = [k for k in act if all(any(t[s][k].get(x) for x in ("inserted", "updated", "deleted")) for s in ("base", "new"))]
    dels = "; ".join("%s %s and %s" % (k, t["base"][k]["deleted"], t["new"][k]["deleted"]) for k in act if t["base"][k]["deleted"] or t["new"][k]["deleted"]) or "none"
    out.append(("transitions", "Transitions: %s base tables changed in the first transition (%s to %s) or the second (%s to %s), %s of them in both; "
                "rows deleted, first and second: %s; the columns updated were the same set "
                "in both on %s of them%s. Per table, first and second transition, inserted/updated: %s." % (
                    len(act), i["base_previous"], B, i["new_previous"], N, len(both), dels, len(same_cols),
                    "; on %s they differ: %s" % (len(diff_cols), "; ".join("%s (first: %s; second: %s)" % (
                        k, ", ".join(sorted(t["base"][k]["updated_columns"])), ", ".join(sorted(t["new"][k]["updated_columns"]))) for k in diff_cols)) if diff_cols else "",
                    "; ".join("%s %s/%s, %s/%s" % (k, n(t["base"][k]["inserted"]), n(t["base"][k]["updated"]), n(t["new"][k]["inserted"]), n(t["new"][k]["updated"])) for k in act))))
    others = [k for k in t["base"] if k not in act]
    out.append(("transitions", "The other %s base tables were unchanged in both transitions." % len(others)))
    ck = ev["candidate_keys"]["result"]
    rows = [(k, "+".join(a["columns"]), a["duplicate_rows"], b["duplicate_rows"], b["rows_with_all_filled"]) for k in ck["base"] for a, b in zip(ck["base"][k], ck["new"][k])]
    out.append(("candidate_keys", "Candidate keys: all %s undeclared candidate keys are unique again on %s (duplicates in %s: %s; in %s: %s); rows with the key filled on %s: %s." % (
        len(rows), N, B, sum(r[2] for r in rows), N, sum(r[3] for r in rows), N, "; ".join("%s (%s, %s)" % (k, c, n(m)) for k, c, _, _, m in rows))))
    r = ev["relations"]["result"]
    rel = [k for k in r["base"] if k != "two_routes"]
    orph = sum(r[s][k]["orphan_rows"] for s in ("base", "new") for k in rel)
    one_b = [k for k in rel if r["base"][k]["max_children"] == 1]
    one_n = [k for k in one_b if r["new"][k]["max_children"] == 1]
    unused = [k for k in rel if r["base"][k]["max_children"] is None and r["new"][k]["max_children"] is None]
    out.append(("relations", "Relations: %s relations, orphans in either extract: %s; of the %s relations with exactly one child at most per parent on %s, %s still have at most one on %s%s; %s relations have no filled child row in either extract (%s)." % (
        len(rel), orph, len(one_b), B, len(one_n), N, "" if len(one_n) == len(one_b) else " (no longer: %s)" % ", ".join(sorted(set(one_b) - set(one_n))),
        len(unused), ", ".join(unused))))
    tr = r["base"]["two_routes"]
    out.append(("relations", "Two routes to the same parent, rows where both are filled agreeing in %s and in %s: %s." % (B, N, "; ".join(
        "%s %s/%s and %s/%s" % (k, n(tr[k]["agree"]), n(tr[k]["rows_with_both_routes"]), n(r["new"]["two_routes"][k]["agree"]), n(r["new"]["two_routes"][k]["rows_with_both_routes"])) for k in tr))))
    rc = ev["reconciliations"]["result"]
    il, lg = rc["new"]["invoice-lines-vs-stock-issues"], rc["new"]["ledger-invoices-vs-invoice-lines"]
    cp, sp = rc["new"]["customer-payments-vs-invoices"], rc["new"]["supplier-payments-vs-invoices"]
    si, sh = rc["new"]["supplier-invoices-vs-purchase-order-lines"], rc["new"]["stock-holdings-vs-movements"]
    out.append(("reconciliations", "Reconciliations on %s: stock issues equal their invoice line negated on %s of %s, with %s line keys having more than one movement and %s lines none; ledger "
                "invoice entries equal the sum of their lines on %s of %s; customer payments equal the invoices finalized that day on %s of %s, at most %s per customer and day; "
                "supplier payments likewise on %s of %s; supplier invoices equal their purchase order at the expected price on %s of %s, with tax below the per-line 15%% on %s." % (
                    N, n(il["quantity"].get("movement = -line quantity", 0)), n(il["movements_with_invoice"]), n(il["line_keys_with_more_than_one_movement"]), n(il["lines_without_movement"]),
                    n(lg["comparisons"].get("TransactionAmount equal to sum of ExtendedPrice", 0)), n(lg["invoice_entries"]),
                    n(cp["payment_against_invoices_finalized_that_day"].get("payment = -(invoices finalized that day)", 0)), n(cp["payments"]), cp["payments_per_party_and_day_max"],
                    n(sp["payment_against_invoices_finalized_that_day"].get("payment = -(invoices finalized that day)", 0)), n(sp["payments"]),
                    n(si["comparisons"].get("AmountExcludingTax equal to sum of ReceivedOuters x ExpectedUnitPricePerOuter", 0)), n(si["supplier_invoices"]),
                    n(si["comparisons"].get("TaxAmount less than the sum over lines of 15% of ReceivedOuters x ExpectedUnitPricePerOuter, each rounded half up", 0)))))
    out.append(("reconciliations", "Customer invoices in the extract of %s: finalized %s day(s) after their date on all %s finalized; %s open in full, %s part paid." % (
        N, " or ".join(cp["days_from_invoice_to_finalization"]), n(sum(cp["days_from_invoice_to_finalization"].values())),
        n(cp["invoice_states"].get("IsFinalized=0|FinalizationDate=empty|OutstandingBalance=the full amount", 0)),
        n(sum(v for k, v in cp["invoice_states"].items() if "partial" in k)))))
    lv, chg = sh["level_against_sum_of_all_movements"], sh["change_against_movements_added"]
    out.append(("reconciliations", "Stock holdings on %s: QuantityOnHand equals the sum of movements for %s of %s items; its change from %s equals the movements added for %s and differs for %s (%s movements added, %s earlier ones changed, %s deleted)." % (
        N, n(lv.get("equal to", 0)), n(sh["items"]), i["new_previous"], n(chg.get("change equal to movements added", 0)),
        n(sum(v for k, v in chg.items() if "equal" not in k)), n(sum(sh["movements_added_between_extracts"].values())),
        n(sh["earlier_movements_with_changed_quantity"]), n(sh["earlier_movements_deleted"]))))
    p = ev["processes"]["result"]
    for slug in ("order-to-cash", "procure-to-pay"):
        a, b = p["base"][slug]["days"], p["new"][slug]["days"]
        same = [k for k in a if (a[k].get("min"), a[k].get("max")) == (b[k].get("min"), b[k].get("max"))]
        out.append(("processes", "%s: the range of days between steps is the same in both extracts for %s of %s step pairs (%s)." % (
            slug, len(same), len(a), "; ".join("%s %s to %s" % (k, n(b[k]["min"]), n(b[k]["max"])) for k in sorted(b) if b[k].get("rows")))))
    pit = ev["point_in_time"]["result"]
    keys = [k for k in pit["new"] if "attributes_that_differ_rows" in pit["new"][k]]
    same = [k for k in keys if sorted(pit["new"][k]["attributes_that_differ_rows"]) == sorted(pit["base"].get(k, {}).get("attributes_that_differ_rows", {}))]
    out.append(("point_in_time", "Point in time: the set of attributes that differ between the version current at a row's date and the current one is the same on %s as on %s for %s of %s relations tested%s: %s." % (
        N, B, len(same), len(keys), "" if len(same) == len(keys) else " (different for %s)" % ", ".join(k for k in keys if k not in same),
        "; ".join("%s %s" % (k, ", ".join(sorted(pit["new"][k]["attributes_that_differ_rows"]))) for k in keys))))
    f = ev["follow_ups"]["result"]
    out.append(("follow_ups", "Left open on %s, seen on %s: the %s customer invoices open then are %s; the %s supplier invoices open then are %s; the %s purchase-order lines open then are %s; no line anywhere has ReceivedOuters between 0 and OrderedOuters (%s)." % (
        B, N, f["Sales.CustomerTransactions_invoices_open_in_base"]["invoices"], "; ".join("%s: %s" % kv for kv in f["Sales.CustomerTransactions_invoices_open_in_base"]["in_new"].items()),
        f["Purchasing.SupplierTransactions_invoices_open_in_base"]["invoices"], "; ".join("%s: %s" % kv for kv in f["Purchasing.SupplierTransactions_invoices_open_in_base"]["in_new"].items()),
        f["purchase_order_lines_open_in_base"]["lines"], "; ".join("%s: %s" % kv for kv in f["purchase_order_lines_open_in_base"]["in_new"].items()),
        f["purchase_order_lines_open_in_base"]["new_lines_with_ReceivedOuters_between_0_and_ordered"])))
    u = f["orders_unpicked_in_base"]
    out.append(("follow_ups", "The %s orders not picked on %s, on %s: %s." % (n(u["orders"]), B, N, "; ".join("%s: %s" % (k, n(v)) for k, v in sorted(u["in_new"].items())))))
    o = f["orders_added"]
    out.append(("follow_ups", "Orders added on %s: %s, all dated %s; %s of them already split into a backorder." % (N, n(o["orders"]), ", ".join(o["order_dates"]), n(o["with_backorder"]))))
    h = f["history_rows_added"]
    out.append(("follow_ups", "Versions added to history tables between the extracts: %s." % ("; ".join("%s %s, columns differing from the current version: %s" % (
        k, v["rows"], ", ".join(v["columns_differing_from_current"]) or "none") for k, v in h.items()) or "none")))
    fmt = lambda d: ", ".join("sensor %s %s" % (k, n(v)) for k, v in sorted(d.items()))
    out.append(("follow_ups", "Telemetry per sensor and day, counted in the extract of %s: rows of Warehouse.ColdRoomTemperatures_Archive (the earlier readings; the current table holds the latest four) recorded on %s: %s; on %s: %s; rows of Warehouse.VehicleTemperatures on %s: %s; on %s: %s." % (
        N, B, fmt(f["Warehouse.ColdRoomTemperatures_Archive_rows_recorded_on_base_day"]), N, fmt(f["Warehouse.ColdRoomTemperatures_Archive_rows_recorded_on_new_day"]),
        B, fmt(f["Warehouse.VehicleTemperatures_rows_recorded_on_base_day"]), N, fmt(f["Warehouse.VehicleTemperatures_rows_recorded_on_new_day"]))))
    return out


def main(argv):
    sp = importlib.util.spec_from_file_location("notes", argv[1])
    notes = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(notes)
    ev = load()
    new = ev["transitions"]["inputs"]["new_extract"]
    claims = [("observed", "high", [p], "every new extract", ascii(t)) for p, t in mechanical(ev)] + list(notes.READINGS)
    conf = ia.CONFIDENCE[min(ia.CONFIDENCE.index(c[1]) for c in claims)]
    lines = ["- C%d | type=%s | status=proposed | confidence=%s | effective=%s | observed=%s | checked=%s | evidence=%s | recheck=%s | text: %s"
             % (k, typ, cf, new, notes.NOW[:10], notes.NOW[:10], ",".join(ev[p]["id"] for p in evs) or "none", rc, t)
             for k, (typ, cf, evs, rc, t) in enumerate(claims, 1)]
    front = dict(notes.COMMON, id="wwi:source:stability", subject="wwi/_source", item="22", topic="stability", tier="best-effort",
                 summary=notes.SUMMARY, confidence=conf, claims=str(len(claims)),
                 method="counts by prototypes/information_analysis/recheck.py (blob %s), claims by write_stability.py (blob %s); readings by %s" % (
                     ev["transitions"]["tool_version"], blob("prototypes/information_analysis/write_stability.py"), notes.COMMON["written_by"]),
                 input_extract=new, input_manifest_sha256=ev["transitions"]["inputs"]["manifests"][new], input_schema_sha256="none",
                 last_checked_against=new, recheck_when="every new extract")
    txt = ("---\n" + "\n".join("%s: %s" % (k, front[k]) for k in ia.FRONT_KEYS) + "\n---\n\n## Claims\n\n" + "\n".join(lines) +
           "\n\n## Reasoning\n\n" + notes.REASONING + "\n\n## Uncertainties\n\n" + notes.UNCERTAINTIES + "\n\n## For a person\n\nNone.\n")
    assert all(ord(ch) < 128 for ch in txt)
    with open(os.path.join(SRC, "22_stability.md"), "w", encoding="ascii", newline="\n") as f:
        f.write(txt)
    print("wrote 22_stability.md with", len(claims), "claims")


def ascii(s):
    assert all(ord(ch) < 128 for ch in s), s
    return s


if __name__ == "__main__":
    main(sys.argv)
