# 128 — Join knowledge: which tables join, how, and with what risk

Part of the context system described in [120_context-layer.md](120_context-layer.md). Drafted
2026-09-25, session 04, from the author's point, verbatim:

> Also we need to record somewhere what tables are joinable, join risks, cardinality,
> referential integrity etc. Maybe also under knowledge. Cardinality being one of the most
> important, this is not always implemented 'hard'.

This is practitioner input and unsourced under [AGENTS.md](../../AGENTS.md) rule 8. Nothing
here is built.

## Why it matters

A wrong join is the classic silent error in BI. Join an order table to a customer table
expecting one customer per order, meet the order that has two, and every revenue figure built
on that join is overstated — without an error message anywhere. Cardinality, the author's
first point, is what prevents this, and it is exactly the property sources rarely enforce.

## Joins get their own card

Join knowledge is about a *pair* of objects, not about one, so it should have its own card
kind: a **relationship** card, alongside the kinds listed in [120](120_context-layer.md). A
relationship card holds:

- **the join** — which columns on each side, including any transformation needed (trimming,
  case, type casts, leading zeros);
- **cardinality** — one-to-one, one-to-many, many-to-one or many-to-many — in three layers, below;
- **optionality** — can a child exist without a parent, can a parent have no children;
- **referential integrity** — the observed rate of orphans, and its trend;
- **key behaviour** — whether keys are unique over time, reused, null, or formatted
  inconsistently;
- **temporal validity** — whether the join must be *as of* a date, because one or both sides
  keep history ([127_temporal-behaviour.md](127_temporal-behaviour.md));
- **risks** — see below;
- **for cross-source matches** (row 9 of [070](../00_concept/070_task-allocation.md)) — the
  matching rule and its measured quality.

## Cardinality in three layers

Because cardinality is so seldom enforced, it has to be recorded in three separate layers,
which can disagree:

| Layer | What it is | Who produces it | Weakness |
|---|---|---|---|
| **Declared** | A constraint in the source database | The source system | Often absent, and absent entirely in files and data lakes |
| **Observed** | What the data shows today | Deterministic machinery, by profiling | Can be coincidence: a relationship that *happens* to be one-to-many today may allow many-to-many tomorrow |
| **Asserted** | What the business says it should be | A person rules; the agentic layer proposes | Can be wrong about what the data actually does |

**Disagreement between the layers is the most valuable signal in the record.** Observed
many-to-many where the business asserts one-to-many is either a data-quality problem or a
misunderstood business rule, and either way it must be found before a mart is built on it.

Observed cardinality also needs time: violations often appear only after months. So an
asserted cardinality should become a **standing test** (row 22 of 070) that deterministic
machinery runs on every load, and a violation becomes drift for gardening
([126_context-gardening.md](126_context-gardening.md)).

This connects to `ARC-OP-22`. When a mart declares a key constraint with `RELY` so the engine
can skip joins, it is handing the engine an *asserted* cardinality that the engine will not
check. The relationship card is where that assertion, its evidence and its test live.

## Join risks worth recording

- **Fan-out** — a one-to-many join that multiplies the measures on the *one* side
  (double-counting).
- **Fan and chasm traps** — two one-to-many paths from the same table, combined in one query,
  producing inflated totals.
- **Many-to-many** — needs a bridge table and an allocation or weighting decision, which is a
  human decision.
- **Filtering side effects** — an inner join silently drops orphans; an outer join keeps them
  with nulls.
- **Time mismatch** — joining a current value to a historical fact gives *as-is* answers to an
  *as-was* question.
- **Key reuse** — a recycled identifier joins today's customer to last year's orders.

## Finding which tables join

Most pairs of tables in a landscape do not join, so candidate pairs have to be found first.
Deterministic machinery computes the evidence: key-like columns, value overlap (the share of
one column's values found in another), and existing lineage. Query logs, where available, show
the joins people already trust (`EVI-OP-3`). The agentic layer ranks the candidates and drafts
relationship cards; a person rules on the intended cardinality where it is not obvious.

## Where it is recorded

Relationship cards hold the knowledge; the observed statistics stay in the landscape-facts
store and are summarised on the card; the tests are generated code. `ARC-OP-27` holds what is
open.
