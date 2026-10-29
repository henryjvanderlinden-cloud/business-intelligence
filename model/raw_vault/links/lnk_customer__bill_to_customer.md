---
id: nsdn:rv:link:customer__bill_to_customer
kind: link
name: lnk_customer__bill_to_customer
status: accepted
ruled_in: ADR-0031, ADR-0030
defined_in: docs/10_architecture/148_wwi-relationships.md#3 link 5
written_by: claude-opus-5-5
written_at: 2026-10-29T11:34:00Z
step: S11-010
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
label: customer billed to (head office)
from: hub_customer
to: hub_customer
driving: hub_customer
optional: no
effectivity: load
subject_area: parties
---

## Columns

- Sales.Customers.CustomerID | end=from | effectivity_start=load
- Sales.Customers.BillToCustomerID | end=to

## Relations

- analysis/wwi/across/relations/Sales.Customers.BillToCustomerID__Sales.Customers.CustomerID

## Evidence

- analysis/wwi/across/relations/Sales.Customers.BillToCustomerID__Sales.Customers.CustomerID/02_meaning.md#C2
- analysis/wwi/across/relations/Sales.Customers.BillToCustomerID__Sales.Customers.CustomerID/07_population.md#C2
