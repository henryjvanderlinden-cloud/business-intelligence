"""Round 2 (ADR-0019, analysis/README.md section 9): evidence on every relation between WWI base tables, and the
generated candidates list.

For each declared foreign key, one evidence file in analysis/wwi/across/relations/<rel>/evidence/: the declaration
(catalogue metadata, verbatim), orphans both ways, optionality, children per referenced parent, and the other unique
columns of the parent that would accept the same values (an ambiguous key target). For undeclared columns whose name
ends in ID, a test of value inclusion in every single-column primary key, written to across/candidates.md.

    python prototypes/information_analysis/relations.py
"""
import collections
import csv
import gzip
import json
import os
import statistics
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from evidence_orders import blob, sha, now  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import ia_lib as ia  # noqa: E402

SCRIPT = "prototypes/information_analysis/relations.py"
RAW = os.path.join(ROOT, "data", "raw", "wwi")
DAY = os.environ.get("IA_DAY", "2016-06-01")   # recheck.py sets it
PROFILE_DIR = os.path.join(ROOT, "scratch", "ia_profile")
ACROSS = os.path.join(ROOT, "analysis", "wwi", "across")
INT_TYPES = {"int", "bigint", "smallint", "tinyint"}
AUDIT_COLUMNS = {"LastEditedBy", "LastEditedWhen", "ValidFrom", "ValidTo"}
csv.field_size_limit(1 << 30)


def rel_name(cs, ct, cc, ps, pt, pc):
    """analysis/README.md section 3: <schema>.<table>.<column>__<schema>.<table>.<column>, each part escaped."""
    return "%s.%s.%s__%s.%s.%s" % tuple(ia.escape(x) for x in (cs, ct, cc, ps, pt, pc))


def load_catalogues():
    cats = {}
    for f in sorted(os.listdir(PROFILE_DIR)):
        with open(os.path.join(PROFILE_DIR, f), encoding="utf-8") as fh:
            d = json.load(fh)
        if d["catalogue"]["table"][0]["temporal_type_desc"] == "HISTORY_TABLE":
            continue
        cats[f[:-5]] = d
    return cats


_cache = {}


def column(table, col):
    """All values of one column of the extract, as strings ("" for empty)."""
    if table not in _cache:
        with gzip.open(os.path.join(RAW, DAY, table + ".csv.gz"), "rt", encoding="utf-8", newline="") as f:
            r = csv.reader(f)
            head = next(r)
            rows = list(r)
        _cache[table] = (head, {})
        _cache[table][1]["__rows__"] = rows
    head, cols = _cache[table]
    if col not in cols:
        i = head.index(col)
        cols[col] = [row[i] for row in cols["__rows__"]]
    return cols[col]


def unique_columns(table, d):
    """Columns of the parent whose values are unique and never empty in the extract, with whether declared unique."""
    declared = collections.defaultdict(list)
    for k in d["catalogue"]["keys"]:
        if k["is_unique"] == "1" or k["is_primary_key"] == "1":
            declared[k["index_name"]].append(k["column_name"])
    single = {cols[0] for cols in declared.values() if len(cols) == 1}
    out = {}
    n = d["profile"]["rows"]
    for c, s in d["profile"]["columns"].items():
        if s.get("distinct") == n and s.get("empty") == 0:
            out[c] = c in single
    return out


def stats(counts):
    v = sorted(counts)
    if not v:
        return {}
    return {"min": v[0], "median": statistics.median(v), "p90": v[int(0.9 * (len(v) - 1))], "max": v[-1],
            "mean": round(sum(v) / len(v), 3), "parents_with_exactly_one": sum(1 for x in v if x == 1)}


