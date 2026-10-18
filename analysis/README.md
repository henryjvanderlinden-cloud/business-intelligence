# Information analysis — how it is recorded

> **STATUS: PROPOSED, NOT RULED** (`ARC-OP-36` item 3). Drafted 2026-10-18, session 08, on the author's brief below.
> One worked example exists, [`wwi/tables/Sales.Orders/`](wwi/tables/Sales.Orders/), to judge the layout by; if the
> layout changes, the example is moved or rewritten. No convention here is enforced by `tools/check_repo.py` yet
> (AGENTS.md rule 11). Unreviewed.

This folder holds the information analysis of [129](../docs/10_architecture/129_information-analysis.md), done under
[ADR-0017](../docs/20_decisions/0017-information-analysis-before-building.md). It is written for agents first. The
author's brief, verbatim:

> Furthermore, think of a good structure on how to record this. It should be primarily usable for agents. I was
> thinking of a folder structure. A folder the information analysis. Maybe a folder per table. Maybe also a folder per
> attribute? What do you think? Also folders per analytical topic? I think we want small ascii/text files, that are
> easily gitable, that allow for multiple agents working simultaneously, that are easily searchable, that follow a
> predictable structure.

## Layout

```
analysis/
  README.md                         this file
  <source>/                         one folder per source, e.g. wwi/
    _source/                        items about the source as a whole
      18_documentation.md           e.g.; also 14, 20, 22, 23 where they hold source-wide
    tables/
      <Schema.Table>/               one folder per table, named exactly as in the source
        01_granularity.md           one file per item of 129, named <nn>_<slug>.md
        03_temporal.md
        05_role.md  06_keys.md  07_population.md  19_sensitivity.md   (the minimum)
        ...                         other items as they are done
        columns/
          <Column>.md               one file per column, named exactly as in the source
        evidence/
          E<nnn>_<slug>.json        what a finding rests on: query or code, as-of, result
    relations/                      item 4: one file per relationship
      <Schema.Table>.<Column>__<Schema.Table>.<Column>.md
    processes/                      item 24: one file per business process
    terms/                          item 25: one file per term with more than one meaning or name
    entities/                       item 26: one file per business entity
```

## Why this shape

**A folder per table: yes.** It is the unit an agent works on and the unit a build consumes. An agent analysing or
building on `Sales.Orders` reads one folder and nothing else.

**A folder per attribute: no; a file per attribute.** A column's findings — its meaning, date role, measure, codes,
format, copied-at-the-time status, sensitivity — belong together and are short. A folder per column with a file per
topic would give WWI about 3,300 files of a few lines each (368 columns outside the history tables, times nine
column-level topics), and an agent would need nine reads to learn one column. One file per column is one read.

**Folders per analytical topic: no, except for the four cross-table items.** A topic view is already a file pattern:
every sensitivity finding in WWI is `analysis/wwi/tables/*/19_sensitivity.md`, and every uncertain minimum is a
search for `confidence: low` or `unknown` in the six minimum files. A second tree organised by topic would hold every
finding twice, and the copies would drift. Relations, processes, terms and entities are different: they have no single
table to live in, so they get folders of their own.

**Small files, one writer.** Each finding lives in exactly one file, about one subject and one item. Two agents
working on different items of the same table, or on different tables, never touch the same file, so they need no
locking and their commits merge cleanly. No hand-maintained index file exists, because an index is the one file every
agent would edit; an index or a progress table is generated from the front matter on demand.

**An absent file means not yet analysed.** No placeholder files are created; the set of files present is the progress.

## Names

File and folder names are ASCII and are the source's own names, case preserved (`Sales.Orders`, `BackorderOrderID`),
so an agent can construct a path from a table or column name without looking it up. Item files take the two-digit
item number of 129 and its slug; 129's numbers are stable (ADR-0017), so a path never changes meaning. A history table
that only mirrors another table gets a folder with `05_role.md` alone, pointing to its base table.

File contents are plain text: Markdown with a front-matter block. ASCII throughout, except where a value is quoted
from the source and needs another character.

## The item file

```
---
item: 06                    two digits, from 129
topic: keys                 129's slug
subject: wwi/Sales.Orders   source/table, or source/table/column
tier: minimum               minimum | best-effort (ADR-0017)
status: proposed            proposed | ruled | stale
confidence: high            high | medium | low | unknown (below)
finding: OrderID is the declared primary key and is unique in the extract.
claims: [declared, observed]   the claim types of 120 the finding rests on
as_of: wwi 2016-06-01 manifest sha256 35b71b2e...
evidence: [E002, E004]      ids of files in evidence/
analysed_by: claude-opus-5-5
analysed_at: 2026-10-18
ruled_by: none              the person who ruled, if anyone
---

## Finding         what is the case, in a few sentences
## Reasoning       why the evidence supports it, and what else was considered
## Uncertainties   what is not established, and what would settle it
## For a person    questions only a person can answer; none if none
```

`finding` is one line, so `grep -r "^finding:" analysis/wwi/tables/Sales.Orders` gives the table's dossier in one
command. Flat `key: value` lines, so plain `grep` works without a YAML parser.

The column file has the same front matter with `item: column` and one section per column-level topic present, each
headed with its item number and carrying its own `confidence` line.

## Confidence

Proposed scale, so that "high" means the same from every agent:

- **high** — declared and observed agree; or observed without exception over the whole population, with a mechanism
  that explains it; or ruled by a person.
- **medium** — observed consistently over a short window (one load transition, one extract), or declared and not yet
  observed.
- **low** — inferred from names, descriptions, documentation or a sample.
- **unknown** — not established. For a minimum item this is the honest answer ADR-0017 asks for, with what would
  settle it under *Uncertainties*.

A declaration that the data contradicts lowers nothing: the contradiction is the finding, recorded with both claims.

## Evidence

Evidence files are written by deterministic machinery, or by an agent running a deterministic query, and are not
edited afterwards; a new run is a new file. Each holds the query or code, the tool, the source and its as-of with the
manifest hash, the run time, and the result. **Results are aggregates** — counts, distinct counts, minimums and
maximums, conformance rates — and never rows of source data, which `.gitignore` keeps out of the repository. They are
JSON because a CSV would be ignored there and because agents parse it without guessing.

## Working rules for agents

1. Read the table's folder before writing in it; write only the files of the item you are analysing.
2. One finding, one file. If a finding about one table needs a fact about another, link to that table's file.
3. Never guess a minimum item. Write `confidence: unknown` and the uncertainty.
4. Contradictions are findings. Keep both claims; do not choose between them.
5. When the evidence a finding rests on is superseded by a newer extract that disagrees, set `status: stale`.
6. Log the work in the step log as usual (`task_type: profiling` for measuring, `modelling` for proposing meaning).
