# 001 — Mission

What this project is for, why the statement is not yet ratified, and which parts of it
are load-bearing claims rather than framing.

## The author's formulation, verbatim

Stated 2026-09-20, session 03, and recorded before it is interpreted:

> The end game is to come up with a methodology, a conceptual architecture and a set of
> technologies that can be let loose on an organizations data environment that will
> increase development speed and quality by orders of magnitude. For that we need a solid
> conceptual foundation.

The author attached a warning to it in the same breath — that he was "operating on vibes"
and partly distracted, and that it should not be taken at face value. This document takes
that instruction seriously. What follows expands the formulation and then argues with four
parts of it.

## What the formulation gets right, and it is the important part

**The ordering is correct and is the project's actual discipline.** *For that we need a
solid conceptual foundation* is the sentence that makes the rest legitimate, and it is why
[ADR-0006](../20_decisions/0006-project-mode.md) sequences argument before proof of concept
before offering. A project of this shape usually inverts that, builds the stack first and
writes the principle afterwards to justify it, and
[ARC-OP-20](../../registers/OPEN_POINTS.md) records that this repository has not yet
ratified its own principles and is therefore currently running on preferences.

**The unit of ambition is the environment, not the task.** Most tooling in this discipline
accelerates a task — write this transform, document this table. The formulation is about
the environment as a whole, which is the claim that makes the architecture necessary rather
than optional, because environment-level work is where the semantics, the identity
resolution and the adjudication burden all live.

## Four things in it that are not yet true

### 1 — "Orders of magnitude" is two claims, and only one of them is coherent as stated

*Speed* and *quality* do not scale alike, and asserting a hundredfold improvement in both
is not one ambition but two of different kinds.

Speed admits the claim straightforwardly: throughput of modelling, mapping and
documentation work is currently bounded by a scarce human, and
[060_faculty-inventory.md](060_faculty-inventory.md) dimension 2 is where the gap lives.

Quality does not, because quality is bounded above. Nothing can be a hundred times more
correct than correct. The claim only becomes coherent when *quality* is replaced by a
quantity with room to move, and there are two candidates, of which the second is much
stronger:

- **Defect density** — a hundredfold reduction in wrong joins, wrong grain, silently stale
  logic. Meaningful, and measurable against the ground truth `EVI-OP-1` owes.
- **Coverage** — the share of the landscape that is modelled at all. An organisation models
  a small fraction of what it holds because modelling is expensive; if the cost collapses,
  the fraction is what moves, and it moves by orders of magnitude without any single
  artifact being better than a good human's work. On this reading the quality claim is a
  coverage claim wearing a quality costume, and it is the most defensible version of the
  mission available.

`CON-OP-2` records that none of this has a number. `CON-OP-15` records that the success
criterion itself is unratified.

### 2 — "Let loose" is the thing the architecture exists to refuse

The phrase is in direct tension with three settled positions.
[ADR-0005](../20_decisions/0005-three-autonomy-tiers.md) holds that autonomy is a property
of each kind of claim rather than of the system, and that the system may measure freely,
guess out loud, and not decide what matters.
[ADR-0004](../20_decisions/0004-models-out-of-the-data-path.md) keeps models out of the
data path entirely. [150_trust-and-blast-radius.md](../10_architecture/150_trust-and-blast-radius.md)
holds that authorisation is a component rather than a prerequisite, and that active
discovery without written authorisation is a security incident regardless of intent.

Read literally, *let loose on an organisation's data environment* names the failure mode
the whole mandate structure was built to prevent. Read charitably it means *installed and
running without needing a human in every loop*, which is compatible with everything above.

The distinction is not pedantry, because the phrase will be read literally by exactly the
audience whose objection matters most — the security and governance function that
[150](../10_architecture/150_trust-and-blast-radius.md) says is where projects of this
shape die. The mission should therefore be stated as **installed into an organisation's
data environment under an explicit mandate**, which loses nothing the author meant and
concedes nothing he did not.

### 3 — Three deliverables with three different lifetimes should not be bundled

A methodology, a conceptual architecture and a set of technologies decay at very different
rates. [ADR-0008](../20_decisions/0008-faculties-substrate-mandate.md) forbids naming a
faculty after its implementation for precisely this reason: a vocabulary tied to current
tooling dates the argument and reduces it to a claim about a technology.

The same logic applies one level up. If the mission owns a technology set, the mission
dates. The durable form is that the mission owns the **methodology** and the **conceptual
architecture**, and that the technology set is an *output* of them, ratified separately and
replaceable without touching the mission — which is what `ARC-OP-20` already describes when
it separates the constitution from the instance design made under it.

### 4 — The formulation quietly asserts the conjunction that `CON-OP-8` just separated

This is the sharpest observation available about the sentence, and it is a finding rather
than a criticism.

`CON-OP-8` now holds that the manifesto carries **two independent theses**: that machine
authorship lowers the cost of expressing and maintaining known deterministic designs, and
that contextual inference makes locally situated semantic hypotheses cheap enough to
propose. External review found no interaction between them, refuted the first candidate
interaction on 2026-09-20, and left the §III rewrite owing either an argument or an
admission.

*Development speed and quality* is, read against those theses, exactly their conjunction:
speed is the first thesis and quality — as coverage or defect density — is the second. The
author's formulation therefore assumes the two go together, which is why the two-thesis
reading feels like a loss rather than a clarification.

**That is evidence about the author's intuition and not evidence about the world.** It does
not discharge `CON-OP-8`'s obligation and must not be treated as doing so. What it does
supply is a reason to look hard for the interaction before conceding there is none: the
person who has spent twenty-six years in this discipline expects the halves to be one
thing, and that expectation is worth taking as a hypothesis with a known provenance rather
than as a conclusion.

## The mission as this document would state it

Offered as a candidate, unratified, and narrower than the author's version in three places
and wider in none:

> To establish a methodology and a conceptual architecture — and, as their output, an
> admissible technology set — that can be installed into an organisation's data
> environment under an explicit mandate, and that raise the throughput and the coverage of
> data-environment development by an order of magnitude or more, at a defect rate no worse
> than competent human practice, with every claim the system makes traceable to the
> evidence or the person that warrants it.

The differences from the author's formulation are deliberate: *installed under an explicit
mandate* rather than *let loose*; *throughput and coverage* rather than *speed and
quality*; the technology set demoted to an output; and a defect-rate floor added, because a
speed claim without one is the ordinary way this discipline produces fast rubbish.

## What is unratified

This document decides nothing. The mission above is a candidate formulation written by a
model from a prompt the author explicitly flagged as unconsidered, at the close of a
session in which two other syntheses by the same model were refuted by external review.
Its provenance is the weakest in the repository.

`CON-OP-15` holds the open question: what the success criterion is, whether it is one claim
or two, and against what it would be measured. It closes in an ADR or not at all, and per
[`../../AGENTS.md`](../../AGENTS.md) rule 3 the ratification is the author's, not the
model's.
