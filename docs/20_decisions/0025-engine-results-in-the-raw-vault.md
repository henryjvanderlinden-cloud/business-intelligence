# ADR-0025 — Engine results land in the raw vault; when full recomputation cannot be afforded, a cut-off date, then going forward only, by human adjudication

- **Status:** Accepted
- **Date:** 2026-10-26
- **Supersedes:** —
- **Superseded by:** —
- **Amends:** [ADR-0024](0024-calculation-engines-are-a-versioned-source.md) (where engine results land; the fallback
  it left open)

## Context

[ADR-0024](0024-calculation-engines-are-a-versioned-source.md) made the calculation engines' output a separate source
and left two things open, listed as items 3 and 5 of [`ARC-OP-37`](../../registers/OPEN_POINTS.md). First, where the
results land: the model proposed the raw vault, under the engine's own source code
([144](../10_architecture/144_raw-vault-business-vault-calculation-engines.md) §4), while the financial-services note
[030](../60_domain-knowledge/financial-services/030_bird-as-data-vault-foundation.md) §2 item 5 placed calculated
values in the business vault. Second, what happens on a new engine version when there is not enough compute or storage
to recompute everything, which the author had answered with "it depends".

The author ruled on 2026-10-26 at 09:12, verbatim:

> 3: engine results go in the raw vault. Open fall back: if there is not enough compute, first let's try it from a
> cut-off date. If still not enough, only do going forward. It always requires human adjudication.

## Options considered

*Engine results in the business vault*, as 030 had it. Its case: the raw vault then holds only what operational
systems delivered, and everything computed here sits together with the rest of our interpretation. Rejected by the
author: the engines are a source (ADR-0024), and their stored, versioned, insert-only results are memory, not
something rebuilt on each run.

*Engine results in the raw vault, under the engine's own source code.* Adopted.

For the fallback, the alternatives were to recompute only on request, or to leave the choice to the agent layer by a
fixed rule. Both are set aside by the ruling, which fixes the order of the fallback and keeps a person in the decision.

## Decision

1. **Engine results land in the raw vault**, under the engine's own source code and labelled as derived, so that they
   are never taken for data delivered by an operational system. The raw vault's placing question is therefore *did a
   system say this?*, with our own engines counted as systems.
2. **When compute or storage do not allow recomputing everything on a new engine version**, the version is first
   recomputed from a cut-off date onwards; if that is still too much, it is applied going forward only.
3. **Every use of the fallback is adjudicated by a person**: the choice of cut-off, and the step down to going forward
   only.

## Consequences

The raw vault holds two kinds of source: operational systems and our own engines. Loading, change detection and tests
treat both alike, insert-only, with the engine version part of what counts as a change (ADR-0024).

Where the fallback is used, the history before the cut-off, or before the release, keeps the earlier version's
results. A mart that spans the boundary mixes versions, and must show which version applies to which period.

Note 030 §2 item 5 is corrected to agree with this decision, with the earlier text kept.

**Revisit** if a second engine depends on the results of a first in a way that makes the raw vault's insert-only
history hard to reason about, or if adjudicating every fallback becomes a burden that a rule could carry.
