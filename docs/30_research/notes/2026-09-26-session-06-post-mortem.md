# Session 06 post-mortem: the first sandbox steps, read from the step log

**Status: written 2026-09-26 by Claude Opus 5.5 at the close of session 06, from `records/` rather than
from memory; unreviewed.** Every figure below is computed from
[`../../../records/steps/S06.jsonl`](../../../records/steps/S06.jsonl) (117 steps, 25–26 September) or from the
blind audit in [`../../../records/audits.jsonl`](../../../records/audits.jsonl). The author asked for it in
these words: "Let's go with A, see what the lessons learned are."

## What happened

Session 06 opened on handover 06, whose task was the candidate-dataset survey. The author re-themed the
sandbox to businesses in the Utrecht region (`EVI-OP-2`), asked for a classified record of every step
([ADR-0014](../../20_decisions/0014-step-log.md), [520](../../50_process/520_record-keeping.md)), had it and a
maintenance baseline reviewed twice on other models, and then the sandbox began: PAR (anonymous, in
substance the 2022 register), OpenStreetMap, and the DUO, LRK and RDW registers were acquired; OSM
businesses were matched to PAR establishments by location and sector in three versions; and the matches
were measured against a blind answer key of twelve KvK lookups and against the three registers.

## Lessons

**1. The apparatus cost most of the first day and little after it.** Steps 1–60 were 35 overhead to 7 build;
steps 61–117 were 5 overhead to 44 build. Record keeping is the largest single task type (25 of 117
steps). The author's warning that the apparatus suffers what *Generative Structures* describes
(`PRC-OP-2`) is borne out in the setup and not, so far, in the running.

**2. The log is reliable on who and what happened, and unreliable on what kind of work it was.** A blind
reclassification of 15 random steps by gpt-6-astra agreed with the recorder on actor 15/15, outcome 15/15,
role 14/15 and tier 12/15, but on work class only 7/15 and task type 5/15. Work class is the field
`CON-OP-16`'s measure depends on, so the maintenance measure cannot yet be trusted. Two causes are visible
in the disagreements: `task_type` mixes activity with subject — "communication" about matching, "matching"
that is really testing — which is exactly sol's finding 8 on the step log, declined on 2026-09-25 and now
supported by evidence; and the work class of coordination steps (the author's approvals, the model's
reports) has no rule, so the recorder called them build and the auditor overhead. Restoring a damaged
file was maintenance to the recorder, as the checker's rule requires, and rework to the auditor.

**3. The work did not follow the task table's allocation.** For row 9 of
[070](../../00_concept/070_task-allocation.md) — business keys and matching, the project's central bet — the
table has the agentic layer propose and a person decide. In the log the model *decided* seven times (the
radius, both rule files and their revision, the sample design, the blind coding, the proposal policy) and
the author decided nothing about matching; he executed lookups. For row 7 — extraction — the table has
machinery execute once a person grants access; in the log the author executed every acquisition by hand,
five large acts, because neither environment could reach a single Dutch data source. The person's effort
went to being the system's hands, not its judgement, which is the reverse of what the framework intends.
That is partly the sandbox's network and partly that no decision was ever put to him as a decision.

**4. The author's effort was small in words and large in acts.** Eighteen answers, 435 words, five large
acts. Every large act was a workaround for blocked network access or a lookup the free KvK search could
barely support (it shows neither SBI code nor start date).

**5. The central bet has its first figures, and they point at data age rather than matching.** Location
within 30 m plus model-written sector rules, applied deterministically, proposing only unique matches:
three of three right on the blind answer key; the right kind of establishment for 99% of
register-confirmed schools (partly circular), 88% of childcare and 92% of garages; start dates agreeing
within a year for 34 of 60 informative childcare matches. Abstentions were right five of five. The
dominant error is that PAR is from 2022 and OSM from 2026: only 5 of 12 answer-key businesses had any
acceptable PAR counterpart, and eleven childcare centres registered after PAR's date still received a
proposal. What a model adds beyond distance and rule tables has **not** been isolated (`EVI-OP-1`).

**6. Review on another model and the checker both earned their keep.** Four external passes; both the step
log and the maintenance baseline failed their first review and were repaired. The checker refused three of
the model's own errors — a missing field twice, and a step "validated" by its own program — and one error
slipped past it because the model piped the checker's output through `tail`, hiding its exit status. That
is now logged as a defect and the pattern changed.

**7. The environment shaped the work more than the design did.** Every data source was blocked from both the
cloud workspace and the computer's shell; the cloud workspace was reclaimed overnight and lost its files;
the link to the computer dropped twice; Excel with Dutch settings rewrote coordinates in a CSV the author
edited. The one real maintenance event of the session was restoring that file — caused by handling, not by
a refresh.

**8. What the maintenance baseline assumed did not happen.** Sources were meant to arrive one per epoch; three
arrived at once. No source has been refreshed, so none yet counts as stock, and no epoch can be compared.

## What follows

Before the log is used for `CON-OP-16`: split task type into activity and subject, and give coordination
steps a work-class rule, then re-audit. Before the next matching work: put matching choices to the author
as decisions, so row 9's allocation is tested rather than bypassed. For the bet itself: handle the time
gap (treat businesses registered after April 2022 as absent from PAR), and design the comparison that
isolates what the model adds.
