#!/usr/bin/env python3
"""Mechanical checks for the nsdn repository.

Written against the standing rule in docs/50_process/500_working-method.md:

    A newly-written rule is unenforced until something mechanical enforces it.
    Write the check, not the sentence.

Run from the repository root:

    python tools/check_repo.py

Exits nonzero if any check fails. Warnings do not fail the run.
"""

import json
import os
import re
import sys
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REGISTER = "registers/OPEN_POINTS.md"
ADR_DIR = "docs/20_decisions"
ADR_INDEX = "docs/20_decisions/README.md"
HANDOVER_DIR = "handovers"
RECORDS_DIR = "records"
TASK_TABLE = "docs/00_concept/070_task-allocation.md"

SCOPES = {"CON", "ARC", "EVI", "PRC", "BIZ", "X"}
CLOSING = {"EXECUTED", "ARCHIVED"}
DATED = {"EXECUTED", "RULED", "ARCHIVED"}
TOKENS = {"EXECUTED", "RULED", "OPEN", "HELD", "ARCHIVED"}

ROW_RE = re.compile(r"^### ([A-Z]+-OP-\d+) — (.+)$")
STATE_RE = re.compile(r"^\*\*(?:[^\sA-Za-z]+\s)?STATE: ([A-Z]+)(.*?)\*\*\s*$")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
SETTLED_WORDS = re.compile(r"\b(RESOLVED|SETTLED|CLOSED|DONE|EXECUTED)\b", re.I)
PARTIAL_WORDS = re.compile(r"\b(PARTLY|PARTIALLY|SUB-ITEM|SIDE)\b", re.I)

errors = []
warnings = []


def err(where, msg):
    errors.append("%s: %s" % (where, msg))


def warn(where, msg):
    warnings.append("%s: %s" % (where, msg))


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


def markdown_files():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in (".git", "node_modules", "__pycache__")]
        for name in filenames:
            if name.endswith(".md"):
                yield os.path.relpath(os.path.join(dirpath, name), ROOT)


def check_register():
    """The state rule, identifier discipline, and the partial-settlement trap."""
    if not os.path.exists(os.path.join(ROOT, REGISTER)):
        err(REGISTER, "register is missing")
        return
    lines = read(REGISTER).splitlines()
    seen = {}
    rows = 0
    live = 0
    for i, line in enumerate(lines):
        m = ROW_RE.match(line)
        if not m:
            if line.startswith("### "):
                err(REGISTER, "line %d: heading is not a well-formed row id — %r" % (i + 1, line))
            continue
        rows += 1
        rid, name = m.group(1), m.group(2)
        where = "%s [%s]" % (REGISTER, rid)

        scope = rid.split("-")[0]
        if scope not in SCOPES:
            err(where, "unknown scope %r (allowed: %s)" % (scope, ", ".join(sorted(SCOPES))))
        if rid in seen:
            err(where, "duplicate id, first seen at line %d" % seen[rid])
        seen[rid] = i + 1

        nxt = None
        for j in range(i + 1, min(i + 4, len(lines))):
            if lines[j].strip():
                nxt = (j, lines[j])
                break
        if nxt is None:
            err(where, "row has no body")
            continue
        sm = STATE_RE.match(nxt[1].strip())
        if not sm:
            err(where, "line %d: first line after the heading is not a state token — %r"
                % (nxt[0] + 1, nxt[1].strip()))
            continue
        token, rest = sm.group(1), sm.group(2).strip()
        if token not in TOKENS:
            err(where, "unknown state token %r (allowed: %s)" % (token, ", ".join(sorted(TOKENS))))
            continue
        if token in DATED and not rest:
            err(where, "state %s must carry a date or cut identifier" % token)
        if token not in CLOSING:
            live += 1
            if SETTLED_WORDS.search(name) and not PARTIAL_WORDS.search(name):
                err(where, "name claims settlement (%r) while state is %s — say PARTLY/PARTIALLY/"
                           "SUB-ITEM, or change the state" % (name, token))
    print("register: %d rows, %d live" % (rows, live))
    if rows and not live:
        warn(REGISTER, "no live rows — either the project is finished or the register has drifted")


