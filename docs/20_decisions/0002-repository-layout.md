# ADR-0002 — Repository layout and documentation conventions

- **Status:** Accepted
- **Date:** 2026-09-19

## Context

The repository begins as a place to organise thinking and is intended to become a place
where components are built. Its layout must serve both without a disruptive
reorganisation in between, and must be navigable by agents that load a handful of files
rather than reading everything.

## Options considered

*Flat `docs/` directory.* Simplest. Rejected because ordering and grouping are
load-bearing for navigation once the document count passes about fifteen.

*Numbered, grouped directories with gapped three-digit filename prefixes.* Stable
ordering, citable filenames, insertion without renumbering. Matches conventions already
in use in the author's other repositories, which has real value for consistency of
habit.

*Wiki or external tool.* Rejected: not diffable, not co-located with code, not readable
by an agent working in the repository.

## Decision

The layout is as follows, with `spec/`, `prototypes/` and `tests/` reserved and
initially near-empty:

```
docs/00_concept/       Problem statement, critique, glossary, open questions, prior art
docs/10_architecture/  How the system is meant to work
docs/20_decisions/     ADRs
docs/30_research/      Prior art, tool evaluations, reading notes
docs/40_roadmap/       Phasing and vertical slices
spec/                  Machine-readable contracts for context-layer artifacts
prototypes/            Throwaway code answering one question
tests/                 Tests for anything graduating out of prototypes/
```

Documents are prose-first, one concept per file, split beyond roughly four hundred
lines, cross-linked with relative links, and numbered with gaps of ten.
[`AGENTS.md`](../../AGENTS.md) carries the working conventions for agents.

## Consequences

Renumbering is forbidden, so gaps will appear and some numbers will be slightly out of
logical order over time. This is preferred to breaking inbound links and ADR citations.
When code arrives it goes in `src/`, alongside rather than instead of `docs/`.
