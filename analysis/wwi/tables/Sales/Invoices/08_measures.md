---
id: wwi:object:2018106230
subject: wwi/tables/Sales/Invoices
item: 08
topic: measures
tier: best-effort
summary: TotalDryItems and TotalChillerItems count lines, not quantities.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-20T20:06:00Z
step: S08-112
method: measures by prototypes/information_analysis/measures.py (blob 89f3c0d7d2fd53e7e60d4575675beeac0ebb43e8), claims by write_measures.py (blob 8f679dc60353e6e20d24f22fad398861cc10b5ab); readings by claude-opus-5-5
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: d89a1e72bf72f1577926929cb7c514b71af6cf08eb13a8181f4f8688da7f99ce
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=10477345ee49ad0b | recheck=every new extract | text: TotalChillerItems: int(10,0), filled on 70,566 of 70,566 rows, range 0 to 3; 0 negative, 69,567 zero, 999 positive; at most 0 decimal(s) used; values 0 (69,567), 1 (956), 2 (41), 3 (2).
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=10477345ee49ad0b | recheck=every new extract | text: TotalDryItems: int(10,0), filled on 70,566 of 70,566 rows, range 0 to 5; 0 negative, 16 zero, 70,550 positive; at most 0 decimal(s) used; values 0 (16), 1 (5,740), 2 (17,039), 3 (17,195), 4 (16,895), 5 (13,681).
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=10477345ee49ad0b | recheck=every new extract | text: TotalDryItems and TotalChillerItems are described as package totals for the driver, but equal the number of dry and chiller lines of the invoice (27_peculiarities.md#C11): additive as counts of lines, not of goods; joined to the lines they are repeated on each.

## Reasoning

measures.py profiles every numeric column that is not a key, a foreign key or an audit column: declared type, filling, range, signs (per transaction type where the table has one) and the decimals actually used. How a column adds up - additive over rows and time, semi-additive (a level: summable across items at one moment, not over time), non-additive (a price, rate, percentage, reading or attribute), or not a measure at all - is the reader's, from the description, the profile and the tests; it is stated as a fact about the column, not as a rule for using it.

## Uncertainties

None.

## For a person

None.
