---
id: wwi:object:1154103152
subject: wwi/tables/Sales/Orders
item: 01
topic: granularity
tier: minimum
summary: One row is one order as WWI fulfils it - a customer order or a backorder split from one - identified by OrderID; one customer purchase order can span up to four rows.
confidence: unknown
claims: 6
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
recheck_when: a schema change of Sales.Orders, a new backorder, or the author's ruling on C6
---

## Claims

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=b8b837693651efad,77ee039bf95c3ee8 | recheck=OrderID stops being unique | text: One row per OrderID: the key is declared (see 06_keys.md#C1) and unique over all 73,653 rows.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=7aa3df3f1beb91b7 | recheck=a line without an order, or an order without lines, appears | text: The table is the order header: every order has 1 to 5 lines in Sales.OrderLines and every line belongs to an existing order.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=6b9b2e34cfa5d3e1 | recheck=the table description changes | text: The source describes the table as "Detail of customer orders"; the word means details about orders, not line detail (C2).
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=c6e5d1bc0af05898 | recheck=a new backorder is created | text: A row is not always a customer's order as placed: 7,546 orders were split, the remainder becoming a new row with the same customer and purchase order number (see columns/BackorderOrderID/02_meaning.md#C2); 7,066 purchase orders span two rows, 234 three and 4 four.
- C5 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=706b5495e97bfd7b | recheck=the empty-column patterns change | text: Three kinds of row share the table, told apart only by which columns are empty: picked orders (63,020), split originals (7,546) and never-picked orders (3,087); see 27_peculiarities.md#C2.
- C6 | type=intended | status=proposed | confidence=unknown | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=none | recheck=the author rules | text: Which grain the business means by "an order" - a row, or a customer purchase order with its backorders - is not established; a person must rule.

## Reasoning

Declared and observed agree on the key, so the row grain is high confidence. The split into backorders and the three row kinds are observed without exception over the whole extract. The table's own description is misleading but harmless once read against the data.

## Uncertainties

C6: the business grain of "an order". Counting rows and counting purchase orders differ by 7,546 (73,653 rows against 66,107 chains, one per original order) on this extract.

## For a person

Does "number of orders" count rows (fulfilment orders, backorders included) or customer purchase orders?
