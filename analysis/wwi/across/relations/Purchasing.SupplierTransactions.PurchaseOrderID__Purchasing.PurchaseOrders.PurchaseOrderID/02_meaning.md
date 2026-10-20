---
id: wwi:fk:FK_Purchasing_SupplierTransactions_PurchaseOrderID_Purchasing_PurchaseOrders
subject: wwi/across/relations/Purchasing.SupplierTransactions.PurchaseOrderID__Purchasing.PurchaseOrders.PurchaseOrderID
item: 02
topic: meaning
tier: minimum
summary: The purchase order a supplier invoice belongs to; payments name none.
confidence: medium
claims: 2
written_by: claude-opus-5-5
written_at: 2026-10-20T05:51:00Z
step: S08-092
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 53939878d4705e61c16bdf86d6ceb01b27fa5dfaf25b382fcafe47549cacadf9
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

- C1 | type=declared | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=b04c588a7e630450 | recheck=the description changes | text: The source describes Purchasing.SupplierTransactions.PurchaseOrderID as "ID of an purchase order (for transactions associated with a purchase order)".
- C2 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=b04c588a7e630450 | recheck=every new extract, or a description changes | text: For the 2,074 supplier invoices, the purchase order invoiced, one invoice per order in this extract (01); the 366 payments leave it empty (07). Two purchase orders have no supplier invoice.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
