"""Verify the sales viewer's numbers down the whole chain, independently of the dbt tests that guard each layer.

The dbt build already tests each object of the slice on every load (grain, keys, lookups, lineage, reconciliation with
the delivery, replay as known; prototypes/wwi_sandbox/dbt/tests/generated/). This script asks the reader's question
instead: do the figures on the page add up to the same totals at every layer they pass through, and are they
plausible? It reads the warehouse read-only and the built page, and changes nothing. Run from the repository root:

    python prototypes/sales_viewer/verify.py [--warehouse <file.duckdb>] [--page <sales_viewer.html>] [--json <file>]

The chain, from source to screen:

  L0 staging      staging.stg_wwi__sales__invoicelines, current rows (not _is_history), as delivered
  L1 raw vault    the latest version of every present invoice line, read from the satellite, the status satellite and
                  the link directly (raw_vault.sat_/sts_invoice_line__wwi, lnk_invoice_line__invoice), not via the PIT
  L2 bus. vault   business_vault.pit_invoice_line + csat_invoice_line__sales_amount (the computed sales amount)
  L3 mart         marts.fct_invoice_line
  L4 analysis     analyses.sales_by_customer_segment_month
  L5 page         the rows embedded in sales_viewer.html, re-aggregated here the way the page does

Totals compared at every layer: line count (where the layer has lines), sales excl. tax, gross profit, invoices.
Cross-cuts compared between the mart and the analysis: per month, per segment, per year. Plausibility checks: lines
add up within themselves, no fan-out through the dimensions, monthly figures stay in range. Exit 0 when all pass.
"""
import argparse
import json
import os
import re
import sys
from collections import defaultdict
from decimal import Decimal

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
DEFAULT_DB = os.path.join(ROOT, "data", "warehouse", "published", "wwi.duckdb")
DEFAULT_PAGE = os.path.join(HERE, "out", "sales_viewer.html")
CENT = Decimal("0.01")

RESULTS = []


def check(name, ok, detail):
    RESULTS.append({"check": name, "ok": bool(ok), "detail": detail})
    print("%-4s %-58s %s" % ("PASS" if ok else "FAIL", name, detail))


def totals(con, sql):
    r = con.execute(sql).fetchone()
    return tuple(Decimal(str(x)) if isinstance(x, (float, Decimal)) else x for x in r)


