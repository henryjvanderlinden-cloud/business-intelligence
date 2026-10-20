---
id: wwi:fk:FK_Purchasing_PurchaseOrders_DeliveryMethodID_Application_DeliveryMethods
subject: wwi/across/relations/Purchasing.PurchaseOrders.DeliveryMethodID__Application.DeliveryMethods.DeliveryMethodID
item: 27
topic: peculiarities
tier: minimum
summary: Warnings: fan-out, chasm, current versions, copy.
confidence: high
claims: 4
written_by: claude-opus-5-5
written_at: 2026-10-20T08:31:00Z
step: S08-095
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: b120f7c462ffd9128079313e0229237102d0854c0084fbe70afac7a4a0f9db4d
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=a7dd3c4f48a17ec2 | recheck=every new extract | text: Fan-out: joined from Application.DeliveryMethods to Purchasing.PurchaseOrders, a Application.DeliveryMethods row repeats up to 1,066 times (median 13), so a measure of Application.DeliveryMethods summed after the join is counted once per referring row.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=a7dd3c4f48a17ec2 | recheck=every new extract | text: Chasm trap: Application.DeliveryMethods also has other referring columns with several rows per parent (Purchasing.Suppliers.DeliveryMethodID (up to 3 per parent), Sales.Customers.DeliveryMethodID (up to 663 per parent), Sales.Invoices.DeliveryMethodID (up to 70,566 per parent)); joining Purchasing.PurchaseOrders and one of these through Application.DeliveryMethods pairs every row of one with every row of the other for the same parent.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=a7dd3c4f48a17ec2 | recheck=the temporal type changes | text: Application.DeliveryMethods is system-versioned and the extract holds its current versions: joined in the extract, a row of Purchasing.PurchaseOrders that names a row of Application.DeliveryMethods gets that row's attributes as they are on 2016-06-01, not as they were when the referring row was written; earlier versions are in the history table.
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=a7dd3c4f48a17ec2 | recheck=every new extract | text: Two routes agree: on all 2,076 rows where both are filled, DeliveryMethodID names the same row of Application.DeliveryMethods as the route SupplierID -> Purchasing.Suppliers.DeliveryMethodID: in this extract DeliveryMethodID repeats that value.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
