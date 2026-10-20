---
id: wwi:object:94623380
subject: wwi/tables/Sales/OrderLines
item: 08
topic: measures
tier: best-effort
summary: Quantity and PickedQuantity additive; UnitPrice and TaxRate non-additive; no amount is stored on an order line.
confidence: medium
claims: 7
written_by: claude-opus-5-5
written_at: 2026-10-20T20:06:00Z
step: S08-112
method: measures by prototypes/information_analysis/measures.py (blob 89f3c0d7d2fd53e7e60d4575675beeac0ebb43e8), claims by write_measures.py (blob 8f679dc60353e6e20d24f22fad398861cc10b5ab); readings by claude-opus-5-5
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: c00930db9c641c1b31801c17473429ceaa1b6c45519761d89148dd23ed44a1e7
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=b05dba876c35f098 | recheck=every new extract | text: PickedQuantity: int(10,0), filled on 231,581 of 231,581 rows, range 0 to 360; 0 negative, 3,149 zero, 228,432 positive; at most 0 decimal(s) used.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=b05dba876c35f098 | recheck=every new extract | text: Quantity: int(10,0), filled on 231,581 of 231,581 rows, range 1 to 360; 0 negative, 0 zero, 231,581 positive; at most 0 decimal(s) used.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=b05dba876c35f098 | recheck=every new extract | text: TaxRate: decimal(18,3), filled on 231,581 of 231,581 rows, range 10.000 to 15.000; 0 negative, 0 zero, 231,581 positive; at most 0 decimal(s) used, 0 non-integer value(s); values 10.000 (1,044), 15.000 (230,537).
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=b05dba876c35f098 | recheck=every new extract | text: UnitPrice: decimal(18,2), filled on 231,581 of 231,581 rows, range 0.66 to 1899.00; 0 negative, 0 zero, 231,581 positive; at most 2 decimal(s) used, 40,293 non-integer value(s).
- C5 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=b05dba876c35f098 | recheck=every new extract | text: Quantity and PickedQuantity are additive over lines of one stock item, in packages of the line's package type; UnitPrice (excluding tax) and TaxRate (a percentage) are non-additive.
- C6 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=b05dba876c35f098 | recheck=every new extract | text: No column holds an amount (of TaxAmount, ExtendedPrice, LineTotal and LineProfit, present: none): the order tables store no value of a line or of an order.
- C7 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=b05dba876c35f098 | recheck=every new extract | text: Picking is all or nothing: PickedQuantity equals Quantity on all 228,432 picked lines (PickingCompletedWhen filled) and is 0 on all 3,149 unpicked ones; no line is part picked.

## Reasoning

measures.py profiles every numeric column that is not a key, a foreign key or an audit column: declared type, filling, range, signs (per transaction type where the table has one) and the decimals actually used. How a column adds up - additive over rows and time, semi-additive (a level: summable across items at one moment, not over time), non-additive (a price, rate, percentage, reading or attribute), or not a measure at all - is the reader's, from the description, the profile and the tests; it is stated as a fact about the column, not as a rule for using it.

## Uncertainties

None.

## For a person

None.
