# 126 — Context gardening: keeping the system's memory true

Part of the context system described in [120_context-layer.md](120_context-layer.md). Drafted
2026-09-25, session 04. The author singled this out as the most important of the context
points raised that day. Nothing here is built.

## Why it is a task in its own right

A context store decays by default. Facts go stale when sources change, summaries drift from
what they summarise, duplicates accumulate, and notes nobody promoted linger as noise. No task
that *uses* context has any reason to fix this, so unless maintaining the store is somebody's
job, nobody does it. That is the Collibra failure of `ARC-OP-23`, and it happens to machine
memory as readily as to human catalogues.

So gardening is a standing task, row 43 of
[070_task-allocation.md](../00_concept/070_task-allocation.md), run on the agentic layer's
heartbeat rather than on demand. It is the context store's counterpart to what
[145_entropy-and-pruning.md](145_entropy-and-pruning.md) does for warehouse objects.

## The jobs

| Job | What it does | Who acts |
|---|---|---|
| **Re-check** | Re-run the evidence or falsifier behind assertions whose review date has passed; mark them *stale* if they cannot be re-confirmed | D re-computes; A interprets |
| **Rebuild summaries** | Regenerate landscape maps, source summaries and cards whose underlying objects changed ([122](122_context-retrieval.md) zoom levels) | A, triggered by D's change detection |
| **Merge near-duplicates** | Find cards or assertions that say the same thing; merge them and keep both provenances | A proposes; routine merges under an approved rule, H where meanings differ |
| **Expire notes** | Remove unpromoted notes past their period ([124](124_context-write-back.md)) | D, under an approved rule |
| **Find contradictions** | Between two cards, or between a card and the landscape facts (a card says *unique*, today's profile shows duplicates) | D detects; A explains; H rules where a ruled fact is contradicted |
| **Detect drift** | A table's temporal behaviour ([127](127_temporal-behaviour.md)) or a relationship's cardinality ([128](128_join-knowledge.md)) no longer matches what was recorded | D monitors; A explains; H decides the consequence |
| **Remove orphans** | Cards for objects that no longer exist, and links that point nowhere | D detects; A proposes; H for anything ruled |
| **Propagate erasure** | When records must be erased or corrected (row 37 of 070), remove them from the context store too: cards may quote sample values, and profiles may hold personal data | H decides policy; D executes and verifies |
| **Improve recipes** | Use the after-task measurements from [122](122_context-retrieval.md) to adjust recipes that load too much or miss what is needed | A proposes; H approves |

## Mandate

Most gardening is routine and runs under rules a person approved once, in the sense
Astra's review gave that phrase in
[XREV_2026-09-24_task-allocation_astra](../30_research/notes/XREV_2026-09-24_task-allocation_astra.md):
approving a procedure is not the same as deciding each case under it. Two things always
escalate to a person: anything that would change or remove a **ruled** fact, and any
contradiction the agentic layer cannot resolve from evidence.

## Measuring it

A garden that is tended shows up in the retrieval measurements of
[122](122_context-retrieval.md): fewer loads per task, fewer *stale* or *disputed* labels
reaching tasks, and fewer after-task reports of context that was needed and not found. If
those measures worsen, the gardening is falling behind.

## Open

How often each job runs, and what it costs, is not yet estimated. It is part of the handoff
and running cost the task table's patterns flag as unmeasured (`ARC-OP-24`).
