"""Round-1 evidence for every table of a WWI extract (ADR-0017 to ADR-0019, analysis/README.md section 7).

For each table it writes, into analysis/wwi/tables/<schema>/<table>/evidence/, content-addressed and write-once:
  catalogue   - the table's rows from the catalogue queries (columns, keys, foreign keys out and in, checks, masks,
                temporal type, description) and the row counts seen by owner and by nsdn_reader (R15);
  profile     - per column: empties, distinct values, numeric range and sign, date time-parts, structured content;
                key uniqueness and gaps; empty-column patterns; low-cardinality columns with their empty pattern per
                value (item 27 test 8); functional dependencies between non-key columns (test 1);
  transition  - the previous extract against this one, by primary key: inserted, deleted, updated, columns updated.
It also writes scratch/ia_profile/<schema>.<table>.json, the same results in one file per table, for drafting.
Aggregates only; low-cardinality value counts are kept only for columns with at most 12 distinct values.

    python prototypes/information_analysis/profile_tables.py [Schema.Table ...]
"""
import collections
import csv
import gzip
import inspect
import json
import os
import sys
import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ia_lib as ia  # noqa: E402
from evidence_orders import blob, sha, now  # noqa: E402

RAW = os.path.join(ROOT, "data", "raw", "wwi")
RESP = os.path.join(ROOT, "data", "wwi", "responses")
PROC = os.path.join(ROOT, "data", "wwi", "processed")
SCRIPT = "prototypes/information_analysis/profile_tables.py"
DAY, PREV = os.environ.get("IA_DAY", "2016-06-01"), os.environ.get("IA_PREV", "2016-05-31")   # recheck.py sets them
CAT = {"columns": "20261018T1301-agent-ia-cat-columns", "keys": "20261018T1302-agent-ia-cat-keys",
       "fks": "20261018T1303-agent-ia-cat-fks", "tables": None, "checks": "20261018T1301-agent-ia-cat-checks",
       "masked": None, "reader_counts": None, "rls": "20261018T1240-agent-ia-rls"}
STATUS = "20261018T1218-agent-status"
BIG = 1000000          # tables above this many rows get the streaming profile only
FD_MAX_ROWS = 300000
TOOL_VERSION = None
csv.field_size_limit(2 ** 31 - 1)


def find(tag):
    hits = sorted(f for f in os.listdir(RESP) if f.endswith("-agent-ia-%s.json" % tag))
    for h in reversed(hits):
        with open(os.path.join(RESP, h), encoding="utf-8-sig") as f:
            if json.load(f).get("status") == "ok":
                return h[:-5]
    return None


