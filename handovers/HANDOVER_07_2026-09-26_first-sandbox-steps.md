# nsdn — Handover 07: the sandbox started, every step was logged, and the log says where it cannot be trusted
## Written 2026-09-26 at the close of session 06

> **STATUS: CURRENT.**

---

## First actions

1. `git log --oneline -15` — expect HEAD at the commit that wrote this handover, on top of `f5c983d`.
2. `python tools/check_repo.py` — must pass. Expect 58 register rows, 14 ADRs, 6 sessions (S06 closed and
   audited), 124 steps, 17 sources (5 acquired), 17 assets. **Run it on its own, never piped:** session 06
   committed once with a failing check because `| tail` hid the exit status.
3. Read [the session 06 post-mortem](../docs/30_research/notes/2026-09-26-session-06-post-mortem.md) — eight
   lessons, all computed from the log — then register rows `PRC-OP-6`, `EVI-OP-2`, `CON-OP-16` and `ARC-OP-24`.
4. **Open a new step file**, `records/steps/S07.jsonl`, add S07 to `records/sessions.jsonl` with
   `allocation_version` set to the current commit of 070, and log from the first step. The spec is
   [520](../docs/50_process/520_record-keeping.md); read its *Added after review* section.

## Outstanding actions for the author, not the model

**Push.** About thirty commits of session 06 are local only.

**Rule the two open classification fixes** (lesson 2 of the post-mortem): split task type into activity and
subject; and decide how coordination steps — his approvals, the model's reports — are classed.

## How to work with the author

Unchanged from handover 06, and confirmed again: **plain English, numbered**; propose, let him react, write
what he settles; quote him verbatim; external review on sol and astra in parallel. Two additions from this
session:

**Keep the apparatus small.** His words: "let's not make it too serious yet, we're still putting our feelers
out" and "this whole system also suffers from the same things described in Generative Structures, so let's
not make it too large." When a review returns many findings, integrate lightly and enforce only the one
that matters most.

**Put decisions to him as decisions.** In session 06 the model made every matching choice and the author
only did lookups (lesson 3). If a choice is his by 070 — meaning, identity, what counts — ask.

**Sheets for him are .xlsx with an unmistakable name.** A CSV next to another CSV invited his entries into
the wrong file, and Dutch-locale Excel rewrote its coordinates. **Ask before overwriting any file he has just
touched** — he stopped the model once for not asking.

## What session 06 did

Re-themed the sandbox to businesses in the Utrecht region, at the author's request: his interest in firm
types and turnover, underserved BI/analytics/AI markets, businesses for sale and e-commerce opportunities
(`EVI-OP-2`). No money is to be spent on it. Built the step log ([ADR-0014](../docs/20_decisions/0014-step-log.md))
and the maintenance baseline (`records/maintenance_baseline.json`, ruled provisionally), each failed on first
review and repaired. Acquired PAR, OSM, DUO, LRK and RDW; matched OSM businesses to PAR establishments in three
versions ([`../prototypes/par_osm_match/`](../prototypes/par_osm_match/README.md)); measured them against a
blind answer key and the three registers
([`../prototypes/register_check/check.py`](../prototypes/register_check/check.py)); closed with a blind audit.

**The data, briefly.** PAR (`SRC-012`) is anonymous — location, sector class, size code, start date; no
name, KvK number or address — and in substance the 1 April 2022 register despite its 2024 title; its size
codes are undocumented and the author declined to ask the province. OSM (`SRC-014`) gives 17,279 named
businesses, 70% with a website. The free KvK search gives neither SBI code nor start date. All raw data sits
under the git-ignored `data/`, every file hashed in `records/assets.jsonl`.

## Task for the next session, in one sentence

Deal with the time gap: treat businesses that demonstrably started after 1 April 2022 as absent from PAR,
and re-measure — after first making the two classification fixes if the author has ruled them.

## Why that task and not another

Data age is the dominant error in every measurement so far (lesson 5), and it is cheap to address with what is
already on disk (LRK registration dates; possibly KvK number ranges, unverified). The alternatives, in the
author's order of interest if he prefers: move towards his prospect list (the ~6,800 unique matches carry PAR
size class and sector, most with a website — but website checks need network access neither environment
has); or design the comparison that isolates what the model adds beyond rule tables (`EVI-OP-1`).

## Traps and warnings

**No Dutch data source is reachable from either environment.** Geofabrik, DUO, LRK, RDW, KvK, the province —
all blocked from the cloud workspace and the computer's shell. Every acquisition is a large act for the
author. Batch requests for downloads.

**The cloud workspace is reclaimed overnight.** Anything processed there must be written back to the computer
the same session. osmium and pyproj install there, not on the computer.

**The checker forces `maintain` for work triggered by a refresh or a failed check.** The auditor disagreed
once (a restore it called rework). That rule stays until the author changes it.

**`validation` needs a check step by a different agent.** A matcher run cannot be validated by a check the same
program ran; the checker refuses it.

**Do not de-anonymise business-for-sale listings; name no individuals.** Both guards proposed in session 06 and
not formally ruled; the LRK file contains childminders' home addresses and contact persons, which are not to
be read.

**"Right kind" in the register check is partly circular for schools.** The class rule selects the class the
check expects; the informative figures are wrong-kind proposals, post-2022 cases and dates.

## Do not reopen

Everything in handover 06's list, plus:

- Every step is logged, classified, and validated by the checker — [ADR-0014](../docs/20_decisions/0014-step-log.md).
- The author's effort is recorded as answers, words and small or large acts, never as time — his ruling in
  [520](../docs/50_process/520_record-keeping.md).
- The sandbox is the Utrecht business landscape, and costs no money — `EVI-OP-2`.
- A blind audit by another model gates each session's close — 520, enforced.

## What session 06 did not do

Did not refresh any source, so no epoch is comparable and `CON-OP-16` is not computable. Did not isolate what
the model adds. Did not check websites, estimate turnover, or produce any prospect list. Did not rule the
two guards or the classification fixes. Did not resolve PAR's size codes.
