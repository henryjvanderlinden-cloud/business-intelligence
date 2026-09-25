# XREV 2026-09-25 — context system, second pass (128, 127, 122) — astra

```yaml
object:        docs/10_architecture/128_join-knowledge.md, 127_temporal-behaviour.md and
               122_context-retrieval.md, as revised after sol's first pass, at commit c4a1315.
reviewer:      gpt-6-astra, reasoning effort medium, via the Codex MCP server on
               desktop-lv8udh0 (pinned Codex 0.153 in C:\Tools\codex-0153), sandbox read-only,
               thread 01a0d79d-eda2-75b2-9cf1-8881795044b5. Read the files itself, one per
               question.
assignment:    crossed second pass: astra took the documents sol had reviewed. Three chained
               questions, adversarial, ranked, 300 words each, praise, assessment and summary
               forbidden, told the documents were already reviewed and revised and not to
               repeat what they reflect.
second reader: assignment set by Claude Opus 5.5, which drafted and revised the object. The
               author accepted every finding, and ruled the publication gate (Q1.3) a design
               decision in ADR-0011.
verdict:       FAILS in part on all three — twelve findings; all integrated 2026-09-25.
```

Astra's answers are reproduced verbatim below.

## Q1 — 128

1. **Passing query tests can conceal incorrect attribution.** Row counts and aggregate totals can both reconcile when one fact disappears and another equal-valued fact duplicates. A join to the wrong customer can preserve both perfectly. Minimal fix: require reconciliation per originating fact identity at the preserved grain, including expected match counts, plus independently specified attribution cases. Whole-query totals should be supplementary evidence.

2. **Declared uniqueness does not necessarily supply the join’s “one” side.** The document allows normalisation but treats source uniqueness as evidence without requiring proof that it survives the join expression. Unique keys `001` and `1` collide after integer casting; a unique `(tenant, customer)` constraint says nothing about joining on `customer` alone. Minimal fix: attach each constraint’s applicability to the complete join predicate and test uniqueness after the actual transformations and population filters.

3. **A standing-test failure has no operational consequence beyond gardening.** A later load could violate a previously approved relationship while marts remain available and `RELY` still authorises incorrect optimiser rewrites. Historical evidence and drift detection do not prevent that exposure. Minimal fix: define a deterministic publication gate tied to the tested data version, with failure blocking publication and revoking affected optimisation assertions before consumers access invalid data. Assign responsibility for remediation and reapproval.

4. **“Bridge weights sum to one per member” leaves the allocation denominator undefined.** In an account-to-customer bridge, weights summing to one per customer can still multiply account balances. Different measures or effective periods may also require different allocations. Minimal fix: specify the originating allocation grain, measure, applicable population and effective interval; sum weights across recipients for each such origin. Test coverage as well as sums, since an origin with no bridge rows can disappear without producing a failing weight group.

## Q2 — 127

1. **“Two timestamps, always” contradicts effective dating being absent.** An overwritten source may expose no business-effective time. Substituting extraction or load time would invent when a value became true, producing false historical answers. Minimal fix: permit unknown effective time, record timestamp provenance, and distinguish observed-state history from business-valid history. A person must decide which reporting questions remain answerable.

2. **Value-based hash differences can discard temporal corrections.** A correction can retain the same attribute value while changing its effective start, end or deletion status. Suppressing that record as a repeated value would lose the correction despite append-only loading and successful capture. Minimal fix: define change identity to include relevant temporal metadata and operation semantics, or preserve these independently of attribute-value deduplication.

3. **Extract completeness does not establish deletion.** A complete extract under a changed filter can legitimately omit existing rows; a fully traversed but non-atomic paginated read can miss rows moving between pages. Control totals, partitions and successful status need not resolve either case. Minimal fix: require an unchanged, explicitly comparable population and a consistent source snapshot or equivalent reconciliation protocol before inferring deletion. Otherwise record disappearance as unresolved.

4. **The capture guarantee confuses source capability with delivered coverage.** A CDC-enabled source can still lose history through log expiry, an inconsistent initial snapshot/stream handoff, or dropped events. Generic sequence-gap monitoring is insufficient: positions may legitimately skip or be ordered only within partitions. Minimal fix: record the guarantee’s coverage interval, bootstrap boundary, retention/recovery assumptions and source-specific cursor semantics. Machinery should verify snapshot-to-stream continuity and durable consumption against those semantics; the card should claim complete history only for demonstrated coverage.

## Q3 — 122

1. **Risk triggers depend on context that may never be retrieved.** If personal-data status is absent from the anchor card and discoverable only through upstream lineage, the security recipe may never activate. All selected mandatory items can be present while a mandatory recipe is missing. Minimal fix: require baseline risk screening before recipe selection; represent unknown risk explicitly and require investigation or escalation before proceeding.

2. **Composition lacks rules for incompatible requirements.** Two recipes can accept different evidence, require different facets or assign different budgets. An implementation could satisfy the weaker recipe and silently bypass the stronger one while claiming neither was truncated. Minimal fix: union mandatory requirements, require claims to satisfy every applicable acceptance rule, and stop on unresolved contradictions. Define a combined budget explicitly.

3. **Claim freshness does not establish compatibility between claims.** A recently verified definition and recently verified transformation may concern different schema or policy versions. Both can pass their individual acceptance rules while their combination supports an invalid decision. Similarly, a summary can cite sources without identifying which revisions it summarises. Minimal fix: bind claims and summaries to source revisions and validity scopes; validate compatibility across the assembled evidence, including transitive dependencies.

4. **The benchmark can reward stopping instead of solving.** A retriever that routinely stops after loading little context can achieve low cost, little irrelevant material and few downstream defects. Required-evidence recall helps, but the document gives no task-success criterion or treatment of appropriate versus unnecessary stops. Minimal fix: score correct completion and justified abstention separately, penalise unnecessary stops, and include benchmark cases with unavailable evidence, conflicting claims and risks discoverable only outside recorded links. Report results by task and risk class so routine cases cannot conceal consequential failures.
