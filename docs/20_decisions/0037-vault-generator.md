# ADR-0037 — The vault generator: SHA-256 keys, one load pattern for every day, every version kept, and the vault's first day replayed from 2016-05-31

- **Status:** Accepted
- **Date:** 2026-11-04
- **Supersedes:** —
- **Superseded by:** —

## Context

[ADR-0032](0032-generated-sql-machinery.md) ruled the machinery: declarations, a generator, generated plain SQL as dbt
models. [ADR-0034](0034-model-declaration-format-and-viewer.md) ruled the declaration format. What the generator
writes, and how each generated model loads, was owed under `ARC-OP-29`, together with the hash algorithm and key
preparation left open by [ADR-0030](0030-hub-and-link-keys-are-hash-keys.md) and the ordering, tie-breaking and late
arrivals owed by the format.

[143](../10_architecture/143_the-vault-generator.md) proposes it. Sol failed its first version on five findings
([XREV](../30_research/notes/XREV_2026-11-03_143-vault-generator_sol.md)), all applied. A query on the sandbox
(`s12-ties`) found 11 versions in three system-versioned tables that share their start time with the next version of
the same key, all zero-length. On 2026-11-03 the model put three choices to the author (143 §11). He replied on
2026-11-04 at 13:27, verbatim:

> 1. agree
> 2. agree
> 3. agree

## Options considered

Per choice, as set out in 143 §11:

1. *Zero-length versions*: keep them, ordered by `source_seq`; or drop them, as SQL Server's own "as of" queries do.
2. *The vault's first day*: start at 2016-06-02, the extract now in landing; or replay the three kept extracts from
   2016-05-31 into a fresh warehouse.
3. *Case of text keys*: a `key_case` field on the source declaration; or one rule for all sources.

The rest of 143 (files and headers, SHA-256, key preparation, knowledge time as the extract's date, the load pattern
of each kind, restatement after a late arrival, deletion of a failed batch before its retry, tests) was put to the
author as one design, with only these three as choices.

## Decision

1. **143 is the design of the generator**, as revised after review.
2. **Zero-length versions are kept**, numbered by `source_seq` (143 §6 item 2), because the raw vault keeps
   everything delivered (144 §2).
3. **The vault's first day is 2016-05-31.** When the generated models go live, the working warehouse
   (`data/warehouse/`) is moved aside, not deleted, and the runner reloads the three kept extracts in order.
4. **The source declaration carries `key_case`**, `fold` or `exact`; Wide World Importers is `fold`. The field is
   added to the format of ADR-0034 and enforced by `check_model`.

## Consequences

The generator, its templates, the generated models and their tests are built next, first in the cloud workspace on
copies of the kept extracts, and written into the live project only when they pass (143 §9 item 3).

149 Rule 3 describes the audit satellite's change detection as covering `LastEditedBy` and source system time; 143 §5
item 6 replaces that with no change detection, because two versions in one instant by one person are otherwise lost.
149 stands otherwise.

`deletion-confirmed` in the status-tracking satellites is not generated until the conditions of 127 are stated as
testable rules (143 §12).

The revised text of 143 is unreviewed on another model. **Revisit** if the first loads show the restatement rule or
the failed-batch pre-hook misbehaving, if loads become slow because each compares incoming versions with whole
satellites, or when a second source is added.
