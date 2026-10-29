# The model declarations — how they are written

> **STATUS: PROPOSED.** Drafted 2026-10-29 in session 11 from handover 11, as the declaration format owed under
> [`ARC-OP-29`](../registers/OPEN_POINTS.md) and [ADR-0032](../docs/20_decisions/0032-generated-sql-machinery.md)
> decision 1. Reviewed on sol, which failed the first version
> ([XREV](../docs/30_research/notes/XREV_2026-10-29_model-format_sol.md)); this is the revised text, itself unreviewed.
> Nothing here is ruled. Enforced by
> `python tools/check_repo.py` (`check_model`), parsed by [`tools/model_lib.py`](../tools/model_lib.py).

This folder holds the data model as text, in the sense of [142](../docs/10_architecture/142_the-data-model.md) §3: one
small file per model object, holding only the decisions, from which the generator of ADR-0032 would write the SQL and
from which every picture is drawn. The files are the truth; the viewer and the generated SQL only read them. The first
content is the raw vault of Wide World Importers as ruled in
[147](../docs/10_architecture/147_wwi-concepts-keys-and-business-time.md) to
[149](../docs/10_architecture/149_wwi-satellites.md) (ADR-0028 to ADR-0031, ADR-0033), transcribed by
[`transcribe_wwi.py`](../prototypes/model_declarations/transcribe_wwi.py) so that the transcription can be repeated
rather than trusted.

## 1. Layout

```
model/
  README.md                                   this file
  sources/<source>.md                         one per source: its key space and its base tables
  raw_vault/
    hubs/hub_<concept>.md                     one per hub; no source in the path, a concept can have several
    links/lnk_<from>__<role>.md               one per link; the role names the relationship from the driving hub
    satellites/<source>/sat_<parent>__<source>[__<part>].md   one per satellite (149 Rule 1)
    reference/<source>/ref_<table>__<source>.md                 one per reference table (149 Rule 8)
```

The business vault and the marts would get folders of their own when they are designed.

## 2. Grammar

The grammar of the analysis record ([`analysis/README.md`](../analysis/README.md)), so that one way of reading serves
both and the checker needs nothing beyond Python's standard library:

1. A front matter between two lines `---`, one `key: value` per line, values on one line, lists comma-separated.
2. Sections headed `## <name>`. Each entry is one line `- <subject> | key=value | key=value`, the subject first.
3. An optional section `## Notes` of prose, for what a reader needs and no field holds.

YAML and LinkML ([142](../docs/10_architecture/142_the-data-model.md) §8) are not used: the declaration language falls
under [`ARC-OP-20`](../registers/OPEN_POINTS.md), which puts languages after principles, and a flat grammar is easy to
move into either later.

## 3. Identity

`id` is permanent and never reused: `nsdn:rv:hub:<concept>`, `nsdn:rv:link:<from>__<role>`, `nsdn:rv:sat:<…>`,
`nsdn:rv:ref:<…>`, `nsdn:source:<source>`. `name` is the table's name and may change; a renamed object keeps its id and
records the earlier name under `aliases`. Other files refer to an object by its current name, which people and agents
can read; this is safe because **a name is never reused**: no name or alias may appear twice across the model, so a
reference cannot silently move to another object, and a reference to an alias fails the check. Source tables and
columns are referred to by their qualified names; their permanent ids are the catalogue's (`wwi:object:<n>`,
[`analysis/README.md`](../analysis/README.md)), and a source rename is a change of source contract, seen by the
checker as one column missing and one column new.

## 4. What each kind declares

Every file carries `id`, `kind`, `name`, `status` (`proposed`, `accepted`, `contested`, `retired`), `ruled_in` (the
ADRs), `defined_in` (the note and section it comes from), `written_by`, `written_at`, `step` and `method`. Then:

**Mappings.** A hub or a link is loaded from one or more source tables, and each such load is a *mapping*. In a hub's
*Business key* section, each line is one mapping: lines are alternatives, never parts of one key. The parts of a
composite key are written on one line, in key order, joined by ` + ` (`Sales.X.A + Sales.X.B`). In a link's *Columns*
section, the lines from one source table form one mapping, which has exactly one `end=from` and one `end=to` line;
a second source would add a second pair. Each endpoint has as many parts as its hub's business key.

**Hub**: `concept`, `grain`, `subject_area`; section *Business key*, one line per mapping, with `key_space` and
`key_kind` (`record-identifier`, `governed`, `source-key`); section *Evidence*.

