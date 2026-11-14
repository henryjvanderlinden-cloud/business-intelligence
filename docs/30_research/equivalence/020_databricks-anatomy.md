# 020 — What Databricks is made of, and what it suggests

**Status: written 2026-11-14, session 12, by Claude Fable 5.2; unreviewed.** This is the first file on the answer side
of the [equivalence investigation](README.md). It asks what the open-source parts of Databricks are, which of the
thirteen capabilities of [010](010_capability-inventory.md) each one answers, and what nsdn can take from the way they
are put together. The author raised it on 2026-11-14: Databricks "is made up of several open source projects. Maybe we
could also draw some inspiration from that."

**Provenance.** Every statement about Databricks or DuckDB below rests on the web sources listed in §5, found on
2026-11-14 and read as search extracts, not as whole pages. Most are Databricks' own pages, so they show how the
company describes itself. A statement marked **(unverified)** is from the model's general knowledge. Verify before
relying on any of it.

## 1. The parts

| Part | Open or managed | What it does | Capability in 010 | Nearest thing in nsdn today |
|---|---|---|---|---|
| Apache Spark | open, Apache Software Foundation | the execution engine | 4 | DuckDB |
| Delta Lake | open, Linux Foundation | table format on object storage, with transactions and versions | 10 | one DuckDB file, an append-only vault, publish by copy |
| Unity Catalog | open since June 2024 (Apache 2.0), also sold managed | catalogue, permissions, lineage | 6, 8 | the declarations and the analysis record; no permissions |
| Spark Declarative Pipelines | open, part of Apache Spark 4.1; given by Databricks in June 2025, formerly Delta Live Tables | tables and flows are declared, the engine plans and runs them | 3, 9 | declarations, the generator, dbt |
| Delta Sharing | open protocol | sharing tables with other parties | none | none |
| MLflow | open, Linux Foundation | the machine-learning life cycle | none | none |
| Lakeflow Connect | managed; over 100 connectors, with change capture; community connectors are open source and carry no service level | ingestion | 1, 2 | the SQL Server export job |
| Lakeflow Jobs | managed; formerly Databricks Workflows | orchestration and monitoring | 3, 5 | `runner.py` |
| Workspace, serverless compute, the Photon engine | managed **(unverified)** | console, deployment, faster execution | 4, 5, 7 | none |

Databricks also reads and writes Apache Iceberg and says no proprietary storage format is required.

## 2. What the anatomy shows

1. **What is sold on top of the open parts is close to the list of gaps.** The open parts cover storage, the engine,
   the catalogue and the way pipelines are declared. The managed parts are connectors, orchestration, the console and
   compute: capabilities 1, 2, 3, 5 and 7. That is where nsdn is thin as well, which suggests these are the parts that
   take sustained work and not design.
2. **It is a composition, not a suite.** Single-purpose parts meet in open formats and one catalogue. That is the
   pattern nsdn already follows at small scale (text declarations, generated SQL, dbt, DuckDB) and an argument for
   answering each capability with a small part of its own.
3. **The industry is moving to declarations.** With Spark Declarative Pipelines the user states what the tables should
   be and the engine works out how. nsdn goes a step further up: it declares the model (hubs, links, satellites) and
   generates the pipeline from it ([ADR-0032](../../20_decisions/0032-generated-sql-machinery.md)).
4. **The catalogue is the hinge.** In Databricks, permissions and lineage hang on one catalogue. nsdn has the lineage
   half in its declarations and has no home for the permission half (capability 6). Whether the declarations should
   carry who may read what, with the platform enforcing it, is a question for 010 capability 6.

## 3. What not to take from it

The parts are sized for clusters. Running Spark or a catalogue server for a mid-size client would go against the four
properties of [180](../../10_architecture/180_technology-posture.md). The inspiration is the architecture, not the
components. Where a client already runs Databricks, the outcome for capability 4 may be *delegate*: the generator
writes for that engine.

## 4. DuckDB and access, found while checking capability 6

DuckDB's own guide on securing it points to the operating system, containers and its configuration options, which is
how the sandbox's profile confines it; it describes no roles inside a database file. Three things turned up that could
serve as the enforcing layer, none of them evaluated: an authentication and authorisation hook in DuckDB's client-server
protocol (documented under the name Quack), DuckLake with its catalogue in PostgreSQL and roles there, and
MotherDuck's role-based access control. DuckDB can also read Delta tables through an extension. These are leads.

## 5. Sources

Found 2026-11-14; extracts only.

- Databricks, "Open source": <https://www.databricks.com/product/open-source> (the open projects).
- Databricks, `llms.txt`: <https://www.databricks.com/llms.txt> (which foundation hosts which project; Apache 2.0;
  Iceberg; no proprietary format required).
- Databricks, press release on Unity Catalog, 2024:
  <https://www.databricks.com/company/newsroom/press-releases/databricks-open-sources-unity-catalog-creating-industrys-only-open>
  (also the DuckDB Delta extension).
- Databricks, press release of 2025-06-11 on Declarative Pipelines:
  <https://www.databricks.com/company/newsroom/press-releases/databricks-donates-declarative-pipelines-apache-sparktm-open-source>.
- Databricks, "How to get started with Spark Declarative Pipelines":
  <https://www.databricks.com/discover/how-to-get-started-with-spark-declarative-pipelines> (in Apache Spark 4.1;
  formerly Delta Live Tables; Lakeflow as the managed version).
- VentureBeat on the same announcement:
  <https://venturebeat.com/ai/databricks-open-sources-declarative-etl-framework-powering-90-faster-pipeline-builds>
  (the commercial version carries further enterprise features).
- Databricks documentation, "What is Lakeflow Connect?": <https://docs.databricks.com/ingestion/overview> (managed,
  community and custom connectors).
- Databricks, "Lakeflow: a new era of agentic data engineering":
  <https://www.databricks.com/blog/lakeflow-new-era-agentic-data-engineering> (more than 100 managed connectors).
- Databricks, "What's new: Lakeflow Jobs", 2025-07-24:
  <https://databricks.com/blog/whats-new-lakeflow-jobs-provides-more-efficient-data-orchestration> (formerly Databricks
  Workflows).
- DuckDB, "Securing DuckDB": <https://duckdb.org/docs/stable/operations_manual/securing_duckdb/overview>.
- DuckDB, Quack security: <https://duckdb.org/docs/1.5/quack/security>.
- DuckLake, access control guide: <https://www.ducklake.select/docs/stable/duckdb/guides/access_control>.
- MotherDuck, security and access: <https://motherduck.com/docs/category/security-and-access/>.

## 6. Other leads, unverified

Named in conversation on 2026-11-14 as examples and not looked at: dlt and Airbyte for extraction, Debezium for change
capture from a database log. 180 names Dagster and Airflow for orchestration and defers them.
