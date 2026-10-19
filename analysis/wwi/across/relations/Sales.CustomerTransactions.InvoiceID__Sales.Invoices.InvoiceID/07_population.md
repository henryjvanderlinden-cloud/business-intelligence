---
id: wwi:fk:FK_Sales_CustomerTransactions_InvoiceID_Sales_Invoices
subject: wwi/across/relations/Sales.CustomerTransactions.InvoiceID__Sales.Invoices.InvoiceID
item: 07
topic: population
tier: minimum
summary: No orphans; 26,676 empty; 0 of 70,566 Sales.Invoices rows unreferenced.
confidence: unknown
claims: 6
written_by: claude-opus-5-5
written_at: 2026-10-19T20:31:00Z
step: S08-079
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob e1598587ca50051cb5e35244cfdae309e6e1c028) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 2b4f18335a52663fe6cf5888eeea86b4017a10df501e0f58e111ff1148ff2e07
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=32b2eaffd73eb69a | recheck=every new extract | text: Orphans: 0 rows of Sales.CustomerTransactions (0 distinct values) name no row of Sales.Invoices.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=32b2eaffd73eb69a | recheck=every new extract | text: Optional: InvoiceID is empty on 26,676 of 97,242 rows of Sales.CustomerTransactions, as its declaration allows.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=32b2eaffd73eb69a | recheck=every new extract | text: 0 of 70,566 rows of Sales.Invoices are named by no row of Sales.CustomerTransactions.
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=32b2eaffd73eb69a | recheck=every new extract | text: By transaction type: Customer Invoice (1): 70,566 filled; Customer Payment Received (3): 26,676 empty.
- C5 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=32b2eaffd73eb69a | recheck=a security policy or a count difference appears | text: Extraction visibility: Sales.CustomerTransactions 97,242 rows for the owner, 97,242 for the extracting reader, 97,242 in the extract; Sales.Invoices 70,566 rows for the owner, 70,566 for the extracting reader, 70,566 in the extract; masked columns: none.
- C6 | type=declared | status=proposed | confidence=unknown | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=32b2eaffd73eb69a | recheck=permission to read security policies is granted | text: Whether a row-level security policy filters either table is not established: the extracting reader sees no security policies and may lack the permission to see them; equal counts for owner and reader (as here) argue against a filter.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

Whether row-level security filters either table: the claim with confidence unknown.

## For a person

None.