def relation_profile(child, ccol, parent, pcol, pd):
    """Orphans both ways, optionality, children per referenced parent, other accepting unique columns."""
    cv = column(child, ccol)
    pv = column(parent, pcol)
    pset = set(pv)
    filled = [v for v in cv if v != ""]
    per = collections.Counter(filled)
    orphan_vals = {v for v in per if v not in pset}
    alt = {}
    for c, declared in unique_columns(parent, pd).items():
        if c == pcol or not per:
            continue
        s = set(column(parent, c))
        if all(v in s for v in per):
            alt[c] = {"declared_unique": declared}
    return {
        "child_rows": len(cv), "child_filled": len(filled), "child_empty": len(cv) - len(filled),
        "child_distinct": len(per),
        "orphan_rows": sum(per[v] for v in orphan_vals), "orphan_distinct": len(orphan_vals),
        "parent_rows": len(pv), "parent_key_distinct": len(pset), "parent_key_empty": sum(1 for v in pv if v == ""),
        "parents_referenced": len(set(per) & pset), "parents_unreferenced": len(pset - set(per)),
        "children_per_referenced_parent": stats([k for v, k in per.items() if v in pset]),
        "other_unique_parent_columns_accepting_all_values": alt,
        "inner_join_rows": sum(per[v] for v in per if v in pset),
    }


def write_evidence(out_dir, record):
    record = dict(record)
    record.pop("id", None)
    record["id"] = ia.evidence_hash(record)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, record["id"] + ".json")
    if not os.path.exists(path):
        with open(path, "w", encoding="ascii", newline="\n") as f:
            json.dump(record, f, indent=1, sort_keys=True, ensure_ascii=True)
            f.write("\n")
    return record["id"]


def path_agreement(a, a1, a2, c, c_key, cx):
    """Two routes from table a to the same parent: a.a1 directly, and a.a2 -> c (on c_key), then c.cx. Counts the
    rows of a where both routes name a parent, and how often they name the same one."""
    v1, v2 = column(a, a1), column(a, a2)
    look = dict(zip(column(c, c_key), column(c, cx)))
    both = agree = 0
    for x, y in zip(v1, v2):
        if x == "" or y == "" or y not in look or look[y] == "":
            continue
        both += 1
        agree += look[y] == x
    return {"rows": len(v1), "rows_with_both_routes": both, "agree": agree, "disagree": both - agree}


VISIBILITY = ("rows_seen_by_owner", "rows_seen_by_nsdn_reader", "rows_in_extract", "security_policies_visible_to_reader",
              "masked_columns")


def column_names(table):
    column(table, column_names_first(table))
    return _cache[table][0]


def column_names_first(table):
    with gzip.open(os.path.join(RAW, DAY, table + ".csv.gz"), "rt", encoding="utf-8", newline="") as f:
        return next(csv.reader(f))[0]


def by_transaction_type(child, ccol):
    """The child's rows counted by TransactionTypeID and by whether ccol is filled."""
    names = dict(zip(column("Application.TransactionTypes", "TransactionTypeID"), column("Application.TransactionTypes", "TransactionTypeName")))
    return {"%s %s|%s" % (t, names.get(t, "?"), "filled" if v != "" else "empty"): k for (t, v), k in sorted(collections.Counter(
        (t, "x" if v != "" else "") for t, v in zip(column(child, "TransactionTypeID"), column(child, ccol))).items())}


def people_flags(child, ccol):
    """For a relation to Application.People: the referring rows counted by the flags of the person they name."""
    flags = ("IsEmployee", "IsSalesperson", "IsPermittedToLogon")
    who = {pid: "|".join("%s=%s" % (f, v) for f, v in zip(flags, vals))
           for pid, *vals in zip(column("Application.People", "PersonID"), *[column("Application.People", f) for f in flags])}
    return dict(collections.Counter(who.get(v, "not found") for v in column(child, ccol) if v != ""))


