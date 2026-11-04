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
    """Parse a JSON Lines file; report and skip bad lines. A missing file is empty."""
    out = []
    if not os.path.exists(os.path.join(ROOT, rel)):
        return out
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
ASSET_REQUIRED = ("id", "kind", "source", "location", "status", "since")
INSTANCE_REQUIRED = ("id", "task_row", "subject", "allocation_version", "opened_by", "status")
AUDIT_REQUIRED = ("id", "session", "reviewer", "sample", "rubric_version", "disagreements")


def check_records():
    """The step log of ADR-0014 as amended after review: see docs/50_process/520_record-keeping.md."""
    rdir = os.path.join(ROOT, RECORDS_DIR)
    if not os.path.isdir(rdir):
        return
    vocab = json.loads(read(os.path.join(RECORDS_DIR, "vocabulary.json")))
    register_ids = set(m.group(1) for m in map(ROW_RE.match, read(REGISTER).splitlines()) if m)
    task_rows = set(int(n) for n in re.findall(r"^\| (\d+) \|", read(TASK_TABLE), re.M))
    data_types = set(vocab["data_task_types"])

    def enum(where, field, value, allowed):
        if value not in allowed:
            err(where, "%s %r not in vocabulary" % (field, value))

    def rel(name):
        return "%s/%s" % (RECORDS_DIR, name)

    sessions = {}
    for n, rec in _load_jsonl(rel("sessions.jsonl")):
        where = "records/sessions.jsonl line %d" % n
        for f in SESSION_REQUIRED:
            if f not in rec:
                err(where, "missing %s" % f)
        sessions[rec.get("id")] = rec

    instances = {}
    for n, rec in _load_jsonl(rel("task_instances.jsonl")):
        where = "records/task_instances.jsonl line %d [%s]" % (n, rec.get("id"))
        for f in INSTANCE_REQUIRED:
            if f not in rec:
                err(where, "missing %s" % f)
        if rec.get("task_row") not in task_rows:
            err(where, "task_row %r is not a row of 070" % rec.get("task_row"))
        enum(where, "status", rec.get("status"), vocab["task_instance_status"])
        instances[rec.get("id")] = rec

    assets = {}
    for n, rec in _load_jsonl(rel("assets.jsonl")):
        where = "records/assets.jsonl line %d [%s]" % (n, rec.get("id"))
        for f in ASSET_REQUIRED:
            if f not in rec:
                err(where, "missing %s" % f)
        enum(where, "kind", rec.get("kind"), vocab["asset_kind"])
        enum(where, "status", rec.get("status"), vocab["asset_status"])
        if rec.get("kind") == "source-file" and not rec.get("sha256"):
            err(where, "a source-file asset needs sha256")
        if rec.get("id") in assets:
            err(where, "duplicate asset id")
        assets[rec.get("id")] = rec

    acq_steps = sorted(r.get("acquired_by") for _, r in _load_jsonl(rel("sources.jsonl")) if r.get("acquired_by"))

    def epoch_start(step_id):
        """The acquisition step that opened the epoch this step falls in; '' before the first."""
        starts = [a for a in acq_steps if a <= step_id]
        return starts[-1] if starts else ""

    steps = {}
    by_actor, by_class = {}, {}
    responses, h_words, h_large = set(), [0], [0]
    step_files = sorted(f for f in os.listdir(os.path.join(rdir, "steps")) if f.endswith(".jsonl"))
    for fname in step_files:
        relf = "%s/steps/%s" % (RECORDS_DIR, fname)
        session = fname[:-len(".jsonl")]
        if session not in sessions:
            err(relf, "session %s is not in sessions.jsonl" % session)
        expect, last_ts = 1, None
        for n, rec in _load_jsonl(relf):
            where = "%s line %d [%s]" % (relf, n, rec.get("id"))
            missing = [f for f in STEP_REQUIRED if f not in rec]
            if missing:
                err(where, "missing %s" % ", ".join(missing))
                continue
            sid = rec["id"]
            contemporaneous = rec["recorded"] == "contemporaneous"
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
            elif contemporaneous:
                if last_ts and t < last_ts:
                    warn(where, "ts earlier than the previous contemporaneous step")
                last_ts = t
            if "ts_end" in rec and _ts(rec["ts_end"]) is None:
                err(where, "ts_end is not ISO 8601 with a UTC offset")
            for field in ("actor", "role", "tier", "work_class", "task_type", "outcome",
                          "ts_precision", "recorded"):
                enum(where, field, rec[field], vocab[field])
            faculty = vocab["agents"].get(rec["agent"])
            if faculty is None:
                err(where, "agent %r is not in vocabulary.agents" % rec["agent"])
            elif faculty != rec["actor"]:
                err(where, "agent %r is %s, but actor is %s" % (rec["agent"], faculty, rec["actor"]))

            # from S07: task_type is the subject, activity what was done (PRC-OP-6, S07-001)
            if session >= "S07":
                enum(where, "activity", rec.get("activity"), vocab["activity"])
                if rec["task_type"] in vocab["_task_type_as_activity"]:
                    err(where, "task_type %r is an activity from S07 on; use activity" % rec["task_type"])

            # people: verbatim, and effort by proxy, counted once per response
            if rec["actor"] == "H" and rec["role"] in ("request", "decide") and not rec.get("verbatim"):
                err(where, "a person's request or decision needs the verbatim field")
            if rec["actor"] == "H":
                he = rec.get("human_effort")
                if not he:
                    err(where, "a person's step needs human_effort")
                else:
                    act = he.get("activity")
                    enum(where, "human_effort.activity", act, vocab["human_activity"])
                    enum(where, "human_effort.size", he.get("size"), vocab["human_size"])
                    want = vocab["_size_by_activity"].get(act)
                    if want and he.get("size") != want:
                        err(where, "activity %r is size %s, not %s" % (act, want, he.get("size")))
                    rid = he.get("response_id")
                    if act in ("answer", "approve") and not rid:
                        err(where, "an answer or approval needs human_effort.response_id")
                    if rid and rid not in responses:
                        responses.add(rid)
                        if act == "answer":
                            if he.get("words") is None:
                                err(where, "the first step of response %s needs words" % rid)
                            elif rec.get("verbatim") and he["words"] != len(rec["verbatim"].split()):
                                err(where, "human_effort.words does not match the verbatim text")
                            h_words[0] += he.get("words") or 0
                    elif rid and he.get("words") is not None:
                        err(where, "response %s is already counted; only its first step carries words" % rid)
                    if he.get("size") == "large":
                        h_large[0] += 1
            elif rec.get("human_effort"):
                err(where, "human_effort on a step whose actor is not H")

            # decisions by machines state their basis
            if rec["role"] == "decide" and rec["actor"] in ("A", "D") and not rec.get("decision_basis"):
                err(where, "a decision by %s needs decision_basis" % rec["actor"])

            # task table, task instances, register
            if rec.get("task_row") is not None and rec["task_row"] not in task_rows:
                err(where, "task_row %r is not a row of 070" % rec["task_row"])
            ti = rec.get("task_instance")
            if ti is not None:
                if ti not in instances:
                    err(where, "task_instance %s is not in task_instances.jsonl" % ti)
                elif rec.get("task_row") != instances[ti]["task_row"]:
                    err(where, "task_row differs from its task instance's row")
            elif rec.get("task_row") is not None and contemporaneous:
                err(where, "a step with a task_row needs a task_instance")
            for rid in rec.get("register_rows", []):
                if rid not in register_ids:
                    err(where, "register row %s does not exist" % rid)
            ref = rec.get("initiated_by")
            if ref is not None and ref not in steps:
                err(where, "initiated_by %s is not an earlier step" % ref)

            # results
            if rec["outcome"] in ("blocked", "failed", "pending"):
                b = rec.get("blocker") or {}
                if not b.get("detail"):
                    err(where, "a %s step needs blocker.detail" % rec["outcome"])
            if rec.get("blocker"):
                enum(where, "blocker.category", rec["blocker"].get("category"), vocab["blocker"])
            for d in rec.get("defects", []):
                enum(where, "defect.type", d.get("type"), vocab["defect"])
                enum(where, "defect.severity", d.get("severity"), vocab["defect_severity"])
                enum(where, "defect.detected_stage", d.get("detected_stage"), vocab["detected_stage"])
                if not d.get("detail"):
                    err(where, "defect without detail")
            if rec["work_class"] == "rework":
                if not rec.get("rework_of"):
                    err(where, "a rework step needs rework_of")
                enum(where, "work_reason", rec.get("work_reason"), vocab["work_reason"])
            elif rec.get("work_reason") is not None:
                enum(where, "work_reason", rec["work_reason"], vocab["work_reason"])

            # the classification guard of the maintenance baseline (sol 1)
            if rec.get("trigger") is not None:
                enum(where, "trigger", rec["trigger"], vocab["trigger"])
            if rec.get("trigger") in ("refresh", "check-failure") and rec["work_class"] not in ("maintain", "rework"):
                err(where, "work triggered by %s is maintain, not %s" % (rec["trigger"], rec["work_class"]))
            for a in rec.get("assets_modified", []):
                since = assets.get(a, {}).get("since")
                if since and since < epoch_start(sid) and rec["work_class"] not in ("maintain", "rework"):
                    err(where, "modifies %s, which predates this epoch: maintain, not %s" % (a, rec["work_class"]))

            # data lineage, from the first acquired source on
            if rec["task_type"] in data_types and contemporaneous:
                if not rec.get("assets"):
                    err(where, "a %s step needs assets" % rec["task_type"])
                if rec["role"] == "check":
                    c = rec.get("check") or {}
                    enum(where, "check.type", c.get("type"), vocab["check_type"])
                    for f in ("expected", "observed", "evidence"):
                        if f not in c:
                            err(where, "check needs %s" % f)
            for a in rec.get("assets", []) + rec.get("assets_modified", []):
                if a not in assets:
                    err(where, "asset %s is not in assets.jsonl" % a)

            eff = rec.get("effort", {})
            if "human_basis" in eff:
                enum(where, "effort.human_basis", eff["human_basis"], vocab["human_basis"])
            for tool in eff.get("tool_calls", {}):
                enum(where, "instrument", tool, vocab["instruments"])
            by_actor[rec["actor"]] = by_actor.get(rec["actor"], 0) + 1
            by_class[rec["work_class"]] = by_class.get(rec["work_class"], 0) + 1

    # references that may point forward
    for sid, rec in steps.items():
        where = "records step %s" % sid
        for d in rec.get("defects", []):
            for key in ("found_by", "fixed_by"):
                if d.get(key) and d[key] not in steps:
                    err(where, "defect.%s %s is not a step" % (key, d[key]))
        if rec.get("rework_of") and rec["rework_of"] not in steps:
            err(where, "rework_of %s is not a step" % rec["rework_of"])
        val = rec.get("validation")
        if val:
            enum(where, "validation.status", val.get("status"), vocab["validation_status"])
            chk = steps.get(val.get("by"))
            if chk is None:
                err(where, "validation.by %s is not a step" % val.get("by"))
            elif chk["role"] != "check":
                err(where, "validation.by %s is not a check step" % val.get("by"))
            elif chk["agent"] == rec["agent"]:
                err(where, "validated by its own agent %s" % rec["agent"])
    for tid, ti in instances.items():
        if ti.get("opened_by") not in steps:
            err("records/task_instances.jsonl [%s]" % tid, "opened_by is not a step")
    for aid, a in assets.items():
        if a.get("since") not in steps:
            err("records/assets.jsonl [%s]" % aid, "since is not a step")

    src_ids, acquired = set(), 0
    for n, rec in _load_jsonl(rel("sources.jsonl")):
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
            acquired += 1
            for f in ("local_path", "retrieved_at", "sha256", "acquired_by"):
                if not rec.get(f):
                    err(where, "an acquired source needs %s" % f)
        for key in ("found_by", "acquired_by"):
            if rec.get(key) and rec[key] not in steps:
                err(where, "%s %s is not a step" % (key, rec[key]))
    for aid, a in assets.items():
        if a.get("source") not in src_ids:
            err("records/assets.jsonl [%s]" % aid, "source %s is not in sources.jsonl" % a.get("source"))
    for aid, a in assets.items():
        for dep in a.get("depends_on", []):
            if dep not in assets:
                err("records/assets.jsonl [%s]" % aid, "depends_on %s is not an asset" % dep)

    bpath = os.path.join(rdir, "maintenance_baseline.json")
    baseline = None
    if os.path.exists(bpath):
        baseline = json.loads(read(os.path.join(RECORDS_DIR, "maintenance_baseline.json")))
        for f in ("status", "epoch", "service_commitment", "stable_units", "effort", "burden_indicators",
                  "tolerances", "limits"):
            if f not in baseline:
                err("records/maintenance_baseline.json", "missing %s" % f)
        if baseline.get("status") not in ("draft", "ruled"):
            err("records/maintenance_baseline.json", "status must be draft or ruled")
        if baseline.get("status") == "ruled" and baseline.get("ruled_by") not in steps:
            err("records/maintenance_baseline.json", "a ruled baseline needs ruled_by, an existing step")
    if acquired > 1 and (baseline is None or baseline.get("status") != "ruled"):
        err(RECORDS_DIR, "a second source is acquired but records/maintenance_baseline.json is missing or "
                         "not ruled by the author — CON-OP-16 precondition")

    # the blind session-close audit
    audited = set()
    for n, rec in _load_jsonl(rel("audits.jsonl")):
        where = "records/audits.jsonl line %d [%s]" % (n, rec.get("id"))
        for f in AUDIT_REQUIRED:
            if f not in rec:
                err(where, "missing %s" % f)
        if vocab["agents"].get(rec.get("reviewer")) != "A" or rec.get("reviewer") == "claude-opus-5-5":
            err(where, "the auditor must be a different model from the recorder")
        for s in rec.get("sample", []):
            if s not in steps:
                err(where, "sampled step %s does not exist" % s)
        audited.add(rec.get("session"))
    for sid, s in sessions.items():
        if s.get("logged") and s.get("closed") and sid not in audited:
            err("records/sessions.jsonl [%s]" % sid, "a closed session needs a blind audit in audits.jsonl")

    fmt = lambda d: ", ".join("%s %d" % kv for kv in sorted(d.items())) or "none"
    print("records: %d sessions, %d steps (%s; %s), %d sources (%d acquired), %d assets, %d task instances"
          % (len(sessions), len(steps), fmt(by_actor), fmt(by_class), len(src_ids), acquired, len(assets),
             len(instances)))
    if baseline is not None:
        print("records: maintenance baseline is %s" % baseline.get("status"))
    print("records: author %d responses, %d words, %d large acts" % (len(responses), h_words[0], h_large[0]))

