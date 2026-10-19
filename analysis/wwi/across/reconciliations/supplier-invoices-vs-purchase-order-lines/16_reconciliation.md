---
id: wwi:reconciliation:supplier-invoices-vs-purchase-order-lines
subject: wwi/across/reconciliations/supplier-invoices-vs-purchase-order-lines
item: 16
topic: reconciliation
tier: best-effort
summary: A supplier invoice equals its purchase order's lines at the expected price; tax is 15% per line rounded half up, except on 5 invoices.
confidence: unknown
claims: 5
written_by: claude-opus-5-5
written_at: 2026-10-19T21:25:00Z
step: S08-085
method: counts by prototypes/information_analysis/reconcile.py (blob 09e7143e7fb2f20127e019cb64133674e1b89c41); readings by claude-opus-5-5 from those counts
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: f09156e0ffc6195d6039ced93f5085fd57db7949e5254eafde450623a26c6fe1
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=49e142452bb04478 | recheck=every new extract | text: For all 2,074 supplier invoices AmountExcludingTax equals the sum over the purchase order's lines of ReceivedOuters x ExpectedUnitPricePerOuter (2,074) and of OrderedOuters x ExpectedUnitPricePerOuter (2,074); TransactionAmount is AmountExcludingTax + TaxAmount on 2,074.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=49e142452bb04478 | recheck=every new extract | text: TaxAmount equals the sum over lines of 15% of ReceivedOuters x ExpectedUnitPricePerOuter, each rounded half up, on 2,069 invoices and is less on 5; it equals 15% of the invoice's AmountExcludingTax, rounded half up, on 2,061.
- C3 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=49e142452bb04478 | recheck=every new extract | text: A supplier invoice holds no lines or prices of its own; in this extract its total equals the purchase order's total at ExpectedUnitPricePerOuter. Received and ordered outers give the same total at that price on every invoiced order, consistent with each invoiced order having been received in full (tested on totals, not line by line).
- C4 | type=observed | status=proposed | confidence=unknown | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=none | recheck=a second extract, a process description or the generating script settles it | text: Whether the supplier's actual line prices equal the expected ones is not established: only totals are compared, and offsetting differences between lines would pass.
- C5 | type=observed | status=proposed | confidence=unknown | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=none | recheck=a second extract, a process description or the generating script settles it | text: Why TaxAmount is below the per-line 15% on 5 invoices - another rate on some lines, a discount or a rounding rule - is not established.

## Reasoning

Line amounts at the expected price are summed per purchase order and compared with the supplier invoice, exactly; tax is tested at 15% on the total and per line, rounded half up.

## Uncertainties

The 5 invoices whose tax is below the per-line 15%.

## For a person

None.
