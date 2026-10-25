# BIRD — Banks' Integrated Reporting Dictionary

Written by Claude, 2026-10-25, from a conversation of 2026-10-22. Revised the same day after review by sol; see [XREV_2026-10-25_fs-020_sol.md](../../30_research/notes/XREV_2026-10-25_fs-020_sol.md).

## 1. What it is

1. BIRD is a voluntary dictionary and methodology for regulatory reporting. It contains semantic definitions, logical model artefacts, input requirements, mappings and transformation rules for producing regulatory outputs. It is not a reporting requirement in itself.
2. It is maintained through cooperation between the ECB, the euro-area national central banks and the banking industry: banks, industry associations and software or service providers.
3. It is meant to help banks organise data from their internal systems once, then generate reports from it consistently.
4. **BIRD and IReF** (the ECB's Integrated Reporting Framework) are complementary:
   - IReF sets harmonised statistical reporting requirements.
   - BIRD describes the bank-side input data and transformations that can serve IReF and other frameworks.
   - The ECB stated in 2020 that the two would share the same data dictionary and modelling approach. Regnology calls them the two pillars of the ECB's long-term reporting strategy.
   - Still, don't assume their dictionaries are identical in a given release. Map them explicitly and keep their versions apart.
5. The ECB publishes the BIRD documentation and model metadata free of charge:
   - documentation on the ECB website
   - a browsable model at bird.ecb.europa.eu
   - the Logical Data Model on GitHub at `DGSbird/BIRD-Logical-Data-Model`

   Check the coverage, version and licence of each artefact separately. This is not one deployable package.

## 2. Layers

1. **Logical Data Model (LDM).** Highly normalised and technology-independent. Use it as a semantic reference and mapping target. It does not settle grain, identifiers, historisation, source-of-record rules or performance, so warehouse design remains a separate step. See [030_bird-as-data-vault-foundation.md](030_bird-as-data-vault-foundation.md).
2. **Enriched LDM (ELDM).** The LDM made easier to write transformation rules against. Enrichment covers two different things:
   - properties brought into an entity's context by navigating LDM relationships
   - derived attributes, such as the SME indicator computed from employee count and turnover (the ECB's own BIRD example)

   Keep the two apart in a warehouse: one is a navigation path, the other a calculation.
3. **Input Layer (IL).** BIRD's logical input interface for reporting banks, organised into "input cubes". Cubes are multidimensional model objects; the BIRD user guide notes they are typically implemented as database tables. Even so, don't read a warehouse schema off the cube boundaries.
4. **Transformation rules and mappings.** These run from the input layer to output layers that match the reporting templates (FINREP, COREP, AnaCredit and others).

## 3. Time in BIRD

1. Input cubes carry a reference date, named `DT_RFRNC` in the Technical Guidelines 4.0. Check the name against the current release. Data is organised primarily per reporting reference date.
2. BIRD also carries domain dates (inception, maturity, default, valuation) and some flow-type measures. It has no general system-time or transaction-time history.
3. So "stock-based" is the dominant shape, not the whole story. Keep source events and their history in the warehouse independently of BIRD.

## 4. Which systems feed it

1. BIRD specifies what is expected at its input boundary, not which systems must supply it.
2. Typical source categories are back and mid office (contracts, instruments, parties, protection and their relationships) and finance and risk calculation engines. The same variable can come from a ledger, a sub-ledger, a risk engine, master data or a governed warehouse.
3. System of record, ownership, reconciliation and lineage have to be decided per input variable.
4. **Accounting and valuation measures at the input boundary.** The Technical Guidelines 4.0 list these input-layer measures. A bank may source them from an accounting sub-ledger, a valuation service, a risk engine or a governed warehouse:
   - accumulated impairment (`ACCMLTD_IMPRMNT`)
   - fair value (`FV`)
   - accumulated changes in fair value (`ACCMLTD_CHNG_FV`)

   Variable names and availability are release- and cube-specific; check the current release. AnaCredit-related content also has the narrower "accumulated changes in fair value due to credit risk".
5. **Risk parameters and classifications.**
   - Default status and the counterparty's probability of default (PD) are AnaCredit attributes, supplied as inputs.
   - LGD is not an AnaCredit attribute, so don't expect it from that part of BIRD.
   - IFRS 9 stage is an accounting impairment classification. Don't equate it with AnaCredit's impairment status without checking the release.
   - Record provenance and temporal scope for every item. Record a model or methodology version only where the value was produced under one (PD, LGD). Default status and stage are classifications, with a governing rule and an assessment date.
6. **What BIRD derives itself.** The technical guidelines contain derivation rules for carrying amount (Technical Guidelines 4.1), exposure class and risk weight. These do not apply everywhere:
   - Carrying amount is also an input attribute in some contexts.
   - Exposure class is derivable only where the framework's rules and inputs are complete.
   - Under internal-ratings-based (IRB) approaches, approved internal models estimate risk parameters: PD, and in advanced IRB also LGD and others. The prescribed regulatory risk-weight functions turn those parameters into risk weights. A BIRD transformation may calculate a risk weight from governed inputs, or a cube may require an externally calculated result as input; release, framework, exposure class and approach decide which. Record provenance either way.

   Classify each variable as input or derived per release, cube, framework and approach.
7. **LTV.** There is no single context-free LTV. Origination, current, indexed, regulatory and template LTVs can differ in:
   - exposure numerator
   - collateral denominator
   - valuation date
   - prior liens
   - allocation and aggregation

   Model each named LTV definition separately, keep its components and valuation date, and decide input or derived from the applicable rule. The DNB residential real-estate model is a separately governed Dutch definition to check on its own terms.

## 5. Dutch national models

1. DNB publishes data reference models for residential real estate (RRE) and commercial real estate (CRE).
2. They reuse and align with BIRD modelling, but they are separately governed, not BIRD releases. Map them to BIRD explicitly and keep their versions apart.
3. They are reference models, not implementations.
4. Objects seen in them include party, protection received, instrument-protection received data, debtor-instrument data, financial data and accounting data. These mix entities, associations and data groupings. Copy each one's formal grain, identifiers and cardinalities before mapping it to warehouse structures.

## Sources

- Regnology, What is BIRD?: https://www.regnology.net/en/resources/regulatory-topics/banks-integrated-reporting-dictionary-bird/
- ECB, BIRD status report (2020): https://ECB.eu/stats/ecb_statistics/co-operation_and_standards/dialogue/shared/files/banking_industry_dialogue_statistics_20201104_Presentation3.1.pdf
- ECB, BIRD Technical Guidelines 4.0: https://www.ecb.europa.eu/stats/ecb_statistics/reporting/html/bird_Technical_Guidelines_4.0.fr.pdf
- ECB, BIRD Technical Guidelines 4.1: https://www.ecb.europa.eu/stats/ecb_statistics/co-operation_and_standards/reporting/html/bird_Technical_Guidelines_4.1.en.pdf
- ECB, Introduction to the BIRD LDM v1.2: https://ecb.europa.eu/stats/ecb_statistics/reporting/html/BIRD_Introduction_to_the_LDM_V1.2.pdf
- ECB, BIRD example (LDM vs ELDM): https://www.ecb.europa.eu/stats/ecb_statistics/reporting/html/BIRD_example_for_website.pdf
- BIRD user guide: https://bird.ecb.europa.eu/userguide/index.html
- DNB, RRE LDM: https://www.dnb.nl/media/srsgflen/rre-ldm-v1-3-1.pdf
- DNB, CRE LDM: https://www.dnb.nl/media/t32orncc/cre-ldm-v1-4-1.pdf
