---
id: wwi:fk:FK_Sales_CustomerTransactions_CustomerID_Sales_Customers
subject: wwi/across/relations/Sales.CustomerTransactions.CustomerID__Sales.Customers.CustomerID
item: 02
topic: meaning
tier: minimum
summary: The customer the ledger entry is booked on: the bill-to customer, not the customer delivered to.
confidence: medium
claims: 2
written_by: claude-opus-5-5
written_at: 2026-10-20T08:31:00Z
step: S08-095
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: dba303311da3e1c6d0f8dd3ca4dc6c701c7bbcbc7c941309c872bb30aa2359c5
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

- C1 | type=declared | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=4dd2845ea6a5f4f9 | recheck=the description changes | text: The source describes Sales.CustomerTransactions.CustomerID as "Customer for this transaction".
- C2 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=4dd2845ea6a5f4f9 | recheck=every new extract, or a description changes | text: The customer whose account the entry is booked on. For the 70,566 invoice entries it equals the invoice's BillToCustomerID on every row and the invoice's CustomerID on only 26,287 (27): the ledger is kept on the customer billed.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
