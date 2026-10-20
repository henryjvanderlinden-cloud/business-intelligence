---
id: wwi:object:366624349
subject: wwi/tables/Sales/CustomerTransactions
item: 28
topic: arithmetic
tier: best-effort
summary: Amounts in decimal(18,2); the invoice's tax is the sum of rounded line taxes, not 15% of the invoice amount.
confidence: high
claims: 2
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=6a9dc3d59f5bb9ff | recheck=every new extract, or a schema change | text: AmountExcludingTax, TaxAmount, TransactionAmount and OutstandingBalance are decimal(18,2).
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=6a9dc3d59f5bb9ff | recheck=every new extract | text: 15% of AmountExcludingTax, rounded to cents, reproduces an invoice's TaxAmount by: half up 69,361, half to even 67,357, half down 65,226, truncation 63,728, unrounded 62,276, of 70,566 invoices. The tax on an invoice is the sum of its lines' rounded tax (09_derived.md#C2), at 10% or 15% per line (Sales.InvoiceLines 08_measures.md#C5), so tax recomputed on the invoice amount differs on 1,205 invoices.

## Reasoning

measures.py rounds each recomputed value to cents by four modes (half up, half to even, half down, truncation) and counts the rows each reproduces; the declared precision and scale come from the catalogue, the decimals used from the extract.

## Uncertainties

None.

## For a person

None.
