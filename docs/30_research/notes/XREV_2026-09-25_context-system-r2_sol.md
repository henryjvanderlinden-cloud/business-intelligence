# XREV 2026-09-25 — context system, second pass (120, 124, 126) — sol

```yaml
object:        docs/10_architecture/120_context-layer.md (sections added 2026-09-25),
               124_context-write-back.md and 126_context-gardening.md, as revised after astra's
               first pass, at commit c4a1315.
reviewer:      gpt-5.6-sol, via the Codex MCP server on desktop-lv8udh0 (pinned Codex 0.153 in
               C:\Tools\codex-0153), sandbox read-only, thread
               01a0d79d-78fd-7462-9b1e-5650b4f6b185. Read the files itself, one per question.
assignment:    crossed second pass: sol took the documents astra had reviewed. Three chained
               questions, adversarial, ranked, 300 words each, praise, assessment and summary
               forbidden, told the documents were already reviewed and revised and not to
               repeat what they reflect.
second reader: assignment set by Claude Opus 5.5, which drafted and revised the object. The
               author accepted every finding, and ruled Q1.1, Q1.4 and Q1.5 as design
               decisions in ADR-0011.
verdict:       FAILS in part on all three — eighteen findings; three became architectural
               decisions; all integrated 2026-09-25.
```

Sol's answers are reproduced verbatim below.

## Q1 — 120

1. **The six kinds conflate semantics, lifecycle, authorship, and storage.** A business key may be machine-observed, human-declared, or contractually mandated; forcing it into “knowledge” loses those distinctions. “Deterministic” lineage and profiles are also tool- and configuration-dependent. This will produce misplaced claims and incorrect trust. **Minimal fix:** classify each assertion independently by subject, epistemic status, authority, volatility, owner, and retention; derive storage placement from those attributes.

2. **Evidence snapshots are underspecified and potentially unbounded.** Retaining “the evidence” could mean sensitive rows, huge profiles, or results that cannot be reproduced because query text, code, parameters, and source state were omitted. Staleness also cannot be inferred merely because evidence changed. **Minimal fix:** define a content-addressed evidence bundle containing source version/as-of time, query or computation, parameters, tool/code version, privacy classification, retained aggregate or sample, and an assertion-specific invalidation predicate.

3. **Normative versus descriptive is too coarse for warehouse reality.** “What is” collapses implemented logic, observed data behaviour, documentation, and certified business interpretation. An ETL expression can disagree with production observations while both remain descriptively true. **Minimal fix:** distinguish at least intended, declared, implemented, observed, and certified claims, each with effective and observation times.

4. **Card kinds mix domain objects with statements and workflow containers.** `assertion`, `hypothesis`, `rule`, and `relationship` overlap; representing joins or set-wide rules as cards will create duplication, inconsistent updates, and card explosion. **Minimal fix:** make assertions the canonical typed graph records; treat cards as bounded projections around stable domain objects. Hypothesis and approval become assertion status, not parallel object kinds.

5. **“One store” contradicts the proposed physical separation and understates security leakage.** A shared index can reveal sensitive object existence, relationships, or draft claims even when text is hidden. Human catalogue publication and agent operational memory also require different retention and transaction guarantees. **Minimal fix:** specify one logical identity plane over separate stores, with policy-filtered indexes and an explicit publication pipeline; do not share an unfiltered graph.

## Q2 — 124

1. **Write-back occurs too late.** A crashed, cancelled, or partially failed task never reaches its mandatory final step, losing precisely the diagnostics needed for recovery. Retrying may instead duplicate writes. **Minimal fix:** append observations and actions incrementally with task/run IDs and idempotency keys; finalisation only marks the run complete.

2. **Routing assumes each write has one destination.** A discovered orphan rate may be simultaneously an observation, evidence for a semantic hypothesis, and a workflow blocker. Single routing either drops required consequences or copies disconnected versions. **Minimal fix:** accept one immutable write-back envelope, then route references to multiple consumers through explicit rules, recording routing decisions and failures.

