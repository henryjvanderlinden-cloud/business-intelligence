---
id: wwi:object:1682105033
subject: wwi/tables/Purchasing/SupplierTransactions
item: 09
topic: derived
tier: best-effort
summary: TransactionAmount = AmountExcludingTax + TaxAmount on invoices; the invoice amount is the purchase order's total; OutstandingBalance follows the finalization state.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-20T20:06:00Z
step: S08-112
method: measures by prototypes/information_analysis/measures.py (blob 89f3c0d7d2fd53e7e60d4575675beeac0ebb43e8), claims by write_measures.py (blob 8f679dc60353e6e20d24f22fad398861cc10b5ab); readings by claude-opus-5-5
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 10c8ac5e8c6792404fbdf9e86336cc8afb432c3106485f0c111b343ad363d85c
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=8458a397c5208387 | recheck=every new extract | text: TransactionAmount equals AmountExcludingTax + TaxAmount on 2,074 of 2,074 invoice rows; payment rows carry only TransactionAmount.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=8458a397c5208387 | recheck=every new extract | text: AmountExcludingTax equals the purchase order's lines at ExpectedUnitPricePerOuter, and TaxAmount the sum of 15% per line rounded half up on 2,069 of 2,074 invoices (across/reconciliations/supplier-invoices-vs-purchase-order-lines/16_reconciliation.md#C1, #C2).
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=8458a397c5208387 | recheck=every new extract | text: OutstandingBalance is 0 on every finalized row (2,070 invoices, 366 payments) and the full TransactionAmount on the 4 unfinalized invoices; no other value occurs.

## Reasoning

measures.py recomputes the values that the table's columns suggest are computed from others and compares them with the stored ones, row by row; where a formula was found by inspecting ratios first, that is said. A formula that holds on every row of the extract is observed; that it is the source's own rule is a reading.

## Uncertainties

None.

## For a person

None.
