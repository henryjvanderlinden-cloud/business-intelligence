---
id: wwi:relation:Warehouse.StockItemTransactions.InvoiceID.StockItemID__Sales.InvoiceLines.InvoiceID.StockItemID
subject: wwi/across/relations/Warehouse.StockItemTransactions.InvoiceID.StockItemID__Sales.InvoiceLines.InvoiceID.StockItemID
item: 06
topic: keys
tier: minimum
summary: Undeclared: Warehouse.StockItemTransactions.InvoiceID + StockItemID against Sales.InvoiceLines.InvoiceID + StockItemID, unique in this extract.
confidence: high
claims: 2
written_by: claude-opus-5-5
written_at: 2026-10-20T08:31:00Z
step: S08-095
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: ac653f2ac4f3bbe7f75773db1b1adb13da2a66c7420490cf50e89e440a7363e5
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=761a808f00d99ece | recheck=a constraint is declared | text: Child side: Warehouse.StockItemTransactions.InvoiceID + StockItemID, not declared as a foreign key; parent side: Sales.InvoiceLines.InvoiceID + StockItemID, not declared unique.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=761a808f00d99ece | recheck=every new extract | text: In this extract InvoiceID + StockItemID is unique over all 228,432 rows of Sales.InvoiceLines.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
