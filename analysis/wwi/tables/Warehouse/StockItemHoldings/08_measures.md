---
id: wwi:object:1474104292
subject: wwi/tables/Warehouse/StockItemHoldings
item: 08
topic: measures
tier: best-effort
summary: QuantityOnHand and LastStocktakeQuantity are levels (semi-additive); LastCostPrice a price; ReorderLevel and TargetStockLevel thresholds.
confidence: low
claims: 8
written_by: claude-opus-5-5
written_at: 2026-10-20T20:06:00Z
step: S08-112
method: measures by prototypes/information_analysis/measures.py (blob 89f3c0d7d2fd53e7e60d4575675beeac0ebb43e8), claims by write_measures.py (blob 8f679dc60353e6e20d24f22fad398861cc10b5ab); readings by claude-opus-5-5
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: bb1ea17573cd7d7073444df38e148e0a4fc7ac5b6c6bc1078e0bd538c0085e24
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=fbf1f0984b515fee | recheck=every new extract | text: LastCostPrice: decimal(18,2), filled on 227 of 227 rows, range 0.36 to 1140.00; 0 negative, 0 zero, 227 positive; at most 2 decimal(s) used, 114 non-integer value(s).
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=fbf1f0984b515fee | recheck=every new extract | text: LastStocktakeQuantity: int(10,0), filled on 227 of 227 rows, range 1 to 1009444; 0 negative, 0 zero, 227 positive; at most 0 decimal(s) used.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=fbf1f0984b515fee | recheck=every new extract | text: QuantityOnHand: int(10,0), filled on 227 of 227 rows, range 0 to 1035144; 0 negative, 1 zero, 226 positive; at most 0 decimal(s) used.
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=fbf1f0984b515fee | recheck=every new extract | text: ReorderLevel: int(10,0), filled on 227 of 227 rows, range 1 to 240; 0 negative, 0 zero, 227 positive; at most 0 decimal(s) used; values 1 (1), 10 (36), 12 (8), 120 (1), 15 (42), 2 (3), 20 (59), 240 (7), 5 (55), 50 (15).
- C5 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=fbf1f0984b515fee | recheck=every new extract | text: TargetStockLevel: int(10,0), filled on 227 of 227 rows, range 2 to 500; 0 negative, 0 zero, 227 positive; at most 0 decimal(s) used.
- C6 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=fbf1f0984b515fee | recheck=every new extract | text: QuantityOnHand and LastStocktakeQuantity are levels: one value per item at a moment, summable across items of one unit at that moment, not over time. LastCostPrice is a price per unit, non-additive. ReorderLevel is a threshold ("Quantity below which reordering should take place"); none of the three is additive.
- C7 | type=intended | status=proposed | confidence=low | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=fbf1f0984b515fee | recheck=every new extract | text: TargetStockLevel is described as "Typical quantity ordered" while its name says a target level to hold; which of the two it is is not established. Either way it is an attribute of the item, not additive.
- C8 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=fbf1f0984b515fee | recheck=every new extract | text: ReorderLevel is at most TargetStockLevel on 227 of 227 items; QuantityOnHand is below ReorderLevel on 5.

## Reasoning

measures.py profiles every numeric column that is not a key, a foreign key or an audit column: declared type, filling, range, signs (per transaction type where the table has one) and the decimals actually used. How a column adds up - additive over rows and time, semi-additive (a level: summable across items at one moment, not over time), non-additive (a price, rate, percentage, reading or attribute), or not a measure at all - is the reader's, from the description, the profile and the tests; it is stated as a fact about the column, not as a rule for using it.

## Uncertainties

None.

## For a person

None.
