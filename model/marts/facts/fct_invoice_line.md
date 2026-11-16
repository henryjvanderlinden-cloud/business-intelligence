---
id: nsdn:mart:fct:invoice_line
kind: fact
name: fct_invoice_line
status: accepted
ruled_in: ADR-0039, ADR-0040
defined_in: docs/10_architecture/141_the-first-slice-business-vault-and-mart.md
written_by: claude-fable-5-2
written_at: 2026-11-15T21:30:00Z
step: S13-016
method: written by hand from note 141 as ruled
fact_kind: transaction
grain: one row per invoice line known and present
pit: pit_invoice_line
bridge: brg_invoice_line__sale
decision: DEC-0001
intent: invoiced sales and gross profit per invoice line, to be summed over time and by customer segment
class: confidential
subject_area: sales
---

## Keys

- invoice_line_id | from=key.InvoiceLineID
- invoice_id | via=invoice | pit=pit_invoice | from=key.InvoiceID
- invoice_date | via=invoice | pit=pit_invoice | from=sat_invoice__wwi.InvoiceDate | dimension=dim_date
- is_credit_note | via=invoice | pit=pit_invoice | from=sat_invoice__wwi.IsCreditNote | expect=false
- hk_customer | via=customer | dimension=dim_customer
- hk_bill_to_customer | via=bill_to_customer | dimension=dim_customer | role=bill-to
- hk_stock_item | via=stock_item
- stock_item_id | via=stock_item | pit=pit_stock_item | from=key.StockItemID

## Measures

- quantity | from=sat_invoice_line__wwi.Quantity | additive=within one stock item only
- sales_amount_excl_tax | from=csat_invoice_line__sales_amount.sales_amount_excl_tax | additive=all
- tax_amount | from=sat_invoice_line__wwi.TaxAmount | additive=all
- sales_amount_incl_tax | from=sat_invoice_line__wwi.ExtendedPrice | additive=all
- gross_profit_at_current_cost | from=sat_invoice_line__wwi.LineProfit | additive=all

## Notes

A line whose invoice or customer the bridge did not reach keeps its row and its amounts, on the unknown member and without a date (ADR-0040 decision 1). The gross profit is the source's LineProfit, which the analysis record shows to be profit at the current cost price (09_derived.md, claim C3). A margin is not stored: it is the sum of profit over the sum of sales. The stock item has a key but no dimension yet (ADR-0039).
