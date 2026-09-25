# 122 — Context retrieval: recipes, facets and trust

Part of the context system described in [120_context-layer.md](120_context-layer.md). Drafted
2026-09-25, session 04, from a brainstorm with the author, and revised the same day after
external review on gpt-5.6-sol, recorded in
[XREV_2026-09-25_context-system_sol](../30_research/notes/XREV_2026-09-25_context-system_sol.md)
Q3. The review replaced the zoom levels with facets, single trust labels with claim-level
dimensions, and the efficiency measures with outcome measures. Nothing here is built;
everything is stated as what the system should do.

## The problem

The agentic layer starts cold on every task (dimension 7 of
[060_faculty-inventory.md](../00_concept/060_faculty-inventory.md)). It needs a lot of context
to be useful, but never all of it at once. Retrieval has to deliver the *right* context for the
task in hand, within a budget, and it has to say how far each piece can be trusted.

## Retrieval is shaped by the task

[070_task-allocation.md](../00_concept/070_task-allocation.md) lists the task types. Each type
needs a predictable core of context, so each should have a **context recipe**: a short,
versioned description of what to load, starting from which object, and at what level of
detail.

A recipe states:

- **the anchor** — the object the task is about, by its permanent identifier;
- **mandatory context** — what the task may not proceed without;
- **optional context** — what helps but can be dropped under budget pressure;
- **the facets** to load for each item (below);
- **a budget**, and what happens when it is exceeded;
- **acceptance rules** — which claims may be relied on for this task, by their trust
  dimensions (below);
- **what to write back** afterwards ([124_context-write-back.md](124_context-write-back.md)).

Example: *propose a business key for table X* (row 9 of 070). Mandatory: the table's card and
profile; its temporal behaviour ([127](127_temporal-behaviour.md)); known relationships and key
roles ([128](128_join-knowledge.md)). Optional: similar columns elsewhere, existing hub cards
for the likely entity, earlier rejected hypotheses, naming conventions for the source.

**Recipes compose, and risk adds to them.** Real work is compound: changing a dimension may
need security, regulatory, ownership, reconciliation, deployment and consumer-impact context
at once. So a task assembles its context from several recipes, and risk triggers add
mandatory items — for example, anything touching personal data adds the access and erasure
context of rows 36 and 37.

**Retrieval fails closed.** If a mandatory item is missing, or would be cut by the budget, the
task stops and says so. It never proceeds on a silently truncated context.

## Links, plus discovery

[120](120_context-layer.md) says "search is the entry point; traversal is the method". Traversal
alone assumes the graph is complete, and real landscapes are full of what nobody recorded:
undocumented reports, copied SQL, spreadsheets, cross-system dependencies. Following recorded
links will confidently miss exactly those.

So retrieval combines three means:

- **traversal** of recorded links from the anchor;
- **bounded search** for what the links do not reach;
- **discovery scans** — lineage parsing, query logs and reverse-dependency searches, run by
  deterministic machinery.

Every retrieval result states how complete the graph around the anchor is believed to be.

## Facets, not a single zoom hierarchy

Context comes in different facets, and a more detailed facet is not a substitute for a
different one:

| Facet | What it holds |
|---|---|
| **Summary** | the landscape map, source summary, dataset card, field card — coarse to fine |
| **Profile** | the measurements: counts, distributions, uniqueness, change rates |
| **Definition** | what the business says it means |
| **Transformation** | the executable code that produces it |
| **Lineage** | where it comes from and what depends on it, with evidence |
| **Usage** | who and what uses it, and how often |
| **Decisions** | what was ruled about it, by whom, and when |

A recipe names which facets it needs. Summaries still come first where they suffice, which is
the "breadcrumb trail" of the author's original vision in
[010_vision.md](../00_concept/010_vision.md). But a summary can erase a rare, decisive
exception, so every summary **cites its sources**, **discloses what it left out**, and carries
**drill-down triggers**: conditions under which the task must load the detail instead — for
example, when the summary mentions exceptions, or when the decision turns on a specific value.

Rebuilding summaries when their sources change is a gardening job
([126_context-gardening.md](126_context-gardening.md)).

## Trust is recorded per claim, in several dimensions

A model does not by itself distinguish between what a person ruled and what it guessed, so
trust has to be explicit. A single label per card is too coarse: one card holds claims with
different owners and evidence, and *ruled*, *evidenced* and *stale* are not alternatives — a
claim can be all three. Following [120](120_context-layer.md)'s split between normative and
descriptive claims, each claim records:

- **provenance** — who or what produced it;
- **authority** — whether someone with the mandate ruled it, and who;
- **scope** — the population and conditions it holds for;
- **evidence method** — how it was established;
- **confidence**;
- **freshness** — when it was last actually verified;
- **conflict status** — whether newer evidence contradicts it.

For display, these may be summarised as a short label — *ruled*, *evidenced*, *inferred*,
*stale*, *disputed* — but the label is a view of the record, not the record.

**Acceptance rules are set per decision type.** A semantic decision needs authority; a
statistical observation cannot stand in for it. A mart may be generated only from key
assertions that are both authorised and currently evidenced.

## Measuring whether it works

Measures that reward looking efficient are easy to game: one enormous "load" satisfies a
three-load rule, and an agent cannot report context it never knew existed. So:

- The **three-load rule** from [120](120_context-layer.md) stays as a design heuristic, with
  *load* defined — one retrieval call returning a bounded amount — and is not used as a target.
- The real measures are taken against **benchmark tasks** whose required evidence is known in
  advance: **required-evidence recall**, the share of irrelevant material loaded, cost, latency,
  corrections made by reviewers, and defects found downstream.
- **Missing context** is found by independent review and by later incidents, not only by the
  agent's own after-task report. The after-task question — *what did you need and not find,
  what did you load and not use?* — stays as one input among several, with the caution that
  "unused" evidence may be what ruled out a dangerous option.

This is continuous improvement of the method, row 38 of 070, applied to the context system.

## Open

`ARC-OP-25` holds what is not yet designed: the recipe format, where recipes live, the
benchmark tasks, and how measurements are collected.