def composite_profile(child, ccols, parent, pcols):
    """An undeclared relation on several columns: inclusion of the child's combinations in the parent's, both ways."""
    ck = list(zip(*[column(child, c) for c in ccols]))
    pk = list(zip(*[column(parent, c) for c in pcols]))
    pset = collections.Counter(pk)
    filled = [k for k in ck if all(v != "" for v in k)]
    per = collections.Counter(filled)
    return {"child_rows": len(ck), "child_filled": len(filled), "child_empty": len(ck) - len(filled),
            "child_distinct": len(per), "orphan_rows": sum(n for k, n in per.items() if k not in pset),
            "orphan_distinct": sum(1 for k in per if k not in pset), "parent_rows": len(pk),
            "parent_combination_distinct": len(pset), "parent_combination_unique": len(pset) == len(pk),
            "parents_referenced": sum(1 for k in pset if k in per), "parents_unreferenced": sum(1 for k in pset if k not in per),
            "children_per_referenced_parent": stats([n for k, n in per.items() if k in pset]),
            "rows_if_joined_on_%s_only" % ccols[0]: header_join_rows(child, ccols[0], parent, pcols[0]),
            "rows_if_joined_on_all_columns": sum(n * pset[k] for k, n in per.items() if k in pset)}


def header_join_rows(child, ccol, parent, pcol):
    """Rows an inner join on one column alone would produce: the sum over its values of child rows times parent rows."""
    a = collections.Counter(v for v in column(child, ccol) if v != "")
    b = collections.Counter(v for v in column(parent, pcol) if v != "")
    return sum(n * b[v] for v, n in a.items() if v in b)


# Undeclared relations on several columns, chosen from round 1's candidate keys (Sales.InvoiceLines 01,
# Purchasing.PurchaseOrderLines 01, Warehouse.StockItemTransactions 01): stock movements against document lines.
COMPOSITE = [("Warehouse.StockItemTransactions", ("InvoiceID", "StockItemID"), "Sales.InvoiceLines", ("InvoiceID", "StockItemID")),
             ("Warehouse.StockItemTransactions", ("PurchaseOrderID", "StockItemID"), "Purchasing.PurchaseOrderLines", ("PurchaseOrderID", "StockItemID"))]


