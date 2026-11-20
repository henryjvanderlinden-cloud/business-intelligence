"""Build the sales viewer: one self-contained HTML page over the first slice's analysis table.

A reader, never a source of truth, like the schema viewer (142 section 3): every figure it shows is read from the
published warehouse on each build, and nothing in the page is edited by hand. It reads the declared analysis
analyses.sales_by_customer_segment_month (ADR-0039) and the calendar in marts.dim_date, checks that the analysis sums
to the same totals as marts.fct_invoice_line, and embeds the rows in template.html. The page then slices and dices in
the browser: period, measure, split (total, category, buying group, segment), grain (month, quarter, year), a line
chart with a crosshair readout and a sortable table underneath. Run from the repository root:

    python prototypes/sales_viewer/build.py [--warehouse <file.duckdb>] [--brand <folder>] [--out <folder>]

Without --brand the page uses a neutral theme. A brand folder holds a brand.json (colours, series palette, font and
logo files relative to that folder); company house styles are kept outside this repository (ADR-0035 decision 2), so
the folder is passed in rather than stored here. Writes <out>/sales_viewer.html (default: out/ beside this file,
which is ignored by git because the page embeds warehouse figures and possibly a house style). Needs duckdb.
"""
import argparse
import base64
import datetime
import json
import mimetypes
import os
import sys
from decimal import Decimal

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
DEFAULT_DB = os.path.join(ROOT, "data", "warehouse", "published", "wwi.duckdb")
STATUS = os.path.join(ROOT, "data", "warehouse", "status.json")
ANALYSIS = "analyses.sales_by_customer_segment_month"
FACT = "marts.fct_invoice_line"
TITLE = "Sales by customer segment"


def read_warehouse(path):
    import duckdb
    con = duckdb.connect(path, read_only=True)
    rows = con.execute(
        "select month, customer_category, buying_group, sales_amount_excl_tax, gross_profit_at_current_cost, invoices "
        "from %s order by month, customer_category, buying_group" % ANALYSIS).fetchall()
    months = con.execute(
        "select month, bool_and(is_complete_month) from marts.dim_date group by month order by month").fetchall()
    fact = con.execute(
        "select sum(sales_amount_excl_tax), sum(gross_profit_at_current_cost), count(distinct invoice_id) from %s" % FACT
    ).fetchone()
    con.close()
    return rows, months, fact


def data_uri(path):
    mime = mimetypes.guess_type(path)[0] or ("font/woff2" if path.endswith(".woff2") else "application/octet-stream")
    with open(path, "rb") as f:
        return "data:%s;base64,%s" % (mime, base64.b64encode(f.read()).decode("ascii"))


def brand_parts(folder):
    """(css, logo_html, series, name) from <folder>/brand.json; neutral defaults when no folder is given."""
    if not folder:
        return "", '<span class="word">nsdn</span>', None, None
    with open(os.path.join(folder, "brand.json"), encoding="utf-8") as f:
        b = json.load(f)
    css = []
    for ff in b.get("fonts", []):
        css.append('  @font-face { font-family: "%s"; src: url(%s) format("woff2"); font-weight: %s; }'
                   % (ff["family"], data_uri(os.path.join(folder, ff["file"])), ff["weight"]))
    vars_ = "".join(" %s: %s;" % (k, v) for k, v in b.get("css", {}).items())
    css.append("  :root {%s }" % vars_)
    logo = b.get("logo")
    logo_html = ('<img src="%s" alt="%s">' % (data_uri(os.path.join(folder, logo)), b.get("name", ""))) if logo \
        else '<span class="word">%s</span>' % b.get("name", "")
    return "\n".join(css), logo_html, b.get("series"), b.get("name")


def main():
    ap = argparse.ArgumentParser(description="Build the sales viewer.")
    ap.add_argument("--warehouse", default=DEFAULT_DB, help="DuckDB file to read (default: the published warehouse)")
    ap.add_argument("--brand", help="folder holding brand.json (house style kept outside this repository)")
    ap.add_argument("--out", default=os.path.join(HERE, "out"), help="output folder (default: out/ beside this file)")
    a = ap.parse_args()

    rows, months, fact = read_warehouse(a.warehouse)
    dated = [r for r in rows if r[0] is not None]
    undated = len(rows) - len(dated)
    tot = [sum((r[i] for r in rows), Decimal(0)) for i in (3, 4)] + [sum(r[5] for r in rows)]
    reconciles = tot[0] == fact[0] and tot[1] == fact[1] and tot[2] == fact[2]

    known_on = None
    if os.path.exists(STATUS):
        with open(STATUS, encoding="utf-8") as f:
            known_on = json.load(f).get("last_ok_date")
    data = {
        "meta": {
            "analysis_table": ANALYSIS, "fact_table": FACT,
            "warehouse": os.path.relpath(a.warehouse, ROOT).replace(os.sep, "/") if a.warehouse.startswith(ROOT) else os.path.basename(a.warehouse),
            "known_on": known_on or "unknown",
            "built_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "reconciles": reconciles, "undated_rows": undated,
            "analysis_totals": [str(tot[0]), str(tot[1]), tot[2]], "fact_totals": [str(fact[0]), str(fact[1]), fact[2]],
        },
        "months": [{"m": m, "c": bool(c)} for m, c in months],
        "domains": {
            "categories": sorted({r[1] for r in dated}),
            "buying_groups": sorted({r[2] for r in dated}),
            "segments": sorted({"%s · %s" % (r[1], r[2]) for r in dated}),
        },
        "rows": [[r[0], r[1], r[2], float(r[3] or 0), float(r[4] or 0), int(r[5] or 0)] for r in dated],
    }

    css, logo_html, series, brand_name = brand_parts(a.brand)
    data["meta"]["brand"] = brand_name
    with open(os.path.join(HERE, "template.html"), encoding="utf-8") as f:
        page = f.read()
    page = page.replace("__TITLE__", TITLE).replace("/*__BRAND_CSS__*/", css).replace("<!--__LOGO__-->", logo_html)
    page = page.replace("/*__DATA__*/null", json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/"))
    if series:
        page = page.replace("/*__SERIES__*/", "%s; //" % json.dumps(series))
    os.makedirs(a.out, exist_ok=True)
    target = os.path.join(a.out, "sales_viewer.html")
    with open(target, "w", encoding="utf-8", newline="\n") as f:
        f.write(page)

    print("rows %d (undated %d), months %d, segments %d" % (len(rows), undated, len(months), len(data["domains"]["segments"])))
    print("analysis totals %s / %s / %d" % (tot[0], tot[1], tot[2]))
    print("fact totals     %s / %s / %d" % (fact[0], fact[1], fact[2]))
    print("reconciles: %s" % ("yes" if reconciles else "NO"))
    print("wrote %s (%d kB)" % (os.path.relpath(target, ROOT), os.path.getsize(target) // 1024))
    return 0 if reconciles else 1


if __name__ == "__main__":
    sys.exit(main())
