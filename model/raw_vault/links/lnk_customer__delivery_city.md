---
id: nsdn:rv:link:customer__delivery_city
kind: link
name: lnk_customer__delivery_city
status: accepted
ruled_in: ADR-0031, ADR-0030
defined_in: docs/10_architecture/148_wwi-relationships.md#3 link 3
written_by: claude-opus-5-5
written_at: 2026-10-29T11:34:00Z
step: S11-010
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
label: customer delivery city
from: hub_customer
to: hub_city
driving: hub_customer
optional: no
effectivity: load
subject_area: parties
---

## Columns

- Sales.Customers.CustomerID | end=from | effectivity_start=load
- Sales.Customers.DeliveryCityID | end=to

## Relations

- analysis/wwi/across/relations/Sales.Customers.DeliveryCityID__Application.Cities.CityID

## Evidence

- analysis/wwi/across/relations/Sales.Customers.DeliveryCityID__Application.Cities.CityID/07_population.md#C2
