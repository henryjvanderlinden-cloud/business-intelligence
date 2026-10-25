# ADR-0023 — Domain knowledge lives in `docs/60_domain-knowledge/`, one subfolder per industry

- **Status:** Accepted
- **Date:** 2026-10-25
- **Supersedes:** —
- **Superseded by:** —

## Context

Rick asked for a "Domain Knowledge" folder with a "Financial Services" (or "Banking") subfolder, to keep findings on industry data models, BIRD, Data Vault patterns for banking and securitisation reconciliation for future reference. [ADR-0002](0002-repository-layout.md) fixes the repository layout and has no place for industry knowledge that is neither about how nsdn works nor a reading note on a single source. Placing a new group is a layout choice, so it is recorded here rather than made silently.

## Options considered

*A top-level `Domain Knowledge/` folder, named exactly as asked.* It is the most literal reading of the request and would sit visibly apart from the nsdn design documents, which suits knowledge that also serves client work outside nsdn. Against it: spaces and capitals break the naming used everywhere else, and a top-level folder is not covered by ADR-0002 or by the checker's assumptions.

*Under `docs/30_research/`.* That group already holds prior art and reading notes, so no new group is needed. Against it: research notes there are dated, single-occasion records, whereas domain knowledge is meant to be maintained and extended by industry over time.

*A new group `docs/60_domain-knowledge/`, with one kebab-case subfolder per industry.* It follows the gapped numbering and naming of ADR-0002, keeps the material under `docs/` where agents already look, and gives domain knowledge its own maintained home.

## Decision

Domain knowledge is kept in `docs/60_domain-knowledge/`, with one subfolder per industry, starting with [`financial-services/`](../60_domain-knowledge/financial-services/README.md). "Financial services" is preferred over "banking" because securitisation and other topics reach beyond banks. Files inside follow the usual conventions: gapped three-digit prefixes, one concept per file, relative links, and provenance on assertions.

## Consequences

ADR-0002's layout listing gains a group; it is not edited, and this ADR is the record of the addition. The financial-services notes were drafted by Claude and are unreviewed until they pass [external review](../50_process/510_external-review.md). Rick accepted filing under `docs/` on 2026-10-25. Revisit if domain knowledge turns out to belong outside this repository because it serves VDL-DIAA work more than nsdn.
