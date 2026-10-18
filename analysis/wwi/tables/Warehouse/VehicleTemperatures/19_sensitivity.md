---
id: wwi:object:1243151474
subject: wwi/tables/Warehouse/VehicleTemperatures
item: 19
topic: sensitivity
tier: minimum
summary: A vehicle's GPS positions over time, which can track a driver.
confidence: low
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-18T20:32:00Z
step: S08-061
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py 102dceeb7d85ec3db493afa75ff1e907c8b3f3a6, profile_tables.py e61ada2547265905e3558722cd127e81fa5cd770, evidence_shared.py 03d3dfbc0522d76aef793a33dc2bc491abc70529
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 917537459f200f48b86e064dc4cf7f1ec6fec8088085a48ff13f8534bbd31e6a
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

- C1 | type=declared | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=9048f084eab5cb11 | recheck=a column is added or renamed | text: Columns whose names or descriptions point to personal, contact, location, credential or free-text content: VehicleRegistration.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=54d0a8a7a090f855 | recheck=every new extract, or a schema change | text: FullSensorData holds GeoJSON-like text with coordinates and the vehicle registration for each reading.
- C3 | type=intended | status=proposed | confidence=low | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=9048f084eab5cb11 | recheck=the author rules | text: Proposed reading: a vehicle's position history is personal data of its driver where the driver can be identified (for instance from delivery runs); not otherwise.

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

None.

## For a person

None.
