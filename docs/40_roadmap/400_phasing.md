# 400 — Phasing

The characteristic failure of projects of this shape is to build the ontology first and
discover, two years later, that nothing consumes it. The phasing below is arranged so
that each phase is independently useful, independently abandonable, and cheap to obtain
permission for relative to the one after it.

## Phase 0 — Consolidate the thinking *(current)*

Assemble the concept, the critique, the architecture and the open questions; complete
the prior-art register far enough to know what is genuinely new; and survey candidate
public datasets against the three conditions in
[410_first-vertical-slice.md](410_first-vertical-slice.md) §Environment. Ends when the
claimed gap in [050_prior-art.md](../00_concept/050_prior-art.md) has been tested
against reality.

This is Mode 1 of [ADR-0006](../20_decisions/0006-project-mode.md) and is deliberately
unhurried.

*Cost: reading and writing. Risk: that it continues indefinitely. The gate into Phase 1
is a decision taken on a date, not a condition that ripens on its own.*

*Status 2026-11-15, session 12.* The gate has not been decided, but the work has run ahead of it in the Wide World
Importers sandbox: parts of Phase 1 (the analysis record, without an adjudication queue) and of Phase 2 (the raw vault,
generated and loaded daily) exist there, while the falsifiable core above is untested, since one clean source cannot
test it. Whether to take the gate, and on what condition, is the author's decision.

*Status 2026-11-17, session 13.* One thin slice of Phase 3 now exists in the sandbox as well: a generated business
vault, one mart and one analysis answering one question, which cites the first entry of a decision register
(`DEC-0001`), as Phase 3 below requires. The gate is still undecided.

## Phase 1 — The read-only half

Access contracts, discovery, profiling, card generation, hypothesis generation, the
adjudication queue. Writes nothing anywhere except its own repository.

This phase is the whole project's hinge. It is independently valuable — an organisation
with a good context layer and nothing else is already better off — it is by far the
easiest thing to get authorised, because it cannot break anything, and it de-risks
everything downstream, since the quality of every later phase is bounded by the quality
of the context layer.

It is also the phase that tests the falsifiable core: **can business keys and entity
identity be substantially machine-proposed, at a precision that makes adjudication
worthwhile?** If the answer is no, the project reduces to a documentation tool and
should be re-scoped rather than continued.

## Phase 2 — Capture and the raw vault

Historisation assessment, capture jobs, hub/link/satellite generation from adjudicated
keys, quality expectations generated from profiles. Mechanical given Phase 1, which is
the point: if Phase 1 succeeded, this phase is largely templating.

*First writes. Blast radius per
[150_trust-and-blast-radius.md](../10_architecture/150_trust-and-blast-radius.md).*

## Phase 3 — Marts, analysis and narrative

Requires a decision register to exist. Without one, this phase produces statistically
true irrelevance, and it is better to delay it than to demonstrate that failure.

## Phase 4 — Pruning and self-assessment

In principle pruning should arrive with Phase 2, since that is when artifacts start
accumulating. In practice it will be deferred, so it is named as a phase to make the
deferral visible rather than accidental. Includes the held-out adjudication set and the
cost-per-artifact accounting that make autonomy calibration possible.

## Phase 5 — Enrichment

External and open data, acquired data, data that should be generated but is not yet
collected. Deliberately last: it is the most enjoyable to think about and the least
valuable without everything preceding it.

## Not on the roadmap

A decision-making unit. See [020_critique.md](../00_concept/020_critique.md) §2.
