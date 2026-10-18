---
id: wwi:object:1301579675
subject: wwi/tables/Application/People
item: 03
topic: temporal
tier: minimum
summary: System-versioned; 182 people have earlier versions (962 in the history table); one version was added on 2016-06-01 without any visible column changing.
confidence: medium
claims: 5
written_by: claude-opus-5-5
written_at: 2026-10-18T13:20:00Z
step: S08-054
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py 102dceeb7d85ec3db493afa75ff1e907c8b3f3a6, profile_tables.py e61ada2547265905e3558722cd127e81fa5cd770, evidence_shared.py 03d3dfbc0522d76aef793a33dc2bc491abc70529
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 5f24e9163953099bd97211216302ba9edbe184de9237880789cd61681982e529
last_checked_at: 2026-10-18T13:20:00Z
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=3654cc5be0d96b13 | recheck=the temporal type changes | text: The table is system-versioned: SQL Server keeps every earlier version of a row in Application.People_Archive, with the period columns ValidFrom and ValidTo.
- C2 | type=observed | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=64f5be9db24826d3 | recheck=every new extract | text: Between the extracts of 31 May and 1 June 2016: 0 inserted, 0 deleted, 1 updated; columns updated: ValidFrom (1).
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=3654cc5be0d96b13 | recheck=a column type changes | text: Date columns: none; date-and-time columns without a time zone: none; system-time period columns, datetime2 without a zone, set by SQL Server: ValidFrom, ValidTo.
- C4 | type=observed | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=64f5be9db24826d3 | recheck=a second transition | text: The one update between 31 May and 1 June changed only ValidFrom: a new version without a visible change, either an update that rewrote the same values or a change in a column the extract renders identically.
- C5 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=419f7b85d80b0191 | recheck=every new extract, or a schema change | text: Current versions date from 2013-01-01 to 2016-06-01 08:00.

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

None.

## For a person

None.
