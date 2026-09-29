# nsdn — Handover 07: the first sandbox was run and parked; the next one is to be thought through before anything is installed
## Written 2026-09-26 at the close of session 06, revised at the pauses of session 07 (26 and 28 September)

> **STATUS: CURRENT.**

---

## First actions

1. `git status`, then `git log --oneline -15`. The revision of 2026-09-28 was written back to the computer without a
   shell and may be uncommitted: if `git status` shows it, commit it first. Otherwise expect HEAD at the commit that
   last revised this handover, on top of `11011a7`.
2. `python tools/check_repo.py` — must pass. Expect 61 register rows, 14 ADRs, 7 sessions (S06 closed and
   audited, **S07 open**), 158 steps, 22 sources (5 acquired), 17 assets. **Run it on its own, never piped:**
   session 06 committed once with a failing check because `| tail` hid the exit status.
3. Read register rows `EVI-OP-7` (the next sandbox), `ARC-OP-29` (the data model) and `PRC-OP-6` (the log's
   reliability), then
   [the session 06 post-mortem](../docs/30_research/notes/2026-09-26-session-06-post-mortem.md).
4. **Continue session S07** in `records/steps/S07.jsonl` from S07-035; it was paused, not closed. From S07 every
   step carries an `activity` as well as a `task_type` — see *Changed after the first audit* in
   [520](../docs/50_process/520_record-keeping.md). Closing S07 needs a blind audit (the checker enforces it).

## Outstanding actions for the author, not the model

**Commit and push** the second revision of 2026-09-28 (the two review notes, 160's status line, `ARC-OP-30`, this
handover, the records) if a shell was not available to do it; that conversation had none. The first revision is
`11011a7`, pushed.

**Nothing to install yet.** He has said SQL Server is no problem to install, but asked that the whole setup be
thought through first. Do not ask him to install anything until the design says what, why, and what it saves him.

**Rule the two guards** from session 06 if they are to stand: no de-anonymising business-for-sale listings;
no named individuals.

## Task for the next session, in one sentence

Think through the entire setup for the next sandbox — source, simulation, capture, landing, the loads the
agent runs, and every point where the author would otherwise have to act — before anything is installed.

## The author's standing instruction for this, verbatim

> let's not move too quickly here with installing SQL server and first think through the entire setup. I
> want to avoid manual work from my side as much as possible, this is the goal of the entire excercise.
> With regards to point 4, updates are not a hard requirement. If it's insert only that is also fine. Don't
> jump to conclusions, just because I said something, everything tentative still, always keep in mind the
> big picture and the small steps to get there.

Read it as three rules. **Minimising his manual work is the goal of the exercise, not a convenience:** a
design that needs his hands at every refresh fails the thesis, whatever else it shows — and session 06
found him acting as the system's hands five times. **Nothing he says is settled until he rules it:** Wide
World Importers is his current preference, not a decision. **Big picture, then small steps:** design the
whole path end to end, then take the smallest step that tests it.

## The data model, raised in a parallel conversation

On the same afternoon a second conversation on this repository took up the author's observation that the
first sandbox did no visible data modelling (steps S07-012 to S07-018). It drafted
[142_the-data-model.md](../docs/10_architecture/142_the-data-model.md), unreviewed, and opened `ARC-OP-29`:
the model held as text declarations, one file per object, navigated along dimensions — at least conceptual
to concrete and raw to refined — with a generated HTML site for people and the files themselves for agents.
His rulings there, verbatim in the step log: navigation is along dimensions but "not in one visual"; the
HTML view is preferred; the graphical representation "does not need to be machine readable, just optimized
for human consumption". He asked for the note, **not** for a hand-modelled trial case. The next sandbox's
design should say where the data model sits in it; whether it is adopted is still open.

## Wide World Importers: the leading candidate, tentatively

