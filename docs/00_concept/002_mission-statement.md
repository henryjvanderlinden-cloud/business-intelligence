# 002 — Mission statement

> **This is a living document.** It holds the current wording of the mission and nothing
> else. Every change is recorded in the changelog at the bottom with what was cut and why.
> [001_mission.md](001_mission.md) holds the author's original formulation verbatim and the
> arguments against it; that document is the reasoning, this one is the wording.
>
> **Current version: 0.6, 2026-09-20. Unratified.** `CON-OP-15` holds the open question and
> closes in an ADR the author rules.

## The statement

> nsdn builds modelled, meaningful and trustworthy data landscapes at far lower cost and
> higher quality than current practice, where quality includes coverage of the scope people
> have prioritised. Its methodology is derived from the demonstrated strengths and limits of
> deterministic machinery, contextual inference and human judgement, rather than applying
> models wherever they appear useful. Its practical test is whether ordinary teams can
> implement and maintain otherwise-appropriate designs, including Data Vault, whose total
> lifecycle burden currently exceeds their time, budget and validation capacity — without
> higher defect rates, and without displacing the burden elsewhere in the lifecycle. People
> decide what matters and rule on meaning; every accepted claim remains traceable to
> evidence or to the responsible person.

## What is not established

**The interaction between deterministic machinery and contextual inference, and whether
human adjudication is the binding constraint, are not yet established.** The statement is
written to be true whichever way both resolve. `CON-OP-8` holds the first and records that
the only interaction candidate so far was refuted; the second was asserted in version 0.2
and withdrawn.

**The strengths and limits the methodology is "derived from" are currently hypotheses, not
demonstrations.** [060_faculty-inventory.md](060_faculty-inventory.md) states them and says
so; no cell in it has been measured on this project's data. The word *demonstrated* in the
statement is therefore a standard the methodology must meet, not a claim that it has been
met.

**No figure exists for cost or coverage.** `CON-OP-2` is open.

## The phrase doing the most work

**"Total lifecycle burden … without displacing the burden elsewhere."** The second half is
the guard and is the harder of the two to satisfy. Displaced cost is the characteristic way
this claim would be won dishonestly: generation becomes cheap, the saving is announced, and
the work reappears as query authoring, tuning, operational toil or review load that nobody
counted. The test is only as good as the accounting behind it, and no such accounting
exists yet — `CON-OP-2`.

**Two things do not reduce to labour, and the statement does not pretend they do.**

*Runtime and compute cost* are not effort, though they draw on the same budget. Cheap
columnar execution and join elimination have weakened the historical objection to designs
like Anchor without abolishing it: whether it binds depends on workload, physical design
and whether joins can in fact be eliminated. Runtime feasibility is therefore an empirical
condition on each design rather than a settled reason to reject one.

*Adjudication capacity* is labour, but it is scarce, specialised and non-fungible, so
calling it labour does not mean an organisation can buy more of it. A representation that
stops a qualified person from reliably judging a claim fails the mandate of
[ADR-0005](../20_decisions/0005-three-autonomy-tiers.md) as a quality problem and not
merely as an expense. That is not a verdict against complex physical models: tooling can
present a comprehensible semantic view over one. It means the thing to assess is the
**adjudication surface**, not the object count — which is `ARC-OP-15`, and is now a
sharper instruction than that row previously carried.

---

## Changelog

**0.6 — 2026-09-20.** Current. From the author's rejection of 0.5's key phrase, put back to
gpt-5.6-sol, which conceded its own earlier finding —
[XREV_2026-09-20_mission-statement_sol](../30_research/notes/XREV_2026-09-20_mission-statement_sol.md)
third sitting.

