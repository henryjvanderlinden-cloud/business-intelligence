---
id: wwi:object:98099390
subject: wwi/tables/Warehouse/PackageTypes
item: 19
topic: sensitivity
tier: minimum
summary: No personal or confidential content beyond the audit reference to the editing person.
confidence: medium
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-20T05:44:00Z
step: S08-088
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py ee7ed532e7ed7d38cce305ca07736b31a32cabaf, profile_tables.py e61ada2547265905e3558722cd127e81fa5cd770, evidence_shared.py 4174839b1036cd70f0c837acdee322e7071ca4b0
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 0263ce1739bb24cfa1adc545bdeab338bb4e156512ec4dcf93e55e467793997d
last_checked_at: 2026-10-20T05:44:00Z
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

- C1 | type=declared | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=1c7b301d8de3dc31 | recheck=a column is added or renamed | text: Columns whose names or descriptions point to personal, contact, location, credential or free-text content: PackageTypeName.
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=1c7b301d8de3dc31 | recheck=a foreign key changes | text: Every row names the person who last edited it (LastEditedBy -> Application.People): attribution of work to identifiable staff, employee data whatever the table's content.
- C3 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=1c7b301d8de3dc31 | recheck=every new extract, or a schema change | text: Reading: not sensitive; LastEditedBy identifies an employee who edited the row, which is employee data only in combination with Application.People.

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

None.

## For a person

None.
