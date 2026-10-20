---
id: wwi:fk:FK_Application_SystemParameters_PostalCityID_Application_Cities
subject: wwi/across/relations/Application.SystemParameters.PostalCityID__Application.Cities.CityID
item: 27
topic: peculiarities
tier: minimum
summary: Warnings: roles, current versions.
confidence: high
claims: 2
written_by: claude-opus-5-5
written_at: 2026-10-20T05:51:00Z
step: S08-092
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 34bc96e16b2626d7afb28471359a18855c5cd77a76a3e26b32540afc887dffdf
last_checked_at: 2026-10-20T05:51:00Z
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=814c3d60a8a87a20 | recheck=a foreign key changes | text: Several paths between the same two tables: Application.SystemParameters also refers to Application.Cities through DeliveryCityID; a join of the two must say which role it means.
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=814c3d60a8a87a20 | recheck=the temporal type changes | text: Application.Cities is system-versioned and the extract holds its current versions: joined in the extract, a row of Application.SystemParameters that names a row of Application.Cities gets that row's attributes as they are on 2016-06-01, not as they were when the referring row was written; earlier versions are in the history table.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
