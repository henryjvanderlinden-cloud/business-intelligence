# ADR-0006 — Project mode: argument first, then proof of concept on public data, then offering

- **Status:** Accepted
- **Date:** 2026-09-19

## Context

[Open question 1](../00_concept/040_open-questions.md) asked whether this project is a
product, an internal capability, or a written argument, and noted that the repository
was hedging. The author has now settled it, and the answer is *sequentially all three*,
which is a different thing from hedging and needs recording as such.

The motivating situation, in the author's terms: he is an independent contractor with
twenty-six years in business intelligence, and judges that language-model capability
will substantially change what human beings are paid to contribute in this field. The
project is a deliberate attempt to be early rather than late. That is a strategic
premise, not merely a technical interest, and it has consequences for how the work
should be sequenced and what counts as progress.

## Decision

The project proceeds in three modes, in order, with an explicit gate between each.

**Mode 1 — Intellectual test.** Establish whether the ideas hold water. Unhurried. The
output is argument: a coherent position on which parts of data-environment construction
are machine-tractable, which are not, and why. Success is that the argument survives
adversarial examination — including examination by models other than the one that helped
write it. The gate is the falsifiable core identified in
[410_first-vertical-slice.md](../40_roadmap/410_first-vertical-slice.md): if business
keys and cross-source entity identity cannot be machine-proposed at adjudication-worthy
precision, the argument fails and the project is re-scoped rather than continued.

**Mode 2 — Proof of concept and pilot.** Once the argument holds, move quickly. Public
practice datasets first, because they remove the access problem entirely and carry no
commercial risk; then pilots against real landscapes. Speed is the priority here and
elegance is not.

**Mode 3 — Offering or product.** Packaging follows demonstrated capability, not the
reverse.

The working method across all three: the author supplies intuitions, domain judgment and
the thing no model has — twenty-six years of observing how these projects actually fail;
the model supplies structure, prior art, and adversarial pressure. Neither role is
decorative, and conflating them would waste both.

## Consequences

Mode 1 has no deadline, which is a risk rather than a liberty — see the Phase 0 note in
[400_phasing.md](../40_roadmap/400_phasing.md) that it may continue indefinitely. The
gate between Mode 1 and Mode 2 should therefore be stated as a decision the author makes
on a date, not as a condition that ripens on its own.

Public practice data becomes a first-class concern rather than a convenience, which
raises its own question about ground truth; see
[410_first-vertical-slice.md](../40_roadmap/410_first-vertical-slice.md) §Environment.

Because Mode 3 is in view from the start, artifacts produced in Modes 1 and 2 should be
written as if someone else will read them. This repository is the record of the thinking
and may become the substance of the offering; that is a reason for the prose discipline
in [`../../AGENTS.md`](../../AGENTS.md) rather than a reason to formalise prematurely.
