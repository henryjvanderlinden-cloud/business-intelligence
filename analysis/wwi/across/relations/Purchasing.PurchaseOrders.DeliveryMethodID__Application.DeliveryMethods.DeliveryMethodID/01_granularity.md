---
id: wwi:fk:FK_Purchasing_PurchaseOrders_DeliveryMethodID_Application_DeliveryMethods
subject: wwi/across/relations/Purchasing.PurchaseOrders.DeliveryMethodID__Application.DeliveryMethods.DeliveryMethodID
item: 01
topic: granularity
tier: minimum
summary: Many-to-one from Purchasing.PurchaseOrders to Application.DeliveryMethods; up to 1,066 rows of Purchasing.PurchaseOrders per row of Application.DeliveryMethods.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-19T20:31:00Z
step: S08-079
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob e1598587ca50051cb5e35244cfdae309e6e1c028) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: b120f7c462ffd9128079313e0229237102d0854c0084fbe70afac7a4a0f9db4d
last_checked_at: 2026-10-19T20:31:00Z
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=a7dd3c4f48a17ec2 | recheck=the foreign key changes | text: Declared foreign key FK_Purchasing_PurchaseOrders_DeliveryMethodID_Application_DeliveryMethods from Purchasing.PurchaseOrders.DeliveryMethodID to Application.DeliveryMethods.DeliveryMethodID, the primary key of Application.DeliveryMethods: each row of Purchasing.PurchaseOrders names at most one row of Application.DeliveryMethods.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=a7dd3c4f48a17ec2 | recheck=every new extract | text: In this extract 2,076 of 2,076 rows of Purchasing.PurchaseOrders name one of 5 referenced rows of Application.DeliveryMethods (of 10); children per referenced parent: from 1 to 1,066, median 13; 1 parents have exactly one.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=a7dd3c4f48a17ec2 | recheck=every new extract | text: Joined from Purchasing.PurchaseOrders to Application.DeliveryMethods, the result keeps the grain of Purchasing.PurchaseOrders: one row per row of Purchasing.PurchaseOrders. Joined the other way, each row of Application.DeliveryMethods repeats once per row of Purchasing.PurchaseOrders that names it (C2).

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
