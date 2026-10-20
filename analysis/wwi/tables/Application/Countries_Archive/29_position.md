---
id: wwi:object:1557580587
subject: wwi/tables/Application/Countries_Archive
item: 29
topic: position
tier: best-effort
summary: History of Application.Countries, outside the graph; row count unchanged.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-20T17:55:00Z
step: S08-103
method: measures by prototypes/information_analysis/structure.py (blob d233c4ccad6463612e1d19890d508485eb6b0fc4), claims by write_position.py (blob ecc1fbffc8f024846f4b6131ea07aea781e7610a); method docs/10_architecture/131_structural-position.md; readings by claude-opus-5-5
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 4840337d7b437a1e0ba71ae6b072f3f504e276f802274f763ad925b52a0bcc05
last_checked_at: 2026-10-20T17:55:00Z
last_checked_by: claude-opus-5-5
last_checked_against: 2016-06-02
reviewed_by: none
reviewed_at: none
ruled_by: none
ruled_at: none
supersedes: none
superseded_by: none
recheck_when: a foreign key changes, or every new extract
---

## Claims

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=94bc8dbba39fcbfb | recheck=a foreign key changes | text: Declares 0 foreign key(s) and is referred to by 0: it is not a node of the graph of 131, whose links are declared foreign keys.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=94bc8dbba39fcbfb | recheck=every new extract | text: Rows: 37 on 2016-05-31; 37 on 2016-06-01; 37 on 2016-06-02. Behaviour: row count unchanged.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=94bc8dbba39fcbfb | recheck=a rule of 131 or the schema changes | text: Class by the rules of 131: history (rule 1, a history table of system-versioning); it keeps the earlier versions of Application.Countries and takes that table's position: master, sink, betweenness rank 23 (../../Application/Countries/29_position.md).

## Reasoning

A history table of system-versioning carries no declared keys and so is not a node of the graph; its position is that of the table whose earlier versions it keeps. Its rows per extract come from the manifests.

## Uncertainties

None.

## For a person

None.
