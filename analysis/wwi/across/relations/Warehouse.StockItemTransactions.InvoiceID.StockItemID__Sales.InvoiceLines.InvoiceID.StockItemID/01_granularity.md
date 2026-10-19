---
id: wwi:relation:Warehouse.StockItemTransactions.InvoiceID.StockItemID__Sales.InvoiceLines.InvoiceID.StockItemID
subject: wwi/across/relations/Warehouse.StockItemTransactions.InvoiceID.StockItemID__Sales.InvoiceLines.InvoiceID.StockItemID
item: 01
topic: granularity
tier: minimum
summary: Warehouse.StockItemTransactions to Sales.InvoiceLines; at most one row of Warehouse.StockItemTransactions per row of Sales.InvoiceLines in this extract.
confidence: medium
claims: 4
written_by: claude-opus-5-5
written_at: 2026-10-19T20:31:00Z
step: S08-079
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob e1598587ca50051cb5e35244cfdae309e6e1c028) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: ac653f2ac4f3bbe7f75773db1b1adb13da2a66c7420490cf50e89e440a7363e5
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=761a808f00d99ece | recheck=a constraint is declared | text: No foreign key or unique constraint declares this relation; Sales.InvoiceLines.InvoiceID + StockItemID is unique in the extract.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=761a808f00d99ece | recheck=every new extract | text: In this extract 228,432 of 236,843 rows of Warehouse.StockItemTransactions name one of 228,432 referenced rows of Sales.InvoiceLines (of 228,432); children per referenced parent: from 1 to 1, median 1; 228,432 parents have exactly one.
- C3 | type=observed | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=761a808f00d99ece | recheck=every new extract | text: Joined from Warehouse.StockItemTransactions to Sales.InvoiceLines, the result keeps the grain of Warehouse.StockItemTransactions: one row per row of Warehouse.StockItemTransactions (an inner join drops the 8,411 rows where InvoiceID + StockItemID is empty). Joined the other way, each row of Sales.InvoiceLines repeats once per row of Warehouse.StockItemTransactions that names it (C2); this rests on the parent combination being unique in this extract, which nothing declares.
- C4 | type=observed | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=761a808f00d99ece | recheck=a second row refers to the same parent | text: One-to-one on the referenced side in this extract: no row of Sales.InvoiceLines is named by more than one row of Warehouse.StockItemTransactions. No unique constraint on InvoiceID + StockItemID declares it.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
