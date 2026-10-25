# BIRD as the foundation for a (bitemporal) Data Vault

Written by Claude, 2026-10-25, from a conversation of 2026-10-22.

## 1. Build on the LDM, not the Input Layer

1. The Input Layer is shaped for producing reports. The LDM is shaped for integration, which is what a raw vault needs.
2. The LDM is published on GitHub (`DGSbird/BIRD-Logical-Data-Model`). Derive hubs, links and satellites from it directly instead of reverse-engineering the input cubes.

## 2. Why the LDM maps well to Data Vault

1. Its design principles say roles are modelled explicitly.
2. Many-to-many relationships use associative entities.
3. This gives the following mapping:

| LDM construct | Data Vault construct |
|---|---|
| Entity with a stable identifier | Hub |
| Associative entity / role | Link |
| Descriptive attributes and measures | Satellites, split by source and rate of change |
| ELDM derived attributes | Business vault, not raw vault |

4. The raw/business vault split lines up with BIRD's own LDM/ELDM split.

## 3. Bitemporality

1. BIRD has one time axis: the reference date (`DT_RFRNC`), a reporting-period snapshot.
2. Data Vault supplies transaction time natively, through load timestamps.
3. Valid time has to be added:
   - valid-from/valid-to in satellites
   - effectivity satellites on links
4. The reference date becomes an attribute, not the temporal backbone.
5. Why bother: regulatory resubmissions need both "as reported then" and "as corrected now". The same holds for ECL recalculations and restatements: "what the engine said on 31 March" versus "what we now know was correct for 31 March".

## 4. Central entities

Verify the exact names against the current GitHub release.

1. **Party.** Debtors, creditors, protection providers, servicers, originators. Roles are expressed through relationships, not subtypes. Data Vault: hub.
2. **Instrument.** Loans and advances, debt securities, derivatives and deposits, organised as a supertype/subtype hierarchy. Data Vault: one hub, with subtype-specific satellites rather than one hub per subtype.
3. **Protection received.** Collateral and guarantees, with type, value and valuation approach. Data Vault: hub.
4. **Party–instrument role** ("has as role in instrument"). Data Vault: link with an effectivity satellite.
5. **Instrument–protection received data.** The allocation of protection to instruments, with allocated value and original protection value. Data Vault: link with its own satellite.
6. **Party–party relationships.** Group structures, head office/branch relationships. Data Vault: link.
7. **Instrument-keyed data sets.** Financial data, accounting data, risk and default data. Data Vault: satellites on the Instrument hub, not hubs.

## 5. Engine outputs in the vault

1. Outputs from finance and risk engines (impairment, fair value, stage, PD/LGD) are just another source.
2. Put them in their own satellites on the Instrument hub, with the engine as record source.
3. Store the calculation run and model version, either as attributes or as a hub with a link.

## 6. Limits of BIRD as a base

BIRD only covers what regulatory reporting requires. These are thin or absent:

1. payments and transaction events (see [040_transactions-and-payments.md](040_transactions-and-payments.md))
2. customer interaction
3. product catalogue

Treat BIRD as the core of the vault, not its full scope.

## Sources

- ECB, Introduction to the BIRD LDM v1.2: https://ecb.europa.eu/stats/ecb_statistics/reporting/html/BIRD_Introduction_to_the_LDM_V1.2.pdf
- ECB, BIRD LDM design principles: https://ecb.europa.eu/stats/ecb_statistics/reporting/html/BIRD_LDM_design_principles_latestVersion.pdf
- ECB, BIRD example (LDM vs ELDM): https://www.ecb.europa.eu/stats/ecb_statistics/reporting/html/BIRD_example_for_website.pdf
- DNB, RRE LDM: https://www.dnb.nl/media/srsgflen/rre-ldm-v1-3-1.pdf
- DNB, CRE LDM: https://www.dnb.nl/media/t32orncc/cre-ldm-v1-4-1.pdf
