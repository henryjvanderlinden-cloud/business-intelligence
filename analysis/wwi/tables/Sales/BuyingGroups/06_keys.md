---
id: wwi:object:1957582012
subject: wwi/tables/Sales/BuyingGroups
item: 06
topic: keys
tier: minimum
summary: Primary key unique and gapless; BuyingGroupName is declared unique.
confidence: medium
claims: 4
written_by: claude-opus-5-5
written_at: 2026-10-18T13:20:00Z
step: S08-054
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py 102dceeb7d85ec3db493afa75ff1e907c8b3f3a6, profile_tables.py e61ada2547265905e3558722cd127e81fa5cd770, evidence_shared.py 03d3dfbc0522d76aef793a33dc2bc491abc70529
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 297115804655cf4216c6a4fddc22ea28db74d9e3dc4eab79962b9172a801b9a3
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=ee1eebac15b0a67f | recheck=a unique constraint changes | text: Declared unique besides the primary key: UQ_Sales_BuyingGroups_BuyingGroupName (BuyingGroupName).
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=f25d3c1535c3ec51 | recheck=the key range changes | text: The key runs from 1 to 2 with no gap.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=ee1eebac15b0a67f | recheck=a foreign key changes | text: 1 declared foreign key, all enabled and trusted: LastEditedBy -> Application.People.PersonID.
- C4 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=ee1eebac15b0a67f | recheck=every new extract, or a schema change | text: Business key candidate: the unique name (BuyingGroupName is declared unique); the numeric key is the source's surrogate.

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

None.

## For a person

None.