def check_adr_index():
    """Every ADR is indexed, and every indexed ADR exists."""
    adr_dir = os.path.join(ROOT, ADR_DIR)
    if not os.path.isdir(adr_dir):
        err(ADR_DIR, "missing")
        return
    on_disk = set()
    for name in os.listdir(adr_dir):
        if re.match(r"^\d{4}-.+\.md$", name) and not name.startswith("0000-"):
            on_disk.add(name)
    index = read(ADR_INDEX)
    listed = set(re.findall(r"\(([0-9]{4}-[^)]+\.md)\)", index))
    listed.discard("0000-template.md")
    for name in sorted(on_disk - listed):
        err(ADR_INDEX, "ADR %s exists but is not in the index" % name)
    for name in sorted(listed - on_disk):
        err(ADR_INDEX, "index lists %s, which does not exist" % name)
    print("adrs: %d indexed" % len(on_disk))


def check_handovers():
    """Exactly one current handover, and CURRENT.md points at it."""
    hdir = os.path.join(ROOT, HANDOVER_DIR)
    if not os.path.isdir(hdir):
        return
    files = sorted(n for n in os.listdir(hdir) if n.startswith("HANDOVER_"))
    if not files:
        warn(HANDOVER_DIR, "no handovers yet")
        return
    current = []
    for name in files:
        body = read(os.path.join(HANDOVER_DIR, name))
        if "STATUS: HISTORICAL" in body:
            continue
        if "STATUS: CURRENT" in body:
            current.append(name)
        else:
            err("%s/%s" % (HANDOVER_DIR, name), "no status block (STATUS: CURRENT or HISTORICAL)")
    if len(current) > 1:
        err(HANDOVER_DIR, "more than one current handover: %s" % ", ".join(current))
    pointer = read(os.path.join(HANDOVER_DIR, "CURRENT.md"))
    targets = LINK_RE.findall(pointer)
    if len(current) == 1 and current[0] not in " ".join(targets):
        err("%s/CURRENT.md" % HANDOVER_DIR, "points at %s but the current handover is %s"
            % (targets, current[0]))
    print("handovers: %d total, current is %s" % (len(files), current[0] if current else "none"))


def check_links():
    """Relative markdown links resolve."""
    checked = 0
    for rel in markdown_files():
        base = os.path.dirname(os.path.join(ROOT, rel))
        for target in LINK_RE.findall(read(rel)):
            target = target.split("#")[0].strip()
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            checked += 1
            if not os.path.exists(os.path.normpath(os.path.join(base, target))):
                err(rel, "broken link -> %s" % target)
    print("links: %d relative links checked" % checked)


def check_superseded():
    """The word 'superseded' is load-bearing: flag struck-through text that omits it."""
    for rel in markdown_files():
        body = read(rel)
        if "~~" in body and "superseded" not in body.lower():
            warn(rel, "contains struck-through text but never says 'superseded'")


def _load_jsonl(rel):
    """Parse a JSON Lines file; report and skip bad lines."""
    out = []
    for n, line in enumerate(read(rel).splitlines(), 1):
        if not line.strip():
            continue
        try:
            out.append((n, json.loads(line)))
        except ValueError as exc:
            err(rel, "line %d: not valid JSON (%s)" % (n, exc))
    return out


def _ts(value):
    try:
        t = datetime.fromisoformat(value)
    except (TypeError, ValueError):
        return None
    return t if t.tzinfo else None


STEP_REQUIRED = ("id", "session", "ts", "ts_precision", "actor", "agent", "role", "task_type",
                 "tier", "work_class", "summary", "outcome", "recorded")
SOURCE_REQUIRED = ("id", "name", "publisher", "status", "found_by")
SESSION_REQUIRED = ("id", "logged")


