# 122 — Context retrieval: recipes, zoom levels and trust labels

Part of the context system described in [120_context-layer.md](120_context-layer.md). Drafted
2026-09-25, session 04, from a brainstorm with the author. Nothing here is built; everything is
stated as what the system should do.

## The problem

The agentic layer starts cold on every task (dimension 7 of
[060_faculty-inventory.md](../00_concept/060_faculty-inventory.md)). It needs a lot of context
to be useful, but never all of it at once. Retrieval has to deliver the *right* context for the
task in hand, within a budget, and it has to say how far each piece can be trusted.

## Retrieval is shaped by the task, not by search

[070_task-allocation.md](../00_concept/070_task-allocation.md) lists about forty task types.
Each type needs a predictable set of context. So each task type should have a **context
recipe**: a short, versioned description of what to load, starting from which object, and at
what level of detail.

A recipe states:

- **the anchor** — the object the task is about, by its permanent identifier;
- **what to load** — named neighbours of the anchor, found by following links, not by search;
- **the zoom level** for each item (see below);
- **a budget** — how much context the task may use;
- **the minimum trust** acceptable for each item, and what to do when only lower-trust context
  exists;
- **what to write back** afterwards, which links it to
  [124_context-write-back.md](124_context-write-back.md).

Example: *propose a business key for table X* (row 9 of 070) would load the table's card and
its profile summary; columns elsewhere that look similar; existing hub cards for the entity the
table seems to describe; hypotheses about this table that were rejected earlier; the naming
conventions that apply to its source; and its temporal profile
([127_temporal-behaviour.md](127_temporal-behaviour.md)) and known relationships
([128_join-knowledge.md](128_join-knowledge.md)).

Search still has a role, but only as the **entry point**: finding the anchor when the task
names something by description rather than by identifier. After that the agent walks links.
This is [120](120_context-layer.md)'s "search is the entry point; traversal is the method",
made concrete per task.

Recipes are know-how, one of the five kinds of context in 120. They are drafted by the agentic
layer, approved by a person, and improved over time from the measurements below.

## Zoom levels

Context is summarised at several levels, and the agent starts coarse:

1. **landscape map** — the whole estate on a page;
2. **source summary** — one per source system;
3. **dataset card** — one per table, file or endpoint;
4. **field card** — one per column;
5. **raw profile** — the full measurements, loaded only when a decision turns on them.

A recipe names the level for each item. Most tasks should need levels 2–4, and should reach
level 5 only for the few objects the decision actually depends on. This is the "breadcrumb
trail" of the author's original vision in [010_vision.md](../00_concept/010_vision.md).

Summaries go stale when what they summarise changes. Rebuilding them is a gardening job
([126_context-gardening.md](126_context-gardening.md)).

## Trust labels

The faculty inventory records that a model does not, by itself, distinguish between what a
person ruled and what it guessed. So every piece of context should arrive with a visible
label:

| Label | Meaning |
|---|---|
| **ruled** | a person with the mandate decided it |
| **evidenced** | backed by a measurement or a recomputable check |
| **inferred** | proposed by the agentic layer, not yet checked or ruled |
| **stale** | was ruled or evidenced, but has not been re-checked within its review period |
| **disputed** | contradicted by newer evidence, awaiting a ruling |

Without these labels the agent treats its own earlier guesses as facts, and errors compound
from task to task. A recipe can then require, for example, that a mart may only be generated
from *ruled* or *evidenced* key assertions.

## Measuring whether it works

Two measures, both cheap:

- **The three-load rule** from [120](120_context-layer.md): a task should establish what exists,
  what is known, what is uncertain and what depends on it in at most three loads. More than
  three means the context system, not the agent, needs fixing.
- **An after-task question:** *what did you need that you could not find, and what did you
  load that you did not use?* The answers are written back and used to improve the recipe.

Over many tasks this gives each recipe a record of how well it serves its task type. That is
continuous improvement of the method, row 38 of 070, applied to the context system itself.

## Open

`ARC-OP-25` holds what is not yet designed: the recipe format, where recipes live, and how
their measurements are collected.