ACROSS_ITEMS = {"reconciliations": {"16"}, "processes": {"24"}, "terms": {"25"}, "entities": {"26"}}


def check_analysis():
    """The information-analysis record of ADR-0018: see analysis/README.md."""
    adir = os.path.join(ROOT, "analysis")
    if not os.path.isdir(adir):
        return
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import ia_lib as ia
    vocab = json.loads(read(os.path.join(RECORDS_DIR, "vocabulary.json")))
    agents = set(vocab["agents"])
    n_items = n_claims = n_evidence = 0
    for dirpath, dirnames, filenames in os.walk(adir):
        rel_dir = os.path.relpath(dirpath, ROOT).replace(os.sep, "/")
        names = dirnames + filenames
        lowered = {}
        for name in names:
            lowered.setdefault(name.lower(), []).append(name)
        for group in lowered.values():
            if len(group) > 1:
                err(rel_dir, "names differ only in case: %s" % ", ".join(group))
        parts = rel_dir.split("/")
        under_tables = "tables" in parts
        under_rel = "across" in parts and "relations" in parts
        kind = next((k for k in ("reconciliations", "processes", "terms", "entities") if k in parts), None)
        under_rec = "across" in parts and kind is not None
        if under_rec and parts[-1] == kind:
            for d in dirnames:
                if not re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", d):
                    err("%s/%s" % (rel_dir, d), "a %s folder is named by a lower-case slug (analysis/README.md 9)" % kind)
        if under_rel and parts[-1] == "relations":
            for d in dirnames:
                if ia.parse_relation(d) is None:
                    err("%s/%s" % (rel_dir, d), "folder name is not a relation name of escaped parts (analysis/README.md 3, 9)")
        for d in dirnames:
            if under_tables and not ia.is_escaped(d):
                err("%s/%s" % (rel_dir, d), "folder name is not a reversibly escaped source name (ADR-0018)")
        for f in filenames:
            rel = "%s/%s" % (rel_dir, f)
            path = os.path.join(dirpath, f)
            if rel == "analysis/README.md":
                continue
            if parts[-1] == "evidence":
                m = ia.EVIDENCE_RE.match(f)
                if not m:
                    err(rel, "an evidence file is named <16 hex digits>.json")
                    continue
                try:
                    with open(path, encoding="utf-8") as fh:
                        rec = json.load(fh)
                except ValueError as e:
                    err(rel, "not JSON: %s" % e)
                    continue
                n_evidence += 1
                if rec.get("id") != m.group(1):
                    err(rel, "id does not match the file name")
                if ia.evidence_hash(rec) != m.group(1):
                    err(rel, "content hash does not match the file name: edited after writing?")
                for k in ("kind", "tool", "inputs", "ran_at", "result"):
                    if k not in rec:
                        err(rel, "evidence lacks %r" % k)
                if not (rec.get("code") or rec.get("query") or rec.get("excerpt")):
                    err(rel, "evidence holds no code, query or excerpt")
                continue
            under_source = "_source" in parts
            if not (under_tables or under_source or under_rel or under_rec) or not f.endswith(".md"):
                continue
            m = ia.ITEM_FILE_RE.match(f)
            if not m:
                err(rel, "an item file is named <nn>_<slug>.md")
                continue
            nn, slug = m.groups()
            is_column = "columns" in parts
            if ia.ITEMS.get(nn) != slug:
                err(rel, "item %s is %r, not %r" % (nn, ia.ITEMS.get(nn), slug))
            allowed = (ia.RELATION_ITEMS if under_rel else ACROSS_ITEMS[kind] if under_rec else ia.SOURCE_ITEMS if under_source else
                       ia.COLUMN_ITEMS if is_column else ia.TABLE_ITEMS)
            if nn not in allowed:
                err(rel, "item %s is not recorded at this level" % nn)
            text = read(rel)
            if any(ord(ch) > 127 for ch in text):
                warn(rel, "non-ASCII characters; allowed only inside values quoted from the source")
            front, claims, perrs = ia.parse_item(text)
            for e in perrs:
                err(rel, e)
            n_items += 1
            n_claims += len(claims)
            for k in ia.FRONT_KEYS:
                if k not in front:
                    err(rel, "front matter lacks %r" % k)
            if front.get("item") != nn or front.get("topic") != slug:
                err(rel, "item and topic must match the file name")
            if front.get("tier") not in ia.TIERS:
                err(rel, "tier %r not in %s" % (front.get("tier"), sorted(ia.TIERS)))
            elif (nn in ia.RELATION_MINIMUM if under_rel else nn in ia.MINIMUM) and front.get("tier") != "minimum":
                err(rel, "item %s is a minimum item (ADR-0017)" % nn)
            for k in ("written_by", "last_checked_by"):
                if front.get(k) not in agents:
                    err(rel, "%s %r is not an agent in records/vocabulary.json" % (k, front.get(k)))
            for k in ("written_at", "last_checked_at"):
                if not _ts((front.get(k) or "").replace("Z", "+00:00")):
                    err(rel, "%s needs an ISO time with a zone" % k)
            if not re.match(r"^S\d\d-\d{3}$", front.get("step", "")):
                err(rel, "step must be a step-log id")
            if str(len(claims)) != front.get("claims"):
                err(rel, "claims: says %s, the file has %d" % (front.get("claims"), len(claims)))
            if not claims:
                err(rel, "an item file holds at least one claim")
            ev_dir = os.path.join(os.path.dirname(path) if not is_column else
                                  os.path.join(dirpath, "..", ".."), "evidence")
            ev_have = set(x[:-5] for x in os.listdir(ev_dir)) if os.path.isdir(ev_dir) else set()
            seen = set()
            lowest = None
            for c in claims:
                w = "%s#%s" % (rel, c["id"])
                if c["id"] in seen:
                    err(w, "claim id repeated")
                seen.add(c["id"])
                for k in ia.CLAIM_KEYS:
                    if k not in c:
                        err(w, "claim lacks %r" % k)
                if c.get("type") not in ia.CLAIM_TYPES:
                    err(w, "type %r not allowed" % c.get("type"))
                if c.get("status") not in ia.STATUSES:
                    err(w, "status %r not allowed" % c.get("status"))
                if c.get("confidence") not in ia.CONFIDENCE:
                    err(w, "confidence %r not allowed" % c.get("confidence"))
                elif c.get("status") not in ("superseded", "retracted"):
                    rank = ia.CONFIDENCE.index(c["confidence"])
                    lowest = rank if lowest is None else min(lowest, rank)
                for e in (c.get("evidence") or "none").split(","):
                    e = e.strip()
                    if e != "none" and e not in ev_have:
                        err(w, "evidence %s not found in %s" % (e, os.path.relpath(ev_dir, ROOT)))
            if lowest is not None and front.get("confidence") != ia.CONFIDENCE[lowest]:
                err(rel, "confidence must be the lowest among live claims (%s)" % ia.CONFIDENCE[lowest])
    print("analysis: %d item files, %d claims, %d evidence files" % (n_items, n_claims, n_evidence))


