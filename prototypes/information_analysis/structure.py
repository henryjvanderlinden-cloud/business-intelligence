"""Item 29, position in the schema (ADR-0021; method in docs/10_architecture/131_structural-position.md).

Builds the graph of a source's tables - a node per base table, an arc per declared foreign key from the referring
table to the referenced one - and measures each table's position in it, twice: on all links, and without the links
that would distort the picture (by default the audit column LastEditedBy, which ties every table to the people table).
Adds volume and change from the extracts, assigns each table a class by the rules of 131, and lists which master tables
each event table reaches (the bus matrix). Writes one evidence file into analysis/<source>/_source/evidence/ and a copy
into each table's evidence folder; counts and catalogue metadata only.

    python prototypes/information_analysis/structure.py

Needs: the catalogue summaries in scratch/ia_profile/, and three extracts (two transitions) in data/raw/<source>/.
"""
import collections
import inspect
import json
import os
import shutil
import sys

import networkx as nx

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from evidence_orders import blob, sha, now  # noqa: E402
from relations import write_evidence, load_catalogues  # noqa: E402
import recheck  # noqa: E402
import profile_tables as pt  # noqa: E402
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import ia_lib as ia  # noqa: E402

SCRIPT = "prototypes/information_analysis/structure.py"
SOURCE = "wwi"
RAW = os.path.join(ROOT, "data", "raw", SOURCE)
DAYS = ["2016-05-31", "2016-06-01", "2016-06-02"]          # three extracts, two transitions
BASE = "2016-06-01"                                        # the extract the record describes
# Links that distort the picture, left out of the second graph, with the reason (131, "Distortion check").
EXCLUDE = {"LastEditedBy": "audit column: every table names the person who last changed a row, which makes the people "
                           "table the centre of the graph for a reason that says nothing about the business"}
AUDIT = {"LastEditedBy", "LastEditedWhen", "ValidFrom", "ValidTo"}   # audit and system-time columns, not business values
HUB_BETWEENNESS = 0.1                                      # 131: a heuristic threshold, recorded with the result
LOOKUP_MAX_DESCRIPTIVE = 2


def links(cats, exclude):
    out = []
    for t, d in cats.items():
        for k in d["catalogue"]["foreign_keys_out"]:
            if k["column_name"] in exclude:
                continue
            out.append((t, k["column_name"], "%s.%s" % (k["ref_schema"], k["ref_table"])))
    return out


def measures(cats, rows_of, filled, exclude):
    """Position measures of every table on the graph without the excluded link columns."""
    L = links(cats, exclude)
    G = nx.DiGraph()
    G.add_nodes_from(cats)
    for c, col, p in L:
        if c != p:
            G.add_edge(c, p)
    U = G.to_undirected()
    bt = nx.betweenness_centrality(U)
    pr = nx.pagerank(G)
    out = {}
    for t in cats:
        ins = [(c, col) for c, col, p in L if p == t and c != t]      # from other tables (131 section 4)
        selfs = [col for c, col, p in L if p == t and c == t]
        outs = [(col, p) for c, col, p in L if c == t]
        tin, tout = {c for c, _ in ins if c != t}, {p for _, p in outs if p != t}
        desc = nx.descendants(G, t)
        longest = max((len(p) - 1 for x in desc for p in nx.all_simple_paths(G, t, x)), default=0)
        out[t] = {
            "links_in": len(ins), "links_out": len(outs), "tables_in": len(tin), "tables_out": len(tout),
            "self_references": selfs,
            "position": "isolated" if not tin and not tout else "source" if not tin else "sink" if not tout else "middle",
            "betweenness": round(bt[t], 4), "pagerank": round(pr[t], 4),
            "roles": len(ins), "rows_referring": sum(filled[(c, col)] for c, col in ins),
            "reaches": len(desc), "reached_by": len(nx.ancestors(G, t)), "longest_path_out": longest}
    order = sorted(cats, key=lambda t: -out[t]["betweenness"])
    for i, t in enumerate(order, 1):
        out[t]["betweenness_rank"] = i
    return out, nx.number_connected_components(U), sorted(sorted(c) for c in nx.connected_components(U) if len(c) == 1)


def business_updates(t, pk, prev, day):
    """Rows present in both extracts whose values differ in a column other than the key and the audit columns
    (131 section 3, point 5), and the rows in the later extract."""
    def load(x):
        f, head, rows = pt.reader(x, t)
        idx = [head.index(k) for k in pk]
        out = {tuple(r[i] for i in idx): r for r in rows}
        f.close()
        return head, out
    ha, a = load(prev)
    hb, b = load(day)
    if ha != hb:
        return None
    keep = [i for i, c in enumerate(hb) if c not in AUDIT and c not in pk]
    return {"rows": sum(1 for k in a if k in b and any(a[k][i] != b[k][i] for i in keep)), "rows_to": len(b)}


