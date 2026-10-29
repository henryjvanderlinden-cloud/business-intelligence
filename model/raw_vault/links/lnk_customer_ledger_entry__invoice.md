---
id: nsdn:rv:link:customer_ledger_entry__invoice
kind: link
name: lnk_customer_ledger_entry__invoice
status: accepted
ruled_in: ADR-0031, ADR-0030
defined_in: docs/10_architecture/148_wwi-relationships.md#3 link 42
written_by: claude-opus-5-5
written_at: 2026-10-29T11:20:00Z
step: S11-004
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
label: customer entry invoice
from: hub_customer_ledger_entry
to: hub_invoice
driving: hub_customer_ledger_entry
optional: yes
effectivity: event
effectivity_start: Sales.CustomerTransactions.TransactionDate
subject_area: ledgers
optional_note: payments
---

## Columns

- Sales.CustomerTransactions.InvoiceID | names=hub_invoice

## Relations

- analysis/wwi/across/relations/Sales.CustomerTransactions.InvoiceID__Sales.Invoices.InvoiceID

## Evidence

- analysis/wwi/across/relations/Sales.CustomerTransactions.InvoiceID__Sales.Invoices.InvoiceID/02_meaning.md#C2
- analysis/wwi/across/relations/Sales.CustomerTransactions.InvoiceID__Sales.Invoices.InvoiceID/07_population.md#C2
