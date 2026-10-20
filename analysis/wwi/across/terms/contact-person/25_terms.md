---
id: wwi:term:contact-person
subject: wwi/across/terms/contact-person
item: 25
topic: terms
tier: best-effort
summary: "Contact person" is the customer's or supplier's person on the sales and master-data side, but a WWI salesperson on purchase orders.
confidence: high
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

- C1 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=none | recheck=a linked claim changes | text: On customers, orders and invoices the contact is a person who is not a WWI employee (across/relations/Sales.Customers.PrimaryContactPersonID__Application.People.PersonID/02_meaning.md#C2, #C3); likewise on suppliers (across/relations/Purchasing.Suppliers.PrimaryContactPersonID__Application.People.PersonID/02_meaning.md#C2).
- C2 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=none | recheck=a linked claim changes | text: On purchase orders the "primary contact" is a WWI employee and salesperson on every order, never the supplier's contact; the role it records is unknown (across/relations/Purchasing.PurchaseOrders.ContactPersonID__Application.People.PersonID/02_meaning.md#C3, #C4).

## Reasoning

Each claim links the files that own the facts it reads.

## Uncertainties

None.

## For a person

None.
