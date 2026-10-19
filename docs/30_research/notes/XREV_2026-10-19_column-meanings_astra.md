# XREV 2026-10-19 — column meanings of SupplierTransactions, People, VehicleTemperatures and StockItems — astra

```yaml
object:        the item-02 files under analysis/wwi/tables/Purchasing/SupplierTransactions/, Application/People/, Warehouse/VehicleTemperatures/ and Warehouse/StockItems/columns/, as committed on 2026-10-19 (0d1c89e).
reviewer:      gpt-6-astra, via the Codex MCP server on the author's desktop, reasoning effort medium, workspace-write
               sandbox, answer written to the ignored scratch/ folder; the call timed out at the device bridge and the
               answer was retrieved from the file. Run in parallel with a pass by sol on other tables.
assignment:    against ADR-0017 (confidence supported by the cited evidence; uncertainties stated), analysis/README.md
               section 5 (counts high, generalisations medium, readings from names low) and ADR-0020: up to three false or
               overstated claims; up to three confidences breaking section 5; up to two misread columns or misapplied
               Microsoft texts; any design advice. 400 words; praise, summary and general assessment forbidden.
second reader: assignment set by Claude Opus 5.5, which wrote the readings and the generator of the mechanical claims the
               same day.
verdict:       FAILS [LogonName C4's shared-value claim contradicts the cited profile's functional dependency and counts]
```

Astra's answer, verbatim:

1. `analysis/wwi/tables/Application/People/columns/LogonName/02_meaning.md#C4`: "one value is shared by everyone else" is contradicted by `419f7b85d80b0191`. Among 956 people with IsPermittedToLogon=0, CustomFields is empty for 954 and populated for two. The same evidence reports `LogonName -> CustomFields`. Therefore those 956 people cannot all share one LogonName; the 156-versus-155 cardinalities do not establish the claimed partition.

   `analysis/wwi/tables/Warehouse/StockItems/columns/IsChillerStock/02_meaning.md#C4` quotes Microsoft: "WWI recently started to sell various food items, like chilly chocolates." Cited `0f9e0d3eb9dd8048` contains no such quotation. Its chilled excerpts describe temperature monitoring and location sensors, without mentioning chocolates or when food sales began. The quotation is unsupported by the recorded evidence.

2. `analysis/wwi/tables/Purchasing/SupplierTransactions/columns/PaymentMethodID/02_meaning.md#C5` assigns medium confidence to "the method by which it is or will be paid". `be40a492ac908708` establishes code 4 on every row, not whether an invoice records an intended method, an actual settlement method, or a default. That semantic choice remains uncertain; the proposed reading merits low confidence.

   `analysis/wwi/tables/Warehouse/StockItems/columns/ValidFrom/02_meaning.md#C3` assigns high confidence to "the clock time of the change" and its usual agreement with simulated time. `fbbc435f3d190ff0` declares AS_ROW_START; `7f977b924a38ef2c` profiles stored timestamps. Neither establishes how historical simulation timestamps were produced or compares them with execution time. The period role is supported; the clock interpretation is not established at high confidence.

3. `analysis/wwi/tables/Warehouse/VehicleTemperatures/columns/FullSensorData/02_meaning.md` summarizes the payload as containing "the vehicle's position, registration, sensor and time". C4's Microsoft location-ingestion passage does not identify this column or those fields. `54d0a8a7a090f855` supplies only truncated Feature/geometry prefixes and zero successful parses. This supports a tentative GeoJSON-like reading, not the asserted complete payload meaning; registration, sensor and time remain unestablished by the cited evidence.

4. No design advice or future decision found in the assigned files.

VERDICT: FAILS + LogonName#C4's shared-value claim contradicts the cited profile's functional dependency and population counts.

## Dispositions

All findings accepted and fixed on 2026-10-19 (step S08-072):

1. **LogonName.** Astra is right. A new evidence (logon_names, counts only) shows NO LOGON shared by 954 people, none
   permitted to log on or an employee; 153 values held by one person each, among them 2 employees not permitted to log
   on; and 2 values shared by two people each, all four permitted to log on. The claim states these counts; why two
   logon names are shared is recorded as unknown. Application.People 19 carried the same error and was corrected.
2. **IsChillerStock quotation.** The quotation was not in the recorded evidence: it was written from memory of the page.
   Replaced by a quotation the evidence holds. A check of every quotation in a Microsoft claim against the evidence's
   excerpts found two more that were cut short without marking (ColdRoomSensorNumber, FullSensorData); both now quote
   in full.
3. **PaymentMethodID on invoices.** Lowered to low, and restated as two possible readings, neither established.
4. **ValidFrom "clock time".** As in sol's note: the declared period start stays high, the comparison with simulated
   time is per table from the new evidence (StockItems: every ValidFrom on or before the extract's date).
5. **FullSensorData.** The summary claimed fields the evidence does not show. It now says what the profile shows (the
   text begins as GeoJSON with a Point geometry and parses in no row), and which fields it holds is unknown.

Section 4: none found.
