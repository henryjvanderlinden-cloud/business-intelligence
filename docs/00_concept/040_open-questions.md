# 040 — Open questions

The register of things not yet resolved. Adding an entry is a contribution. Resolving
one ends in an ADR, after which the entry is struck through here with a link.

Entries are grouped, not prioritised.

## Scope and framing

1. ~~Is the target a **product**, an **internal capability**, or a **written
   argument**?~~ Resolved: sequentially all three, with explicit gates.
   See [ADR-0006](../20_decisions/0006-project-mode.md).
2. ~~Is the first realistic environment a real corporate landscape, or a synthetic
   one?~~ Resolved in part by [ADR-0006](../20_decisions/0006-project-mode.md): public
   practice datasets first. The residual question is **ground truth** — public data
   supplies genuine messiness but no answer key for cross-source entity identity, and
   without an answer key the falsifiable core cannot be measured. See
   [410_first-vertical-slice.md](../40_roadmap/410_first-vertical-slice.md) §Environment.
3. What is the smallest landscape on which the idea is falsifiable? Two sources and one
   question, per the roadmap — but which two, and whose question?

## Structural layer

4. How is a source *discovered* rather than registered? Network discovery is the
   brief's most evocative image and its most legally fraught. Is discovery in scope at
   all, or does the system begin from a human-supplied inventory?
5. What is the minimum profiling pass that yields useful joinability evidence at
   acceptable cost? Sketch-based (HyperLogLog, MinHash) profiling makes cross-source
   overlap estimation cheap without moving data; how far does that get us?
6. How are heterogeneous SQL dialects normalised for parsing and lineage extraction?

## Semantic layer

7. What evidence, precisely, promotes a joinability hypothesis to a business-key
   assertion? A stated threshold is needed or the system will either flood the queue or
   silently assert nonsense.
8. How is disagreement between two human adjudicators represented? Semantics are
   contested in real organisations, and a model that admits only one answer will
   record whichever answer arrived last.
9. How does an assertion age? A confirmed fact about a system that was re-platformed
   two years later is no longer true, and nothing in the data will say so.

## Teleological layer

10. Who maintains the decision register, and what keeps it current?
11. What is the acceptance test for an automated analysis? "Interesting" is not
    measurable; "changed a decision" is, but only retrospectively and rarely.

## Mechanics

12. Is the context layer a git repository of files, a graph database, or both with one
    derived from the other? This is the most consequential unmade decision and is
    treated in [`../10_architecture/120_context-layer.md`](../10_architecture/120_context-layer.md).
13. What is the unit of agent work — a long-running loop, or many short, idempotent,
    independently retryable jobs? The second is almost certainly right but has
    implications for how state is passed.
14. Which model, at which tier, for which task, and who decides? Structural work is
    high-volume and cheap; semantic work is low-volume and benefits from the strongest
    available reasoning. A routing policy is needed.
15. How is cross-model review wired in? A second model reviewing the first model's
    semantic assertions is a cheap and plausible quality mechanism.
16. What does the human interface actually look like? Repository pull requests, a web
    application, a chat surface, or a weekly digest? The answer determines whether
    adjudication happens at all.
