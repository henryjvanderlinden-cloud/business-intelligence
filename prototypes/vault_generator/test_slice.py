"""nsdn - the cloud test suite of the first slice (141 section 9 items 7 and 8; section 11 item 6).

Starts from a copy of a warehouse whose last load is the extract given, and loads two constructed days after it, the
way test_load.py constructs its late arrival: the last real extract is landed again under a later date and the landing
tables are edited before `dbt build` runs, with the runner's own landing code, profile (2 GB, file access off) and
build. The constructed cases are the paths of 141 section 3 that the simulation has not produced:

  absent      an invoice disappears from the extract while its lines stay: its lines keep their rows, on the unknown
              customer and without a date (bridge status 'not present'), on both days;
  reappears   a customer disappears on day 1 and comes back on day 2: on day 1 it is not in dim_customer and its lines
              are unplaced; on day 2 it is back and its lines are placed again;
  link ends   a buying-group member leaves its group (BuyingGroupID emptied, the old version closed into the history
              table): dim_customer shows 'No buying group' from day 1, and as known on the day before, the group;
  history     a customer known only from the history table, never current, with one invoice and one line: the
              customer is not in dim_customer and the line is unplaced (review of 141, finding 1).

On each day every test must pass, the warning test on unplaced rows must count exactly the constructed lines, and
the analysis must still reconcile. Replay: each object's macro as known on the day before equals the table built that
day (fingerprints of all 13 objects).

Usage: python test_slice.py --root REPO --warehouse WH.duckdb --extract DIR_OF_LAST_EXTRACT
The warehouse file is changed in place. If it does not exist, it is first created by loading the extract as the
warehouse's first day (whole history read), which needs no other extract. Exit 0 when every check passes.
"""
import argparse
import datetime as dt
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import test_load as tl   # noqa: E402

UNKNOWN = "0" * 64
OBJECTS = [("business_vault", "pit_buying_group"), ("business_vault", "pit_customer"),
           ("business_vault", "pit_customer_category"), ("business_vault", "pit_invoice"),
           ("business_vault", "pit_invoice_line"), ("business_vault", "pit_stock_item"),
           ("business_vault", "brg_customer__segment"), ("business_vault", "brg_invoice_line__sale"),
           ("business_vault", "csat_invoice_line__sales_amount"), ("marts", "dim_customer"), ("marts", "dim_date"),
           ("marts", "fct_invoice_line"), ("analyses", "sales_by_customer_segment_month")]


def fingerprints(con, as_known=None):
    out = {}
    for schema, name in OBJECTS:
        src = "%s.%s" % (schema, name) if as_known is None else "%s.%s__as_known(DATE '%s')" % (schema, name, as_known)
        out[name] = con.execute("select count(*), coalesce(sum(cast(hash(x) as hugeint)), 0) from (select * from %s) x"
                                % src).fetchone()
    return out


def pick(con):
    """The keys of the four cases, chosen from the landed extract so that they do not overlap."""
    one = lambda sql: con.execute(sql).fetchone()[0]
    k2 = one('select c."CustomerID" from landing.sales__customers c where c."BuyingGroupID" is null '
             'and c."CustomerID" = c."BillToCustomerID" and c."CustomerID" not in '
             '(select "BillToCustomerID" from landing.sales__customers where "CustomerID" <> "BillToCustomerID") '
             'and c."CustomerID" in (select "CustomerID" from landing.sales__invoices) order by cast(c."CustomerID" as int) limit 1')
    k3 = one('select "CustomerID" from landing.sales__customers where "BuyingGroupID" = \'1\' '
             'and "CustomerID" <> "BillToCustomerID" order by cast("CustomerID" as int) limit 1')
    inv = one('select "InvoiceID" from landing.sales__invoices where "CustomerID" not in (\'%s\', \'%s\') '
              'order by cast("InvoiceID" as int) desc limit 1' % (k2, k3))
    k4 = str(one('select max(cast("CustomerID" as int)) from landing.sales__customers') + 1000)
    return k2, k3, inv, k4


