---
id: wwi:fk:FK_Purchasing_PurchaseOrderLines_PurchaseOrderID_Purchasing_PurchaseOrders
subject: wwi/across/relations/Purchasing.PurchaseOrderLines.PurchaseOrderID__Purchasing.PurchaseOrders.PurchaseOrderID
item: 03
topic: temporal
tier: best-effort
summary: Point in time: parent not versioned; dates: child date same day as parent date 8,376.
confidence: high
claims: 2
written_by: claude-opus-5-5
written_at: 2026-10-20T08:31:00Z
step: S08-095
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: e5d38761d28646cbd83a50f38d53d1a443f914b4ea4cb03705ef80bf7b2e33dc
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=a1d7f559f4f6a7e1 | recheck=the temporal type changes | text: Purchasing.PurchaseOrders is not system-versioned: an earlier state of a row is not kept, so a row of Purchasing.PurchaseOrderLines can only be joined to the row as it is in the extract.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=a1d7f559f4f6a7e1 | recheck=every new extract | text: Date order on 8,376 rows: child date same day as parent date 8,376; days from Purchasing.PurchaseOrders.OrderDate to Purchasing.PurchaseOrders.OrderDate via PurchaseOrderID: from 0 to 0, median 0.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
