# ADR-0020 — While in the analysis stage, the analysis describes the as-is and does not look ahead

- **Status:** Accepted
- **Date:** 2026-10-18
- **Supersedes:** —
- **Superseded by:** —

## Context

The round-1 dossiers ([ADR-0017](0017-information-analysis-before-building.md) to
[ADR-0019](0019-information-analysis-in-two-rounds.md)) put questions to the author that belong to later stages:
whether "number of orders" counts rows or customer orders, which date orders are reported by, and what may be loaded
into the warehouse. Their claims also carried design advice (hubs, dimensions, "a build should"). The author answered
on 2026-10-18, verbatim:

> 1. I think we're getting ahead of ourselves. Defining KPI's is what we do in a later stage. Maybe we should make a
> ruling somewhere that as long as we are in the analysis stage, we do not look ahead yet. Although we should make a
> note somewhere in the peculiarities section that "orders" mean two things.
>
> 3. Same, we're not there yet. As for now, we are investigating the as-is situation.

## Options considered

*Let the analysis prepare later decisions as it goes.* Its case: questions surface while the facts are fresh. Rejected:
it mixes stages, invites guesses about designs not yet chosen, and puts decisions to the author before their time.

*Describe the as-is only.* Adopted.

## Decision

1. **While in the analysis stage, the analysis records what is**: what the data and the source declare, show and do,
   with the consequences of those facts stated as warnings where they matter (a column that double counts when summed,
   a word that means two things).
2. **It does not decide or propose** measures and KPIs, reporting dates, model designs (hubs, links, satellites,
   dimensions, facts), loading or exclusion. Questions of that kind are not put to a person during the analysis; facts
   that will bear on them are recorded as facts.
3. Questions already raised of that kind are retracted from the dossiers (status `retracted`) and remain in the git
   history; the facts behind them stay.

## Consequences

The dossiers become shorter and do not age when a design changes. Later stages must re-read them for the facts they
need; the warnings are where those facts are easiest to find. The convention is not enforced by
`tools/check_repo.py` (AGENTS.md rule 11): telling a statement of fact from advice is a judgement, and a word list would
both miss advice and flag facts. Revisit when the build stage begins.
