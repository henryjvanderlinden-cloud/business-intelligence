"""Shared rules of the information-analysis record (analysis/README.md, ADR-0018).

Used by tools/check_repo.py, tools/ia_status.py and the evidence scripts, so that one definition of names, hashes,
items and claim lines serves all of them.
"""
import hashlib
import json
import re

KEEP = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_-")
RESERVED = {"CON", "PRN", "AUX", "NUL"} | {"COM%d" % i for i in range(10)} | {"LPT%d" % i for i in range(10)}

ITEMS = {
    "01": "granularity", "02": "meaning", "03": "temporal", "04": "relations", "05": "role", "06": "keys",
    "07": "population", "08": "measures", "09": "derived", "10": "codes", "11": "formats", "12": "copies",
    "13": "hierarchies", "14": "provenance", "15": "quality", "16": "reconciliation", "17": "volume",
    "18": "documentation", "19": "sensitivity", "20": "ownership", "21": "demand", "22": "stability",
    "23": "extraction", "24": "processes", "25": "terms", "26": "entities", "27": "peculiarities",
    "28": "arithmetic", "29": "position",
}
TABLE_ITEMS = set(ITEMS) - {"04", "24", "25", "26"}
SOURCE_ITEMS = {"14", "18", "20", "22", "23", "29"}   # analysis/README.md section 1: source-wide items in _source/
RELATION_ITEMS = {"01", "02", "03", "06", "07", "27"}   # analysis/README.md section 9
RELATION_MINIMUM = {"01", "02", "06", "07", "27"}
COLUMN_ITEMS = {"02", "03", "06", "07", "08", "09", "10", "11", "12", "13", "15", "18", "19", "21", "22", "27", "28"}
MINIMUM = {"01", "03", "05", "06", "07", "19"}

CLAIM_TYPES = {"declared", "observed", "implemented", "intended", "certified"}
STATUSES = {"proposed", "accepted", "contested", "superseded", "retracted"}
CONFIDENCE = ["unknown", "low", "medium", "high"]          # ascending
TIERS = {"minimum", "best-effort"}

FRONT_KEYS = ["id", "subject", "item", "topic", "tier", "summary", "confidence", "claims", "written_by",
              "written_at", "step", "method", "input_source", "input_extract", "input_manifest_sha256",
              "input_schema_sha256", "last_checked_at", "last_checked_by", "last_checked_against", "reviewed_by",
              "reviewed_at", "ruled_by", "ruled_at", "supersedes", "superseded_by", "recheck_when"]
CLAIM_KEYS = ["type", "status", "confidence", "effective", "observed", "checked", "evidence", "recheck"]
CLAIM_RE = re.compile(r"^- (C\d+) \| (.*?) \| text: (.+)$")
ITEM_FILE_RE = re.compile(r"^(\d\d)_([a-z-]+)\.md$")
EVIDENCE_RE = re.compile(r"^([0-9a-f]{16})\.json$")


def escape(name):
    out = "".join(chr(b) if chr(b) in KEEP else "%%%02X" % b for b in name.encode("utf-8"))
    if out.upper() in RESERVED:
        out = out[:-1] + "%%%02X" % ord(out[-1])
    return out


def unescape(name):
    return re.sub(r"%([0-9A-F]{2})", lambda m: chr(int(m.group(1), 16)), name).encode("latin-1").decode("utf-8")


def is_escaped(name):
    try:
        return escape(unescape(name)) == name
    except (UnicodeDecodeError, UnicodeEncodeError):
        return False


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def evidence_hash(record):
    body = {k: v for k, v in record.items() if k != "id"}
    return hashlib.sha256(canonical(body).encode("ascii")).hexdigest()[:16]


def schema_hash(columns):
    return hashlib.sha256("\n".join(columns).encode("utf-8")).hexdigest()


def parse_item(text):
    """Return (front matter dict, list of claims, error list) for an item file."""
    errs = []
    lines = text.split("\n")
    if not lines or lines[0] != "---":
        return {}, [], ["no front matter"]
    try:
        end = lines.index("---", 1)
    except ValueError:
        return {}, [], ["front matter not closed"]
    front = {}
    for ln in lines[1:end]:
        if ":" not in ln:
            errs.append("front matter line without a key: %r" % ln)
            continue
        k, v = ln.split(":", 1)
        front[k.strip()] = v.strip()
    claims = []
    for ln in lines[end + 1:]:
        if ln.startswith("- C") and " | " in ln:
            m = CLAIM_RE.match(ln)
            if not m:
                errs.append("malformed claim line: %r" % ln[:80])
                continue
            fields = {}
            for part in m.group(2).split(" | "):
                if "=" not in part:
                    errs.append("claim %s: field without '=': %r" % (m.group(1), part))
                    continue
                k, v = part.split("=", 1)
                fields[k.strip()] = v.strip()
            fields["id"] = m.group(1)
            fields["text"] = m.group(3)
            claims.append(fields)
    return front, claims, errs


def parse_relation(name):
    """A relation folder name (analysis/README.md sections 3 and 9) as two (schema, table, [columns]) sides, unescaped;
    None if it does not parse or is not reversibly escaped."""
    sides = name.split("__")
    if len(sides) != 2:
        return None
    out = []
    for side in sides:
        parts = side.split(".")
        if len(parts) < 3 or not all(is_escaped(p) for p in parts):
            return None
        out.append((unescape(parts[0]), unescape(parts[1]), [unescape(p) for p in parts[2:]]))
    return tuple(out)


def relation_schema_hash(child_schema_sha256, parent_schema_sha256):
    """input_schema_sha256 of a relation's item files: both tables' column lists, so either changing makes it stale."""
    return hashlib.sha256((child_schema_sha256 + "\n" + parent_schema_sha256).encode("ascii")).hexdigest()
