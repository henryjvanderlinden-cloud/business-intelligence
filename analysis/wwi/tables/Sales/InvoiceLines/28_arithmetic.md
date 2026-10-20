---
id: wwi:object:510624862
subject: wwi/tables/Sales/InvoiceLines
item: 28
topic: arithmetic
tier: best-effort
summary: Money in decimal(18,2), rates in decimal(18,3); tax reproduced by rounding per line, half up, to cents; nothing rounded at invoice level.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-20T20:06:00Z
step: S08-112
method: measures by prototypes/information_analysis/measures.py (blob 89f3c0d7d2fd53e7e60d4575675beeac0ebb43e8), claims by write_measures.py (blob 8f679dc60353e6e20d24f22fad398861cc10b5ab); readings by claude-opus-5-5
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: a450891eaeade41ce15c8097eee5390bcd9678fc811045b440235fd42c933f74
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=fa43419277162f95 | recheck=every new extract | text: Rounding Quantity x UnitPrice x TaxRate / 100 to cents reproduces TaxAmount by: half up 228,432, half to even 226,319, half down 223,860, truncation 222,285, unrounded 220,700, of 228,432 lines; the largest difference between stored and unrounded tax is 0.00500. This is consistent with tax rounded half up, per line; no tax is negative, so half up is not told apart from rounding ties towards positive infinity.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=fa43419277162f95 | recheck=every new extract, or a schema change | text: Declared: UnitPrice, TaxAmount, ExtendedPrice and LineProfit decimal(18,2); TaxRate decimal(18,3), using 0 decimals; Quantity int.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=fa43419277162f95 | recheck=every new extract | text: The invoice totals in the customer ledger are sums of the rounded line values, with no residue (across/reconciliations/ledger-invoices-vs-invoice-lines/16_reconciliation.md#C1); tax computed on an invoice total instead differs (Sales.CustomerTransactions 28_arithmetic.md#C2).

## Reasoning

measures.py rounds each recomputed value to cents by four modes (half up, half to even, half down, truncation) and counts the rows each reproduces; the declared precision and scale come from the catalogue, the decimals used from the extract.

## Uncertainties

None.

## For a person

None.
