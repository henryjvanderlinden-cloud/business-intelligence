---
id: wwi:reconciliation:customer-payments-vs-invoices
subject: wwi/across/reconciliations/customer-payments-vs-invoices
item: 16
topic: reconciliation
tier: best-effort
summary: Payment matching is implicit: a payment equals the total of the customer's invoices finalized that day, one payment per customer and day; no part payments in this extract.
confidence: unknown
claims: 8
written_by: claude-opus-5-5
written_at: 2026-10-19T21:25:00Z
step: S08-085
method: counts by prototypes/information_analysis/reconcile.py (blob 09e7143e7fb2f20127e019cb64133674e1b89c41); readings by claude-opus-5-5 from those counts
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 58409e6b643eab5d557cc760d95fb0736c9de909948c63456219c7d320718c70
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=db6e744afaed8012 | recheck=every new extract | text: 26,676 payments (Customer Payment Received): each equals, negated, the total of the customer's invoices finalized on the payment's date, on 26,676 of 26,676; no customer pays twice on one day (at most 1 payment per customer and day); no customer-day with finalized invoices lacks a payment (0).
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=db6e744afaed8012 | recheck=every new extract | text: Invoices finalized on the payment's customer-day: one for 23,113 payments, several for 3,563, at most 47; no key says which invoices a payment settles, so this counts candidates, not allocations.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=db6e744afaed8012 | recheck=every new extract | text: Invoice states: IsFinalized=0|FinalizationDate=empty|OutstandingBalance=the full amount on 56; IsFinalized=1|FinalizationDate=set|OutstandingBalance=0 on 70,510. Payment states: IsFinalized=1|OutstandingBalance=0 on 26,676.
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=db6e744afaed8012 | recheck=every new extract | text: Days from invoice to finalization: 1 day on 70,510.
- C5 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=db6e744afaed8012 | recheck=every new extract | text: Matching payments to invoices (Dutch: afletteren) leaves no key in Sales.CustomerTransactions: payments have no InvoiceID (across/relations), and a paid invoice only changes state - IsFinalized = 1, a FinalizationDate, OutstandingBalance 0. In this extract the match can be rebuilt on (CustomerID, date), because a customer pays at most once a day and that payment equals the day's finalized invoices.
- C6 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=db6e744afaed8012 | recheck=every new extract | text: In this extract no invoice is part paid: every invoice is fully open (OutstandingBalance the full amount) or fully paid, every payment has OutstandingBalance 0 and equals the invoices finalized that day, and every paid invoice was finalized one day after its date - consistent with all of a customer's invoices of one day being paid together the next day.
- C7 | type=observed | status=proposed | confidence=unknown | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=none | recheck=a second extract, a process description or the generating script settles it | text: Whether the source records the allocation of payments to invoices anywhere else (another table, a procedure's log) is not established; only Sales.CustomerTransactions was examined.
- C8 | type=observed | status=proposed | confidence=unknown | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=none | recheck=a second extract, a process description or the generating script settles it | text: How the source would record a part payment or an overpayment - an OutstandingBalance between 0 and the amount, a payment left open, or something else - is not established: none occurs.

## Reasoning

Invoices are grouped by (CustomerID, FinalizationDate) and compared with payments by (CustomerID, TransactionDate), exactly. CustomerID in the ledger is the bill-to customer (across/relations, Sales.CustomerTransactions.CustomerID).

## Uncertainties

The behaviour of part payments, overpayments and payments on account: absent from the data.

## For a person

None.
