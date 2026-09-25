# 128 — Join knowledge: which tables join, how, and with what risk

Part of the context system described in [120_context-layer.md](120_context-layer.md). Drafted
2026-09-25, session 04, from the author's point, verbatim:

> Also we need to record somewhere what tables are joinable, join risks, cardinality,
> referential integrity etc. Maybe also under knowledge. Cardinality being one of the most
> important, this is not always implemented 'hard'.

Revised the same day after external review on gpt-5.6-sol, recorded in
[XREV_2026-09-25_context-system_sol](../30_research/notes/XREV_2026-09-25_context-system_sol.md)
Q1, which added grain and population, split the declared layer, added key roles, specified
referential integrity properly and required query-level tests. The author's point is
practitioner input and unsourced under [AGENTS.md](../../AGENTS.md) rule 8. Nothing here is
built.

## Why it matters

A wrong join is the classic silent error in BI. Join an order table to a customer table
expecting one customer per order, meet the order that has two, and every revenue figure built on
that join is overstated — without an error message anywhere. Cardinality, the author's first
point, is what prevents this, and it is exactly the property sources rarely enforce.

## Joins get their own card

Join knowledge is about a *pair* of objects, not about one, so it should have its own card kind:
a **relationship** card, alongside the kinds in [120](120_context-layer.md). A relationship card
holds:

- **the join** — the columns on each side, including any normalisation needed (trimming, case,
  type casts, leading zeros), and who owns that normalisation;
- **grain and population** — below;
- **cardinality** — below, in layers;
- **key roles** — below;
- **optionality** — can a child exist without a parent, can a parent have no children;
- **referential integrity** — below;
- **temporal validity** — whether the join must be *as of* a date because one or both sides keep
  history ([127_temporal-behaviour.md](127_temporal-behaviour.md));
- **risks**, and the **tests** that guard against them;
- **for cross-source matches** (row 9 of [070](../00_concept/070_task-allocation.md)) — the
  matching rule and its measured quality.

## Grain and population come first

Cardinality is not an unconditional property of two tables. It depends on the **grain** of each
side, on **filters** (tenant, source, status), and on the **time window**. Profiling an
unfiltered pair can hide fan-out that appears within one tenant, or invent fan-out that no real
query would see.

So every relationship card states:

- the **grain** of both sides — what one row represents;
- the **direction and purpose** of the join — what question it serves;
- the **population predicates** under which the recorded cardinality holds;
- the **measure** whose aggregate must stay unchanged by the join — the thing the join must not
  multiply.

## Cardinality in layers

Because cardinality is so seldom enforced, it is recorded in layers that can disagree:

| Layer | What it records | Weakness |
|---|---|---|
| **Declared uniqueness** | A primary-key or unique constraint in the source — this is what supplies the *one* side | Often absent; may be disabled, unvalidated, partial or limited by a condition |
| **Declared inclusion** | A foreign-key constraint — every child value exists in the parent | Declares *inclusion*, not cardinality; same enforcement caveats |
| **Observed** | What the data shows: multiplicity **in both directions**, with counts of violations, the maximum multiplicity found, the population measured, and when | Can be coincidence; a relationship that *happens* to be one-to-many today may allow many-to-many tomorrow |
| **Asserted** | What the business says it should be — proposed by the agentic layer, ruled by a person | Can be wrong about what the data actually does |

Each declared constraint also records its **enforcement state**: enforced; declared but not
validated; trusted but not enforced (`RELY`, `NOT ENFORCED`); disabled.

**Disagreement between the layers is the most valuable signal in the record.** Observed
many-to-many where the business asserts one-to-many is either a data-quality problem or a
misunderstood business rule, and either way it must be found before a mart is built on it.
Observed violations are kept as a history, not overwritten by the latest measurement, because
violations often appear only after months.

This connects to `ARC-OP-22`. When a mart declares a key constraint with `RELY` so the engine can
skip joins, it hands the engine an *asserted* cardinality that the engine will not check. The
relationship card is where that assertion, its evidence and its tests live.

## Key roles

"Key" means several different things in a Data Vault and dimensional landscape, and joining on
the wrong one is a common way to multiply measures. Each key column records its **role**:

| Role | What it is |
|---|---|
| **Business key** | The identifier the business uses: customer number, IBAN, product code |
| **Source-qualified key** | A business key made unique by adding its source or namespace |
| **Hash key** | The vault's computed key for a hub or link |
| **Surrogate key** | A warehouse-generated key, typically for a dimension row |
| **Version key** | The key of one historical version in a type 2 dimension |

It also records its **namespace**, its **components** if composite, who owns its
**normalisation**, and — for historised tables — the **point-in-time rule** or the rule for
resolving to the right surrogate.

The canonical failure: a fact joined to a type 2 dimension on the **business key** matches every
historical version of that customer and multiplies the measures. The correct join resolves the
version valid at the fact's date, or uses the surrogate key assigned at load.

## Referential integrity

A single orphan rate is not enough; its meaning depends on choices that must be explicit:

- **direction** — children without parents, and parents without children, measured separately;
- **the denominator** — orphans as a share of what;
- **nulls** — whether a null reference counts as an orphan or as *not applicable*;
- **late arrival** — a grace window within which a missing parent is expected to arrive;
- **deletes** — whether a parent deleted after the child arrived counts;
- **unknown members** — rows deliberately pointed at an *unknown* dimension member;
- **temporal validity** — whether the parent existed at the child's date.

Counts are kept **segmented** — by source, tenant or period — alongside the overall rate,
because one average can hide a failure concentrated in the partition that matters most.

## Join risks worth recording

- **Fan-out** — a one-to-many join that multiplies the measures on the *one* side
  (double-counting).
- **Fan and chasm traps** — two one-to-many paths from the same table, combined in one query,
  producing inflated totals.
- **Many-to-many** — needs a bridge table and an allocation or weighting decision, which is a
  human decision.
- **Filtering side effects** — an inner join silently drops orphans; an outer join keeps them with
  nulls.
- **Time mismatch** — joining a current value to a historical fact gives *as-is* answers to an
  *as-was* question.
- **Key reuse** — a recycled identifier joins today's customer to last year's orders.
- **Wrong key role** — joining on the business key where the version or surrogate key was meant.

## Tests before use

A person approving a cardinality, plus row-level tests, is not enough: a reviewer can approve a
plausible cardinality while missing the grain, and a passing row-level test still allows fan or
chasm inflation across a query that combines several joins.

So before a relationship may be used to build marts, deterministic machinery runs
**query-level tests with representative measures**:

- **row-count preservation** — the join does not change the number of rows on the side whose
  grain must be kept;
- **aggregate reconciliation** — the recorded invariant measure totals the same before and after
  the join;
- **bridge-weight totals** — allocation weights on a bridge sum to one per member;
- **multi-path fan-out checks** — queries combining several relationships do not inflate totals.

These then run as **standing tests** on every load (row 22 of 070), and a failure is drift for
gardening ([126_context-gardening.md](126_context-gardening.md)).

## Finding which tables join

Most pairs of tables in a landscape do not join, so candidate pairs have to be found first.
Deterministic machinery computes the evidence: key-like columns, value overlap (the share of one
column's values found in another), and existing lineage. Query logs, where available, show the
joins people already trust (`EVI-OP-3`). The agentic layer ranks the candidates and drafts
relationship cards; a person rules on the intended cardinality where it is not obvious.

## Where it is recorded

Relationship cards hold the knowledge, with evidence snapshots; the observed statistics and
their history stay in the landscape-facts store and are summarised on the card; the tests are
generated code. `ARC-OP-27` holds what is open.
