---
id: wwi:object:1179151246
subject: wwi/tables/Warehouse/ColdRoomTemperatures
item: 06
topic: keys
tier: minimum
summary: ColdRoomTemperatureID is the declared key, but it changes with every reading; ColdRoomSensorNumber is the stable key.
confidence: medium
claims: 2
written_by: claude-opus-5-5
written_at: 2026-10-19T07:26:00Z
step: S08-066
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py 102dceeb7d85ec3db493afa75ff1e907c8b3f3a6, profile_tables.py e61ada2547265905e3558722cd127e81fa5cd770, evidence_shared.py 35cdfcd24713d6e9eb43784f7e3be5b8228ce8bb
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 14944a147c4e342c01346a89c29d042ac1cf08b8a5e6a7295cf5942e81465a82
last_checked_at: 2026-10-19T07:26:00Z
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=d661ae2a5f707ded | recheck=the key range changes | text: The key runs from 3,676,805 to 3,676,808 with no gap.
- C2 | type=observed | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=fa20eeab979e5e25,832defd8d73a4d23 | recheck=the sensors change | text: Across the two extracts the same four sensor numbers carry new ColdRoomTemperatureID values: the sensor number is the identity that persists, the id identifies a reading. Two observations, no declared rule.

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

None.

## For a person

None.
