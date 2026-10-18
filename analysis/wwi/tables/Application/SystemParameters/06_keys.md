---
id: wwi:object:498100815
subject: wwi/tables/Application/SystemParameters
item: 06
topic: keys
tier: minimum
summary: SystemParameterID is the key of the single row.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-18T13:20:00Z
step: S08-054
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py 102dceeb7d85ec3db493afa75ff1e907c8b3f3a6, profile_tables.py e61ada2547265905e3558722cd127e81fa5cd770, evidence_shared.py 03d3dfbc0522d76aef793a33dc2bc491abc70529
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 1f26426deac5de8b5258e1a7f6e26fc36706678e138f773b0dfe3dfa5f0d5e27
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=72df613f2d4d80f5 | recheck=the key range changes | text: The key runs from 1 to 1 with no gap.
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=0c6c31f37cdc5cc9 | recheck=a foreign key changes | text: 3 declared foreign keies, all enabled and trusted: LastEditedBy -> Application.People.PersonID; DeliveryCityID -> Application.Cities.CityID; PostalCityID -> Application.Cities.CityID.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=72df613f2d4d80f5 | recheck=every new extract, or a schema change | text: One row; the key is trivially unique.

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

None.

## For a person

None.
