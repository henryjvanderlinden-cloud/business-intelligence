---
id: wwi:object:1474104292
subject: wwi/tables/Warehouse/StockItemHoldings
item: 29
topic: position
tier: best-effort
summary: Extension, source; betweenness rank 30 of 31; changes without growing.
confidence: medium
claims: 8
written_by: claude-opus-5-5
written_at: 2026-10-20T17:55:00Z
step: S08-103
method: measures by prototypes/information_analysis/structure.py (blob d233c4ccad6463612e1d19890d508485eb6b0fc4), claims by write_position.py (blob ecc1fbffc8f024846f4b6131ea07aea781e7610a); method docs/10_architecture/131_structural-position.md; readings by claude-opus-5-5
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: bb1ea17573cd7d7073444df38e148e0a4fc7ac5b6c6bc1078e0bd538c0085e24
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=94bc8dbba39fcbfb | recheck=a foreign key changes | text: On all 98 declared links between the 31 base tables: referred to by 0 link(s) from 0 other table(s), refers by 2 link(s) to 2 other table(s).
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=94bc8dbba39fcbfb | recheck=a foreign key changes | text: Without the links of LastEditedBy (131, distortion check): referred to by 0 link(s) from 0 other table(s), refers by 1 link(s) to 1 other table(s); position: source.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=94bc8dbba39fcbfb | recheck=a foreign key changes, or every new extract | text: Measures without those links: betweenness 0.0 (rank 30 of 31; 0.0 with all links), 0 role(s) in which other tables name it, 0 rows naming it, reaches 10 table(s) by following links (longest path 5), reached from 0 table(s).
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=94bc8dbba39fcbfb | recheck=every new extract | text: 227 rows on 2016-06-01, 6 attribute(s) besides keys and audit columns; 2016-05-31 to 2016-06-01: 0 inserted, 227 updated, 0 deleted; 2016-06-01 to 2016-06-02: 0 inserted, 227 updated, 0 deleted; behaviour: changes without growing.
- C5 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=94bc8dbba39fcbfb | recheck=a rule of 131 or a foreign key changes | text: Class by the rules of 131: extension (rule: its primary key is a foreign key to one parent: at most one row per parent row). The rule rests on the catalogue and the row count, not on behaviour.
- C6 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=94bc8dbba39fcbfb | recheck=every new extract | text: Rows updated, by changed column: 2016-05-31 to 2016-06-01, 227 row(s) (LastEditedBy 227, LastEditedWhen 227, QuantityOnHand 226), of which 226 changed in a column other than the key and the audit columns; 2016-06-01 to 2016-06-02, 227 row(s) (LastEditedBy 130, LastEditedWhen 227, QuantityOnHand 225), of which 225 changed in a column other than the key and the audit columns.
- C7 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=94bc8dbba39fcbfb | recheck=every new extract | text: Its primary key is a foreign key to Warehouse.StockItems, so it has at most one row per row there; it has 227 rows for 227 there.
- C8 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=94bc8dbba39fcbfb | recheck=a foreign key changes, or every new extract | text: One row per stock item, kept outside system-versioning (05_role.md#C3); every row is updated in both transitions, QuantityOnHand on 226 and 225 of the 227 and the audit column LastEditedWhen on all. These are the stock levels that disagree with the movements in level and in daily change, for a cause the record leaves unknown (across/reconciliations/stock-holdings-vs-movements/16_reconciliation.md#C1, #C2).

## Reasoning

structure.py builds the graph of the 31 base tables, a node per table and an arc per declared foreign key from the referring table to the referenced one, and measures each table on it twice: with all declared links, and without the links of the audit column LastEditedBy, which ties every table to Application.People for a reason that says nothing about the business (docs/10_architecture/131_structural-position.md, distortion check). Betweenness is computed on the graph without direction. Volume and behaviour come from the extracts of 2016-05-31, 2016-06-01 and 2016-06-02. The class follows the rules of 131 in their order; readings in business terms, where a reader adds one, are separate claims and do not change the class by rule.

## Uncertainties

None.

## For a person

None.
