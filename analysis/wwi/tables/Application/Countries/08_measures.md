---
id: wwi:object:1461580245
subject: wwi/tables/Application/Countries
item: 08
topic: measures
tier: best-effort
summary: IsoNumericCode is a code, not a number; LatestRecordedPopulation an attribute.
confidence: high
claims: 4
written_by: claude-opus-5-5
written_at: 2026-10-20T20:06:00Z
step: S08-112
method: measures by prototypes/information_analysis/measures.py (blob 89f3c0d7d2fd53e7e60d4575675beeac0ebb43e8), claims by write_measures.py (blob 8f679dc60353e6e20d24f22fad398861cc10b5ab); readings by claude-opus-5-5
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 4840337d7b437a1e0ba71ae6b072f3f504e276f802274f763ad925b52a0bcc05
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=48b2d646452e9414 | recheck=every new extract | text: IsoNumericCode: int(10,0), filled on 190 of 190 rows, range 4 to 894; 0 negative, 0 zero, 190 positive; at most 0 decimal(s) used.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=48b2d646452e9414 | recheck=every new extract | text: LatestRecordedPopulation: bigint(19,0), filled on 190 of 190 rows, range 14019 to 1392157488; 0 negative, 0 zero, 190 positive; at most 0 decimal(s) used.
- C3 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=48b2d646452e9414 | recheck=every new extract | text: IsoNumericCode is the ISO numeric code of the country, an identifier stored as an int, not a measure.
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=48b2d646452e9414 | recheck=every new extract | text: Where a country has provinces (1 compared), the sum of their LatestRecordedPopulation exceeds the country's own on 1 and equals it on 0.

## Reasoning

measures.py profiles every numeric column that is not a key, a foreign key or an audit column: declared type, filling, range, signs (per transaction type where the table has one) and the decimals actually used. How a column adds up - additive over rows and time, semi-additive (a level: summable across items at one moment, not over time), non-additive (a price, rate, percentage, reading or attribute), or not a measure at all - is the reader's, from the description, the profile and the tests; it is stated as a fact about the column, not as a rule for using it.

## Uncertainties

None.

## For a person

None.
