---
id: wwi:fk:FK_Sales_Invoices_BillToCustomerID_Sales_Customers
subject: wwi/across/relations/Sales.Invoices.BillToCustomerID__Sales.Customers.CustomerID
item: 07
topic: population
tier: minimum
summary: No orphans; 0 empty; 400 of 663 Sales.Customers rows unreferenced.
confidence: unknown
claims: 5
written_by: claude-opus-5-5
written_at: 2026-10-20T08:31:00Z
step: S08-095
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 2ce83d3e97200a06f4d8df60b09a4948373b555ba7aa8f288282685f535571a5
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=1645fee7c1580915 | recheck=every new extract | text: Orphans: 0 rows of Sales.Invoices (0 distinct values) name no row of Sales.Customers.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=1645fee7c1580915 | recheck=every new extract | text: BillToCustomerID is filled on every row of Sales.Invoices.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=1645fee7c1580915 | recheck=every new extract | text: 400 of 663 rows of Sales.Customers are named by no row of Sales.Invoices.
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=1645fee7c1580915 | recheck=a security policy or a count difference appears | text: Extraction visibility: Sales.Customers 663 rows for the owner, 663 for the extracting reader, 663 in the extract; Sales.Invoices 70,566 rows for the owner, 70,566 for the extracting reader, 70,566 in the extract; masked columns: none.
- C5 | type=declared | status=proposed | confidence=unknown | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=1645fee7c1580915 | recheck=permission to read security policies is granted | text: Whether a row-level security policy filters either table is not established: the extracting reader sees no security policies and may lack the permission to see them; equal counts for owner and reader (as here) argue against a filter.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

Whether row-level security filters either table: the claim with confidence unknown.

## For a person

None.
