# ADR-0013 — The integration layer is Data Vault or a functionally equivalent layer

- **Status:** Accepted
- **Date:** 2026-09-25
- **Supersedes:** —
- **Superseded by:** —

## Context

The overview for discussion, [080](../00_concept/080_overview-for-discussion.md), names Data Vault as
the layer that holds all data, all the time. External review of its updated points on 2026-09-25,
recorded in
[XREV_2026-09-25_overview-points_sol](../30_research/notes/XREV_2026-09-25_overview-points_sol.md),
found that a mandatory Data Vault contradicts the claim of [ADR-0012](0012-generic-framework-lean-start.md)
that the framework is generic. The author ruled, verbatim:

> No, it's not Data Vault per se, but it is kind of an industry standard on capturing all the data,
> all the time. So Data Vault is the example, but I'd be hard pressed to find another. Maybe hedge
> with Data vault or functionally equivalent framework.

"Functionally equivalent" needs a test, or it admits anything. The test below is the one the rest of
the framework depends on, proposed by Claude Opus 5.5 in the same conversation and adopted with the
author's instruction to process the findings.

## Options considered

*Data Vault, mandatory.* Its case: it is the industry standard for this job, practitioners recognise
it at once, and the design documents are written in its terms. Rejected as a requirement because it
ties a generic framework to one modelling method when what the framework needs is a set of
properties.

*Any historised layer.* Its case: maximal generality. Rejected because a layer that historises only
source keys — a plain persistent staging area — does not integrate across sources on business keys,
and the framework's central bet, `EVI-OP-1`, is about proposing exactly those keys.

*Data Vault as the example, or a layer with the same properties.* Adopted.

## Decision

**The integration layer is Data Vault or a functionally equivalent layer.** Data Vault is the
example the framework is described in. A layer is functionally equivalent when it has all three
properties:

1. it keeps **all the data** delivered from the sources, not a selection made for current reports;
2. it keeps **all the history**, insert-only, so that any past state can be reconstructed;
3. it **integrates on business keys** across sources, not only on source keys.

Anchor modelling, for example, meets the test; a persistent staging area on its own does not.

## Consequences

Framework documents may keep using Data Vault terms — hubs, links, satellites — and should be read as
using the example. Where a claim depends on something peculiar to Data Vault rather than on the three
properties, it should say so.

The central bet is unaffected: every equivalent layer depends on business keys.

**Revisit** if a layer is found that serves the framework without integrating on business keys, or if
the three properties turn out not to be what the rest of the design depends on.
