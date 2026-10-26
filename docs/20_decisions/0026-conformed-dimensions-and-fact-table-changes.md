# ADR-0026 — Marts share conformed dimensions; changing a fact table to serve a new question is a deliberate, adjudicated decision

- **Status:** Accepted
- **Date:** 2026-10-26
- **Supersedes:** —
- **Superseded by:** —

## Context

On 2026-10-26 the author asked whether marts are derived from the raw and business vault, and proposed "dimensional
models for every distinct use case". The model answered that a dimensional model per use case works if dimensions are
conformed (defined, generated and shared once across marts), and asked what counts as a distinct use case. The author
ruled at 09:12, verbatim:

> 12: Like you said, dimensions should be shared. So we're focused mainly on fact tables. I think there is a
> consideration / deliberation necessary if for a new question a fact table only kind of fits. We should do an analysis
> then, to see how much we have to alter the fact table to make it compatible with the new request and how much we are
> drifting away from the original intent. If we can formalize these questions, then fine, otherwise human adjudication
> is necessary. Under normal circumstances this is not a continuous process / going concern thing. Expanding fact
> tables to fit new business questions is quite the fundamental decision. If you can list a number of considerations
> to base the decision on, that is very helpful. Maybe when enough experience has been built up the decision making
> can be automated.

## Options considered

*Each use case gets its own dimensions as well as its own facts.* Its case: marts are independent and can change
without coordination. Rejected: "customer" would come to mean different things in different marts.

*One enterprise-wide fact model that every question must fit.* Its case: one version of every measure. Rejected: it
forces questions into tables built for other purposes, which is the drift the author warns against.

*Conformed dimensions shared by all marts; fact tables per use case; a deliberate analysis whenever a new question
only partly fits an existing fact table.* Adopted.

## Decision

1. **Dimensions are conformed**: defined once, generated once, and shared by all marts.
2. **Design for a new question is mainly about fact tables.**
3. **When a new question only partly fits an existing fact table, an analysis is made first**: how much the table
   would have to change to serve the request, and how far that drifts from the table's original intent.
4. **Where the questions of that analysis can be formalised, the formal answer decides; otherwise a person
   adjudicates.**
5. **Extending a fact table to fit a new business question is a fundamental decision**, not routine maintenance.
   Under normal circumstances it is not a continuous process.

## Consequences

Every fact table needs a stated original intent, so that drift can be judged against it.

The considerations for the analysis are drafted in [146](../10_architecture/146_fact-tables-and-new-questions.md),
with a proposed classification into serving without change, minor extension, fundamental change and new fact table,
and a proposed case base of past decisions from which automation could later be judged. These are open under
[`ARC-OP-37`](../../registers/OPEN_POINTS.md) item 8, as are where marts take their data from and what counts as a
distinct use case.

Because extension is rare and adjudicated, the system should not grow fact tables on its own initiative; this narrows
what the agent layer may do in the marts without a ruling.

**Revisit** when enough adjudicated cases exist to test whether the formal answers agree with the author's, which is
the condition he set for automating the decision.
