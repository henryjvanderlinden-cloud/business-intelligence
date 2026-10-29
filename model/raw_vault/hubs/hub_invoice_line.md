---
id: nsdn:rv:hub:invoice_line
kind: hub
name: hub_invoice_line
status: accepted
ruled_in: ADR-0029, ADR-0030
defined_in: docs/10_architecture/147_wwi-concepts-keys-and-business-time.md#3 item 15
written_by: claude-opus-5-5
written_at: 2026-10-29T11:25:00Z
step: S11-008
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
concept: invoice line
grain: one line
subject_area: sales
---

## Business key

- Sales.InvoiceLines.InvoiceLineID | key_space=wwi | key_kind=record-identifier

## Evidence

- analysis/wwi/tables/Sales/InvoiceLines/01_granularity.md#C1
- analysis/wwi/tables/Sales/InvoiceLines/01_granularity.md#C2
- analysis/wwi/tables/Sales/InvoiceLines/01_granularity.md#C3
