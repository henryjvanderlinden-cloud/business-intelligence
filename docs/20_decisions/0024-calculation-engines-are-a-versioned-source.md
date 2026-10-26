# ADR-0024 — Business rules and calculations run in versioned calculation engines whose results are a source

- **Status:** Accepted
- **Date:** 2026-10-26
- **Supersedes:** —
- **Superseded by:** —
- **Amended by:** [ADR-0025](0025-engine-results-in-the-raw-vault.md) (where engine results land; the fallback
  left open in decision 4)

## Context

Handover 09 put to the author, as decision 2 of the design of the generic integration layer, how derived measures and
calculations are handled. The analysis record shows why the question matters for Wide World Importers: an order's
value is stored nowhere (`analysis/wwi/tables/Sales/OrderLines/08_measures.md#C6`), invoice tax is rounded half up per
line (`analysis/wwi/tables/Sales/InvoiceLines/09_derived.md#C1`), and `LineProfit` follows the cost price as it stands
in the extract (`#C3`). The model had offered three options: keep the source's values and calculate later; the same
plus one register of calculations, defined once with rounding and version and reconciled to the source's own figures;
or recompute everything and distrust the source's computed columns. It leaned to the second.

On 2026-10-26 at 08:46 the author answered with a design of his own, verbatim:

> Where do you place calculation engines? For any application of business rules and calculations (except for very
> basic addition and multiplication) I envisage to have calculation engines, which are more like software (think
> python programs) then doing it in SQL. The thing with calculation engines, is that they should have versioning, unit
> testing, inline documentation etc. I imagine building them with e.g. numpy and panda. If a calculation is performed,
> ideally it would store the value and the version of the calculation engine. I see this as a separate source. What do
> you thinkg?

The model agreed, placed the engines outside both vaults as deterministic machinery, proposed conditions, and put
three choices to him: the boundary between SQL and engine, what happens on a new version, and what happens when inputs
are corrected. He answered at 08:58, verbatim:

> 13. Agree
> 14. I think the uncomfortable answer is: it depends. If we have enough compute (and storage), I'd recompute
> everything, and using a bitemporal database structure, we can time travel. If the version changes, this means the
> data changes, even if the outcome is the same.
> 15. same, also use the bi-temporality and just rerun.

Point 13 agreed to this boundary, as the model proposed it: "anything with a rounding decision, a condition that
carries business meaning, an allocation, or logic over time goes to an engine", with the example that even an order's
value goes to an engine because of the rounding.

Real constraints: models stay out of the data path ([ADR-0004](0004-models-out-of-the-data-path.md)); the machinery
must keep working without the agent layer (420 §5, ruled 2026-10-07); the codebase is text in git (`ARC-OP-20`, ruled
2026-10-07); the sandbox's warehouse is DuckDB with dbt-core ([ADR-0015](0015-sandbox-warehouse-dbt-duckdb.md)).
Assumed and not verified: that Python engines can read from and write to the DuckDB warehouse within the runner's
confinement.

## Options considered

*Calculations in SQL, in the business vault, as dbt models.* Its case: one toolchain, set-based performance, dbt's
tests and its manifest's lineage, and nothing to run beside dbt. Rejected for anything beyond basic arithmetic: SQL is
poor at unit testing, versioning per rule and inline documentation, and business rules are where that discipline is
needed most.

*Compute on read, without storing results.* Its case: no storage, and always the latest logic. Rejected: it cannot
show what was reported, or with which logic, after the logic has changed.

*Calculation engines as versioned software whose results are stored as a source.* The author's design. Adopted.

## Decision

1. **Business rules and calculations are performed by calculation engines**: software, such as Python with numpy and
   pandas, with versioning, unit tests and inline documentation, and not SQL. SQL keeps joins, filters and basic
   addition and multiplication without a rounding decision. Anything with a rounding decision, a condition that carries
   business meaning, an allocation, or logic over time is an engine's.
2. **Every result is stored with the version of the engine that produced it.**
3. **The engines' output is a separate source** to the warehouse.
4. **On a new version, everything is recomputed** when compute and storage allow, and the bitemporal structure lets
   the warehouse travel back to any earlier state. **A new version is new data, even when its values are the same.**
   What is done when compute or storage do not allow full recomputation is left open: "it depends".
   *Ruled 2026-10-26 in [ADR-0025](0025-engine-results-in-the-raw-vault.md): first from a cut-off date, then going
   forward only, each step adjudicated by a person.*
5. **Corrected inputs are handled by rerunning**, using the same bitemporality.

## Consequences

Engine results are bitemporal: each has the period it describes and the time it was computed, and an earlier state is
reached by time travel rather than by keeping only the latest run. Change detection on engine results includes the
engine version, so a new version that reproduces the old values is still recorded as new.

Engines are deterministic code: agents may write and change them, but do not run in the data path, and the engines run
without agents. Their results are stored insert-only and are not rebuilt on each run; ADR-0015's rule that the business
vault and marts are rebuilt on each run continues to hold for what is built in SQL.

Full recomputation on every version costs compute and storage that grow with history; the fallback when they run short
is not decided.

Open, under [`ARC-OP-37`](../../registers/OPEN_POINTS.md) and drafted in
[144](../10_architecture/144_raw-vault-business-vault-calculation-engines.md) §4: whether engine results land in the
raw vault under the engine's own source code or in the business vault (the financial-services note
[030](../60_domain-knowledge/financial-services/030_bird-as-data-vault-foundation.md) §2 item 5 says the business
vault); what a version comprises (code and locked dependencies, as proposed); what each result row records of its
inputs; how money is represented; the order of the pipeline; and whether calculation runs get identity of their own.
Whether the integration layer as a whole is bitemporal is decision 1 of handover 09 and is not decided here.
*Since ruled in [ADR-0025](0025-engine-results-in-the-raw-vault.md): engine results land in the raw vault.*

This decision is unreviewed on another model ([510](../50_process/510_external-review.md)).

**Revisit** if engines cannot run within the runner's confinement, if full recomputation outgrows the sandbox's
compute or disk, or when the framework's execution engine is settled under `ARC-OP-20`.
