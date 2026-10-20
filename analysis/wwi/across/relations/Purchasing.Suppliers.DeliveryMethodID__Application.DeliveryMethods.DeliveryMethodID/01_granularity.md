---
id: wwi:fk:FK_Purchasing_Suppliers_DeliveryMethodID_Application_DeliveryMethods
subject: wwi/across/relations/Purchasing.Suppliers.DeliveryMethodID__Application.DeliveryMethods.DeliveryMethodID
item: 01
topic: granularity
tier: minimum
summary: Many-to-one from Purchasing.Suppliers to Application.DeliveryMethods; up to 3 rows of Purchasing.Suppliers per row of Application.DeliveryMethods.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-20T08:31:00Z
step: S08-095
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 275b0d705d1fc538a764af021043dc17aa18c3c941bfde7def277e6f3f916408
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=32271a64033671f4 | recheck=the foreign key changes | text: Declared foreign key FK_Purchasing_Suppliers_DeliveryMethodID_Application_DeliveryMethods from Purchasing.Suppliers.DeliveryMethodID to Application.DeliveryMethods.DeliveryMethodID, the primary key of Application.DeliveryMethods: each row of Purchasing.Suppliers names at most one row of Application.DeliveryMethods.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=32271a64033671f4 | recheck=every new extract | text: In this extract 9 of 13 rows of Purchasing.Suppliers name one of 5 referenced rows of Application.DeliveryMethods (of 10); children per referenced parent: from 1 to 3, median 1; 3 parents have exactly one.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=32271a64033671f4 | recheck=every new extract | text: Joined from Purchasing.Suppliers to Application.DeliveryMethods, the result keeps the grain of Purchasing.Suppliers: one row per row of Purchasing.Suppliers (an inner join drops the 4 rows where DeliveryMethodID is empty). Joined the other way, each row of Application.DeliveryMethods repeats once per row of Purchasing.Suppliers that names it (C2).

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
