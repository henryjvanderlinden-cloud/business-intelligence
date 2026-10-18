# ADR-0019 — Information analysis in two rounds: each table first, then what lies between tables

- **Status:** Accepted
- **Date:** 2026-10-18
- **Supersedes:** —
- **Superseded by:** —
- **Amends:** [ADR-0017](0017-information-analysis-before-building.md) and
  [ADR-0018](0018-information-analysis-record.md) (scope of the minimum; item 28)

## Context

Sol's review of [129](../10_architecture/129_information-analysis.md)
([XREV](../30_research/notes/XREV_2026-10-18_information-analysis-inventory-gaps_sol.md)) showed that two tables can
pass every per-table test and still be joined wrongly, and proposed a minimum per join (R14), a check of what the
extracting account can see (R15) and a new item on arithmetic policy (R16). The author answered on 2026-10-18,
verbatim:

> Well, let's scope this correctly. My initial request was to do an information analysis on a per-table basis. So
> table "transcending" analyses were not yet part of the brief. It does raise a valid point though. A second round of
> analyses should uncover cross-table relations. Maybe they should get their own folder structure, and similar
> analyses. How do the tables relate to each other, if at all, and which peculiarities are there that deserve a
> warning? What is the meaning of this assumed (or proven) join? This includes point R14 you raised. R15 you'd have
> to explain to me. R16 is relevant, though minor, so I agree with your proposal.

## Options considered

*One round covering tables and their relations together.* Its case: a join's meaning is found while the tables are
fresh in mind. Rejected by the author's scoping: the brief was per table, and a relation is best analysed once both
its tables are understood.

*Two rounds.* Adopted.

## Decision

1. **Round 1 is per table and per column.** It covers the items of 129 that are about one table: 1 to 3, 5 to 23, 27
   and 28. A table's declared foreign keys are recorded under item 6 (keys) as facts about that table.
2. **Round 2 is across tables.** It covers how tables relate, if at all; which cross-table peculiarities deserve a
   warning; and what an assumed or proven join means. It takes item 4 (relations), the cross-table part of item 16
   (reconciliation), and items 24 to 26 (processes, terms, entities). R14 — that a join needs the meaning of its key
   columns and its own analysis before a build relies on it — belongs to round 2.
3. **Item 28, arithmetic policy**, is added, best effort: precision, rounding mode, where rounding happens (line or
   document) and how residues are treated.
4. **Not decided here:** round 2's folder structure (proposed in [`analysis/README.md`](../../analysis/README.md)
   section 9, not ruled), and R15, which the author asked to have explained first (`ARC-OP-36`).

## Consequences

Round 1 can be finished table by table and in parallel, with no table waiting for another. A build that joins tables
before round 2 has analysed the join does so on an unanalysed relation, which ADR-0017 permits (never a hard gate) but
which must be visible as an uncertainty. Revisit if round 1 turns out to need cross-table facts it cannot do without.
