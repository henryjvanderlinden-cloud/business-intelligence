# ADR-0011 — Assertions are the core record; one identity plane over separate stores; a publication gate

- **Status:** Accepted
- **Date:** 2026-09-25
- **Supersedes:** —
- **Superseded by:** —

## Context

[120_context-layer.md](../10_architecture/120_context-layer.md) proposed a context layer of
*cards*, one per object, with assertions carried in each card's front matter, and — as
extended on 2026-09-25 — six kinds of context, a normative/descriptive split, and "one store,
two views" serving agents and people. A second external review on gpt-5.6-sol, recorded in
[XREV_2026-09-25_context-system-r2_sol](../30_research/notes/XREV_2026-09-25_context-system-r2_sol.md),
found that this conflated what a claim is with where it is stored and how it is shown: card kinds
mixed business objects with statements about them (`assertion`, `hypothesis`, `rule`,
`relationship` overlapped); the six kinds classified whole categories where attributes of each
claim decide trust and storage; and "one store" both contradicted the proposed physical
separation and would leak the existence of sensitive objects through a shared index. A parallel
review on GPT-6 Astra, recorded in
[XREV_2026-09-25_context-system-r2_astra](../30_research/notes/XREV_2026-09-25_context-system-r2_astra.md),
found that a failing join test had no consequence beyond housekeeping: marts stayed published
and `RELY` constraints kept licensing optimiser rewrites on a false assumption.

The author accepted these as design decisions on 2026-09-25: *"Agreed with the design decisions.
Publication gate also."*

## Options considered

*Cards as the unit of knowledge*, as 120 first proposed. Its case: one readable file per object
is simple, diffs well, and is what people and models both read. Rejected because a claim about a
pair of objects, a rule over a set, or a claim that changes status has no natural single card, and
parallel card kinds for the same statement duplicate and drift.

*Assertions as the unit, cards as views.* Adopted.

*One physical store for agent context and the human catalogue.* Its case: one investment, and the
catalogue stays current because agents depend on it. Rejected in its literal form because the two
need different retention, transaction and security guarantees, and a shared unfiltered index leaks.

*One identity plane over separate stores, with a publication pipeline.* Adopted; it keeps the
case for sharing without the leak.

*Detection without consequence.* Tests that report failures to gardening only. Rejected: detection
that does not stop publication leaves consumers exposed until a person notices.

## Decision

**Assertions are the canonical record.** Every claim the system holds is a typed assertion with
its own attributes: subject, claim type, lifecycle status, authority, evidence bundle, scope,
volatility, owner, retention class and privacy class. *Hypothesis*, *approved*, *contested* and
*retracted* are statuses of an assertion, not separate kinds of object. A relationship between
two objects and a rule over a set of objects are assertion types.

**Cards are views.** A card is a bounded, readable projection of the assertions about one stable
business object — a source, dataset, field, entity, metric or decision — generated for people and
for agents. It is not where knowledge is kept.

**Claim types distinguish five things** where 120 distinguished two: what is *intended*, what is
*declared*, what is *implemented*, what is *observed*, and what is *certified*, each with its own
effective time and observation time.

**One identity plane over separate stores.** All stores share one scheme of permanent identifiers.
The stores stay separate because their guarantees differ. Indexes are filtered by access policy
before anything is retrieved, and material reaches the human catalogue only through an explicit
publication pipeline. No unfiltered graph is shared.

**A publication gate.** A mart or other published artifact is released only when the tests on the
data version it was built from have passed. A failing test blocks publication and revokes the
optimisation assertions — `RELY` or `NOT ENFORCED` constraints — that depend on the failed claim,
before consumers see the result. Responsibility for remediation and re-approval is assigned.

## Consequences

120's card kinds are narrowed to business objects, with `procedure` retained for know-how; the
proposed `relationship` and `rule` card kinds become assertion types, which also answers the shape
`ARC-OP-16` asked for.

`ARC-OP-7`, files or graph or both, is **partly** answered: the logical model is decided. The
physical medium for assertions — git, a database, or both — is still open and still wants
deciding, since the audit-log argument for git in 120 now applies to assertions rather than cards.

The publication gate turns the standing tests of
[128_join-knowledge.md](../10_architecture/128_join-knowledge.md) and the checks of
[127_temporal-behaviour.md](../10_architecture/127_temporal-behaviour.md) from monitoring into
control, and it creates a new failure mode: a flaky or over-strict test now stops delivery. Test
quality becomes a production concern.

**Revisit** if generating cards as views proves too slow or too lossy for people to work with, or if
the publication gate blocks delivery more often than it prevents defects.
