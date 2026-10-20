---
id: wwi:fk:FK_Sales_Invoices_PackedByPersonID_Application_People
subject: wwi/across/relations/Sales.Invoices.PackedByPersonID__Application.People.PersonID
item: 02
topic: meaning
tier: minimum
summary: Person who packed this shipment (or checked the packing)
confidence: medium
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-20T08:31:00Z
step: S08-095
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 3aa149bb0b9739b54a558409e637e207fdd32b81f8963ff081ad814fe3f44eff
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

- C1 | type=declared | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=ed489c7e2ae07807 | recheck=the description changes | text: The source describes Sales.Invoices.PackedByPersonID as "Person who packed this shipment (or checked the packing)".
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=ed489c7e2ae07807 | recheck=every new extract | text: The people named: 70,566 of 70,566 rows name an employee of WWI (IsEmployee = 1), 39,570 a salesperson, 0 a person who is not an employee.
- C3 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=ed489c7e2ae07807 | recheck=every new extract, or a description changes | text: The staff member who packed the shipment, or checked the packing (declared). It is not the order's picker: they are the same person on 3,219 of 63,020 invoices whose order has a picker.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
