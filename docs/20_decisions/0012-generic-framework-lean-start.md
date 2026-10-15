# ADR-0012 — A generic framework; every implementation starts lean

- **Status:** Accepted
- **Date:** 2026-09-25
- **Supersedes:** —
- **Superseded by:** —
- **Qualified by:** [ADR-0016](0016-regulatory-requirements-from-production.md) (2026-10-15): regulatory requirements are kept in mind from the start and apply from production

## Context

External review of [155_adjudication-economy.md](../10_architecture/155_adjudication-economy.md) on
2026-09-25 split along a familiar line. One reviewer asked for more rigour — numeric estimates,
clustered statistics, independent confirmation of audits; the other argued that a real
organisation lacks the traceability that rigour depends on, and that the design should start lean.
Settling that disagreement document by document would recur in every part of the design. The author
settled it once, and gave the background that explains why. His words, verbatim:

> Checks: blinded form and exclude. They point to something valid. A lean start is about
> implementation. Every implementation must start lean. A bit of background. I don't have a
> specific environment in mind for this methodology. I just want it to be a generic framework. I do
> however want to test it, first couple of times with a sandbox environment with open source data.
> We're developing the framework first and foremost. I am convinced that the agentic layer can
> provide real value in BI implementations.

The first sentence is a ruling on seeded checks in 155 and is recorded there.

## Options considered

*Design for a first implementation.* Its case: a concrete target keeps documents honest and
buildable. Rejected because it would tailor a generic framework to whichever environment came first,
and drop every part a first implementation cannot yet support.

*Design the full framework, with no guidance on how to begin.* Its case: completeness. Rejected
because a framework that must be implemented whole will either not be implemented or be implemented
as precise-looking nonsense, as the review showed for monitoring that assumes traceability nobody has
yet.

*Design the full framework, and state how an implementation grows into it.* Adopted.

## Decision

**The framework is generic.** It is written for no particular organisation, platform or technology
stack. Where a document needs an example it uses one, and says it is an example.

**Framework documents describe the full design.** They do not drop a part because a first
implementation could not support it.

**Every implementation starts lean.** Where it matters, a framework document states how an
implementation grows into it: in stages, each stage adopted only once the prerequisites it depends on
have been shown to work. [155](../10_architecture/155_adjudication-economy.md) is the first document
written this way.

**The framework is developed first.** Testing it comes next, the first few times in a sandbox built
on open data — consistent with [ADR-0006](0006-project-mode.md) and with the candidate dataset survey
`EVI-OP-2`.

**The author's conviction is the project's premise, not its evidence.** The author is convinced the
agentic layer can provide real value in BI implementations. That is why the project exists; it is not
a finding, and the claims that would show it — the success criterion `CON-OP-15`, the economics
`CON-OP-2`, the falsifiable core `EVI-OP-1` — remain open and are to be tested, not assumed.

## Consequences

Documents already written for a particular setting should be read as examples of the framework, not
as its definition.

A sandbox on open data has no real business owners, stewards or reviewers. Anything in the framework
that depends on people — adjudication, decision owners and deadlines, adoption, commitment — will be
exercised with the author or others playing those roles, and the results must say so. What a sandbox
cannot test is itself worth recording, so that it is not mistaken for something that was tested.

**Revisit** if a staged start proves impossible for some part of the framework, or if the framework
turns out to fit only one kind of environment.
