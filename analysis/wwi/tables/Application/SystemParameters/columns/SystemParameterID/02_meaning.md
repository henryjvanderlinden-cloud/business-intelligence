---
id: wwi:object:498100815:column:1
subject: wwi/tables/Application/SystemParameters/columns/SystemParameterID
item: 02
topic: meaning
tier: best-effort
summary: Numeric ID used for row holding system parameters
confidence: medium
claims: 4
written_by: claude-opus-5-5
written_at: 2026-10-19T09:21:00Z
step: S08-072
method: mechanical claims by prototypes/information_analysis/write_column_meanings.py from the catalogue and profile evidence; readings by claude-opus-5-5 from that evidence and Microsoft's description of the business (evidence 0f9e0d3eb9dd8048); script blob write_column_meanings.py d323750bb7f53a5d89ef6436d25f033e9ecfabd0
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 1f26426deac5de8b5258e1a7f6e26fc36706678e138f773b0dfe3dfa5f0d5e27
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

- C1 | type=declared | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=0c6c31f37cdc5cc9 | recheck=the description changes | text: The source describes it as "Numeric ID used for row holding system parameters" (declared, not verified against behaviour beyond the claims below).
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=0c6c31f37cdc5cc9 | recheck=a column type changes | text: Declared as int, not nullable.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=0c6c31f37cdc5cc9 | recheck=a key changes | text: Part of the primary key PK_Application_SystemParameters.
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=72df613f2d4d80f5 | recheck=every new extract | text: Observed: filled on 1 of 1 row; 1 distinct value; from 1 to 1; the same value in every row: 1.

## Reasoning

Mechanical claims from the catalogue and profile; any reading is the writer's, with its confidence.

## Uncertainties

None.

## For a person

None.
