# ADR-0015 — The Wide World Importers sandbox's warehouse is DuckDB, transformed with dbt-core

- **Status:** Accepted
- **Date:** 2026-10-11
- **Supersedes:** —
- **Superseded by:** —

## Context

The Wide World Importers sandbox (`EVI-OP-7`, [420](../40_roadmap/420_next-sandbox-setup.md) §11) delivers a full
extract per simulated day into the repository's data folder. Nothing loads it yet, and
[AGENTS.md](../../AGENTS.md) forbids scaffolding code before an ADR adopts the thing being scaffolded.

On 2026-10-10 the author asked how the data manipulation, the DDL, the load scripts, the scheduling and the triggers on
change capture and file arrival would work. The model proposed an answer, recorded in
[420 §12](../40_roadmap/420_next-sandbox-setup.md). The constraints that are real: the machinery must keep running
without agents (420 §5, ruled 2026-10-07); the agent's shell on his computer exists only during a session and cannot
reach SQL Server; the Windows job is a pinned copy that only the author can replace; C: has about 4 GB free; and the
codebase is to be text files in git (`ARC-OP-20`, ruled 2026-10-07). Assumed, not verified: that DuckDB can confine a
process to one file and one folder, and that dbt-duckdb runs from a pinned runner under Task Scheduler.

`ARC-OP-20` asks that the principles be ratified before an execution engine and a declaration language are adopted,
each in its own ADR. This ADR does not do that for the framework. Under [ADR-0012](0012-generic-framework-lean-start.md)
the framework stays generic and every implementation starts lean; this is a choice for one sandbox implementation, made
by the author, and is not the framework's constitution.

## Options considered

*A second database in the author's SQL Server, loaded with generated T-SQL.* Its case: the server is installed and
running, the source is next to it, and nothing new is needed on Windows. Rejected because it costs disk that C: does not
have, and because the agent could reach it only through the request folder, never directly.

*A DuckDB file in the repository's ignored data folder.* Its case: no server, a single file of modest size, readable by
the agent from its Linux shell, and named in [180](../10_architecture/180_technology-posture.md) as the likely spine.
Adopted.

*Our own small runner with Jinja templates, instead of dbt.* Its case: leaner, one dependency fewer, and every line ours.
Rejected in favour of dbt, which brings dependency ordering, tests and a manifest with lineage, all as text files, and is
"boring and well documented" in 180's sense.

*dbt-core with dbt-duckdb.* Adopted, with the Data Vault patterns as small macros of our own; whether a package such as
datavault4dbt would serve better is to be looked at, not assumed.

## Decision

For the Wide World Importers sandbox, in the author's words of 2026-10-11: "let's go with dbt-core and dbt-duckdb", and,
on the engine, "agree with proposal".

**The warehouse is a DuckDB file** in the repository's ignored data folder, written on the Windows side and read by the
agent.

**Transformations are a dbt-core project with dbt-duckdb**, in the repository as text. DDL and load logic are generated
from declarations and templates, not written by hand; the raw vault is insert-only; the business vault and marts are
rebuilt on each run.

**A pinned runner under Task Scheduler** polls for complete extracts newer than the last load, and runs the dbt project
as it stands in the repository. The agent changes the project, never the runner. The runner is confined to the warehouse
file and to reading the extracts.

**No change gate in this sandbox**, on the author's ruling: "maybe postpone for now, just push all new SQL without gates".
The gates within a load (420 §12, D) and the runner's confinement stand.

## Consequences

The sandbox can now be built: the runner and its task in setup, the Windows installs that setup performs, and the first
dbt project. Setup must be rerun once by the author to install the runner; after that, changes to the SQL need nothing
from him.

Without a change gate, a broken change reaches the warehouse at the next load. That is accepted for a sandbox whose
warehouse can be rebuilt from the extracts; it would not be accepted for a client. `ARC-OP-33` stays open.

Postponed with it: the retention problem and the frozen regression copy (420 §12, G). Until they are fixed the agent
requests one simulated day at a time.

This choice is unreviewed on another model ([510](../50_process/510_external-review.md)).

**Revisit** if DuckDB cannot be confined as assumed, if the warehouse outgrows the disk, when the framework's own
engine and declaration language are settled under `ARC-OP-20`, or before any use outside a sandbox, where the change gate
returns.
