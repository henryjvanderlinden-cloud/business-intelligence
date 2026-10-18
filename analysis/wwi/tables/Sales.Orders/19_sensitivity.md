---
item: 19
topic: sensitivity
subject: wwi/Sales.Orders
tier: minimum
status: proposed
confidence: medium
finding: No names or contact details in the table, but four columns identify people in Application.People, which holds their names, e-mail addresses and phone numbers; three free-text columns could hold personal data and are empty today.
claims: [declared, observed]
as_of: wwi 2016-06-01 manifest sha256 35b71b2e3ff4bb9e
evidence: [E001, E003, E005, E008]
analysed_by: claude-opus-5-5
analysed_at: 2026-10-18
ruled_by: none
---

## Finding

1. **Person references.** `SalespersonPersonID` (10 distinct, all flagged salespersons), `PickedByPersonID`
   (19 distinct, all employees), `ContactPersonID` (663 customer contacts, none employees) and `LastEditedBy` all resolve to
   `Application.People` (E003, E008). All 663 contacts have an e-mail address and a phone number there (E008).
2. **Employee activity.** Salesperson and picker, with dates, record who did which work when.
3. **Free text.** `Comments` and `DeliveryInstructions` are described as sent to the customer and
   `InternalComments` as internal (E001); all three are empty in every row (E005).
4. **Customers may be people.** Some customer names read as a person's name rather than a company's — an impression
   from reading names, not measured (low confidence). If so, `CustomerID` identifies a natural person too.
5. **Commercial.** `CustomerPurchaseOrderNumber` is the customer's own reference.

## Reasoning

Under the GDPR an identifier that can be linked to a named person is personal data, so a table holding only person
IDs is personal data while `Application.People` is reachable — this is the model's reading, not legal advice, and
is unsourced here. Employee activity data is commonly treated with extra care in an employment setting; in the
Netherlands a works council may have a say in its use. The WWI data is synthetic, so no real person is affected; the
classification is practised as if it were real.

## Uncertainties

1. **Legal basis and retention: unknown.** A person must rule.
2. **Free text: empty today, not guaranteed empty.** A check that alerts when these columns fill would settle it per
   load.

## For a person

1. Is `Sales.Orders` classified as personal data, and are salesperson and picker treated as employee-monitoring data?
2. May the person IDs be loaded as they are, or pseudonymised before the warehouse?
