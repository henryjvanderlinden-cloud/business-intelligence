---
id: DEC-0001
kind: decision
name: customer-segment-sales-attention
status: accepted
ruled_in: ADR-0039, ADR-0040
decision: Which customer segments get sales attention.
owner: the sales manager of Wide World Importers; the author stands in, the manager does not exist
cadence: monthly
evidence: sales excluding tax and gross profit at current cost per customer segment per month
written_by: claude-fable-5-2
written_at: 2026-11-15T21:30:00Z
step: S13-015
---

## Served by

- fct_invoice_line
- sales_by_customer_segment_month

## Notes

The first entry of the decision register (ADR-0039 decision 5, ADR-0040 decision 3). A segment is a customer category
together with a buying group. Wide World Importers is a sample company, so this entry tests the mechanism, a mart and
an analysis citing a decision, and nothing about whether an organisation would keep such a register up (ARC-OP-12).
