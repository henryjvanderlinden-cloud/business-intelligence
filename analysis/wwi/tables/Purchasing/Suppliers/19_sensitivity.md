---
id: wwi:object:610101214
subject: wwi/tables/Purchasing/Suppliers
item: 19
topic: sensitivity
tier: minimum
summary: Bank account details (masked by the source, unmasked in the extract), contact phone numbers, and internal remarks about named individuals.
confidence: unknown
claims: 8
written_by: claude-opus-5-5
written_at: 2026-10-18T13:20:00Z
step: S08-054
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py 102dceeb7d85ec3db493afa75ff1e907c8b3f3a6, profile_tables.py e61ada2547265905e3558722cd127e81fa5cd770, evidence_shared.py 03d3dfbc0522d76aef793a33dc2bc491abc70529
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 7bcb78223c92bb8418652485c9f8ee3acdcdaf5d5f711f56ade275cb0fd6aa98
last_checked_at: 2026-10-18T13:20:00Z
last_checked_by: claude-opus-5-5
last_checked_against: 2016-06-01
reviewed_by: none
reviewed_at: none
ruled_by: none
ruled_at: none
supersedes: none
superseded_by: none
recheck_when: every new extract, or a schema change
---

## Claims

- C1 | type=declared | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=3087bee387e117ef | recheck=a column is added or renamed | text: Columns whose names or descriptions point to personal, contact, location, credential or free-text content: SupplierName, BankAccountName, BankAccountBranch, BankAccountCode, BankAccountNumber, BankInternationalCode, InternalComments, PhoneNumber, FaxNumber, WebsiteURL, DeliveryAddressLine1, DeliveryAddressLine2, DeliveryLocation, PostalAddressLine1, PostalAddressLine2.
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=3087bee387e117ef | recheck=a foreign key changes | text: Every row names the person who last edited it (LastEditedBy -> Application.People): attribution of work to identifiable staff, employee data whatever the table's content.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=3087bee387e117ef | recheck=a foreign key changes | text: Columns referring to people in Application.People (names, contact details): AlternateContactPersonID, PrimaryContactPersonID, besides the audit column LastEditedBy.
- C4 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=3087bee387e117ef | recheck=a masking rule changes | text: The source masks BankAccountName, BankAccountBranch, BankAccountCode, BankAccountNumber, BankInternationalCode from ordinary readers, a declaration that they are sensitive; the extract holds them unmasked.
- C5 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=69833227169e67f1 | recheck=every new extract, or a schema change | text: The five bank columns are filled for all 13 suppliers in the extract and are not masked there: account numbers, codes and international codes in clear.
- C6 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=69833227169e67f1 | recheck=every new extract, or a schema change | text: InternalComments holds two remarks about named contact persons' availability, described as not exposed outside the organisation.
- C7 | type=intended | status=proposed | confidence=low | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=3087bee387e117ef | recheck=the author rules | text: Proposed reading, not legal advice: bank details are financial data the source itself protects, so the warehouse should mask or exclude them too; the remarks are personal data about individuals.
- C8 | type=intended | status=proposed | confidence=unknown | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=none | recheck=the author rules | text: Whether bank details may enter the warehouse at all is not established; a person must rule.

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

None.

## For a person

May supplier bank details be loaded, masked, or not at all? The source masks them; our extract does not.
