---
id: wwi:term:customer
subject: wwi/across/terms/customer
item: 25
topic: terms
tier: best-effort
summary: "Customer" names two roles: the customer delivered to (orders, invoices' CustomerID, stock movements) and the customer billed (the ledger, invoices' BillToCustomerID).
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

- C1 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=none | recheck=a linked claim changes | text: The order, the invoice's CustomerID and the stock issue name the customer the goods go to (across/relations/Sales.Invoices.CustomerID__Sales.Customers.CustomerID/02_meaning.md#C2; across/relations/Warehouse.StockItemTransactions.CustomerID__Sales.Customers.CustomerID/02_meaning.md#C2).
- C2 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=none | recheck=a linked claim changes | text: The customer ledger and the invoice's BillToCustomerID name the customer billed, the head office where a customer has one (across/relations/Sales.CustomerTransactions.CustomerID__Sales.Customers.CustomerID/02_meaning.md#C2, 27_peculiarities.md#C4 and #C5; across/relations/Sales.Customers.BillToCustomerID__Sales.Customers.CustomerID/02_meaning.md#C2).
- C3 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=none | recheck=a linked claim changes | text: A column called CustomerID therefore means the delivered-to customer in Sales.Orders, Sales.Invoices and Warehouse.StockItemTransactions and the billed customer in Sales.CustomerTransactions (across/relations/Sales.CustomerTransactions.CustomerID__Sales.Customers.CustomerID/27_peculiarities.md#C6).

## Reasoning

Each claim links the files that own the facts it reads.

## Uncertainties

None.

## For a person

None.
