# Architecture decision records

A decision that shapes the system goes here. A document elsewhere in `docs/` may
describe options; only an ADR adopts one.

## Rules

- Sequential four-digit numbers. Never reuse, never renumber.
- Status is one of `Proposed`, `Accepted`, `Superseded by ADR-NNNN`, `Rejected`.
- Superseded records stay in place. The history of what was believed is part of the
  record.
- Copy [`0000-template.md`](0000-template.md) to start.

## Index

| ADR | Title | Status |
| --- | --- | --- |
| [0001](0001-record-architecture-decisions.md) | Record architecture decisions | Accepted |
| [0002](0002-repository-layout.md) | Repository layout and documentation conventions | Accepted |
| [0003](0003-codename-nsdn.md) | Internal codename `nsdn`; metaphor stays private | Accepted |
| [0004](0004-models-out-of-the-data-path.md) | Models never operate in the data path | Accepted |
| [0005](0005-three-autonomy-tiers.md) | Autonomy is tiered: structural, semantic, teleological | Accepted |
| [0006](0006-project-mode.md) | Project mode: argument, then proof of concept, then offering | Accepted |
| [0007](0007-register-and-handover-apparatus.md) | Adopt the register, handover and enforcement apparatus | Accepted |
| [0008](0008-faculties-substrate-mandate.md) | Three faculties act on a substrate, each under a mandate | Accepted |
| [0009](0009-separate-capabilities-open-value-areas.md) | Separate capabilities, an open list of value areas, and no interaction owed | Accepted |
| [0010](0010-the-agentic-layer.md) | The second faculty is the agentic layer | Accepted |
| [0011](0011-assertions-identity-plane-publication-gate.md) | Assertions are the core record; one identity plane over separate stores; a publication gate | Accepted |
| [0012](0012-generic-framework-lean-start.md) | A generic framework; every implementation starts lean | Accepted |
| [0013](0013-data-vault-or-equivalent.md) | The integration layer is Data Vault or a functionally equivalent layer | Accepted |
| [0014](0014-step-log.md) | Record every step of the work in a classified step log | Accepted |
| [0015](0015-sandbox-warehouse-dbt-duckdb.md) | The Wide World Importers sandbox's warehouse is DuckDB, transformed with dbt-core | Accepted |
| [0016](0016-regulatory-requirements-from-production.md) | Regulatory requirements are kept in mind from the start and apply from production | Accepted |
| [0017](0017-information-analysis-before-building.md) | Information analysis precedes building: hard effort on a minimum, best effort on the rest, never a hard gate | Accepted (amended by 0018) |
| [0018](0018-information-analysis-record.md) | The information-analysis record: a folder per table and per column, a file per item, a line per claim, content-addressed evidence and provenance in every file | Accepted (amended by 0019) |
| [0019](0019-information-analysis-in-two-rounds.md) | Information analysis in two rounds: each table first, then what lies between tables | Accepted |
| [0020](0020-analysis-describes-the-as-is.md) | While in the analysis stage, the analysis describes the as-is and does not look ahead | Accepted (amended by 0022) |
| [0021](0021-position-in-the-schema.md) | Position in the schema is inventoried: measured on the declared keys, checked for distortion, classed by rules | Accepted |
| [0022](0022-the-analysis-stage-closes.md) | The analysis stage of the first trial closes; its record stays a description of the as-is and stays open | Accepted |
| [0023](0023-domain-knowledge-folder.md) | Domain knowledge lives in `docs/60_domain-knowledge/`, one subfolder per industry | Accepted |
| [0024](0024-calculation-engines-are-a-versioned-source.md) | Business rules and calculations run in versioned calculation engines whose results are a source | Accepted (amended by 0025) |
| [0025](0025-engine-results-in-the-raw-vault.md) | Engine results land in the raw vault; when full recomputation cannot be afforded, a cut-off date, then going forward only, by human adjudication | Accepted |
| [0026](0026-conformed-dimensions-and-fact-table-changes.md) | Marts share conformed dimensions; changing a fact table to serve a new question is a deliberate, adjudicated decision | Accepted |
| [0027](0027-bitemporal-integration-layer.md) | The integration layer is bitemporal on evidence, with source system time kept as a labelled third timestamp | Accepted |
| [0028](0028-wwi-country-key-milestones-and-sensors.md) | Wide World Importers: the country is keyed on ISO 3166-1; existence is dated by the event and each milestone is a satellite of its own; the sensor tables as proposed | Accepted |
| [0029](0029-wwi-step-a-concepts-and-keys.md) | Wide World Importers, step A: the hubs, business keys and business time of note 147 | Accepted |
| [0030](0030-hub-and-link-keys-are-hash-keys.md) | Hubs and links are keyed on hash keys computed from the key-space code and the business key | Accepted |
| [0031](0031-wwi-step-b-links.md) | Wide World Importers, step B: the links between the hubs of note 148 | Accepted |
| [0032](0032-generated-sql-machinery.md) | The deterministic machinery is generated plain SQL: declarations, a generator, and dbt models in folders | Accepted |
| [0033](0033-wwi-step-c-satellites.md) | Wide World Importers, step C: the satellites of note 149; password hashes are never loaded, their column kept empty | Accepted |
| [0034](0034-model-declaration-format-and-viewer.md) | The model is declared in small text files under `model/`, and viewed in a static page with no library | Accepted |
| [0035](0035-reference-case-and-client-repositories.md) | nsdn keeps Wide World Importers as its reference case; each client gets a repository of its own with a tagged release of nsdn | Accepted |
| [0036](0036-releases-and-upstream-notes.md) | nsdn travels to clients as numbered releases with release notes, and improvements come back as upstream notes without client material | Accepted |
