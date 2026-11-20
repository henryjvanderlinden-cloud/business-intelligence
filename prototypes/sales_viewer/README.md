# Sales viewer

**Question.** What does the first slice's answer (sales over time by customer segment, ADR-0039) look like to a
business reader who wants to slice and dice it, without a BI tool in between, and do its figures add up all the way
down the chain?

**Answer, so far.** A single self-contained HTML page, built from the declared analysis on the mart, whose totals agree
to the cent with the mart, the business vault, the raw vault and staging (section 4). Ruled on 2026-11-19
([ADR-0045](../../docs/20_decisions/0045-sales-viewer-proof-of-concept.md), closing `ARC-OP-39`): a **proof of
concept, not a supported tool**. What it demonstrates is that the agentic layer can generate a functioning
visualization of the datamart, given the context the model has. Like the
[schema viewer](../schema_viewer/build.py) it is a reader, never a source of truth. `verify.py` is recorded as a first
test towards the [test framework](../../docs/10_architecture/162_test-framework.md) (`ARC-OP-31`).

    python prototypes/sales_viewer/build.py
    python prototypes/sales_viewer/build.py --brand C:\Git\vdl-diaa\huisstijl
    python prototypes/sales_viewer/verify.py --json prototypes/sales_viewer/out/verify.json

Both need the `duckdb` Python package and read the published warehouse read-only.

## 1. What the page does

`build.py` reads `analyses.sales_by_customer_segment_month` and the calendar in `marts.dim_date`, checks that the
analysis sums to the same sales, gross profit and invoice count as `marts.fct_invoice_line` (it exits non-zero if
not), and writes `out/sales_viewer.html` from `template.html` with the rows embedded. In the page the reader chooses a
month range with presets, a measure (sales excl. tax, gross profit at current cost, gross margin, invoices), what the
lines stand for (total, category, buying group, segment), a grain (month, quarter, year), and which categories and
buying groups are in; four totals, a line chart with a crosshair readout and a sortable table underneath with a CSV
download all follow the same selection. A period that is not complete in the warehouse, or is cut by the range, is
drawn dashed and badged. Margin is always the sum of profit over the sum of sales, never an average of margins, and
its axis is fitted to the data with a note saying so.

## 2. How it was built (session of 2026-11-19, Claude Opus 5.5, at the author's request)

The author asked for an HTML visualization of the datamart with slicing and dicing, a line chart and a table
underneath, in the style of the VDL-DIAA website. The work went as follows.

