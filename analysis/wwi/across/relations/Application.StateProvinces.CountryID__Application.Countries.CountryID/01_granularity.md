---
id: wwi:fk:FK_Application_StateProvinces_CountryID_Application_Countries
subject: wwi/across/relations/Application.StateProvinces.CountryID__Application.Countries.CountryID
item: 01
topic: granularity
tier: minimum
summary: Many-to-one from Application.StateProvinces to Application.Countries; up to 53 rows of Application.StateProvinces per row of Application.Countries.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-20T05:51:00Z
step: S08-092
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 0765d4299c45b3422ed4ffa9d158da0b45a09e2183bde8e61f5f0224242db0ec
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=fef9ba94ef9792ab | recheck=the foreign key changes | text: Declared foreign key FK_Application_StateProvinces_CountryID_Application_Countries from Application.StateProvinces.CountryID to Application.Countries.CountryID, the primary key of Application.Countries: each row of Application.StateProvinces names at most one row of Application.Countries.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=fef9ba94ef9792ab | recheck=every new extract | text: In this extract 53 of 53 rows of Application.StateProvinces name one of 1 referenced rows of Application.Countries (of 190); children per referenced parent: from 53 to 53, median 53; 0 parents have exactly one.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=fef9ba94ef9792ab | recheck=every new extract | text: Joined from Application.StateProvinces to Application.Countries, the result keeps the grain of Application.StateProvinces: one row per row of Application.StateProvinces. Joined the other way, each row of Application.Countries repeats once per row of Application.StateProvinces that names it (C2).

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
