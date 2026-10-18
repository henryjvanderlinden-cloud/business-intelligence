---
id: wwi:object:1154103152
subject: wwi/tables/Sales/Orders
item: 06
topic: keys
tier: minimum
summary: OrderID is the declared primary key, unique, gapless and the only key; meaningless and not a time proxy; CustomerPurchaseOrderNumber is not a key.
confidence: unknown
claims: 7
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
recheck_when: a schema change, a deletion, or a duplicate OrderID
---

## Claims

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=b8b837693651efad,b6da684f0b7581f7 | recheck=the primary key changes | text: OrderID (int) is the primary key PK_Sales_Orders, described as "Numeric ID used for reference to an order within the database"; no other unique constraint is declared.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=77ee039bf95c3ee8 | recheck=OrderID stops being unique | text: OrderID is unique over 73,653 rows and runs from 1 to 73,653 without a gap.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=77ee039bf95c3ee8 | recheck=the inversion count falls to zero | text: OrderID mostly rises with OrderDate but not strictly (215 inversions), so it must not be used to order by time.
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=77ee039bf95c3ee8,c6e5d1bc0af05898 | recheck=CustomerPurchaseOrderNumber becomes unique | text: CustomerPurchaseOrderNumber is not a key: 9,984 distinct values over 73,653 rows, shared by an order and its backorders.
- C5 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=597ef697da37cd0e | recheck=a foreign key changes | text: Six foreign keys, all enabled and trusted: CustomerID, SalespersonPersonID, PickedByPersonID, ContactPersonID, LastEditedBy and the self-reference BackorderOrderID (its direction: columns/BackorderOrderID/02_meaning.md#C2).
- C6 | type=observed | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=77ee039bf95c3ee8 | recheck=a deletion or a re-used OrderID is seen | text: Key stability: no number was lost to a deletion; whether a deleted number could be reused is not observable yet.
- C7 | type=observed | status=proposed | confidence=unknown | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=none | recheck=documents sent to customers are found | text: Whether OrderID is known outside the database, on documents sent to customers, is not established.

## Reasoning

Key and uniqueness are declared and observed and agree. For a Data Vault hub the business key would be OrderID: it is the source's own identifier and there is no better candidate inside the table.

## Uncertainties

C6 rests on the absence of gaps, which reuse would hide; settled by watching deletions and inserts over many days. C7 is open.

## For a person

None for the minimum.
