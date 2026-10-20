---
id: wwi:fk:FK_Application_Cities_StateProvinceID_Application_StateProvinces
subject: wwi/across/relations/Application.Cities.StateProvinceID__Application.StateProvinces.StateProvinceID
item: 06
topic: keys
tier: minimum
summary: Application.Cities.StateProvinceID refers to the primary key Application.StateProvinces.StateProvinceID, enforced.
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=f2b00b75fd8704a0 | recheck=the foreign key changes | text: Child side: Application.Cities.StateProvinceID, int, not nullable; a foreign key, enabled and trusted; on delete no action.
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=f2b00b75fd8704a0 | recheck=the primary key changes | text: Parent side: Application.StateProvinces.StateProvinceID, the declared primary key of Application.StateProvinces.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=f2b00b75fd8704a0 | recheck=every new extract | text: No other column of Application.StateProvinces that is unique in this extract holds all values of StateProvinceID: the primary key is the only key the values fit.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