def edit_day(con, day_no, k2, k3, inv, k4, prev_day):
    """Apply the constructed cases to the landing tables of one day."""
    ex = con.execute
    # absent: the invoice goes, its lines stay (both days)
    ex('delete from landing.sales__invoices where "InvoiceID" = ?', [inv])
    # link ends: the member leaves its buying group, the old version closed into history (both days, so the source
    # stays consistent with what it said the day before)
    t = "%sT15:00:00.0000000" % prev_day
    ex('insert into landing.sales__customers_archive by name select * exclude ("ValidTo"), ? as "ValidTo" '
       'from landing.sales__customers where "CustomerID" = ?', [t, k3])
    ex('update landing.sales__customers set "BuyingGroupID" = null, "ValidFrom" = ? where "CustomerID" = ?', [t, k3])
    # history: a customer only ever in the history table, with one invoice of one line (both days)
    ex('insert into landing.sales__customers_archive by name select * exclude ("CustomerID", "BillToCustomerID", '
       '"CustomerName", "ValidFrom", "ValidTo"), ? as "CustomerID", ? as "BillToCustomerID", '
       '\'History Only Customer\' as "CustomerName", ? as "ValidFrom", ? as "ValidTo" '
       'from landing.sales__customers where "CustomerID" = ?',
       [k4, k4, "%sT10:00:00.0000000" % prev_day, "%sT11:00:00.0000000" % prev_day, k2])
    # reappears: the customer goes on day 1 only (after it served as the template of the history-only customer)
    if day_no == 1:
        ex('delete from landing.sales__customers where "CustomerID" = ?', [k2])
    new_inv = str(con.execute('select max(cast("InvoiceID" as int)) + 1000 from landing.sales__invoicelines').fetchone()[0])
    src_inv = con.execute('select min("InvoiceID") from landing.sales__invoices where "CustomerID" = ?', [k2]).fetchone()[0]
    if src_inv is None:   # day 1: k2's invoices are still there; take any other
        src_inv = con.execute('select min("InvoiceID") from landing.sales__invoices').fetchone()[0]
    ex('insert into landing.sales__invoices by name select * exclude ("InvoiceID", "CustomerID", "BillToCustomerID", '
       '"LastEditedWhen"), ? as "InvoiceID", ? as "CustomerID", ? as "BillToCustomerID", ? as "LastEditedWhen" '
       'from landing.sales__invoices where "InvoiceID" = ?', [new_inv, k4, k4, "%sT12:00:00.0000000" % prev_day, src_inv])
    ex('insert into landing.sales__invoicelines by name select * exclude ("InvoiceLineID", "InvoiceID", "LastEditedWhen"), '
       '? as "InvoiceLineID", ? as "InvoiceID", ? as "LastEditedWhen" from landing.sales__invoicelines '
       'where "InvoiceID" = ? order by cast("InvoiceLineID" as int) limit 1',
       [str(int(new_inv) * 10), new_inv, "%sT12:00:00.0000000" % prev_day, src_inv])
    return new_inv


