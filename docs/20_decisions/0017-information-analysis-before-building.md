# ADR-0017 — Information analysis precedes building: hard effort on a minimum, best effort on the rest, never a hard gate

- **Status:** Accepted
- **Date:** 2026-10-18
- **Supersedes:** —
- **Superseded by:** —
- **Amended by:** [ADR-0018](0018-information-analysis-record.md) (item 27's grain tests join the minimum);
  [ADR-0019](0019-information-analysis-in-two-rounds.md) (two rounds; item 28)

## Context

On 2026-10-18 the author proposed an information-analysis phase before anything is built on a table, naming
granularity, meaning, temporal characteristics and relation to other tables, and asked what else should be
inventoried. [129](../10_architecture/129_information-analysis.md) recorded his four items and 22 further items
proposed in reply, and put four questions to him (`ARC-OP-36`): which items stay; whether every table is analysed in
full before the first build or a minimum is required per table; whether the analysis is a gate; and whether the first
trial is the Wide World Importers sandbox. He ruled the same day, verbatim:

> 1. all of them stay.
> 2. I'd do a hard effort, no guessing, on the minimal ones, state uncertainties clearly, the rest is on best effort
> basis, also provide confidence level. Also provide reasoning for every item, and evidence where possible. It's
> never a hard gate.
> 3. Yes, as a proof of concept, definitely, good idea.
> 4. Definitely

## Options considered

*A full inventory of every table before the first build.* Its case: nothing is built on a misreading, and the
inventory is complete in one pass. Rejected because it delays every first result until the least important item of
the least important table is done, and because many items can only be answered as a build reaches them.

*A minimum dossier per table, as a blocking gate.* Its case: a build can never start on an unknown grain or an
unclassified personal-data column. Rejected because a gate that blocks on missing analysis invites guessing to open
it, which is exactly what the minimum is meant to prevent, and because an emergency must be able to proceed
([ADR-0016](0016-regulatory-requirements-from-production.md)).

*A minimum dossier done with hard effort and stated uncertainty, the rest best effort, never blocking.* Adopted.

## Decision

1. **All 26 items of 129 are inventoried.** Their numbers are stable; new items take new numbers.
2. **The minimum — items 1, 3, 5, 6, 7 and 19 (granularity, temporal characteristics, role, keys, population,
   sensitivity) — is done with hard effort and no guessing.** What cannot be established is recorded as an
   uncertainty, stated clearly, with what would settle it, not filled in with the likeliest answer.
3. **The other items are best effort.**
4. **Every item carries a confidence level and its reasoning, and evidence wherever evidence can be had.**
5. **The analysis is never a hard gate.** An incomplete or uncertain analysis does not stop a build; it travels with
   the build as a known uncertainty. The publication gate of
   [ADR-0011](0011-assertions-identity-plane-publication-gate.md), which governs what is published to users, is
   unchanged.
6. **The first trial is the Wide World Importers sandbox** (`EVI-OP-7`), as a proof of concept.

## Consequences

The builder of `ARC-OP-34` gets a defined input, and its uncertainties are visible rather than buried. The
confidence scale must be defined so that "high" means the same thing from every agent; a proposal is in
[`analysis/README.md`](../../analysis/README.md), with the record layout (`ARC-OP-36`, not yet ruled). Because the
analysis never blocks, nothing mechanical stops a build on a table whose minimum is uncertain; the quality gates of
`ARC-OP-33` are where such a build would be flagged. Revisit if builds on uncertain minimums turn out to produce
defects that a gate would have prevented.
