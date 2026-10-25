# Industry data models for financial services

Written by Claude, 2026-10-25, from a conversation of 2026-10-22. Revised the same day after review by sol; see [XREV_2026-10-25_fs-010_sol.md](../../30_research/notes/XREV_2026-10-25_fs-010_sol.md).

## 1. FSLDM is not public

1. FSLDM (Teradata Financial Services Logical Data Model) is a licensed Teradata product. Teradata now markets it as the **Financial Services Data Model (FSDM)**.
2. FSDM is paired with the **Financial Services Analytic Schemas (FSAS)**:
   - FSDM is the normalised, integrated layer.
   - FSAS is the dimensional access layer.
   - They can be bought separately or together.
3. Teradata's product page advertises "400+ broad subject areas". The counting unit is unclear and the figure is release-dependent, so don't rely on it.
4. You get it through a Teradata engagement. The only public material is marketing pages and white papers.
5. Copies on document-sharing sites are not licensed. Do not use them.

## 2. Proprietary peers

1. **IBM Banking and Financial Markets Data Warehouse.** It grew out of IBM's Banking Data Warehouse (BDW) and Financial Markets Data Warehouse; naming varies by release.
2. **Oracle Financial Services Data Foundation (OFSDF).** Within Oracle's OFSAA family, OFSDF supplies the logical model and the staging and reporting physical data models used as a common analytical data foundation. OFSAA is the application family, not the model.

Both are licensed products, like FSDM.

## 3. Publicly accessible alternatives

No single public model matches FSDM's scope. The alternatives are grouped by what they offer, not ranked on one scale.

### 3.1 Enterprise logical models (closest in form to FSDM)

1. **FIB-DM (Financial Industry Business Data Model).** A conceptual enterprise data model derived from FIBO, in conventional data-modelling form, published by Jayzed Data Models. Of the models listed here it is closest in *modelling form* to FSDM (not in scope, currency or implementation readiness). It comes in two editions:
   - **FIB-DM Core:** a partial model derived from the 2018/Q4 FIBO release, downloadable (via a form) under GPL-3.0.
   - **Full FIB-DM:** derived from the current quarterly FIBO release, a commercial edition under Jayzed's proprietary licence.
2. **Len Silverston, *The Data Model Resource Book*, Vol. 2.** Not free, but openly purchasable. Financial-services entity-relationship patterns at the logical level.

### 3.2 Regulatory reporting

1. **ECB BIRD (Banks' Integrated Reporting Dictionary).** Free. The nearest public analogue *for the regulatory-reporting part of a bank*, not for FSDM's full scope. See [020_bird.md](020_bird.md).
2. **EBA DPM (Data Point Model).** Public, but it models reporting outputs, not source data.

### 3.3 Semantics

1. **FIBO (EDM Council).** An OWL ontology of financial concepts. It gives you definitions, not a warehouse schema. The ontology source is released under the MIT licence; separately published specification documents and trademarks keep their own terms.

### 3.4 Messaging and transaction standards

1. **ISO 20022.** The online repository and message definitions are freely accessible. It covers payments, securities, trade services, foreign exchange and cards. That access does not make every ISO standards document free. See [040_transactions-and-payments.md](040_transactions-and-payments.md).
2. **FpML.** A public standard for OTC derivatives: products, confirmations, reporting and lifecycle messages.
3. **FIX Protocol and FIX Orchestra.** Machine-readable semantics and workflows for electronic trading. Terms vary by artefact and version.
4. **FINOS Common Domain Model (CDM).** Originally the ISDA CDM. An open, machine-executable model of financial products, trades and lifecycle events. It is a transactional domain model, not a bank-wide integration schema.

### 3.5 Architecture

1. **BIAN (Banking Industry Architecture Network).** A service landscape and business object model for banking. It is architecture-oriented rather than a warehouse model. Some packaged Service Landscape downloads require free portal registration; other public material, including API definitions, does not. Check the terms for the release you use.

## 4. Practical conclusion

1. There is no free, scope-equivalent replacement for FSDM.
2. BIRD supplies regulatory-reporting structure. FIBO (or FIB-DM, in data-model form) supplies financial semantics. Combining them still takes substantial design and alignment work.
3. They avoid a proprietary licence fee, not licensing altogether: each has its own terms.

## Sources

- Teradata, Financial Services Data Model: https://www.teradata.com/Industries/Financial-Services/Financial-Services-Data-Model
- Regnology, What is BIRD?: https://www.regnology.net/en/resources/regulatory-topics/banks-integrated-reporting-dictionary-bird/
- Jayzed, FIB-DM Core download: https://fib-dm.com/data-model-download/
- Jayzed, FIB-DM licence and copyright: https://jayzed.com/fib-dm-open-source-license-and-copyright/
- Oracle, Introduction to OFSDF: https://docs.oracle.com/cd/E92917_01/PDF/8.1.x.x/8.1.2.0.0/FSDF_HTML/UG/2_Introduction_to_OFSDF.htm
- The remaining entries in sections 2 and 3 rest on general knowledge, checked by the sol review cited above, not on sources fetched for this note.
