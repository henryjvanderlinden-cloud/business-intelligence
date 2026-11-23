# nsdn — Handover 14: the first slice runs from extract to answer; a second, messy source with an answer key is next
## Written 2026-11-17 at the close of session 13

> **STATUS: HISTORICAL (superseded 2026-11-23 by [handover 15](HANDOVER_15_2026-11-23_second-source-built-e1-frozen-matching-next.md))**

---

## First actions

1. `git status`, then `git log --oneline -15`. Expect HEAD at the commit that closed S13 (message begins "Close session
   13"). The author pushes himself; if `origin/main` is behind, say so, do not push.
2. `python tools/check_repo.py` on a copy (on the desktop's shell it is slow; see *Traps*). It passes with the known
   warnings in `S07.jsonl`. Expect 13 sessions, S13 closed with `AUD-S13-1`, 40 ADRs, one decision (`DEC-0001`).
3. `python prototypes/vault_generator/generate.py --check`: 590 generated files, 0 problems.
4. Read, in this order: this handover; [410](../docs/40_roadmap/410_first-vertical-slice.md) (the falsifiable core);
   `EVI-OP-1`, `EVI-OP-2` and `EVI-OP-7` in the register; [420](../docs/40_roadmap/420_next-sandbox-setup.md);
   the [post-mortem of session 06](../docs/30_research/notes/2026-09-26-session-06-post-mortem.md) lesson 5 (the
   Utrecht answer key); the [general assessment](../docs/30_research/notes/2026-11-14-general-assessment.md) points 6,
   7 and 18; [144](../docs/10_architecture/144_raw-vault-business-vault-calculation-engines.md) §3 (several sources,
   proposed, not ruled) and `ARC-OP-37` item 2.
5. Ask the sandbox job for its status (handover 08, *Driving the sandbox*). Expect simulated date 2016-06-06 and the
   runner `loaded`, `last_ok_date` 2016-06-06, its last good project equal to the current one. 8.6 GB was free on
   2026-11-17, after the author pushed the S13 commits and deleted the two old warehouse copies; he set the open points
   below for the next session.
6. Open session S14 in `records/sessions.jsonl` and log from S14-001.

## Where we stand

Session 13 ran from 2026-11-15 to 2026-11-17: on Claude Fable 5.2 until 2026-11-16, then on Claude Opus 5.5.

- **The first slice is built and live** (point 17 of the assessment, landed). The author picked the question, sales
  over time by customer segment, and ruled where marts read from, where sales excluding tax is derived, that a
  segment is shown as currently known, and the decision it serves
  ([ADR-0039](../docs/20_decisions/0039-first-use-case-and-where-marts-read-from.md)); then that unplaced lines stay
  visible, that "as known on" is a replay, and that the decision register is one file per decision
  ([ADR-0040](../docs/20_decisions/0040-the-first-slice-design.md)). Design in
  [141](../docs/10_architecture/141_the-first-slice-business-vault-and-mart.md), built by
  [`generate_marts.py`](../prototypes/vault_generator/generate_marts.py), generator **0.4.1**: six point-in-time
  tables, two bridges, one computed satellite, two dimensions, one fact table at invoice-line grain, one analysis;
  each a table and an `__as_known(known_on)` table macro; 48 tests for the slice, 831 per load.
- **The answer** is the first findings note,
  [`findings/DEC-0001/2026-11-17_sales-by-customer-segment.md`](../findings/DEC-0001/2026-11-17_sales-by-customer-segment.md):
  growth stopped in 2016; the two buying groups carry 63% of sales and grow slowest; margin is about 50% in every
  segment, partly because the source's profit is at today's cost. WWI is generated data, which the note says.
- **Reviewed twice on sol, both first versions failing**: the design (five findings, applied) and the code (five
  findings, three real and applied, two resting on a state the raw vault excludes and guarded anyway). The paths no
  simulated day had produced (an invoice gone, a customer gone and back, a buying group ended, a customer known only
  from history) were exercised on constructed days by
  [`test_slice.py`](../prototypes/vault_generator/test_slice.py): all checks pass (141 §11 items 7 and 8).
- **The decision register** exists (`registers/decisions/`), and so does `findings/`. `README.md`, `AGENTS.md` and
  400 say what is built. The phase gate of 400 is still undecided.
- The falsifiable core of 410 is still untested: WWI is one clean source with declared keys.

## Task for the next session, in one sentence

Add a second, messy source with an answer key, so that whether business keys and entity identity across sources can be
machine-proposed at a useful precision (410) is tested for the first time, and the generator meets a second source,
as the author ruled on 2026-11-15 ("do them in that order", `PRC-OP-10`, point 18).

## Scope

**In.** In this order, each put to the author before it is built:

1. **Which source.** Two or three options, each with how its answer key would be made and kept hidden from the
   model that proposes matches. Candidates to look into, none checked yet: a second system of record derived from WWI
   (a CRM or web-shop export of its customers and orders, with planted inconsistencies and a hidden key), which keeps
   the sandbox but tests matching only against what was planted; a public entity-resolution benchmark with published
   ground truth; a real public pair, as the Utrecht sandbox was (three of three right on a blind key, session 06). The
   author's measure applies: as little manual work from him as possible (420).
2. **How the answer key is held and scored**: who writes it, where it lives so that the proposing model cannot read it,
   what precision is "useful" and is fixed before scoring (`EVI-OP-1`).
3. **The analysis record and the declarations for the new source**, as for WWI: the catalogue pass, per-table then
   cross-table analysis, then keys. Where the proposal of identity across the two sources is the falsifiable core, it
   is made blind and scored against the key.
4. **What it asks of the generator**: a second source file under `model/sources/` (0.4.1 stops on more than one), the
   rules of 144 §3 for several sources (proposed, not ruled: key spaces, satellites per source, matching in the business
   vault), and the generator's type map for anything other than SQL Server.

Review each design on sol before building, confined and framed as before (*Traps*). Bring the author only the weak
cases.

**The checker's precondition is met.** It refuses a second acquired source unless the maintenance baseline of
[520](../docs/50_process/520_record-keeping.md) is ruled; `records/maintenance_baseline.json` has been `ruled` since
S06-052 (handover 13 said otherwise, wrongly). Its tolerances are recorded as proposals for the author to set; say so
before the first comparison is run.

**Out unless he asks.** Calculation engines and the forecast; stock groups and the stock item dimension; a second mart;
access rules per sensitivity class; quality gates (`ARC-OP-33`); further growth classes (030 §8); releases and client
repositories; the rest of the assessment except where the new source touches it.

## How to work with the author

Plain English, numbered points; propose, let him react, write what he settles; quote him verbatim; everything tentative
until he rules it. He asked that only weak-evidence cases come to him. When he rules, record it the same turn, in an ADR
or the register, and commit. **The main goal is generally applicable knowledge; WWI is only an example** (his words,
2026-11-06): say what in a design is general and what belongs to one source.

## Traps and warnings

**Every first version has failed review on sol**, now in every session since S09, including both in S13. Build the time
in. A bundle must hold every file a claim depends on: in S13 two code findings rested on the raw vault's
`version_unique` tests, which the bundle left out, and in S12 two findings on a test it left out. Name the upstream
guarantees in the bundle.

**Turns get cut off before they report.** On 2026-11-15 and 11-16 the work was done and committed, and the runner took
it live, but the author never got the report and sent his rulings three times. Commit as soon as a step is whole, log
the step at once, and report in short messages as work completes rather than once at the end. A cut-off turn also left
`.git/HEAD.lock` and `.git/objects/maintenance.lock`: before committing, look for stale locks (dated, no git process)
and remove them; deletion permission is per session (`device_request_delete_permission`).

**Long runs go to the cloud workspace.** A `device_bash` call ends at 180 s, and nothing it starts in the background
survives the call. A full `dbt build` of a day there takes longer. For suites, pack the dbt project, the suite and one
extract into a single archive under `scratch/_transfer/` (55 MB), stage it into the cloud workspace, install
dbt-core 1.12.5, dbt-duckdb 1.11.0 and DuckDB 1.5.6, and run the suite there with a long timeout; it builds its own
warehouse from one extract. Short builds of the slice alone fit in the desktop's shell on a copy of the published
warehouse (`rsync` it; 2.2 GB, about two minutes).

**Test the test before trusting a run.** `test_slice.py` took three runs: a construction that deleted a customer before
copying it as a template, and two ambiguous column names in its own checks. Run new check queries once against an
existing warehouse before starting a ten-minute run.

**Codex calls time out after 60 to 80 seconds but keep running**; poll for the answer file. Short tasks, such as the
audit, may return within the call.

**The author's machine is the constraint.** A rebuild of a day now takes about 12 minutes there (725 s for 0.4.1, from
318 s for a daily load before the slice); a daily load with the slice has not been measured, since the simulation has
not advanced in S13. DuckDB runs within 2 GB and cannot write files. Any file written into `prototypes/wwi_sandbox/dbt/`
goes live within a minute; the runner retries a failed date only when the dbt project changes.

**The cloud workspace's disk fills up.** Delete test warehouses when done (S13's were deleted).

