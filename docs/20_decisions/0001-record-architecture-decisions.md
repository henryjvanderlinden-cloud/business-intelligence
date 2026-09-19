# ADR-0001 — Record architecture decisions

- **Status:** Accepted
- **Date:** 2026-09-19

## Context

This project will be developed over a long period, largely in conversation with language
models, with long gaps between sessions. An agent arriving cold — and the author
returning after three months — needs to know not only what the design is but which parts
of it are settled and why. Prose documents do not distinguish between "this is what we
decided" and "this is what someone was thinking at the time", and without that
distinction every document becomes negotiable, which means nothing accumulates.

## Options considered

*Prose documents only.* Lighter, and adequate for a solo project. Rejected because the
project's working mode is agentic: without an explicit record of settled decisions, each
new session is free to relitigate them, and will.

*Decision records.* Small overhead per decision; well understood; readable in isolation,
which suits the retrieval constraints in
[120_context-layer.md](../10_architecture/120_context-layer.md).

## Decision

Architecture decision records are kept in `docs/20_decisions/`, numbered sequentially,
never renumbered, never deleted. A decision is not in force until it has an ADR.

## Consequences

Documents in `docs/` become explicitly provisional, which is the intended effect. The
ADR index becomes the shortest honest summary of the project's state. Superseded ADRs
accumulate, and that is acceptable — the history of what was believed is itself useful
context.
