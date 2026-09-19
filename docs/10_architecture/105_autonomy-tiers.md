# 105 — Autonomy tiers

The central reframing of the brief. Autonomy is not a property of the system; it is a
property of each *kind of claim* the system makes, and the three kinds differ by orders
of magnitude in how safely they can be left alone.

## Tier 1 — Structural

*Claims computable from the data and the catalogue.*

Types, formats, cardinality, nullity, distributions, candidate keys, functional
dependencies, value overlap, volatility, growth rate, partitioning behaviour.

**Mandate: full autonomy.** The system observes, computes and records without asking.
These claims are cheap to verify and cheap to recompute, so error is self-correcting.
The only constraints are budget and access, both enforced by the Access capability
rather than by a human in the loop.

**Failure mode:** cost, and noise in the catalogue. Both are bounded by budget and by
pruning.

## Tier 2 — Semantic

*Claims about meaning, identity and authority.*

What an entity is, whether two identifiers denote it, which source is authoritative,
what a code meant historically, which grain a measure is valid at.

**Mandate: propose freely, assert only on evidence or adjudication.** The system may
generate unlimited hypotheses — this is where its throughput advantage over a human
analyst is largest — but a hypothesis becomes an assertion only when either the evidence
crosses a declared threshold or a named human rules on it. Assertions never lose their
provenance, and an assertion made by evidence alone is distinguishable forever from one
made by a person.

**Failure mode:** confident error that propagates. A wrong business key produces a
structurally valid vault that encodes a false statement about the world, and because the
vault is non-destructive it is recoverable — which is the argument for the vault in the
first place. The second-order defence is that assertions carry falsifiers and
evaluation watches them.

## Tier 3 — Teleological

*Claims about what is worth knowing.*

Which questions matter, which insight is actionable, which mart is worth building, which
analysis deserves a human's attention.

**Mandate: human-anchored, machine-assisted.** The system does not originate purpose. It
works against an explicit decision register maintained by people, and every artifact it
proposes at this tier cites the decision it serves. An artifact that cannot cite one is
not built.

**Failure mode:** a system that is busy and irrelevant — statistically true observations
nobody acts on, and marts with no consumers. This is the most likely way the project
disappoints, and it is a design failure rather than a model failure.

## Why the tiering matters operationally

It gives a defensible answer to the question every stakeholder asks, which is "how much
is it allowed to do on its own?" The answer is not a number. It is: *it may measure
freely, it may guess out loud, and it may not decide what matters.*

It also determines model routing, cost and review. Tier 1 is high-volume, cheap, and
suits the smallest capable model. Tier 2 is low-volume, consequential, and justifies the
strongest available reasoning plus cross-model review. Tier 3 is a conversation.
