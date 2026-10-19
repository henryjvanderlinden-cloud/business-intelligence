---
id: wwi:reconciliation:supplier-payments-vs-invoices
subject: wwi/across/reconciliations/supplier-payments-vs-invoices
item: 16
topic: reconciliation
tier: best-effort
summary: As on the customer side: a supplier payment equals the total of that supplier's invoices finalized that day; no part payments.
confidence: unknown
claims: 6
written_by: claude-opus-5-5
written_at: 2026-10-19T21:25:00Z
step: S08-085
method: counts by prototypes/information_analysis/reconcile.py (blob 09e7143e7fb2f20127e019cb64133674e1b89c41); readings by claude-opus-5-5 from those counts
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: d8ddf732d75e3b302d58a9679e602ddd65ae7d55726454109e0f674183c153b9
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=6b688a5c2222b115 | recheck=every new extract | text: 366 payments (Supplier Payment Issued): each equals, negated, the total of the supplier's invoices finalized on the payment's date, on 366 of 366; no supplier pays twice on one day (at most 1 payment per supplier and day); no supplier-day with finalized invoices lacks a payment (0).
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=6b688a5c2222b115 | recheck=every new extract | text: Invoices finalized on the payment's supplier-day: one for 4 payments, several for 362, at most 6; no key says which invoices a payment settles, so this counts candidates, not allocations.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=6b688a5c2222b115 | recheck=every new extract | text: Invoice states: IsFinalized=0|FinalizationDate=empty|OutstandingBalance=the full amount on 4; IsFinalized=1|FinalizationDate=set|OutstandingBalance=0 on 2,070. Payment states: IsFinalized=1|OutstandingBalance=0 on 366.
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=6b688a5c2222b115 | recheck=every new extract | text: Days from invoice to finalization: 0 days on 641; 3 days on 356; 4 days on 358; 5 days on 358; 6 days on 357.
- C5 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=6b688a5c2222b115 | recheck=every new extract | text: As on the customer side, no key links a payment to supplier invoices; in this extract the match can be rebuilt by (SupplierID, date) and the finalization state of the invoices. Unlike customer invoices, supplier invoices are finalized 0, 3, 4, 5 or 6 days after their date, so the delay is not fixed.
- C6 | type=observed | status=proposed | confidence=unknown | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=none | recheck=a second extract, a process description or the generating script settles it | text: How a part payment to a supplier would be recorded is not established: none occurs.

## Reasoning

As for customer payments, with SupplierID.

## Uncertainties

Part payments; the rule behind the 0 to 6 day delay.

## For a person

None.