3. **The ladder incorrectly makes trust appear monotonic.** Human ruling and empirical evidence are alternative paths to “assertion,” although they establish different things. Later contradiction, revoked approval, or changed source behaviour has no defined demotion path. `Rule` is wider scope, not greater maturity. **Minimal fix:** separate lifecycle (`proposed`, `accepted`, `contested`, `superseded`, `retracted`) from evidence and authority; model rules as scoped assertions, not the top rung.

4. **Queue caps create silent knowledge loss and gaming.** Agents must choose what not to submit, task splitting bypasses caps, and batching can force reviewers to accept or reject mixed-quality claims together. Consequence/reuse prioritisation can indefinitely starve rare but regulatory-critical claims. **Minimal fix:** persist all candidates outside the adjudication queue; apply deduplication, service classes, ageing, capacity limits, and per-claim decisions inside batches.

5. **Expiry policy is not operationally decidable.** “Likelihood of recurrence” and “cost to rediscover” lack owners, values, or decision points, so notes will either accumulate or disappear arbitrarily. Sensitive notes may also outlive their permitted retention. **Minimal fix:** assign retention class, review date, owner, privacy ceiling, and expiry reason at creation; retain a tombstone or non-sensitive digest.

6. **Merging lacks reversibility and concurrency control.** Equivalent-looking claims may later diverge by validity period or source correction; concurrent PRs can merge against stale state. **Minimal fix:** keep source claims immutable, create reversible canonical-group links, and require optimistic version checks before consolidation.

## Q3 — 126

1. **Essential job missing: dependency invalidation.** Re-checking or quarantining a premise does not automatically invalidate derived assertions, summaries, recipes, or benchmark answers. Downstream material can remain trusted indefinitely. **Minimal fix:** add an impact-propagation job that traverses provenance dependencies, marks affected products stale, and schedules recomputation in dependency order.

2. **Per-object revision checks do not protect multi-object consistency.** A contradiction scan, merge, or graph rebuild can publish a mixture of revisions even though every individual write passes its precondition. Agents then traverse a state that never existed. **Minimal fix:** run multi-object jobs against a read watermark and atomically publish a complete generation, or reject it if any dependency changed.

3. **Quarantine has no blast-radius policy.** Failure of one widely reused assertion could block an entire reporting estate; allowing “qualified” continuation without defined semantics could instead expose known-bad outputs. **Minimal fix:** type dependency edges as hard or advisory, assign failure severity, calculate impact before activation, and define approved degraded modes and escalation deadlines.

4. **Absence confirmation may be impossible.** Many sources provide neither deletion events nor authoritative inventories, so requiring positive deletion evidence leaves permanent ghost objects. **Minimal fix:** define source-specific confirmation protocols and a lifecycle such as `suspected-absent`, `confirmed-absent`, and `retired`; retirement preserves history without presenting the object as current.

5. **Erasure has no bounded persistence inventory.** “Every copy” cannot be demonstrated if prompts, provider logs, caches, backups, exports, and user downloads are not registered. Git history may require destructive rewriting that conflicts with audit retention. **Minimal fix:** maintain a data-location register with processor, retention, deletion mechanism, backup horizon, exceptions, and verifiable erasure receipts; prohibit sensitive material where deletion cannot be guaranteed.

6. **The mandate is too binary.** Requiring a person for every ruled-fact change creates a backlog during routine migrations, while automatic quarantine can itself have major operational impact. **Minimal fix:** use risk-tiered mandates with pre-approved supersession patterns, impact thresholds, sampled review, and emergency override rules.

7. **Measurements lack denominators and service objectives.** Counts vary with estate size and scan intensity; fixed benchmarks invite overfitting. **Minimal fix:** report rates by risk class, time-to-detect and time-to-remediate, coverage denominators, explicit SLOs, and rotating held-out tasks.