def expectations(con, day_no, k2, k3, inv, k4, new_inv):
    """[(name, ok, detail)] for one day."""
    q1 = lambda sql, p=(): con.execute(sql, list(p)).fetchone()
    out = []
    n_inv_lines = q1('select count(*) from staging.stg_wwi__sales__invoicelines where not _is_history and "InvoiceID" = ?', [int(inv)])[0]
    absent = q1('select count(*), count(*) filter (where f.hk_customer = ? and f.invoice_date is null and f.invoice_id is null) '
                'from marts.fct_invoice_line f join business_vault.brg_invoice_line__sale b on b.hk_invoice_line = f.hk_invoice_line '
                'where b.invoice__status = \'not present\'', [UNKNOWN])
    out.append(("absent invoice: its %d lines kept, unplaced, undated" % n_inv_lines,
                absent[0] == n_inv_lines and absent[1] == n_inv_lines and n_inv_lines > 0, absent))
    k2_in_dim = q1('select count(*) from marts.dim_customer where customer_id = ?', [int(k2)])[0]
    k2_lines = q1('select count(*), count(*) filter (where f.hk_customer = ?) from marts.fct_invoice_line f '
                  'join staging.stg_wwi__sales__invoicelines l on l."InvoiceLineID" = f.invoice_line_id and not l._is_history '
                  'join staging.stg_wwi__sales__invoices i on i."InvoiceID" = l."InvoiceID" and not i._is_history '
                  'where i."CustomerID" = ?', [UNKNOWN, int(k2)])
    if day_no == 1:
        out.append(("reappearing customer, day 1: not in dim, %d lines unplaced" % k2_lines[0],
                    k2_in_dim == 0 and k2_lines[0] > 0 and k2_lines[1] == k2_lines[0], (k2_in_dim, k2_lines)))
    else:
        st = q1('select status from raw_vault.sts_customer__wwi s join raw_vault.hub_customer h using (hk_customer) '
                'where h."CustomerID" = ? order by s.load_date desc limit 1', [int(k2)])[0]
        out.append(("reappearing customer, day 2: %s, in dim, lines placed" % st,
                    st == "reappeared" and k2_in_dim == 1 and k2_lines[0] > 0 and k2_lines[1] == 0, (st, k2_in_dim, k2_lines)))
    k3_bg = q1('select buying_group, buying_group_id from marts.dim_customer where customer_id = ?', [int(k3)])
    out.append(("link ends: member shows 'No buying group'", k3_bg == ("No buying group", None), k3_bg))
    k4_dim = q1('select count(*) from marts.dim_customer where customer_id = ?', [int(k4)])[0]
    k4_hub = q1('select count(*) from raw_vault.hub_customer where "CustomerID" = ?', [int(k4)])[0]
    k4_line = q1('select count(*), count(*) filter (where hk_customer = ? and invoice_date is not null) from marts.fct_invoice_line '
                 'where invoice_id = ?', [UNKNOWN, int(new_inv)])
    out.append(("history-only customer: in the hub, not in dim, its line unplaced but dated",
                k4_hub == 1 and k4_dim == 0 and k4_line == (1, 1), (k4_hub, k4_dim, k4_line)))
    expect_unplaced = n_inv_lines + 1 + (k2_lines[0] if day_no == 1 else 0)
    unplaced = q1("select count(*) from marts.fct_invoice_line where hk_customer = ? or hk_bill_to_customer = ? "
                  "or invoice_date is null", [UNKNOWN, UNKNOWN])[0]
    out.append(("unplaced rows: exactly the constructed ones (%d)" % expect_unplaced, unplaced == expect_unplaced, unplaced))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--warehouse", required=True)
    ap.add_argument("--extract", required=True, help="folder of the last extract loaded into the warehouse")
    args = ap.parse_args()
    import duckdb
    runner = tl.runner_module(args.root)
    project = os.path.join(args.root, "prototypes", "wwi_sandbox", "dbt")
    profiles = os.path.join(args.root, "prototypes", "wwi_sandbox", "profiles")
    work = os.path.dirname(os.path.abspath(args.warehouse))
    p = tl.P(work, project, profiles)
    p.warehouse = os.path.abspath(args.warehouse)
    last = dt.date.fromisoformat(os.path.basename(os.path.normpath(args.extract)))
    results, ok_all = [], True
    if not os.path.exists(p.warehouse):
        t0 = dt.datetime.now()
        print("first day %s: %s in %ds" % (last, tl.load_day(runner, p, args.extract, last)[:300],
                                           (dt.datetime.now() - t0).seconds), flush=True)
    con = duckdb.connect(p.warehouse, read_only=True)
    before = {last: fingerprints(con)}
    con.close()
    keys = None
    for day_no in (1, 2):
        day = last + dt.timedelta(days=day_no)
        prev = day - dt.timedelta(days=1)
        tl.land(runner, p, args.extract, day)
        con = duckdb.connect(p.warehouse)
        if keys is None:
            keys = pick(con)
            print("keys: customer reappearing %s, member leaving %s, invoice absent %s, history-only customer %s" % keys, flush=True)
        new_inv = edit_day(con, day_no, *keys, prev.isoformat())
        con.close()
        t0 = dt.datetime.now()
        ok, summary = tl.dbt_build(runner, p, day)
        tl.log_row(runner, p, day, "ok" if ok else "failed")
        print("day %d (%s): build %s in %ds: %s" % (day_no, day, "ok" if ok else "FAILED", (dt.datetime.now() - t0).seconds,
                                                     summary[:600]), flush=True)
        if not ok:
            results.append(("build %s" % day, False, summary[:600]))
            ok_all = False
            break
        con = duckdb.connect(p.warehouse, read_only=True)
        for name, good, detail in expectations(con, day_no, *keys, new_inv):
            results.append(("day %d: %s" % (day_no, name), good, detail))
        replay = fingerprints(con, as_known=prev.isoformat())
        diff = [n for n in replay if replay[n] != before[prev][n]]
        results.append(("day %d: as known on %s equals the tables built that day (13 objects)" % (day_no, prev),
                        not diff, diff))
        before[day] = fingerprints(con)
        con.close()
    for name, good, detail in results:
        ok_all = ok_all and good
        print("%-4s %s%s" % ("ok" if good else "FAIL", name, "" if good else "  -> %s" % (detail,)), flush=True)
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