**Generated files are never edited.** After a generator change, regenerate on the author's machine too, and check that
a version bump changes nothing but the header (it did for 0.4.1).

## Outstanding for the author, not the model

**Rule or reject 030** (growth classes, the watermark conditions, the Sunday reread, one day
of overlap). **The phase gate** of 400 and ADR-0006. **`PRC-OP-10`**: points 1 to 7, 9, 10, 12 to 15 and 19.
**The tolerances** of the maintenance baseline, before the first comparison. From handover 12, still open: `git gc`; the
task type for design work; `ARC-OP-37` items 2 and 4 (several sources, conditions on engines); which customers are
individuals and access rules per sensitivity class before production; the two guards of session 06; two commits of
2026-10-25 not in any step log.

## Driving the sandbox

Unchanged from handover 08: request files in `data/wwi/requests/`, four actions (`status`, `advance`, `export`,
`query`), one request per job run, the newest three extracts kept, `data/frozen` never touched, no row edits, no
`setup.ps1 -Reset`. Advance at most two days at a time unless the author says otherwise. The marts are read from
`data/warehouse/published/wwi.duckdb`, read-only.

## Do not reopen

Everything in handovers 06 to 13, plus:

- ADR-0039: the first use case; marts read only from the business vault and never calculate; sales excluding tax
  derived in the business vault; a segment shown as currently known; the forecast out of the slice.
- ADR-0040: unplaced lines kept visible on the unknown member as a data-quality issue; "as known on" as a replay; the
  decision register as one file per decision, cited by every fact table and analysis.
- The order of the work: the messy source next (2026-11-15).

## What was not done

No second source; the falsifiable core untested. The revisions after both S13 reviews are unreviewed. The header of a
file written by `generate_marts.py` does not carry the module's checksum, unlike a template's. Whether the
status-tracking satellite should record a key first seen only in history is open under `ARC-OP-37`. The simulation was
not advanced, so no daily load with the slice has run. The findings note is not adjudicated. The register still only
grows (`PRC-OP-2`).