def main():
    import inspect
    cats = load_catalogues()
    base = {"kind": "profile", "tool": SCRIPT, "tool_version": blob(SCRIPT), "ran_at": now()}
    inp = {"source": "wwi", "extract": DAY, "manifest_sha256": sha(os.path.join(RAW, DAY, "manifest.json"))}
    code = "\n".join(inspect.getsource(f) for f in (relation_profile, unique_columns, stats, path_agreement, people_flags,
                                                   by_transaction_type))
    fks = []
    for t, d in cats.items():
        for k in d["catalogue"]["foreign_keys_out"]:
            fks.append(("%s.%s" % (k["schema_name"], k["table_name"]), k["column_name"],
                        "%s.%s" % (k["ref_schema"], k["ref_table"]), k["ref_column"], k))
    declared, in_fk, pending = [], set(), []
    for child, ccol, parent, pcol, k in fks:
        d = cats[child]
        in_fk.add((child, ccol))
        name = rel_name(k["schema_name"], k["table_name"], ccol, k["ref_schema"], k["ref_table"], pcol)
        res = relation_profile(child, ccol, parent, pcol, cats[parent])
        ccat = next(x for x in d["catalogue"]["columns"] if x["column_name"] == ccol)
        pcat = cats[parent]["catalogue"]
        res["declaration"] = {"foreign_key": k, "child_column": {x: ccat[x] for x in ("type_name", "is_nullable", "description")},
                              "parent_temporal_type": pcat["table"][0]["temporal_type_desc"],
                              "child_temporal_type": d["catalogue"]["table"][0]["temporal_type_desc"]}
        # structure: other foreign keys from the same child to the same parent (roles), other children of the parent
        res["same_child_same_parent"] = sorted(c2 for ch, c2, p2, _, _ in fks if ch == child and p2 == parent and c2 != ccol)
        # two routes to the same parent: child.ccol directly, and child.a2 -> c -> c.cx
        routes = {}
        if ccol != "LastEditedBy":
            for ch, a2, c, c_key, _ in fks:
                if ch != child or a2 == ccol or a2 == "LastEditedBy" or c == child:
                    continue
                for ch2, cx, p2, _, _ in fks:
                    if ch2 == c and p2 == parent and cx != "LastEditedBy":
                        routes["%s -> %s.%s" % (a2, c, cx)] = path_agreement(child, ccol, a2, c, c_key, cx)
        res["two_routes_to_parent"] = routes
        if parent == "Application.People":
            res["child_rows_by_flags_of_person_named"] = people_flags(child, ccol)
        if "TransactionTypeID" in column_names(child) and ccol != "TransactionTypeID":
            res["child_rows_by_transaction_type"] = by_transaction_type(child, ccol)
        res["extraction_visibility"] = {t: {x: cats[t]["catalogue"][x] for x in VISIBILITY} for t in sorted({child, parent})}
        pending.append((name, child, ccol, parent, pcol, k, res))
    # after all relations are profiled: the multiplicity of the parent's other referring columns (chasm traps)
    most = {(ch, cc): r["children_per_referenced_parent"].get("max", 0) for _, ch, cc, _, _, _, r in pending}
    for name, child, ccol, parent, pcol, k, res in pending:
        res["other_children_of_parent"] = {"%s.%s" % (ch, c2): most[(ch, c2)] for ch, c2, p2, _, _ in fks
                                           if p2 == parent and (ch, c2) != (child, ccol) and c2 != "LastEditedBy"}
        h = write_evidence(os.path.join(ACROSS, "relations", name, "evidence"),
                           dict(base, code=code, inputs=dict(inp, child=child, child_column=ccol,
                                                             parent=parent, parent_column=pcol), result=res))
        declared.append((name, child, ccol, parent, pcol, k["fk_name"], h, res))
        print(name, h, res["orphan_rows"], res["child_empty"], res["children_per_referenced_parent"].get("max"))
    composite = []
    for child, ccols, parent, pcols in COMPOSITE:
        cs, ct = child.split(".")
        ps, pt = parent.split(".")
        name = "%s.%s.%s__%s.%s.%s" % (ia.escape(cs), ia.escape(ct), ".".join(ia.escape(c) for c in ccols),
                                       ia.escape(ps), ia.escape(pt), ".".join(ia.escape(c) for c in pcols))
        res = composite_profile(child, ccols, parent, pcols)
        if "TransactionTypeID" in column_names(child):
            res["child_rows_by_transaction_type"] = by_transaction_type(child, ccols[0])
        res["extraction_visibility"] = {t: {x: cats[t]["catalogue"][x] for x in VISIBILITY} for t in sorted({child, parent})}
        h = write_evidence(os.path.join(ACROSS, "relations", name, "evidence"),
                           dict(base, code=inspect.getsource(composite_profile) + "\n" + inspect.getsource(header_join_rows) + "\n" + inspect.getsource(by_transaction_type), inputs=dict(inp, child=child, child_columns=list(ccols),
                                                                                         parent=parent, parent_columns=list(pcols)), result=res))
        composite.append((name, h, res))
        print(name, h, res)
    # undeclared: integer columns named ...ID, not a foreign key, not the table's own single-column primary key
    pks = {}
    for t, d in cats.items():
        pk = [k["column_name"] for k in d["catalogue"]["keys"] if k["is_primary_key"] == "1"]
        if len(pk) == 1:
            pks[t] = pk[0]
    undeclared = []
    for t, d in cats.items():
        for x in d["catalogue"]["columns"]:
            c = x["column_name"]
            if not c.endswith("ID") or x["type_name"] not in INT_TYPES or (t, c) in in_fk or pks.get(t) == c:
                continue
            vals = {v for v in column(t, c) if v != ""}
            if not vals:
                undeclared.append((t, c, None, 0, 0, False))
                continue
            for p, pc in pks.items():
                ps = set(column(p, pc))
                hit = len(vals & ps)
                if hit:
                    undeclared.append((t, c, "%s.%s" % (p, pc), hit, len(vals), c.endswith(pc)))
    # columns of the same name in several tables, other than keys, foreign keys and audit columns: possible copies
    keyish = {(t, c) for t, c in in_fk} | {(t, c) for t, c in pks.items()} | {(p, c) for p, c in pks.items()}
    names = collections.defaultdict(list)
    for t, d in cats.items():
        for x in d["catalogue"]["columns"]:
            c = x["column_name"]
            if c in AUDIT_COLUMNS or (t, c) in keyish or c in pks.values():
                continue
            names[c].append(t)
    same_name = {c: sorted(ts) for c, ts in names.items() if len(ts) > 1}
    rec = dict(base, code=inspect.getsource(main), inputs=dict(inp, tables=sorted(cats)),
               result={"undeclared_inclusion": [list(u) for u in undeclared], "same_name_columns": same_name})
    h = write_evidence(os.path.join(ACROSS, "evidence"), rec)
    write_candidates(declared, undeclared, same_name, composite, h, base["ran_at"])


