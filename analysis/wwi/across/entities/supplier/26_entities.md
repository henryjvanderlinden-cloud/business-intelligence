---
id: wwi:entity:supplier
subject: wwi/across/entities/supplier
item: 26
topic: entities
tier: best-effort
summary: Purchasing.Suppliers, system-versioned, identified by SupplierID; named by purchase orders, the supplier ledger, stock receipts and as an item's usual supplier.
confidence: medium
claims: 2
written_by: claude-opus-5-5
written_at: 2026-10-20T05:51:00Z
step: S08-092
method: readings by claude-opus-5-5 linking the claims that own each fact; written by prototypes/information_analysis/write_glossary.py (blob ffcc3813a793cc9facce4b98cc396d0f16cffa08)
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: none
last_checked_at: 2026-10-20T05:51:00Z
last_checked_by: claude-opus-5-5
last_checked_against: 2016-06-01
reviewed_by: none
reviewed_at: none
ruled_by: none
ruled_at: none
supersedes: none
superseded_by: none
recheck_when: a linked claim changes
---

## Claims

- C1 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=none | recheck=a linked claim changes | text: One table of 13 suppliers, versioned in Purchasing.Suppliers_Archive; SupplierID is its key (tables/Purchasing/Suppliers/06_keys.md).
- C2 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=none | recheck=a linked claim changes | text: A stock receipt's supplier is both its purchase order's supplier and the item's usual supplier on every receipt (across/relations/Warehouse.StockItemTransactions.SupplierID__Purchasing.Suppliers.SupplierID/02_meaning.md#C2; across/relations/Warehouse.StockItems.SupplierID__Purchasing.Suppliers.SupplierID/02_meaning.md#C2).

## Reasoning

Each claim links the files that own the facts it reads.

## Uncertainties

None.

## For a person

None.
