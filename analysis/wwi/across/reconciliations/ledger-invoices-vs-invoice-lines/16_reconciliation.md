---
id: wwi:reconciliation:ledger-invoices-vs-invoice-lines
subject: wwi/across/reconciliations/ledger-invoices-vs-invoice-lines
item: 16
topic: reconciliation
tier: best-effort
summary: Each ledger invoice entry equals the sum of its invoice lines exactly - amount excluding tax, tax and total - on the invoice date.
confidence: medium
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-19T21:25:00Z
step: S08-085
method: counts by prototypes/information_analysis/reconcile.py (blob 09e7143e7fb2f20127e019cb64133674e1b89c41); readings by claude-opus-5-5 from those counts
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 2151f88717db78da8c975357583298b3ee5d2e660a988fe1b8b034ddc04751f3
last_checked_at: 2026-10-19T21:25:00Z
last_checked_by: claude-opus-5-5
last_checked_against: 2016-06-01
reviewed_by: none
reviewed_at: none
ruled_by: none
ruled_at: none
supersedes: none
superseded_by: none
recheck_when: every new extract, or a schema change of the tables compared
---

## Claims

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=984fa6c9a59d0522 | recheck=every new extract | text: For all 70,566 ledger invoice entries: AmountExcludingTax equals the sum of Quantity x UnitPrice of the invoice's lines on 70,566, TaxAmount the sum of the lines' TaxAmount on 70,566, TransactionAmount the sum of their ExtendedPrice on 70,566, and TransactionDate the InvoiceDate on 70,566.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=984fa6c9a59d0522 | recheck=every new extract | text: On all 228,432 invoice lines ExtendedPrice is Quantity x UnitPrice + TaxAmount.
- C3 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=984fa6c9a59d0522 | recheck=every new extract | text: The ledger entry is the invoice's total, carried as a copy: in this extract it adds no amount the lines do not hold, and an invoice is booked in the ledger in full on its date.

## Reasoning

Line amounts are summed per invoice and compared with the ledger entry's amounts, exactly (decimal arithmetic, no tolerance).

## Uncertainties

Credit notes would test the sign convention; there are none (round 1, Sales.Invoices 07).

## For a person

None.
