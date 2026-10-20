# XREV 2026-10-20 — position in the schema (item 29), code and measures — sol

```yaml
object:        prototypes/information_analysis/structure.py and its result (evidence 9c767ee159e3e3db, an intermediate run
               after astra's fixes, now in scratch/_superseded/position_v2), against 131 sections 2 to 5 and
               analysis/wwi/_source/29_position.md C1 to C6 and tables/Application/People/29_position.md C1 to C6.
reviewer:      gpt-5.6-sol, via the Codex MCP server on the author's desktop, reasoning effort medium, workspace-write
               sandbox. A first, broader brief (code, counts, class rules and confidences over all 49 files) wrote no
               answer; this narrower brief did. The call timed out at the device bridge and the answer was retrieved
               from the file.
assignment:    places where the code computes something other than 131 says; claims that misstate the evidence. Praise
               and summary forbidden.
second reader: assignment set by Claude Opus 5.5, which wrote structure.py and write_position.py the same evening.
verdict:       FAILS [self-references counted in measures defined for other tables; history tables without the position
               131 says they take]
```

Sol's answer, verbatim:

1. Three mismatches:

   - `measures()` defines `roles = len(ins)` and sums every `ins` row into `rows_referring`, including `c == t`. Section 4 defines both as foreign-key columns/rows in *other* tables. `Application.People` is a concrete counterexample: its full result identifies the self-reference `LastEditedBy`, yet includes it in `roles: 41` and in `rows_referring`. Self-references should remain separately reported, not inflate these two measures.
   - `classify()` tests “every row updated daily” by taking the maximum per-column business-update count and comparing it in both transitions with `rows_of[t]`, the single base-extract count. That is not a test that every row was updated: disjoint rows updated across different columns can cover the whole table while no column’s maximum does; conversely transition 2 can pass against the stale 2016-06-01 row count after its population changes. Use the transition’s updated-row count/row population, after excluding audit-only updates.
   - Section 2 says a history table “take[s] the position of the table whose versions [it keeps].” `history_tables()` records only `history_of`, link counts, rows, behaviour, class, and rule; it copies none of the owner’s position measures. The JSON therefore leaves all 17 history tables without the required inherited position. Its count-only behaviour test can also call an equal-cardinality changed history table `unchanged`.

2. None. C1–C6 in both named Markdown files accurately transcribe the corresponding JSON values. That does not validate how the code produced them.

VERDICT: FAILS + counterexample: Application.People’s self-reference is counted in measures defined for other tables, and every history table lacks the position 131 requires it to inherit.

## Dispositions

All findings accepted and fixed the same evening (step S08-107):

1. **Self-references in roles and rows referring.** Links in, roles and rows referring now count other tables only;
   self-references are reported separately. Application.People with all links: 40 links from 28 other tables, plus its
   own LastEditedBy (was 41); Sales.Customers 6 roles (was 7); Sales.Orders 2 links in (was 3). 131 section 3 and the
   readings of Customers and Orders were corrected.
2. **"Every row updated daily" from a column maximum and the base row count.** `business_updates()` now compares the two
   extracts row by row and counts rows changed in a column other than the key and the audit columns, against the rows
   of the later extract of each transition.
3. **History tables without the inherited position.** Each history table now records its owner's class, position and
   betweenness rank, and its file states them. The label from row counts alone is now "rows added in both transitions"
   or "row count unchanged", which says only what was counted.

Section 2: none found.
