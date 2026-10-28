# ADR-0030 — Hubs and links are keyed on hash keys computed from the key-space code and the business key

- **Status:** Accepted
- **Date:** 2026-10-28
- **Supersedes:** —
- **Superseded by:** —

## Context

[ADR-0029](0029-wwi-step-a-concepts-and-keys.md) settled which business key each hub of Wide World Importers holds and
left open how the hub's primary key is formed from it. [142](../10_architecture/142_the-data-model.md) and
[144](../10_architecture/144_raw-vault-business-vault-calculation-engines.md) §2 already assumed hash keys. On
2026-10-28 the author asked whether Data Vault hubs use meaningless keys rather than the business key; the model
answered that Data Vault 1.0 used sequence numbers, Data Vault 2.0 uses a hash of the business key, and that some
practitioners now argue for the concatenated business key itself (Roelant Vos, "Using a Natural Business Key – the end
of hash keys?", roelantvos.com, read 2026-10-28), and leaned to hash keys. The author ruled at 11:01, verbatim:

> Okay, let's do hash keys then. I've we have to merge data from separate systems (which is not the case right now)
> and they keys in the other database are postfixed or suffixed we'll fix it then. There are specialized tables for
> that, right?

## Options considered

*Sequence numbers*, as in Data Vault 1.0. Its case: small, ordered keys. Rejected: every load of a link or satellite
must first look up its hub's number, which fixes the loading order and prevents parallel and independent reloads.

*Hash keys*, as in Data Vault 2.0. Its case: deterministic, so any table loads in any order and can be rebuilt alone;
the standard of the dbt packages for Data Vault. Adopted.

*The concatenated business key itself.* Its case: deterministic too, readable, often smaller. Not chosen: the author
chose hash keys; it remains the alternative if hash keys prove costly.

## Decision

1. **Every hub's primary key is a hash of its key-space code and its business key**; every link's is a hash of the
   business keys it joins. The business key itself is always stored in the hub.
2. **Keys from another system are reconciled when such a system is added**, not now. Where its keys are the same
   identifiers written differently, or different identifiers for the same things, the integration follows 144 §3: a
   crosswalk the source delivers loads as a raw link, and matching that is our own judgement is a same-as link in the
   business vault.

## Consequences

The hash algorithm and how the key is prepared before hashing (delimiter between parts, treatment of empty values,
case and spaces) are not decided here; they belong to the model files and their generator (`ARC-OP-29`). Preparation
affects only the hash input: the business key is stored as delivered, in line with 144 §6 item 1 (tidying is
interpretation).

A hash key is meaningless to read, so the model files and the generated documentation show the business key beside it
(142 §6).

**Revisit** if hashing costs measurably in the sandbox's load times or storage, or when the second source is added.
