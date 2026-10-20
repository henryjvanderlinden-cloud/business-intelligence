---
id: wwi:entity:person
subject: wwi/across/entities/person
item: 26
topic: entities
tier: best-effort
summary: Application.People holds every person: WWI staff (salespeople, pickers, packers, editors), customer and supplier contacts, and a technical user, told apart by flags.
confidence: high
claims: 3
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

- C1 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=none | recheck=a linked claim changes | text: One table, versioned, with flags IsEmployee, IsSalesperson, IsPermittedToLogon (tables/Application/People/07_population.md#C6); its rows are last edited only by person 1, whose name is Data Conversion Only (#C7).
- C2 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=none | recheck=a linked claim changes | text: Staff roles name an employee on every row where they are filled: salesperson, picker, packer (across/relations/Sales.Invoices.SalespersonPersonID__Application.People.PersonID/02_meaning.md#C2; across/relations/Sales.Orders.PickedByPersonID__Application.People.PersonID/02_meaning.md#C2; across/relations/Sales.Invoices.PackedByPersonID__Application.People.PersonID/02_meaning.md#C2); salespeople also pick and pack.
- C3 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=none | recheck=a linked claim changes | text: Contact roles name people who are not employees, except the purchase-order contact (across/terms/contact-person/25_terms.md).

## Reasoning

Each claim links the files that own the facts it reads.

## Uncertainties

None.

## For a person

None.
