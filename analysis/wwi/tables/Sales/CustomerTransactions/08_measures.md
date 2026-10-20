---
id: wwi:object:366624349
subject: wwi/tables/Sales/CustomerTransactions
item: 08
topic: measures
tier: best-effort
summary: AmountExcludingTax and TaxAmount on invoices only, TransactionAmount signed (invoices positive, payments negative), OutstandingBalance a state on the row.
confidence: medium
claims: 8
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=6a9dc3d59f5bb9ff | recheck=every new extract | text: AmountExcludingTax: decimal(18,2), filled on 97,242 of 97,242 rows, range 0.00 to 32026.00; 0 negative, 26,676 zero, 70,566 positive; at most 2 decimal(s) used, 19,111 non-integer value(s); by transaction type: Customer Invoice positive 70,566; Customer Payment Received zero 26,676.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=6a9dc3d59f5bb9ff | recheck=every new extract | text: OutstandingBalance: decimal(18,2), filled on 97,242 of 97,242 rows, range 0.00 to 22583.70; 0 negative, 97,186 zero, 56 positive; at most 2 decimal(s) used, 54 non-integer value(s); by transaction type: Customer Invoice positive 56, zero 70,510; Customer Payment Received zero 26,676.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=6a9dc3d59f5bb9ff | recheck=every new extract | text: TaxAmount: decimal(18,2), filled on 97,242 of 97,242 rows, range 0.00 to 4803.90; 0 negative, 26,676 zero, 70,566 positive; at most 2 decimal(s) used, 65,244 non-integer value(s); by transaction type: Customer Invoice positive 70,566; Customer Payment Received zero 26,676.
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=6a9dc3d59f5bb9ff | recheck=every new extract | text: TransactionAmount: decimal(18,2), filled on 97,242 of 97,242 rows, range -169387.42 to 36829.90; 26,676 negative, 0 zero, 70,566 positive; at most 2 decimal(s) used, 90,089 non-integer value(s); by transaction type: Customer Invoice positive 70,566; Customer Payment Received negative 26,676.
- C5 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=6a9dc3d59f5bb9ff | recheck=every new extract | text: AmountExcludingTax and TaxAmount are amounts on invoice rows (positive on all 70,566) and zero on payment rows (all 26,676): summed over rows they give invoiced amounts, not payments.
- C6 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=6a9dc3d59f5bb9ff | recheck=every new extract | text: TransactionAmount carries the sign of the event: positive on 70,566 invoices, negative on 26,676 payments. It is additive: for each of the 263 customers the sum of its TransactionAmount equals the sum of its OutstandingBalance (on all 263): the amounts not offset by payments are exactly the open invoices (09_derived.md#C3).
- C7 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=6a9dc3d59f5bb9ff | recheck=every new extract | text: OutstandingBalance is a state on an event row, not an event: it is the full amount on the 56 open invoices and 0 on every finalized row, and it is overwritten when the invoice is paid (across/reconciliations/customer-payments-vs-invoices/16_reconciliation.md#C3). Summed over rows it gives the open amount at the moment of the extract; summed over extracts it counts the same open amount again (27_peculiarities.md#C3).
- C8 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=6a9dc3d59f5bb9ff | recheck=every new extract, or a schema change | text: No column holds a currency; the catalogue declares none, so all amounts are in one currency the source does not name.

## Reasoning

measures.py profiles every numeric column that is not a key, a foreign key or an audit column: declared type, filling, range, signs (per transaction type where the table has one) and the decimals actually used. How a column adds up - additive over rows and time, semi-additive (a level: summable across items at one moment, not over time), non-additive (a price, rate, percentage, reading or attribute), or not a measure at all - is the reader's, from the description, the profile and the tests; it is stated as a fact about the column, not as a rule for using it.

## Uncertainties

None.

## For a person

None.
