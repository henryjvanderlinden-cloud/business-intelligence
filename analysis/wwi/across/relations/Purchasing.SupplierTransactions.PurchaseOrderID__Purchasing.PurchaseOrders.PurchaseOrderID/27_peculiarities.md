---
id: wwi:fk:FK_Purchasing_SupplierTransactions_PurchaseOrderID_Purchasing_PurchaseOrders
subject: wwi/across/relations/Purchasing.SupplierTransactions.PurchaseOrderID__Purchasing.PurchaseOrders.PurchaseOrderID
item: 27
topic: peculiarities
tier: minimum
summary: Warnings: one-to-one not enforced, see claims.
confidence: medium
claims: 2
written_by: claude-opus-5-5
written_at: 2026-10-19T20:31:00Z
step: S08-079
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob e1598587ca50051cb5e35244cfdae309e6e1c028) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 53939878d4705e61c16bdf86d6ceb01b27fa5dfaf25b382fcafe47549cacadf9
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

- C1 | type=observed | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=b04c588a7e630450 | recheck=a second row refers to the same parent | text: One row of Purchasing.SupplierTransactions per row of Purchasing.PurchaseOrders holds only in this extract: nothing declares PurchaseOrderID unique, so several referring rows per parent are allowed, and a join that counts on one per parent rests on the extract.
- C2 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=b04c588a7e630450 | recheck=every new extract, or a description changes | text: As on the customer side, entries of type Supplier Payment Issued leave PurchaseOrderID empty (07) and the table has no other declared reference to an invoice or order: which supplier invoices a payment settles is not recorded by key.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
