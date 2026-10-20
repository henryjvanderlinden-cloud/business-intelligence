---
id: wwi:fk:FK_Sales_CustomerTransactions_InvoiceID_Sales_Invoices
subject: wwi/across/relations/Sales.CustomerTransactions.InvoiceID__Sales.Invoices.InvoiceID
item: 02
topic: meaning
tier: minimum
summary: The invoice an invoice entry books; payments name no invoice, so which invoices a payment settles is not recorded by key.
confidence: medium
claims: 2
written_by: claude-opus-5-5
written_at: 2026-10-20T08:31:00Z
step: S08-095
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 2b4f18335a52663fe6cf5888eeea86b4017a10df501e0f58e111ff1148ff2e07
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

- C1 | type=declared | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=32b2eaffd73eb69a | recheck=the description changes | text: The source describes Sales.CustomerTransactions.InvoiceID as "ID of an invoice (for transactions associated with an invoice)".
- C2 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=32b2eaffd73eb69a | recheck=every new extract, or a description changes | text: For the 70,566 entries of type Customer Invoice, the invoice booked, one entry per invoice in this extract (01). The 26,676 entries of type Customer Payment Received leave it empty (07).

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
