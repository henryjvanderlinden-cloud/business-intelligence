---
id: wwi:object:802101898
subject: wwi/tables/Sales/Customers
item: 19
topic: sensitivity
tier: minimum
summary: Customers can be individuals (declared); phone, fax, addresses and locations; contacts refer to people.
confidence: unknown
claims: 6
written_by: claude-opus-5-5
written_at: 2026-10-18T13:20:00Z
step: S08-054
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py 102dceeb7d85ec3db493afa75ff1e907c8b3f3a6, profile_tables.py e61ada2547265905e3558722cd127e81fa5cd770, evidence_shared.py 03d3dfbc0522d76aef793a33dc2bc491abc70529
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: f54b9d7dd163d0d1e3ce34f4adf4d1a76e8caeebe545ad0831277bb0e5b89fb6
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

- C1 | type=declared | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=4ffc9f716d8c1e42 | recheck=a column is added or renamed | text: Columns whose names or descriptions point to personal, contact, location, credential or free-text content: CustomerName, PhoneNumber, FaxNumber, WebsiteURL, DeliveryAddressLine1, DeliveryAddressLine2, DeliveryLocation, PostalAddressLine1, PostalAddressLine2.
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=4ffc9f716d8c1e42 | recheck=a foreign key changes | text: Every row names the person who last edited it (LastEditedBy -> Application.People): attribution of work to identifiable staff, employee data whatever the table's content.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=4ffc9f716d8c1e42 | recheck=a foreign key changes | text: Columns referring to people in Application.People (names, contact details): AlternateContactPersonID, PrimaryContactPersonID, besides the audit column LastEditedBy.
- C4 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=4ffc9f716d8c1e42 | recheck=every new extract, or a schema change | text: The source describes customers as "organizations or individuals": where a customer is a person, its name, address, location and phone number are personal data.
- C5 | type=intended | status=proposed | confidence=low | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=4ffc9f716d8c1e42 | recheck=the author rules | text: Proposed reading, not legal advice: personal data for individual customers and for contact persons; business data otherwise.
- C6 | type=intended | status=proposed | confidence=unknown | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=none | recheck=the author rules | text: Which customers are individuals is not established from the table; a person must rule how they are treated.

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

Telling individuals from organisations would need a rule (for instance names without a head-office or branch suffix); none is declared.

## For a person

None.
