---
id: wwi:object:1301579675
subject: wwi/tables/Application/People
item: 29
topic: position
tier: best-effort
summary: Master, sink; betweenness rank 12 of 31; only audit or system-time columns change.
confidence: medium
claims: 8
written_by: claude-opus-5-5
written_at: 2026-10-20T17:55:00Z
step: S08-103
method: measures by prototypes/information_analysis/structure.py (blob d233c4ccad6463612e1d19890d508485eb6b0fc4), claims by write_position.py (blob ecc1fbffc8f024846f4b6131ea07aea781e7610a); method docs/10_architecture/131_structural-position.md; readings by claude-opus-5-5
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 5f24e9163953099bd97211216302ba9edbe184de9237880789cd61681982e529
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=94bc8dbba39fcbfb | recheck=a foreign key changes | text: On all 98 declared links between the 31 base tables: referred to by 40 link(s) from 28 other table(s), refers by 1 link(s) to 0 other table(s); self-reference through LastEditedBy.
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=94bc8dbba39fcbfb | recheck=a foreign key changes | text: Without the links of LastEditedBy (131, distortion check): referred to by 12 link(s) from 5 other table(s), refers by 0 link(s) to 0 other table(s); position: sink.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=94bc8dbba39fcbfb | recheck=a foreign key changes, or every new extract | text: Measures without those links: betweenness 0.0234 (rank 12 of 31; 0.5966 with all links), 12 role(s) in which other tables name it, 495,757 rows naming it, reaches 0 table(s) by following links (longest path 0), reached from 15 table(s).
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=94bc8dbba39fcbfb | recheck=every new extract | text: 1,111 rows on 2016-06-01, 17 attribute(s) besides keys and audit columns; 2016-05-31 to 2016-06-01: 0 inserted, 1 updated, 0 deleted; 2016-06-01 to 2016-06-02: 0 inserted, 1 updated, 0 deleted; behaviour: only audit or system-time columns change.
- C5 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=94bc8dbba39fcbfb | recheck=a rule of 131 or the behaviour changes | text: Class by the rules of 131: master (rule: none of the rules above: does not grow, and has attributes or references of its own). Medium: the behaviour rests on two transitions.
- C6 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=94bc8dbba39fcbfb | recheck=every new extract | text: Rows updated, by changed column: 2016-05-31 to 2016-06-01, 1 row(s) (ValidFrom 1), of which 0 changed in a column other than the key and the audit columns; 2016-06-01 to 2016-06-02, 1 row(s) (ValidFrom 1), of which 0 changed in a column other than the key and the audit columns.
- C7 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=94bc8dbba39fcbfb | recheck=a foreign key changes, or every new extract | text: Without the audit links its position rests on 12 roles in 5 tables: the contact persons of purchase orders, suppliers, customers, invoices and orders (primary, alternate, accounts or contact), the salesperson on orders and invoices, the picker on orders and the packer on invoices (06_keys.md). It is central through what persons do in the business, at betweenness rank 12, not through lying on many paths; with LastEditedBy it would rank first, which is the distortion that 131 checks for.
- C8 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=94bc8dbba39fcbfb | recheck=every new extract | text: Its history table gains one row in each transition, as one row here is updated in ValidFrom only (03_temporal.md#C4, #C6; ../People_Archive/29_position.md).

## Reasoning

structure.py builds the graph of the 31 base tables, a node per table and an arc per declared foreign key from the referring table to the referenced one, and measures each table on it twice: with all declared links, and without the links of the audit column LastEditedBy, which ties every table to Application.People for a reason that says nothing about the business (docs/10_architecture/131_structural-position.md, distortion check). Betweenness is computed on the graph without direction. Volume and behaviour come from the extracts of 2016-05-31, 2016-06-01 and 2016-06-02. The class follows the rules of 131 in their order; readings in business terms, where a reader adds one, are separate claims and do not change the class by rule.

## Uncertainties

None.

## For a person

None.
