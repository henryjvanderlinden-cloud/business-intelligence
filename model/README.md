# The model declarations — how they are written

> **STATUS: PROPOSED, unreviewed.** Drafted 2026-10-29 in session 11 from handover 11, as the declaration format owed
> under [`ARC-OP-29`](../registers/OPEN_POINTS.md) and [ADR-0032](../docs/20_decisions/0032-generated-sql-machinery.md)
> decision 1. Nothing here is ruled: the author has the proposal and has not answered. Enforced by
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
records the earlier name under `aliases`. Other files refer to an object by its name, which the checker resolves.

## 4. What each kind declares

Every file carries `id`, `kind`, `name`, `status` (`proposed`, `accepted`, `contested`, `retired`), `ruled_in` (the
ADRs), `defined_in` (the note and section it comes from), `written_by`, `written_at`, `step` and `method`. Then:

**Hub**: `concept`, `grain`, `subject_area`; section *Business key*, one line per source column that feeds the key, with
`key_space` and `key_kind` (`record-identifier`, `governed`, `source-key`); section *Evidence*.

**Link**: `label`, `from` and `to` (hubs), `driving` (the `from` hub, or `none` for a bridge), `optional` (`yes` where
the naming column may be empty, 148 Rule 4), `effectivity` (`load`, `event`, `milestone`, `absence`, 148 §3) and
`effectivity_start` (the column, `load`, or `unknown`); sections *Columns* (the source column, with `names=<hub>`),
*Relations* (the analysis record's relation folder) and *Evidence*.

**Satellite**: `parent`, `source`, `source_table`, `parent_key` (the column of the source table that identifies the
parent), `satellite_kind` (`payload`, `milestone`, `reading`), `split_reason`, `valid_time` (a column, `unknown`, or
`none; sampled`), `class` (149 Rule 9) and, where the class depends on a fact not yet known, `class_condition`;
section *Columns*, one line per source column, with these flags where they apply: `as_delivered=<link>` (an optional
relationship kept as delivered, 149 Rule 5), `code=<reference table>`, `reading_key=yes`, `repeats=<satellite>` (a
reading's key or time carried by both satellites of one reading series), `load=never` (ADR-0033 decision 2),
`valid_time=…` (a column whose valid time differs from the satellite's).

**Reference table**: `source_table`, `key`, `key_space`, `history` (its history table), `class`; section *Columns*.

**Source**: `title`, `key_space`, `extract`, `by_rule`; section *Base tables*, one line per base table with
`system_time`, `audit`, `history` and `catalogue`, the analysis record's catalogue evidence for that table.

## 5. What is not declared

Declared is what carries a decision (142 §3). The rest follows by rule and would be generated:

1. **Data types, nullability and descriptions**: read from the source catalogue named in the source file.
2. **Hash keys** of hubs and links (ADR-0030), load time, batch, the three clocks and the source-version identifier on
   every satellite row (149 Rule 2).
3. **The audit satellite** of every hub (149 Rule 3), `sat_<hub>__<source>__audit`, from the source's audit column and
   source system time.
4. **The status-tracking satellite** of every hub loaded from a full extract (149 Rule 7), `sts_<hub>__<source>`.
5. **The effectivity satellite** of every link (149 Rule 6), `eff_<link>__<source>`, whose start is declared on the
   link.

For Wide World Importers that is 123 declared tables (22 hubs, 49 links, 45 satellites, 7 reference tables) and 93
generated by rule, 216 raw-vault tables in all.

## 6. What the checker enforces

`check_model` in [`tools/check_repo.py`](../tools/check_repo.py), on every run:

1. Front matter and sections complete for the kind; names follow the patterns above; the file name is the name; ids
   unique and prefixed by kind; status and class from their lists; the writer a known agent.
2. Every reference resolves: `ruled_in` to ADRs on disk, `defined_in` to a file, hubs, links, parents, codes and
   `as_delivered` to declared objects, every citation in *Evidence* and *Relations* to a file and, where given, to its
   claim.
3. **Every column of every base table has exactly one place**: a hub's business key, a link, one satellite, a
   reference table, or a rule of the source file (source system time; the audit column, except in reference tables).
   A forgotten column, a column in two satellites, an optional relationship not kept as delivered, or a mandatory one
   copied into a satellite fails the run.
4. `Application.People.HashedPassword` is declared `load=never`.

Not enforced yet: that a declared object is consumed by a generator or cited by a decision (142 §9), because no
generator exists.
