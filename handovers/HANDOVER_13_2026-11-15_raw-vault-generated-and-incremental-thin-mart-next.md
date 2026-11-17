# nsdn — Handover 13: the raw vault is generated, tested and loaded incrementally; one thin mart and analysis is next
## Written 2026-11-15 at the close of session 12

> **STATUS: HISTORICAL (superseded 2026-11-17 by [handover 14](HANDOVER_14_2026-11-17_first-slice-live-messy-source-next.md))**

---

## First actions

1. `git status`, then `git log --oneline -15`. Expect HEAD at the commit that closed S12 (message begins "Close session
   12"). The author pushes himself; if `origin/main` is behind, say so, do not push.
2. `python tools/check_repo.py` on a copy (on the desktop's shell it is slow; see *Traps*). It passes with the known
   warnings in `S07.jsonl`. Expect 12 sessions, S12 closed with `AUD-S12-1`, 38 ADRs.
3. `python prototypes/vault_generator/generate.py --check`: 510 generated files, 0 problems.
4. Read, in this order: this handover; the [general assessment](../docs/30_research/notes/2026-11-14-general-assessment.md)
   points 6 to 8 and 16 to 18, and `PRC-OP-10`; [ADR-0026](../docs/20_decisions/0026-conformed-dimensions-and-fact-table-changes.md);
   `ARC-OP-37` item 8 (marts) and [146](../docs/10_architecture/146_fact-tables-and-new-questions.md);
   [144](../docs/10_architecture/144_raw-vault-business-vault-calculation-engines.md) §2 (the raw/business line, not
   ruled); [143](../docs/10_architecture/143_the-vault-generator.md) §13 (what the generator does now); 400 Phase 3
   ("requires a decision register").
5. Ask the sandbox job for its status (handover 08, *Driving the sandbox*). Expect simulated date 2016-06-06 and the
   runner `loaded` with `last_ok_date` 2016-06-06. 7.4 GB was free on 2026-11-15.
6. Open session S13 in `records/sessions.jsonl` and log from S13-001.

## Where we stand

Session 12 ran from 2026-11-03 to 2026-11-15, mostly on Claude Opus 5.5, with one evening (2026-11-14) on Claude Fable
5.2.

- **The vault generator** ([143](../docs/10_architecture/143_the-vault-generator.md), ruled in
  [ADR-0037](../docs/20_decisions/0037-vault-generator.md)) writes the whole WWI raw vault from `model/`: 22 hubs, 49
  links, 45 satellites, 7 reference tables, and the audit, status-tracking and effectivity satellites by rule; 216
  tables, 510 files, 777 tests per load. Version **0.3.0**. Three sol reviews, each failing its first version, all
  findings applied. The cloud suite (`prototypes/vault_generator/test_load.py`) passes eight checks: clean load,
  twice-is-once, a failed batch and a failed rebuild leave nothing, exact reconstruction of every staged version, a
  late arrival restated, a source closing time kept, an empty table dated.
- **Live on the author's machine**, replayed from 2016-05-31 as ruled, now at 2016-06-06. Loads on his machine and in
  the cloud were identical in all 216 tables up to 2016-06-04 (the last two days exist only on his machine).
- **Incremental capture** ([equivalence/030](../docs/30_research/equivalence/030_incremental-capture.md), proposed, not
  ruled): growth classes, a watermark only with a guarantee from the source, overlap, a weekly full reread, control
  totals, an extract specification. Trialled as 0.3.0 on engine-kept histories: a day takes 318 s on his machine
  (whole-history Sunday 425 s), against 893 to 1,330 s with 0.2.1.
- **The ETL capability equivalence investigation** (Fable, 2026-11-14): thirteen capabilities in
  [010](../docs/30_research/equivalence/010_capability-inventory.md), the Databricks anatomy in 020, name, place,
  order (capabilities 1, 2, 5, 6 first), three-step method and five principles ruled in
  [ADR-0038](../docs/20_decisions/0038-etl-capability-equivalence-investigation.md); `ARC-OP-38`.
- **The general assessment** of 2026-11-14 (Fable) and `PRC-OP-10`, opened by the author to work through it with Opus.
  Points 11 and 16 to 18 have landed (see the row); the rest have not.
- `README.md`, `AGENTS.md` and 400 now say what is built and what is not. **The phase gate of 400 and ADR-0006 has not
  been decided**: formally the project is in Phase 0, in practice parts of Phases 1 and 2 exist in the sandbox.

## Task for the next session, in one sentence

Build one thin, end-to-end slice on the existing vault, one mart and one analysis answering one business question,
so the chain runs from a source extract to an answer, as the author ruled on 2026-11-15 ("Allright, let's write the
handover, and do them in that order").

## Scope

**In.** In this order, each put to the author before it is built:

1. **The business question.** One question a WWI manager would ask (for example: which customers and stock groups
   drive gross margin, by month), proposed with two or three alternatives; the author picks. ADR-0026 makes each mart
   cite the use case it serves, and 400 says Phase 3 needs a decision register: this question is its first entry.
2. **Where the mart takes its data from** (`ARC-OP-37` item 8, proposed 2026-10-26, not ruled): from the business vault,
   reaching the raw vault through point-in-time and bridge structures, never calculating. A thin slice may need only
   one point-in-time table and the conformed dimensions it uses; say so, and get the ruling.
3. **The smallest business vault the question needs**, generated, not hand-written (ADR-0032), with the raw/business
   line of 144 §2 (not ruled) put to the author where the slice depends on it.
4. **One dimensional mart** (a fact table at a stated grain, the conformed dimensions it uses) and **one analysis**
   answering the question, with tests (grain, reconciliation of the measure against the raw vault, plausibility).
5. The "as of" views of ADR-0027 for the mart: knowledge time and business time.

Review the design on sol before building, confined and framed as before (*Traps*). Bring the author only the weak
cases.

**Then, as ruled, the session after:** a second, messy source with an answer key (assessment point 18), which tests the
falsifiable core of 410 and the generator's generality; it needs the maintenance baseline of
[520](../docs/50_process/520_record-keeping.md) ruled first, since the checker refuses a second acquired source without it.

**Out unless he asks.** Calculation engines; access rules per sensitivity class; quality gates (`ARC-OP-33`); further
growth classes or watermarks (030 §8); releases and client repositories; the rest of the assessment except where the
slice touches it.

## How to work with the author

Plain English, numbered points; propose, let him react, write what he settles; quote him verbatim; everything tentative
until he rules it. He asked that only weak-evidence cases come to him. When he rules, record it the same turn, in an ADR
or the register, and commit. **The main goal is generally applicable knowledge; WWI is only an example** (his words,
2026-11-06): say what in a design is general and what is WWI's.

## Traps and warnings

**Every first version has failed review on sol**, in every session since S09: the declaration format, the catalogue
pass, 143 twice, 030. Build the time in. A bundle sent for review must include every file the claim depends on: 030's
review judged two findings without the test that answered them.

**Codex calls time out after 60 to 80 seconds but keep running, and sometimes never start.** Poll for the answer file
with a loop of `sleep 5` in one `device_bash` call. If nothing arrives after about ten minutes, the call did not start;
a second call writing to a different file is harmless.

**The author's machine is the constraint, not the cloud.**
- Memory: the runner's DuckDB now runs within a 2 GB budget set in the pinned profile, because without one it failed
  with "Allocation failure" when Windows refused memory (2016-06-05). DuckDB cannot write to the file system there
  (external access off), so anything over a whole history must stream; a test that compared 3.7 million rows as
  multisets needed 3.6 GB. Test memory under a cap in the cloud before shipping.
- A change to the pinned profile, `runner.py`, `job.ps1` or `request.ps1` takes effect only when the author re-runs
  `setup.ps1` as administrator.
- The runner retries a failed date only when the dbt project changes. Any file written into
  `prototypes/wwi_sandbox/dbt/` goes live within a minute.
- Loads take about five minutes there, three times the cloud's; uploads from his machine fail above roughly 20 MB and
  are flaky while dbt runs (split into 8 MB parts); `git status` and `check_repo.py` can take minutes on his shell.

**The cloud workspace's disk fills up.** Each warehouse copy is about 2.5 GB and the suite makes seven. Delete test
copies when done.

**Step timestamps ran ahead of the clock** three times in this session. Take the time from the shell immediately before
writing a step, and use `same-session-reconstruction` for steps written later.

**Generated files are never edited; scope widens through `scope.txt`.** After a generator change, run it on the
author's machine too (`generate.py` removes files it no longer writes; unpacking an archive does not).

## Outstanding for the author, not the model

**Push** (the S12 commits). **Rule or reject 030** (growth classes, the watermark conditions, the Sunday reread, one day
of overlap: guesses for WWI). **The phase gate** of 400 and ADR-0006: whether to take it, and on what condition.
**`PRC-OP-10`**: the remaining fifteen points. **Delete** `data/warehouse_pre-vault_2026-11-04` and
`data/warehouse_vault-0.1.0_2026-11-04` (1.8 GB) when satisfied. From handover 12, still open: `git gc`; the task type
for design work; `ARC-OP-37` items 2, 4 and 8; which customers are individuals and access rules per sensitivity class
before production; the two guards of session 06; two commits of 2026-10-25 not in any step log.

## Driving the sandbox

Unchanged from handover 08: request files in `data/wwi/requests/`, four actions (`status`, `advance`, `export`,
`query`), one request per job run, the newest three extracts kept, `data/frozen` never touched, no row edits, no
`setup.ps1 -Reset`. Advance at most two days at a time unless the author says otherwise.

## Do not reopen

Everything in handovers 06 to 12, plus:

- The generator's design (143, ADR-0037): SHA-256 keys, knowledge time as the extract's date, zero-length versions
  kept, the vault's first day 2016-05-31, `key_case` on the source; the bridge's audit on the link and staging as
  tables (agreed 2026-11-04).
- The equivalence investigation's name, place, order, method and principles (ADR-0038), with its two readings ruled.
- The order of the next work: the thin slice, then the messy source (2026-11-15, `PRC-OP-10`).

## What was not done

No business vault, mart or analysis. 030 is not ruled and its revised text is unreviewed, as are the fixes after the
third review of 143. The last two loaded days (2016-06-05 and 06-06) were not compared with a full read. The
falsifiable core of 410 is untested. The register still only grows (`PRC-OP-2`).
