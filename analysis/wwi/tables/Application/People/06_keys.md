---
id: wwi:object:1301579675
subject: wwi/tables/Application/People
item: 06
topic: keys
tier: minimum
summary: PersonID is the declared key, unique; 2,150 unused numbers; LogonName and EmailAddress are near-unique but not declared.
confidence: low
claims: 4
written_by: claude-opus-5-5
written_at: 2026-10-18T20:32:00Z
step: S08-061
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py 102dceeb7d85ec3db493afa75ff1e907c8b3f3a6, profile_tables.py e61ada2547265905e3558722cd127e81fa5cd770, evidence_shared.py 03d3dfbc0522d76aef793a33dc2bc491abc70529
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 5f24e9163953099bd97211216302ba9edbe184de9237880789cd61681982e529
last_checked_at: 2026-10-18T20:32:00Z
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=419f7b85d80b0191 | recheck=the key range changes | text: The key runs from 1 to 3,261 with 2,150 unused numbers.
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=3654cc5be0d96b13 | recheck=a foreign key changes | text: 1 declared foreign key, all enabled and trusted: LastEditedBy -> Application.People.PersonID.
- C3 | type=observed | status=proposed | confidence=low | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=419f7b85d80b0191 | recheck=round 2 confirms the bands | text: PersonID numbers appear to fall in bands by kind of person - staff up to 20, supplier contacts from 21, customer contacts from 1001 - which would explain the unused numbers; read from the ranges other tables refer to, so confirmed only in round 2.
- C4 | type=observed | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=419f7b85d80b0191 | recheck=a duplicate e-mail address appears | text: EmailAddress is not unique: about 1,030 distinct values for 1,110 filled rows.

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

The banding of PersonID is read from the ranges of the people referred to as contacts and editors; it is not declared.

## For a person

None.
