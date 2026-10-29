# ADR-0031 — Wide World Importers, step B: the links between the hubs of note 148

- **Status:** Accepted
- **Date:** 2026-10-29
- **Supersedes:** —
- **Superseded by:** —

## Context

[148](../10_architecture/148_wwi-relationships.md) proposes step B of the route of 2026-10-21 for Wide World Importers:
the links between the twenty-two hubs settled in [ADR-0029](0029-wwi-step-a-concepts-and-keys.md). Its first version
failed review on sol (event links without effectivity would leave two current targets after a correction); all five
findings were applied in full or in part ([XREV](../30_research/notes/XREV_2026-10-28_148-links_sol.md)). The revised
text was put to the author as a whole on 2026-10-28, with binary links named as the choice most open to disagreement.
He ruled on 2026-10-29 at 10:52, verbatim:

> Agree with 148

## Options considered

As set out in 148 §2 (binary links against one link per source row; loading repeated routes against choosing one;
zero keys against no row for empty columns; effectivity on every link against effectivity where change was observed)
and in the review note's dispositions.

## Decision

1. **Step B for Wide World Importers is as in 148**: the eight rules of §2, the forty-nine links of §3 with their
   driving sides and the business start of their effectivity, and the four relationships of §4 derived in the business
   vault as candidates under a versioned rule.
2. **Links are binary, one per relationship and role**; the links and satellites of one extract load and become
   visible as one batch.
3. **Every link gets a driving-key effectivity satellite** in step C.

## Consequences

Step C, the satellites, starts from settled hubs and links. It owes, from this decision: an effectivity satellite per
link; the optional relationship columns kept as delivered in the naming hub's satellite (148 Rule 4); the milestone
satellites of [ADR-0028](0028-wwi-country-key-milestones-and-sensors.md).

The batch rule depends on the runner publishing only whole loads, as it does in the sandbox
([ADR-0015](0015-sandbox-warehouse-dbt-duckdb.md)); a production runner must keep that property.

The revised text of 148 is unreviewed on another model since its revision. **Revisit** when step C or the first load
shows a link that no query uses, or a relationship the record did not show.
