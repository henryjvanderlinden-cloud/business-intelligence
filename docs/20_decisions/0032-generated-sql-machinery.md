# ADR-0032 — The deterministic machinery is generated plain SQL: declarations, a generator, and dbt models in folders

- **Status:** Accepted
- **Date:** 2026-10-29
- **Supersedes:** —
- **Superseded by:** —

## Context

On 2026-10-28 at 22:21 the author asked, verbatim: "By the way, how will we structure the deterministic machinery? How
will the DDL files for the tables be generated? How do we generate the load scripts? Will it all be SQL files in a
folder structure? (this seems to me to be the lightest approach, and also most accessible to LLMs). How will we
orchestrate and execute?"

Already decided: DuckDB and a dbt-core project, run by a pinned runner under Task Scheduler that lands each complete
extract and runs `dbt build`, publishing the warehouse only after a successful load
([ADR-0015](0015-sandbox-warehouse-dbt-duckdb.md)); the model held as text declarations, with everything mechanical
generated and never edited ([142](../10_architecture/142_the-data-model.md) §3); hash keys
([ADR-0030](0030-hub-and-link-keys-are-hash-keys.md)). The runner refuses Python models and dbt packages, so that it
runs no code but the project's SQL (ADR-0015; `prototypes/wwi_sandbox/runner.py`).

The model answered with an outline, and the author replied on 2026-10-29 at 11:04, verbatim: "The generator etc is
fine, let's go with step C."

## Options considered

*Hand-written SQL.* Rejected by 142: the generated layers are where modelling tools accumulate ballast.

*dbt macros from a Data Vault package (such as automate_dv).* Its case: patterns maintained by others. Not available:
the runner refuses dbt packages by design, and macros hide the SQL that a reader, person or model, needs to see.

*A generator of our own writing plain SQL files.* Adopted.

## Decision

1. **Three layers, all text in git**: declarations (one small file per hub, link and satellite, holding only the
   decisions); a deterministic generator in the repository that reads the declarations and SQL templates; and the
   generated SQL, committed, so that every model change appears as a diff.
2. **The generated SQL is a set of dbt models in a folder structure** (raw vault hubs, links and satellites, business
   vault, marts), each file complete and readable on its own, headed with the declaration and generator version it came
   from and "do not edit". The generator writes full SQL rather than calls to macros.
3. **No separate DDL files**: dbt creates each table from its model; the raw vault is append-only (incremental), the
   business vault and marts are rebuilt; column names and types are fixed by explicit casts and may be enforced by
   dbt's model contracts.
4. **The load scripts are those models**, written by the generator from the standard Data Vault 2.0 patterns.
5. **Orchestration stays with the runner and dbt**: the runner triggers a build per complete extract; dbt orders the
   models by their dependencies and runs the tests in the same build; a load is published only when whole.
6. **The generator is run by a person or the agent layer, never by the runner.**

## Consequences

The declaration format and the generator remain to be designed (`ARC-OP-29`, `ARC-OP-20`), after the satellites
(step C), which decide much of what a declaration must hold.

The Python calculation engines of [ADR-0024](0024-calculation-engines-are-a-versioned-source.md) do not fit a runner
that refuses Python; they need a pinned step of their own, installed by the author's setup. The first day's load of the
source's history tables is a pattern of its own (ADR-0027 decision 2).

This decision is unreviewed on another model. **Revisit** if generated files become too many to review as diffs, or if
dbt's handling of append-only models proves unable to carry the patterns.
