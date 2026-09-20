# 002 — Mission statement

> **This is a living document.** It holds the current wording of the mission and nothing
> else. It is expected to change, and every change is recorded in the changelog at the
> bottom with what was cut and why. [001_mission.md](001_mission.md) holds the author's
> original formulation verbatim and the arguments against it; that document is the
> reasoning, this one is the wording.
>
> **Current version: 0.3, 2026-09-20. Unratified.** `CON-OP-15` holds the open question and
> closes in an ADR the author rules.

## The statement

> nsdn exists to extend how much of an organisation's data landscape can be reliably
> understood. Machines express and maintain human-specified deterministic designs more
> cheaply, and — separately — propose semantic interpretations for people to judge. People
> decide what matters; every accepted claim stays traceable to the evidence or the person
> behind it. Success is more of what people have prioritised, modelled and maintained, at a
> defect rate no worse than competent practice and without disproportionate validation
> cost. Whether those two capabilities interact, and whether human judgement is the binding
> constraint, are open.

## What it deliberately does not claim

**No order of magnitude.** Quality is bounded above and nothing is a hundred times more
correct than correct. The quantity with room to move is coverage, and no figure for it has
been computed — `CON-OP-2` is open.

**No single mechanism.** The two capabilities are stated separately because `CON-OP-8`
holds them to be independent theses and the first proposed interaction between them was
refuted. The statement says they are open rather than asserting either way.

**No autonomy.** *Installed under an explicit mandate* rather than let loose. The system
may measure freely, propose freely, and may not decide what matters
([ADR-0005](../20_decisions/0005-three-autonomy-tiers.md)).

**No technology.** A technology set is an output of the methodology and the architecture,
ratified separately and replaceable without touching this statement — which is
[ADR-0008](../20_decisions/0008-faculties-substrate-mandate.md)'s rule against naming a
thing after its implementation, applied one level up.

## The word doing the most work

**Prioritised.** The statement measures coverage *of what people have prioritised*, and
that qualifier is the whole defence against the metric rewarding legible abundance. Remove
it and a system maximises the measure by modelling thousands of easy, stable, low-value
tables under one coarse bulk approval, scoring well while diverting scarce experts from the
few consequential claims and enlarging the trusted surface.

The qualifier is also the statement's weakest point, and the objection is unanswered:
human priorities may be incomplete, political or unstable, so optimising against them may
relocate the value problem from the system to its governors rather than solving it. It also
makes the mission depend on the decision register that `ARC-OP-12` says may simply never be
supplied.

---

## Changelog

**0.3 — 2026-09-20.** Current. Produced by gpt-5.6-sol under adversarial review and
rewritten for cadence; recorded in
[XREV_2026-09-20_mission-statement_sol](../30_research/notes/XREV_2026-09-20_mission-statement_sol.md).

- **Cut: "not by removing the people who understand both the systems and the business, but
  by making their judgement reach very much further."** Rhetorically the best line in 0.2
  and refused on substance. Paired with *machines propose, people rule*, it recast
  authoring a known deterministic design as a proposal awaiting adjudication, which
  collapses specification labour into adjudication labour and makes the second thesis's
  governance pattern universal. That is the unification `CON-OP-8` refused, arriving
  through the governance clause instead of through a causal claim.
- **Cut: "coverage gained per unit of human adjudication" as the success measure.**
  Gameable: coverage was not value-weighted and a unit of adjudication was undefined, so
  the ratio is maximised by bulk-approving large quantities of easy low-value modelling.
  Replaced by coverage *of what people have prioritised*, which moves the weighting to
  people — necessarily, since ADR-0005 forbids the system from deciding consequence.
- **Added: an explicit statement that the interaction and the bottleneck are open.** 0.2
  asserted the adjudication bottleneck as established. It is not.

**0.2 — 2026-09-20.** Drafted by Claude Opus 5 from the session's findings. Reframed the
binding constraint from development speed to adjudication capacity. Failed review on both
counts above; retained here because the reframing may still be right and only its assertion
was premature.

**0.1 — 2026-09-20.** The author's formulation, verbatim in
[001_mission.md](001_mission.md).

- **Cut: "by orders of magnitude", applied to quality.** Two claims of different kinds;
  only the coverage reading survives.
- **Changed: "let loose on" to "installed under an explicit mandate".** The original names
  the failure mode [ADR-0005](../20_decisions/0005-three-autonomy-tiers.md) and
  [150_trust-and-blast-radius.md](../10_architecture/150_trust-and-blast-radius.md) exist
  to prevent, and would be read literally by the governance function whose objection
  matters most.
- **Demoted: "a set of technologies" from a deliverable to an output.** Bundling it dates
  the mission.
- **Retained without change: "for that we need a solid conceptual foundation."** It is the
  sentence that makes the rest legitimate and it is the project's actual discipline.
