---
id: wwi:object:638625318
subject: wwi/tables/Warehouse/StockItemTransactions
item: 08
topic: measures
tier: best-effort
summary: Quantity is a signed movement: negative on issues, positive on receipts, either sign at stocktake.
confidence: medium
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-20T20:06:00Z
step: S08-112
method: measures by prototypes/information_analysis/measures.py (blob 89f3c0d7d2fd53e7e60d4575675beeac0ebb43e8), claims by write_measures.py (blob 8f679dc60353e6e20d24f22fad398861cc10b5ab); readings by claude-opus-5-5
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: aa0ff84050dc38732c7bd5472378de21f412a1f72bdf0c9aa4958b125c232331
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=851490a2e4d3f456 | recheck=every new extract | text: Quantity: decimal(18,3), filled on 236,843 of 236,843 rows, range -360.000 to 67368.000; 228,453 negative, 4 zero, 8,386 positive; at most 0 decimal(s) used, 0 non-integer value(s); by transaction type: Stock Adjustment at Stocktake negative 21, positive 19, zero 4; Stock Issue negative 228,432; Stock Receipt positive 8,367.
- C2 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=851490a2e4d3f456 | recheck=every new extract | text: Quantity is additive over time per stock item, in the item's units; its sign is the direction, as the source describes ("positive is incoming stock, negative is outgoing"). Summed it does not reproduce QuantityOnHand (Warehouse.StockItemHoldings 09_derived.md#C1).
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=851490a2e4d3f456 | recheck=every new extract | text: Declared decimal(18,3), it holds whole numbers only (0 non-integer values).

## Reasoning

measures.py profiles every numeric column that is not a key, a foreign key or an audit column: declared type, filling, range, signs (per transaction type where the table has one) and the decimals actually used. How a column adds up - additive over rows and time, semi-additive (a level: summable across items at one moment, not over time), non-additive (a price, rate, percentage, reading or attribute), or not a measure at all - is the reader's, from the description, the profile and the tests; it is stated as a fact about the column, not as a rule for using it.

## Uncertainties

None.

## For a person

None.
