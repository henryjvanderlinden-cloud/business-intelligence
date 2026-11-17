# XREV 2026-11-17 — the build of the first slice (generator 0.4.0, generate_marts.py) — sol

```yaml
object:        prototypes/vault_generator/generate_marts.py as committed in bf0c6c3 (generator 0.4.0), with the generated
               files of pit_invoice_line, brg_invoice_line__sale, csat_invoice_line__sales_amount, dim_customer,
               fct_invoice_line and the analysis, two of their table macros and seven of their tests; note 141 sections
               2 to 5, 9 and 11 as the standard; three raw-vault files the slice reads as context. Bundled as
               scratch/REVIEW_141_build.txt.
reviewer:      gpt-5.6-sol, via the Codex MCP server on the author's desktop, reasoning effort medium, workspace-write
               sandbox, no browsing; confined to the one file; answer written to the ignored scratch/ folder with
               apply_patch.
assignment:    assume the generated code is wrong and show it, as an analytics engineer who has shipped Data Vault
               business vaults and Kimball marts on dbt and DuckDB in production and rejects the build; judged
               against the standard: the SQL implements the four rules of 141 section 3 exactly, at the load date and
               as known on any earlier date; table and macro return exactly the same rows; no line or amount lost,
               duplicated or mis-assigned; each test fails when its defect is present; unsupported patterns refused.
               Up to five findings, generated SQL and tests preferred; naming, layout, prose, the business question
               and the design itself excluded; praise, summary and general assessment forbidden.
second reader: assignment set by Claude Opus 5.5 in session 13; the code was drafted by Claude Fable 5.2 in the same
               session. The dispositions below are Opus's; the changes made in response are unreviewed.
limits:        the bundle left out the raw vault's generated version_unique tests, which fail a build when a satellite
               holds two rows for one source version, and the satellite template, which inserts only versions not yet
               stored. Findings 1 and 3 were judged without them and rest on a state those exclude.
verdict:       FAILS [historical macros leak and multiply restated satellite rows]. Disposition: 1 and 3 rest on a
               premise the raw vault excludes, and are guarded anyway (every pointer join bounded by the knowledge
               date; a test per point-in-time satellite that each pointer names exactly one row); 2 applied (table
               against macro and the lineage test compare with multiplicity, except all); 4 applied (a keys_complete
               test on every point-in-time table, bridge, computed satellite and dimension); 5 applied (the lineage
               test compares every attribute a dimension shows, labels included, derived from the delivered rows).
               Generator 0.4.1. Unreviewed.
```

## sol's answer, verbatim

**A PIT pointer does not identify a unique satellite row, and every downstream satellite join ignores `known_on`, so a late restatement both leaks into an earlier macro and multiplies fact rows.**

> `and %s.source_ts is not distinct from %s.%s__source_ts and %s.source_seq = %s.%s__source_seq`

For `hk_invoice_line='L1'`, let the satellite contain `(load_date=2026-06-01, source_ts=2026-05-10, source_seq=1, ExtendedPrice=120, TaxAmount=20)` and, after a late `2026-05-05` arrival, the required restatement `(load_date=2026-06-02, source_ts=2026-05-10, source_seq=1, ExtendedPrice=120, TaxAmount=20)`.  The `2026-06-01` PIT pointer contains only record source, `2026-05-10`, and `1`; after the second load, `fct_invoice_line__as_known(date '2026-06-01')` joins both raw rows despite the later `load_date`, while its computed-satellite macro also returns both, producing four copies of L1 instead of the one row that existed on June 1.

**The table-versus-macro test uses set difference and therefore declares unequal row multiplicities equal.**

> `(select * from {{ ref('fct_invoice_line') }} except select * from marts.fct_invoice_line__as_known(...))`

With the June 1 table containing one L1 row `(L1, 100, 20, ...)` and the June 1 macro returning four identical copies from the restatement example above, both `EXCEPT` branches return no rows because DuckDB `EXCEPT` removes duplicates, so `fct_invoice_line__equals_as_known` passes although the two objects do not return exactly the same rows.

**Exact ties in source order are selected arbitrarily, and the purported source-order test neither detects the tie nor makes the generator refuse it.**

> `qualify row_number() over (partition by %s order by source_ts desc, source_seq desc) = 1`

For `hk_customer='C1'` on `2026-06-03`, insert two `sat_customer__wwi` rows from the same record source with identical `(source_ts='2026-06-01 09:00:00', source_seq=7)` but names `Alpha` and `Beta`.  The PIT can point to either row and its later join matches both; meanwhile `one_source_order__sat_customer__wwi` passes because `count(distinct record_source)=1` and neither `source_ts` is null, so unsupported ordering is neither refused nor diagnosed.

**The generated “one row per key” test checks only duplicates, so it passes when a PIT, bridge, or computed satellite has silently lost keys.**

> `select %s from %s group by 1 having count(*) > 1`

At `2026-06-04`, let present hub keys be `L1` and `L2` but let `brg_invoice_line__sale` contain only L1 because a defective bridge predicate dropped L2.  `brg_invoice_line__sale__key_unique` returns no rows and passes: no generated test compares its key set or count with the two known-and-present hub keys, despite the named invariant requiring exactly one row for each.

**The lineage test omits every satellite-sourced dimension attribute, so wrong customer and segment labels can pass its row-by-row comparison.**

> `if afl.get("from", "").startswith("key.") and "via" not in afl:`

On `2026-06-05`, let staging identify customer 7 with category 10 named `Retail`, but let a bad category satellite pointer make `dim_customer` expose category ID 10 as `Wholesale`.  The generated delivered and mart projections compare `CustomerID`, `CustomerCategoryID`, `BuyingGroupID`, line identifiers, and amounts but never `customer_name`, `customer_category`, or `buying_group`; both `EXCEPT` branches are empty even though the analysis groups the sale under the wrong label.

VERDICT: FAILS historical macros leak and multiply restated satellite rows
