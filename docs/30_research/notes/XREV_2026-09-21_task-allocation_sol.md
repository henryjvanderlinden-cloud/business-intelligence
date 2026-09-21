# XREV 2026-09-21 — task allocation draft — sol

```yaml
object:        the 28-row draft allocation of BI implementation tasks to faculties, stated
               inline in the prompt (no file existed yet). Now superseded by
               docs/00_concept/070_task-allocation.md, which incorporates this pass.
reviewer:      gpt-5.6-sol, via the Codex MCP server on desktop-lv8udh0, sandbox read-only,
               thread 01a0c50e-6d3e-7d73-8fd2-75f8bb50a972
assignment:    three chained questions, one per reply, 250-300 words each, reading and
               general assessment forbidden: Q1 omissions and wrong merges; Q2 wrong
               allocations; Q3 table structure and any consideration outside the 13
               dimensions. A first attempt with two questions in one reply timed out at the
               bridge's sixty-second ceiling.
second reader: assignment set by Claude Opus 5, which drafted the object. The author asked for
               the review and afterwards stated agreement with every finding.
verdict:       FAILS as drafted — fourteen omissions or splits, seven allocations disputed,
               the one-owner format replaced by a chain, and a fourteenth dimension proposed.
               All accepted by the author, 2026-09-21.
```

Sol's answers are reproduced verbatim below.

## Q1 — missing tasks, or wrong merges

- Requirements acceptance criteria and business sign-off — **human** — **13 (mandate)**.
- Source inventory should split into source discovery/ownership — **human** — **8 (unwritten/politics)**; and connectivity, extraction, CDC, ingestion — **deterministic** — **3 (repeatability)**.
- Data contracts, SLAs, and source-owner responsibilities — **human** — **13 (mandate)**.
- Data-quality rule definition should be separate from test writing — **human** — **8 (business context)**; rule execution/quarantine — **deterministic** — **3**.
- Reference/master-data stewardship and survivorship decisions — **human** — **9 (settles disputes)**.
- Reconciliation among source, vault, marts, finance, and legacy outputs — **deterministic** — **5 (checking cost)**; acceptance of discrepancies — **human** — **13**.
- Semantic-layer work should split into semantic contract/metric governance — **human** — **13**; generated implementation — **agentic** — **1 (spell-out cost)**.
- Dashboards should split into audience, questions, interaction and visual choices — **human** — **8**; dashboard construction — **agentic** — **1**; refresh/rendering — **deterministic** — **3**.
- Deployment engineering: versioning, CI/CD, environment promotion, rollback — **deterministic** — **6 (undoability)**.
- Performance engineering and capacity planning — **agentic** for diagnosis/proposals — **10 (novelty)**; deterministic benchmarking — **3**.
- Operational recovery: retries, replay, backfill, disaster recovery — **deterministic** — **6**.
- Troubleshooting should split diagnosis — **agentic** — **10**; routine remediation — **deterministic** — **3**; consequential decisions — **human** — **13**.
- Ad-hoc analysis should split retrieval/calculation — **deterministic** — **3**; exploratory hypothesis generation — **agentic** — **10**; interpretation and communication — **human** — **8**.
- User acceptance, training, adoption, and decommissioning legacy reports — **human** — **8**.

## Q2 — wrong allocations

- **Row 4 — Human. Dimension 8 (sees the unwritten/politics).** Tools can discover databases and schemas, but identifying authoritative sources, shadow systems, ownership, and politically preferred versions is primarily human work.
- **Row 7 — Deterministic. Dimension 12 (notices change).** Technical metadata upkeep should lead with automated harvesting, lineage capture, schema comparison, and catalog synchronization. Agentic systems can enrich descriptions and flag ambiguity.
- **Row 10 — Human. Dimension 13 (mandate).** Grain and historisation encode business meaning, audit obligations, correction policy, and what counts as the same event. The agent can recommend patterns, but humans should lead the choice, not merely rule on unusual cases.
- **Row 13 — Agentic. Dimension 10 (handles novelty).** If "orchestration" includes designing dependencies, retry policy, recovery paths, backfills, and exception handling, agentic should lead the design; deterministic machinery should execute the resulting schedule. If the row means execution only, the original allocation is correct.
- **Row 17 — Human. Dimension 8 (sees the unwritten/politics).** The semantic layer determines which measures, relationships, defaults, and perspectives users actually encounter. Generation can be agentic, but business-facing semantic design needs human leadership. Mart physical implementation may remain agentic/deterministic.
- **Row 23 — Deterministic. Dimension 3 (same answer every time).** Structural impact analysis should lead from machine-readable lineage, dependency graphs, version control, and query logs. Agentic reasoning is useful only for interpreting incomplete lineage and explaining business consequences.
- **Row 26 — Human. Dimension 13 (mandate).** Methodology determines governance, evidence standards, review gates, and acceptable risk. Agents can detect recurring friction and draft improvements, but "proposes" understates the human lead required to set institutional practice.

## Q3 — structure, and a fourteenth dimension

**(a) Use a chain per task:** proposes → decides → executes → checks.

BI tasks routinely cross faculty boundaries. The chain exposes control points, handoffs, segregation of duties, and where deterministic evidence must replace probabilistic judgment. "Lead" can still be derived as the faculty holding the decisive step.

A one-lead table loses these distinctions. It can label "testing" agentic even though humans define acceptance, agents draft cases, machinery executes them, and humans accept material discrepancies. It also hides whether "deterministic" means designing a process or merely running it.

**(b) Yes: candidate dimension 14 — ability to create commitment.**

This means gaining trust, changing behaviour, negotiating adoption, and getting people to retire familiar reports or processes. It differs from dimension 8: seeing unwritten politics does not imply being able to persuade people. It also differs from dimension 13: having a mandate does not ensure adoption.

It drove my Q1 allocation of **user acceptance, training, adoption, and legacy-report decommissioning** to humans. Without this dimension, one might allocate much of that work to the agentic faculty because it can generate training materials, analyse usage, collect feedback, and propose migration plans. The need to create durable human commitment flips the lead to humans.

## How it was incorporated

In [070_task-allocation.md](../../00_concept/070_task-allocation.md). Splits that are exactly
a proposes/decides/executes chain are represented by the chain columns rather than as
separate rows; splits that separate genuinely different work have their own rows.
