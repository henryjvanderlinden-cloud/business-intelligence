---
id: wwi:object:510624862
subject: wwi/tables/Sales/InvoiceLines
item: 09
topic: derived
tier: best-effort
summary: TaxAmount = Quantity x UnitPrice x TaxRate / 100, rounded; ExtendedPrice = Quantity x UnitPrice + TaxAmount; LineProfit = Quantity x (UnitPrice - the item's current LastCostPrice); all on every line.
confidence: high
claims: 4
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=fa43419277162f95 | recheck=every new extract | text: TaxAmount equals Quantity x UnitPrice x TaxRate / 100 rounded half up to cents on 228,432 of 228,432 lines (28_arithmetic.md#C1).
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=fa43419277162f95 | recheck=every new extract | text: ExtendedPrice equals Quantity x UnitPrice + TaxAmount on 228,432 of 228,432 lines.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=fa43419277162f95 | recheck=every new extract | text: LineProfit equals Quantity x (UnitPrice - LastCostPrice), with LastCostPrice the stock item's value in Warehouse.StockItemHoldings in this extract, on 228,432 of 228,432 lines. The source describes it as "Profit made on this line item at current cost price".
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=fa43419277162f95 | recheck=every new extract | text: UnitPrice equals the stock item's current UnitPrice on 227,915 of 228,432 lines and TaxRate its current TaxRate on 228,432: the line keeps the price charged (27_peculiarities.md#C4).

## Reasoning

measures.py recomputes the values that the table's columns suggest are computed from others and compares them with the stored ones, row by row; where a formula was found by inspecting ratios first, that is said. A formula that holds on every row of the extract is observed; that it is the source's own rule is a reading.

## Uncertainties

Whether LineProfit follows a change in cost price, and whether the cost at the time of a sale differed from the current one, is not established: no LastCostPrice changed between the extracts compared (Warehouse.StockItemHoldings 29_position.md#C6).

## For a person

None.
