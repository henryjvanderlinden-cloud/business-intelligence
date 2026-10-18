---
item: 05
topic: role
subject: wwi/Sales.Orders
tier: minimum
status: proposed
confidence: high
finding: Transaction header for the business event "customer order raised", carrying one workflow milestone (picking completed); its lines are Sales.OrderLines.
claims: [declared, observed]
as_of: wwi 2016-06-01 manifest sha256 35b71b2e3ff4bb9e
evidence: [E003, E004, E006, E008]
analysed_by: claude-opus-5-5
analysed_at: 2026-10-18
ruled_by: none
---

## Finding

A transaction header. Each row records one order event and refers to master data: `Sales.Customers` and, for four
person roles, `Application.People` (E003, six declared, enabled and trusted foreign keys). Its lines are in
`Sales.OrderLines` (E008). It is not a history table and not configuration (E004).

It also carries state: the picking milestone is filled in later, in place (E006). In dimensional terms this is an
accumulating-snapshot shape (milestones on one row); in Data Vault terms, a hub on `OrderID` with links to customer
and people, and a satellite whose picking attributes change once.

## Reasoning

Declared foreign keys, the observed header-line pattern and the observed update pattern all point the same way.

## Uncertainties

None about the role. Whether the order also has a later life in other tables (invoices) belongs to items 4 and 24,
not done yet.

## For a person

None.
