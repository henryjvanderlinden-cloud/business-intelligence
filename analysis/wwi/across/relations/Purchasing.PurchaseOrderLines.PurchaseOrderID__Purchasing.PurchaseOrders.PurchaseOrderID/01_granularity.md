---
id: wwi:fk:FK_Purchasing_PurchaseOrderLines_PurchaseOrderID_Purchasing_PurchaseOrders
subject: wwi/across/relations/Purchasing.PurchaseOrderLines.PurchaseOrderID__Purchasing.PurchaseOrders.PurchaseOrderID
item: 01
topic: granularity
tier: minimum
summary: Many-to-one from Purchasing.PurchaseOrderLines to Purchasing.PurchaseOrders; up to 34 rows of Purchasing.PurchaseOrderLines per row of Purchasing.PurchaseOrders.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-20T05:51:00Z
step: S08-092
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: e5d38761d28646cbd83a50f38d53d1a443f914b4ea4cb03705ef80bf7b2e33dc
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=b0bb4dad228ddf2a | recheck=the foreign key changes | text: Declared foreign key FK_Purchasing_PurchaseOrderLines_PurchaseOrderID_Purchasing_PurchaseOrders from Purchasing.PurchaseOrderLines.PurchaseOrderID to Purchasing.PurchaseOrders.PurchaseOrderID, the primary key of Purchasing.PurchaseOrders: each row of Purchasing.PurchaseOrderLines names at most one row of Purchasing.PurchaseOrders.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=b0bb4dad228ddf2a | recheck=every new extract | text: In this extract 8,376 of 8,376 rows of Purchasing.PurchaseOrderLines name one of 2,076 referenced rows of Purchasing.PurchaseOrders (of 2,076); children per referenced parent: from 1 to 34, median 3; 150 parents have exactly one.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=b0bb4dad228ddf2a | recheck=every new extract | text: Joined from Purchasing.PurchaseOrderLines to Purchasing.PurchaseOrders, the result keeps the grain of Purchasing.PurchaseOrderLines: one row per row of Purchasing.PurchaseOrderLines. Joined the other way, each row of Purchasing.PurchaseOrders repeats once per row of Purchasing.PurchaseOrderLines that names it (C2).

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
