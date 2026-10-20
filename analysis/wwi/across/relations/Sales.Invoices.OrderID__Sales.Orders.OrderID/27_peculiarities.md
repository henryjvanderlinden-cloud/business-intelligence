---
id: wwi:fk:FK_Sales_Invoices_OrderID_Sales_Orders
subject: wwi/across/relations/Sales.Invoices.OrderID__Sales.Orders.OrderID
item: 27
topic: peculiarities
tier: minimum
summary: Warnings: one-to-one not enforced.
confidence: medium
claims: 1
written_by: claude-opus-5-5
written_at: 2026-10-20T08:31:00Z
step: S08-095
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: f8298521c727f76a5df7d60cceab9113551c38c8ab8ff1e0fdb8c864540f7bdf
last_checked_at: 2026-10-20T08:31:00Z
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

- C1 | type=observed | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=4fe6c2f192a15dd6 | recheck=a second row refers to the same parent | text: One row of Sales.Invoices per row of Sales.Orders holds only in this extract: nothing declares OrderID unique, so several referring rows per parent are allowed, and a join that counts on one per parent rests on the extract.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
