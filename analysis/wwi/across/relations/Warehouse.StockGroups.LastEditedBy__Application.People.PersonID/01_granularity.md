---
id: wwi:fk:FK_Warehouse_StockGroups_Application_People
subject: wwi/across/relations/Warehouse.StockGroups.LastEditedBy__Application.People.PersonID
item: 01
topic: granularity
tier: minimum
summary: Many-to-one from Warehouse.StockGroups to Application.People; up to 9 rows of Warehouse.StockGroups per row of Application.People.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-20T08:31:00Z
step: S08-095
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: b791d6bd103ae24d5893d3486c289e38db44dfdfd12ba70f91fc840ba04f2c26
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=3db7bb0b628f9333 | recheck=the foreign key changes | text: Declared foreign key FK_Warehouse_StockGroups_Application_People from Warehouse.StockGroups.LastEditedBy to Application.People.PersonID, the primary key of Application.People: each row of Warehouse.StockGroups names at most one row of Application.People.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=3db7bb0b628f9333 | recheck=every new extract | text: In this extract 10 of 10 rows of Warehouse.StockGroups name one of 2 referenced rows of Application.People (of 1,111); children per referenced parent: from 1 to 9, median 5; 1 parents have exactly one.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=3db7bb0b628f9333 | recheck=every new extract | text: Joined from Warehouse.StockGroups to Application.People, the result keeps the grain of Warehouse.StockGroups: one row per row of Warehouse.StockGroups. Joined the other way, each row of Application.People repeats once per row of Warehouse.StockGroups that names it (C2).

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
