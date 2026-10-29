---
id: nsdn:rv:hub:invoice
kind: hub
name: hub_invoice
status: accepted
ruled_in: ADR-0029, ADR-0030
defined_in: docs/10_architecture/147_wwi-concepts-keys-and-business-time.md#3 item 14
written_by: claude-opus-5-5
written_at: 2026-10-29T11:20:00Z
step: S11-004
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
concept: invoice
grain: one invoice
subject_area: sales
---

## Business key

- Sales.Invoices.InvoiceID | key_space=wwi | key_kind=record-identifier

## Evidence

- analysis/wwi/tables/Sales/Invoices/01_granularity.md#C1
- analysis/wwi/tables/Sales/Invoices/01_granularity.md#C2
- analysis/wwi/tables/Sales/Invoices/01_granularity.md#C4
