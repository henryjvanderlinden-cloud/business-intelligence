---
id: nsdn:rv:link:special_deal__customer
kind: link
name: lnk_special_deal__customer
status: accepted
ruled_in: ADR-0031, ADR-0030
defined_in: docs/10_architecture/148_wwi-relationships.md#3 link 16
written_by: claude-opus-5-5
written_at: 2026-10-29T11:20:00Z
step: S11-004
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
label: deal for customer
from: hub_special_deal
to: hub_customer
driving: hub_special_deal
optional: yes
effectivity: load
effectivity_start: load
subject_area: products and deals
optional_note: empty: all customers
---

## Columns

- Sales.SpecialDeals.CustomerID | names=hub_customer

## Relations

- analysis/wwi/across/relations/Sales.SpecialDeals.CustomerID__Sales.Customers.CustomerID

## Evidence

- analysis/wwi/across/relations/Sales.SpecialDeals.CustomerID__Sales.Customers.CustomerID/02_meaning.md#C2
- analysis/wwi/across/relations/Sales.SpecialDeals.CustomerID__Sales.Customers.CustomerID/07_population.md#C2
