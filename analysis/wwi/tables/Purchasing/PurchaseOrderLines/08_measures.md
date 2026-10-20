---
id: wwi:object:1554104577
subject: wwi/tables/Purchasing/PurchaseOrderLines
item: 08
topic: measures
tier: best-effort
summary: OrderedOuters and ReceivedOuters additive per item, in outers; ExpectedUnitPricePerOuter a price per outer.
confidence: medium
claims: 5
written_by: claude-opus-5-5
written_at: 2026-10-20T20:06:00Z
step: S08-112
method: measures by prototypes/information_analysis/measures.py (blob 89f3c0d7d2fd53e7e60d4575675beeac0ebb43e8), claims by write_measures.py (blob 8f679dc60353e6e20d24f22fad398861cc10b5ab); readings by claude-opus-5-5
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: ff3afe91393905debcfd3922ce15e0214e6da79b9a15f2e41e4abf504040d77e
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=1684a9f73e9758c8 | recheck=every new extract | text: ExpectedUnitPricePerOuter: decimal(18,2), filled on 8,376 of 8,376 rows, range 4.50 to 1140.00; 0 negative, 0 zero, 8,376 positive; at most 2 decimal(s) used, 1,551 non-integer value(s).
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=1684a9f73e9758c8 | recheck=every new extract | text: OrderedOuters: int(10,0), filled on 8,376 of 8,376 rows, range 1 to 3776; 0 negative, 0 zero, 8,376 positive; at most 0 decimal(s) used.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=1684a9f73e9758c8 | recheck=every new extract | text: ReceivedOuters: int(10,0), filled on 8,376 of 8,376 rows, range 0 to 3768; 0 negative, 9 zero, 8,367 positive; at most 0 decimal(s) used.
- C4 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=1684a9f73e9758c8 | recheck=every new extract | text: OrderedOuters and ReceivedOuters count outer packages, each holding QuantityPerOuter units of the item (Warehouse.StockItems): additive over lines of one item, not comparable with the unit quantities of the sales tables without that factor. ExpectedUnitPricePerOuter is a price per outer, non-additive.
- C5 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=1684a9f73e9758c8 | recheck=every new extract | text: ReceivedOuters equals OrderedOuters on all 8,367 finalized lines and is 0 on the 9 open ones; no line is part received or over received (0, 0).

## Reasoning

measures.py profiles every numeric column that is not a key, a foreign key or an audit column: declared type, filling, range, signs (per transaction type where the table has one) and the decimals actually used. How a column adds up - additive over rows and time, semi-additive (a level: summable across items at one moment, not over time), non-additive (a price, rate, percentage, reading or attribute), or not a measure at all - is the reader's, from the description, the profile and the tests; it is stated as a fact about the column, not as a rule for using it.

## Uncertainties

None.

## For a person

None.
