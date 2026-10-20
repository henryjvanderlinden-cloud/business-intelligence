---
id: wwi:object:366624349
subject: wwi/tables/Sales/CustomerTransactions
item: 09
topic: derived
tier: best-effort
summary: TransactionAmount = AmountExcludingTax + TaxAmount on invoices; the invoice amounts are the sums of its lines; OutstandingBalance follows the finalization state.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-20T20:06:00Z
step: S08-112
method: measures by prototypes/information_analysis/measures.py (blob 89f3c0d7d2fd53e7e60d4575675beeac0ebb43e8), claims by write_measures.py (blob 8f679dc60353e6e20d24f22fad398861cc10b5ab); readings by claude-opus-5-5
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 8e272ee961a192b88ad69f58e01cf2ccba809358d2e23ff34de608bfd295c067
last_checked_at: 2026-10-20T20:06:00Z
last_checked_by: claude-opus-5-5
last_checked_against: 2016-06-01
reviewed_by: none
reviewed_at: none
ruled_by: none
ruled_at: none
supersedes: none
superseded_by: none
recheck_when: every new extract, or a schema change
---

## Claims

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=6a9dc3d59f5bb9ff | recheck=every new extract | text: TransactionAmount equals AmountExcludingTax + TaxAmount on 70,566 of 70,566 invoice rows; payment rows carry only TransactionAmount.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=6a9dc3d59f5bb9ff | recheck=every new extract | text: On invoice rows AmountExcludingTax, TaxAmount and TransactionAmount equal the sums over the invoice's lines (across/reconciliations/ledger-invoices-vs-invoice-lines/16_reconciliation.md#C1); a payment equals, negated, the invoices finalized on its customer-day (across/reconciliations/customer-payments-vs-invoices/16_reconciliation.md#C1).
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=6a9dc3d59f5bb9ff | recheck=every new extract | text: OutstandingBalance is 0 on every finalized row (70,510 invoices, 26,676 payments) and the full TransactionAmount on the 56 unfinalized invoices; no other value occurs.

## Reasoning

measures.py recomputes the values that the table's columns suggest are computed from others and compares them with the stored ones, row by row; where a formula was found by inspecting ratios first, that is said. A formula that holds on every row of the extract is observed; that it is the source's own rule is a reading.

## Uncertainties

None.

## For a person

None.
