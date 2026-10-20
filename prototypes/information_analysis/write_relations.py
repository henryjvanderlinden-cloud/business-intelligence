"""Write round-2 relation dossiers (ADR-0019; analysis/README.md section 9): items 01, 02, 06, 07 and 27 for every
relation folder that relations.py gave evidence.

Mechanical claims come from the relation's evidence (declaration, orphans, cardinality, routes); judgement claims
(what the join means, warnings beyond the mechanical ones) from a notes module written by the agent. As-is only
(ADR-0020): the files say what the data and the declarations show, and warn; they do not design joins.

    python prototypes/information_analysis/write_relations.py <notes module>
"""
import importlib.util
import json
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from evidence_orders import blob  # noqa: E402
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import ia_lib as ia  # noqa: E402

REL_DIR = os.path.join(ROOT, "analysis", "wwi", "across", "relations")
PROFILE_DIR = os.path.join(ROOT, "scratch", "ia_profile")
DAY = "2016-06-01"
RANK = ia.CONFIDENCE


def ascii_only(s):
    s = s.replace("—", "-").replace("–", "-").replace("’", "'").replace("“", '"').replace("”", '"')
    assert all(ord(ch) < 128 for ch in s), s
    return s


def n(x):
    if isinstance(x, float) and x.is_integer():
        x = int(x)
    return format(x, ",")


class Item:
    def __init__(self):
        self.claims = []

    def add(self, typ, conf, recheck, text, ev=("rel",)):
        self.claims.append((typ, conf, list(ev), recheck, ascii_only(text)))


def write_item(path, front, claims, evmap, observed, reasoning, uncert):
    lines = []
    for i, (typ, conf, ev, recheck, text) in enumerate(claims, 1):
        evs = ",".join(evmap[e] for e in ev if evmap.get(e)) or "none"
        lines.append("- C%d | type=%s | status=proposed | confidence=%s | effective=%s | observed=%s | checked=%s | "
                     "evidence=%s | recheck=%s | text: %s" % (i, typ, conf, DAY, observed, observed, evs, recheck, text))
    front = dict(front, confidence=RANK[min(RANK.index(c[1]) for c in claims)], claims=str(len(claims)))
    txt = "---\n" + "\n".join("%s: %s" % (k, front[k]) for k in ia.FRONT_KEYS) + "\n---\n\n## Claims\n\n" + \
        "\n".join(lines) + "\n\n## Reasoning\n\n" + ascii_only(reasoning.strip()) + "\n\n## Uncertainties\n\n" + \
        ascii_only(uncert.strip() or "None.") + "\n\n## For a person\n\nNone.\n"
    with open(path, "w", encoding="ascii", newline="\n") as f:
        f.write(txt)


def latest_evidence(folder, tool="prototypes/information_analysis/relations.py"):
    best = None
    for f in sorted(os.listdir(os.path.join(folder, "evidence"))):
        with open(os.path.join(folder, "evidence", f), encoding="utf-8") as fh:
            rec = json.load(fh)
        if rec.get("tool") == tool and (best is None or rec["ran_at"] > best["ran_at"]):
            best = rec
    return best


