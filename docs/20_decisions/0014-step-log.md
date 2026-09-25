# ADR-0014 — Record every step of the work in a classified step log

- **Status:** Accepted
- **Date:** 2026-09-25
- **Supersedes:** —
- **Superseded by:** —

## Context

The project is about to leave pure argument and begin the sandbox on public data about businesses in
the Utrecht region (`EVI-OP-2`). Its hypotheses are about who does what — faculties, roles, tiers, human
attention, maintenance against building — and they can only be tested afterwards if the work was
recorded as it happened, in those terms. The author ruled, verbatim:

> We need to start record keeping, exactly on what we do, how to classify it (human, agentic,
> deterministic, type of task etc), so that we can do a complete post mortem on what we did
> afterwards and to test our hypotheses. Can you build a structure to record all the data, and do
> meticulous record keeping of every step?

The design below was proposed by Claude Opus 5.5 in the same session and has not been reviewed.

## Options considered

*Rely on git history, handovers and the conversation transcript.* Its case: no new apparatus, which is
what `PRC-OP-2` asks for. Rejected: git records what changed, not who decided it or what was tried and
abandoned; handovers summarise; transcripts are not in the repository and are not classified. A
post-mortem from these would be a reconstruction, which is the failure the handover convention exists to
prevent.

*A prose journal per session.* Its case: easy to write and to read. Rejected because it cannot be counted.
The hypotheses need figures by faculty, role, tier and work class.

*A classified step log in the repository, validated by the checker.* Adopted.

## Decision

Every step of the work is recorded in `records/steps/<session>.jsonl`, with sessions and data sources in
their own files, classified by the vocabulary in `records/vocabulary.json`, as specified in
[520_record-keeping.md](../50_process/520_record-keeping.md). `tools/check_repo.py` validates the records.
Records travel in the same commit as the work. The top-level `records/` directory is added to the layout
of [ADR-0002](0002-repository-layout.md).

## Consequences

The log adds a small cost to every step, and that cost is itself logged as `overhead`, so the post-mortem
can see whether the apparatus stayed proportionate — the question `PRC-OP-2` holds.

The author's time is not observable; it is recorded as stated or as an elapsed upper bound, and the
limitation is stated in 520 rather than hidden.

Steps before this ADR in session 06 were reconstructed from the transcript in the same session and are
marked so. Sessions 01–05 are not logged; they remain covered by their handovers and review notes only.

**Revisit** if the log is not used by the first post-mortem, if its overhead share exceeds what the
author judges proportionate, or if the classification proves unable to express a step that matters.
