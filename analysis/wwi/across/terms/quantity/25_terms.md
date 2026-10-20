---
id: wwi:term:quantity
subject: wwi/across/terms/quantity
item: 25
topic: terms
tier: best-effort
summary: Quantities count packages of the line's package type: unit packages on sales lines, outer packages on purchase lines.
confidence: medium
claims: 1
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

- C1 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=none | recheck=a linked claim changes | text: Sales order and invoice lines count the item's unit package; purchase-order lines count its outer package (across/relations/Sales.InvoiceLines.PackageTypeID__Warehouse.PackageTypes.PackageTypeID/02_meaning.md#C2; across/relations/Purchasing.PurchaseOrderLines.PackageTypeID__Warehouse.PackageTypes.PackageTypeID/02_meaning.md#C2, 27_peculiarities.md#C5).

## Reasoning

Each claim links the files that own the facts it reads.

## Uncertainties

None.

## For a person

None.
