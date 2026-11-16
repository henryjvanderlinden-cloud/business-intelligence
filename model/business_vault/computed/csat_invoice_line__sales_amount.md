---
id: nsdn:bv:csat:invoice_line__sales_amount
kind: computed
name: csat_invoice_line__sales_amount
status: accepted
ruled_in: ADR-0039, ADR-0040
defined_in: docs/10_architecture/141_the-first-slice-business-vault-and-mart.md
written_by: claude-fable-5-2
written_at: 2026-11-15T21:30:00Z
step: S13-016
method: written by hand from note 141 as ruled
hub: hub_invoice_line
pit: pit_invoice_line
satellite: sat_invoice_line__wwi
rule: sales-amount-excl-tax
rule_version: 1
subject_area: sales
---

## Values

- sales_amount_excl_tax | expr=ExtendedPrice - TaxAmount | oracle=Quantity * UnitPrice | type=DECIMAL(18,2)

## Notes

Sales means the amount excluding tax (ADR-0039 decision 3): the delivered amount including tax less the delivered tax. The oracle is the source's own arithmetic (analysis/wwi/tables/Sales/InvoiceLines/09_derived.md, claim C2).