def classify(t, d, m, tr, rows_of):
    """The class of a table by the rules of 131, in order; returns (class, rule that fired, behaviour)."""
    c = d["catalogue"]
    cols = [x["column_name"] for x in c["columns"]]
    pk = [k["column_name"] for k in c["keys"] if k["is_primary_key"] == "1"]
    fkcols = {k["column_name"] for k in c["foreign_keys_out"]}
    descriptive = [x for x in cols if x not in pk and x not in fkcols and x not in AUDIT]
    t1, t2 = tr

    def business(x):   # rows updated in a column other than the key and the audit columns (131, distortion check)
        return (x.get("business_updates") or {}).get("rows", 0)
    grows = all(x.get("inserted", 0) > 0 and x.get("deleted", 0) == 0 for x in (t1, t2))
    replaced = all(x.get("inserted", 0) > 0 and x.get("inserted") == x.get("deleted") for x in (t1, t2))
    updated_all = all(x.get("business_updates") and business(x) == x["business_updates"]["rows_to"] > 0 for x in (t1, t2))
    static = all(not (x.get("inserted") or x.get("updated") or x.get("deleted")) for x in (t1, t2))
    audit_only = all(not (x.get("inserted") or x.get("deleted")) and business(x) == 0 and x.get("business_updates") for x in (t1, t2))
    behaviour = ("grows" if grows else "replaced daily" if replaced else "every row updated daily" if updated_all
                 else "unchanged" if static else "only audit or system-time columns change" if audit_only
                 else "changes without growing")
    pk_is_fk = bool(pk) and all(p in fkcols for p in pk) and len({k["ref_table"] for k in c["foreign_keys_out"] if k["column_name"] in pk}) == 1
    if c["table"][0]["temporal_type_desc"] == "HISTORY_TABLE":
        return "history", "a history table of system-versioning", behaviour, descriptive
    if rows_of[t] == 1 and m["tables_in"] == 0:
        return "configuration", "one row, referred to by no table", behaviour, descriptive
    if m["tables_in"] == 0 and m["tables_out"] >= 2 and not descriptive:
        return "bridge", "refers to two or more tables, is referred to by none, has no attribute besides keys and audit columns", behaviour, descriptive
    if m["tables_in"] == 0 and pk_is_fk:
        return "extension", "its primary key is a foreign key to one parent: at most one row per parent row", behaviour, descriptive
    if grows:
        return "event", "rows are added in both transitions and none deleted", behaviour, descriptive
    if replaced:
        return "state", "its rows are replaced in both transitions without growing", behaviour, descriptive
    if m["tables_out"] == 0 and len(descriptive) <= LOOKUP_MAX_DESCRIPTIVE:
        return "lookup", "refers to no table and has at most %d attributes besides keys and audit columns" % LOOKUP_MAX_DESCRIPTIVE, behaviour, descriptive
    return "master", "none of the rules above: does not grow, and has attributes or references of its own", behaviour, descriptive


def history_tables(cats):
    """The history tables of system-versioning: outside the graph (they carry no declared keys), class history by rule 1
    of 131; their rows in each extract, from the manifests."""
    owner = {d["catalogue"]["table"][0]["history_table"]: t for t, d in cats.items() if d["catalogue"]["table"][0]["history_table"]}
    rows = {}
    for day in DAYS:
        with open(os.path.join(RAW, day, "manifest.json"), encoding="utf-8") as fh:
            rows[day] = {f["table"]: f["rows"] for f in json.load(fh)["files"]}
    out = {}
    for f in sorted(os.listdir(os.path.join(ROOT, "scratch", "ia_profile"))):
        with open(os.path.join(ROOT, "scratch", "ia_profile", f), encoding="utf-8") as fh:
            d = json.load(fh)
        if d["catalogue"]["table"][0]["temporal_type_desc"] != "HISTORY_TABLE":
            continue
        t = f[:-5]
        n = [rows[day][t] for day in DAYS]
        out[t] = {"history_of": owner.get(t), "declared_links_out": len(d["catalogue"]["foreign_keys_out"]),
                  "declared_links_in": len(d["catalogue"]["foreign_keys_in"]), "rows_by_extract": dict(zip(DAYS, n)),
                  "behaviour": "rows added in both transitions" if n[0] < n[1] < n[2] else "row count unchanged" if n[0] == n[1] == n[2]
                  else "row count changes",
                  "class": "history", "rule": "a history table of system-versioning"}
    return out