**Link**: `label`, `from` and `to` (hubs), `driving` (the `from` hub, or `none` for a bridge), `optional` (`yes` where
the naming column may be empty, 148 Rule 4), `effectivity` (`load`, `event`, `milestone`, `absence`, 148 §3) and
sections *Columns*, *Relations* (the analysis record's relation folder) and *Evidence*. In *Columns*, the `end=from`
line names the column that identifies the driving hub (for most links, that hub's own key in the same table) and carries
`effectivity_start` for that mapping: a column, `load`, `presence in a complete extract`, or `unknown`; the `end=to`
line names the column that identifies the named hub, with `resolve=…` where the source names it by another identifier
than the hub's key (the country, ADR-0028 decision 1). A source column the link keeps without its being an endpoint is
marked `kept=…`.

**Satellite**: `parent`, `source`, `source_table`, `parent_key` (the columns of the source table that identify the
parent, in the order of the parent's business key, joined by ` + `; for a link parent, `from=<column>, to=<column>`), `satellite_kind` (`payload`, `milestone`, `reading`), `split_reason`, `valid_time` (a column, `unknown`, or
`none; sampled`), `class` (149 Rule 9) and, where the class depends on a fact not yet known, `class_condition`;
section *Columns*, one line per source column, with these flags where they apply: `as_delivered=<link>` (an optional
relationship kept as delivered, 149 Rule 5), `code=<reference table>`, `reading_key=yes`, `repeats=<satellite>` (a
reading's key or time carried by both satellites of one reading series), `load=never` (ADR-0033 decision 2),
`valid_time=…` (a column whose valid time differs from the satellite's).

**Reference table**: `source_table`, `key`, `key_space`, `history` (its history table), `class`; section *Columns*.

**Source**: `title`, `key_space`, `extract`, `by_rule`; section *Base tables*, one line per base table with `extract`
(`full`: every extract holds the table complete, which is what absence is judged against; `delta` otherwise),
`system_time`, `audit`, `history` and `catalogue`, the analysis record's catalogue evidence for that table.

## 5. What is not declared

Declared is what carries a decision (142 §3). The rest follows by rule and would be generated:

1. **Data types, nullability and descriptions**: read from the source catalogue named in the source file.
2. **Hash keys** of hubs and links (ADR-0030), load time, batch, the three clocks and the source-version identifier on
   every satellite row (149 Rule 2).
3. **The audit satellite** of every hub (149 Rule 3), `sat_<hub>__<source>__audit`, from the source's audit column and
   source system time.
4. **The status-tracking satellite** of every hub whose mapping's table is declared `extract=full` (149 Rule 7),
   `sts_<hub>__<source>`; absence is judged against that table's complete extract and resolved under 127, "Absence is
   not deletion". A table filtered at extraction is not `full`.
5. **The effectivity satellite** of every link (149 Rule 6), `eff_<link>__<source>`, with the start declared on the
   mapping's `end=from` line and the end by driving key.

What a generator would still have to be told, and the format does not yet hold, is listed under `ARC-OP-29`: ordering
and tie-breaking of versions with equal source system time, and late arrivals. Both wait for the generator's design.

For Wide World Importers that is 123 declared tables (22 hubs, 49 links, 45 satellites, 7 reference tables) and 93
generated by rule, 216 raw-vault tables in all.

## 6. What the checker enforces

`check_model` in [`tools/check_repo.py`](../tools/check_repo.py), on every run:

1. Front matter and sections complete for the kind; names follow the patterns above; the file name is the name; ids
   unique and prefixed by kind; status and class from their lists; the writer a known agent.
2. Every reference resolves: `ruled_in` to ADRs on disk, `defined_in` to a file, hubs, links, parents, codes and
   `as_delivered` to declared objects, every citation in *Evidence* and *Relations* to a file and, where given, to its
   claim.
3. Every link mapping has one `from` and one `to` line from one table, each with as many parts as its hub's key, and
   the `from` line carries `effectivity_start`; every satellite's `parent_key` has as many parts as its parent's key;
   every base table declares `extract`; no name or alias is used twice.
4. **Every column of every base table has exactly one disposition**: a hub's business key, a link endpoint, one
   satellite, a reference table, a column kept by a link, or a rule of the source file (source system time; the audit
   column, except in reference tables). A column may be used more than once only in the patterns that follow from
   that disposition: a business key is also the `from` end of the hub's links and the `parent_key` of its satellites;
   an optional relationship is a link's `to` end and is kept as delivered in the naming hub's satellite (149 Rule 5).
   A forgotten column, a column in two satellites, an optional relationship not kept as delivered, or a mandatory one
   copied into a satellite fails the run.
5. `Application.People.HashedPassword` is declared `load=never`.

Not enforced yet: that a declared object is consumed by a generator or cited by a decision (142 §9), because no
generator exists.