1. **Reading the mart.** The declarations in `model/marts/` (`fct_invoice_line`, `dim_customer`, `dim_date`) and the
   generated SQL in `prototypes/wwi_sandbox/dbt/models/` were read to establish grain, measures and their caveats
   (gross profit is the source's LineProfit at current cost; margin is not stored). The published warehouse,
   `data/warehouse/published/wwi.duckdb`, known on 2016-06-06 (`data/warehouse/status.json`), holds the analysis
   at 294 rows: 42 months by 7 segments.
2. **Choosing the source.** The page reads the declared analysis, not the fact table, because the analysis is the
   ruled answer to the business question (ADR-0039) and is small enough to embed whole (about 300 rows). Every
   slicing the page offers is a roll-up of that analysis: invoices add up across months and segments because an
   invoice has one date and one customer, which section 4 checks rather than assumes.
3. **Finding the house style.** `C:\Git\vdl-diaa` has no website code yet, only images; the house style is carried
   by the invoice template (`facturen/sjabloon/factuur-sjabloon.html`: navy, brown and sky with a tri-colour strip,
   IBM Plex Sans) and the header logo (`website/vdl-diaa-logo-header.png`).
4. **Keeping company material out of this repository.** ADR-0035 decision 2 keeps VDL-DIAA's logo and website
   material out of nsdn, and the repository is public under CC0 (ADR-0041). So the page is built neutral by default,
   the house style was put in `C:\Git\vdl-diaa\huisstijl\brand.json` (colours, series palette, fonts and logo by
   relative path) and is passed in with `--brand`, and `out/` is ignored by git, since the page embeds warehouse
   figures and, when branded, company material. Proposed by the model; the author ruled on 2026-11-19 that house
   styles stay outside this repository (ADR-0045).
5. **Colours.** The line colours are brand-led (a steel blue and the house brown first) and were checked with a
   palette validator for lightness, chroma, colour-blind and normal-vision separation between neighbours; all pass.
   Three colours fall below 3:1 contrast on white, which is acceptable only because every value is also in the table.
6. **Rendering and correcting.** The page was rendered in a headless browser and inspected at each split and grain.
   Three faults were found and fixed: margin was unreadable on an axis from zero (now fitted, and said so), the
   sticky table footer misdrew under `border-collapse` (now separate borders), and a resize redraw wiped the hover
   readout (now redrawn only when the width changes).

## 3. What was already guarding the numbers

The dbt build tests every object of the slice on every load (`prototypes/wwi_sandbox/dbt/tests/generated/`): grain and
key uniqueness, lookups into the dimensions, a lineage test that rebuilds every fact row from staging and compares row
by row, a reconciliation of every measure with the delivery, the computed sales amount against its oracle, replay "as
known", and warnings on unplaced rows, credit notes and implausible months. The build that produced the published
warehouse (2026-11-17 11:46 UTC, load date 2016-06-06) passed all 831 tests with no warnings
(`data/warehouse/dbt-target/run_results.json`, `data/warehouse/runner.log`).

## 4. Verification of the page's figures (2026-11-19)

`verify.py` asks the reader's question across the layers rather than per object, reads everything read-only, and
changes nothing. Its run on the published warehouse gave 22 checks, 0 failed:

| layer | lines | sales excl. tax | gross profit | invoices |
| --- | ---: | ---: | ---: | ---: |
| staging (current rows) | 229,483 | 173,266,439.30 | 86,218,715.65 | 70,888 |
| raw vault (satellite, status, link; not via the PIT) | 229,483 | 173,266,439.30 | 86,218,715.65 | 70,888 |
| business vault (PIT, computed satellite, bridge) | 229,483 | 173,266,439.30 | 86,218,715.65 | 70,888 |
| mart (`fct_invoice_line`) | 229,483 | 173,266,439.30 | 86,218,715.65 | 70,888 |
| analysis | | 173,266,439.30 | 86,218,715.65 | 70,888 |
| rows embedded in the page | | 173,266,439.30 | 86,218,715.65 | 70,888 |

Beyond the totals, the analysis was recomputed from the fact table and matched cell for cell per month (42), per year
(4), per segment (7) and per month by segment (294); the page's embedded rows matched the fact per year and its
calendar matched `dim_date`. The plausibility checks found no line where excl. tax plus tax differs from incl. tax, no
invoice line twice, one dimension row per customer (so no fan-out on the join), every invoice in exactly one segment
and one month (so invoice counts may be summed), no unplaced lines and no credit notes, no negative quantities or
sales and no profit above sales, monthly margins between 48.8 % and 50.6 %, complete months between 0.66 and 1.23
times the median, all seven segments in every month, and in the partial month only invoice days up to the load date.

The figures the page computes on screen were checked once more, separately, because the checks above read the
embedded rows and not the page's own roll-ups. The built page was driven in a headless browser in the cloud
workspace and its table cells compared with SQL on the fact table: sales by year and buying group (12 cells), invoices
by quarter (14), margin by year and category (20) and gross profit by segment for March 2015 (7). All 53 matched,
money to the displayed dollar and margins to the displayed tenth of a percent. That script needs a browser and was not
kept in the repository; the check is recorded here and is not reproducible from it as it stands.

## 5. Not done

The session did not write a handover, as the work is a side branch of handover 14's task. The page and its checks
are unreviewed on another model (rule 12 of `AGENTS.md`). The page has a light theme only, matching the house style.
The verification is a script run by hand, not a gate in the build; whether it should become one belongs to
`ARC-OP-31` and `ARC-OP-33`. As a proof of concept the viewer is not maintained (ADR-0045).
