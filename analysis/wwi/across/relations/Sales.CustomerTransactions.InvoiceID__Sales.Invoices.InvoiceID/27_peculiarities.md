---
id: wwi:fk:FK_Sales_CustomerTransactions_InvoiceID_Sales_Invoices
subject: wwi/across/relations/Sales.CustomerTransactions.InvoiceID__Sales.Invoices.InvoiceID
item: 27
topic: peculiarities
tier: minimum
summary: Warnings: one-to-one not enforced, see claims.
confidence: medium
claims: 2
written_by: claude-opus-5-5
written_at: 2026-10-20T05:51:00Z
step: S08-092
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 2b4f18335a52663fe6cf5888eeea86b4017a10df501e0f58e111ff1148ff2e07
last_checked_at: 2026-10-20T05:51:00Z
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

- C1 | type=observed | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=32b2eaffd73eb69a | recheck=a second row refers to the same parent | text: One row of Sales.CustomerTransactions per row of Sales.Invoices holds only in this extract: nothing declares InvoiceID unique, so several referring rows per parent are allowed, and a join that counts on one per parent rests on the extract.
- C2 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=32b2eaffd73eb69a | recheck=every new extract, or a description changes | text: Which invoices a payment settles is not recorded by key: payment entries leave InvoiceID empty (07), Sales.CustomerTransactions has no other declared foreign key to Sales.Invoices (06 and its declaration), and it has no undeclared ...ID column (across/candidates.md). Whether a non-key column links them is not tested here.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
