---
id: wwi:fk:FK_Warehouse_StockItemTransactions_CustomerID_Sales_Customers
subject: wwi/across/relations/Warehouse.StockItemTransactions.CustomerID__Sales.Customers.CustomerID
item: 02
topic: meaning
tier: minimum
summary: The customer the stock was issued to: the invoice's (delivered-to) customer, not the customer billed.
confidence: medium
claims: 2
written_by: claude-opus-5-5
written_at: 2026-10-20T08:31:00Z
step: S08-095
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 7e9f021b9e3ca91f628a9af5c51ebb0f736fe0deaa5af8eaa9e0254293209e21
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

- C1 | type=declared | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=6dc7199c652dc08f | recheck=the description changes | text: The source describes Warehouse.StockItemTransactions.CustomerID as "Customer for this transaction (if applicable)".
- C2 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=6dc7199c652dc08f | recheck=every new extract, or a description changes | text: For stock issues, the customer the goods went to: it equals the invoice's CustomerID on all 228,432 rows where both are filled and its BillToCustomerID on only 85,160 (27). Filled on all 228,432 Stock Issue rows; empty on the 8,367 Stock Receipt and 44 stocktake-adjustment rows (07).

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
