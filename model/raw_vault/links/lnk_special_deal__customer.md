---
id: nsdn:rv:link:special_deal__customer
kind: link
name: lnk_special_deal__customer
status: accepted
ruled_in: ADR-0031, ADR-0030
defined_in: docs/10_architecture/148_wwi-relationships.md#3 link 16
written_by: claude-opus-5-5
written_at: 2026-10-29T11:25:00Z
step: S11-008
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
label: deal for customer
from: hub_special_deal
to: hub_customer
driving: hub_special_deal
optional: yes
effectivity: load
subject_area: products and deals
optional_note: empty: all customers
---

## Columns

- Sales.SpecialDeals.SpecialDealID | end=from | effectivity_start=load
- Sales.SpecialDeals.CustomerID | end=to

## Relations

- analysis/wwi/across/relations/Sales.SpecialDeals.CustomerID__Sales.Customers.CustomerID

## Evidence

- analysis/wwi/across/relations/Sales.SpecialDeals.CustomerID__Sales.Customers.CustomerID/02_meaning.md#C2
- analysis/wwi/across/relations/Sales.SpecialDeals.CustomerID__Sales.Customers.CustomerID/07_population.md#C2
