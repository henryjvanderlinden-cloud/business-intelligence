---
id: wwi:fk:FK_Sales_CustomerTransactions_PaymentMethodID_Application_PaymentMethods
subject: wwi/across/relations/Sales.CustomerTransactions.PaymentMethodID__Application.PaymentMethods.PaymentMethodID
item: 07
topic: population
tier: minimum
summary: No orphans; 70,566 empty; 3 of 4 Application.PaymentMethods rows unreferenced.
confidence: unknown
claims: 6
written_by: claude-opus-5-5
written_at: 2026-10-19T20:31:00Z
step: S08-079
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob e1598587ca50051cb5e35244cfdae309e6e1c028) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 44fef738b353833eca086d59ebea46802593b4418a1a329198d32862bcc3bfcf
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=59ce7f1dd67ff9d6 | recheck=every new extract | text: Orphans: 0 rows of Sales.CustomerTransactions (0 distinct values) name no row of Application.PaymentMethods.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=59ce7f1dd67ff9d6 | recheck=every new extract | text: Optional: PaymentMethodID is empty on 70,566 of 97,242 rows of Sales.CustomerTransactions, as its declaration allows.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=59ce7f1dd67ff9d6 | recheck=every new extract | text: 3 of 4 rows of Application.PaymentMethods are named by no row of Sales.CustomerTransactions.
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=59ce7f1dd67ff9d6 | recheck=every new extract | text: By transaction type: Customer Invoice (1): 70,566 empty; Customer Payment Received (3): 26,676 filled.
- C5 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=59ce7f1dd67ff9d6 | recheck=a security policy or a count difference appears | text: Extraction visibility: Application.PaymentMethods 4 rows for the owner, 4 for the extracting reader, 4 in the extract; Sales.CustomerTransactions 97,242 rows for the owner, 97,242 for the extracting reader, 97,242 in the extract; masked columns: none.
- C6 | type=declared | status=proposed | confidence=unknown | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=59ce7f1dd67ff9d6 | recheck=permission to read security policies is granted | text: Whether a row-level security policy filters either table is not established: the extracting reader sees no security policies and may lack the permission to see them; equal counts for owner and reader (as here) argue against a filter.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

Whether row-level security filters either table: the claim with confidence unknown.

## For a person

None.
