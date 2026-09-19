#!/usr/bin/env python3
"""Mechanical checks for the nsdn repository.

Written against the standing rule in docs/50_process/500_working-method.md:

    A newly-written rule is unenforced until something mechanical enforces it.
    Write the check, not the sentence.

Run from the repository root:

    python tools/check_repo.py

Exits nonzero if any check fails. Warnings do not fail the run.
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REGISTER = "registers/OPEN_POINTS.md"
ADR_DIR = "docs/20_decisions"
ADR_INDEX = "docs/20_decisions/README.md"
HANDOVER_DIR = "handovers"

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


def main():
    check_register()
    check_adr_index()
    check_handovers()
    check_links()
    check_superseded()

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
