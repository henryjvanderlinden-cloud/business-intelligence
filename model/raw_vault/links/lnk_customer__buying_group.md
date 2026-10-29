---
id: nsdn:rv:link:customer__buying_group
kind: link
name: lnk_customer__buying_group
status: accepted
ruled_in: ADR-0031, ADR-0030
defined_in: docs/10_architecture/148_wwi-relationships.md#3 link 6
written_by: claude-opus-5-5
written_at: 2026-10-29T11:34:00Z
step: S11-010
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
label: customer in buying group
from: hub_customer
to: hub_buying_group
driving: hub_customer
optional: yes
effectivity: load
subject_area: parties
---

## Columns

- Sales.Customers.CustomerID | end=from | effectivity_start=load
- Sales.Customers.BuyingGroupID | end=to

## Relations

- analysis/wwi/across/relations/Sales.Customers.BuyingGroupID__Sales.BuyingGroups.BuyingGroupID

## Evidence

- analysis/wwi/across/relations/Sales.Customers.BuyingGroupID__Sales.BuyingGroups.BuyingGroupID/07_population.md#C2
