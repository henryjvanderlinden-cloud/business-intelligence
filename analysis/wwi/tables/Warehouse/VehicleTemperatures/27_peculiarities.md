---
id: wwi:object:1243151474
subject: wwi/tables/Warehouse/VehicleTemperatures
item: 27
topic: peculiarities
tier: minimum
summary: A structured column that does not parse: FullSensorData is malformed JSON in every row; unused compression columns.
confidence: high
claims: 6
written_by: claude-opus-5-5
written_at: 2026-10-18T13:20:00Z
step: S08-054
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py 102dceeb7d85ec3db493afa75ff1e907c8b3f3a6, profile_tables.py e61ada2547265905e3558722cd127e81fa5cd770, evidence_shared.py 03d3dfbc0522d76aef793a33dc2bc491abc70529
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 917537459f200f48b86e064dc4cf7f1ec6fec8088085a48ff13f8534bbd31e6a
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=54d0a8a7a090f855 | recheck=the empty-column patterns change | text: Test 8: 1 distinct pattern of empty columns; the most common: 66,430 rows with CompressedSensorData empty.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=54d0a8a7a090f855 | recheck=a row breaks a dependency | text: Test 1: 0 functional dependencies between non-key columns over the whole extract (0 involving audit columns, a batch-edit signature, not listed).
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=54d0a8a7a090f855 | recheck=the structured columns change | text: Test 6: FullSensorData holds JSON in 66,430 rows, 0 of which parse.
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=54d0a8a7a090f855 | recheck=a column is added | text: Test 16: no column name ends in a digit.
- C5 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=54d0a8a7a090f855 | recheck=every new extract, or a schema change | text: Test 6 and a quality defect: FullSensorData starts as JSON but fails to parse in all 66,430 rows (a missing quote after the sensor number); a parser must repair or skip it.
- C6 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=54d0a8a7a090f855 | recheck=every new extract, or a schema change | text: IsCompressed is 0 and CompressedSensorData empty in every row: a second representation of the same data, unused.

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

None.

## For a person

None.
