"""Turn the CSV files of a catalogue pass into catalogue evidence in an analysis record (analysis/README.md, ADR-0018).

Reads the folder that catalogue_postgres.sql wrote (one CSV per query, with manifest.csv) and writes, for every table
and view, one evidence file `analysis/<source>/tables/<schema>/<table>/evidence/<hash>.json` of kind "catalogue
query", in the shape the Wide World Importers record uses, and one source-wide evidence under
`analysis/<source>/_source/evidence/`. Evidence is named by its content and written once: ingesting the same folder again writes
nothing new; a later pass writes new files beside the old ones, and readers take the newest by `ran_at`.
No item files are written; those carry judgement and are the agent's (129, ADR-0019).

Standard library only. Run from the root of the repository that holds the analysis record:

    python <nsdn>/prototypes/catalogue_pass/ingest_catalogue.py --source <code> <folder with the CSV files>

`<nsdn>` is the path of the nsdn release (`.` inside the nsdn repository itself). Written in session S11.
"""
import argparse
import csv
import hashlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
import ia_lib  # noqa: E402

QUERIES = ["manifest", "tables", "columns", "keys", "foreign_keys", "checks", "triggers", "views", "view_dependencies"]
TOOL = "prototypes/catalogue_pass (catalogue_postgres.sql through psql, then ingest_catalogue.py)"
SOURCE_RE = re.compile(r"^[a-z][a-z0-9_]*$")


def read_csv(folder, name):
    path = os.path.join(folder, name + ".csv")
    if not os.path.isfile(path):
        sys.exit("missing %s: run catalogue_postgres.sql in that folder first" % path)
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def file_sha(folder, name):
    with open(os.path.join(folder, name + ".csv"), "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def query_texts():
    """The SQL of each query, from the file itself, so the evidence holds what was run."""
    with open(os.path.join(HERE, "catalogue_postgres.sql"), encoding="utf-8") as f:
        text = f.read()
    out = {}
    for block in text.split("-- @query ")[1:]:
        name, body = block.split("\n", 1)
        out[name.strip()] = body.split("\n-- @query")[0].strip()
    return out


def flag(v):
    return "1" if str(v).lower() in ("1", "t", "true") else "0"


def write_evidence(directory, record, written):
    record = dict(record)
    record.pop("id", None)
    h = ia_lib.evidence_hash(record)
    record = dict({"id": h}, **record)
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, h + ".json")
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            json.dump(record, f, indent=1, ensure_ascii=False, sort_keys=True)
            f.write("\n")
        written.append(path)
    return h


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--source", required=True, help="the source's code in the record, e.g. crm (lower case)")
    ap.add_argument("--root", default=".", help="root of the repository holding analysis/ (default: here)")
    ap.add_argument("folder", help="the folder the SQL wrote its CSV files to")
    a = ap.parse_args()
    if not SOURCE_RE.match(a.source):
        sys.exit("source code must be lower case letters, digits and underscores")
    data = {q: read_csv(a.folder, q) for q in QUERIES}
    man = data["manifest"][0]
    sql = query_texts()
    inputs = {"source": a.source, "database": man["database"], "run_as": man["run_as"],
              "server_version": man["server_version_num"], "server_time_zone": man["server_time_zone"],
              "files_sha256": {q: file_sha(a.folder, q) for q in QUERIES}}
    ran_at = man["extracted_at"]
    base = os.path.join(a.root, "analysis", a.source)

    def key(r, s="schema_name", t="table_name"):
        return (r[s], r[t])

    by = {q: {} for q in QUERIES}
    for q in ("columns", "keys", "checks", "triggers"):
        for r in data[q]:
            by[q].setdefault(key(r), []).append(r)
    fk_out, fk_in = {}, {}
    for r in data["foreign_keys"]:
        r = dict(r, is_disabled=flag(r["is_disabled"]), is_not_trusted=flag(r["is_not_trusted"]))
        fk_out.setdefault(key(r), []).append(r)
        fk_in.setdefault((r["ref_schema"], r["ref_table"]), []).append(r)
    views = {key(r, t="view_name"): r for r in data["views"]}
    vdeps = {}
    for r in data["view_dependencies"]:
        vdeps.setdefault(key(r, t="view_name"), []).append({"ref_schema": r["ref_schema"], "ref_table": r["ref_table"]})

    written, n = [], 0
    for t in data["tables"]:
        k = key(t)
        cols = []
        for c in by["columns"].get(k, []):
            cols.append({"object_id": c["object_id"], "schema_name": c["schema_name"], "table_name": c["table_name"],
                         "column_id": c["column_id"], "column_name": c["column_name"], "type_name": c["type_name"],
                         "base_type": c["base_type"], "max_length": c["max_length"], "precision": c["precision"],
                         "scale": c["scale"], "is_nullable": flag(c["is_nullable"]), "is_identity": flag(c["is_identity"]),
                         "is_computed": flag(c["is_computed"]), "is_masked": "0",
                         "default_definition": c["default_definition"], "computed_definition": c["computed_definition"],
                         "description": c["description"], "collation": c["collation"]})
        table = {"object_id": t["object_id"], "schema_name": t["schema_name"], "table_name": t["table_name"],
                 "table_kind": t["table_kind"], "description": t["description"], "estimated_rows": t["estimated_rows"],
                 "is_partition": flag(t["is_partition"]), "partition_of": t["partition_of"],
                 "partition_bound": t["partition_bound"],
                 "row_level_security": flag(t["row_level_security"]), "owner": t["owner"],
                 "temporal_type_desc": "NON_TEMPORAL_TABLE", "history_table": ""}
        result = {"table": [table], "columns": cols,
                  "keys": [dict(r, is_primary_key=flag(r["is_primary_key"]), is_unique=flag(r["is_unique"]),
                                is_unique_constraint=flag(r["is_unique_constraint"]),
                                nulls_not_distinct=flag(r["nulls_not_distinct"])) for r in by["keys"].get(k, [])],
                  "foreign_keys_out": fk_out.get(k, []), "foreign_keys_in": fk_in.get(k, []),
                  "checks": by["checks"].get(k, []), "triggers": by["triggers"].get(k, [])}
        if k in views:
            result["view_definition"] = views[k]["definition"]
            result["view_reads"] = vdeps.get(k, [])
        record = {"kind": "catalogue query", "tool": TOOL, "tool_version": "nsdn S11", "inputs": inputs,
                  "ran_at": ran_at, "query": {q: sql.get(q, "") for q in QUERIES if q != "manifest"}, "result": result}
        d = os.path.join(base, "tables", ia_lib.escape(t["schema_name"]), ia_lib.escape(t["table_name"]), "evidence")
        write_evidence(d, record, written)
        n += 1
    summary = {"kind": "catalogue query", "tool": TOOL, "tool_version": "nsdn S11", "inputs": inputs, "ran_at": ran_at,
               "query": {"manifest": sql.get("manifest", ""), "tables": sql.get("tables", "")},
               "result": {"manifest": man, "schemas": sorted({t["schema_name"] for t in data["tables"]}),
                          "counts": {q: len(data[q]) for q in QUERIES if q != "manifest"},
                          "tables": [{"schema_name": t["schema_name"], "table_name": t["table_name"],
                                      "table_kind": t["table_kind"]} for t in data["tables"]]}}
    write_evidence(os.path.join(base, "_source", "evidence"), summary, written)
    print("%s: %d tables and views, %d columns, %d foreign-key columns; %d new evidence files"
          % (a.source, n, len(data["columns"]), len(data["foreign_keys"]), len(written)))


if __name__ == "__main__":
    main()
