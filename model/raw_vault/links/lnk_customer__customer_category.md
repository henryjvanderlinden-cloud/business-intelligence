---
id: nsdn:rv:link:customer__customer_category
kind: link
name: lnk_customer__customer_category
status: accepted
ruled_in: ADR-0031, ADR-0030
defined_in: docs/10_architecture/148_wwi-relationships.md#3 link 7
written_by: claude-opus-5-5
written_at: 2026-10-29T11:20:00Z
step: S11-004
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
label: customer in category
from: hub_customer
to: hub_customer_category
driving: hub_customer
optional: no
effectivity: load
effectivity_start: load
subject_area: parties
---

## Columns

- Sales.Customers.CustomerCategoryID | names=hub_customer_category

## Relations

- analysis/wwi/across/relations/Sales.Customers.CustomerCategoryID__Sales.CustomerCategories.CustomerCategoryID

## Evidence

- analysis/wwi/across/relations/Sales.Customers.CustomerCategoryID__Sales.CustomerCategories.CustomerCategoryID/07_population.md#C2
