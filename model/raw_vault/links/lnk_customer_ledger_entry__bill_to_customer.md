---
id: nsdn:rv:link:customer_ledger_entry__bill_to_customer
kind: link
name: lnk_customer_ledger_entry__bill_to_customer
status: accepted
ruled_in: ADR-0031, ADR-0030
defined_in: docs/10_architecture/148_wwi-relationships.md#3 link 41
written_by: claude-opus-5-5
written_at: 2026-10-29T11:25:00Z
step: S11-008
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
label: customer entry account (billed)
from: hub_customer_ledger_entry
to: hub_customer
driving: hub_customer_ledger_entry
optional: no
effectivity: event
subject_area: ledgers
---

## Columns

- Sales.CustomerTransactions.CustomerTransactionID | end=from | effectivity_start=Sales.CustomerTransactions.TransactionDate
- Sales.CustomerTransactions.CustomerID | end=to

## Relations

- analysis/wwi/across/relations/Sales.CustomerTransactions.CustomerID__Sales.Customers.CustomerID

## Evidence

- analysis/wwi/across/relations/Sales.CustomerTransactions.CustomerID__Sales.Customers.CustomerID/02_meaning.md#C2
