---
id: wwi:fk:FK_Application_Cities_StateProvinceID_Application_StateProvinces
subject: wwi/across/relations/Application.Cities.StateProvinceID__Application.StateProvinces.StateProvinceID
item: 27
topic: peculiarities
tier: minimum
summary: Warnings: fan-out, current versions.
confidence: high
claims: 2
written_by: claude-opus-5-5
written_at: 2026-10-20T08:31:00Z
step: S08-095
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 0359b9f5c4b90450b710ba5d0250ce82e696c1550d527c926b3be656bde893b7
last_checked_at: 2026-10-20T08:31:00Z
last_checked_by: claude-opus-5-5
last_checked_against: 2016-06-01
reviewed_by: none
reviewed_at: none
ruled_by: none
ruled_at: none
supersedes: none
superseded_by: none
recheck_when: every new extract, or a schema change of either table
---

## Claims

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=f2b00b75fd8704a0 | recheck=every new extract | text: Fan-out: joined from Application.StateProvinces to Application.Cities, a Application.StateProvinces row repeats up to 2,395 times (median 645), so a measure of Application.StateProvinces summed after the join is counted once per referring row.
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=f2b00b75fd8704a0 | recheck=the temporal type changes | text: Application.StateProvinces is system-versioned and the extract holds its current versions: joined in the extract, a row of Application.Cities that names a row of Application.StateProvinces gets that row's attributes as they are on 2016-06-01, not as they were when the referring row was written; earlier versions are in the history table.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
