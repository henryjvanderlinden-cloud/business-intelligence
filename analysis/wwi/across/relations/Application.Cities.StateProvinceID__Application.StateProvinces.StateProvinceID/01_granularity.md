---
id: wwi:fk:FK_Application_Cities_StateProvinceID_Application_StateProvinces
subject: wwi/across/relations/Application.Cities.StateProvinceID__Application.StateProvinces.StateProvinceID
item: 01
topic: granularity
tier: minimum
summary: Many-to-one from Application.Cities to Application.StateProvinces; up to 2,395 rows of Application.Cities per row of Application.StateProvinces.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-20T05:51:00Z
step: S08-092
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 0359b9f5c4b90450b710ba5d0250ce82e696c1550d527c926b3be656bde893b7
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=f2b00b75fd8704a0 | recheck=the foreign key changes | text: Declared foreign key FK_Application_Cities_StateProvinceID_Application_StateProvinces from Application.Cities.StateProvinceID to Application.StateProvinces.StateProvinceID, the primary key of Application.StateProvinces: each row of Application.Cities names at most one row of Application.StateProvinces.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=f2b00b75fd8704a0 | recheck=every new extract | text: In this extract 37,940 of 37,940 rows of Application.Cities name one of 53 referenced rows of Application.StateProvinces (of 53); children per referenced parent: from 1 to 2,395, median 645; 1 parents have exactly one.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=f2b00b75fd8704a0 | recheck=every new extract | text: Joined from Application.Cities to Application.StateProvinces, the result keeps the grain of Application.Cities: one row per row of Application.Cities. Joined the other way, each row of Application.StateProvinces repeats once per row of Application.Cities that names it (C2).

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
