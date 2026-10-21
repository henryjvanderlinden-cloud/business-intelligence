# ADR-0016 — Regulatory requirements are kept in mind from the start and apply from production

- **Status:** Accepted
- **Date:** 2026-10-15
- **Supersedes:** —
- **Superseded by:** —

## Context

On 2026-10-15 the author instructed that the principles of BCBS 239 must be followed when working for a financial
institution. [152](../10_architecture/152_bcbs-239.md) lists the principles and what they would mean for the design.
Two of its consequences collide with existing rulings. [ADR-0012](0012-generic-framework-lean-start.md) says every
implementation starts lean, while BCBS 239 sets controls that a lean start would postpone (152, item 15). And the
publication gate of [ADR-0011](0011-assertions-identity-plane-publication-gate.md) can stop a risk report that the
principles require on time (152, item 16). BCBS 239 is also addressed to banks, while the instruction named financial
institutions in general. The author ruled on all three the same day, verbatim:

> connection is back. BCBS 239 only applies to banks, indeed, but it's inspiration for e.g. other credit institutions.
> I think 15 is not that far of a stretch. Let's say that regulatory requirements need to be kept in mind when starting
> lean, although compliance is not necessary when still in a proof of concept or pilot phase. Once a system is in
> production though, regulatory requirements apply. So best to keep those considerations in mind from the start. Item
> 16: as is customary, as we say in Dutch "nood breekt wet". If you make reference of this, keep it brief. It is
> obvious and distracting, although for an LLM it might be necessary to make it explicit ;-).

## Options considered

*Comply from the first implementation.* Its case: nothing has to be retrofitted, and no proof of concept can drift into
production without its controls. Rejected because it makes a proof of concept or a pilot as heavy as production and
contradicts the lean start of ADR-0012 for no gain while no real report depends on the system.

*Ignore regulation until production.* Its case: the leanest possible start. Rejected because controls that were not
designed in — lineage, reconciliation, an inventory of manual steps — are expensive to retrofit, and the gap is found
when it is most costly.

*Keep the requirements in mind from the start; require compliance from production.* Adopted.

## Decision

**Regulatory requirements apply once a system is in production.** A proof of concept or a pilot need not comply.

**They are kept in mind from the start.** A lean start does not postpone the design of the controls production will
need, only their operation, so that they can be switched on rather than retrofitted.

**BCBS 239 binds banks.** For a bank, its principles are followed in production; for another financial institution
they are a reference to design against, and the regime that applies to that institution is followed.

**Necessity overrides the publication gate.** In an emergency a report goes out despite a failed test — *nood breekt
wet* — with the failure stated and the release decided and recorded by a named person, never by an agent.

## Consequences

ADR-0012 stands, qualified: every implementation starts lean, above the design of what production will require.
ADR-0011 stands with a recorded emergency release. Which of the other consequences in 152 (items 8 to 14) are adopted is
still open in `ARC-OP-35`.

**A system is in production from the moment a real decision or report relies on its output.** Proposed by Claude Opus
5.5 and confirmed by the author on 2026-10-21 ("3: yes."). **Revisit** if that test proves too loose to apply, or if a
pilot is found to feed real reports before it is called production.
