---
id: nsdn:rv:link:special_deal__customer_category
kind: link
name: lnk_special_deal__customer_category
status: accepted
ruled_in: ADR-0031, ADR-0030
defined_in: docs/10_architecture/148_wwi-relationships.md#3 link 18
written_by: claude-opus-5-5
written_at: 2026-10-29T11:34:00Z
step: S11-010
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
label: deal for customer category
from: hub_special_deal
to: hub_customer_category
driving: hub_special_deal
optional: yes
effectivity: load
subject_area: products and deals
---

## Columns

- Sales.SpecialDeals.SpecialDealID | end=from | effectivity_start=load
- Sales.SpecialDeals.CustomerCategoryID | end=to

## Relations

- analysis/wwi/across/relations/Sales.SpecialDeals.CustomerCategoryID__Sales.CustomerCategories.CustomerCategoryID

## Evidence

- analysis/wwi/across/relations/Sales.SpecialDeals.CustomerCategoryID__Sales.CustomerCategories.CustomerCategoryID/02_meaning.md#C2
- analysis/wwi/across/relations/Sales.SpecialDeals.CustomerCategoryID__Sales.CustomerCategories.CustomerCategoryID/07_population.md#C2
