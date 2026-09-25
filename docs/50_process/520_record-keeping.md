# 520 — Record keeping: a step log for the post-mortem

**Status: working draft, amended after review.** Built on 2026-09-25, session 06, at the author's
request, and adopted by [ADR-0014](../20_decisions/0014-step-log.md). Reviewed the same day by sol and
astra, both of whom failed it
([sol](../30_research/notes/XREV_2026-09-25_step-log_sol.md),
[astra](../30_research/notes/XREV_2026-09-25_step-log_astra.md)); the findings the author accepted are
integrated below under *Added after review*. The amendments themselves are unreviewed.

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
| `records/task_instances.jsonl` | one piece of work under one row of 070 | task dimension |
| `records/assets.jsonl` | one data asset: a delivered file, table, model, report or control | asset dimension; the start of the stable-unit inventory |
| `records/audits.jsonl` | one blind reclassification of a session's sample | audit fact |
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

**Result.** `outcome` records completion only — whether the step's own agent finished it — and is
`done`, `partial`, `failed`, `blocked`, `pending` (waiting on someone) or
`superseded` (overtaken by a later decision). A blocked or failed step carries a `blocker` with a category
from the vocabulary and a sentence of detail. `defects` lists anything wrong in the step's output, with
its type, who found it and which step fixed it. A defect found later is appended to the original step,
never silently corrected.

**Effort, kept apart.** `effort` holds `elapsed_minutes`, `tool_calls` by tool, `model_calls` for
external reviewer passes, and `compute_eur`. They are never summed into one total, as `CON-OP-16`'s guard
and 155 both require.

**The author's effort, by proxy.** Every step whose actor is H carries `human_effort`, as the author ruled
on 2026-09-25:

> Don't record mytime, just the number of answers. If anything, answer length is a good indicator.
> Another one is maybe the type of activity. Answering is Small. If I have to download stuff, or am
> otherwise your hands in the real world, it's a size large.

So `human_effort` holds `activity` — `answer`, `approve` (a permission prompt) or `act` (downloads,
installs, logins, moving files: being the model's hands) — `size`, which follows from the activity
(`small` for answering and approving, `large` for acting), `answers` (a count, usually 1), and for answers
`words`, the length of his verbatim text. The checker enforces the size mapping and recounts the words.
A step in which the model asks him to act is recorded as the model's; his doing it is a separate H step
of size large.

*Superseded 2026-09-25 by that ruling:* `effort` was to hold `human_minutes` with a `human_basis` of
measured, stated, estimated or unknown. His time is not recorded; `human_basis` stays in the vocabulary
for old records only.

**Words and references.** `summary` is one sentence. `verbatim` is required whenever a person requests or
decides something: the author's words, unedited. `inputs` and `outputs` are paths, URLs, commit hashes or
step ids. `notes` is free text.

**Provenance of the record itself.** `recorded` is `contemporaneous` (written at or just after the step),
`same-session-reconstruction` (written later in the same session from the transcript), or
`later-reconstruction`. The post-mortem weighs them differently.

## Added after review

The reviews found that the log let the recorder certify its own work, left the step grain to taste, and
could not compute two of the three hypotheses it exists for. The author accepted the recommended
dispositions on 2026-09-25: "I'll go with the recommendations." What follows is the amended design. Each
rule is enforced by `tools/check_repo.py` unless it says otherwise.

**Completion is not validation.** `outcome` says the work was finished. `validation`, when present, says
whether a check confirmed it: `{"status": "validated" | "failed", "by": <step>}`, where the referenced step
must have the role `check` and a different agent from the step it validates. No validation means
unvalidated. The model cannot validate its own output.

**Choosing is deciding.** Selecting among alternatives — a default, a mapping, a threshold, an exclusion,
a source — is a `decide` step, even in the middle of executing. A decision by A or D carries
`decision_basis`. Whether hidden decisions were split out is not mechanically checkable; the blind audit
tests it.

**Grain.** One step has one observable state change or one check result. Steps that belong to one piece
of work share a `task_instance`, defined in `task_instances.jsonl` with its 070 row, subject, the
`allocation_version` of 070 it is compared against (a commit hash, frozen per session in
`sessions.jsonl`), the step that opened it, and its status. Any contemporaneous step with a `task_row`
must name its instance, and the rows must agree. Accounting for every role of an instance at close —
proposes, decides, executes, checks, including roles skipped — is deferred to the first real instance.

**Each of the author's messages counts once.** `human_effort.response_id` identifies the message. A
message that feeds several steps is counted once: only its first step carries `words`, which the checker
recounts from `verbatim`. Real-world acts (`act`, size large) are counted separately from answers.

**Rework names its cause.** A `rework` step carries `rework_of`, the step it corrects, and a
`work_reason`: `defect-correction`, `scope-change` or `expected-iteration` (`first-pass` exists for
completeness).

**Defects carry severity and stage.** Every defect has a `severity` (low, medium, high, critical) and a
`detected_stage` (self-check, review, author, downstream, audit). The stage a defect escaped to is
deferred until there are stages to escape to.

**Unknown is not zero.** An effort figure that was not observed is omitted, never written as zero, and an
analysis treats an absent figure as unknown. *Unenforced:* the checker cannot tell a true zero from a
guessed one.

**The session-close audit.** Before a session is marked `closed` in `sessions.jsonl`, a different model
reclassifies a random sample of its steps from their summaries and verbatim text, without seeing the
recorder's labels, on the fields listed in `vocabulary.audit_fields`, against this document and the
vocabulary at a named commit (`rubric_version`). The result goes in `audits.jsonl` with every
disagreement kept. The checker refuses a closed session without one.

**Data lineage, from the first acquired source.** Contemporaneous steps of the data task types
(`vocabulary.data_task_types`) name the `assets` they touched, from `assets.jsonl`, which records each
asset's kind, source, location, status (supported, unsupported, retired), the step since which it
exists, its hash if it is a delivered file, and its `data_as_of`. A `check` step on data records
`check.type`, `expected`, `observed` and `evidence`.

**The maintenance baseline comes before the second source.** `CON-OP-16` cannot be computed without a
stable denominator. The asset inventory is its start. Before a second source is acquired,
`records/maintenance_baseline.json` must define the stable units counted, the denominator rules, the
reporting window, the burden indicators with their severity weights, and the numerical tolerance for
"holding steady" — fixed before any comparison is run. The checker refuses a second acquired source
without it.

**Parked.** Separate activity and subject types; multiple causes and dependencies per step; a planned
test of whether human attention is the binding constraint rather than merely in demand. Declined:
deriving `size` rather than recording it, since it is the author's term.

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
`python tools/check_repo.py` validates every record against the vocabulary and the rules above, checks
that references resolve, and prints counts by faculty and work class and the author's responses, words
and large acts.

## What cannot be measured

This should be stated before it is discovered. **The author's time is not recorded, by his ruling.** The
proxy — answers, their length, and small or large activity — stands in for it; the deciding number of
[155](../10_architecture/155_adjudication-economy.md), human minutes, is therefore approximated by counts
and sizes, and any figure derived from them must say so. **The model's token use is not visible to the
model** in this environment, so agent effort is recorded as tool calls and elapsed time, and tokens are
left empty rather than guessed. **Work outside the conversation is invisible** unless someone records it:
a download the author makes is logged only because the model asked for it and he reports it done.
