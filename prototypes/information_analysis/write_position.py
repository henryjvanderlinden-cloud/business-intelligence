"""Write item 29, position in the schema (ADR-0021, method in docs/10_architecture/131_structural-position.md): one
29_position.md per base table and one for the source, from structure.py's evidence plus readings from a notes module.

    python prototypes/information_analysis/write_position.py <notes module> [<source>, default wwi]
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

TOOL = "prototypes/information_analysis/structure.py"


def n(x):
    if isinstance(x, float) and x.is_integer():
        x = int(x)
    return format(x, ",")


def latest(src):
    best = None
    for f in os.listdir(os.path.join(src, "evidence")):
        with open(os.path.join(src, "evidence", f), encoding="utf-8") as fh:
            rec = json.load(fh)
        if rec.get("tool") == TOOL and (best is None or rec["ran_at"] > best["ran_at"]):
            best = rec
    return best


def tr(x):
    return "%s inserted, %s updated, %s deleted" % (n(x.get("inserted", 0)), n(x.get("updated", 0)), n(x.get("deleted", 0))) if x else "not compared"


def write(path, front, claims, h, notes, reasoning, uncert):
    conf = ia.CONFIDENCE[min(ia.CONFIDENCE.index(c[1]) for c in claims)]
    lines = ["- C%d | type=%s | status=proposed | confidence=%s | effective=%s | observed=%s | checked=%s | evidence=%s | recheck=%s | text: %s"
             % (i, typ, cf, notes.BASE, notes.NOW[:10], notes.NOW[:10], h if ev else "none", rc, t) for i, (typ, cf, ev, rc, t) in enumerate(claims, 1)]
    front = dict(front, confidence=conf, claims=str(len(claims)))
    txt = ("---\n" + "\n".join("%s: %s" % (k, front[k]) for k in ia.FRONT_KEYS) + "\n---\n\n## Claims\n\n" + "\n".join(lines) +
           "\n\n## Reasoning\n\n" + reasoning + "\n\n## Uncertainties\n\n" + (uncert or "None.") + "\n\n## For a person\n\nNone.\n")
    assert all(ord(ch) < 128 for ch in txt), path
    with open(path, "w", encoding="ascii", newline="\n") as f:
        f.write(txt)


def main(argv):
    sp = importlib.util.spec_from_file_location("notes", argv[1])
    notes = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(notes)
    source = argv[2] if len(argv) > 2 else "wwi"
    SRC = os.path.join(ROOT, "analysis", source, "_source")
    rec = latest(SRC)
    h, r = rec["id"], rec["result"]
    method = "measures by %s (blob %s), claims by write_position.py (blob %s); method docs/10_architecture/131_structural-position.md; readings by %s" % (
        TOOL, rec["tool_version"], blob("prototypes/information_analysis/write_position.py"), notes.COMMON["written_by"])
    excl = ", ".join(r["excluded_links"])
    inputs = dict(input_extract=r["base"], input_manifest_sha256=rec["inputs"]["extracts"][r["base"]], last_checked_against=r["days"][-1])
    T = r["tables"]
    total = len(T)
    for t, v in T.items():
        a, w = v["all_links"], v["without_excluded"]
        c = [("declared", "high", True, "a foreign key changes",
              "On all %s declared links between the %s base tables: referred to by %s link(s) from %s other table(s), refers by %s link(s) to %s other table(s)%s." % (
                  r["graph_all_links"]["links"], total, a["links_in"], a["tables_in"], a["links_out"], a["tables_out"],
                  "; self-reference through %s" % ", ".join(a["self_references"]) if a["self_references"] else "")),
             ("declared", "high", True, "a foreign key changes",
              "Without the links of %s (131, distortion check): referred to by %s link(s) from %s other table(s), refers by %s link(s) to %s other table(s); position: %s%s." % (
                  excl, w["links_in"], w["tables_in"], w["links_out"], w["tables_out"], w["position"],
                  "; self-reference through %s" % ", ".join(w["self_references"]) if w["self_references"] else "")),
             ("observed", "high", True, "a foreign key changes, or every new extract",
              "Measures without those links: betweenness %s (rank %s of %s; %s with all links), %s role(s) in which other tables name it, %s rows naming it, "
              "reaches %s table(s) by following links (longest path %s), reached from %s table(s)." % (
                  w["betweenness"], w["betweenness_rank"], total, a["betweenness"], w["roles"], n(w["rows_referring"]), w["reaches"],
                  w["longest_path_out"], w["reached_by"])),
             ("observed", "high", True, "every new extract",
              "%s rows on %s, %s attribute(s) besides keys and audit columns; %s to %s: %s; %s to %s: %s; behaviour: %s." % (
                  n(v["rows"]), r["base"], v["descriptive_columns"], r["days"][0], r["days"][1], tr(v["transition_1"]),
                  r["days"][1], r["days"][2], tr(v["transition_2"]), v["behaviour"])),
             ("intended", "high", True, "a rule of 131 or a foreign key changes",
              "Class by the rules of 131: %s (rule: %s). The rule rests on the catalogue and the row count, not on behaviour." % (v["class"], v["rule"]))
             if v["class"] in ("configuration", "bridge", "extension") else
             ("intended", "medium", True, "a rule of 131 or the behaviour changes",
              "Class by the rules of 131: %s%s (rule: %s). Medium: the behaviour rests on two transitions." % (
                  v["class"], " (%s)" % v["event_kind"] if v.get("event_kind") else "", v["rule"]))]
        ups = [(r["days"][i], r["days"][i + 1], x) for i, x in enumerate((v["transition_1"], v["transition_2"])) if x and x.get("updated")]
        if ups:
            c.append(("observed", "high", True, "every new extract",
                      "Rows updated, by changed column: %s.%s" % ("; ".join("%s to %s, %s row(s) (%s), of which %s changed in a column other than the key and the audit columns" % (
                          a_, b_, n(x["updated"]), ", ".join("%s %s" % (k, n(m_)) for k, m_ in sorted(x["updated_columns"].items())),
                          n((x.get("business_updates") or {}).get("rows", 0))) for a_, b_, x in ups),
                          " The class event says that rows are added; it does not say that rows, once added, stay as they are." if v["class"] == "event" else "")))
        if v.get("extension_of"):
            c.append(("observed", "high", True, "every new extract",
                      "Its primary key is a foreign key to %s, so it has at most one row per row there; it has %s rows for %s there." % (
                          v["extension_of"], n(v["rows"]), n(v["parent_rows"]))))
        if w["betweenness"] >= r["hub_betweenness_threshold"]:
            c.append(("observed", "high", True, "a foreign key changes",
                      "A hub: betweenness %s is at or above the threshold %s of 131; it lies on many of the shortest paths between other tables." % (
                          w["betweenness"], r["hub_betweenness_threshold"])))
        note = notes.TABLES.get(t, {})
        c += note.get("claims", [])
        s, nm = t.split(".")
        d = os.path.join(ROOT, "analysis", source, "tables", ia.escape(s), ia.escape(nm))
        prof = json.load(open(os.path.join(ROOT, "scratch", "ia_profile", t + ".json")))
        front = dict(notes.COMMON, id="%s:object:%s" % (source, prof["catalogue"]["table"][0]["object_id"]), subject="%s/tables/%s/%s" % (source, ia.escape(s), ia.escape(nm)),
                     item="29", topic="position", tier="best-effort", method=method, input_schema_sha256=prof["profile"]["schema_sha256"],
                     summary=note.get("summary") or "%s, %s%s; betweenness rank %s of %s; %s." % (
                         v["class"].capitalize(), w["position"], " (%s)" % v["event_kind"] if v.get("event_kind") else "", w["betweenness_rank"], total, v["behaviour"]),
                     recheck_when="a foreign key changes, or every new extract", **inputs)
        write(os.path.join(d, "29_position.md"), front, c, h, notes, note.get("reasoning", notes.TABLE_REASONING), note.get("uncertainties", ""))
    # the history tables: outside the graph
    for t, v in r["history_tables"].items():
        s, nm = t.split(".")
        d = os.path.join(ROOT, "analysis", source, "tables", ia.escape(s), ia.escape(nm))
        rows = v["rows_by_extract"]
        c = [("declared", "high", True, "a foreign key changes",
              "Declares %s foreign key(s) and is referred to by %s: it is not a node of the graph of 131, whose links are declared foreign keys." % (
                  v["declared_links_out"], v["declared_links_in"])),
             ("observed", "high", True, "every new extract",
              "Rows: %s. Behaviour: %s." % ("; ".join("%s on %s" % (n(x), day) for day, x in rows.items()), v["behaviour"])),
             ("declared", "high", True, "a rule of 131 or the schema changes",
              "Class by the rules of 131: history (rule 1, %s); it keeps the earlier versions of %s and takes that table's position: %s, %s, betweenness rank %s (%s/29_position.md)." % (
                  v["rule"], v["history_of"], v["owner"]["class"], v["owner"]["position"], v["owner"]["betweenness_rank"],
                  "../../%s/%s" % (ia.escape(v["history_of"].split(".")[0]), ia.escape(v["history_of"].split(".")[1]))))]
        note = notes.TABLES.get(t, {})
        c += note.get("claims", [])
        prof = json.load(open(os.path.join(ROOT, "scratch", "ia_profile", t + ".json")))
        front = dict(notes.COMMON, id="%s:object:%s" % (source, prof["catalogue"]["table"][0]["object_id"]), subject="%s/tables/%s/%s" % (source, ia.escape(s), ia.escape(nm)),
                     item="29", topic="position", tier="best-effort", method=method, input_schema_sha256=prof["profile"]["schema_sha256"],
                     summary="History of %s, outside the graph; %s." % (v["history_of"], v["behaviour"]),
                     recheck_when="a foreign key changes, or every new extract", **inputs)
        write(os.path.join(d, "29_position.md"), front, c, h, notes, note.get("reasoning", notes.HISTORY_REASONING), note.get("uncertainties", ""))
    # the source as a whole
    ppl = T["Application.People"]
    hubs = sorted((t for t in T if T[t]["without_excluded"]["betweenness"] >= r["hub_betweenness_threshold"]), key=lambda t: -T[t]["without_excluded"]["betweenness"])
    classes = {}
    for t, v in T.items():
        classes.setdefault(v["class"], []).append(t)
    top_pr = max(T, key=lambda t: T[t]["without_excluded"]["pagerank"])
    bus = r["bus_matrix"]
    reach = {m: sum(1 for e in bus if m in bus[e]) for m in r["masters"]}
    c = [("declared", "high", True, "a foreign key changes",
          "The graph: %s base tables, %s declared links, of which %s are %s; %s connected components, the isolated tables being %s." % (
              total, r["graph_all_links"]["links"], r["graph_all_links"]["links"] - r["graph_without_excluded"]["links"], excl,
              r["graph_without_excluded"]["components"], ", ".join(x[0] for x in r["graph_without_excluded"]["isolated"]))),
         ("observed", "high", True, "a foreign key changes",
          "Distortion check: with all links Application.People is referred to by %s links from %s tables and has betweenness %s (rank %s); without %s, by %s links from %s tables, betweenness %s (rank %s)." % (
              ppl["all_links"]["links_in"], ppl["all_links"]["tables_in"], ppl["all_links"]["betweenness"],
              sorted(T, key=lambda t: -T[t]["all_links"]["betweenness"]).index("Application.People") + 1, excl,
              ppl["without_excluded"]["links_in"], ppl["without_excluded"]["tables_in"], ppl["without_excluded"]["betweenness"], ppl["without_excluded"]["betweenness_rank"])),
         ("observed", "high", True, "a foreign key changes",
          "Hubs (betweenness at or above %s without the excluded links): %s." % (
              r["hub_betweenness_threshold"], "; ".join("%s %s" % (t, T[t]["without_excluded"]["betweenness"]) for t in hubs))),
         ("observed", "high", True, "a foreign key changes",
          "PageRank on the referring-to-referenced direction ranks %s first (%s): a sink at the end of a chain collects the rank of the chain, so PageRank is reported but not used to find hubs (131)." % (
              top_pr, T[top_pr]["without_excluded"]["pagerank"])),
         ("intended", "medium", True, "a rule of 131 or the behaviour changes",
          "Classes by the rules of 131: %s; and history %s (the _Archive tables, outside the graph)." % (
              "; ".join("%s %s (%s)" % (k, len(v), ", ".join(sorted(v))) for k, v in sorted(classes.items())), len(r["history_tables"]))),
         ("observed", "high", True, "a foreign key changes",
          "Reach matrix - the master tables each event or state table reaches by following links: %s. Masters by the number of these %s tables that reach them: %s." % (
              "; ".join("%s: %s" % (e, ", ".join(m) or "none") for e, m in bus.items()), len(bus),
              "; ".join("%s %s" % (m, reach[m]) for m in sorted(reach, key=lambda m: -reach[m]))))]
    c += notes.SOURCE_CLAIMS
    front = dict(notes.COMMON, id="%s:source:position" % source, subject="%s/_source" % source, item="29", topic="position", tier="best-effort", method=method,
                 input_schema_sha256="none", summary=notes.SOURCE_SUMMARY, recheck_when="a foreign key changes, or every new extract", **inputs)
    write(os.path.join(SRC, "29_position.md"), front, c, h, notes, notes.SOURCE_REASONING, notes.SOURCE_UNCERTAINTIES)
    print("wrote", len(T) + len(r["history_tables"]) + 1, "position files")


if __name__ == "__main__":
    main(sys.argv)
