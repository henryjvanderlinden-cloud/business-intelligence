---
id: nsdn:bv:brg:invoice_line__sale
kind: bridge
name: brg_invoice_line__sale
status: accepted
ruled_in: ADR-0039, ADR-0040
defined_in: docs/10_architecture/141_the-first-slice-business-vault-and-mart.md
written_by: claude-fable-5-2
written_at: 2026-11-15T21:30:00Z
step: S13-016
method: written by hand from note 141 as ruled
start: hub_invoice_line
subject_area: sales
---

## Walk

- invoice | link=lnk_invoice_line__invoice | from=start
- customer | link=lnk_invoice__customer | from=invoice
- bill_to_customer | link=lnk_invoice__bill_to_customer | from=invoice
- stock_item | link=lnk_invoice_line__stock_item | from=start