**Why it leads.** The author parked the Utrecht sandbox because it was scraping, not a company's internal
data: "There are no regularly updating records, or a regular creation of new records." He set the next use
case as a simple financial administration or ERP "with regular inserts and updates" (`EVI-OP-7`), and said
of Wide World Importers "I think the Wide World is a good case" — a wholesale company's database with
Microsoft's own day-by-day simulator (`DataLoadSimulation.PopulateDataToCurrentDate`; parameters: orders per
day, Saturday and Sunday share). A simulator not written by the model is the property that matters (410).
**Updates are not required; insert-only is acceptable** (his ruling above), so whether the simulator also
advances existing orders or keeps temporal history is a nice-to-have to check, not a criterion.

**What the design has to settle, in the order it matters to his manual work:**

1. *Where the source runs.* Options so far: SQL Server Developer edition on his Windows machine (he is
   willing); something that runs without him, if any exists — a database the agent can start and advance
   itself, in the cloud workspace or the Linux shell on his computer. The cloud workspace is reclaimed
   overnight and cannot reach most sites; the Linux shell has no network and cannot see Windows services.
   Both limits shape this choice.
2. *How new data reaches the agent.* If the source is on Windows, the agent cannot read it directly; a
   scheduled export into `data/` is one route, the Codex MCP server on his machine another (another model
   as executor; its sandbox so far read-only). Every route should be judged by how often it needs him.
3. *Who advances the simulation.* Ideally a schedule, not a person.
4. *What happens when it breaks.* Who notices, who repairs, and whether that is him.
5. *Where the frozen regression copy comes from* (`ARC-OP-30`): a copy of the source data and one reference date
   per quarter, beside the live feed, so that code changes can be tested on data that stands still.

**Do not port it without cause.** He asked whether to port to Postgres. The case against: the model would be
rewriting the simulator, which undoes the reason for choosing it. The case for, not yet weighed: a source
the agent can run itself might remove his manual work entirely. That trade-off belongs in the design, and
the decision is his.

**Measure from the start.** One source, refreshed on a schedule, is what `CON-OP-16`'s epochs assume. Put
design and modelling choices to him as decisions (lesson 3 of the post-mortem).

## Release regression, raised 2026-09-28

In a new conversation the author asked whether release notes are needed for regression testing and described
his employer's method: frozen data for a quarter with one reference date, a daily snapshot with the current
code diffed against the previous day's, and every difference attributed to a release note or treated as a
regression; the developer checks the intended consequence, a dedicated tester the regression; nothing is
deployed on the quarter turn, and the two reference dates get a plausibility check. At his request it is now in
[160](../docs/10_architecture/160_evaluation-and-regression.md) under *Release regression*, with `ARC-OP-30`
open. The model's two adaptations — context changes as a second source of attribution, and an agent-run loop
leaving him only the residue — are marked there as proposals, not rulings. Reviewed the same evening by sol and
astra, both FAIL on one finding — attribution is not acceptance: a difference inside a declared impact can still
be wrong. Five recommended changes are in `ARC-OP-30`; **his ruling on them is owed** before 160 is amended.
Nothing to build before there is code to release. The Codex bridge times out after 60 seconds: have the reviewer
write its answer to the ignored `scratch/` folder and read it from there.

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

**Do not jump to conclusions from what he says.** Everything is tentative until he rules it; keep the big
picture and the small steps to it in view.

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

Session 07 (26 September, straight after, in two parallel conversations) made the classification fix the author accepted, parked the
Utrecht use case (`EVI-OP-2`), opened `EVI-OP-7`, surveyed candidates (`SRC-018`–`SRC-022`) and recorded his
current preference for Wide World Importers, which he then asked to be treated as tentative until the
whole setup has been thought through; the parallel conversation drafted 142 on the data model.

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
- The Utrecht landscape is parked; the next sandbox is a simulated internal system with regular inserts
  (updates welcome, not required). Which system, and how it runs, is **not** settled.

## What was not done

No source of the Utrecht sandbox was refreshed; `CON-OP-16` was never computable there. What a model adds
beyond rule tables was not isolated. The setup for the next sandbox has not been designed; nothing is
installed; Wide World Importers' simulator is unverified.
