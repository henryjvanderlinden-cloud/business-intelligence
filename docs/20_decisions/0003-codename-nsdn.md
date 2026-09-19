# ADR-0003 — Internal codename `nsdn`; the metaphor stays private

- **Status:** Accepted
- **Date:** 2026-09-19

## Context

The working title is *neural synaptic data network*, described by its author as "a bunch
of fancy words I threw together to evoke a kind of feeling." It needs a short handle for
directories, packages and document headers, and the project needs a position on how far
the biological metaphor should travel.

The metaphor is genuinely productive in places — the dendritic image of cheap local
hypotheses reinforced by use is apt, and synaptic pruning supplies a component the
original brief was missing (see
[145_entropy-and-pruning.md](../10_architecture/145_entropy-and-pruning.md)). It also
misleads: organisms carry no accountability requirement, and much of what makes
corporate data infrastructure usable is bureaucratic — provenance, authorisation,
attribution, reversibility. A design led by the metaphor will underweight exactly that.

There is a second, blunter problem: "neural" will be read as "neural network" by every
technical reader, and the system is not one.

## Options considered

*Adopt the full title externally.* Evocative and memorable. Rejected on the
misidentification risk and because a system explained by analogy invites scrutiny of the
analogy rather than of the design.

*Abandon the metaphor entirely.* Rejected: it has already generated at least one real
architectural component, and it is a useful private heuristic for generating others.

*Neutral short handle, metaphor retained as a heuristic.* Adopted.

## Decision

`nsdn` is the internal handle used for directories, packages, identifiers and document
headers. The full working title is recorded in
[010_vision.md](../00_concept/010_vision.md) and may be used in informal contexts. The
biological analogy is used as a generative heuristic, not as an explanatory frame in any
document intended for an outside reader. A public name, if one is ever needed, is a
later decision.

## Consequences

Documents must explain mechanisms in their own terms rather than by analogy, which is
more work and better writing. Revisit if the project ever needs an external identity.
