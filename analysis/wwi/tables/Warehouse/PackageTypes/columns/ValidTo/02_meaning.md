---
id: wwi:object:98099390:column:5
subject: wwi/tables/Warehouse/PackageTypes/columns/ValidTo
item: 02
topic: meaning
tier: best-effort
summary: The moment this version stopped being current (period end); 9999-12-31 23:59:59.9999999 for the current version, so in a base table it is always that value.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-19T07:28:00Z
step: S08-067
method: mechanical claims by prototypes/information_analysis/write_column_meanings.py from the catalogue and profile evidence; readings by claude-opus-5-5 from that evidence and Microsoft's description of the business (evidence 0f9e0d3eb9dd8048); script blob write_column_meanings.py ab6eb04a93fb24b0da04e43e0e5426fa51442758
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 0263ce1739bb24cfa1adc545bdeab338bb4e156512ec4dcf93e55e467793997d
last_checked_at: 2026-10-19T07:28:00Z
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=1c7b301d8de3dc31 | recheck=a column type changes | text: Declared as datetime2, not nullable, system-time period end.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=16ad09f897cb33f1 | recheck=every new extract | text: Observed: filled on 14 of 14 rows; 1 distinct value; from 9999-12-31T23:59:59 to 9999-12-31T23:59:59.
- C3 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=1c7b301d8de3dc31,16ad09f897cb33f1 | recheck=a description is found | text: The moment this version stopped being current (period end); 9999-12-31 23:59:59.9999999 for the current version, so in a base table it is always that value.

## Reasoning

Mechanical claims from the catalogue and profile; any reading is the writer's, with its confidence.

## Uncertainties

None.

## For a person

None.
