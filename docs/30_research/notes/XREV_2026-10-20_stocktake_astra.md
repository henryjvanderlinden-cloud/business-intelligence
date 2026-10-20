# XREV 2026-10-20 — stocktake, terms and entities — astra

```yaml
object:        analysis/wwi/across/processes/stocktake/ and every file under across/terms/ and across/entities/, as first generated on 2026-10-20 (uncommitted).
reviewer:      gpt-6-astra, via the Codex MCP server on the author's desktop, reasoning effort medium, workspace-write
               sandbox, answer written to the ignored scratch/ folder; the call timed out at the device bridge and the
               answer was retrieved from the file. Run in parallel with a pass by sol on point-in-time and processes.
assignment:    against ADR-0017, ADR-0019, analysis/README.md sections 4 and 5 and ADR-0020: up to three false or
               overstated claims; up to two places where code or a link says something else than the claim; up to two
               confidences breaking section 5; any design advice. 450 words; praise, summary and general assessment
               forbidden.
second reader: assignment set by Claude Opus 5.5, which wrote the scripts, readings and links the same morning.
verdict:       FAILS [four zero-quantity adjustments contradict 'only differences leave a movement'; several readings exceed their links]
```

Astra's answer, verbatim:

1. False or overstated claims (paths below are relative to `analysis/wwi/`).

   `across/processes/stocktake/24_processes.md#C6`: "only differences leave a movement." Its own C2 and evidence `bd26210b8b502c9a` record four zero-quantity adjustments. A recorded stocktake movement need not represent a nonzero difference.

   `across/terms/finalized/25_terms.md#C2`: "before they are invoiced or paid." The cited procure-to-pay C1 counts current flags and reached steps; it establishes no time at which a finalization flag was set. C2 there reports receipt and invoice on the same date. Neither establishes the asserted ordering or that finalization means completed receipt.

   `across/entities/person/26_entities.md#C2`: "Staff roles name employees on every row." Its picker reference counts only 63,020 populated references; that reference's C3 explicitly records 10,633 orders without a picker. "Every populated reference" would match the evidence.

2. Measurement or reference mismatches.

   `across/processes/stocktake/24_processes.md#C5`: "Only a few items are adjusted at each stocktake (1 to 5)." `processes.py::stocktake()` counts transaction rows per date, not distinct items per date. Its distinct-item count is across all dates. Repeated adjustments of one item would make the asserted per-date item count wrong.

   `across/entities/stock-item/26_entities.md#C3`: "lines and movements ... versions current at their dates differ only in CustomFields and Tags." The cited `across/relations/Sales.InvoiceLines.StockItemID__Warehouse.StockItems.StockItemID/03_temporal.md#C3` and C4 concern invoice lines evaluated at InvoiceDate. They establish nothing about order lines or movements at their respective dates.

3. Confidence or unstated uncertainty.

   `across/terms/transaction/25_terms.md#C1`, high: "draw their keys from one numbering." `tables/Sales/CustomerTransactions/06_keys.md#C3` establishes a disjoint, gapless partition of observed identifiers, not a shared allocation mechanism. The mechanism remains an inference; high confidence belongs to the observed partition.

   `across/entities/customer/26_entities.md#C2`: "scope of a special deal ... empty meaning all." Its sole reference, `across/terms/customer/25_terms.md`, says nothing about special deals or null semantics. Without a declaration or behavioural evidence, the meaning of an empty CustomerID is unestablished, not medium-confidence knowledge supplied by that reference.

4. `across/terms/customer/25_terms.md`, "For a person": "whether the two roles are to be grouped, if a relation is found and it adds value." This is a future design decision retained in the analysis, although explicitly parked rather than currently requested. ADR-0020 excludes such questions from these dossiers.

VERDICT: FAILS — four zero-quantity adjustments contradict "only differences leave a movement"; several readings exceed their cited claims.

## Dispositions

All findings accepted and fixed the same morning (step S08-092):

1. **"Only differences leave a movement".** Removed; the unknown claim now also asks why some counts leave a movement
   of zero while others leave none.
2. **"Finalized ... before they are invoiced or paid".** Replaced by the counts that show it does not mean paid on
   purchase orders (2,074 finalized orders, 4 of their invoices unpaid); what sets it is left unknown.
3. **"Employees on every row".** Now "on every row where they are filled".
4. **Items per stocktake counted as rows.** processes.py now counts distinct items per date (1 to 5; 2014-10-31 has 4
   adjustments of 3 items), and the claim cites them.
5. **Stock-item versions from invoice lines only.** The claim now names the four relations whose 03 files show the
   same (order lines, purchase-order lines and stock movements as well as invoice lines).
6. **"One numbering" at high.** Split: the observed partition (high) and the shared numbering as its reading (medium).
7. **Special-deal scope without a link.** Now cites the declared description of SpecialDeals.CustomerID (empty means
   all customers).
8. **The parked question in the customer term.** Removed from the analysis file; it stays only in the register
   (ARC-OP-36), as ADR-0020 asks.
