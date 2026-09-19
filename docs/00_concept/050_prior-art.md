# 050 — Prior art

A register of work this project should not reinvent, and of the specific gap it claims
to fill. Entries are stubs to be filled in during Phase 0; each should end with a
one-line verdict — *adopt*, *learn from*, or *distinguish from*.

> Nothing in this file has been verified yet. Treat every entry as a lead, not a fact.
> Per [`../../AGENTS.md`](../../AGENTS.md) rule 8, add a source when you fill one in.

## Catalogue and discovery

- OpenMetadata, DataHub, Amundsen — open-source catalogues with crawler/ingestion
  frameworks. The connector layer is likely worth adopting outright rather than rebuilt.
- Apache Atlas; Collibra, Alation, Microsoft Purview on the commercial side.

## Automated modelling

- AutomateDV (formerly dbtvault), Datavault Builder, WhereScape — Data Vault generation
  from declared metadata. These solve the generation problem; they do not solve the
  *declaration* problem, which is where this project claims its contribution.
- dbt-core as the deterministic execution substrate.

## Profiling and matching

- Schema-matching and entity-resolution literature (COMA, Valentine benchmark, and the
  broader record-linkage tradition). Decades of work on exactly the joinability problem;
  the question worth answering is how much a language model adds on top of these
  signals rather than in place of them.
- Sketch-based overlap estimation: HyperLogLog, MinHash/LSH, for cheap cross-source
  candidate generation.

## Quality and testing

- Great Expectations, Soda Core, dbt tests, Elementary — data-quality contracts.
- OpenLineage / Marquez — lineage as an interchange standard.

## Semantic layers

- dbt Semantic Layer / MetricFlow, Cube — versioned metric definitions, which is the
  prerequisite for semantic regression detection.

## Automated analysis

- The automated-insight tradition (Power BI Quick Insights, Tableau Explain Data,
  Google Sheets Explore, and the academic work on interestingness measures). The
  consistent lesson is that statistical surprise is a poor proxy for relevance. Worth
  reading specifically for its failure modes.

## Agentic data engineering

- Recent agentic text-to-SQL and pipeline-generation work. Moves quickly; verify
  currency before citing.

## The claimed gap

Existing tools automate *generation* given declared semantics, or *documentation* given
generated artifacts. The proposition here is that the declaration itself — business
keys, entity identity, relevance — can be substantially machine-produced and
human-adjudicated, and that the resulting context layer is the product rather than a
by-product. Whether that gap is real is the first thing this register should test.
