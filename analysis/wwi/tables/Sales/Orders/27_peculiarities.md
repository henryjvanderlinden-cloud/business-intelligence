---
id: wwi:object:1154103152
subject: wwi/tables/Sales/Orders
item: 27
topic: peculiarities
tier: minimum
summary: Three hidden kinds of row; the customer's contact and the expected delivery date ride along as functions of other columns; order chains are a hierarchy inside the table; the daily simulation stops creating backorders, a change of behaviour at a date.
confidence: low
claims: 11
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
recheck_when: every new extract, or a schema change
---

## Claims

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=706b5495e97bfd7b | recheck=the dependency is broken by a row | text: Test 1, two entities side by side: ContactPersonID and CustomerID determine each other on every row, so the contact is a customer attribute carried on the order (whether copied at the time or looked up is item 12, not done).
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=706b5495e97bfd7b,c6e5d1bc0af05898 | recheck=a fourth empty-column pattern appears | text: Test 8, subtypes: three kinds of row, told apart only by empty columns - picked orders (63,020), split originals with picking time but no picker (7,546, exactly the orders with a backorder) and never-picked orders (3,087).
- C3 | type=observed | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=706b5495e97bfd7b | recheck=the dependency is broken by a row | text: OrderDate determines ExpectedDeliveryDate on every row: the expected date appears to be derived from the order date by a rule (item 9, not done).
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=c6e5d1bc0af05898 | recheck=a chain changes | text: Test 11, levels of a hierarchy: an order and its backorders form chains of up to four rows inside the table (7,066 of two rows, 234 of three, 4 of four).
- C5 | type=implemented | status=proposed | confidence=low | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=ecb87399219a74ce,c6e5d1bc0af05898 | recheck=a simulated day creates a backorder | text: Test 18, behaviour changing at a date: backorders were created in every year of the history (1,012 in 2016 to June), but the daily simulation creates none, so from 2016-06-01 the share of split orders will fall.
- C6 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=7aa3df3f1beb91b7 | recheck=another technical editor appears | text: Test 14, rows of another origin: 5 orders were last edited by the technical user Data Conversion Only (07_population.md#C5); no other sign of migrated rows.
- C7 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=b6da684f0b7581f7,77ee039bf95c3ee8,706b5495e97bfd7b | recheck=a numeric measure column or a rollup row appears | text: Tests 2 to 7 and 9 find nothing: the table has no measures (only ids, dates, a flag and text), no total rows (no empty customer or date), no structure inside a column, one time grain (dates without time), and no exclusive arcs.
- C8 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=b8b837693651efad,77ee039bf95c3ee8 | recheck=OrderID stops being unique | text: Test 12: no current and historical rows together; OrderID alone is unique.
- C9 | type=observed | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=b6da684f0b7581f7 | recheck=a company, tenant or scenario column appears | text: Test 13: no company, tenant or scenario column; one partition.
- C10 | type=observed | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=b6da684f0b7581f7,706b5495e97bfd7b | recheck=a sign flag or a repeating group appears | text: Best-effort tests 10, 15, 16, 17: no reversal flag, no overloaded column found, no repeating groups (no column names ending in digits), no unit columns.
- C11 | type=observed | status=proposed | confidence=low | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=706b5495e97bfd7b | recheck=the dependency is broken by a row | text: PickingCompletedWhen and LastEditedWhen each determine the picker: probably an artefact of how the simulator schedules pickers, not a business rule.

## Reasoning

The empty-column patterns and dependencies are exact over the whole extract. C3 and C11 are dependencies found in the data whose cause is not established, hence lower confidence. C5 rests on the simulator's code read second-hand.

## Uncertainties

C3 and C11: whether the dependencies are rules or coincidences of a synthetic data set. C5 is settled by advancing days and counting new backorders.

## For a person

None.
