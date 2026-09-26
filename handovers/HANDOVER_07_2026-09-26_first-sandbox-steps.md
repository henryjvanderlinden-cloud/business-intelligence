# nsdn — Handover 07: the first sandbox was run and parked; the next one is Wide World Importers
## Written 2026-09-26 at the close of session 06, revised at the pause of session 07

> **STATUS: CURRENT.**

---

## First actions

1. `git log --oneline -15` — expect HEAD at the commit that last revised this handover, on top of `ec901e6`.
2. `python tools/check_repo.py` — must pass. Expect 59 register rows, 14 ADRs, 7 sessions (S06 closed and
   audited, **S07 open**), 133 steps, 22 sources (5 acquired), 17 assets. **Run it on its own, never piped:**
   session 06 committed once with a failing check because `| tail` hid the exit status.
3. Read register rows `EVI-OP-7` (the next sandbox) and `PRC-OP-6` (the log's reliability), then
   [the session 06 post-mortem](../docs/30_research/notes/2026-09-26-session-06-post-mortem.md).
4. **Continue session S07** in `records/steps/S07.jsonl` from S07-010; it was paused, not closed. From S07 every
   step carries an `activity` as well as a `task_type` — see *Changed after the first audit* in
   [520](../docs/50_process/520_record-keeping.md). Closing S07 needs a blind audit (the checker enforces it).

## Outstanding actions for the author, not the model

**Push.** Commits since `53e0815`'s predecessor are local only.

**Install SQL Server Developer edition and the Wide World Importers sample** (`SRC-018`). A large act, and he
has agreed to it.

**Rule the two guards** from session 06 if they are to stand: no de-anonymising business-for-sale listings;
no named individuals.

## Task for the next session, in one sentence

Get Wide World Importers running as a simulated internal system the model can read: verify what its daily
simulation actually changes, settle the access route, and capture the first change feed.

## The plan for Wide World Importers, as proposed and not yet tried

**Why this dataset.** The author parked the Utrecht sandbox because it was scraping, not a company's internal
data: "There are no regularly updating records, or a regular creation of new records." He set the next use
case as a simple financial administration or ERP "with regular inserts and updates" (`EVI-OP-7`), and chose
Wide World Importers: a wholesale company's database — sales, purchasing, warehouse, customer and supplier
transactions — with Microsoft's own day-by-day simulator, `DataLoadSimulation.PopulateDataToCurrentDate`
(parameters: orders per day, Saturday and Sunday share). The simulator being Microsoft's and not the model's
is the point: a landscape simulated by the tested party flatters it (410).

**Verify first; these are from the model's knowledge, not checked:** that the simulation also advances
existing orders (picking, invoicing, payments), not only inserts; and that master tables (customers,
suppliers, stock items, people) are system-versioned temporal tables with history. The answers decide how
much real update behaviour the sandbox has.

**Do not port it.** The author asked whether to port to Postgres. Porting means the model rewriting the
simulator and the temporal tables, which undoes the reason for the choice.

**Access.** The model's shell on the author's computer is an isolated Linux environment: it cannot reach
services on the Windows host (localhost) and has no network of its own. Test that once the server is
installed, but expect it to fail. The proposed route is a **scheduled export on his side**: a small script
(PowerShell with `sqlcmd` or `bcp`, run by Task Scheduler) that advances the simulation a few days and writes
changed rows — by `ValidFrom`/`LastEditedWhen` or the temporal history — into `data/raw/WWI/<date>/`. Setting
it up is one large act; after that each refresh arrives without his hands, which is what the maintenance
baseline's refresh rule needs. A second, untried route: the Codex MCP server runs on his Windows machine and
could run `sqlcmd` there — but that makes another model the executor, and its sandbox has so far been
read-only.

**Measure from the start.** One source, refreshed on a schedule, is exactly what `CON-OP-16`'s epochs assume.
Put matching and modelling choices to the author as decisions (lesson 3 of the post-mortem).

## How to work with the author

**Plain English, numbered**; propose, let him react, write what he settles; quote him verbatim; external
review on sol and astra in parallel. From session 06:

**Keep the apparatus small.** "let's not make it too serious yet, we're still putting our feelers out";
"this whole system also suffers from the same things described in Generative Structures, so let's not make it
too large." Integrate review findings lightly; enforce only what matters most.

**Put decisions to him as decisions.** In session 06 the model made every matching choice and he only did
lookups.

**Sheets for him are .xlsx with an unmistakable name**, and **ask before overwriting a file he has touched.**

**He will say when a session is long.** Wrap up when he does.

## What sessions 06 and 07 did

Session 06 (25–26 September) built the step log ([ADR-0014](../docs/20_decisions/0014-step-log.md),
[520](../docs/50_process/520_record-keeping.md)) and the maintenance baseline, each failed on first review and
repaired; ran the first sandbox on the Utrecht business landscape — PAR, OSM, DUO, LRK, RDW acquired, OSM
businesses matched to PAR establishments in three versions, measured against a blind answer key and three
registers; and closed with a blind audit and a
[post-mortem](../docs/30_research/notes/2026-09-26-session-06-post-mortem.md). Its eight lessons in one line
each: the apparatus was costly to set up and cheap to run; the log is reliable on who and what, not on work
class (7/15) or task type (5/15); the model decided and the author was its hands; his effort was small in
words, large in acts; matching worked (88–99% right kind) and data age was the main error; review and the
checker earned their keep; the environment shaped the work; the maintenance measure was never computable.

Session 07 (26 September, straight after) made the classification fix the author accepted, parked the
Utrecht use case (`EVI-OP-2`), opened `EVI-OP-7`, surveyed candidates (`SRC-018`–`SRC-022`) and recorded his
choice of Wide World Importers.

## Traps and warnings

**No Dutch data portal, 4TU, Kaggle or Microsoft Learn is reachable from either environment; GitHub and PyPI
are.** Prefer sources that are.

**The cloud workspace is reclaimed overnight.** Write results back to the computer the same day.

**The checker forces `maintain` for work triggered by a refresh or a failed check**; **`validation` needs a
check by a different agent**; **from S07, `communication`, `documentation` and `review` are activities, not
task types.**

**The Utrecht data stays on disk, parked.** Do not delete it; the LRK file contains home addresses and contact
persons, which are never to be read.

## Do not reopen

Everything in handover 06's list, plus:

- Every step is logged, classified, and validated by the checker — [ADR-0014](../docs/20_decisions/0014-step-log.md).
- The author's effort is recorded as answers, words and small or large acts, never as time.
- A blind audit by another model gates each session's close.
- Task type is the subject, activity what was done (from S07).
- The Utrecht landscape is parked; the next sandbox is a simulated internal system, Wide World Importers, not
  ported.

## What was not done

No source of the Utrecht sandbox was refreshed; `CON-OP-16` was never computable there. What a model adds
beyond rule tables was not isolated. Wide World Importers is not installed, its simulator's behaviour is
unverified, and the access route is untested.
