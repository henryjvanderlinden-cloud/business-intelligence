# XREV 2026-10-19 — column meanings of Sales.Invoices, Customers and Orders — sol

```yaml
object:        the item-02 files under analysis/wwi/tables/Sales/{Invoices,Customers,Orders}/columns/, as committed on 2026-10-19 (0d1c89e).
reviewer:      gpt-5.6-sol, via the Codex MCP server on the author's desktop, reasoning effort medium, workspace-write
               sandbox, answer written to the ignored scratch/ folder; the call timed out at the device bridge and the
               answer was retrieved from the file. Run in parallel with a pass by astra on other tables.
assignment:    against ADR-0017 (confidence supported by the cited evidence; uncertainties stated), analysis/README.md
               section 5 (counts high, generalisations medium, readings from names low) and ADR-0020: up to three false or
               overstated claims; up to three confidences breaking section 5; up to two misread columns or misapplied
               Microsoft texts; any design advice. 400 words; praise, summary and general assessment forbidden.
second reader: assignment set by Claude Opus 5.5, which wrote the readings and the generator of the mechanical claims the
               same day.
verdict:       FAILS [LastEditedBy assigns roles and an initial-load meaning its cited evidence cannot establish]
```

Sol's answer, verbatim:

1. False or overstated claims against cited evidence

- `analysis/wwi/tables/Sales/Invoices/columns/DeliveryInstructions/02_meaning.md#C4`: “the first row holds an address line: the description and the content disagree.” Evidence `b7b43b18cf6be97a` records only 663 distinct values and lexicographic minimum/maximum strings; its code neither retains nor reports the first row. The claimed inspection and categorical disagreement are not evidenced.
- `analysis/wwi/tables/Sales/Orders/columns/LastEditedBy/02_meaning.md#C4`: “a staff member … or person 1 (Data Conversion Only), the technical user of the initial load.” Evidence `f61ebb431b7b9012` supplies the type/FK and `af410313550bceb2` only the distribution 1–20. Neither identifies People rows, staff status, person 1’s name, technical role, or an initial load. The same unsupported template occurs for Customers and Invoices.
- `analysis/wwi/tables/Sales/Customers/columns/ValidFrom/02_meaning.md#C3`: “WWI usually but not always matches simulated time (Application.Countries has a version stamped 2022-10-07).” The cited Customers catalogue/profile evidence contains no Application.Countries observation and does not compare system time with simulated time.

2. Confidence or uncertainty failures

- `analysis/wwi/tables/Sales/Orders/columns/LastEditedWhen/02_meaning.md#C3` is `medium`, but “when the row was last changed” is inferred from the name, type, and range; the cited evidence declares no meaning. Section 5 makes this `low`, or `unknown` pending a description/mechanism. The same defect occurs in Invoices.
- `analysis/wwi/tables/Sales/Customers/columns/BillToCustomerID/02_meaning.md#C5` generalises a functional dependency from one extract. `medium` is possible only if the claim says “in this extract” and states that no constraint/mechanism establishes the rule; it does neither.
- `analysis/wwi/tables/Sales/Customers/columns/ValidFrom/02_meaning.md#C3` cannot be `high`: the period-start declaration supports SQL Server semantics, but the simulated-time qualification is uncited and unobserved here.

3. Misread or misapplied columns

- `analysis/wwi/tables/Sales/Customers/columns/CustomerName/02_meaning.md#C4`: Microsoft describes WWI’s customer population, not this column or which rows represent individuals.
- `analysis/wwi/tables/Sales/Orders/columns/IsUndersupplyBackordered/02_meaning.md#C4`: Microsoft describes a customer workflow/preference; it does not document this bit or establish what `1` means on every order.

4. None found.

VERDICT: FAILS — `LastEditedBy` assigns roles and an initial-load meaning that its cited evidence cannot establish.

## Dispositions

All findings accepted and fixed on 2026-10-19 (step S08-072), in every table, not only the three reviewed:

1. **DeliveryInstructions "first row".** The profile keeps only the lowest and highest value, both address lines; the
   claim now says exactly that, the reading that the column holds addresses is low, and the uncertainty names what was
   not seen. The Invoices sensitivity dossier (19) had the same overclaim and was split the same way.
2. **The LastEditedBy template.** A new evidence per table (`evidence_shared.py columns`, editors_and_system_time) counts
   the rows by editor kind against Application.People and records person 1's FullName. Every LastEditedBy file now
   carries that count as an observation; the reading "the person who last changed the row" is low, from the name and
   the foreign key; "technical user of the initial load" is gone from the template. Application.People 07 says the same.
3. **ValidFrom and Application.Countries.** The template no longer cites another table: the period start is declared
   (catalogue, high), and each table's own evidence says whether any ValidFrom lies after the extract's simulated date.
   Only Application.Countries has one (2022-10-07), and only its file now says so.
4. **LastEditedWhen at medium.** Lowered to low: a reading from the name.
5. **BillToCustomerID.** Now says "in this extract" and that no constraint enforces it.
6. **ValidFrom at high.** See 3: the high claim is now only the declared period start.
7. **CustomerName and IsUndersupplyBackordered.** Every claim citing Microsoft's description is now low and opens with
   "Context, not a description of this column", in all 14 column files that cite it (BackorderOrderID's C3 among them).

Section 4: none found.
