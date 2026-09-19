# 180 — Technology posture

The brief asks for lightweight, open-source technology that language models can
maintain. That constraint deserves a precise reading, because "lightweight" is otherwise
just a preference.

> Nothing here is adopted. These are the candidates a Phase 0 evaluation should test;
> adoption happens in an ADR. Per [`../../AGENTS.md`](../../AGENTS.md) rule 8, verify
> currency before relying on any of it.

## What "maintainable by an LLM" actually means

Four properties, in order of importance.

**Declarative over imperative.** A model maintains a YAML model definition far more
reliably than it maintains a bespoke Python class hierarchy, because the former has a
schema to validate against and no hidden state. Prefer tools whose unit of work is a
file that describes an outcome.

**Regenerable.** If a component can be rebuilt from its declaration, a model breaking it
costs a rebuild rather than a debugging session. This is the strongest single argument
for a generate-everything architecture and it should be preserved even where hand-
writing would be more elegant.

**Small files, one concept each, stable identity.** Context-window economics at the code
level, mirroring [120_context-layer.md](120_context-layer.md) at the metadata level.

**Boring and well-documented.** Models are far more reliable on tools with a decade of
public examples than on whatever launched this quarter, and this consideration should
outrank technical superiority more often than an engineer would like.

## Candidates

**Analytic engine — DuckDB.** In-process, no infrastructure, reads Parquet and most
source formats directly, and fast enough that profiling and joinability work need no
cluster. Very likely the right spine for everything the system does locally, and
possibly for the warehouse itself at small and mid scale.

**SQL parsing — sqlglot.** Dialect-aware parsing and transpilation. Underrated and
close to essential: it is what makes it possible to read query logs, extract join
predicates and lineage from heterogeneous sources, and emit portable DDL. Much of the
key-hypothesis evidence in [140_data-vault-automation.md](140_data-vault-automation.md)
depends on being able to parse other people's SQL.

**Transformation — dbt-core.** Declarative, file-based, testable, universally
documented, and its manifest is itself a metadata source. Near-ideal fit for the four
properties above.

**Vault generation — AutomateDV**, or hand-rolled templates. Worth evaluating against
the cost of owning the templates directly; the generation problem is not the hard part,
so the deciding factor is which is easier to keep correct.

**Profiling and sketches — HyperLogLog and MinHash/LSH**, via `datasketches` or
equivalent. The mechanism that makes cross-source overlap estimable without centralising
data, which is what makes profiling affordable and, more importantly, permissible.

**Quality — dbt tests, Great Expectations or Soda Core.** Selection should follow from
how expectations are generated rather than from feature lists.

**Lineage — OpenLineage.** An interchange standard rather than a product, which suits a
system that will both consume and emit lineage.

**Orchestration — deliberately deferred.** The job queue in
[130_agent-loop.md](130_agent-loop.md) is simple enough that a database table and a
worker will do for a long time. Adopting Dagster or Airflow early buys operational
weight before there is anything to operate.

**Storage — Parquet, with Iceberg if table semantics become necessary.** Avoid until
needed.

**Presentation — Evidence or Streamlit.** Both are code-first and therefore generatable,
which matters more here than their visual ceiling.

**Catalogue — none initially.** The context layer is files (see
[120_context-layer.md](120_context-layer.md)). Existing catalogues are *sources* to read,
not substrates to adopt. Revisit if and when file count becomes the binding problem.

## Posture on models

No dependency on a single vendor. Jobs declare a capability requirement — cheap and
structural, or strong and semantic — and routing is configuration. Cross-model review
(see [130_agent-loop.md](130_agent-loop.md)) requires at least two vendors by
construction, which usefully forecloses lock-in as a side effect.
