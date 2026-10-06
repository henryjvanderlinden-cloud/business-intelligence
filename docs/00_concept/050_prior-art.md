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
- **Open Knowledge Format (OKF)** — an open specification for knowledge about data, published by Google
  Cloud's data analytics team: a bundle is a directory of markdown files with YAML front matter, one concept
  per file, `type` the only required field, concepts linked by ordinary markdown links into a graph, with
  optional `index.md` and `log.md` files. Version 0.2 adds provenance (`sources`), trust (`generated` kept
  apart from `verified`, giving tiers of unverified, machine-confirmed and human-reviewed), lifecycle
  (`status`, `stale_after`) and an *Attested Computation* type whose computation an agent may parameterise
  but not author, checked by deterministic code. Apache 2.0. The same design as
  [120](../10_architecture/120_context-layer.md)'s cards in git, arrived at independently; it differs in
  taking the file path as identity where 120 uses URNs, in untyped links, and in keeping trust per concept
  rather than per assertion. *Verdict: learn from, and align field names; keep URN identity.* Whether to
  conform is `ARC-OP-32`. Sources: S. McVeety and A. Hormati, "Introducing the Open Knowledge Format,"
  Google Cloud blog, 12 June 2026,
  <https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing>;
  `okf/SPEC.md`, version 0.2, in <https://github.com/GoogleCloudPlatform/knowledge-catalog>, read at commit
  `85a2be8` on 2026-10-06.

## The limits of codification

- Michael Polanyi, *The Tacit Dimension* (1966) — "we can know more than we can tell."
  The origin of the articulability condition in
  [005_manifesto.md](005_manifesto.md) §III. *Verdict: cite.*
- David H. Autor, "Polanyi's Paradox and the Shape of Employment Growth," NBER Working
  Paper 20485 (2014) — tacitness as the binding constraint on automation, and the
  machine-learning-from-examples resolution. The nearest prior statement of this
  project's framing, and the thing `CON-OP-4` must distinguish itself from. *Verdict:
  cite, and state the difference — this project claims data work fails generality rather
  than articulability, which makes learning-from-examples the wrong remedy.* Confirmed
  bibliographically 2026-09-19; the argument has not been read in full.
- The wider codification / tacit-knowledge literature in knowledge management (Nonaka
  and Takeuchi and successors) is likely to contain adjacent claims and is unexamined.

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
