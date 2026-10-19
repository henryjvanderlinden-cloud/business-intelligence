---
id: wwi:fk:FK_Sales_CustomerTransactions_TransactionTypeID_Application_TransactionTypes
subject: wwi/across/relations/Sales.CustomerTransactions.TransactionTypeID__Application.TransactionTypes.TransactionTypeID
item: 27
topic: peculiarities
tier: minimum
summary: Warnings: fan-out, chasm, current versions.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-19T20:31:00Z
step: S08-079
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob e1598587ca50051cb5e35244cfdae309e6e1c028) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: a7888a9841c4129718fc4e064f7db2b7f3056ca4f62d75810b30059a006b52b8
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=1ada314ed586c6e3 | recheck=every new extract | text: Fan-out: joined from Application.TransactionTypes to Sales.CustomerTransactions, a Application.TransactionTypes row repeats up to 70,566 times (median 48,621), so a measure of Application.TransactionTypes summed after the join is counted once per referring row.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=1ada314ed586c6e3 | recheck=every new extract | text: Chasm trap: Application.TransactionTypes also has other referring columns with several rows per parent (Purchasing.SupplierTransactions.TransactionTypeID (up to 2,074 per parent), Warehouse.StockItemTransactions.TransactionTypeID (up to 228,432 per parent)); joining Sales.CustomerTransactions and one of these through Application.TransactionTypes pairs every row of one with every row of the other for the same parent.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=1ada314ed586c6e3 | recheck=the temporal type changes | text: Application.TransactionTypes is system-versioned and the extract holds its current versions: joined in the extract, a row of Sales.CustomerTransactions that names a row of Application.TransactionTypes gets that row's attributes as they are on 2016-06-01, not as they were when the referring row was written; earlier versions are in the history table.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
