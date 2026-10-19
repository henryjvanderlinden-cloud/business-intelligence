---
id: wwi:object:1243151474
subject: wwi/tables/Warehouse/VehicleTemperatures
item: 06
topic: keys
tier: minimum
summary: VehicleTemperatureID is the declared key, unique and gapless; (ChillerSensorNumber, RecordedWhen) is a natural key.
confidence: medium
claims: 2
written_by: claude-opus-5-5
written_at: 2026-10-19T09:21:00Z
step: S08-072
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py 102dceeb7d85ec3db493afa75ff1e907c8b3f3a6, profile_tables.py e61ada2547265905e3558722cd127e81fa5cd770, evidence_shared.py 4174839b1036cd70f0c837acdee322e7071ca4b0
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 917537459f200f48b86e064dc4cf7f1ec6fec8088085a48ff13f8534bbd31e6a
last_checked_at: 2026-10-19T09:21:00Z
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=54d0a8a7a090f855 | recheck=the key range changes | text: The key runs from 1 to 66,430 with no gap.
- C2 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=b34c6f70cd6b509d | recheck=every new extract, or a schema change | text: Natural key: (VehicleRegistration, ChillerSensorNumber, RecordedWhen); with one vehicle, the sensor and time suffice.

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

None.

## For a person

None.
