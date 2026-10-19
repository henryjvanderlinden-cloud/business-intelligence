---
id: wwi:reconciliation:invoice-lines-vs-stock-issues
subject: wwi/across/reconciliations/invoice-lines-vs-stock-issues
item: 16
topic: reconciliation
tier: best-effort
summary: Each invoice line is issued from stock once, in full, on the invoice date: the movement is the line's quantity negated.
confidence: medium
claims: 4
written_by: claude-opus-5-5
written_at: 2026-10-19T21:25:00Z
step: S08-085
method: counts by prototypes/information_analysis/reconcile.py (blob 09e7143e7fb2f20127e019cb64133674e1b89c41); readings by claude-opus-5-5 from those counts
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 4faefb5925bee7eb25a1d9930b15bdad1334290a8c6a705169809cc66f79fe69
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=a4ab20d7bf9e7c25 | recheck=every new extract | text: Every one of the 228,432 stock movements that name an invoice is a Stock Issue (type 10) and finds an invoice line on (InvoiceID, StockItemID); the movement's Quantity is the line's Quantity negated on 228,432 of them, and its date is the invoice date on 228,432.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=a4ab20d7bf9e7c25 | recheck=every new extract | text: One to one: 228,432 invoice-line rows with 228,432 distinct (InvoiceID, StockItemID) keys; 0 keys have more than one movement and 0 lines have none.
- C3 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=a4ab20d7bf9e7c25 | recheck=every new extract | text: Physically, an invoice line is shipped once and in full in this extract. The one-to-one of lines and issues concerns goods, and says nothing about how invoices are paid (customer-payments-vs-invoices).
- C4 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=a4ab20d7bf9e7c25 | recheck=every new extract | text: A stock issue repeats its invoice line's quantity and date: in this extract the issues add no quantity or date the lines do not hold.

## Reasoning

Each issue is joined to its invoice line on (InvoiceID, StockItemID), the undeclared one-to-one relation of across/relations, and the quantities and dates compared.

## Uncertainties

Whether a partial shipment of a line would give one or several issues cannot be seen: none occurs. Round 1 found 7,546 orders split into backorders (Sales/Orders/27_peculiarities.md), which may be why no line is shipped in part; that link is not tested.

## For a person

None.
