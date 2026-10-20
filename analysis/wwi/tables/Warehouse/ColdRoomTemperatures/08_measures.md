---
id: wwi:object:1179151246
subject: wwi/tables/Warehouse/ColdRoomTemperatures
item: 08
topic: measures
tier: best-effort
summary: Temperature a reading (non-additive); ColdRoomSensorNumber an identifier.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-20T20:06:00Z
step: S08-112
method: measures by prototypes/information_analysis/measures.py (blob 89f3c0d7d2fd53e7e60d4575675beeac0ebb43e8), claims by write_measures.py (blob 8f679dc60353e6e20d24f22fad398861cc10b5ab); readings by claude-opus-5-5
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 14944a147c4e342c01346a89c29d042ac1cf08b8a5e6a7295cf5942e81465a82
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=dd6aacdd0951d4c8 | recheck=every new extract | text: ColdRoomSensorNumber: int(10,0), filled on 4 of 4 rows, range 1 to 4; 0 negative, 0 zero, 4 positive; at most 0 decimal(s) used; values 1 (1), 2 (1), 3 (1), 4 (1).
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=dd6aacdd0951d4c8 | recheck=every new extract | text: Temperature: decimal(10,2), filled on 4 of 4 rows, range 3.33 to 4.86; 0 negative, 0 zero, 4 positive; at most 2 decimal(s) used, 4 non-integer value(s); values 3.33 (1), 3.36 (1), 3.98 (1), 4.86 (1).
- C3 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=dd6aacdd0951d4c8 | recheck=every new extract | text: Temperature is a reading, non-additive (averaged or compared, not summed); ColdRoomSensorNumber identifies the sensor and is not a measure. The unit of Temperature is not declared.

## Reasoning

measures.py profiles every numeric column that is not a key, a foreign key or an audit column: declared type, filling, range, signs (per transaction type where the table has one) and the decimals actually used. How a column adds up - additive over rows and time, semi-additive (a level: summable across items at one moment, not over time), non-additive (a price, rate, percentage, reading or attribute), or not a measure at all - is the reader's, from the description, the profile and the tests; it is stated as a fact about the column, not as a rule for using it.

## Uncertainties

None.

## For a person

None.
