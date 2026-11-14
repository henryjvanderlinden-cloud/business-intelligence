# 010 — The capability inventory: what an enterprise-grade environment provides, and where nsdn stands

**Status: written 2026-11-14, session 12, by Claude Fable 5.2; unreviewed.** This is the question side of the
[equivalence investigation](README.md). It answers nothing; candidates are in the files from 020 on.

**Provenance.** The lines headed *Suites* come from the model's general knowledge of ETL and data-platform products
(PowerCenter, SSIS and Azure Databricks were the author's examples) and were not checked against current product
versions: by rule 8 of [`AGENTS.md`](../../../AGENTS.md) they are hypotheses. The lines headed *nsdn today* describe
the repository at commit `01b5092` and are taken from
[the sandbox's README](../../../prototypes/wwi_sandbox/README.md),
[the generator's README](../../../prototypes/vault_generator/README.md) and the documents linked. The lines headed
*Asked* are the research questions. The lines headed *First thought* are the model's and are not ruled.

**Added 2026-11-14, after [ADR-0038](../../20_decisions/0038-etl-capability-equivalence-investigation.md).** This file is
step 1 of the ruled method, the gaps. The words *delegate* and *decline* in the first thoughts come from the model's
first proposal, which the ADR did not adopt; read them as what a later judgement might come to.

The numbers are permanent. The author's own five observations are quoted in the [README](README.md).

## The thirteen capabilities

### 1. Connectivity

- *Suites.* Maintained connectors for ERP systems, SaaS applications, APIs, mainframes and file formats, with
  authentication, paging and rate limits handled.
- *nsdn today.* One export job for SQL Server on the author's machine, driven by request files, and a catalogue pass
  that reads a PostgreSQL catalogue without reading rows ([catalogue pass](../../../prototypes/catalogue_pass/README.md)).
- *Asked.* How does data from an arbitrary source land as dated, complete, checksummed extracts without a connector
  written by hand for each source?
- *First thought.* The largest real gap. A separate extraction part, replaceable, that delivers into the landing
  contract the runner already checks.

### 2. Incremental capture

- *Suites.* Change data capture from the database log, watermarks, detection of deletions.
- *nsdn today.* A full extract of every table for every day; a deletion is seen as absence from a complete extract.
- *Asked.* How are changes captured from a large production source without reading all of it every day, and how is a
  deletion still seen?
- *First thought.* Does not scale as it is. The vault's load pattern already takes versions in source order, so a
  change feed could fit it; that is untested.

### 3. Orchestration

- *Suites.* Dependencies across sources, calendars, retries, restart from the point of failure, backfills, deadlines.
- *nsdn today.* `runner.py` as a scheduled task: one extract at a time, oldest first, never past a failed or missing
  date; dbt orders the models; a failed date is retried when the project or the extract changes. One source.
- *Asked.* What orders and restarts the work once there are several sources with different rhythms?
- *First thought.* Enough for one source. [180](../../10_architecture/180_technology-posture.md) deferred
  orchestration on purpose; the question is when that stops holding.

### 4. Scale

- *Suites.* Parallel or distributed execution, bulk loaders, partitioning.
- *nsdn today.* DuckDB in one file on one machine, one thread
  ([`profiles.yml`](../../../prototypes/wwi_sandbox/profiles/profiles.yml)). A daily load of the sandbox takes 572
  seconds on the author's machine (S12-027).
- *Asked.* Up to what volume does one machine hold, and what happens above it?
- *First thought.* Fine for mid-size. Above it the generated SQL would be written for another engine and not stretched;
  [ADR-0037](../../20_decisions/0037-vault-generator.md) already names slow loads as a reason to revisit.

### 5. Operations console

- *Suites.* Run history, alerting, and a way to rerun for an operator who did not build the thing.
- *nsdn today.* `status.json`, alert files, a load log in the warehouse and a text log. No page, no notification.
- *Asked.* How does someone who is neither the author nor the agent see what ran, what failed and what is late, and
  act on it?
- *First thought.* Needed for the rule that the machinery works with the agent layer down. A static page built from
  the load log, in the manner of the [schema viewer](../../../prototypes/schema_viewer/build.py), may be enough.

### 6. Security administration

- *Suites.* Integration with the directory (AD), roles, a secrets vault, an audit trail of who ran and changed what.
- *nsdn today.* A read-only database user for extraction; scheduled tasks under the author's account; DuckDB confined
  to its own file ([ADR-0015](../../20_decisions/0015-sandbox-warehouse-dbt-duckdb.md)); a sensitivity class on every
  satellite ([149](../../10_architecture/149_wwi-satellites.md) Rule 9) with no access rule per class yet; password
  hashes never loaded ([ADR-0033](../../20_decisions/0033-wwi-step-c-satellites.md)).
- *Asked.* Who may read what, how is that enforced, and where are credentials kept?
- *First thought.* The author is right that the suites are better here. Delegate to the platform and do not rebuild
  it. DuckDB as used here, in process on one file, has no users or roles of its own, so access per class cannot be
  enforced inside that file; see [020](020_databricks-anatomy.md) §4 for what was found on this.

### 7. Environments and promotion (DTAP)

- *Suites.* Separate environments, parameters per environment, approvals, rollback.
- *nsdn today.* One environment. The runner builds the dbt project as it stands in the repository, so new SQL is live
  within a minute, with no change gate (the author's ruling of 2026-10-11). Releases by tag are ruled in
  [ADR-0036](../../20_decisions/0036-releases-and-upstream-notes.md) and none exists.
- *Asked.* How does a change travel from development to production, who approves it, and how is it taken back?
- *First thought.* Not built, but text in git with tags can do this better than most suites. Related to the gates of
  `ARC-OP-33` and the release regression of `ARC-OP-30`.

### 8. Lineage and impact

- *Suites.* Column lineage inside the tool.
- *nsdn today.* Every one of the 368 source columns is placed exactly once in the declarations, and the checker
  refuses a forgotten one ([`model/README.md`](../../../model/README.md)); dbt knows the order of the models. Nothing
  beyond the raw vault.
- *Asked.* Can a figure in a mart be traced to its source columns, and a source change to the figures it touches?
- *First thought.* Already stronger than the suites as far as the raw vault; the question is keeping it through the
  business vault and the marts (`ARC-OP-37`).

### 9. Data quality handling

- *Suites.* Rules, rejected rows routed to error tables, thresholds.
- *nsdn today.* 777 generated tests per load, each pass or fail for the whole batch; nothing is published from a
  failed build. No handling of single rejected rows. The gate catalogue is open (`ARC-OP-33`), plausibility checks are
  drafted (`ARC-OP-31`).
- *Asked.* What happens to a row that is wrong, as distinct from a batch that is wrong?
- *First thought.* Matters less in a raw vault, which keeps what was delivered. It will matter at the business vault.

### 10. Recoverability

- *Suites.* Atomic batches, checkpoints.
- *nsdn today.* Tested: loading an extract twice changes nothing, a failed batch leaves nothing after its retry, the
  published copy is replaced only after a successful load, and every delivered version can be rebuilt from the
  satellites.
- *Asked.* None at present.
- *First thought.* Strong. Listed so that the inventory also shows what is not a gap.

### 11. Schema drift

- *Suites.* Some evolve the target automatically.
- *nsdn today.* A changed source schema fails the load (`on_schema_change='fail'`), and the checker shows the column
  that is missing or new.
- *Asked.* Who regenerates after a source change, and how long may the load stand still meanwhile?
- *First thought.* Failing loudly fits the design. It needs a person or the agent layer to act, which is a question of
  capability 5 as much as of this one.

### 12. Odd formats and streaming

- *Suites.* Excel, XML, EDI, message queues, real time.
- *nsdn today.* Batch files only.
- *Asked.* Which formats must be read, and is anything faster than a daily batch ever in scope?
- *First thought.* Formats are ordinary Python work. Streaming is a different architecture and a candidate for
  *decline*.

### 13. Acceptance

- *Suites.* Vendor support, certifications, staff and auditors who know the tool.
- *nsdn today.* None. Regulatory requirements apply from production
  ([ADR-0016](../../20_decisions/0016-regulatory-requirements-from-production.md)).
- *Asked.* What does a client's IT department, security officer or auditor need to see before this may run in
  production?
- *First thought.* Not a function, but often what decides. An answer is documents and evidence more than software.

## Four findings that go with the list

1. **The design overview and the operational overview are two things.** The author finds that the suites do not help
   him keep *overzicht*. For the design that holds, and declarations with a viewer do better. What ran, what failed
   and what is late is another overview, and there the consoles do help (capability 5).
2. **A generator collects edge cases too.** His experience is that the suites meet their limits quickly and need
   workarounds. The generator already stops on a pattern it does not support
   ([143](../../10_architecture/143_the-vault-generator.md) §4). Stopping and never guessing is the guard, and it
   needs keeping as the generator grows.
3. **Databricks is not in one class with PowerCenter and SSIS.** It is an engine with code in git, so generated SQL
   could run on it. It is a possible target as well as a comparison.
4. **Do not build these.** For capabilities 1, 2, 5 and 6 the lightweight answer is a small part or a platform feature
   kept outside the transformation logic, which stays generated SQL.