def temporal_item(it, t, child, parent, cc):
    """Item 03 from relations_temporal.py's evidence; returns the summary."""
    r = t["result"]
    src = r.get("child_date_column")
    summ = []
    if r["parent_temporal_type"] == "SYSTEM_VERSIONED_TEMPORAL_TABLE":
        it.add("declared", "high", "the temporal type changes",
               "%s is system-versioned: the version of a row current at a given time is in %s_Archive or the table itself, "
               "by ValidFrom and ValidTo." % (parent, parent), ev=("tmp",))
    else:
        it.add("declared", "high", "the temporal type changes",
               "%s is not system-versioned: an earlier state of a row is not kept, so a row of %s can only be joined to the "
               "row as it is in the extract." % (parent, child), ev=("tmp",))
        summ.append("parent not versioned")
    if src is None:
        it.add("observed", "high", "a date column is added", "%s has no date column, so the relation cannot be placed in time." % child, ev=("tmp",))
        return "No date on the child side."
    a = r.get("as_of")
    if a:
        v = a["parent_version_at_end_of_child_date"]
        parts = ["the current version on %s" % n(v.get("the current version", 0)),
                 "an earlier version on %s" % n(v.get("an earlier version", 0))]
        if v.get("no version yet at the child's date"):
            parts.append("no version yet on %s" % n(v["no version yet at the child's date"]))
        if v.get("no version current at the child's date (a gap between versions)"):
            parts.append("in a gap between versions on %s" % n(v["no version current at the child's date (a gap between versions)"]))
        if v.get("no key or no date"):
            parts.append("no key or no date on %s" % n(v["no key or no date"]))
        it.add("observed", "high", "every new extract",
               "As of the end of each row's date (%s), the row of %s it names was: %s." % (src, parent, "; ".join(parts)), ev=("tmp",))
        d = a["attributes_that_differ_rows"]
        if d:
            it.add("observed", "high", "every new extract",
                   "On %s of those earlier versions some attributes differ from the current version: %s. Joined in the extract, "
                   "these rows get the current values of these columns, not the values of their date." % (
                       n(v.get("an earlier version whose attributes differ from the current", 0)),
                       ", ".join("%s (%s rows)" % (k, n(x)) for k, x in d.items())), ev=("tmp",))
            it.add("observed", "high", "every new extract",
                   "No other attribute of %s differs between the version current at a row's date and the current version "
                   "(LastEditedBy, LastEditedWhen and the period columns are not compared)." % parent, ev=("tmp",))
            summ.append("earlier parent version on %s rows, differing in %s" % (n(v.get("an earlier version", 0)), ", ".join(d)))
        elif v.get("an earlier version"):
            it.add("observed", "high", "every new extract",
                   "The earlier versions have the same attributes as the current one (LastEditedBy, LastEditedWhen and the period "
                   "columns not compared): joined in the extract, no attribute differs from the one of the row's date.", ev=("tmp",))
            summ.append("earlier versions without differences")
        else:
            summ.append("always the current parent version")
        it.add("intended", "medium", "a ValidFrom far from simulated time appears",
               "The comparison places business dates against system time (ValidFrom), which is the server's clock at the change; "
               "in WWI it follows the simulated dates except for one version of Application.Countries stamped 2022 (round 1), "
               "so it holds as far as the two clocks agree.", ev=())
    o = r.get("date_order")
    if o and o.get("rows"):
        dd = o["days_child_minus_parent"]
        it.add("observed", "high", "every new extract",
               "Date order on %s rows: %s; days from %s.%s to %s: from %s to %s, median %s." % (
                   n(o["rows"]), "; ".join("%s %s" % (k, n(x)) for k, x in sorted(o["order"].items())),
                   parent, o["parent_date_column"], src, n(dd["min"]), n(dd["max"]), n(dd["median"])), ev=("tmp",))
        summ.append("dates: %s" % "; ".join("%s %s" % (k, n(x)) for k, x in sorted(o["order"].items())))
    bb = r.get("date_order_by_backorder")
    if bb:
        it.add("observed", "high", "every new extract", "By whether the order is a backorder: %s." % "; ".join(
            "%s, %s: %s" % (k.split("|")[0], k.split("|")[1], n(x)) for k, x in bb.items()), ev=("tmp",))
    return ("Point in time: " + "; ".join(summ) + ".") if summ else "Point in time: see the claims."


def schema_sha(table):
    with open(os.path.join(PROFILE_DIR, table + ".json"), encoding="utf-8") as f:
        return json.load(f)["profile"]["schema_sha256"]


def card(r):
    c = r["children_per_referenced_parent"]
    return c


