"""Shared reading of the model declarations under model/ (format: model/README.md; open under ARC-OP-29).

Used by tools/check_repo.py and prototypes/schema_viewer/build.py, so that one parser serves both. Standard library
only, like ia_lib.py, whose grammar it follows: a flat front matter of `key: value` lines, then sections headed `## `,
whose entries are lines `- <subject> | key=value | key=value`.
"""
import json
import os
import re

MODEL_DIR = "model"
KINDS = {"hub": "model/raw_vault/hubs", "link": "model/raw_vault/links", "satellite": "model/raw_vault/satellites",
         "reference": "model/raw_vault/reference", "source": "model/sources"}
ID_PREFIX = {"hub": "nsdn:rv:hub:", "link": "nsdn:rv:link:", "satellite": "nsdn:rv:sat:", "reference": "nsdn:rv:ref:",
             "source": "nsdn:source:"}
NAME_RE = {"hub": re.compile(r"^hub_[a-z][a-z0-9_]*$"),
           "link": re.compile(r"^lnk_[a-z][a-z0-9_]*__[a-z][a-z0-9_]*$"),
           "satellite": re.compile(r"^sat_[a-z][a-z0-9_]*__[a-z][a-z0-9]*(__[a-z][a-z0-9_]*)?$"),
           "reference": re.compile(r"^ref_[a-z][a-z0-9_]*__[a-z][a-z0-9]*$"),
           "source": re.compile(r"^[a-z][a-z0-9]*$")}
COMMON = ["id", "kind", "name", "status", "ruled_in", "defined_in", "written_by", "written_at", "step", "method"]
REQUIRED = {
    "hub": COMMON + ["concept", "grain", "subject_area"],
    "link": COMMON + ["label", "from", "to", "driving", "optional", "effectivity", "subject_area"],
    "satellite": COMMON + ["parent", "source", "source_table", "parent_key", "satellite_kind", "split_reason",
                           "valid_time", "class", "subject_area"],
    "reference": COMMON + ["source", "source_table", "key", "key_space", "history", "class", "subject_area"],
    "source": COMMON + ["title", "key_space", "key_case", "extract", "by_rule"],
}
SECTIONS = {"hub": {"Business key"}, "link": {"Columns", "Relations"}, "satellite": {"Columns"},
            "reference": {"Columns"}, "source": {"Base tables"}}
STATUSES = {"proposed", "accepted", "contested", "retired"}
CLASSES = {"open", "internal", "confidential", "personal", "restricted"}
SAT_KINDS = {"payload", "milestone", "reading"}
EFFECTIVITY = {"load", "event", "milestone", "absence"}
ENTRY_RE = re.compile(r"^- (\S.*)$")


def parse(text):
    """Return (front dict, {section: [(subject, {flag: value})]}, prose lines, errors)."""
    errs = []
    lines = text.split("\n")
    if not lines or lines[0] != "---":
        return {}, {}, [], ["no front matter"]
    try:
        end = lines.index("---", 1)
    except ValueError:
        return {}, {}, [], ["front matter not closed"]
    front = {}
    for ln in lines[1:end]:
        if ": " not in ln and not ln.endswith(":"):
            errs.append("front matter line without a key: %r" % ln)
            continue
        k, v = ln.split(":", 1)
        if k.strip() in front:
            errs.append("front matter key repeated: %s" % k.strip())
        front[k.strip()] = v.strip()
    sections, prose, current = {}, [], None
    for ln in lines[end + 1:]:
        if ln.startswith("## "):
            current = ln[3:].strip()
            if current in sections:
                errs.append("section repeated: %s" % current)
            sections.setdefault(current, [])
            continue
        if current is None or not ln.strip():
            continue
        if current == "Notes":
            prose.append(ln)
            continue
        m = ENTRY_RE.match(ln)
        if not m:
            errs.append("section %s: line is not an entry: %r" % (current, ln[:80]))
            continue
        parts = m.group(1).split(" | ")
        flags = {}
        for p in parts[1:]:
            if "=" not in p:
                errs.append("section %s: flag without '=': %r" % (current, p))
                continue
            k, v = p.split("=", 1)
            flags[k.strip()] = v.strip()
        sections[current].append((parts[0].strip(), flags))
    return front, sections, prose, errs


def load(root):
    """All declaration files: [(relative path, front, sections, prose, errors)]."""
    out = []
    base = os.path.join(root, MODEL_DIR)
    for dirpath, dirnames, filenames in os.walk(base):
        dirnames.sort()
        for fn in sorted(filenames):
            if not fn.endswith(".md") or fn == "README.md":
                continue
            rel = os.path.relpath(os.path.join(dirpath, fn), root).replace(os.sep, "/")
            with open(os.path.join(root, rel), encoding="utf-8") as f:
                front, sections, prose, errs = parse(f.read())
            out.append((rel, front, sections, prose, errs))
    return out


def catalogue(root, rel_path):
    """The catalogue evidence of one source table: [{column_name, type_name, is_nullable, ...}] and its keys."""
    with open(os.path.join(root, rel_path), encoding="utf-8") as f:
        d = json.load(f)
    r = d["result"]
    cols = sorted(r["columns"], key=lambda c: int(c["column_id"]))
    return {"columns": cols, "keys": r.get("keys", []), "fks_out": r.get("foreign_keys_out", []),
            "table": r.get("table"), "triggers": r.get("triggers", []), "checks": r.get("checks", []),
            "view_reads": r.get("view_reads", []), "view_definition": r.get("view_definition", "")}


def type_text(c):
    """A source column's declared type as the catalogue states it, e.g. nvarchar(100), decimal(18,2)."""
    t = c["type_name"]
    if t in ("nvarchar", "varchar", "varbinary", "nchar", "char"):
        n = int(c["max_length"])
        size = "max" if n == -1 else str(n // 2 if t.startswith("n") else n)
        return "%s(%s)" % (t, size)
    if t in ("decimal", "numeric"):
        return "%s(%s,%s)" % (t, c["precision"], c["scale"])
    if t == "datetime2":
        return "datetime2(%s)" % c["scale"]
    return t


def split_list(value):
    return [v.strip() for v in value.split(",") if v.strip()]
