# BIRD as the foundation for a (bitemporal) Data Vault

Written by Claude, 2026-10-25, from a conversation of 2026-10-22. Revised the same day after review by sol; see [XREV_2026-10-25_fs-030_sol.md](../../30_research/notes/XREV_2026-10-25_fs-030_sol.md).

## 1. Where BIRD fits

1. **The raw vault stays source-aligned.** Land each source losslessly, at its own grain and meaning, with business keys, source record identifier, load time and record source. Don't force sources into BIRD's shape before the raw vault: a record with no clean BIRD equivalent would be rejected, collapsed or reinterpreted before its original assertion was kept.
2. **BIRD's LDM guides the shared concepts.** Use it to name the hubs (party, instrument, protection) and the relationships between them. It does not settle whether source identifiers share a key domain. Resolve each key's issuer or collision scope (for example, an identifier unique only per reporting agent), and assert crosswalks between different identifiers for the same object explicitly.
3. **BIRD conformance happens in the business vault**, or in a downstream canonical layer, with lineage. The exception is a source that already delivers data at exactly BIRD's grain and meaning.
4. The LDM is published on GitHub (`DGSbird/BIRD-Logical-Data-Model`). Work from it rather than reverse-engineering the input cubes.

## 2. Mapping LDM constructs to Data Vault

There is no one-for-one mapping. Classify each LDM entity by what it means and at what grain:

1. **Hubs** only for independently identifiable business concepts with a durable business key. A stable identifier is not enough. An observation identified by instrument, reference date, accounting standard and consolidation scope is not a hub; it is a dated, context-dependent observation of the instrument.
2. **Links** for associations, at a declared grain. Put a role into the link's identity only when it distinguishes relationships that exist at the same time, for example the same party being both debtor and protection provider on one instrument. Otherwise historise the role in a satellite.
3. **An associative entity** becomes a hub plus links only when it is independently meaningful as a business concept. If its identifier merely tells instances of a relationship apart, use it as a dependent-child or link-grain discriminator. One that represents an event becomes a transactional link.
4. **Satellites** for descriptive history, split by source and rate of change, attached only once the parent grain is right.
5. **Raw versus business vault** is decided by provenance, not by BIRD layer:
   - A value received from a source goes in the raw vault unchanged, even if BIRD files it under the ELDM.
   - ~~A value calculated here goes in the business vault, with its rule, inputs and run, even if BIRD files it under the LDM.~~ Superseded 2026-10-26 by [ADR-0025](../../20_decisions/0025-engine-results-in-the-raw-vault.md), the earlier text kept struck through: a value calculated here by a calculation engine goes in the raw vault, under the engine's own source code and labelled as derived, with its engine version, run and inputs, even if BIRD files it under the LDM. Interpretation that is not an engine's result (matching, readings of roles, point-in-time views) stays in the business vault.

## 3. Time

1. **BIRD's main time coordinate** is the reporting reference date (`DT_RFRNC` in the Technical Guidelines 4.0). It also carries domain dates: inception, maturity, default, valuation. Keep each according to its own meaning.
2. **The reference date is part of the observation's grain**, not just an attribute. Several reference dates for the same instrument can arrive in one load, for example a backfill or resubmission. Use a periodic-snapshot, multi-active or dependent-child pattern keyed on the reference date. Otherwise rows collide, or an old snapshot that arrived late is mistaken for the latest period.
3. **The load timestamp is warehouse system time:** when this vault saw the row. It is not when the source recorded the fact, nor when a report was submitted. Capture source assertion times and submission identifiers and timestamps separately whenever "as known" or "as reported" refers to them.
4. **Valid time has to be defined per relationship and attribute,** from source evidence:
   - Use an effectivity satellite only where the source supports relationship start and end, and declare its driving key and cardinality.
   - Distinguish "not observed" from "ended". An instrument missing from an incomplete April extract has not ended.
   - Concurrent relationships, such as two debtors on one instrument, are separate link instances, (A, I, debtor) and (B, I, debtor), each with its own effectivity. The second debtor's arrival then doesn't close the first. Multi-active satellites are for several concurrent attribute values of one parent, not for several parties.
