# ADR-0009 — Separate capabilities, an open list of value areas, and no interaction owed

- **Status:** Accepted
- **Date:** 2026-09-21
- **Supersedes:** —
- **Superseded by:** —

## Context

`CON-OP-8` asked whether the canon-cost argument should replace statability as the
manifesto's spine. By 2026-09-20 it had a disposition: no single spine, but two independent
theses — cheap machine authorship of known deterministic designs, and cheap proposal of
locally situated semantic hypotheses — plus an obligation, set by external review, that the
§III rewrite either argue an interaction between them or state its absence. Two interaction
candidates were drafted to meet that obligation. Both were refuted, the second in session 04.

On 2026-09-21 the author reviewed the session 04 findings in plain terms, with the two
theses restated as **Claim A**, the machine builds the known plumbing cheaply, and **Claim
B**, the machine proposes meaning — keys, identity, metadata — for a person to sign off. He
ruled on two things. His words, verbatim:

> Right, and this work is about both Claim A and Claim B. Both have tremendous value. It's
> good to separate the two capabilities. They are both excellent use cases for LLMs. There
> may be more, like monitoring, troubleshooting and regression testing, a test framework.
> [...] I also see options for continuous improvement on methodology and meta data. So
> yeah, let's separate the two, leave room for more value areas (or whatever we want to
> call them).

> Everything is connected, and everything is a trade-off. I don't know what point you were
> trying to prove. We're not writing an academic paper here. If there is a link, and it is
> relevant, sure then mention it. Otherwise no need.

The elision is his naming proposal for the second faculty, which belongs to `CON-OP-10` and
is recorded there.

## Options considered

*One spine.* Either capability as the single causal story, the other subordinate. Its case:
one mechanism is easier to state and defend. Rejected in session 03 by external review and
not reopened here, because each version either drops or misdescribes one of the two.

*Two theses, with an interaction owed.* The 2026-09-20 disposition. Its case: two claims
side by side read as a list rather than an argument, and showing how they bear on each other
would be stronger. Rejected by the author on the ground that the obligation belongs to a
genre this manifesto is not, and it had twice produced drafted links that did not survive
review.

*Separate capabilities, open list.* Adopted.

## Decision

**The manifesto presents what the system does as separate capabilities, each with its own
value and its own evidence**, starting with two: building known designs cheaply, and
proposing meaning for people to rule on.

**The list is open.** Further value areas the author names as candidates: monitoring;
troubleshooting; regression testing and a test framework; and continuous improvement of the
methodology and of the metadata. *Value area* is a working term, not a ruled one.

**No interaction is owed.** A link between capabilities is mentioned where it exists and
matters to the reader. The manifesto does not have to establish one, and the absence of one
is not a weakness it must confess.

## Consequences

`CON-OP-8` is ruled. The §III rewrite is still owed, and it is simpler: it states
capabilities and their evidence rather than defending a thesis, and it needs no interaction
section.

Each capability still has to be evidenced on its own terms, and they will not be evidenced
at the same rate — building through the canon survey (`ARC-OP-14`), meaning through the
falsifiable core (`EVI-OP-1`). An open list makes this more pressing rather than less:
naming a value area is not evidencing it.

The mandates of [ADR-0005](0005-three-autonomy-tiers.md) apply per capability. Monitoring,
troubleshooting and testing are new kinds of work for the second faculty and, like the design
claims in `ARC-OP-19`, may not fit the existing tiers.

`CON-OP-15`'s question *one claim or two* is answered for the capabilities. What success
means for each is still open.

**Revisit** if the capabilities cannot be kept apart in practice — if evidencing one turns
out to need the other's output, as the Data Vault finding in
[2026-09-20-canon-survey](../30_research/notes/2026-09-20-canon-survey.md) suggests it may —
or if the list grows until it no longer says what the system is for.
