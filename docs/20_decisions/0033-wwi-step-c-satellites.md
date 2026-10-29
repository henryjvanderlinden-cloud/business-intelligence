# ADR-0033 — Wide World Importers, step C: the satellites of note 149; password hashes are never loaded, their column kept empty

- **Status:** Accepted
- **Date:** 2026-10-29
- **Supersedes:** —
- **Superseded by:** —

## Context

[149](../10_architecture/149_wwi-satellites.md) proposes step C for Wide World Importers: the satellites of the
twenty-two hubs ([ADR-0029](0029-wwi-step-a-concepts-and-keys.md)) and the forty-nine links
([ADR-0031](0031-wwi-step-b-links.md)), with an effectivity satellite per link, an audit and a status-tracking satellite
per hub, reference tables with history, a source-version identifier on every satellite row, and a sensitivity class per
satellite. Its first version failed review on sol; all five findings were applied in full or in part
([XREV](../30_research/notes/XREV_2026-10-29_149-satellites_sol.md)). It put one case to the author (149 §6): whether
password hashes are loaded at all, `Application.People.HashedPassword` holding them for 157 people with no analytical
use (`analysis/wwi/tables/Application/People/19_sensitivity.md#C3`), the legal basis of the people data not being
established (`#C7`). The model recommended not loading them, as the one exception to keeping everything delivered
([144](../10_architecture/144_raw-vault-business-vault-calculation-engines.md) §2).

The author ruled on 2026-10-29 at 11:33, verbatim:

> Definitely don't load hashed passwords. Maybe we should have an empty placeholder for them, so the table structure
> mimics the source system, but the values are empty. Agree with 149.

## Options considered

*Load the hashes into the restricted satellite.* Its case: the raw vault keeps everything delivered. Rejected: a
credential is a risk with no purpose in a warehouse.

*Leave the column out.* Its case: nothing to protect. Not chosen: the satellite would no longer show the source's
structure.

*Keep the column, always empty.* The author's design. Adopted.

## Decision

1. **Step C for Wide World Importers is as in 149**: the ten rules of §2, the satellites of §3, the effectivity
   satellites, reference tables and configuration of §4, and the loading of §5.
2. **Password hashes are never loaded.** `HashedPassword` is kept as a column of `sat_person__wwi__account`, so that
   the satellite mirrors the source's structure, and is always empty. The loading writes no value into it, whatever the
   source delivers; it is the one exception to keeping everything delivered (144 §2), and a deliberate one.

## Consequences

Because the column is always empty, it never changes and never affects change detection; a change of password in the
source shows only as a new version in the audit satellite. A test that the column is empty in every row belongs to the
satellite's generated tests. The analysis record keeps its claims about the hashes, which describe the source
(ADR-0020), not the warehouse.

The integration layer for Wide World Importers is now designed in full: hubs (ADR-0029), keys (ADR-0030), links
(ADR-0031) and satellites (this decision), with time (ADR-0027) and milestones (ADR-0028). Nothing is built. The
revised text of 149 is unreviewed on another model since its revision.

**Revisit** if another credential or secret is found in a source, which should be treated the same way, or when the
access rules per sensitivity class are decided.