- **Changed: "whose principal obstacle is modelling labour" to "whose total lifecycle
  burden currently exceeds their time, budget and validation capacity."** The author's
  argument: cognitive complexity is a subset of modelling labour rather than a separate
  obstacle class; 6NF does not avoid labour but relocates it into query authoring and
  performance optimisation; and practitioners are perfectly capable of these designs — what
  defeats them is the organisation's calendar and budget, not their capacity. The reviewer
  conceded, on the ground that authoring, comprehension, querying and optimisation are
  better understood as *locations where lifecycle work accumulates* than as distinct
  obstacle classes, and that naming only the first "modelling labour" arbitrarily privileges
  where the work happens. The word *currently* is load-bearing: the burden is historical,
  not intrinsic to the design.
- **Added: "without displacing the burden elsewhere in the lifecycle."** This is the half of
  the reviewer's original finding that survives its own concession — a warning against
  claiming success because model generation became cheap, while the work reappears
  downstream uncounted.
- **Consequence for `ARC-OP-14`.** The canon survey should classify designs by *where their
  lifecycle work accumulates*, not by whether they were rejected as "too laborious", which
  was the distinction this change dissolved.

**0.5 — 2026-09-20.** Current. Produced by gpt-5.6-sol under adversarial review of 0.4,
recorded in
[XREV_2026-09-20_mission-statement_sol](../30_research/notes/XREV_2026-09-20_mission-statement_sol.md)
second sitting. One cadence change only — *It builds a methodology around* became *Its
methodology is derived from*, to avoid repeating the verb. No substantive change.

**0.4 — 2026-09-20.** Drafted by Claude Opus 5 from the author's rejection of 0.3. Adopted
the author's corrections: the objective is to **build** a landscape rather than to
understand one, coverage is an aspect of quality rather than a separate measure, the
methodology is derived from capability analysis rather than from applying models where they
look interesting, and Data Vault is named to make the claim concrete. Failed review on two
of three counts.

- **Repaired: coverage was unqualified.** Folding coverage into quality is coherent only if
  quality means quality of the landscape as a portfolio, and then coverage must still be
  coverage of a human-prioritised scope. *People set priorities* assigns authority but does
  not constrain the measure, so 0.4 reopened the legible-abundance gaming that 0.3's
  qualifier existed to prevent. Restored as *coverage of the scope people have prioritised*.
- **Repaired: the attainability test was too broad.** *Designs the canon rejected as too
  laborious become ordinary* is defeated by the 6NF finding, because laboriousness was one
  of several reasons for non-adoption and cheap authorship addresses only that one.
  *Become ordinary* also confounds technical attainability with adoption, training and
  fashion. Narrowed to designs *whose principal obstacle is modelling labour*, tested by
  whether ordinary teams can implement and maintain them without higher defect rates or
  disproportionate validation cost.
- **Upheld: moving the open hypotheses out of the statement.** Legitimate on condition that
  the adjacent section states them plainly, which it now does. Without that, *derived from
  what each does well and badly* would read as though the decomposition were already
  established.

**0.3 — 2026-09-20.** Rejected by the author for making the objective *understanding* the
landscape, which he named as drift into an academic exercise. The rejection is upheld and
the drift was real: 0.3 made the output knowledge, when the output is a built environment.
It was a consequence of drafting toward what was defensible rather than toward what is
true.

**0.2 — 2026-09-20.** Drafted by Claude Opus 5. Reframed the binding constraint from
development speed to adjudication capacity.

- **Cut: "not by removing the people who understand both the systems and the business, but
  by making their judgement reach very much further."** Paired with *machines propose,
  people rule*, it recast authoring a known deterministic design as a proposal awaiting
  adjudication, collapsing specification labour into adjudication labour and making the
  second thesis's governance pattern universal — the unification `CON-OP-8` refused,
  arriving through a clause written for cadence.
- **Cut: "coverage gained per unit of human adjudication."** Gameable: maximised by
  bulk-approving large quantities of easy low-value modelling.

**0.1 — 2026-09-20.** The author's formulation, verbatim in [001_mission.md](001_mission.md).

- **Cut: "by orders of magnitude", applied to quality.**
- **Changed: "let loose on" to "installed under an explicit mandate".**
- **Demoted: "a set of technologies" from a deliverable to an output.**
- **Retained without change: "for that we need a solid conceptual foundation."**
