#!/usr/bin/env python3
"""Summarise the information-analysis record and compute freshness (analysis/README.md section 6, ADR-0018).

    python tools/ia_status.py [path under analysis/]

Prints one line per item file: freshness, tier, confidence, item, subject and summary; then the recheck conditions
an agent must evaluate. Generated on demand and never committed, so no agent edits a shared index.
"""
import csv
import gzip
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ia_lib as ia  # noqa: E402


def newest_extract(source):
    d = os.path.join(ROOT, "data", "raw", source)
    days = sorted(x for x in os.listdir(d) if os.path.isdir(os.path.join(d, x))) if os.path.isdir(d) else []
    return days[-1] if days else None


def current_schema(source, extract, schema, table):
    f = os.path.join(ROOT, "data", "raw", source, extract, "%s.%s.csv.gz" % (schema, table))
    if not os.path.exists(f):
        return None
    with gzip.open(f, "rt", encoding="utf-8", newline="") as fh:
        return ia.schema_hash(next(csv.reader(fh)))


def main(argv):
    base = os.path.join(ROOT, argv[1]) if len(argv) > 1 else os.path.join(ROOT, "analysis")
    rows, rechecks, cache = [], [], {}
    for dirpath, _, files in os.walk(base):
        for f in sorted(files):
            if not ia.ITEM_FILE_RE.match(f):
                continue
            path = os.path.join(dirpath, f)
            rel = os.path.relpath(path, ROOT).replace(os.sep, "/")
            with open(path, encoding="utf-8") as fh:
                front, claims, _ = ia.parse_item(fh.read())
            parts = rel.split("/")
            fresh = "?"
            if "tables" in parts:
                i = parts.index("tables")
                source, schema, table = parts[1], ia.unescape(parts[i + 1]), ia.unescape(parts[i + 2])
                key = (source, schema, table)
                if key not in cache:
                    ext = newest_extract(source)
                    cache[key] = (ext, current_schema(source, ext, schema, table) if ext else None)
                ext, sch = cache[key]
                if front.get("superseded_by", "none") != "none" or (sch and sch != front.get("input_schema_sha256")):
                    fresh = "stale"
                elif ext and front.get("last_checked_against") == ext:
                    fresh = "fresh"
                else:
                    fresh = "ageing"
            rows.append((fresh, front.get("tier", "?"), front.get("confidence", "?"), front.get("item", "?"),
                         front.get("subject", rel), front.get("summary", "")))
            if front.get("recheck_when", "none") != "none":
                rechecks.append("%s: %s" % (rel, front["recheck_when"]))
    for r in rows:
        print("%-6s %-11s %-7s %s  %s\n       %s" % r)
    counts = {}
    for r in rows:
        counts[r[0]] = counts.get(r[0], 0) + 1
    print("\n%d item files: %s" % (len(rows), ", ".join("%s %d" % kv for kv in sorted(counts.items()))))
    if rechecks:
        print("\nRecheck conditions for an agent to evaluate:")
        for r in rechecks:
            print("  " + r)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
