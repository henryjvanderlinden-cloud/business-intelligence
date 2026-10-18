---
id: wwi:object:290100074
subject: wwi/tables/Application/StateProvinces
item: 01
topic: granularity
tier: minimum
summary: One row per state or province, identified by StateProvinceID; all 53 in the United States.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-18T20:32:00Z
step: S08-061
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py 102dceeb7d85ec3db493afa75ff1e907c8b3f3a6, profile_tables.py e61ada2547265905e3558722cd127e81fa5cd770, evidence_shared.py 03d3dfbc0522d76aef793a33dc2bc491abc70529
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: b85fd6a1b65683d407663a7b52ebc7c96f376f8345323ada5a5fc81b70edef97
last_checked_at: 2026-10-18T20:32:00Z
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=b4dd7fb18f3fa094 | recheck=the primary key changes | text: The declared primary key is StateProvinceID (PK_Application_StateProvinces).
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=42d1716e974f6792 | recheck=the key stops being unique | text: The key is unique over all 53 rows, with no empty values.
- C3 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=b4dd7fb18f3fa094 | recheck=every new extract, or a schema change | text: Grain: one row per state, territory or district, with its sales territory, boundary and population.

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

None.

## For a person

None.
