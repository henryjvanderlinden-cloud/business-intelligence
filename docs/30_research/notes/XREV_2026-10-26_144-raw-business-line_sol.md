# XREV 2026-10-26 — 144 section 2: the line between raw vault and business vault — sol

```yaml
object:        docs/10_architecture/144_raw-vault-business-vault-calculation-engines.md §2, as committed in ad64b5b/68090d3.
reviewer:      gpt-5.6-sol, via the Codex MCP server on the author's desktop, reasoning effort medium, workspace-write sandbox,
               no browsing; answer written to the ignored scratch/ folder with apply_patch.
assignment:    assume an experienced Data Vault 2.0 practitioner would reject the line; up to six modelling errors with failure
               cases; ADR-0025 (engine results in the raw vault) not to be argued as a preference; the rule-8 hedge and
               that nothing is built excluded; praise, summary and general assessment forbidden.
second reader: assignment set by Claude Opus 5.5, which drafted the object in session 09 on 2026-10-26; the revisions
               made in response are unreviewed by construction.
verdict:       FAILS [a source-supplied value produced by a mutable source rule satisfies both placement tests, so the proposed
               boundary can remove the source assertion required for audit]. Resolved in the revised text, unreviewed.
```

## sol's answer, verbatim

## Finding 1

**Quote:** “It would keep everything every source delivered, integrated on business keys and stamped with when it arrived, so that nothing is ever lost and any past state can be reconstructed.”

**What is wrong:** An arrival timestamp provides load-time history, not source-valid history, and an insert-only payload satellite does not by itself record disappearance from a snapshot or deletion from a source. The raw vault described here therefore cannot support the universal reconstruction claim.

**Failure case:** A daily customer snapshot contains `C1,status=active` on 1 March and contains no `C1` row on 2 March because the customer was deleted. Loading only delivered rows leaves the 1 March satellite row current. A reconstruction of the source on 2 March wrongly returns C1 as active.

**Correction:** Distinguish load time from source-effective time. Preserve snapshot membership or CDC operation explicitly, using a record-tracking/effectivity structure and source-provided effective timestamps where they exist; limit reconstruction claims to the temporal evidence actually captured.

**Confidence:** High.

## Finding 2

**Quote:** “It is generated from the key declarations by templates; the only human judgement in it is the keys.”

**What is wrong:** Keys do not determine relationship grain, driving-key behaviour, multi-active cardinality, or whether a source row is an entity, event, relationship, or repeating child. Those are raw-vault modelling decisions, not template consequences of hub-key declarations.

**Failure case:** The source delivers two order lines, `(order=O1,line=1,product=P1,qty=1)` and `(order=O1,line=2,product=P1,qty=2)`. A template that knows only the Order and Product business keys creates the same Order–Product link key twice and collapses the two occurrences. A downstream order total is 1 or 2 instead of 3.

**Correction:** Require explicit declarations of source grain, relationship identity, dependent-child or event keys, multi-active discriminators, and CDC semantics. Generate raw-vault objects only after those modelling judgements are recorded.

**Confidence:** High.

## Finding 3

**Quote:** “The only transformations allowed are technical and loss-free: hashing keys, mapping types without loss, and splitting attributes into satellites by source and rate of change.”

**What is wrong:** Rate of change is not a stable semantic boundary for raw-vault satellites. Splitting one atomic source assertion on that basis permits independently loaded timelines to manufacture combinations the source never asserted.

**Failure case:** One source row changes atomically from `{address=A,status=active}` to `{address=B,status=inactive}`. Separate “slow” address and “fast” status loaders commit at 12:00:01 and 12:00:03. An as-of query at 12:00:02 returns `{address=B,status=active}`, although neither input row had that state.

**Correction:** Group raw-vault satellite attributes primarily by source and source assertion/grain, with separate satellites only for a justified semantic, security, cardinality, or delivery boundary. If one source transaction must populate several satellites, preserve a common batch/assertion identifier and atomic temporal alignment.

**Confidence:** High.

## Finding 4