def cat_rows(rid):
    with open(os.path.join(RESP, rid + ".csv"), encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def cat_query(rid):
    with open(os.path.join(PROC, rid + ".json"), encoding="utf-8") as f:
        return json.load(f)["sql"]


def cat_ran(rid):
    with open(os.path.join(RESP, rid + ".json"), encoding="utf-8-sig") as f:
        return json.load(f)["finished_at"]


def write(out_dir, record):
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


def reader(day, table):
    f = gzip.open(os.path.join(RAW, day, table + ".csv.gz"), "rt", encoding="utf-8", newline="")
    r = csv.reader(f)
    return f, next(r), r


def as_num(v):
    try:
        return float(v)
    except ValueError:
        return None


def profile(table, pk):
    """Profile one table of the extract DAY; pk is the list of primary-key columns from the catalogue."""
    f, head, rows = reader(DAY, table)
    rows = list(rows)
    f.close()
    n = len(rows)
    idx = {c: i for i, c in enumerate(head)}
    out = {"rows": n, "columns": {}}
    for c, i in idx.items():
        vals = [r[i] for r in rows]
        nonempty = [v for v in vals if v != ""]
        d = {"empty": n - len(nonempty), "distinct": len(set(vals))}
        nums = [x for x in (as_num(v) for v in nonempty) if x is not None]
        if nonempty and len(nums) == len(nonempty):
            d["numeric"] = {"min": min(nums), "max": max(nums), "negative": sum(1 for x in nums if x < 0),
                            "zero": sum(1 for x in nums if x == 0), "positive": sum(1 for x in nums if x > 0),
                            "non_integer": sum(1 for x in nums if x != int(x))}
        elif nonempty:
            d["min"], d["max"] = min(nonempty)[:60], max(nonempty)[:60]
        dated = [v for v in nonempty if len(v) >= 19 and v[4] == "-" and v[10] == "T"]
        if nonempty and len(dated) == len(nonempty):
            d["time_parts"] = dict(collections.Counter(v[10:19] for v in dated).most_common(3))
            d["time_parts_distinct"] = len(set(v[10:] for v in dated))
            d["far_future"] = sum(1 for v in dated if v.startswith("9999"))
        js = [v for v in nonempty if v[:1] in "{["]
        if js:
            ok, sizes = 0, collections.Counter()
            for v in js:
                try:
                    o = json.loads(v)
                    ok += 1
                    if isinstance(o, list):
                        sizes["list:%d" % len(o)] += 1
                    elif isinstance(o, dict):
                        sizes["keys:" + ",".join(sorted(o.keys()))[:120]] += 1
                except ValueError:
                    pass
            d["json"] = {"rows": len(js), "parsed": ok, "shapes": dict(sizes.most_common(5))}
        wkt = sum(1 for v in nonempty if v.split(" ")[0] in ("POINT", "POLYGON", "MULTIPOLYGON", "LINESTRING"))
        if wkt:
            d["geometry_rows"] = wkt
        if d["distinct"] <= 12:
            d["values"] = dict(collections.Counter(vals).most_common(12))
        out["columns"][c] = d
    if pk and all(k in idx for k in pk):
        keys = [tuple(r[idx[k]] for k in pk) for r in rows]
        out["pk"] = {"columns": pk, "distinct": len(set(keys)), "empty": sum(1 for k in keys if "" in k)}
        if len(pk) == 1:
            ints = [int(k[0]) for k in keys if k[0].lstrip("-").isdigit()]
            if ints and len(ints) == n:
                out["pk"].update({"min": min(ints), "max": max(ints), "gaps": max(ints) - min(ints) + 1 - len(set(ints))})
    sig = collections.Counter(tuple(c for c in head if r[idx[c]] == "") for r in rows)
    out["empty_patterns"] = [{"empty": list(k), "rows": v} for k, v in sig.most_common(8)]
    out["empty_patterns_distinct"] = len(sig)
    low = [c for c in head if 1 < out["columns"][c]["distinct"] <= 12 and c not in pk]
    per = {}
    for c in low:
        by = collections.defaultdict(lambda: collections.Counter())
        cnt = collections.Counter()
        for r in rows:
            v = r[idx[c]]
            cnt[v] += 1
            for o in head:
                if r[idx[o]] == "":
                    by[v][o] += 1
        varying = {}
        for o in head:
            counts = {v: by[v][o] for v in cnt}
            kinds = set("none" if counts[v] == 0 else "all" if counts[v] == cnt[v] else "some" for v in cnt)
            if len(kinds) > 1 or kinds == {"some"}:
                varying[o] = counts
        if varying:
            per[c] = {"rows_per_value": dict(cnt), "empty_rows_by_value": varying}
    out["empty_rows_by_low_cardinality_value"] = per
    fds = []
    if n <= FD_MAX_ROWS:
        live = [c for c in head if c not in pk and 1 < out["columns"][c]["distinct"] < n]
        for x in live:
            xi = idx[x]
            for y in head:
                if y == x or y in pk or out["columns"][y]["distinct"] <= 1:
                    continue
                yi, m, ok = idx[y], {}, True
                for r in rows:
                    if m.setdefault(r[xi], r[yi]) != r[yi]:
                        ok = False
                        break
                if ok:
                    fds.append("%s -> %s" % (x, y))
    out["functional_dependencies"] = fds if n <= FD_MAX_ROWS else "not computed: too many rows"
    out["column_names_with_trailing_digits"] = [c for c in head if c[-1:].isdigit()]
    out["schema_sha256"] = ia.schema_hash(head)
    return out


def profile_big(table, pk):
    """Streaming profile for very large tables: counts, empties, ranges and distinct of the key's first column."""
    f, head, rows = reader(DAY, table)
    idx = {c: i for i, c in enumerate(head)}
    n, empty = 0, collections.Counter()
    lo, hi = {}, {}
    first = set()
    for r in rows:
        n += 1
        for c, i in idx.items():
            v = r[i]
            if v == "":
                empty[c] += 1
            else:
                if c not in lo or v < lo[c]:
                    lo[c] = v
                if c not in hi or v > hi[c]:
                    hi[c] = v
        first.add(r[0])
    f.close()
    return {"rows": n, "streaming_profile": True, "first_column": head[0], "first_column_distinct": len(first),
            "columns": {c: {"empty": empty[c], "min": lo.get(c, "")[:60], "max": hi.get(c, "")[:60]} for c in head},
            "schema_sha256": ia.schema_hash(head)}


def transition(table, pk):
    """Compare the previous extract with this one by primary key."""
    def load(day):
        f, head, rows = reader(day, table)
        idx = [head.index(k) for k in pk]
        d = {tuple(r[i] for i in idx): r for r in rows}
        f.close()
        return head, d
    ha, a = load(PREV)
    hb, b = load(DAY)
    if ha != hb:
        return {"columns_changed": True}
    changed = [k for k in a if k in b and a[k] != b[k]]
    return {"rows_from": len(a), "rows_to": len(b), "inserted": sum(1 for k in b if k not in a),
            "deleted": sum(1 for k in a if k not in b), "updated": len(changed),
            "updated_columns": dict(collections.Counter(
                hb[i] for k in changed for i in range(len(hb)) if a[k][i] != b[k][i]))}


def main(argv):
    global TOOL_VERSION
    TOOL_VERSION = blob(SCRIPT)
    for k in ("tables", "masked", "reader_counts"):
        CAT[k] = CAT[k] or find({"tables": "cat-tables", "masked": "cat-masked", "reader_counts": "cat-reader-counts"}[k])
    missing = [k for k, v in CAT.items() if not v]
    if missing:
        sys.exit("catalogue responses missing: %s" % missing)
    rows = {k: cat_rows(v) for k, v in CAT.items()}
    with open(os.path.join(RESP, STATUS + ".json"), encoding="utf-8-sig") as f:
        status = json.load(f)
    owner = {r["table"]: r["rows"] for r in status["result"]["row_counts"]}
    readers = {r["table_name"]: int(r["reader_rows"]) for r in rows["reader_counts"]}
    with open(os.path.join(RAW, DAY, "manifest.json"), encoding="utf-8") as f:
        manifest = json.load(f)
    inputs = {"source": "wwi", "extract": DAY, "manifest_sha256": sha(os.path.join(RAW, DAY, "manifest.json"))}
    wanted = set(argv[1:])
    summary_dir = os.path.join(ROOT, "scratch", "ia_profile")
    os.makedirs(summary_dir, exist_ok=True)
    for entry in manifest["files"]:
        table = entry["table"]
        if wanted and table not in wanted:
            continue
        schema, name = table.split(".", 1)
        out_dir = os.path.join(ROOT, "analysis", "wwi", "tables", ia.escape(schema), ia.escape(name), "evidence")
        mine = lambda r: r.get("schema_name") == schema and r.get("table_name") == name
        pk = [r["column_name"] for r in rows["keys"] if mine(r) and r["is_primary_key"] == "1"]
        cat = {
            "table": [r for r in rows["tables"] if mine(r)],
            "columns": [r for r in rows["columns"] if mine(r)],
            "keys": [r for r in rows["keys"] if mine(r)],
            "foreign_keys_out": [r for r in rows["fks"] if mine(r)],
            "foreign_keys_in": [r for r in rows["fks"] if r["ref_schema"] == schema and r["ref_table"] == name],
            "checks": [r for r in rows["checks"] if mine(r)],
            "masked_columns": [r for r in rows["masked"] if mine(r)],
            "security_policies_visible_to_reader": len(rows["rls"]),
            "rows_seen_by_owner": owner.get(table), "rows_seen_by_nsdn_reader": readers.get(table),
            "rows_in_extract": entry["rows"], "temporal_in_manifest": entry["temporal"],
        }
        e_cat = write(out_dir, {"kind": "catalogue query", "tool": "sandbox request folder (job.ps1 query and status)",
                                "tool_version": "pinned job in C:\\ProgramData\\nsdn-wwi",
                                "query": {k: cat_query(v) for k, v in CAT.items()},
                                "inputs": {"source": "wwi", "database": "WideWorldImporters", "simulation_clock": DAY,
                                           "requests": CAT, "status_request": STATUS, "run_as": "nsdn_reader; status as owner"},
                                "ran_at": max(cat_ran(v) for v in CAT.values()), "result": cat})
        fn = profile_big if entry["rows"] > BIG else profile
        prof = fn(table, pk)
        e_prof = write(out_dir, {"kind": "profile", "tool": SCRIPT, "tool_version": TOOL_VERSION,
                                 "code": inspect.getsource(fn), "inputs": dict(inputs, table=table),
                                 "ran_at": now(), "result": prof})
        e_tr, tr = None, None
        if pk and entry["rows"] <= BIG:
            tr = transition(table, pk)
            e_tr = write(out_dir, {"kind": "comparison of two extracts", "tool": SCRIPT, "tool_version": TOOL_VERSION,
                                   "code": inspect.getsource(transition),
                                   "inputs": {"from": {"source": "wwi", "extract": PREV, "manifest_sha256": sha(os.path.join(RAW, PREV, "manifest.json"))},
                                              "to": inputs, "table": table},
                                   "ran_at": now(), "result": tr})
        with open(os.path.join(summary_dir, table + ".json"), "w", encoding="utf-8") as f:
            json.dump({"table": table, "evidence": {"catalogue": e_cat, "profile": e_prof, "transition": e_tr},
                       "catalogue": cat, "profile": prof, "transition": tr}, f, indent=1)
        print("%-42s rows %8d  cat %s  prof %s  tr %s" % (table, entry["rows"], e_cat, e_prof, e_tr), flush=True)


if __name__ == "__main__":
    main(sys.argv)
