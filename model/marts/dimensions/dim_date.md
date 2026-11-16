---
id: nsdn:mart:dim:date
kind: dimension
name: dim_date
status: accepted
ruled_in: ADR-0039, ADR-0040
defined_in: docs/10_architecture/141_the-first-slice-business-vault-and-mart.md
written_by: claude-fable-5-2
written_at: 2026-11-15T21:30:00Z
step: S13-016
method: written by hand from note 141 as ruled
rule: calendar
first_date: 2013-01-01
subject_area: time
---

## Attributes

- date | from=rule
- year | from=rule
- quarter | from=rule
- month | from=rule
- month_start | from=rule
- is_complete_month | from=rule

## Notes

A calendar by rule, from first_date (the first invoice date of Wide World Importers, analysis/wwi/tables/Sales/Invoices/07_population.md, claim C1) to the end of the month of the knowledge date. A month is complete when its last day is not after the knowledge date.
