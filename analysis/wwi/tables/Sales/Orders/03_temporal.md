---
id: wwi:object:1154103152
subject: wwi/tables/Sales/Orders
item: 03
topic: temporal
tier: minimum
summary: No history in the source: rows are inserted daily and updated in place once, when picking completes; no deletion seen, ever; one transition observed.
confidence: unknown
claims: 9
written_by: claude-opus-5-5
written_at: 2026-10-18T12:40:00Z
step: S08-042
method: reading of evidence written by prototypes/information_analysis/evidence_orders.py (blob 5b39164821d92e89109688e68c204752d9edeff5) and of catalogue queries through the sandbox request folder
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: df493a1a20d890a2e0931a1a6e6ddd9510bec9c2a6d09162f4d0a907b0bebca6
last_checked_at: 2026-10-18T12:40:00Z
last_checked_by: claude-opus-5-5
last_checked_against: 2016-06-01
reviewed_by: none
reviewed_at: none
ruled_by: none
ruled_at: none
supersedes: analysis layout 1 of c7b7aa2 (moved out of the repository)
superseded_by: none
recheck_when: every new extract (re-run the transition), a schema change, or a second kind of update
---

## Claims

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=6b9b2e34cfa5d3e1 | recheck=the temporal type changes | text: Mutation: the table is NON_TEMPORAL_TABLE, so the source keeps no history of its own.
- C2 | type=observed | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=339f4ab018dfda14 | recheck=a second transition shows another kind of update | text: Between 31 May and 1 June 2016, 58 rows were inserted and 6 updated; every update set PickedByPersonID and PickingCompletedWhen on an order not picked before and moved LastEditedWhen; no other column changed.
- C3 | type=implemented | status=proposed | confidence=low | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=ecb87399219a74ce | recheck=the simulator procedures change | text: Microsoft's simulator inserts orders with picking empty and sets the header's picking only when all its lines are picked; read through a summarising fetch.
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=339f4ab018dfda14,77ee039bf95c3ee8 | recheck=a row disappears, or OrderID shows a gap | text: Deletion: none in the transition, and none in the history, since OrderID runs from 1 to 73,653 without a gap, unless deleted numbers were reused.
- C5 | type=observed | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=339f4ab018dfda14 | recheck=a late-dated insert appears | text: Arrival latency: all 58 inserted orders are dated the day they arrived; correction: none observed.
- C6 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=b6da684f0b7581f7 | recheck=a column type changes | text: Effective dating: none. OrderDate and ExpectedDeliveryDate are of type date; PickingCompletedWhen and LastEditedWhen are datetime2 without a zone.
- C7 | type=observed | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=77ee039bf95c3ee8,7aa3df3f1beb91b7 | recheck=old unpicked orders keep being picked | text: Lifecycle: raised, then picked, sometimes long after (an order of 2015-12-29 was picked on 2016-06-01); 3,087 orders were never picked, the oldest from 2013-01-12, and none of their 3,149 lines has a picked quantity above zero.
- C8 | type=observed | status=proposed | confidence=unknown | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=none | recheck=a time zone is found in documentation or the catalogue | text: The time zone of PickingCompletedWhen and LastEditedWhen is not established; nothing in the catalogue states one.
- C9 | type=intended | status=proposed | confidence=unknown | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=none | recheck=the author rules | text: Which date the business reports orders by is not established.

## Reasoning

The source declares no history, and the one transition shows one kind of update, which the simulator's code explains. Daily full extracts therefore capture every state change seen so far; warehouse history would be sampled history in 127's sense, exact only while no order changes twice in a day.

## Uncertainties

C2 and C5 rest on one transition: corrections, deletions and late arrivals could exist and not show in a day. Settled by comparing more simulated days. C8 and C9 are open.

## For a person

Which date do reports use for orders: OrderDate, or the picking date?
