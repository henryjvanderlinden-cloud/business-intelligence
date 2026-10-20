---
id: wwi:fk:FK_Warehouse_StockItemTransactions_StockItemID_Warehouse_StockItems
subject: wwi/across/relations/Warehouse.StockItemTransactions.StockItemID__Warehouse.StockItems.StockItemID
item: 03
topic: temporal
tier: best-effort
summary: Point in time: earlier parent version on 236,667 rows, differing in CustomFields, Tags.
confidence: medium
claims: 5
written_by: claude-opus-5-5
written_at: 2026-10-20T05:51:00Z
step: S08-092
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 78540177fbf453018f99dd3faf7db85cb13d79118746359fed7bfcbad97c7655
last_checked_at: 2026-10-20T05:51:00Z
last_checked_by: claude-opus-5-5
last_checked_against: 2016-06-01
reviewed_by: none
reviewed_at: none
ruled_by: none
ruled_at: none
supersedes: none
superseded_by: none
recheck_when: every new extract, or a schema change of either table
---

## Claims

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=9611dca6b52c15f1 | recheck=the temporal type changes | text: Warehouse.StockItems is system-versioned: the version of a row current at a given time is in Warehouse.StockItems_Archive or the table itself, by ValidFrom and ValidTo.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=9611dca6b52c15f1 | recheck=every new extract | text: As of the end of each row's date (TransactionOccurredWhen), the row of Warehouse.StockItems it names was: the current version on 176; an earlier version on 236,667.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=9611dca6b52c15f1 | recheck=every new extract | text: On 236,667 of those earlier versions some attributes differ from the current version: CustomFields (236,667 rows), Tags (236,667 rows). Joined in the extract, these rows get the current values of these columns, not the values of their date.
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=9611dca6b52c15f1 | recheck=every new extract | text: No other attribute of Warehouse.StockItems differs between the version current at a row's date and the current version (LastEditedBy, LastEditedWhen and the period columns are not compared).
- C5 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=none | recheck=a ValidFrom far from simulated time appears | text: The comparison places business dates against system time (ValidFrom), which is the server's clock at the change; in WWI it follows the simulated dates except for one version of Application.Countries stamped 2022 (round 1), so it holds as far as the two clocks agree.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
