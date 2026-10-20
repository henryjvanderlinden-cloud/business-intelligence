---
id: wwi:object:1314103722
subject: wwi/tables/Warehouse/StockItems
item: 08
topic: measures
tier: best-effort
summary: UnitPrice and RecommendedRetailPrice prices, TaxRate a percentage, QuantityPerOuter a conversion factor, LeadTimeDays and TypicalWeightPerUnit attributes: none additive.
confidence: high
claims: 7
written_by: claude-opus-5-5
written_at: 2026-10-20T20:06:00Z
step: S08-112
method: measures by prototypes/information_analysis/measures.py (blob 89f3c0d7d2fd53e7e60d4575675beeac0ebb43e8), claims by write_measures.py (blob 8f679dc60353e6e20d24f22fad398861cc10b5ab); readings by claude-opus-5-5
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: a2a70ec4f434c5caf3e43bfaa2fcb63886a956c95e50e40cbf6b01c6e0f40c7d
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=277c0ec49cddab1c | recheck=every new extract | text: LeadTimeDays: int(10,0), filled on 227 of 227 rows, range 2 to 20; 0 negative, 0 zero, 227 positive; at most 0 decimal(s) used; values 12 (90), 14 (96), 2 (3), 20 (4), 3 (8), 7 (26).
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=277c0ec49cddab1c | recheck=every new extract | text: QuantityPerOuter: int(10,0), filled on 227 of 227 rows, range 1 to 36; 0 negative, 0 zero, 227 positive; at most 0 decimal(s) used; values 1 (119), 10 (31), 12 (42), 20 (1), 24 (17), 25 (12), 26 (1), 36 (2), 5 (2).
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=277c0ec49cddab1c | recheck=every new extract | text: RecommendedRetailPrice: decimal(18,2), filled on 227 of 227 rows, range 0.99 to 2839.01; 0 negative, 0 zero, 227 positive; at most 2 decimal(s) used, 227 non-integer value(s).
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=277c0ec49cddab1c | recheck=every new extract | text: TaxRate: decimal(18,3), filled on 227 of 227 rows, range 10.000 to 15.000; 0 negative, 0 zero, 227 positive; at most 0 decimal(s) used, 0 non-integer value(s); values 10.000 (8), 15.000 (219).
- C5 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=277c0ec49cddab1c | recheck=every new extract | text: TypicalWeightPerUnit: decimal(18,3), filled on 227 of 227 rows, range 0.050 to 21.000; 0 negative, 0 zero, 227 positive; at most 2 decimal(s) used, 187 non-integer value(s).
- C6 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=277c0ec49cddab1c | recheck=every new extract | text: UnitPrice: decimal(18,2), filled on 227 of 227 rows, range 0.66 to 1899.00; 0 negative, 0 zero, 227 positive; at most 2 decimal(s) used, 45 non-integer value(s).
- C7 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=277c0ec49cddab1c | recheck=every new extract | text: None of the numeric columns is additive: UnitPrice (selling price excluding tax, per unit) and RecommendedRetailPrice are prices, TaxRate a percentage, QuantityPerOuter the number of units in an outer package (the factor between purchase and sales quantities), LeadTimeDays and TypicalWeightPerUnit attributes of the item. TypicalWeightPerUnit's unit is not declared.

## Reasoning

measures.py profiles every numeric column that is not a key, a foreign key or an audit column: declared type, filling, range, signs (per transaction type where the table has one) and the decimals actually used. How a column adds up - additive over rows and time, semi-additive (a level: summable across items at one moment, not over time), non-additive (a price, rate, percentage, reading or attribute), or not a measure at all - is the reader's, from the description, the profile and the tests; it is stated as a fact about the column, not as a rule for using it.

## Uncertainties

None.

## For a person

None.
