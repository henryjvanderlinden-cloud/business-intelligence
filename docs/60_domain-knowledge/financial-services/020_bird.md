# BIRD — Banks' Integrated Reporting Dictionary

Written by Claude, 2026-10-25, from a conversation of 2026-10-22.

## 1. What it is

1. BIRD is a methodology and data model for regulatory reporting. It is developed by the ECB, euro-area national central banks and banking software vendors.
2. Use is voluntary for banks.
3. It is meant to help banks organise data from their internal systems once, then generate reports from it consistently.
4. BIRD and IReF (the ECB's Integrated Reporting Framework) share the same data dictionary and modelling approach. The ECB treats them as the two pillars of its long-term reporting strategy.
5. Everything is published free:
   - documentation on the ECB website
   - a browsable model at bird.ecb.europa.eu
   - the Logical Data Model on GitHub at `DGSbird/BIRD-Logical-Data-Model`

## 2. Layers

1. **Logical Data Model (LDM).** Highly normalised and designed for integrity and consistency. This is the layer to build on. See [030_bird-as-data-vault-foundation.md](030_bird-as-data-vault-foundation.md).
2. **Enriched LDM (ELDM).** The LDM plus derived attributes needed for reporting. Example: an SME indicator derived from employee count and turnover.
3. **Input Layer (IL).** BIRD's implementation model, derived from the LDM. Its tables are called "input cubes".
4. **Transformation rules and mappings.** These run from the input layer to output layers that match the reporting templates (FINREP, COREP, AnaCredit and others).

## 3. Time in BIRD

1. Input cubes carry a reference date (`DT_RFRNC`). Data is a snapshot per reporting period.
2. There is no transaction-time dimension. BIRD is stock-based: positions at a date, not events.

## 4. Which systems feed it

BIRD is fed by both back/mid-office systems and finance/risk calculation engines.

1. **Back and mid office** supply contracts, instruments, parties, protection, and relationships between them.
2. **Finance and risk engines** supply measures that exist only as their outputs. Standard input-layer measures of this kind include:
   - accumulated impairment (`ACCMLTD_IMPRMNT`)
   - fair value (`FV`)
   - accumulated changes in fair value (`ACCMLTD_CHNG_FV`)
3. IFRS 9 stage, default status, PD and LGD are likewise engine outputs taken as inputs. They come from the AnaCredit-derived parts of the model **(unverified at attribute level)**.
4. BIRD derives reporting-specific constructs itself. The technical guidelines contain derivation rules for:
   - carrying amount
   - exposure class
   - risk weight
5. **LTV** is usually on the derived side. It is computed from instrument amounts and protection data (protection value, valuation approach, allocated protection value per instrument–protection pair). National extensions sometimes take origination LTV as a raw attribute. Check the DNB residential real-estate model specifically.

## 5. Dutch national variants

DNB publishes logical data models in BIRD style for:

1. Residential real estate (RRE)
2. Commercial real estate (CRE)

They are useful Dutch reference implementations. Entity names seen in them:

- party
- protection received
- instrument-protection received data
- debtor-instrument data
- financial data
- accounting data

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
