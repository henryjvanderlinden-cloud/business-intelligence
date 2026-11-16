# ADR-0040 — The first slice is built as designed in note 141: unplaced lines stay visible, "as known on" is a replay, and the decision register is one file per decision

- **Status:** Accepted
- **Date:** 2026-11-15
- **Supersedes:** —
- **Superseded by:** —

## Context

[141](../10_architecture/141_the-first-slice-business-vault-and-mart.md) designs the slice ruled in
[ADR-0039](0039-first-use-case-and-where-marts-read-from.md). It was reviewed on sol, which failed the first version on
five points, all applied ([XREV](../30_research/notes/XREV_2026-11-15_141-first-slice_sol.md)). The model reported the
five findings and put to the author the three design choices he had not seen, numbered 8 to 10. He ruled on
2026-11-15 at 22:14, verbatim:

> 8: agree, it's a dq issue and needs to be visible.
> 9: okay
> 10: okay
>
> You can proceed.

## Options considered

**A line whose invoice or customer is not reached.** *Leave it out of the fact table.* Its case: every row of the fact
table is then complete, and no report shows an "unknown" customer. Rejected: the totals would no longer equal what the
source delivered, and the gap would be invisible. *Keep it, on the unknown member.* Adopted.

**"As known on" a date.** *Store the history of every business-vault and mart object, as snapshots or as ranges of
knowledge time.* Its case: an answer is read, not recomputed, and it stays what was published. Rejected for now: a
second structure to keep right beside an insert-only vault that already holds the evidence. *Replay.* Adopted.

**The decision register.** *One document listing all decisions.* Its case: one place to read. Rejected: one concept
per file is the repository's rule, and files can be cited and checked one by one. *One file per decision.* Adopted.

## Decision

1. **A present invoice line that cannot be placed keeps its row and its amounts**, on the unknown member of the
   dimension and without a date, and a test reports how many there are. It is a data quality issue and is kept
   visible, in the author's words.
2. **"As known on" a date is a replay**: every object above the raw vault is one query with a knowledge date as its
   parameter, kept as a table at the latest date and as a table macro for any earlier one. It answers what the current
   model gives on the deliveries dated up to that date, provided they were loaded in date order.
3. **The decision register is one small file per decision** under `registers/decisions/`. Every fact table and every
   analysis cites one, and the checker refuses those that do not.
4. With these, **the slice is built as note 141 describes it**, as revised after review.

## Consequences

An "unknown" customer or an undated line in a report is a finding about the data, not a defect of the report. What is
done about such lines is not decided here; quality gates are open (`ARC-OP-33`).

An "as known on" answer can change when a declaration or template changes, with no data having changed; what was
published on a date is a matter for release regression (`ARC-OP-30`). The replay is cheap at this size and would not
be for a very large fact table.

The decision register now exists with one entry, whose owner is the author standing in for a manager who does not
exist. Who maintains it at an organisation stays open (`ARC-OP-12`).

The revisions to 141 after review are unreviewed, and this decision is unreviewed on another model
([510](../50_process/510_external-review.md)).

**Revisit** decision 1 when quality gates are ruled; decision 2 when a fact table is too large to replay, or a user
needs what was published; decision 3 when the register has enough entries to show whether one file per decision
serves the people who keep it.
