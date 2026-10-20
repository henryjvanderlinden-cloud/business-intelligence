---
id: wwi:fk:FK_Sales_Orders_PickedByPersonID_Application_People
subject: wwi/across/relations/Sales.Orders.PickedByPersonID__Application.People.PersonID
item: 01
topic: granularity
tier: minimum
summary: Many-to-one from Sales.Orders to Application.People; up to 4,042 rows of Sales.Orders per row of Application.People.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-20T05:51:00Z
step: S08-092
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 51805da5178a316233382b96b4193aac7558e4460d848a9ce9951eeae31a4a1e
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=f35899fc41d8d217 | recheck=the foreign key changes | text: Declared foreign key FK_Sales_Orders_PickedByPersonID_Application_People from Sales.Orders.PickedByPersonID to Application.People.PersonID, the primary key of Application.People: each row of Sales.Orders names at most one row of Application.People.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=f35899fc41d8d217 | recheck=every new extract | text: In this extract 63,020 of 73,653 rows of Sales.Orders name one of 19 referenced rows of Application.People (of 1,111); children per referenced parent: from 2,751 to 4,042, median 3,235; 0 parents have exactly one.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=f35899fc41d8d217 | recheck=every new extract | text: Joined from Sales.Orders to Application.People, the result keeps the grain of Sales.Orders: one row per row of Sales.Orders (an inner join drops the 10,633 rows where PickedByPersonID is empty). Joined the other way, each row of Application.People repeats once per row of Sales.Orders that names it (C2).

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
