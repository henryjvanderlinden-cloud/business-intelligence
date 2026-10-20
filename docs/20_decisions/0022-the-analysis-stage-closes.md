# ADR-0022 — The analysis stage of the first trial closes; its record stays a description of the as-is and stays open

- **Status:** Accepted
- **Date:** 2026-10-20
- **Supersedes:** —
- **Superseded by:** —
- **Amends:** [ADR-0020](0020-analysis-describes-the-as-is.md) (what follows when the analysis stage ends)

## Context

[ADR-0020](0020-analysis-describes-the-as-is.md) bound the analysis to the as-is "while in the analysis stage" and asked
to be revisited when the build stage begins. On 2026-10-20 the author named the next phase - modelling the data in a
generic integration layer such as a Data Vault, with the questions of bitemporality and of derived measures and
calculation engines - and asked whether the analysis was done. The model answered that it was enough to start
modelling, with one gap bearing on derived measures (items 8, 9 and 28), and proposed to record, at the close, a
statement of coverage, what becomes of ADR-0020, and the lessons of the trial. The author answered at 21:51, verbatim:

> Yes, do items 8,9 and 29 before we close. Write down points 8 to 10.

"29" is read as 28: item 29 was already done that evening, and the gap named was items 8, 9 and 28. Items 8, 9 and 28
were done the same evening (`ARC-OP-36`).

## Options considered

*Keep analysing until every best-effort item is done for every table.* Its case: a model built on a complete record
needs fewer corrections. Rejected: the remaining items (codes, formats, copies, hierarchies, quality, volume) bear less
on an integration layer than what is done, ADR-0017 makes the analysis best effort and never a gate, and the items that
need people (provenance, ownership, demand) cannot be done in a sandbox at all.

*Close the analysis and freeze its record.* Its case: a fixed reference for the design. Rejected: modelling will find
facts the analysis missed, and a frozen record would push them into design documents, where facts and designs mix.

*Close the stage, keep the record open.* Adopted.

## Decision

1. **The analysis stage of the first trial, on the Wide World Importers sandbox, is closed** with what is recorded on
   2026-10-20. Its coverage is stated in `ARC-OP-36`; what is not covered is said there with the reason.
2. **The record remains a description of the as-is.** ADR-0020's rule continues to hold for the files under
   `analysis/`: they record what the source declares, shows and does, and carry no design advice, also during and after
   modelling.
3. **Design goes into design documents.** Choices of model, temporality, measures and calculation belong in
   `docs/10_architecture/`, ADRs and the model's own files, which cite the analysis claims they rest on.
4. **The record stays open.** A fact found during modelling is added to the record as a claim with its evidence, by the
   rules of `analysis/README.md`; a claim found wrong is corrected or superseded there. The analysis never becomes a
   gate (ADR-0017).
5. **The questions ADR-0020 kept out of the analysis** - measures and KPIs, reporting dates, model designs, loading and
   exclusion - may now be put to the author as part of modelling.

## Consequences

The design stage starts from a record it can cite but not edit to suit a design. The record ages: its files describe
the extract of 2016-06-01 and show as ageing in `tools/ia_status.py`; a recheck against a newer extract
(`recheck.py`, item 22) says which rules still hold. Revisit when a second source is analysed, or if modelling finds
that a design cannot be stated without facts the record does not hold.
