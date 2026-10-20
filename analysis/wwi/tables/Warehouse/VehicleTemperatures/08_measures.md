---
id: wwi:object:1243151474
subject: wwi/tables/Warehouse/VehicleTemperatures
item: 08
topic: measures
tier: best-effort
summary: Temperature a reading (non-additive); ChillerSensorNumber an identifier.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-20T20:06:00Z
step: S08-112
method: measures by prototypes/information_analysis/measures.py (blob 89f3c0d7d2fd53e7e60d4575675beeac0ebb43e8), claims by write_measures.py (blob 8f679dc60353e6e20d24f22fad398861cc10b5ab); readings by claude-opus-5-5
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 917537459f200f48b86e064dc4cf7f1ec6fec8088085a48ff13f8534bbd31e6a
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=15eedb412674f5ad | recheck=every new extract | text: ChillerSensorNumber: int(10,0), filled on 66,430 of 66,430 rows, range 1 to 2; 0 negative, 0 zero, 66,430 positive; at most 0 decimal(s) used; values 1 (33,215), 2 (33,215).
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=15eedb412674f5ad | recheck=every new extract | text: Temperature: decimal(10,2), filled on 66,430 of 66,430 rows, range 3.00 to 5.00; 0 negative, 0 zero, 66,430 positive; at most 2 decimal(s) used, 65,741 non-integer value(s).
- C3 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=15eedb412674f5ad | recheck=every new extract | text: Temperature is a reading, non-additive; ChillerSensorNumber identifies the sensor and is not a measure. The unit of Temperature is not declared.

## Reasoning

measures.py profiles every numeric column that is not a key, a foreign key or an audit column: declared type, filling, range, signs (per transaction type where the table has one) and the decimals actually used. How a column adds up - additive over rows and time, semi-additive (a level: summable across items at one moment, not over time), non-additive (a price, rate, percentage, reading or attribute), or not a measure at all - is the reader's, from the description, the profile and the tests; it is stated as a fact about the column, not as a rule for using it.

## Uncertainties

None.

## For a person

None.
