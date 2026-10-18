# ADR-0018 — The information-analysis record: a folder per table and per column, a file per item, a line per claim, content-addressed evidence and provenance in every file

- **Status:** Accepted
- **Date:** 2026-10-18
- **Supersedes:** —
- **Superseded by:** —
- **Amended by:** [ADR-0019](0019-information-analysis-in-two-rounds.md) (round 2 takes the cross-table folders)
- **Amends:** [ADR-0017](0017-information-analysis-before-building.md) (item 27's grain tests join the minimum)

## Context

[ADR-0017](0017-information-analysis-before-building.md) ruled what the information analysis of
[129](../10_architecture/129_information-analysis.md) inventories and with what effort. The author then asked for a
recording structure, verbatim:

> Furthermore, think of a good structure on how to record this. It should be primarily usable for agents. I was
> thinking of a folder structure. A folder the information analysis. Maybe a folder per table. Maybe also a folder per
> attribute? What do you think? Also folders per analytical topic? I think we want small ascii/text files, that are
> easily gitable, that allow for multiple agents working simultaneously, that are easily searchable, that follow a
> predictable structure.

A first layout, with a file per column and locally numbered evidence, was reviewed by astra
([XREV_2026-10-18_information-analysis-record_astra](../30_research/notes/XREV_2026-10-18_information-analysis-record_astra.md))
and failed: two agents could allocate the same evidence id, every item about a column shared one file, source names
broke as paths, and one status per file bundled several claims against
[ADR-0011](0011-assertions-identity-plane-publication-gate.md). Eleven recommendations followed (`ARC-OP-36`, R1 to
R11). The author then added two points, verbatim:

> one more thing before we proceed, we should also test each table for peculiarities like multiple granularities in
> one table (a table containing both customer data and contract data apart from keys, or events/transactions and
> balances), I'm sure you can come up with more. Also, in every file we should probably record who wrote it, when it
> was written, maybe also other meta data. That we we can see if claims are stale or fresh.

which became item 27 of 129 and recommendations R12 and R13. He ruled on all thirteen on 2026-10-18 at 14:13:
"Proceed as suggested".

## Options considered

*One file per table with sections.* Its case: fewest files, one read per table. Rejected: every agent on a table
edits the same file, and the files grow large.

*A file per item and a file per column* (the first layout). Its case: one read per column. Rejected on astra's
finding that item ownership is then not file ownership.

*A folder per column with a file per item, as the author suggested.* Its case: every finding has exactly one file,
so agents never share one. Its cost — many small files — is what the author asked for, and files exist only where
something has been found. Adopted.

*Folders per topic.* Its case: a topic view in one place. Rejected for findings with a single table as their home:
a second tree would hold every finding twice. A topic view is a file pattern.

## Decision

The layout and its rules are specified in [`analysis/README.md`](../../analysis/README.md), which is the operating
manual for agents. In short:

1. **R1, R2.** `analysis/<source>/tables/<schema>/<table>/`, with a file per item (`<nn>_<slug>.md`) and
   `columns/<column>/` holding a file per item about that column. Names are the source's own, reversibly escaped:
   `A-Z a-z 0-9 _ -` kept, every other byte of the UTF-8 name percent-encoded, the last letter of a reserved Windows
   name encoded. Names that differ only in case are an error.
2. **R3, R4.** Evidence files are named by the first 16 hex digits of the SHA-256 of their content, written once, and
   hold the computation, its run time and its inputs. Data rows are never stored; catalogue metadata may be.
3. **R5, R6.** Each claim is one line, with its own type, lifecycle status (proposed, accepted, contested,
   superseded, retracted), confidence, evidence, effective and observation dates and recheck condition. Confidence
   measures evidence; a ruling sets status and `ruled_by`, not confidence.
4. **R7, R8.** Each fact is stated once and linked elsewhere; each subject carries a permanent id.
5. **R9, R10.** `<source>/_source/`, `<source>/reconciliations/` and `analysis/_landscape/` hold set-level
   findings; dependency closure needs a generated index, not grep.
6. **R12.** Every file records who wrote it, when, at which step, by which method, on which inputs, when it was last
   checked and against what, review and ruling, supersession and its recheck condition. Freshness — fresh, ageing,
   stale — is computed by a tool from those fields.
7. **R13, amending ADR-0017.** The tests of item 27 that bear on grain (1 to 9 and 11 to 13) are part of the minimum
   and done with its hard effort; the others are best effort.
8. **R11.** The `Sales.Orders` example is redone in this layout.

## Consequences

The checker validates the record (rule 11), so a malformed file fails the repository check. Many small files make a
table's dossier several reads rather than one; `tools/ia_status.py` gives the summary in one command. The permanent id
is the source catalogue's own object id for now, which survives a rename in the source but not a re-platforming;
revisit when the identity plane of ADR-0011 is built. Revisit the whole layout if agents working in parallel on it
still conflict, or if the file count becomes a cost in git.
