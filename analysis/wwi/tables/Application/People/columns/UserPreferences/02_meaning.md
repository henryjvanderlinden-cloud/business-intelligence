---
id: wwi:object:1301579675:column:12
subject: wwi/tables/Application/People/columns/UserPreferences
item: 02
topic: meaning
tier: best-effort
summary: JSON with a person's website preferences (theme, date format, time zone, table paging); filled for 182 people.
confidence: medium
claims: 4
written_by: claude-opus-5-5
written_at: 2026-10-19T09:21:00Z
step: S08-072
method: mechanical claims by prototypes/information_analysis/write_column_meanings.py from the catalogue and profile evidence; readings by claude-opus-5-5 from that evidence and Microsoft's description of the business (evidence 0f9e0d3eb9dd8048); script blob write_column_meanings.py d323750bb7f53a5d89ef6436d25f033e9ecfabd0
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 5f24e9163953099bd97211216302ba9edbe184de9237880789cd61681982e529
last_checked_at: 2026-10-19T09:21:00Z
last_checked_by: claude-opus-5-5
last_checked_against: 2016-06-01
reviewed_by: none
reviewed_at: none
ruled_by: none
ruled_at: none
supersedes: none
superseded_by: none
recheck_when: the description changes, or every new extract
---

## Claims

- C1 | type=declared | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=3654cc5be0d96b13 | recheck=the description changes | text: The source describes it as "User preferences related to the website (holds JSON data)" (declared, not verified against behaviour beyond the claims below).
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=3654cc5be0d96b13 | recheck=a column type changes | text: Declared as nvarchar(max), nullable.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=419f7b85d80b0191 | recheck=every new extract | text: Observed: filled on 182 of 1,111 rows; 59 distinct values; JSON on 182 rows, 182 parse.
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=419f7b85d80b0191 | recheck=the description changes, or every new extract | text: The JSON keys are dateFormat, favoritesOnDashboard, table, theme and timeZone on all 182 filled rows.

## Reasoning

Mechanical claims from the catalogue and profile; any reading is the writer's, with its confidence.

## Uncertainties

None.

## For a person

None.
