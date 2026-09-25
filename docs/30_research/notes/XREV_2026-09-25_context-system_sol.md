# XREV 2026-09-25 — context system (128, 127, 122) — sol

```yaml
object:        docs/10_architecture/128_join-knowledge.md, 127_temporal-behaviour.md and
               122_context-retrieval.md, first drafts, at commit 24ec30f.
reviewer:      gpt-5.6-sol, via the Codex MCP server on desktop-lv8udh0 (pinned Codex 0.153 in
               C:\Tools\codex-0153), sandbox read-only, thread
               01a0d769-39ab-78c1-aab6-c66d0865b44e. The reviewer read the files itself, one
               file per question.
assignment:    three chained questions, adversarial ("assume it is wrong or incomplete as a
               practitioner would judge it"), ranked, praise, general assessment and summary
               forbidden, no repeats, 300 words each. Q1 128; Q2 127; Q3 122. 120, 124 and 126
               went to astra in parallel.
second reader: assignment set by Claude Opus 5.5, which drafted the object. The author read
               the findings and accepted all of them.
verdict:       FAILS in part on all three — fifteen findings, each with a minimal fix; all
               integrated 2026-09-25.
```

Sol's answers are reproduced verbatim below.

## Q1 — 128: join knowledge

1. **Join grain and population are absent.** Cardinality is not an unconditional property of two objects; it depends on each side’s grain, filters, tenant/source, status, and effective-time window. Profiling an unfiltered pair can either hide or invent fan-out. **Minimal fix:** require each card to state both grains, directional join purpose, population predicates, and the measure whose aggregation must remain invariant.

2. **The three layers are not comparable as defined.** A foreign key declares inclusion, not cardinality; uniqueness supplies the “one” side. Constraints may also be disabled, unvalidated, partial, or scoped by predicates. A single observed label discards duplicate distributions and historical violations. **Minimal fix:** represent declared uniqueness and foreign-key constraints separately with enforcement/trust state; record observed multiplicity in both directions, violation counts, maxima, scope, and measurement time.

3. **Key semantics are insufficient for Data Vault and SCD joins.** “Key reuse” and temporal validity do not distinguish business keys, source-qualified keys, hash keys, warehouse surrogate keys, and SCD version keys. A fact joined to a dimension business key can match every historical version and multiply measures. **Minimal fix:** record key role and namespace, composite components, normalization ownership, and the exact point-in-time or resolved-surrogate rule.

4. **Referential integrity as an orphan rate is underspecified.** The denominator, direction, null treatment, late-arrival allowance, deletes, unknown members, and temporal validity determine whether an “orphan” is erroneous. One aggregate rate can conceal concentrated failures in valuable partitions. **Minimal fix:** define directional coverage metrics, exception classes, grace windows, temporal predicates, and segmented counts alongside rates.

5. **Human assertion followed by generated tests cannot safely resolve semantic ambiguity.** A reviewer may approve plausible cardinality while missing grain or measure behavior; a passing row-level test still permits fan/chasm inflation across a multi-join query. **Minimal fix:** add deterministic query-plan tests using representative measures: row-count preservation, aggregate reconciliation, bridge-weight totals, and multi-path fan-out checks before an asserted relationship becomes usable.

## Q2 — 127: temporal behaviour

1. **The behaviour classes combine independent dimensions.** An append-only event may arrive late; a versioned source may retroactively correct and soft-delete; a periodic snapshot may overwrite values. Forcing one classification loses necessary behaviour and produces the wrong history policy. **Minimal fix:** model separate axes for mutation, extraction/delivery, effective dating, arrival latency, correction, and deletion.

2. **“The Data Vault layer keeps every change it sees” is not inherently true.** Hash-difference rules may suppress repeats, faulty load logic may update satellites, and deletion or effective-date changes need explicit structures. A Raw Vault also cannot distinguish a correction from a new business-effective state merely from load order. **Minimal fix:** specify append-only loading guarantees, audit metadata, deduplication rules, effectivity/deletion records, and both source-effective and warehouse-load timestamps.

3. **Increasing load frequency cannot guarantee capture of overwritten states.** Two or more transitions between polls remain invisible regardless of profiling, so “observed change frequency” systematically understates actual volatility. The warehouse could present incomplete history as full history. **Minimal fix:** record the source’s capture guarantee; require CDC, an audit log, or source versions where complete transition history is required, otherwise label the history explicitly as sampled.

4. **Successive-load disappearance is not enough to detect hard deletion.** Missing rows can result from partial extracts, changed filters, pagination failures, delayed partitions, or failed source reads. Treating absence as deletion could create false tombstones and incorrect historical status. **Minimal fix:** require extraction-completeness evidence—control totals, watermarks, expected partitions, run status, and preferably explicit delete events—before classifying disappearance as deletion.

5. **The proposed monitoring observes values but not temporal order integrity.** Backfilled records, replayed batches, duplicate events, out-of-order CDC, and gaps in source sequences can all leave plausible values while corrupting the timeline. **Minimal fix:** deterministically monitor source sequence continuity, event-versus-ingestion latency, replay identifiers, duplicate delivery, and reconciliation of closed historical periods; route policy exceptions to the accountable data owner rather than generic “gardening.”

## Q3 — 122: retrieval

1. **Link traversal assumes the knowledge graph is already complete.** Real landscapes contain undocumented reports, copied SQL, aliases, spreadsheets, and cross-system dependencies. Starting from one anchor and following recorded links will confidently omit precisely the unknown relationships discovery must find. **Minimal fix:** combine traversal with bounded search, lineage/query-log scans, and reverse dependency discovery; expose graph-coverage uncertainty in every result.

2. **Fixed task-type recipes cannot represent compound work.** “Change a dimension” may simultaneously require security, regulatory, ownership, reconciliation, deployment, and consumer-impact context. A token budget can silently discard mandatory evidence while still satisfying the recipe. **Minimal fix:** make recipes composable and risk-triggered, distinguish mandatory from optional context, and fail closed when mandatory items are missing or truncated.

3. **The zoom levels form a false hierarchy.** A raw profile is not a more detailed field card, and neither substitutes for executable transformations, business definitions, lineage evidence, usage patterns, or prior decisions. Coarse summaries can also erase rare but decisive exceptions. **Minimal fix:** model independent context facets rather than five levels; every summary should cite its source artifacts, disclose omissions, and define automatic drill-down triggers.

4. **A single trust label is too coarse and sometimes unsafe.** “Ruled” describes authority, “evidenced” describes support, and “stale” describes freshness; these are not mutually exclusive. One card can contain claims with different owners and evidence. Accepting either ruled or evidenced can let a statistical observation substitute for an authorised semantic decision. **Minimal fix:** attach claim-level dimensions for provenance, authority, scope, evidence method, confidence, freshness, and conflict status; define acceptance rules per decision type.

5. **Both proposed measurements reward apparent efficiency, not correct outcomes.** “Load” is undefined: one enormous payload can game the three-load rule. The completing agent cannot report context it never knew existed, and “unused” evidence may have ruled out a dangerous option. **Minimal fix:** measure required-evidence recall, irrelevant-token ratio, cost, latency, reviewer corrections, and downstream defects against sampled benchmark tasks; collect missing-context findings from independent review and later incidents.

## How it was incorporated

122, 127 and 128 were rewritten around the findings; each opens with a note of what changed.
Three findings converged with astra's independent pass on 120, 124 and 126: absence is not
deletion (sol Q2.4, astra Q3.5), a single trust label conflates authority, evidence and
freshness (sol Q3.4, astra Q1.2), and the proposed measures can be gamed (sol Q3.5, astra
Q3.3).