def main(argv):
    sp = importlib.util.spec_from_file_location("notes", argv[1])
    notes = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(notes)
    method = ("mechanical claims by prototypes/information_analysis/write_relations.py (blob %s) from the relation's "
              "evidence by relations.py; readings by %s from that evidence, the catalogue's column descriptions and "
              "round 1's files" % (blob("prototypes/information_analysis/write_relations.py"), notes.COMMON["written_by"]))
    observed = notes.NOW[:10]
    # every relation's evidence first, for the warnings that need the others (chasm traps)
    rels = {}
    for name in sorted(os.listdir(REL_DIR)):
        rec = latest_evidence(os.path.join(REL_DIR, name))
        if rec:
            rels[name] = rec
    count = 0
    for name, rec in rels.items():
        i, r = rec["inputs"], rec["result"]
        composite = "child_columns" in i
        child, parent = i["child"], i["parent"]
        ccols = i["child_columns"] if composite else [i["child_column"]]
        pcols = i["parent_columns"] if composite else [i["parent_column"]]
        cc, pc = " + ".join(ccols), " + ".join(pcols)
        C, P = "%s.%s" % (child, cc), "%s.%s" % (parent, pc)
        evmap = {"rel": rec["id"]}
        trec = latest_evidence(os.path.join(REL_DIR, name), "prototypes/information_analysis/relations_temporal.py")
        if trec:
            evmap["tmp"] = trec["id"]
        note = notes.NOTES.get(name, {})
        # round-1 evidence a reading relies on is copied into the relation's folder (content-addressed: same file, same name)
        for key in note.get("copy", ()):
            src = os.path.join(ROOT, "analysis", "wwi", notes.COPY[key])
            dst = os.path.join(REL_DIR, name, "evidence", os.path.basename(src))
            if not os.path.exists(dst):
                shutil.copyfile(src, dst)
            evmap[key] = os.path.basename(src)[:-5]
        ch = card(r)
        decl = r.get("declaration")
        audit = ccols == ["LastEditedBy"]
        items = {}

        # ---------------------------------------------------------------- 01 granularity
        it = Item()
        if decl:
            fk = decl["foreign_key"]
            it.add("declared", "high", "the foreign key changes",
                   "Declared foreign key %s from %s to %s, the primary key of %s: each row of %s names at most one row of %s."
                   % (fk["fk_name"], C, P, parent, child, parent))
        else:
            it.add("declared", "high", "a constraint is declared",
                   "No foreign key or unique constraint declares this relation; %s is %s in the extract."
                   % (P, "unique" if r["parent_combination_unique"] else "NOT unique"))
        if ch:
            it.add("observed", "high", "every new extract",
                   "In this extract %s of %s rows of %s name one of %s referenced rows of %s (of %s); children per referenced "
                   "parent: from %s to %s, median %s; %s parents have exactly one."
                   % (n(r["child_filled"]), n(r["child_rows"]), child, n(r["parents_referenced"]), parent, n(r["parent_rows"]),
                      n(ch["min"]), n(ch["max"]), n(ch["median"]), n(ch["parents_with_exactly_one"])))
        else:
            it.add("observed", "high", "the column fills", "In this extract no row of %s names a row of %s: %s is empty in all %s rows."
                   % (child, parent, cc, n(r["child_rows"])))
        if ch:
            it.add("declared" if decl else "observed", "high" if decl else "medium", "every new extract",
                   "Joined from %s to %s, the result keeps the grain of %s: one row per row of %s%s. Joined the other way, each "
                   "row of %s repeats once per row of %s that names it (C2)%s."
                   % (child, parent, child, child,
                      " (an inner join drops the %s rows where %s is empty)" % (n(r["child_empty"]), cc) if r["child_empty"] else "",
                      parent, child,
                      "" if decl else "; this rests on the parent combination being unique in this extract, which nothing declares"))
            if ch["max"] == 1:
                it.add("observed", "medium", "a second row refers to the same parent",
                       "One-to-one on the referenced side in this extract: no row of %s is named by more than one row of %s. "
                       "No unique constraint on %s declares it." % (parent, child, cc))
        for cl in note.get("01", []):
            it.add(*cl)
        items["01"] = (it, note.get("summary_01") or
                       ("Many-to-one from %s to %s; up to %s rows of %s per row of %s." % (child, parent, n(ch["max"]), child, parent)
                        if ch and ch["max"] > 1 else
                        "%s to %s; at most one row of %s per row of %s in this extract." % (child, parent, child, parent) if ch else
                        "Declared from %s to %s, but no row refers in this extract." % (child, parent)))

        # ---------------------------------------------------------------- 02 meaning
        it = Item()
        if decl and decl["child_column"]["description"]:
            it.add("declared", "medium", "the description changes",
                   "The source describes %s as \"%s\"." % (C, decl["child_column"]["description"]))
        fl = r.get("child_rows_by_flags_of_person_named")
        if fl and not audit:
            emp = sum(v for k, v in fl.items() if "IsEmployee=1" in k)
            sal = sum(v for k, v in fl.items() if "IsSalesperson=1" in k)
            it.add("observed", "high", "every new extract",
                   "The people named: %s of %s rows name an employee of WWI (IsEmployee = 1), %s a salesperson, %s a person who is "
                   "not an employee." % (n(emp), n(r["child_filled"]), n(sal), n(r["child_filled"] - emp)))
        if audit:
            it.add("intended", "low", "a description is found",
                   "By the column's name: the join gives, for each row of %s, the person who last changed it; it says nothing of "
                   "who created the row or of earlier editors (see the column file LastEditedBy/02_meaning.md of %s)." % (child, child))
        for cl in note.get("02", []):
            it.add(*cl)
        if not it.claims or (len(it.claims) == 1 and it.claims[0][0] == "declared"):
            it.add("intended", "low", "a description is found",
                   "By the names: the join answers which row of %s is the one %s names for each row of %s." % (parent, cc, child))
        items["02"] = (it, note.get("summary_02") or (decl["child_column"]["description"] if decl and decl["child_column"]["description"] else
                                                      "What the join means is read from the names; see the claims."))

        # ---------------------------------------------------------------- 03 temporal (best effort)
        if trec:
            it = Item()
            summary = temporal_item(it, trec, child, parent, cc)
            for cl in note.get("03", []):
                it.add(*cl)
            items["03"] = (it, note.get("summary_03") or summary)

        # ---------------------------------------------------------------- 06 keys
        it = Item()
        if decl:
            cd = decl["child_column"]
            fk = decl["foreign_key"]
            it.add("declared", "high", "the foreign key changes",
                   "Child side: %s, %s, %s; a foreign key, %s; on delete %s." % (
                       C, cd["type_name"], "nullable" if cd["is_nullable"] == "1" else "not nullable",
                       "enabled and trusted" if fk["is_disabled"] == "0" and fk["is_not_trusted"] == "0" else "disabled or not trusted",
                       fk["delete_referential_action_desc"].replace("_", " ").lower()))
            it.add("declared", "high", "the primary key changes", "Parent side: %s, the declared primary key of %s." % (P, parent))
            alt = r["other_unique_parent_columns_accepting_all_values"]
            if r["child_distinct"]:
                if alt:
                    it.add("observed", "high", "every new extract",
                           "Ambiguous target: other unique columns of %s also hold every value of %s: %s." % (
                               parent, cc, ", ".join("%s (%s)" % (k, "declared unique" if v["declared_unique"] else "unique in this extract")
                                                     for k, v in sorted(alt.items()))))
                else:
                    it.add("observed", "high", "every new extract",
                           "No other column of %s that is unique in this extract holds all values of %s: the primary key is the only "
                           "key the values fit." % (parent, cc))
            if child == parent:
                it.add("declared", "high", "the foreign key changes",
                       "A self-reference: %s points to another row of the same table." % C)
        else:
            it.add("declared", "high", "a constraint is declared",
                   "Child side: %s, not declared as a foreign key; parent side: %s, not declared unique." % (C, P))
            it.add("observed", "high", "every new extract",
                   "In this extract %s is %s over all %s rows of %s." % (pc, "unique" if r["parent_combination_unique"] else "NOT unique",
                                                                         n(r["parent_rows"]), parent))
        for cl in note.get("06", []):
            it.add(*cl)
        items["06"] = (it, note.get("summary_06") or ("%s refers to the primary key %s%s." % (
            C, P, ", enforced" if decl and decl["foreign_key"]["is_not_trusted"] == "0" else "") if decl else
            "Undeclared: %s against %s, unique in this extract." % (C, P)))

        # ---------------------------------------------------------------- 07 population
        it = Item()
        it.add("observed", "high", "every new extract",
               "Orphans: %s rows of %s (%s distinct values) name no row of %s." % (n(r["orphan_rows"]), child, n(r["orphan_distinct"]), parent))
        if r["child_empty"]:
            it.add("observed", "high", "every new extract",
                   "Optional: %s is empty on %s of %s rows of %s%s." % (cc, n(r["child_empty"]), n(r["child_rows"]), child,
                                                                     ", as its declaration allows" if decl and decl["child_column"]["is_nullable"] == "1" else ""))
        else:
            it.add("observed", "high", "every new extract", "%s is filled on every row of %s." % (cc, child))
        it.add("observed", "high", "every new extract",
               "%s of %s rows of %s are named by no row of %s." % (n(r["parents_unreferenced"]), n(r["parent_rows"]), parent, child))
        tt = r.get("child_rows_by_transaction_type")
        if tt:
            it.add("observed", "high", "every new extract", "By transaction type: %s." % "; ".join(
                "%s (%s): %s %s" % (k.split("|")[0].split(" ", 1)[1], k.split(" ", 1)[0], n(v), k.split("|")[1]) for k, v in tt.items()))
        vis = r.get("extraction_visibility")
        if vis:
            same = all(v["rows_seen_by_owner"] == v["rows_seen_by_nsdn_reader"] == v["rows_in_extract"] for v in vis.values())
            it.add("observed", "high", "a security policy or a count difference appears",
                   "Extraction visibility: %s; masked columns: %s." % (
                       "; ".join("%s %s rows for the owner, %s for the extracting reader, %s in the extract" % (
                           t, n(v["rows_seen_by_owner"]), n(v["rows_seen_by_nsdn_reader"]), n(v["rows_in_extract"])) for t, v in sorted(vis.items())),
                       ", ".join("%s.%s" % (t, c) for t, v in sorted(vis.items()) for c in v["masked_columns"]) or "none"))
            it.add("declared", "unknown", "permission to read security policies is granted",
                   "Whether a row-level security policy filters either table is not established: the extracting reader sees %s "
                   "security policies and may lack the permission to see them; equal counts for owner and reader (%s) argue against a filter." % (
                       "no" if all(v["security_policies_visible_to_reader"] == 0 for v in vis.values()) else "some",
                       "as here" if same else "not the case here"))
        for cl in note.get("07", []):
            it.add(*cl)
        items["07"] = (it, note.get("summary_07") or "No orphans; %s empty; %s of %s %s rows unreferenced." % (
            n(r["child_empty"]), n(r["parents_unreferenced"]), n(r["parent_rows"]), parent))

        # ---------------------------------------------------------------- 27 peculiarities
        it = Item()
        warn = []
        if ch and ch["max"] > 1:
            it.add("observed", "high", "every new extract",
                   "Fan-out: joined from %s to %s, a %s row repeats up to %s times (median %s), so a measure of %s summed after the "
                   "join is counted once per referring row." % (parent, child, parent, n(ch["max"]), n(ch["median"]), parent))
            warn.append("fan-out")
        if decl and r["same_child_same_parent"]:
            it.add("declared", "high", "a foreign key changes",
                   "Several paths between the same two tables: %s also refers to %s through %s; a join of the two must say which "
                   "role it means." % (child, parent, ", ".join(r["same_child_same_parent"])))
            warn.append("roles")
        if decl and not audit:
            sib = ["%s (up to %s per parent)" % (x, n(m)) for x, m in sorted(r["other_children_of_parent"].items()) if m > 1]
            if ch and ch["max"] > 1 and sib:
                it.add("observed", "high", "every new extract",
                       "Chasm trap: %s also has other referring columns with several rows per parent (%s); joining %s and one of "
                       "these through %s pairs every row of one with every row of the other for the same parent." % (parent, ", ".join(sib), child, parent))
                warn.append("chasm")
        if decl and decl["parent_temporal_type"] == "SYSTEM_VERSIONED_TEMPORAL_TABLE" and not audit and r["child_filled"]:
            it.add("declared", "high", "the temporal type changes",
                   "%s is system-versioned and the extract holds its current versions: joined in the extract, a row of %s that "
                   "names a row of %s gets that row's attributes as they are on %s, not as they were when the referring row was "
                   "written; earlier versions are in the history table." % (parent, child, parent, DAY))
            warn.append("current versions")
        if decl and ch and ch["max"] == 1 and r["parents_referenced"] > 1:
            it.add("observed", "medium", "a second row refers to the same parent",
                   "One row of %s per row of %s holds only in this extract: nothing declares %s unique, so several referring rows "
                   "per parent are allowed, and a join that counts on one per parent rests on the extract." % (child, parent, cc))
            warn.append("one-to-one not enforced")
        if composite:
            hk = [k for k in r if k.startswith("rows_if_joined_on_") and k != "rows_if_joined_on_all_columns"][0]
            first = hk[len("rows_if_joined_on_"):-len("_only")]
            it.add("observed", "high", "every new extract",
                   "Header join: joined on %s alone, the two tables give %s rows instead of the %s that the full combination "
                   "gives: every referring row is paired with every row of %s for the same %s." % (
                       first, n(r[hk]), n(r["rows_if_joined_on_all_columns"]), parent, first))
            warn.append("header join")
        for route, a in sorted(r.get("two_routes_to_parent", {}).items()):
            if not a["rows_with_both_routes"]:
                continue
            via_col = route.rsplit(".", 1)[1]
            if a["disagree"] == 0:
                it.add("observed", "high", "every new extract",
                       "Two routes agree: on all %s rows where both are filled, %s names the same row of %s as the route %s: in this "
                       "extract %s repeats that value." % (n(a["rows_with_both_routes"]), cc, parent, route, cc))
                warn.append("copy")
            elif via_col == cc:
                it.add("observed", "high", "every new extract",
                       "Two routes disagree: %s names the same row of %s as the route %s on %s of %s rows, a different one on %s."
                       % (cc, parent, route, n(a["agree"]), n(a["rows_with_both_routes"]), n(a["disagree"])))
                warn.append("routes disagree")
        if audit:
            it.add("intended", "low", "a description is found",
                   "The relation records only the last edit; it cannot attribute a row's creation or earlier changes.")
        for cl in note.get("27", []):
            it.add(*cl)
            warn.append("see claims")
        if not it.claims:
            it.add("observed", "high", "every new extract", "None of the mechanical tests (fan-out, roles, chasm, versions, routes, "
                   "unenforced one-to-one) finds anything for this relation.")
        items["27"] = (it, note.get("summary_27") or ("Warnings: %s." % ", ".join(dict.fromkeys(warn)) if warn else "No warning."))

        # ---------------------------------------------------------------- write
        folder = os.path.join(REL_DIR, name)
        rid = ("wwi:fk:%s" % decl["foreign_key"]["fk_name"]) if decl else ("wwi:relation:%s" % name)
        for nn, (it, summary) in items.items():
            front = dict(notes.COMMON, id=rid, subject="wwi/across/relations/%s" % name, item=nn, topic=ia.ITEMS[nn],
                         tier="best-effort" if nn == "03" else "minimum", summary=ascii_only(summary), method=method,
                         input_schema_sha256=ia.relation_schema_hash(schema_sha(child), schema_sha(parent)),
                         recheck_when=ascii_only(note.get("recheck_" + nn, "every new extract, or a schema change of either table")))
            default = ("Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, "
                       "with their confidence.")
            if composite and nn == "27":
                default += (" The tests for roles, chasm traps, system-versioning and two routes are run on declared foreign keys "
                            "only; for this undeclared relation they were not run.")
            write_item(os.path.join(folder, "%s_%s.md" % (nn, ia.ITEMS[nn])), front, it.claims, evmap, observed,
                       note.get("reasoning_" + nn, default),
                       note.get("uncert_" + nn, "Whether row-level security filters either table: the claim with confidence unknown."
                                if nn == "07" and r.get("extraction_visibility") else ""))
            count += 1
    print("wrote", count, "relation item files for", len(rels), "relations")


if __name__ == "__main__":
    main(sys.argv)