**Quote:** “It serves five purposes: nothing is lost (all the data and all the history, insert-only, the first two properties of ADR-0013); integration on identity where identity is certain (hubs join sources only on keys that mean the same thing) …”

**What is wrong:** Equal-looking business keys are not necessarily in the same namespace. “Mean the same thing” is insufficient unless uniqueness scope and collision policy are part of the hub definition; otherwise raw-vault integration can create a false enterprise identity.

**Failure case:** CRM delivers customer `123` for Alice and the German billing system delivers locally scoped customer `123` for Bob. Loading both to one Customer hub on the literal key produces one hub row with two satellites. A customer mart then reports Alice’s contacts with Bob’s invoices.

**Correction:** Define each hub key’s uniqueness scope and business-key collision code. Qualify locally scoped keys by the owning namespace, and represent cross-key-space identity claims as historised, evidence-bearing same-as mappings rather than collapsing hubs.

**Confidence:** High.

## Finding 5

**Quote:** “Two questions place an object: *did a system say this?* puts it in the raw vault; *would it change if a rule changed tomorrow?* puts it in the business vault.”

**What is wrong:** The tests are not mutually exclusive. Operational systems routinely deliver values calculated by their own mutable rules. The raw/business boundary is provenance—source assertion versus warehouse derivation—not whether some rule could change the value.

**Failure case:** An ERP invoice row says `net=100,tax=20,total=120`; the ERP tax rule later changes. The first test puts `tax=20` in the raw vault, while the second puts it in the business vault. Following the second test and retaining only a warehouse-recalculated tax of 21 makes an audit of the original invoice wrongly report that the ERP said 121.

**Correction:** Store exactly what the source asserted in the raw vault, including source-calculated values, with record source and load metadata. Put warehouse-applied interpretations and recalculations in the business vault and retain their rule versions and lineage back to the source assertion.

**Confidence:** High.

## Finding 6

**Quote:** “Raw vault, business vault and marts then form a chain in which marts select and shape but never calculate, so that two marts cannot compute ‘revenue’ in two ways.”

**What is wrong:** A Data Vault business vault should centralise reusable business rules, not every presentation-specific aggregation or analytic measure. Different marts can legitimately calculate differently because they answer different questions; forcing both calculations into one business-vault value erases required semantic context rather than preventing inconsistency.

**Failure case:** The raw data contains a EUR sale of 100, a transaction-date rate of 1.10, and a month-end management rate of 1.20. The statutory mart requires revenue of 110 USD and the management mart requires 120 USD. A single precomputed business-vault `revenue_usd` makes one mart wrong whichever rate it chooses.

**Correction:** Put shared, governed derivations and reusable rule outputs in the business vault. Permit marts to calculate grain-, aggregation-, scenario-, and presentation-specific measures, with explicit measure definitions and lineage; create distinct governed business-vault measures only when both conversions are genuinely reusable.

**Confidence:** High.

VERDICT: FAILS [a source-supplied value produced by a mutable source rule satisfies both placement tests, so the proposed boundary can remove the source assertion required for audit]

## Dispositions

1. **Accepted.** The reconstruction claim is limited to captured evidence; deletions and snapshot membership need
   explicit record tracking or effectivity, and source effective time is kept beside load time, as 127 already says.
2. **Accepted.** Declarations carry grain, relationship identity, dependent-child and event keys, multi-active
   discriminators and change-capture semantics, not only keys; generation follows once they are recorded.
3. **Accepted in substance.** Satellites are grouped by source and by what one source row asserts; a split needs a
   stated reason, and satellites filled from one row share load time and batch identifier. Note 030 §2 item 4 still
   says "split by source and rate of change"; flagged under `ARC-OP-37`, not edited.
4. **Accepted.** Hub integration is on keys from the same key space; section 3 carries the rule.
5. **Accepted; the strongest finding.** The boundary is provenance. The second placing test is withdrawn, and
   source-computed values stay in the raw vault.
6. **Partly accepted.** "Never calculate" was overstated: marts may aggregate. Not accepted that marts compute
   rule-dependent measures themselves, which would contradict ADR-0024 decision 1; two legitimate conversions become two
   named engine measures, and each mart selects one.
