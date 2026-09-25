# 126 — Context gardening: keeping the system's memory true

Part of the context system described in [120_context-layer.md](120_context-layer.md). Drafted
2026-09-25, session 04; the author singled it out as the most important of the context points
raised that day. Revised the same day after external review on GPT-6 Astra, recorded in
[XREV_2026-09-25_context-system_astra](../30_research/notes/XREV_2026-09-25_context-system_astra.md)
Q3, which added erasure across every copy, quarantine, concurrency control, a stricter test for
deletion, measures that cannot be improved by hiding defects, and a job that checks gardening
itself. Nothing here is built.

## Why it is a task in its own right

A context store decays by default. Facts go stale when sources change, summaries drift from
what they summarise, duplicates accumulate, and notes nobody promoted linger as noise. No task
that *uses* context has any reason to fix this, and agents that use the store can succeed for a
long time on stale shortcuts. Unless maintaining the store is somebody's job, nobody does it.
That is the catalogue failure of `ARC-OP-23`, and it happens to machine memory as readily as to
human catalogues.

So gardening is a standing task, row 43 of
[070_task-allocation.md](../00_concept/070_task-allocation.md), run on the agentic layer's
heartbeat rather than on demand. It is the context store's counterpart to what
[145_entropy-and-pruning.md](145_entropy-and-pruning.md) does for warehouse objects.

## The jobs

| Job | What it does | Who acts |
|---|---|---|
| **Re-check** | Re-run the evidence or falsifier behind assertions whose revalidation trigger has fired or whose review date has passed; mark them stale if they cannot be re-confirmed | D re-computes; A interprets |
| **Quarantine** | When a check fails on a *ruled* fact, mark it unusable at once, without waiting for a person — the ruling itself is untouched; dependent tasks go to a blocked or qualified state until a person decides | D, under an approved rule; H decides the outcome |
| **Rebuild summaries** | Regenerate summaries whose underlying objects changed ([122](122_context-retrieval.md)) | A, triggered by D's change detection |
| **Merge near-duplicates** | Merge claims only where predicates and scopes are equivalent; otherwise link them ([124](124_context-write-back.md)) | A proposes; routine merges under an approved rule; H where meanings differ |
| **Expire notes** | Remove unpromoted notes past their period, keeping negative findings ([124](124_context-write-back.md)) | D, under an approved rule |
| **Find contradictions** | Between two cards, between a normative and a descriptive claim, or between a card and the landscape facts (a card says unique; today's profile shows duplicates) | D detects; A explains; H rules where a ruled fact is contradicted |
| **Detect drift** | A table's temporal behaviour ([127](127_temporal-behaviour.md)) or a relationship's cardinality ([128](128_join-knowledge.md)) no longer matches what was recorded | D monitors; A explains; H decides the consequence |
| **Handle absences** | Cards for objects that seem to have disappeared, and links that point nowhere | D detects; see *absence is not deletion* below |
| **Propagate erasure** | When records must be erased or corrected (row 37 of 070), remove them from *every* copy — see below | H decides policy; D executes and verifies |
| **Improve recipes** | Use the measurements of [122](122_context-retrieval.md) to adjust recipes | A proposes; H approves |
| **Reconcile gardening itself** | Check that every eligible object was actually maintained: coverage counts, the oldest overdue work, retry limits, alerts for stalled or permanently failing jobs | D |

## Absence is not deletion

A failed scan, a lost permission or a partial inventory makes live objects look deleted.
Removing their context on that basis destroys knowledge that is still true. So a card is
removed only on **a successful, complete inventory plus positive evidence of deletion**.
Uncertain absences are quarantined, not removed. The same principle governs deletion detection
in the data itself ([127](127_temporal-behaviour.md)).

## Erasure reaches every copy

Removing sample values from the current version of a card leaves them in git history, derived
indexes and retained outputs; verifying against the current files alone would falsely report
completion. So every place the store persists data is tracked, each has a deletion procedure,
and erasure is verified across all of them. The cheaper protection is prevention: **cards
should not hold raw values of personal data at all.** Such values belong only in the facts
store, under its retention policy, where deleting them is an ordinary operation.

## Concurrency

Gardening runs alongside other work. A summary rebuild that reads a card, while another task
corrects it, would otherwise publish the older interpretation over the correction. So every
write carries a **revision precondition** — it succeeds only if the object has not changed since
it was read — conflicts are retried, and retries are **idempotent**.

## Mandate

Most gardening is routine and runs under rules a person approved once, in the sense Astra's
earlier review gave that phrase in
[XREV_2026-09-24_task-allocation_astra](../30_research/notes/XREV_2026-09-24_task-allocation_astra.md):
approving a procedure is not the same as deciding each case under it. Changing or removing a
**ruled** fact always goes to a person — but *quarantining* one, when a check fails, does not
wait, because otherwise agents keep consuming a disproven fact in the meantime.

## Measuring it

Measures that improve when defects are hidden are worse than none: deleting disputed material
makes a store look healthier, and better detection looks like deterioration. So three things
are measured separately:

- **detection** — defects found;
- **unresolved defects** — found and not yet fixed, with their age;
- **exposure** — how often stale, quarantined or disputed claims still reach tasks.

Alongside them, **answer correctness** on the fixed benchmark tasks of
[122](122_context-retrieval.md), and **freshness and contradiction coverage** measured
independently of whether tasks succeed.

## Open

How often each job runs, and what it costs, is not yet estimated. It is part of the running
cost the task table's patterns flag as unmeasured (`ARC-OP-24`).
