---
id: wwi:entity:customer
subject: wwi/across/entities/customer
item: 26
topic: entities
tier: best-effort
summary: Sales.Customers, system-versioned, identified by CustomerID; it appears as delivered-to customer, billed customer and head office.
confidence: medium
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-20T05:51:00Z
step: S08-092
method: readings by claude-opus-5-5 linking the claims that own each fact; written by prototypes/information_analysis/write_glossary.py (blob ffcc3813a793cc9facce4b98cc396d0f16cffa08)
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: none
last_checked_at: 2026-10-20T05:51:00Z
last_checked_by: claude-opus-5-5
last_checked_against: 2016-06-01
reviewed_by: none
reviewed_at: none
ruled_by: none
ruled_at: none
supersedes: none
superseded_by: none
recheck_when: a linked claim changes
---

## Claims

- C1 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=none | recheck=a linked claim changes | text: One table holds every customer, versioned in Sales.Customers_Archive; CustomerID is its key (tables/Sales/Customers/06_keys.md).
- C2 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=none | recheck=a linked claim changes | text: Its roles in other tables: delivered-to (Sales.Orders, Sales.Invoices.CustomerID, Warehouse.StockItemTransactions), billed (Sales.Invoices.BillToCustomerID, Sales.CustomerTransactions), head office (Sales.Customers.BillToCustomerID) - see across/terms/customer/25_terms.md - and scope of a special deal, where by declaration an empty CustomerID means all customers (across/relations/Sales.SpecialDeals.CustomerID__Sales.Customers.CustomerID/02_meaning.md#C1).
- C3 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=none | recheck=a linked claim changes | text: Joined in the extract a customer's current version is used; for 1,868 invoices an earlier version was current at the invoice date and differs in CreditLimit (across/relations/Sales.Invoices.CustomerID__Sales.Customers.CustomerID/03_temporal.md).

## Reasoning

Each claim links the files that own the facts it reads.

## Uncertainties

None.

## For a person

None.
