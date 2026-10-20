---
id: wwi:object:802101898
subject: wwi/tables/Sales/Customers
item: 08
topic: measures
tier: best-effort
summary: No measure: CreditLimit, PaymentDays and StandardDiscountPercentage are terms of the customer.
confidence: high
claims: 4
written_by: claude-opus-5-5
written_at: 2026-10-20T20:06:00Z
step: S08-112
method: measures by prototypes/information_analysis/measures.py (blob 89f3c0d7d2fd53e7e60d4575675beeac0ebb43e8), claims by write_measures.py (blob 8f679dc60353e6e20d24f22fad398861cc10b5ab); readings by claude-opus-5-5
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: f54b9d7dd163d0d1e3ce34f4adf4d1a76e8caeebe545ad0831277bb0e5b89fb6
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=2d52e613da90eec8 | recheck=every new extract | text: CreditLimit: decimal(18,2), filled on 261 of 663 rows, range 1100.00 to 4630.50; 0 negative, 0 zero, 261 positive; at most 2 decimal(s) used, 4 non-integer value(s).
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=2d52e613da90eec8 | recheck=every new extract | text: PaymentDays: int(10,0), filled on 663 of 663 rows, range 7 to 7; 0 negative, 0 zero, 663 positive; at most 0 decimal(s) used; values 7 (663).
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=2d52e613da90eec8 | recheck=every new extract | text: StandardDiscountPercentage: decimal(18,3), filled on 663 of 663 rows, range 0.000 to 0.000; 0 negative, 663 zero, 0 positive; at most 0 decimal(s) used, 0 non-integer value(s); values 0.000 (663).
- C4 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=2d52e613da90eec8 | recheck=every new extract | text: CreditLimit, PaymentDays and StandardDiscountPercentage are terms, not measures. CreditLimit is filled on 261 of 663 customers (empty means unlimited, as described); PaymentDays is 7 on all; StandardDiscountPercentage is 0 on all.

## Reasoning

measures.py profiles every numeric column that is not a key, a foreign key or an audit column: declared type, filling, range, signs (per transaction type where the table has one) and the decimals actually used. How a column adds up - additive over rows and time, semi-additive (a level: summable across items at one moment, not over time), non-additive (a price, rate, percentage, reading or attribute), or not a measure at all - is the reader's, from the description, the profile and the tests; it is stated as a fact about the column, not as a rule for using it.

## Uncertainties

None.

## For a person

None.
