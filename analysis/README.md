# Information analysis - how it is recorded

> **STATUS: RULED** 2026-10-18 in [ADR-0018](../docs/20_decisions/0018-information-analysis-record.md) and, for the two
> rounds, item 28, round 2's layout (section 9) and extraction visibility under item 7,
> [ADR-0019](../docs/20_decisions/0019-information-analysis-in-two-rounds.md). After review
> by astra ([XREV](../docs/30_research/notes/XREV_2026-10-18_information-analysis-record_astra.md)). Enforced by
> `python tools/check_repo.py`; summarised by `python tools/ia_status.py`.

This folder holds the information analysis of [129](../docs/10_architecture/129_information-analysis.md), done under
[ADR-0017](../docs/20_decisions/0017-information-analysis-before-building.md). It is written for agents first. The
author's brief, verbatim:

> Furthermore, think of a good structure on how to record this. It should be primarily usable for agents. I was
> thinking of a folder structure. A folder the information analysis. Maybe a folder per table. Maybe also a folder per
> attribute? What do you think? Also folders per analytical topic? I think we want small ascii/text files, that are
> easily gitable, that allow for multiple agents working simultaneously, that are easily searchable, that follow a
> predictable structure.

and, on metadata:

> Also, in every file we should probably record who wrote it, when it was written, maybe also other meta data. That
> we we can see if claims are stale or fresh.

## 1. Layout

Round 1 (ADR-0019) is per table and per column: the `tables/` tree and `_source/`. Round 2, across tables, is section 9,
whose `across/` tree replaces the cross-table folders shown here (`reconciliations/`, `relations/`, `processes/`,
`terms/`, `entities/` live under `<source>/across/`).

```
analysis/
  README.md                                this file
  _landscape/<slug>.md                     findings spanning more than one source
  <source>/                                e.g. wwi
    _source/<nn>_<slug>.md                 source-wide items (14, 18, 20, 22, 23, 29)
    reconciliations/<slug>.md              item 16 when it spans tables
    relations/<rel>.md                     item 4, one file per relationship (name below)
    processes/<slug>.md                    item 24, one per business process
    terms/<slug>.md                        item 25, one per term
    entities/<slug>.md                     item 26, one per business entity
    tables/<schema>/<table>/
      <nn>_<slug>.md                       one file per item about the table
      columns/<column>/<nn>_<slug>.md      one file per item about one column
      evidence/<hash>.json                 what claims rest on; written once
```

A source without schemas uses `_` as its schema folder. **A file exists only when something has been found**: an
absent file means not yet analysed, and no placeholder is ever created.

**Every finding has exactly one file**, so two agents never edit the same file unless they analyse the same item of
the same subject, which the step log assigns to one of them. Evidence files are named by their content, so no id is
allocated and none can collide. No index is kept by hand; `tools/ia_status.py` generates one.

## 2. Items and their file names

The number is the item's number in 129 and never changes. Column-level files use the items marked *c*.

| nn | slug | level | | nn | slug | level |
|---|---|---|---|---|---|---|
| 01 | granularity | table, minimum | | 15 | quality | table, c |
| 02 | meaning | table, c | | 16 | reconciliation | table |
| 03 | temporal | table, c, minimum | | 17 | volume | table |
| 04 | relations | `relations/` | | 18 | documentation | table, c, source |
| 05 | role | table, minimum | | 19 | sensitivity | table, c, minimum |
| 06 | keys | table, c, minimum | | 20 | ownership | table, source |
| 07 | population | table, c, minimum | | 21 | demand | table, c |
| 08 | measures | table, c | | 22 | stability | table, c, source |
| 09 | derived | table, c | | 23 | extraction | table, source |
| 10 | codes | table, c | | 24 | processes | `processes/` |
| 11 | formats | table, c | | 25 | terms | `terms/` |
| 12 | copies | table, c | | 26 | entities | `entities/` |
| 13 | hierarchies | table, c | | 27 | peculiarities | table, c; tests 1-9, 11-13 minimum |
| 14 | provenance | table, source | | 28 | arithmetic | table, c |
| | | | | 29 | position | table, source (ADR-0021) |

## 3. Names

Folder and file names are the source's own names, **escaped reversibly**: the characters `A-Z a-z 0-9 _ -` are kept;
every other byte of the name in UTF-8, `%` and `.` included, becomes `%` and two upper-case hex digits; and if the
result is a reserved Windows name (`CON`, `PRN`, `AUX`, `NUL`, `COM0`-`COM9`, `LPT0`-`LPT9`, in any case), its last
letter is encoded too. So `Unit/Price` is `Unit%2FPrice`, `AUX` is `AU%58`, `Klantnaam beeindigd` with a diaeresis
is `Klantnaam%20be%C3%ABindigd`. Every path is ASCII and can be built from the source name without a lookup. Two
names in one folder that differ only in case are an error. A relation file is named
`<schema>.<table>.<column>__<schema>.<table>.<column>.md`, each part escaped; since `.` inside a name is escaped,
the separators are unambiguous.

