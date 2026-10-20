---
id: wwi:relation:Warehouse.StockItemTransactions.InvoiceID.StockItemID__Sales.InvoiceLines.InvoiceID.StockItemID
subject: wwi/across/relations/Warehouse.StockItemTransactions.InvoiceID.StockItemID__Sales.InvoiceLines.InvoiceID.StockItemID
item: 27
topic: peculiarities
tier: minimum
summary: Warnings: header join.
confidence: high
claims: 1
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=761a808f00d99ece | recheck=every new extract | text: Header join: joined on InvoiceID alone, the two tables give 847,672 rows instead of the 228,432 that the full combination gives: every referring row is paired with every row of Sales.InvoiceLines for the same InvoiceID.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence. The tests for roles, chasm traps, system-versioning and two routes are run on declared foreign keys only; for this undeclared relation they were not run.

## Uncertainties

None.

## For a person

None.
