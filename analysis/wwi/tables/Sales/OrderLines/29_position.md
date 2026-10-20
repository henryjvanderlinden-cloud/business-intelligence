---
id: wwi:object:94623380
subject: wwi/tables/Sales/OrderLines
item: 29
topic: position
tier: best-effort
summary: Event, source (record); betweenness rank 15 of 31; grows.
confidence: medium
claims: 6
written_by: claude-opus-5-5
written_at: 2026-10-20T17:55:00Z
step: S08-103
method: measures by prototypes/information_analysis/structure.py (blob d233c4ccad6463612e1d19890d508485eb6b0fc4), claims by write_position.py (blob ecc1fbffc8f024846f4b6131ea07aea781e7610a); method docs/10_architecture/131_structural-position.md; readings by claude-opus-5-5
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: c00930db9c641c1b31801c17473429ceaa1b6c45519761d89148dd23ed44a1e7
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=94bc8dbba39fcbfb | recheck=a foreign key changes | text: On all 98 declared links between the 31 base tables: referred to by 0 link(s) from 0 other table(s), refers by 4 link(s) to 4 other table(s).
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=94bc8dbba39fcbfb | recheck=a foreign key changes | text: Without the links of LastEditedBy (131, distortion check): referred to by 0 link(s) from 0 other table(s), refers by 3 link(s) to 3 other table(s); position: source.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=94bc8dbba39fcbfb | recheck=a foreign key changes, or every new extract | text: Measures without those links: betweenness 0.0142 (rank 15 of 31; 0.0023 with all links), 0 role(s) in which other tables name it, 0 rows naming it, reaches 14 table(s) by following links (longest path 5), reached from 0 table(s).
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=94bc8dbba39fcbfb | recheck=every new extract | text: 231,581 rows on 2016-06-01, 6 attribute(s) besides keys and audit columns; 2016-05-31 to 2016-06-01: 169 inserted, 6 updated, 0 deleted; 2016-06-01 to 2016-06-02: 370 inserted, 4 updated, 0 deleted; behaviour: grows.
- C5 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=94bc8dbba39fcbfb | recheck=a rule of 131 or the behaviour changes | text: Class by the rules of 131: event (record) (rule: rows are added in both transitions and none deleted). Medium: the behaviour rests on two transitions.
- C6 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=94bc8dbba39fcbfb | recheck=every new extract | text: Rows updated, by changed column: 2016-05-31 to 2016-06-01, 6 row(s) (LastEditedBy 5, LastEditedWhen 6, PickedQuantity 6, PickingCompletedWhen 6), of which 6 changed in a column other than the key and the audit columns; 2016-06-01 to 2016-06-02, 4 row(s) (LastEditedBy 3, LastEditedWhen 4, PickedQuantity 4, PickingCompletedWhen 4), of which 4 changed in a column other than the key and the audit columns. The class event says that rows are added; it does not say that rows, once added, stay as they are.

## Reasoning

structure.py builds the graph of the 31 base tables, a node per table and an arc per declared foreign key from the referring table to the referenced one, and measures each table on it twice: with all declared links, and without the links of the audit column LastEditedBy, which ties every table to Application.People for a reason that says nothing about the business (docs/10_architecture/131_structural-position.md, distortion check). Betweenness is computed on the graph without direction. Volume and behaviour come from the extracts of 2016-05-31, 2016-06-01 and 2016-06-02. The class follows the rules of 131 in their order; readings in business terms, where a reader adds one, are separate claims and do not change the class by rule.

## Uncertainties

None.

## For a person

None.
