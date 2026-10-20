---
id: wwi:fk:FK_Warehouse_StockItemTransactions_InvoiceID_Sales_Invoices
subject: wwi/across/relations/Warehouse.StockItemTransactions.InvoiceID__Sales.Invoices.InvoiceID
item: 27
topic: peculiarities
tier: minimum
summary: Warnings: fan-out, chasm.
confidence: high
claims: 2
written_by: claude-opus-5-5
written_at: 2026-10-20T05:51:00Z
step: S08-092
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: e6048a362329a61d413f431238613a8db164c4631242fadf46d6f32e53a685f4
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=e2856474e75a7c5b | recheck=every new extract | text: Fan-out: joined from Sales.Invoices to Warehouse.StockItemTransactions, a Sales.Invoices row repeats up to 5 times (median 3), so a measure of Sales.Invoices summed after the join is counted once per referring row.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=e2856474e75a7c5b | recheck=every new extract | text: Chasm trap: Sales.Invoices also has other referring columns with several rows per parent (Sales.InvoiceLines.InvoiceID (up to 5 per parent)); joining Warehouse.StockItemTransactions and one of these through Sales.Invoices pairs every row of one with every row of the other for the same parent.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
