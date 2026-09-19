# ADR-0005 — Autonomy is tiered: structural, semantic, teleological

- **Status:** Accepted
- **Date:** 2026-09-19

## Context

The original brief proposes a system that builds data infrastructure autonomously,
resting on the claim that the analysis part can be done independently. That claim is
true of some analysis and false of the rest, and the distinction is not a detail: it
determines what the system may do unsupervised, what it must ask about, and what it must
never originate. See [020_critique.md](../00_concept/020_critique.md) §1.

Stakeholders will ask how much the system is allowed to do on its own, and a single
answer — a percentage, a trust level — is not defensible for any of the three.

## Options considered

*Uniform autonomy with a human approval gate on writes.* Simple to explain. Rejected:
it over-constrains structural work, which is self-verifying and should never need a
human, while under-constraining teleological work, where the gate is a rubber stamp
because the reviewer has no basis to disagree.

*Per-capability autonomy settings.* Finer-grained but arbitrary, and it attaches the
policy to the component rather than to the kind of claim, which is where the actual risk
lives.

*Tiering by kind of claim.* Adopted.

## Decision

Every claim the system makes is classified into one of three tiers, and the tier
determines the mandate:

**Structural** — computable from data and catalogue. Full autonomy, bounded only by
budget and access.

**Semantic** — meaning, identity, authority. Propose freely; assert only on declared
evidence thresholds or human adjudication. Provenance is permanent and distinguishes the
two routes.

**Teleological** — what is worth knowing. The system does not originate purpose. Every
artifact at this tier cites an entry in the decision register.

Thresholds at the semantic tier are set from measured precision against a held-out
adjudication set, not from judgement.

## Consequences

Job types, model routing, cost profile and review policy all follow from the tier, which
simplifies several otherwise arbitrary decisions. The decision register becomes a hard
dependency for anything at Tier 3, which means the project cannot produce useful
automated analysis in an organisation unwilling to maintain one. That is a real
limitation and should be stated to stakeholders rather than discovered by them.
