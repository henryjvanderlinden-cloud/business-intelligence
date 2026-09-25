# 126 — Context gardening: keeping the system's memory true

Part of the context system described in [120_context-layer.md](120_context-layer.md). Drafted
2026-09-25, session 04; the author singled it out as the most important of the context points
raised that day. Revised twice the same day after external review: first on GPT-6 Astra
([XREV_2026-09-25_context-system_astra](../30_research/notes/XREV_2026-09-25_context-system_astra.md)
Q3), which added erasure across every copy, quarantine, concurrency control, a stricter test for
deletion, honest measures and a job that checks gardening itself; then on gpt-5.6-sol
([XREV_2026-09-25_context-system-r2_sol](../30_research/notes/XREV_2026-09-25_context-system-r2_sol.md)
Q3), which added dependency invalidation, publishing in whole generations, limits on the impact
of quarantine, an absence lifecycle, a register of where data lives, risk-tiered mandates and
measures with denominators and targets. Nothing here is built.

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
| **Re-check** | Re-run the evidence behind assertions whose invalidation predicate has fired or whose review date has passed; mark them stale if they cannot be re-confirmed | D re-computes; A interprets |
| **Propagate invalidation** | When a premise is re-checked, quarantined or retracted, follow its dependencies and mark everything built on it — derived assertions, summaries, recipes, benchmark answers — stale, then schedule recomputation in dependency order | D |
| **Quarantine** | When a check fails on an accepted fact, mark it unusable within the limits below, without waiting for a person; the ruling itself is untouched | D, under an approved rule; H decides the outcome |
| **Rebuild summaries and views** | Regenerate cards and summaries whose underlying assertions changed ([122](122_context-retrieval.md)) | A, triggered by D's change detection |
| **Consolidate near-duplicates** | Only where predicates and scopes are equivalent, reversibly ([124](124_context-write-back.md)) | A proposes; routine cases under an approved rule; H where meanings differ |
| **Expire notes** | Apply the retention recorded on each note, keeping negative findings and tombstones ([124](124_context-write-back.md)) | D |
| **Find contradictions** | Between assertions of different claim types ([120](120_context-layer.md)), or between an assertion and the landscape facts | D detects; A explains; H rules where an authorised claim is contradicted |
| **Detect drift** | Temporal behaviour ([127](127_temporal-behaviour.md)) or cardinality ([128](128_join-knowledge.md)) no longer matching what was recorded | D monitors; A explains; H decides the consequence |
| **Handle absences** | Objects that seem to have disappeared — see the absence lifecycle below | D detects; source-specific protocols decide |
| **Propagate erasure** | Remove erased or corrected data from every registered location — see below | H decides policy; D executes and verifies |
| **Improve recipes** | Use the measurements of [122](122_context-retrieval.md) to adjust recipes | A proposes; H approves |
| **Reconcile gardening itself** | Check that every eligible object was actually maintained: coverage counts, oldest overdue work, retry limits, alerts for stalled or failing jobs | D |

## Quarantine, and its limits

When a check fails on a fact others rely on, agents must stop consuming it at once, not after a
person has looked. But quarantine can itself cause damage: one widely reused assertion failing
could block an entire reporting estate, while a vague "qualified" state could let known-bad output
through. So:

- dependencies are typed as **hard** (the dependent cannot be used without it) or **advisory**;
- each failure has a **severity**;
- the **impact is calculated before quarantine takes effect** — what would be blocked;
- there are **approved degraded modes** — for example, publish with a visible warning, or fall back
  to the last good version — and an **escalation deadline** by which a person must decide.

## Absence is not deletion

A failed scan, a lost permission or a partial inventory makes live objects look deleted. Many
sources also offer neither delete events nor an authoritative inventory, so demanding positive
proof of deletion would leave permanent ghost objects. So absent objects follow a lifecycle:

**suspected absent → confirmed absent → retired**

Each source has its own **confirmation protocol** saying what counts as confirmation for it. A
retired object keeps its history but is no longer presented as current. The same principle governs
deletion detection in the data itself ([127](127_temporal-behaviour.md)).

## Erasure reaches every copy — which means knowing every copy

Removing data from the current version of a record leaves it in git history, indexes, caches,
backups, prompts, provider logs, exports and user downloads. "Every copy" cannot be demonstrated
unless those places are known. So the system keeps a **data-location register**: for each place
data can persist, the processor, the retention, the deletion mechanism, the backup horizon and any
exceptions. Erasure is verified against the register and produces an **erasure receipt**.

Two consequences follow. Rewriting git history to erase something conflicts with keeping git as the
audit log, so **sensitive material is not allowed wherever deletion cannot be guaranteed** — which
includes cards and assertion records in git. Raw personal values belong only in the facts store,
under its retention policy, where deleting them is an ordinary operation.

## Consistency under concurrency

Gardening runs alongside other work. For a single object, every write carries a **revision
precondition** — it succeeds only if the object has not changed since it was read — conflicts are
retried, and retries are **idempotent**. That is not enough for jobs that touch many objects: a
contradiction scan or an index rebuild could publish a mix of versions that never existed together.
So multi-object jobs read against a **watermark** and **publish a complete new generation at once**,
or discard it if anything it depends on changed in the meantime.

## Mandate, tiered by risk

Most gardening is routine and runs under rules a person approved once — approving a procedure is
not the same as deciding each case under it
([XREV_2026-09-24_task-allocation_astra](../30_research/notes/XREV_2026-09-24_task-allocation_astra.md)).
But "a person for every change to an authorised fact" is too blunt: it creates a backlog during
routine source migrations, while automatic quarantine can itself have large consequences. So the
mandate is **tiered by risk**:

- **pre-approved patterns** for routine supersessions, such as a column renamed in a source
  migration;
- **impact thresholds** above which a person must decide;
- **sampled review** of what was done automatically;
- **emergency override** rules, with who may use them.

## Measuring it

Measures that improve when defects are hidden are worse than none, and raw counts move with the
size of the estate and the intensity of scanning. So:

- **detection**, **unresolved defects** and **exposure** (stale, quarantined or disputed claims
  still reaching tasks) are reported separately, as **rates with explicit denominators**, by
  **risk class**;
- **time to detect** and **time to fix** are tracked against **explicit targets**;
- **coverage** — the share of eligible objects actually maintained on schedule — is reported with
  its denominator;
- answer correctness is measured on the benchmark tasks of [122](122_context-retrieval.md), with
  a **rotating, held-out** portion so the system cannot tune itself to a fixed test.

## Open

How often each job runs, and what it costs, is not yet estimated. It is part of the running cost
the task table's patterns flag as unmeasured (`ARC-OP-24`).
