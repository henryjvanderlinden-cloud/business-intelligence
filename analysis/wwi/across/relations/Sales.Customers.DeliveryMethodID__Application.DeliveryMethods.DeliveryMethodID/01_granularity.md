---
id: wwi:fk:FK_Sales_Customers_DeliveryMethodID_Application_DeliveryMethods
subject: wwi/across/relations/Sales.Customers.DeliveryMethodID__Application.DeliveryMethods.DeliveryMethodID
item: 01
topic: granularity
tier: minimum
summary: Many-to-one from Sales.Customers to Application.DeliveryMethods; up to 663 rows of Sales.Customers per row of Application.DeliveryMethods.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-20T05:51:00Z
step: S08-092
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 53292ed2d24b8a2b01c2edba3c93793b0f57a751260b0fe45c641df232692f49
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=49eabecb8c2d044c | recheck=the foreign key changes | text: Declared foreign key FK_Sales_Customers_DeliveryMethodID_Application_DeliveryMethods from Sales.Customers.DeliveryMethodID to Application.DeliveryMethods.DeliveryMethodID, the primary key of Application.DeliveryMethods: each row of Sales.Customers names at most one row of Application.DeliveryMethods.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=49eabecb8c2d044c | recheck=every new extract | text: In this extract 663 of 663 rows of Sales.Customers name one of 1 referenced rows of Application.DeliveryMethods (of 10); children per referenced parent: from 663 to 663, median 663; 0 parents have exactly one.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=49eabecb8c2d044c | recheck=every new extract | text: Joined from Sales.Customers to Application.DeliveryMethods, the result keeps the grain of Sales.Customers: one row per row of Sales.Customers. Joined the other way, each row of Application.DeliveryMethods repeats once per row of Sales.Customers that names it (C2).

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
