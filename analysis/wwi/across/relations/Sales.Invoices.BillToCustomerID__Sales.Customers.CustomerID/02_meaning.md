---
id: wwi:fk:FK_Sales_Invoices_BillToCustomerID_Sales_Customers
subject: wwi/across/relations/Sales.Invoices.BillToCustomerID__Sales.Customers.CustomerID
item: 02
topic: meaning
tier: minimum
summary: The customer billed: the invoice customer's head office where it has one; it differs from CustomerID on 44,279 invoices.
confidence: medium
claims: 2
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

- C1 | type=declared | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=1645fee7c1580915 | recheck=the description changes | text: The source describes Sales.Invoices.BillToCustomerID as "Bill to customer for this invoice (invoices might be billed to a head office)".
- C2 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=1645fee7c1580915 | recheck=every new extract, or a description changes | text: The customer the invoice is billed to. On every invoice it equals the BillToCustomerID that the invoice's customer has in Sales.Customers on 2016-06-01 (27): the head-office relation of Sales.Customers, repeated on the invoice.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

Whether the bill-to customer is copied at invoicing or always equal to the customer's current bill-to cannot be told from one extract: no customer's bill-to changed in it.

## For a person

None.
