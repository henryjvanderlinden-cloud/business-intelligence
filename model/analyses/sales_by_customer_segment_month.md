---
id: nsdn:analysis:sales_by_customer_segment_month
kind: analysis
name: sales_by_customer_segment_month
status: accepted
ruled_in: ADR-0039, ADR-0040
defined_in: docs/10_architecture/141_the-first-slice-business-vault-and-mart.md
written_by: claude-fable-5-2
written_at: 2026-11-15T21:30:00Z
step: S13-016
method: written by hand from note 141 as ruled
decision: DEC-0001
question: How do sales and gross profit develop per month in each customer segment?
fact: fct_invoice_line
---

## Rows

- month | from=dim_date.month
- is_complete_month | from=dim_date.is_complete_month
- customer_category | from=dim_customer.customer_category
- buying_group | from=dim_customer.buying_group

## Values

- sales_amount_excl_tax | sum=sales_amount_excl_tax
- gross_profit_at_current_cost | sum=gross_profit_at_current_cost
- invoices | count_distinct=invoice_id

## Plausibility

- every_complete_period_has_rows | period=month
- latest_complete_period_within | value=sales_amount_excl_tax | period=month | low=0.5 | high=2 | of=12

## Notes

A segment is a customer category together with a buying group. Plausibility checks are warnings while ARC-OP-31 is open: every complete month has sales, and the latest complete month lies between half and double the median of the twelve before it.