def main():
    ap = argparse.ArgumentParser(description="Verify the sales viewer down the chain.")
    ap.add_argument("--warehouse", default=DEFAULT_DB)
    ap.add_argument("--page", default=DEFAULT_PAGE)
    ap.add_argument("--json", help="also write the results to this file")
    a = ap.parse_args()
    import duckdb
    con = duckdb.connect(a.warehouse, read_only=True)
    load_date = con.execute("select max(load_date) from raw_vault.sat_invoice_line__wwi").fetchone()[0]
    print("warehouse %s, latest invoice-line load %s\n" % (os.path.relpath(a.warehouse, ROOT), load_date))

    # ---- layer totals: lines, sales excl. tax, gross profit, invoices
    L = {}
    L["L0 staging"] = totals(con, """
        select count(*), sum(cast("ExtendedPrice" - "TaxAmount" as decimal(18,2))), sum("LineProfit"), count(distinct "InvoiceID")
        from staging.stg_wwi__sales__invoicelines where not _is_history""")
    # The raw vault on its own terms, without the business vault's PIT: the latest satellite version of each line whose
    # latest status is 'present', and the invoice through the link.
    L["L1 raw vault"] = totals(con, """
        with cur as (select * from raw_vault.sat_invoice_line__wwi
                     qualify row_number() over (partition by hk_invoice_line order by load_date desc, source_ts desc nulls last, source_seq desc) = 1),
        st as (select * from raw_vault.sts_invoice_line__wwi
               qualify row_number() over (partition by hk_invoice_line order by load_date desc) = 1)
        select count(*), sum(cast(s."ExtendedPrice" - s."TaxAmount" as decimal(18,2))), sum(s."LineProfit"), count(distinct l.hk_invoice)
        from cur s join st on st.hk_invoice_line = s.hk_invoice_line and st.status = 'present'
        left join raw_vault.lnk_invoice_line__invoice l on l.hk_invoice_line = s.hk_invoice_line""")
    L["L2 business vault"] = totals(con, """
        select count(*), sum(c.sales_amount_excl_tax), sum(s."LineProfit"), count(distinct b.hk_invoice)
        from business_vault.pit_invoice_line p
        join business_vault.csat_invoice_line__sales_amount c on c.hk_invoice_line = p.hk_invoice_line
        join business_vault.brg_invoice_line__sale b on b.hk_invoice_line = p.hk_invoice_line
        join raw_vault.sat_invoice_line__wwi s on s.hk_invoice_line = p.hk_invoice_line
         and s.record_source = p.sat_invoice_line__wwi__record_source
         and s.source_ts is not distinct from p.sat_invoice_line__wwi__source_ts
         and s.source_seq = p.sat_invoice_line__wwi__source_seq""")
    L["L3 mart"] = totals(con, """
        select count(*), sum(sales_amount_excl_tax), sum(gross_profit_at_current_cost), count(distinct invoice_id)
        from marts.fct_invoice_line""")
    L["L4 analysis"] = (None,) + totals(con, """
        select sum(sales_amount_excl_tax), sum(gross_profit_at_current_cost), sum(invoices)
        from analyses.sales_by_customer_segment_month""")

    page = None
    if os.path.exists(a.page):
        with open(a.page, encoding="utf-8") as f:
            html = f.read()
        m = re.search(r"const DATA = (\{.*?\});\n", html, re.S)
        page = json.loads(m.group(1).replace("<\\/", "</"))
        rows = page["rows"]
        L["L5 page"] = (None, sum(Decimal(str(r[3])) for r in rows).quantize(CENT),
                        sum(Decimal(str(r[4])) for r in rows).quantize(CENT), sum(r[5] for r in rows))

    print("%-18s %10s %18s %18s %9s" % ("layer", "lines", "sales excl. tax", "gross profit", "invoices"))
    for k, v in L.items():
        print("%-18s %10s %18s %18s %9s" % (k, "" if v[0] is None else v[0], v[1], v[2], v[3]))
    print()
    ref = L["L3 mart"]
    for k, v in L.items():
        if k == "L3 mart":
            continue
        same = all(v[i] == ref[i] for i in range(4) if v[i] is not None)
        check("totals %s = mart" % k, same, "lines, sales, profit, invoices" if v[0] is not None else "sales, profit, invoices")

    # ---- cross-cuts: mart recomputed by month and by segment, straight from the fact, vs the analysis table
    cut = """select %s, sum(f.sales_amount_excl_tax), sum(f.gross_profit_at_current_cost), count(distinct f.invoice_id)
        from marts.fct_invoice_line f left join marts.dim_customer d on d.hk_customer = f.hk_customer group by all"""
    acut = """select %s, sum(sales_amount_excl_tax), sum(gross_profit_at_current_cost), sum(invoices)
        from analyses.sales_by_customer_segment_month group by all"""
    for label, fk, ak in [("month", "strftime(f.invoice_date, '%Y-%m')", "month"),
                          ("year", "cast(year(f.invoice_date) as varchar)", "left(month, 4)"),
                          ("segment", "d.customer_category || ' / ' || d.buying_group", "customer_category || ' / ' || buying_group"),
                          ("month x segment", "strftime(f.invoice_date, '%Y-%m') || ' ' || d.customer_category || ' / ' || d.buying_group",
                           "month || ' ' || customer_category || ' / ' || buying_group")]:
        fm = {r[0]: r[1:] for r in con.execute(cut % fk).fetchall()}
        am = {r[0]: r[1:] for r in con.execute(acut % ak).fetchall()}
        diff = [k for k in set(fm) | set(am) if fm.get(k) != am.get(k)]
        check("analysis = fact, per %s" % label, not diff, "%d cells%s" % (len(fm), "" if not diff else ", differing: %s" % sorted(diff)[:5]))

    if page:
        pm = defaultdict(lambda: [Decimal(0), Decimal(0), 0])
        for r in page["rows"]:
            k = r[0][:4]
            pm[k][0] += Decimal(str(r[3])); pm[k][1] += Decimal(str(r[4])); pm[k][2] += r[5]
        fy = {r[0]: r[1:] for r in con.execute(cut % "cast(year(f.invoice_date) as varchar)").fetchall()}
        diff = [k for k in fy if (pm[k][0].quantize(CENT), pm[k][1].quantize(CENT), pm[k][2]) != fy[k]]
        check("page rows = fact, per year", not diff, "%d years%s" % (len(fy), "" if not diff else ", differing: %s" % diff))
        months = con.execute("select month, bool_and(is_complete_month) from marts.dim_date group by 1 order by 1").fetchall()
        check("page calendar = dim_date", [[m, bool(c)] for m, c in months] == [[x["m"], x["c"]] for x in page["months"]],
              "%d months, %d partial" % (len(months), sum(1 for _, c in months if not c)))

    # ---- plausibility
    q = lambda sql: con.execute(sql).fetchone()
    n = q("select count(*) from marts.fct_invoice_line where sales_amount_excl_tax + tax_amount <> sales_amount_incl_tax")[0]
    check("each line: excl. tax + tax = incl. tax", n == 0, "%d lines off" % n)
    n = q("select count(*) from (select invoice_line_id from marts.fct_invoice_line group by 1 having count(*) > 1)")[0]
    check("no invoice line twice in the fact (no double counting)", n == 0, "%d duplicates" % n)
    n = q("select count(*) from (select hk_customer from marts.dim_customer group by 1 having count(*) > 1)")[0]
    check("one dimension row per customer (no fan-out on the join)", n == 0, "%d customers with several rows" % n)
    n = q("""select count(*) from (select invoice_id from marts.fct_invoice_line f join marts.dim_customer d on d.hk_customer = f.hk_customer
             group by 1 having count(distinct d.customer_category || d.buying_group) > 1)""")[0]
    check("each invoice in exactly one segment (invoice counts add up)", n == 0, "%d invoices in several segments" % n)
    n = q("select count(*) from (select invoice_id from marts.fct_invoice_line group by 1 having count(distinct invoice_date) > 1)")[0]
    check("each invoice in exactly one month (invoice counts add up)", n == 0, "%d invoices in several months" % n)
    r = q("""select count(*) filter (where invoice_date is null), count(*) filter (where hk_customer = repeat('0', 64)),
             count(*) filter (where is_credit_note) from marts.fct_invoice_line""")
    check("no unplaced lines, no credit notes", r == (0, 0, 0), "undated %d, unknown customer %d, credit notes %d" % r)
    r = q("""select count(*) filter (where quantity <= 0), count(*) filter (where sales_amount_excl_tax < 0),
             count(*) filter (where gross_profit_at_current_cost > sales_amount_excl_tax) from marts.fct_invoice_line""")
    check("no negative quantities or sales, profit never above sales", r == (0, 0, 0), "%d / %d / %d lines" % r)
    r = q("""select min(m), max(m), min(v), max(v), median(v) from (
             select month, 100 * sum(gross_profit_at_current_cost) / sum(sales_amount_excl_tax) as m, sum(sales_amount_excl_tax) as v
             from analyses.sales_by_customer_segment_month where is_complete_month group by 1)""")
    check("monthly margin within 40-60 %", 40 <= r[0] and r[1] <= 60, "%.1f %% to %.1f %%" % (r[0], r[1]))
    check("monthly sales within 0.5x-2x the median", r[2] >= Decimal("0.5") * r[4] and r[3] <= 2 * r[4],
          "%s to %s, median %s" % (round(r[2]), round(r[3]), round(r[4])))
    r = q("""select count(*) from (select month from analyses.sales_by_customer_segment_month group by 1 having count(*) <> 7)""")
    check("every month has all seven segments", r[0] == 0, "%d months short" % r[0])
    r = q("""select count(distinct invoice_date), max(invoice_date) from marts.fct_invoice_line where strftime(invoice_date, '%Y-%m') = '2016-06'""")
    check("the partial month holds only days up to the load date", r[1] is None or r[1] <= load_date, "%d invoice days, last %s" % r)

    con.close()
    failed = [x for x in RESULTS if not x["ok"]]
    print("\n%d checks, %d failed" % (len(RESULTS), len(failed)))
    if a.json:
        with open(a.json, "w", encoding="utf-8") as f:
            json.dump({"warehouse": os.path.relpath(a.warehouse, ROOT), "load_date": str(load_date),
                       "layers": {k: [None if x is None else str(x) for x in v] for k, v in L.items()},
                       "checks": RESULTS}, f, indent=1)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