def write_candidates(declared, undeclared, same_name, composite, h, ran_at):
    L = ["# Relations to analyse (generated)", "",
         "Generated by `%s` at %s from the 2016-06-01 extract; not hand-edited (analysis/README.md section 9). "
         "**proven** = declared and no orphan in the extract; **declared** = declared, with orphans; **observed** = not "
         "declared, every value found in the target key; **assumed** = not declared, some values found; the name column "
         "says whether the column name ends in the target key's name. Evidence of the undeclared tests: "
         "`evidence/%s.json`." % (SCRIPT, ran_at, h), "",
         "## Declared foreign keys (%d)" % len(declared), "",
         "| relation | constraint | status | orphans | empty | max children per parent | evidence |", "|---|---|---|---|---|---|---|"]
    for name, child, cc, parent, pc, fk, eh, r in sorted(declared):
        st = "proven" if r["orphan_rows"] == 0 else "declared"
        L.append("| [%s](relations/%s/) | %s | %s | %s | %s | %s | %s |" % (
            name, name, fk, st, format(r["orphan_rows"], ","), format(r["child_empty"], ","),
            r["children_per_referenced_parent"].get("max", "-"), eh))
    L += ["", "## Undeclared columns named ...ID (%d tests)" % len(undeclared), "",
          "| column | target key | values found | of distinct values | name matches | status |", "|---|---|---|---|---|---|"]
    for t, c, target, hit, n, nm in sorted(undeclared, key=lambda u: (u[0], u[1], -(u[3] or 0))):
        if target is None:
            L.append("| %s.%s | - | - | 0 (always empty) | - | none |" % (t, c))
            continue
        st = "observed" if hit == n else "assumed"
        L.append("| %s.%s | %s | %s | %s | %s | %s |" % (t, c, target, format(hit, ","), format(n, ","), "yes" if nm else "no", st))
    if not undeclared:
        L.append("| (none: every integer column named ...ID other than a table's own key is a declared foreign key) | | | | | |")
    L += ["", "## Undeclared relations on several columns (%d)" % len(composite), "",
          "Chosen from round 1's candidate keys; tested for inclusion both ways.", "",
          "| relation | status | orphans | empty | parents unreferenced | evidence |", "|---|---|---|---|---|---|"]
    for name, eh, r in composite:
        L.append("| [%s](relations/%s/) | %s | %s | %s | %s | %s |" % (
            name, name, "observed" if r["orphan_rows"] == 0 else "assumed", format(r["orphan_rows"], ","),
            format(r["child_empty"], ","), format(r["parents_unreferenced"], ","), eh))
    L += ["", "## Columns of the same name in several tables (%d)" % len(same_name), "",
          "Not keys, foreign keys or audit columns. A shared name suggests a copy or a common domain (item 12, round 2); "
          "it proves nothing. Status: **assumed** until a relation folder tests it.", "",
          "| column | tables |", "|---|---|"]
    for c, ts in sorted(same_name.items()):
        L.append("| %s | %s |" % (c, ", ".join(ts)))
    L.append("")
    with open(os.path.join(ACROSS, "candidates.md"), "w", encoding="ascii", newline="\n") as f:
        f.write("\n".join(L))


if __name__ == "__main__":
    main()
