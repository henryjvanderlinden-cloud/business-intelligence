# ADR-0029 — Wide World Importers, step A: the hubs, business keys and business time of note 147

- **Status:** Accepted
- **Date:** 2026-10-28
- **Supersedes:** —
- **Superseded by:** —

## Context

[147](../10_architecture/147_wwi-concepts-keys-and-business-time.md) proposes step A of the route of 2026-10-21 for Wide
World Importers: twenty-two hubs and nine tables without one, the business key, key space and grain of each hub, and the
business time of every base table under [ADR-0027](0027-bitemporal-integration-layer.md) decision 4. Its three weak cases
were ruled in [ADR-0028](0028-wwi-country-key-milestones-and-sensors.md); the rest was put to the author as a whole on
2026-10-28. He answered at 10:31, verbatim:

> allright, let's see. Agreed with all point, but there is one thing. If memory serves me correct, in DataVaults we
> would introduce synthetic keys / meaningless keys, and not use the business key for hubs, not sure what the term
> was. Or am I incorrect, or was this idea abandoned in later versions of Datavault? I'm a bit in the dark here, please
> help me out.

His question concerns the hub's technical key, which 147 does not decide: 147 decides which business key a hub holds,
not how the hub's primary key is formed from it.

## Options considered

The alternatives to each part are set out in 147 and in the two review notes it cites
([keys](../30_research/notes/XREV_2026-10-26_147-keys_sol.md),
[business time](../30_research/notes/XREV_2026-10-26_147-business-time_sol.md)).

## Decision

1. **Step A for Wide World Importers is as in 147 §2 to §5**, with ADR-0028: the three rules (record identifiers in the
   key space `wwi` where no business identifier is evidenced, code lists as hubs only where they take part in a
   relationship, lines as hubs on their own identifiers), the twenty-two hubs of §3, the nine tables without a hub of
   §4, and the business time of §5 with its four consequences.
2. **The business key is what the hub holds, always, as an attribute.** How the hub's primary key is formed from it
   (a hash of the key-space code and the business key, as [142](../10_architecture/142_the-data-model.md) and
   [144](../10_architecture/144_raw-vault-business-vault-calculation-engines.md) §2 already assume; a sequence; or the
   concatenated key itself) is not decided here, and is open under `ARC-OP-37`. *Ruled 2026-10-28 in
   [ADR-0030](0030-hub-and-link-keys-are-hash-keys.md): hash keys.*

## Consequences

Step B, the relationships, can start from a settled set of hubs. The satellites (step C) remain open, apart from the
milestones (ADR-0028).

The revised text of 147 is unreviewed on another model since its revision; the two reviews that failed its first
version were applied in full or in part. **Revisit** when step B shows a hub that no relationship or satellite needs, or
a relationship that needs a hub 147 did not propose.
