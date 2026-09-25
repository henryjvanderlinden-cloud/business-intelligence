# XREV 2026-09-25 — context system (120, 124, 126) — astra

```yaml
object:        docs/10_architecture/120_context-layer.md (sections "Five kinds of context" and
               "One store, two views"), 124_context-write-back.md and
               126_context-gardening.md, first drafts, at commit 24ec30f.
reviewer:      gpt-6-astra, reasoning effort medium, via the Codex MCP server on
               desktop-lv8udh0 (pinned Codex 0.153 in C:\Tools\codex-0153), sandbox read-only,
               thread 01a0d768-e51b-7cf3-9e78-b973e8e6abff. First pass in which the reviewer
               read the files itself, one file per question.
assignment:    three chained questions, adversarial ("assume they are wrong"), ranked, praise,
               general assessment and summary forbidden, no repeats across questions, 300
               words each. Q1 120; Q2 124; Q3 126. 122, 127 and 128 went to sol in parallel.
second reader: assignment set by Claude Opus 5.5, which drafted the object. The author read
               the findings and accepted all of them.
verdict:       FAILS in part on all three — seventeen findings, each with a minimal fix; all
               integrated 2026-09-25.
```

Astra's answers are reproduced verbatim below.

## Q1 — 120: kinds of context, and one store with two views

1. **The split loses the evidence behind durable knowledge.** A card could approve a join because yesterday’s profile showed unique keys; regenerated landscape facts could erase that observation while the approval survives. Retrieval could also combine incompatible database, Git and journal versions. **Minimal fix:** retain immutable evidence snapshots for promoted assertions, record their dependencies, and retrieve against an explicit version manifest. Mark conclusions stale when supporting evidence changes.

2. **“Highest trust” conflates authority with truth.** A person can authoritatively define a KPI without correctly describing its implementation. An approved decision could therefore override measured evidence that the warehouse calculates something different. **Minimal fix:** distinguish normative decisions from descriptive claims. Record authority, scope and effective dates separately from evidential confidence; expose contradictions rather than choosing by kind.

3. **A shared store needs security and publication boundaries, not just two presentations.** Task journals could contain sensitive samples; hypotheses could appear beside approved catalogue definitions; retrieved prose could be mistaken for executable procedure. Agent access and human catalogue access need not coincide. **Minimal fix:** enforce access, publication status and executable authority before retrieval, including graph traversal and search. Share identifiers and assertions without assuming identical visible content.

4. **Expiring working memory conflates disposable reasoning with durable coordination.** An unresolved approval, retry checkpoint or external action receipt could disappear with its journal. Another heartbeat could repeat an action or abandon unfinished work. **Minimal fix:** separate durable workflow state and action records from expiring scratch memory; retain them until explicit closure.

5. **Agent dependence does not guarantee catalogue maintenance.** An agent could repeatedly succeed using stale shortcuts, never visiting neglected objects or noticing changed business meaning. Usage could reinforce the same unsupported claims. **Minimal fix:** give assertions explicit revalidation triggers and ownership; measure freshness and contradiction coverage independently of task success.

## Q2 — 124: write-back

1. **Matching an existing claim is treated as rechecking it.** An agent could retrieve an assertion, recognise its own proposed write as equivalent, and advance *last re-checked* without testing anything. Repetition would manufacture apparent freshness. **Minimal fix:** update that timestamp only after a recorded verification; track encounters separately.

2. **“Machine-checkable” does not mean the machine checked the right claim.** A uniqueness test could exclude nulls or examine one partition, then admit “this column is unique” as evidenced. The routing would bypass review of the mismatch. **Minimal fix:** bind verification to an explicit predicate, population, exclusions and test result. Admit only the claim those checks establish.

3. **The ladder mistakes broader scope for greater trust.** Evidence for one dataset could become a rule covering an entire source family merely by promotion. Recording counterexamples would not establish validity for unexamined members. **Minimal fix:** treat generalisation as a new hypothesis requiring its own validation; keep scope and trust as independent attributes.

4. **Mandatory write-back creates an unbounded adjudication workload.** Every task could submit semantic claims and question cards faster than people resolve them. Agents could manufacture marginal “learnings” to satisfy completion, burying consequential submissions. **Minimal fix:** permit an explicit no-change result, cap submissions, and prioritise review by consequence and reuse. Batch related claims before requesting adjudication.

5. **Expiry selects for attention, not informational value.** A rare failed approach could expire because nobody references it; the next quarterly task would repeat the same investigation. Popular notes would survive regardless of usefulness. **Minimal fix:** retain compact, searchable negative findings with revisit conditions; choose retention by recurrence and rediscovery cost rather than references alone.

6. **Near-duplicate merging can erase meaningful distinctions.** “Unique per tenant” and “globally unique” could collapse into one claim despite retained provenance. **Minimal fix:** require equivalent predicates and scopes before merging; otherwise link the claims.

## Q3 — 126: gardening

1. **Erasure could leave recoverable copies.** Removing sample values from current cards would leave them in Git history, derived indexes or retained outputs. Verification against current files would falsely report completion. **Minimal fix:** track every persisted copy, define deletion procedures for each substrate, and verify erasure across those copies.

2. **Escalation could leave disproven ruled facts operational.** If marking a ruled assertion unusable counts as changing it, gardening would await a human while agents continue consuming it. **Minimal fix:** authorise immediate quarantine on failed checks, separately from changing the ruling; route dependent tasks to an explicit blocked or qualified state.

3. **The measurements reward hiding defects.** Deleting disputed material could reduce labels reaching tasks and shorten retrieval, making a less informative store look healthier. Better detection could conversely look like deterioration. **Minimal fix:** measure detection, unresolved defects and retrieval exposure separately; evaluate answer correctness and coverage against fixed cases.

4. **Concurrent gardening could overwrite newer work.** A summary rebuild could read a card, another task could correct it, and the rebuild could publish the older interpretation over that correction. Individually approved procedures would still produce an invalid result. **Minimal fix:** require revision preconditions on writes, retry conflicts, and make job retries idempotent.

5. **“Remove orphans” confuses absence with deletion.** A failed scan or lost source permission could make live objects appear nonexistent and trigger removal of their context. **Minimal fix:** require a successful, complete inventory plus positive deletion evidence; quarantine uncertain absences.

6. **A missing reconciliation job would let gardening silently stop.** Heartbeat execution alone would not reveal skipped objects, lost change events or permanently failing jobs. Retrieval complaints might arrive much later. **Minimal fix:** periodically reconcile eligible objects against completed maintenance, with coverage counts, oldest overdue work, retry limits and alerts for stalled jobs.

## How it was incorporated

120 gained a sixth kind of context (workflow state), evidence snapshots and version manifests,
the normative/descriptive split, publication boundaries for the shared store, and revalidation
triggers with owners. 124 and 126 were rewritten around the findings; each opens with a note of
what changed.
