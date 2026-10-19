# XREV 2026-10-19 — round-2 relation dossiers on stock movements, roles and candidates — astra

```yaml
object:        nine relation folders under analysis/wwi/across/relations/ and across/candidates.md, as first generated on 2026-10-19 (uncommitted; moved to scratch/_superseded/across_r2_v1).
reviewer:      gpt-6-astra, via the Codex MCP server on the author's desktop, reasoning effort medium, workspace-write
               sandbox, answer written to the ignored scratch/ folder; the call timed out at the device bridge and the
               answer was retrieved from the file. Run in parallel with a pass by sol on other relations.
assignment:    against ADR-0017 and ADR-0019 (the relation minimum 01, 02, 06, 07, 27 with hard effort, no guessing),
               analysis/README.md section 5 and ADR-0020: up to three false or overstated claims; up to three
               confidences breaking section 5; the most important missed cross-table warning; any design advice.
               450 words; praise, summary and general assessment forbidden.
second reader: assignment set by Claude Opus 5.5, which wrote the readings, the generator and the evidence script the
               same evening.
verdict:       FAILS [the invoice-header route gives 25 pairs where the composite relation gives five, yet 27 declared the tests inapplicable]
```

Astra's answer, verbatim:

1. Paths below are relative to `analysis/wwi/across/relations/`; hashes identify each dossier's `evidence/<hash>.json`.

   `Sales.Customers.AlternateContactPersonID__Application.People.PersonID/02_meaning.md#C4`: "Sales.Customers has one pattern of empty columns". Evidence `0cbc424f80836d13` reports `empty_patterns_distinct=2`: 261 rows have the quoted pattern; 402 instead have CreditLimit, DeliveryRun and RunPosition empty. The co-absence of BuyingGroupID and AlternateContactPersonID is supported; the single-pattern claim is false.

   `Sales.SpecialDeals.CustomerID__Sales.Customers.CustomerID/27_peculiarities.md#C1`: "joined in the extract, a row of Sales.SpecialDeals gets the attributes of Sales.Customers". Evidence `8f7c4468a72cc585` reports `child_filled=0` and `inner_join_rows=0`. Neither deal obtains customer attributes through this equality join; a left join supplies nulls. System versioning does not establish the asserted match.

   `Warehouse.StockItemTransactions.InvoiceID.StockItemID__Sales.InvoiceLines.InvoiceID.StockItemID/27_peculiarities.md#C1`: "None of the mechanical tests (fan-out, roles, chasm, versions, routes) applies." Evidence `8c8dd5b8784e3b82` contains only composite-key inclusion and multiplicity measurements. Its embedded code performs no route, role or temporal tests. Absence of testing is not evidence of inapplicability.

2. `Purchasing.PurchaseOrders.ContactPersonID__Application.People.PersonID/02_meaning.md#C3`, medium: "WWI's own person responsible for the order". Evidence `54ca269b48e46fd9` establishes employee/salesperson flags and disagreement with supplier-contact routes, not responsibility. The declared description merely says primary contact. Responsibility remains unknown; source workflow evidence would settle it.

   `Warehouse.StockItemTransactions.PurchaseOrderID.StockItemID__Purchasing.PurchaseOrderLines.PurchaseOrderID.StockItemID/02_meaning.md#C2`, low: "either ... no line was received in parts ... or ... update the same movement". Evidence `4010b6fe4a0c8c94` establishes one matching movement per referenced line, not this exhaustive choice. A first partial receipt awaiting another movement also fits. The minimum item needs an unknown claim about receipt lifecycle, settled by workflow or change-history evidence.

3. The composite invoice relation's 27 misses the alternative route through invoice headers. `../candidates.md` records up to five invoice lines per invoice (`cf205a1bb25c374b`) and five stock movements (`7949e6bda8b28601`); `8c8dd5b8784e3b82` establishes one movement per line on the composite key. Joining through InvoiceID alone pairs every movement with every line: a five-line invoice yields 25 pairs instead of five. The warning must distinguish header association from line identity.

4. No clear ADR-0020 violation found. Warnings about multiplication, role selection and unlike units describe consequences of the existing data, without choosing a future design.

VERDICT: FAILS + the invoice-header route produces 25 pairs where the composite relation produces five, yet its 27 declares the tests inapplicable.

## Dispositions

All findings accepted and fixed the same evening (step S08-079):

1. **"One pattern of empty columns".** Reworded: one of the two patterns in Sales.Customers.
2. **System-versioning warning on a relation never used.** The warning is now written only when some row refers, and
   says it applies to a row that names a parent.
3. **"None of the tests applies" on the composite relations.** The composite relations now carry the header-join
   count: on InvoiceID alone, stock movements and invoice lines give 847,672 rows instead of 228,432; on
   PurchaseOrderID alone, 43,007 instead of 8,367. Their 27 says which tests are not run on undeclared relations. The
   generic "none applies" text now names the tests it ran.
4. **"Responsible for the order".** Replaced by the observed fact (an employee and salesperson on every order, never
   the supplier's contact) and an unknown claim on the role.
5. **Receipt lifecycle as a closed choice.** Replaced by an unknown claim listing the possibilities and what would
   settle it.

Section 4: none found.