def compute():
    cats = load_catalogues()
    rows_of = {t: d["profile"]["rows"] for t, d in cats.items()}
    filled = {}
    for t, d in cats.items():
        for k in d["catalogue"]["foreign_keys_out"]:
            filled[(t, k["column_name"])] = d["profile"]["rows"] - d["profile"]["columns"][k["column_name"]]["empty"]
    full, comp_full, iso_full = measures(cats, rows_of, filled, set())
    clean, comp_clean, iso_clean = measures(cats, rows_of, filled, set(EXCLUDE))
    t1 = recheck.run("transitions", DAYS[1], DAYS[0])
    t2 = recheck.run("transitions", DAYS[2], DAYS[1])
    for t, d in cats.items():
        pk = [k["column_name"] for k in d["catalogue"]["keys"] if k["is_primary_key"] == "1"]
        for tr, (prev, day) in ((t1, DAYS[0:2]), (t2, DAYS[1:3])):
            if tr.get(t) and tr[t].get("updated"):
                tr[t]["business_updates"] = business_updates(t, pk, prev, day)
    tables = {}
    for t, d in cats.items():
        cls, rule, behaviour, descriptive = classify(t, d, clean[t], (t1.get(t, {}), t2.get(t, {})), rows_of)
        parent = None
        if cls == "extension":
            parent = "%s.%s" % next((k["ref_schema"], k["ref_table"]) for k in d["catalogue"]["foreign_keys_out"] if k["column_name"] not in EXCLUDE)
        tables[t] = {"rows": rows_of[t], "extension_of": parent, "parent_rows": rows_of.get(parent), "temporal": d["catalogue"]["table"][0]["temporal_type_desc"],
                     "descriptive_columns": len(descriptive), "transition_1": t1.get(t), "transition_2": t2.get(t),
                     "all_links": full[t], "without_excluded": clean[t], "class": cls, "rule": rule, "behaviour": behaviour}
    for t, v in tables.items():
        if v["class"] == "event":
            v["event_kind"] = "header" if any(tables[c]["class"] == "event" for c, _, p in links(cats, set(EXCLUDE)) if p == t) else "record"
    hist = history_tables(cats)
    for v in hist.values():   # 131 section 2: a history table takes the position of the table it keeps versions of
        o = tables.get(v["history_of"])
        v["owner"] = {"class": o["class"], "position": o["without_excluded"]["position"],
                      "betweenness_rank": o["without_excluded"]["betweenness_rank"]} if o else None
    G = nx.DiGraph()
    for c, _, p in links(cats, set(EXCLUDE)):
        if c != p:
            G.add_edge(c, p)
    masters = sorted(t for t, v in tables.items() if v["class"] == "master")
    bus = {t: sorted(m for m in masters if G.has_node(t) and m in nx.descendants(G, t))
           for t, v in sorted(tables.items()) if v["class"] in ("event", "state")}
    return {"days": DAYS, "base": BASE, "excluded_links": EXCLUDE, "hub_betweenness_threshold": HUB_BETWEENNESS,
            "graph_all_links": {"links": len(links(cats, set())), "components": comp_full, "isolated": iso_full},
            "graph_without_excluded": {"links": len(links(cats, set(EXCLUDE))), "components": comp_clean, "isolated": iso_clean},
            "tables": tables, "bus_matrix": bus, "masters": masters, "history_tables": hist}


def main():
    res = compute()
    rec = {"kind": "profile", "tool": SCRIPT, "tool_version": blob(SCRIPT), "ran_at": now(),
           "code": "\n".join(inspect.getsource(f) for f in (links, measures, business_updates, classify, history_tables, compute)),
           "inputs": {"source": SOURCE, "extracts": {d: sha(os.path.join(RAW, d, "manifest.json")) for d in DAYS},
                      "catalogue": "scratch/ia_profile/*.json (catalogue and profile of the base extract)"},
           "result": res}
    h = write_evidence(os.path.join(ROOT, "analysis", SOURCE, "_source", "evidence"), rec)
    src = os.path.join(ROOT, "analysis", SOURCE, "_source", "evidence", h + ".json")
    for t in list(res["tables"]) + list(res["history_tables"]):
        s, n = t.split(".")
        d = os.path.join(ROOT, "analysis", SOURCE, "tables", ia.escape(s), ia.escape(n), "evidence")
        os.makedirs(d, exist_ok=True)
        shutil.copyfile(src, os.path.join(d, h + ".json"))
    print(h)
    for t, v in sorted(res["tables"].items(), key=lambda kv: (kv[1]["class"], kv[0])):
        w = v["without_excluded"]
        print("%-36s %-13s %-8s %-7s bt %.3f in %d/%d out %d/%d roles %d reach %d" % (
            t, v["class"], v.get("event_kind", ""), w["position"], w["betweenness"], w["tables_in"], w["links_in"], w["tables_out"], w["links_out"], w["roles"], w["reaches"]))
    print(json.dumps(res["bus_matrix"], indent=0))


if __name__ == "__main__":
    main()
