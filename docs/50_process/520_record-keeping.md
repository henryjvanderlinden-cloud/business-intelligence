# 520 — Record keeping: a step log for the post-mortem

**Status: working draft, unreviewed.** Built on 2026-09-25, session 06, at the author's request.
Adopted by [ADR-0014](../20_decisions/0014-step-log.md). External review is owed under `PRC-OP-6`.

## Why this exists

The author asked for it in these words:

> We need to start record keeping, exactly on what we do, how to classify it (human, agentic,
> deterministic, type of task etc), so that we can do a complete post mortem on what we did
> afterwards and to test our hypotheses. Can you build a structure to record all the data, and do
> meticulous record keeping of every step?

The project's claims are claims about the division of labour. [070](../00_concept/070_task-allocation.md)
says which faculty should propose, decide, execute and check each task. `CON-OP-16` proposes that success
is maintenance effort per stable unit of landscape. [155](../10_architecture/155_adjudication-economy.md)
says human attention is the scarce resource. None of these can be tested after the fact unless the work
was recorded as it happened, in the same terms. A post-mortem written from memory, or reconstructed from
git history, measures the storyteller rather than the work.

So the log is not documentation of the project. It is the project's first dataset about itself.

## The shape: a small star schema

Everything lives under [`../../records/`](../../records/README.md), as JSON Lines — one record per line,
diffable in git, loadable in one statement by DuckDB (`read_json_auto('records/steps/*.jsonl')`) or pandas.

| File | Grain | Role |
|---|---|---|
| `records/steps/<session>.jsonl` | one step | the fact table |
| `records/sessions.jsonl` | one working session | session dimension |
| `records/sources.jsonl` | one candidate or acquired data source | source dimension and lineage |
| `records/vocabulary.json` | — | the allowed values of every classified field, and the known agents |

The vocabulary is data, not code, so a new value is added by editing one file. The checker reads it.

## What a step is

A **step** is one coherent action with one purpose, performed by one actor in one role. Reading five
register rows to orient is one step; running the checker is another; the author approving a deletion is a
third. A step is not a tool call — tool calls are counted inside the step that made them — and it is not a
whole conversational turn, which usually contains several steps by several actors.

The test for splitting: if two parts of the work would be classified differently on any field below, they
are two steps.

## The fields

**Identity and time.** `id` is `<session>-<nnn>`, sequential within the session. `ts` is an ISO timestamp
with its UTC offset, and `ts_precision` says how it was obtained: `exact` from a clock or a message
timestamp, `approx` estimated to within a few minutes, `bound` when only an earlier-or-later bound is
known. `ts_end` is optional.

**Who.** `actor` is the faculty — `H`, `A` or `D`, as ruled in
[ADR-0008](../20_decisions/0008-faculties-substrate-mandate.md) and
[ADR-0010](../20_decisions/0010-the-agentic-layer.md). `agent` names the specific person, model or program,
from the list in the vocabulary, and the checker enforces that it belongs to the stated faculty.
`initiated_by` points to the step that caused this one.

The line between A and D is drawn by **who determined the content of the result**. When a model chose
what to do and composed the output, the actor is A, whatever tools it used. When the result is fully
determined by a program given its inputs — the checker's verdict, a file deletion, a commit, a load — the
actor is D, even if a model typed the command. This is the distinction
[ADR-0004](../20_decisions/0004-models-out-of-the-data-path.md) rests on, and the log would blur it if it
recorded every machine action as the agent's.

**What kind of work.** `role` is the position in 070's chain — `propose`, `decide`, `execute`, `check` —
plus `request` for a person asking for something and `inform` for reporting without proposing.
`task_type` is from the vocabulary. `task_row` is the row of 070 the step belongs to, or `null` when no row
fits; a `null` is itself a finding, because it marks work the task table does not yet describe.
`tier` is the claim tier from [ADR-0005](../20_decisions/0005-three-autonomy-tiers.md), or `none` for work
that makes no claim. `register_rows` lists the open points the step bears on.

**Build or maintain.** `work_class` applies the counterfactual test from `CON-OP-16`: *would this work be
needed merely to keep the existing landscape running?* If yes, `maintain`. New capability is `build`.
Redoing something because it was wrong is `rework`, and is charged to whichever step's defect caused it.
Looking for options without yet building is `explore`. Coordination, session admin and record keeping are
`overhead`. The five are exclusive; where a step straddles two, it is split.

**Result.** `outcome` is `done`, `partial`, `failed`, `blocked`, `pending` (waiting on someone) or
`superseded` (overtaken by a later decision). A blocked or failed step carries a `blocker` with a category
from the vocabulary and a sentence of detail. `defects` lists anything wrong in the step's output, with
its type, who found it and which step fixed it. A defect found later is appended to the original step,
never silently corrected.

**Effort, kept apart.** `effort` holds `human_minutes` with `human_basis` (`measured`, `estimated`,
`stated` by the person, or `unknown`), `elapsed_minutes`, `tool_calls` by tool, `model_calls` for
external reviewer passes, and `compute_eur`. They are never summed into one total, as `CON-OP-16`'s guard
and 155 both require.

**Words and references.** `summary` is one sentence. `verbatim` is required whenever a person requests or
decides something: the author's words, unedited. `inputs` and `outputs` are paths, URLs, commit hashes or
step ids. `notes` is free text.

**Provenance of the record itself.** `recorded` is `contemporaneous` (written at or just after the step),
`same-session-reconstruction` (written later in the same session from the transcript), or
`later-reconstruction`. The post-mortem weighs them differently.

## Sources

`sources.jsonl` holds every data source considered, whether used or not, with its publisher, URL,
licence, access route, status (`candidate`, `acquired`, `rejected`, `blocked`), the step that found or
fetched it and, once acquired, its local path under the ignored `data/` directory, retrieval time and
SHA-256. A rejected source keeps its reason. The post-mortem will want to know what was passed over as
much as what was used.

## Discipline

The model appends steps as it works, reading the clock at step boundaries. Records travel in the same
commit as the work they describe, as register updates do. The author's steps are recorded by the model
from his messages, with timestamps from those messages, and he corrects them when they are wrong.
`python tools/check_repo.py` validates every record against the vocabulary, checks that references
resolve, and prints a count by faculty and by work class.

## What cannot be measured

This should be stated before it is discovered. **The author's minutes are not observed.** The log knows
when his messages arrive, not how long he spent on them; `elapsed_minutes` between a reply and his
answer is an upper bound, not effort. He can state his time, and a stated figure is marked `stated`.
**The model's token use is not visible to the model** in this environment, so agent effort is recorded
as tool calls and elapsed time, and tokens are left empty rather than guessed. **Work outside the
conversation is invisible** — a download, a conversation with a colleague, thinking in the shower —
unless someone records it.

These gaps matter most for the adjudication economy, whose deciding number is human minutes. The
sandbox should close the first gap by having the author state his time on the steps that cost him
something, which is `PRC-OP-6`'s second question.
