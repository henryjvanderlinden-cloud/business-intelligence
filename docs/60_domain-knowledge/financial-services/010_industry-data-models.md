# Industry data models for financial services

Written by Claude, 2026-10-25, from a conversation of 2026-10-22.

## 1. FSLDM is not public

1. FSLDM (Teradata Financial Services Logical Data Model) is a licensed Teradata product. Teradata now markets it as the **Financial Services Data Model (FSDM)**.
2. FSDM is paired with the **Financial Services Analytic Schemas (FSAS)**:
   - FSDM is the normalised, integrated layer.
   - FSAS is the dimensional access layer.
   - They can be bought separately or together.
3. Teradata describes FSDM as covering 400+ broad subject areas.
4. You get it through a Teradata engagement. The only public material is marketing pages and white papers.
5. Copies on document-sharing sites are not licensed. Do not use them.

## 2. Proprietary peers

1. IBM Banking & Financial Markets Data Warehouse (formerly BDW).
2. Oracle Financial Services Analytical Applications (OFSAA) data model.

Both are licensed products, like FSDM.

## 3. Publicly accessible alternatives

These are ordered from closest to furthest from an FSLDM-style integration layer.

1. **ECB BIRD (Banks' Integrated Reporting Dictionary).** Free. This is the nearest analogue. It has a Logical Data Model, an Input Layer, and transformation rules to regulatory outputs. See [020_bird.md](020_bird.md).
2. **FIBO (EDM Council).** An open-licensed OWL ontology of financial concepts. It gives you semantics (definitions), not a physical warehouse schema. The exact licence is **(unverified)**; it was MIT at last check.
3. **ISO 20022 data dictionary / business model.** Free. A repository of business components, oriented around payment and securities messages. See [040_transactions-and-payments.md](040_transactions-and-payments.md).
4. **BIAN (Banking Industry Architecture Network).** A service landscape and business object model for banking. It is architecture-oriented rather than a warehouse model. Download terms (registration) are **(unverified)**.
5. **EBA DPM (Data Point Model).** Public, but it models reporting outputs, not source data.
6. **Len Silverston, *The Data Model Resource Book*, Vol. 2.** Not free, but openly purchasable. It contains financial-services patterns at the logical level.

## 4. Practical conclusion

Combining BIRD's model for structure with FIBO for definitions comes closest to what FSLDM provides, without licensing.

## Sources

- Teradata, Financial Services Data Model: https://www.teradata.com/Industries/Financial-Services/Financial-Services-Data-Model
- Regnology, What is BIRD?: https://www.regnology.net/en/resources/regulatory-topics/banks-integrated-reporting-dictionary-bird/