## 4. The item file

```
---
id: wwi:object:1154103152:column:6       permanent id of the subject (below)
subject: wwi/tables/Sales/Orders/columns/BackorderOrderID
item: 02
topic: meaning
tier: minimum                            minimum | best-effort (ADR-0017, ADR-0018)
summary: one line: the finding
confidence: high                         the lowest confidence among the claims below
claims: 3                                the number of claim lines
written_by: claude-opus-5-5              as named in records/vocabulary.json
written_at: 2026-10-18T12:40:00Z
step: S08-041                            the step-log entry: who asked, and why
method: what produced the claims, with the git blob hash of any script
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: <sha256 of the extract's manifest.json>
input_schema_sha256: <sha256 of the table's column names in order, from the extract header>
last_checked_at: 2026-10-18T12:40:00Z    last re-verification, even without a rewrite
last_checked_by: claude-opus-5-5
last_checked_against: 2016-06-01         the extract it was last verified against
reviewed_by: none
reviewed_at: none
ruled_by: none
ruled_at: none
supersedes: none
superseded_by: none
recheck_when: the condition under which the claims must be re-checked, in words
---

## Claims

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=3f2a9c01d4e5b6a7 | recheck=description changes | text: The source describes ...

## Reasoning
## Uncertainties
## For a person
```

Every key is a flat `key: value` line, so `grep` works without a YAML parser: `grep -r "^summary:"` on a table
folder gives its dossier; `grep -rl "^confidence: unknown"` finds every file with an unestablished claim.

**A claim is one line**, an assertion in the sense of [ADR-0011](../docs/20_decisions/0011-assertions-identity-plane-publication-gate.md):