5. **"As reported then" versus "as corrected now":**
   1. Model the submission or report version as a business object, and make it part of (or unambiguously identify) the grain of each reported observation. Linking a submission only to the instrument doesn't say which of several values it reported.
   2. Record submitted and accepted timestamps separately from load time.
   3. Combine that lineage with the fact's reference date or valid interval.

   Valid-from/valid-to plus a load timestamp alone cannot distinguish two submissions loaded in the same batch, nor a submission that corrects several reference dates.

## 4. Central concepts

Verify the exact names against the current GitHub release.

1. **Party.** Debtors, creditors, protection providers, servicers, originators. Roles are relationships, not subtypes. Hub.
2. **Instrument.** Loans and advances, debt securities, derivatives and deposits, in a supertype/subtype hierarchy. One hub, with subtype-specific satellites.
3. **Protection received.** Collateral and guarantees. Hub.
4. **Party–instrument role** ("has as role in instrument"). A link whose grain includes whatever distinguishes concurrent roles. Never infer that one party replaced another merely because a second one appeared. End a relationship only on explicit end evidence, or where the source's completeness and declared cardinality make absence into evidence. Example: a complete daily snapshot that guarantees exactly one primary servicer per instrument.
5. **Instrument–protection received data.** The allocation of protection to instruments, with allocated value and original protection value. A link with its own satellite.
6. **Party–party relationships.** Group structures, head office/branch. A link.
7. **Instrument-keyed data sets** (financial data, accounting data, risk and default data). "Instrument-keyed" does not mean "one row per instrument". Find each data set's full grain:
   - Genuinely instrument-level, single-valued facts go in instrument satellites.
   - Measures that depend on a relationship (for example a PD for a debtor–instrument pair) go on that link.
   - Observations that repeat by context (accounting standard, consolidation scope, currency, scenario) need an explicit grain that includes that context: a link to context hubs, a dependent-child key or a multi-active pattern. Adding the context informally to an ordinary instrument satellite either splits the instrument hub or makes rows collide.

## 5. Engine outputs in the vault

1. Finance and risk outputs don't share one instrument grain:
   - Stage and impairment can be per instrument and accounting scope.
   - PD and LGD can be per counterparty, facility, rating, collateral, scenario, horizon or allocation.
2. Model each output at its full calculation grain: the relevant party/instrument/protection relationship, reference date, scenario or horizon, run and model version.
3. Record source tells you where a row came from, not what grain it has. Without scenario and run in the key, two scenarios from the same run collide, and a later run's correction looks like ordinary history.
4. Where calculation runs are shared lineage objects, give them a hub and links rather than storing them as row attributes.

## 6. Limits of BIRD as a base

BIRD only covers what regulatory reporting requires. Payments and transaction events (see [040_transactions-and-payments.md](040_transactions-and-payments.md)), customer interaction and product catalogue are thin or absent. Treat BIRD as a reference for the core concepts, not the vault's full scope.

## Sources

- ECB, Introduction to the BIRD LDM v1.2: https://ecb.europa.eu/stats/ecb_statistics/reporting/html/BIRD_Introduction_to_the_LDM_V1.2.pdf
- ECB, BIRD LDM design principles: https://ecb.europa.eu/stats/ecb_statistics/reporting/html/BIRD_LDM_design_principles_latestVersion.pdf
- ECB, BIRD Technical Guidelines 4.0: https://www.ecb.europa.eu/stats/ecb_statistics/reporting/html/bird_Technical_Guidelines_4.0.fr.pdf
- DNB, RRE LDM: https://www.dnb.nl/media/srsgflen/rre-ldm-v1-3-1.pdf
- DNB, CRE LDM: https://www.dnb.nl/media/t32orncc/cre-ldm-v1-4-1.pdf
