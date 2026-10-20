---
id: wwi:fk:FK_Application_SystemParameters_PostalCityID_Application_Cities
subject: wwi/across/relations/Application.SystemParameters.PostalCityID__Application.Cities.CityID
item: 01
topic: granularity
tier: minimum
summary: Application.SystemParameters to Application.Cities; at most one row of Application.SystemParameters per row of Application.Cities in this extract.
confidence: medium
claims: 4
written_by: claude-opus-5-5
written_at: 2026-10-20T08:31:00Z
step: S08-095
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 34bc96e16b2626d7afb28471359a18855c5cd77a76a3e26b32540afc887dffdf
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=814c3d60a8a87a20 | recheck=the foreign key changes | text: Declared foreign key FK_Application_SystemParameters_PostalCityID_Application_Cities from Application.SystemParameters.PostalCityID to Application.Cities.CityID, the primary key of Application.Cities: each row of Application.SystemParameters names at most one row of Application.Cities.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=814c3d60a8a87a20 | recheck=every new extract | text: In this extract 1 of 1 rows of Application.SystemParameters name one of 1 referenced rows of Application.Cities (of 37,940); children per referenced parent: from 1 to 1, median 1; 1 parents have exactly one.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=814c3d60a8a87a20 | recheck=every new extract | text: Joined from Application.SystemParameters to Application.Cities, the result keeps the grain of Application.SystemParameters: one row per row of Application.SystemParameters. Joined the other way, each row of Application.Cities repeats once per row of Application.SystemParameters that names it (C2).
- C4 | type=observed | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=814c3d60a8a87a20 | recheck=a second row refers to the same parent | text: One-to-one on the referenced side in this extract: no row of Application.Cities is named by more than one row of Application.SystemParameters. No unique constraint on PostalCityID declares it.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
