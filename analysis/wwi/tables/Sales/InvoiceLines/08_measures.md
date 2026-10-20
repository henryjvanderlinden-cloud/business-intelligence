---
id: wwi:object:510624862
subject: wwi/tables/Sales/InvoiceLines
item: 08
topic: measures
tier: best-effort
summary: Quantity in packages of the line's package type; UnitPrice and TaxRate non-additive; TaxAmount, ExtendedPrice (tax included) and LineProfit (tax excluded) additive.
confidence: medium
claims: 10
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=fa43419277162f95 | recheck=every new extract | text: ExtendedPrice: decimal(18,2), filled on 228,432 of 228,432 rows, range 2.88 to 21838.50; 0 negative, 0 zero, 228,432 positive; at most 2 decimal(s) used, 171,118 non-integer value(s).
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=fa43419277162f95 | recheck=every new extract | text: LineProfit: decimal(18,2), filled on 228,432 of 228,432 rows, range -645.00 to 9200.00; 4,632 negative, 0 zero, 223,800 positive; at most 2 decimal(s) used, 51,219 non-integer value(s).
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=fa43419277162f95 | recheck=every new extract | text: Quantity: int(10,0), filled on 228,432 of 228,432 rows, range 1 to 360; 0 negative, 0 zero, 228,432 positive; at most 0 decimal(s) used.
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=fa43419277162f95 | recheck=every new extract | text: TaxAmount: decimal(18,2), filled on 228,432 of 228,432 rows, range 0.38 to 2848.50; 0 negative, 0 zero, 228,432 positive; at most 2 decimal(s) used, 171,118 non-integer value(s).
- C5 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=fa43419277162f95 | recheck=every new extract | text: TaxRate: decimal(18,3), filled on 228,432 of 228,432 rows, range 10.000 to 15.000; 0 negative, 0 zero, 228,432 positive; at most 0 decimal(s) used, 0 non-integer value(s); values 10.000 (1,044), 15.000 (227,388).
- C6 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=fa43419277162f95 | recheck=every new extract | text: UnitPrice: decimal(18,2), filled on 228,432 of 228,432 rows, range 0.66 to 1899.00; 0 negative, 0 zero, 228,432 positive; at most 2 decimal(s) used, 39,752 non-integer value(s).
- C7 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=fa43419277162f95 | recheck=every new extract | text: Quantity is additive over lines of one stock item; across items it adds packages of different kinds (27_peculiarities.md#C6).
- C8 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=fa43419277162f95 | recheck=every new extract | text: UnitPrice is a price per unit of Quantity, excluding tax (Quantity x UnitPrice is the line amount before tax, 09_derived.md#C2), and TaxRate a percentage (10.000 on 1,044 lines, 15.000 on 227,388 lines): both non-additive; a total is Quantity x UnitPrice summed, not UnitPrice summed.
- C9 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=fa43419277162f95 | recheck=every new extract | text: TaxAmount and ExtendedPrice are additive amounts; ExtendedPrice includes tax (09_derived.md#C2). LineProfit is additive and excludes tax (09_derived.md#C3).
- C10 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=fa43419277162f95 | recheck=every new extract | text: LineProfit is negative on 4,632 lines: sold below the current cost price (09_derived.md#C3).

## Reasoning

measures.py profiles every numeric column that is not a key, a foreign key or an audit column: declared type, filling, range, signs (per transaction type where the table has one) and the decimals actually used. How a column adds up - additive over rows and time, semi-additive (a level: summable across items at one moment, not over time), non-additive (a price, rate, percentage, reading or attribute), or not a measure at all - is the reader's, from the description, the profile and the tests; it is stated as a fact about the column, not as a rule for using it.

## Uncertainties

None.

## For a person

None.
