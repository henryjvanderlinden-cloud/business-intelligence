# ADR-0004 — Models never operate in the data path

- **Status:** Accepted
- **Date:** 2026-09-19

## Context

An agent-driven data system can place a language model in one of two positions: emitting
the artifacts that process data, or processing the data itself. The distinction is easy
to blur in practice — a model that "just cleans up these addresses" or "just classifies
these free-text fields" has crossed it — and the blurring is usually incremental and
locally reasonable.

## Options considered

*Models may process rows where it is convenient.* Genuinely capable for entity
resolution on messy text, classification of unstructured fields, and extraction. Real
value is forgone by refusing it, and this should be acknowledged.

*Models emit artifacts only.* Preserves reproducibility (a rerun of Q2 produces Q2's
numbers), auditability (every transformation is inspectable code), cost predictability
(cost scales with decisions, not rows), and testability (Level 1 in
[160_evaluation-and-regression.md](../10_architecture/160_evaluation-and-regression.md)
becomes meaningful).

## Decision

Language models read metadata, samples and context, and emit code, configuration,
assertions and prose. Deterministic engines execute. No model output is ever a row in
the warehouse.

Where model-based row processing is genuinely required — free-text classification, for
example — it is implemented as an explicit, versioned, separately evaluated enrichment
step with its outputs materialised, attributed and treated as a *source* under its own
contract, never as a transformation. Such a step requires its own ADR.

## Consequences

Some problems become harder or are deferred. In exchange, every number the system
publishes is reproducible from versioned declarations, and the system's cost scales with
the number of decisions rather than with data volume. This is the constraint from which
most of the rest of the architecture follows, and reversing it would invalidate large
parts of it.
