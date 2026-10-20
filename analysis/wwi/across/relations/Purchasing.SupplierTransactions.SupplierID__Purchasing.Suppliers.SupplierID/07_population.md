---
id: wwi:fk:FK_Purchasing_SupplierTransactions_SupplierID_Purchasing_Suppliers
subject: wwi/across/relations/Purchasing.SupplierTransactions.SupplierID__Purchasing.Suppliers.SupplierID
item: 07
topic: population
tier: minimum
summary: No orphans; 0 empty; 6 of 13 Purchasing.Suppliers rows unreferenced.
confidence: unknown
claims: 6
written_by: claude-opus-5-5
written_at: 2026-10-20T08:31:00Z
step: S08-095
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 542df9b5000ffee23364ad50df9b8732b2917a3a0a2c6ffc0e28059364cb0f83
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=6feb4a3743493f3b | recheck=every new extract | text: Orphans: 0 rows of Purchasing.SupplierTransactions (0 distinct values) name no row of Purchasing.Suppliers.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=6feb4a3743493f3b | recheck=every new extract | text: SupplierID is filled on every row of Purchasing.SupplierTransactions.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=6feb4a3743493f3b | recheck=every new extract | text: 6 of 13 rows of Purchasing.Suppliers are named by no row of Purchasing.SupplierTransactions.
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=6feb4a3743493f3b | recheck=every new extract | text: By transaction type: Supplier Invoice (5): 2,074 filled; Supplier Payment Issued (7): 366 filled.
- C5 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=6feb4a3743493f3b | recheck=a security policy or a count difference appears | text: Extraction visibility: Purchasing.SupplierTransactions 2,440 rows for the owner, 2,440 for the extracting reader, 2,440 in the extract; Purchasing.Suppliers 13 rows for the owner, 13 for the extracting reader, 13 in the extract; masked columns: Purchasing.Suppliers.{'column_name': 'BankAccountName', 'masking_function': 'default()', 'schema_name': 'Purchasing', 'table_name': 'Suppliers'}, Purchasing.Suppliers.{'column_name': 'BankAccountBranch', 'masking_function': 'default()', 'schema_name': 'Purchasing', 'table_name': 'Suppliers'}, Purchasing.Suppliers.{'column_name': 'BankAccountCode', 'masking_function': 'default()', 'schema_name': 'Purchasing', 'table_name': 'Suppliers'}, Purchasing.Suppliers.{'column_name': 'BankAccountNumber', 'masking_function': 'default()', 'schema_name': 'Purchasing', 'table_name': 'Suppliers'}, Purchasing.Suppliers.{'column_name': 'BankInternationalCode', 'masking_function': 'default()', 'schema_name': 'Purchasing', 'table_name': 'Suppliers'}.
- C6 | type=declared | status=proposed | confidence=unknown | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=6feb4a3743493f3b | recheck=permission to read security policies is granted | text: Whether a row-level security policy filters either table is not established: the extracting reader sees no security policies and may lack the permission to see them; equal counts for owner and reader (as here) argue against a filter.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

Whether row-level security filters either table: the claim with confidence unknown.

## For a person

None.
