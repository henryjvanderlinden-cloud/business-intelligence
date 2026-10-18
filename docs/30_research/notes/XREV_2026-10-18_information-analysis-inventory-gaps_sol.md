# XREV 2026-10-18 — information-analysis inventory, gaps and minimum — sol

```yaml
object:        docs/10_architecture/129_information-analysis.md, items 1 to 27, as ruled in ADR-0017 and ADR-0018, at commit 5ee40de.
reviewer:      gpt-5.6-sol, via the Codex MCP server on the author's desktop, reasoning effort medium,
               workspace-write sandbox, answer written to the ignored scratch/ folder. The call timed out at the
               device bridge (60 s); the answer was retrieved from the file. Thread id not returned. Run in parallel
               with its other half; an earlier single pass at high effort (S08-033) never wrote an answer.
assignment:    framed by PRC-OP-7 against the standard of what an experienced information analyst would establish before a Data Vault and mart build. Two refutation questions: at most three uncovered things, each with the wrong build it causes; and whether the minimum suffices against wrong grain or wrong joins, with the smallest counterexample. 400 words; data files, praise, summary and general assessment forbidden.
second reader: assignment set by Claude Opus 5.5, which drafted items 5 to 27 of the object. Dispositions owed to
               the author.
verdict:       FAILS [two tables with an ambiguous foreign-key target can pass the minimum and still produce a plausible one-to-one wrong join]
```

Sol's answer, verbatim:

1. Two omissions are identifiable.

   First, the inventory does not require the source's arithmetic policy: decimal precision during intermediate calculations, rounding mode, rounding point (line or document), and treatment of residual pennies. Items 8 and 9 capture additivity, units and formulas, but the same formula evaluated with different rounding can disagree. Recomputing line tax and then summing it when the source rounds tax at invoice level produces wrong tax, gross revenue and margin.

   Second, it does not require the effective visibility of the extraction identity: row-level-security predicates, security-definer views, session or tenant context, and column masking applied to that identity. Item 19 records who may see data and item 23 the access route, but neither establishes what that route silently filters or rewrites. A profile and load run through a tenant-filtered view can therefore report a complete-looking but incomplete population, producing understated totals and false orphan rates.

2. No. The minimum excludes both item 2 (meaning) and item 4 (relationships). The smallest counterexample is two tables. `Sale(SaleID, LocationID, Amount)` has one row per sale. `Location(LocationID, SourceLocationID, Name)` has a primary key on `LocationID` and a unique candidate key on `SourceLocationID`. In the source interface, `Sale.LocationID` denotes `Location.SourceLocationID`; current values happen to overlap both location columns. Every minimum item can be established for both tables, and none of item 27's required tests exposes the ambiguity. A builder can join `Sale.LocationID = Location.LocationID`, obtaining exactly one match per sale with unchanged row counts and totals, while attributing every amount to the wrong location. Item 4's join assertion, informed by item 2's meaning, is needed before that join is safe.

VERDICT: FAILS + two tables with an ambiguous foreign-key target can pass the minimum and still produce a plausible one-to-one wrong join.

## Dispositions

Proposed in `ARC-OP-36`.