- `C<n>`, unique in the file; elsewhere a claim is cited as `<path>#C<n>`.
- `type`: declared, observed, implemented, intended, certified ([120](../docs/10_architecture/120_context-layer.md)).
- `status`: proposed, accepted, contested, superseded, retracted (120's lifecycle).
- `confidence`: section 5.
- `effective`: the date the claim holds for in the source (the extract date); `observed`: when it was established;
  `checked`: when it was last re-verified.
- `evidence`: evidence hashes from the table's `evidence/`, comma-separated, or `none`.
- `recheck`: the condition under which this claim must be re-checked.
- `text:` last, so the text may contain `|`.

The uncertain part of a minimum item is **its own claim with `confidence=unknown`**, saying what would settle it.
Contradicting claims are both kept; neither is retracted for the other. **Each fact is stated once**: other files link
to the claim that owns it rather than restate it.

**The permanent id** is the source catalogue's own identity: `wwi:object:<object_id>` for a table,
`...:column:<column_id>` for a column. It survives a rename in the source, not a re-platforming (ADR-0018).

## 5. Confidence

Confidence measures evidence, not authority.

- **high** - declared and observed agree; or observed without exception over the whole population, with a mechanism
  that explains it.
- **medium** - observed consistently over a short window (one load transition, one extract), or declared and not yet
  observed.
- **low** - inferred from names, descriptions, documentation, a sample or a second-hand summary.
- **unknown** - not established; the claim says what would settle it.

A count over an extract, stated as a fact about that extract, is high: the evidence shows it. A rule generalised from
it - a value that is unique, a code that never occurs, one row per something - is medium unless a declared constraint
or a mechanism explains it; the claim says "in this extract" and, where true, that no constraint enforces it. A
reading from names alone is low.

A ruling sets `status=accepted` and the file's `ruled_by` and `ruled_at`; it does not raise confidence.

## 6. Freshness

Computed by `tools/ia_status.py`, never set by hand, per file:

- **fresh** - `last_checked_against` is the newest extract of the source, and the table's columns are unchanged
  (`input_schema_sha256` equals the newest extract's);
- **ageing** - last checked against an older extract, columns unchanged;
- **stale** - the columns have changed, or `superseded_by` is set.

`recheck_when` and each claim's `recheck` are in words; the tool lists them for an agent to evaluate. Re-verifying a
claim without changing it updates `checked`, `last_checked_at`, `last_checked_by` and `last_checked_against`, so an
old claim confirmed yesterday shows as fresh. Git cannot carry this: every commit is under the author's git identity
whichever agent wrote it, and records when the commit was made, not when the analysis was done or on which data.

## 7. Evidence

An evidence file is JSON, written by deterministic machinery or by an agent running a deterministic query, and never
edited: a new run is a new file. It holds `kind`, `tool` and `tool_version` (the git blob hash of the script), the
`code` or `query` that produced it, `inputs` (source, extract, manifest hash, or database and simulation clock),
`ran_at`, and `result`. Its name is the first 16 hex digits of the SHA-256 of its canonical JSON without the `id`
field, and `id` repeats it; the checker verifies both. **Results are aggregates** - counts, distinct counts, minimums,
maximums, conformance rates - and never rows of source data. Catalogue metadata (column names, types, constraints,
descriptions) may be kept verbatim. A source read on the web is evidence too, with its URL, the fetch date, how it
was read, and the excerpt relied on.

## 8. Rules for agents

1. Read the subject's folder before writing in it; write only the file of the item you were assigned.
2. Never guess a minimum item. Write the claim with `confidence=unknown` and what would settle it.
3. Keep contradictions as two claims.
4. State a fact once; link to it elsewhere.
5. When you re-verify, update the check fields; when the evidence disagrees, add a claim and set the old one to
   `status=contested` or `superseded`.
6. Log the work in the step log (`task_type: profiling` for measuring, `modelling` for proposing meaning).
7. "What must be rechecked if this changes" is a question for a generated dependency index, not for grep; none
   exists yet.
8. Describe the as-is ([ADR-0020](../docs/20_decisions/0020-analysis-describes-the-as-is.md)): record what the data and
   the source show and do, and warn where a fact has consequences; do not propose measures, reporting dates, designs
   or loading, and put no such question to a person. Not enforced by the checker.

## 9. Round 2: across tables (ruled 2026-10-18, ADR-0019)

Round 2 asks how tables relate, if at all; which cross-table peculiarities deserve a warning; and what an assumed or
proven join means (ADR-0019). It has its own tree, built like round 1 so an agent needs to learn one shape:

```
analysis/<source>/across/
  relations/<rel>/                  one folder per relation; <rel> as in section 3, composite keys as more columns
    01_granularity.md               the grain of each side and of the joined result; cardinality both ways,
                                    declared, observed and asserted (128)
    02_meaning.md                   what the join means: which question it answers, the role of each side
                                    (customer or bill-to customer), and which candidate key it targets
    03_temporal.md                  whether it holds as of a time: point-in-time joins, late-arriving parents
    06_keys.md                      key roles on each side; enforced or not
    07_population.md                orphans both ways, optionality, the filters under which the cardinality holds
    27_peculiarities.md             warnings: fan-out, double counting, chasm and fan traps, many-to-many through a
                                    bridge, ambiguous key targets, several paths between the same two tables
    evidence/<hash>.json
  processes/<slug>/                 item 24, the same item files where they apply
  terms/<slug>/                     item 25
  entities/<slug>/                  item 26
  reconciliations/<slug>/           item 16 across tables
  candidates.md                     generated, not hand-edited: relations to analyse, from declared foreign keys,
                                    observed value inclusion and names, each marked assumed or proven
```

The minimum for a relation is items 01, 02, 06, 07 and 27: the cardinality, the meaning, the key roles, the
orphans and the warnings, with the same hard effort as round 1's minimum (R14). Sol's counterexample — two candidate
keys a foreign key could point to, both giving a clean one-to-one join — is caught by 02 and 06 together. A relation
nobody has proven stays a folder whose claims say `type=observed` or `intended` with their confidence; "assumed" is a
confidence, not a separate kind of file.

**The tests per relation** (guideline, added 2026-10-19 at the author's request; `relations.py` runs them, the item
named holds the result):

| test | what it shows | item |
|---|---|---|
| orphans, child to parent | **referential integrity**: rows naming a parent that does not exist | 07 |
| unreferenced parents | parent rows no child names (a parent without children, or children not yet loaded) | 07 |
| optionality | rows where the referring column is empty, by transaction type where the table has one | 07 |
| extraction visibility | whether the extract holds every row the owner sees, for both tables (R15) | 07 |
| children per parent | the cardinality as observed, against the declared one; one-to-one that nothing enforces | 01, 27 |
| other accepting keys | other unique columns of the parent that hold every value: an ambiguous key target | 06 |
| several paths | other foreign keys from the same child to the same parent: roles that a join must name | 27 |
| fan-out and chasm | how often a parent row repeats; other children of the same parent that multiply against it | 27 |
| current versions | a system-versioned parent gives its attributes as of the extract, not as of the child row | 27 |
| two routes | a second path to the same parent through another table: agreement shows a copy, disagreement a role | 27 |
| header join | for a relation on several columns, the rows a join on the first column alone would give | 27 |

Referential integrity holds by construction where the source declares an enabled and trusted foreign key; it is still
measured, because an extract can break it (tables extracted at different moments, rows hidden from the extracting
account) and because an undeclared relation has no such guarantee. Item 16 across tables, in `reconciliations/`,
compares what two tables say about the same amounts, quantities or dates (`reconcile.py`).