def check_records():
    """The step log of ADR-0014: vocabulary, required fields, and references that resolve."""
    rdir = os.path.join(ROOT, RECORDS_DIR)
    if not os.path.isdir(rdir):
        return
    vocab = json.loads(read(os.path.join(RECORDS_DIR, "vocabulary.json")))
    register_ids = set(m.group(1) for m in map(ROW_RE.match, read(REGISTER).splitlines()) if m)
    task_rows = set(int(n) for n in re.findall(r"^\| (\d+) \|", read(TASK_TABLE), re.M))

    def enum(where, field, value, allowed):
        if value not in allowed:
            err(where, "%s %r not in vocabulary" % (field, value))

    sessions = {}
    for n, rec in _load_jsonl(os.path.join(RECORDS_DIR, "sessions.jsonl")):
        where = "records/sessions.jsonl line %d" % n
        for f in SESSION_REQUIRED:
            if f not in rec:
                err(where, "missing %s" % f)
        sessions[rec.get("id")] = rec

    steps = {}
    by_actor, by_class, overhead = {}, {}, 0
    h_sizes, h_words = {}, [0]
    step_files = sorted(f for f in os.listdir(os.path.join(rdir, "steps")) if f.endswith(".jsonl"))
    for fname in step_files:
        rel = "%s/steps/%s" % (RECORDS_DIR, fname)
        session = fname[:-len(".jsonl")]
        if session not in sessions:
            err(rel, "session %s is not in sessions.jsonl" % session)
        expect, last_ts = 1, None
        for n, rec in _load_jsonl(rel):
            where = "%s line %d [%s]" % (rel, n, rec.get("id"))
            missing = [f for f in STEP_REQUIRED if f not in rec]
            if missing:
                err(where, "missing %s" % ", ".join(missing))
                continue
            sid = rec["id"]
            if rec["session"] != session:
                err(where, "session %r does not match file %s" % (rec["session"], fname))
            if sid != "%s-%03d" % (session, expect):
                err(where, "id out of sequence; expected %s-%03d" % (session, expect))
            expect += 1
            if sid in steps:
                err(where, "duplicate step id")
            steps[sid] = rec
            t = _ts(rec["ts"])
            if t is None:
                err(where, "ts %r is not ISO 8601 with a UTC offset" % rec["ts"])
            elif last_ts and t < last_ts:
                warn(where, "ts earlier than the previous step")
            last_ts = t or last_ts
            if "ts_end" in rec and _ts(rec["ts_end"]) is None:
                err(where, "ts_end is not ISO 8601 with a UTC offset")
            for field, key in (("actor", "actor"), ("role", "role"), ("tier", "tier"),
                               ("work_class", "work_class"), ("task_type", "task_type"),
                               ("outcome", "outcome"), ("ts_precision", "ts_precision"),
                               ("recorded", "recorded")):
                enum(where, field, rec[field], vocab[key])
            faculty = vocab["agents"].get(rec["agent"])
            if faculty is None:
                err(where, "agent %r is not in vocabulary.agents" % rec["agent"])
            elif faculty != rec["actor"]:
                err(where, "agent %r is %s, but actor is %s" % (rec["agent"], faculty, rec["actor"]))
            if rec["actor"] == "H" and rec["role"] in ("request", "decide") and not rec.get("verbatim"):
                err(where, "a person's request or decision needs the verbatim field")
            if rec["actor"] == "H":
                he = rec.get("human_effort")
                if not he:
                    err(where, "a person's step needs human_effort (activity, size, answers)")
                else:
                    enum(where, "human_effort.activity", he.get("activity"), vocab["human_activity"])
                    enum(where, "human_effort.size", he.get("size"), vocab["human_size"])
                    want = vocab["_size_by_activity"].get(he.get("activity"))
                    if want and he.get("size") != want:
                        err(where, "activity %r is size %s, not %s" % (he.get("activity"), want, he.get("size")))
                    if not isinstance(he.get("answers"), int):
                        err(where, "human_effort.answers must be an integer")
                    if he.get("activity") == "answer":
                        if rec.get("verbatim") and he.get("words") != len(rec["verbatim"].split()):
                            err(where, "human_effort.words does not match the verbatim text")
                    h_sizes[he.get("size")] = h_sizes.get(he.get("size"), 0) + 1
                    h_words[0] += he.get("words", 0) or 0
            elif rec.get("human_effort"):
                err(where, "human_effort on a step whose actor is not H")
            if rec.get("task_row") is not None and rec["task_row"] not in task_rows:
                err(where, "task_row %r is not a row of 070" % rec["task_row"])
            for rid in rec.get("register_rows", []):
                if rid not in register_ids:
                    err(where, "register row %s does not exist" % rid)
            ref = rec.get("initiated_by")
            if ref is not None and ref not in steps:
                err(where, "initiated_by %s is not an earlier step" % ref)
            if rec["outcome"] in ("blocked", "failed"):
                b = rec.get("blocker") or {}
                if not b.get("detail"):
                    err(where, "a %s step needs blocker.detail" % rec["outcome"])
            if rec.get("blocker"):
                enum(where, "blocker.category", rec["blocker"].get("category"), vocab["blocker"])
            for d in rec.get("defects", []):
                enum(where, "defect.type", d.get("type"), vocab["defect"])
                if not d.get("detail"):
                    err(where, "defect without detail")
            eff = rec.get("effort", {})
            if "human_basis" in eff:
                enum(where, "effort.human_basis", eff["human_basis"], vocab["human_basis"])
            for tool in eff.get("tool_calls", {}):
                enum(where, "instrument", tool, vocab["instruments"])
            by_actor[rec["actor"]] = by_actor.get(rec["actor"], 0) + 1
            by_class[rec["work_class"]] = by_class.get(rec["work_class"], 0) + 1

    # defect fix references and sources can point forward, so resolve them once all steps are read
    for sid, rec in steps.items():
        for d in rec.get("defects", []):
            for key in ("found_by", "fixed_by"):
                if d.get(key) and d[key] not in steps:
                    err("records step %s" % sid, "defect.%s %s is not a step" % (key, d[key]))

    src_ids = set()
    for n, rec in _load_jsonl(os.path.join(RECORDS_DIR, "sources.jsonl")):
        where = "records/sources.jsonl line %d [%s]" % (n, rec.get("id"))
        for f in SOURCE_REQUIRED:
            if f not in rec:
                err(where, "missing %s" % f)
        if rec.get("id") in src_ids:
            err(where, "duplicate source id")
        src_ids.add(rec.get("id"))
        enum(where, "status", rec.get("status"), vocab["source_status"])
        if rec.get("status") in ("rejected", "blocked") and not rec.get("reason"):
            err(where, "a %s source needs a reason" % rec.get("status"))
        if rec.get("status") == "acquired":
            for f in ("local_path", "retrieved_at", "sha256"):
                if not rec.get(f):
                    err(where, "an acquired source needs %s" % f)
        for key in ("found_by", "acquired_by"):
            if rec.get(key) and rec[key] not in steps:
                err(where, "%s %s is not a step" % (key, rec[key]))

    fmt = lambda d: ", ".join("%s %d" % kv for kv in sorted(d.items())) or "none"
    print("records: %d sessions, %d steps (%s; %s), %d sources"
          % (len(sessions), len(steps), fmt(by_actor), fmt(by_class), len(src_ids)))
    print("records: author steps by size: %s; %d words answered" % (fmt(h_sizes), h_words[0]))


def main():
    check_register()
    check_adr_index()
    check_handovers()
    check_links()
    check_superseded()
    check_records()

    if warnings:
        print("\n%d warning(s):" % len(warnings))
        for w in warnings:
            print("  ! %s" % w)
    if errors:
        print("\n%d error(s):" % len(errors))
        for e in errors:
            print("  x %s" % e)
        return 1
    print("\nOK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
