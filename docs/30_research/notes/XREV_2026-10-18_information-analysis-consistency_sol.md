# XREV 2026-10-18 — information-analysis inventory, consistency and WWI facts — sol

```yaml
object:        docs/10_architecture/129_information-analysis.md, items 1 to 27, against 127 and 128, at commit 5ee40de.
reviewer:      gpt-5.6-sol, via the Codex MCP server on the author's desktop, reasoning effort medium,
               workspace-write sandbox, answer written to the ignored scratch/ folder. The call timed out at the
               device bridge (60 s); the answer was retrieved from the file. Thread id not returned. Run in parallel
               with its other half; an earlier single pass at high effort (S08-033) never wrote an answer.
assignment:    two questions: contradictions with 127 or 128, quoting both; and five build-critical WWI claims checked cheaply against catalogue and extract. 400 words; praise, summary and general assessment forbidden.
second reader: assignment set by Claude Opus 5.5, which drafted items 5 to 27 of the object. Dispositions owed to
               the author.
verdict:       FAILS [a join finding cannot satisfy both 129's dataset/field-card-only output and 128's required relationship assertion/view]
```

Sol's answer, verbatim:

1. 129 contradicts 128 on where item 4 is recorded. 129 says: “The phase would produce no separate report. Its output would be the `dataset` and `field` cards.” 128 says: “Join knowledge is about a *pair* of objects, not about one, so it is recorded as a **relationship assertion** … shown to people and agents as a relationship view.” A relationship finding therefore cannot be recorded only on the two object-card types named by 129. I found no contradiction with 127.

2. Five build-dependent WWI claims:

   a. **Holds:** `Sales.Orders` carries `OrderDate`, `ExpectedDeliveryDate`, `PickingCompletedWhen`, and `LastEditedWhen`. The CSV header has all four; the existing catalogue evidence types the first two as `date` and the latter two as `datetime2`.

   b. **Holds:** 17 of 48 tables are `_Archive` history tables rather than separate entities. `manifest.json` contains 48 entries, exactly 17 marked `HISTORY_TABLE`, all named `_Archive`.

   c. **Holds:** `Sales.Orders.BackorderOrderID` self-references `Sales.Orders`. The catalogue evidence records an enabled, trusted foreign key from that column to `Sales.Orders.OrderID`.

   d. **Holds:** `Application.People` starts with technical row 1, `Data Conversion Only`. Its first row has that name, `NO LOGON`, and all four person-role flags false; it is also its own `LastEditedBy` value.

   e. **Not checkable cheaply:** `Sales.Invoices.TotalDryItems` and `TotalChillerItems` equal dry/chiller line counts on all 70,566 invoices and match quantity sums on only 145. The headers and first rows establish the columns and one example, but the universal counts require scanning the two large invoice files or reading retained aggregate evidence; neither is available from the cheap evidence specified.

VERDICT: FAILS + a join finding cannot satisfy both 129’s dataset/field-card-only output and 128’s required relationship assertion/view.

## Dispositions

Proposed in `ARC-OP-36`.
