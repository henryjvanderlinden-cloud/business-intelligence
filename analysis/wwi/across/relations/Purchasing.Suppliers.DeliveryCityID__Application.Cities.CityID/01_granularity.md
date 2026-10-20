---
id: wwi:fk:FK_Purchasing_Suppliers_DeliveryCityID_Application_Cities
subject: wwi/across/relations/Purchasing.Suppliers.DeliveryCityID__Application.Cities.CityID
item: 01
topic: granularity
tier: minimum
summary: Many-to-one from Purchasing.Suppliers to Application.Cities; up to 2 rows of Purchasing.Suppliers per row of Application.Cities.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-20T05:51:00Z
step: S08-092
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 6731121b96b01e540a87f05789e0d036d5bff51807a760c46d45f6643e765b1b
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=63940b003f3cb635 | recheck=the foreign key changes | text: Declared foreign key FK_Purchasing_Suppliers_DeliveryCityID_Application_Cities from Purchasing.Suppliers.DeliveryCityID to Application.Cities.CityID, the primary key of Application.Cities: each row of Purchasing.Suppliers names at most one row of Application.Cities.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=63940b003f3cb635 | recheck=every new extract | text: In this extract 13 of 13 rows of Purchasing.Suppliers name one of 12 referenced rows of Application.Cities (of 37,940); children per referenced parent: from 1 to 2, median 1; 11 parents have exactly one.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=63940b003f3cb635 | recheck=every new extract | text: Joined from Purchasing.Suppliers to Application.Cities, the result keeps the grain of Purchasing.Suppliers: one row per row of Purchasing.Suppliers. Joined the other way, each row of Application.Cities repeats once per row of Purchasing.Suppliers that names it (C2).

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