def _cite_ok(path):
    """A citation `path` or `path#Cn` resolves to an existing file and, if given, an existing claim line."""
    p, _, claim = path.partition("#")
    full = os.path.join(ROOT, p)
    if os.path.isdir(full) and not claim:
        return True
    if not os.path.isfile(full):
        return False
    if not claim or not claim.startswith("C"):
        return True
    return ("\n- %s |" % claim) in read(p)


def check_model():
    """The model declarations under model/ (model/README.md, proposed under ARC-OP-29)."""
    if not os.path.isdir(os.path.join(ROOT, "model")):
        return
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import model_lib as ml
    vocab = json.loads(read(os.path.join(RECORDS_DIR, "vocabulary.json")))
    agents = set(vocab["agents"])
    adrs = {f[:8].replace("-", "-") for f in os.listdir(os.path.join(ROOT, ADR_DIR)) if re.match(r"^\d{4}-", f)}
    adrs = {"ADR-" + a[:4] for a in adrs}
    decls = ml.load(ROOT)
    by_name, by_id, all_names = {}, {}, {}
    for rel, front, sections, prose, errs in decls:
        for e in errs:
            err(rel, e)
        kind = front.get("kind")
        if kind not in ml.REQUIRED:
            err(rel, "unknown kind %r" % kind)
            continue
        if not rel.startswith(ml.KINDS[kind] + "/"):
            err(rel, "a %s belongs under %s/" % (kind, ml.KINDS[kind]))
        for k in ml.REQUIRED[kind]:
            if not front.get(k):
                err(rel, "front matter lacks %s" % k)
        for s in ml.SECTIONS[kind]:
            if not sections.get(s):
                err(rel, "section %s missing or empty" % s)
        name, ident = front.get("name", ""), front.get("id", "")
        if not ml.NAME_RE[kind].match(name):
            err(rel, "name %r does not follow the %s naming pattern" % (name, kind))
        if os.path.basename(rel) != name + ".md":
            err(rel, "file name differs from name %r" % name)
        if not ident.startswith(ml.ID_PREFIX[kind]):
            err(rel, "id %r lacks the prefix %s" % (ident, ml.ID_PREFIX[kind]))
        for alias in ml.split_list(front.get("aliases", "")):
            if alias in all_names:
                err(rel, "alias %r is also used by %s; a name is never reused" % (alias, all_names[alias]))
            all_names[alias] = rel
        if name in all_names and all_names[name] != rel:
            err(rel, "name %r is also an alias or name in %s; a name is never reused" % (name, all_names[name]))
        all_names[name] = rel
        for key, seen in ((name, by_name), (ident, by_id)):
            if key in seen:
                err(rel, "%r also declared in %s" % (key, seen[key][0]))
            seen[key] = (rel, front, sections)
        if front.get("status") not in ml.STATUSES:
            err(rel, "status %r not one of %s" % (front.get("status"), sorted(ml.STATUSES)))
        if front.get("written_by") not in agents:
            err(rel, "written_by %r is not a known agent" % front.get("written_by"))
        for a in ml.split_list(front.get("ruled_in", "")):
            if a not in adrs:
                err(rel, "ruled_in %s is not an ADR on disk" % a)
        if front.get("defined_in"):
            p = front["defined_in"].split("#")[0].split(" ")[0]
            if not os.path.isfile(os.path.join(ROOT, p)):
                err(rel, "defined_in %s does not exist" % p)
        if "class" in front and front["class"] not in ml.CLASSES:
            err(rel, "class %r not one of %s" % (front["class"], sorted(ml.CLASSES)))
        for subj, _ in sections.get("Evidence", []) + sections.get("Relations", []):
            if not _cite_ok(subj):
                err(rel, "citation does not resolve: %s" % subj)

    # The source: base tables, their catalogues and the columns handled by rule.
    sources = {f["name"]: (r, f, s) for r, f, s, p, e in decls if f.get("kind") == "source"}
    cats, rule_cols, ref_sources = {}, {}, set()
    for r, f, s, p, e in decls:
        if f.get("kind") == "reference":
            ref_sources.add(f.get("source_table"))
    for sname, (rel, front, sections) in sources.items():
        if front.get("key_case") not in ("fold", "exact"):
            err(rel, "key_case must be fold or exact (143 section 3 item 4, ADR-0037)")
        for table, flags in sections.get("Base tables", []):
            cpath = flags.get("catalogue", "")
            if not os.path.isfile(os.path.join(ROOT, cpath)):
                err(rel, "%s: catalogue %s missing" % (table, cpath))
                continue
            if flags.get("extract") not in ("full", "delta"):
                err(rel, "%s: extract must be full or delta" % table)
            cat = ml.catalogue(ROOT, cpath)
            cats[table] = {c["column_name"]: c for c in cat["columns"]}
            by_rule = set()
            st = flags.get("system_time", "none")
            if st != "none":
                by_rule |= set(ml.split_list(st))
            if flags.get("audit", "none") != "none" and table not in ref_sources:
                by_rule.add(flags["audit"])
            for c in by_rule:
                if c not in cats[table]:
                    err(rel, "%s: rule column %s not in the catalogue" % (table, c))
            rule_cols[table] = by_rule

    def qualified(rel, value):
        parts = value.split(".")
        if len(parts) != 3 or ".".join(parts[:2]) not in cats or parts[2] not in cats[".".join(parts[:2])]:
            err(rel, "column %r is not a column of a declared base table" % value)
            return None
        return ".".join(parts[:2]), parts[2]

    places = {}   # (table, column) -> [(place, file, flags)]

    def place(tc, what, rel, flags=None):
        if tc:
            places.setdefault(tc, []).append((what, rel, flags or {}))

    link_cols = {}
    for rel, front, sections, prose, errs in decls:
        kind = front.get("kind")
        if kind == "hub":
            for subj, flags in sections.get("Business key", []):
                for comp in subj.split(" + "):   # one line per mapping; " + " joins the parts of a composite key
                    place(qualified(rel, comp.strip()), "key", rel)
                if not flags.get("key_space") or not flags.get("key_kind"):
                    err(rel, "business key %s lacks key_space or key_kind" % subj)
        elif kind == "link":
            for end in ("from", "to"):
                tgt = by_name.get(front.get(end, ""))
                if not tgt or tgt[1].get("kind") != "hub":
                    err(rel, "%s %r is not a declared hub" % (end, front.get(end)))
            if front.get("driving") not in ("none", front.get("from")):
                err(rel, "driving must be the from hub or none")
            if front.get("optional") not in ("yes", "no"):
                err(rel, "optional must be yes or no")
            if front.get("effectivity") not in ml.EFFECTIVITY:
                err(rel, "effectivity %r not one of %s" % (front.get("effectivity"), sorted(ml.EFFECTIVITY)))
            maps = {}
            for subj, flags in sections.get("Columns", []):
                if "kept" in flags:
                    place(qualified(rel, subj), "kept", rel, flags)
                    continue
                end = flags.get("end")
                if end not in ("from", "to"):
                    err(rel, "%s: end must be from or to" % subj)
                    continue
                comps = [c.strip() for c in subj.split(" + ")]
                tabs = {c.rsplit(".", 1)[0] for c in comps}
                if len(tabs) != 1:
                    err(rel, "%s: the components of one endpoint come from one table" % subj)
                    continue
                maps.setdefault(tabs.pop(), {}).setdefault(end, []).append((comps, flags))
                hub = by_name.get(front.get(end, ""))
                nkey = len(hub[2].get("Business key", [("", {})])[0][0].split(" + ")) if hub else 0
                if hub and len(comps) != nkey:
                    err(rel, "%s: %d components, but %s has a %d-part business key" % (subj, len(comps), front.get(end), nkey))
                for c in comps:
                    tc = qualified(rel, c)
                    place(tc, "link-" + end, rel, flags)
                    if tc and end == "to":
                        link_cols[tc] = (front.get("name"), front.get("optional"))
                if end == "from":
                    st = flags.get("effectivity_start", "")
                    if not st:
                        err(rel, "%s: the from line carries effectivity_start" % subj)
                    elif front.get("effectivity") in ("event", "milestone") and st != "unknown":
                        qualified(rel, st)
            if not maps:
                err(rel, "no mapping: a link needs a from and a to line from one source table")
            for t, ends in maps.items():
                if len(ends.get("from", [])) != 1 or len(ends.get("to", [])) != 1:
                    err(rel, "mapping from %s needs exactly one from and one to line" % t)
        elif kind == "satellite":
            par = by_name.get(front.get("parent", ""))
            if not par or par[1].get("kind") not in ("hub", "link"):
                err(rel, "parent %r is not a declared hub or link" % front.get("parent"))
            table = front.get("source_table", "")
            if table not in cats:
                err(rel, "source_table %s is not a declared base table" % table)
                continue
            if front.get("satellite_kind") not in ml.SAT_KINDS:
                err(rel, "satellite_kind %r not one of %s" % (front.get("satellite_kind"), sorted(ml.SAT_KINDS)))
            pkv = front.get("parent_key", "")
            if par and par[1].get("kind") == "link":
                comps = [x.split("=", 1)[1] for x in ml.split_list(pkv) if "=" in x]
            else:
                comps = [x.strip() for x in pkv.split(" + ")]
                if par and par[1].get("kind") == "hub":
                    nkey = len(par[2].get("Business key", [("", {})])[0][0].split(" + "))
                    if len(comps) != nkey:
                        err(rel, "parent_key has %d components, %s a %d-part business key" % (len(comps), par[1]["name"], nkey))
            for c in comps:
                place(qualified(rel, c), "parent_key", rel)
            vt = front.get("valid_time", "")
            if vt.split(" ")[0] not in ("unknown", "none;", "none") and "." in vt.split(" ")[0]:
                qualified(rel, vt.split(" ")[0])
            for subj, flags in sections.get("Columns", []):
                if subj not in cats[table]:
                    err(rel, "column %s is not in %s" % (subj, table))
                    continue
                place((table, subj), "sat", rel, flags)
                if "code" in flags and flags["code"] not in by_name:
                    err(rel, "%s: code %r is not a declared reference table" % (subj, flags["code"]))
                if "as_delivered" in flags and flags["as_delivered"] not in by_name:
                    err(rel, "%s: as_delivered %r is not a declared link" % (subj, flags["as_delivered"]))
        elif kind == "reference":
            table = front.get("source_table", "")
            if table not in cats:
                err(rel, "source_table %s is not a declared base table" % table)
                continue
            place(qualified(rel, front.get("key", "")), "key", rel)
            for subj, flags in sections.get("Columns", []):
                if subj not in cats[table]:
                    err(rel, "column %s is not in %s" % (subj, table))
                    continue
                place((table, subj), "ref", rel, flags)

    # Coverage: every column of every base table has exactly one disposition (model/README.md, section 6).
    n_cols = 0
    for table, cols in cats.items():
        for c in cols:
            n_cols += 1
            ps = list(places.get((table, c), []))
            if c in rule_cols.get(table, set()):
                ps.append(("rule", "model/sources", {}))
            kinds = [p[0] for p in ps]
            where = "model: %s.%s" % (table, c)
            if not ps:
                err(where, "has no disposition in the model (hub key, link endpoint, satellite, reference or rule)")
                continue
            sats = [p for p in ps if p[0] == "sat"]
            if len([p for p in sats if "repeats" not in p[2]]) > 1:
                err(where, "in more than one satellite: %s" % ", ".join(p[1] for p in sats))
            lk = link_cols.get((table, c))
            for p in sats:
                if lk and lk[1] == "no":
                    err(where, "mandatory relationship of %s also in satellite %s (149 Rule 5)" % (lk[0], p[1]))
                elif lk and "as_delivered" not in p[2]:
                    err(where, "an endpoint of %s and in %s without as_delivered" % (lk[0], p[1]))
                elif not lk and "as_delivered" in p[2]:
                    err(where, "as_delivered, but no link has the column as an endpoint")
            if lk and lk[1] == "yes" and not any(p[2].get("as_delivered") == lk[0] for p in sats):
                err(where, "optional relationship of %s not kept as delivered in a satellite (149 Rule 5)" % lk[0])
            # One disposition per column; reuse is legal only in these patterns (model/README.md section 6).
            used = frozenset(k for k in kinds if not (k == "sat" and lk))
            legal = [{"key"}, {"key", "link-from"}, {"key", "parent_key"}, {"key", "link-from", "parent_key"},
                     {"rule"}, {"ref"}, {"sat"}, {"link-to"}, {"link-from"}, {"link-from", "link-to"}, {"kept"},
                     {"parent_key"}]
            if set(used) not in legal:
                err(where, "uses %s are not one disposition: %s" % (
                    "+".join(sorted(used)), ", ".join("%s in %s" % (p[0], p[1]) for p in ps)))
            if kinds.count("key") > 1 or kinds.count("rule") > 1 or kinds.count("ref") > 1:
                err(where, "declared more than once: %s" % ", ".join("%s in %s" % (p[0], p[1]) for p in ps))
    hp = places.get(("Application.People", "HashedPassword"), [])
    if cats and not any(p[2].get("load", "").startswith("never") for p in hp):
        err("model: Application.People.HashedPassword", "must be declared load=never (ADR-0033 decision 2)")
    counts = {}
    for r, f, s, p, e in decls:
        counts[f.get("kind")] = counts.get(f.get("kind"), 0) + 1
    print("model: %d hubs, %d links, %d satellites, %d reference tables, %d sources; %d source columns placed"
          % (counts.get("hub", 0), counts.get("link", 0), counts.get("satellite", 0), counts.get("reference", 0),
             counts.get("source", 0), n_cols))


def main():
    check_register()
    check_adr_index()
    check_handovers()
    check_links()
    check_superseded()
    check_records()
    check_analysis()
    check_model()

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
