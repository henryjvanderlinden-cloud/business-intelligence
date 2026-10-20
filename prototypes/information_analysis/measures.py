"""Items 8 (measures), 9 (derived columns) and 28 (arithmetic policy) of 129, per base table with numeric columns.

For every numeric column that is not a key, a foreign key or an audit column: the declared type, precision and scale,
filling, range, signs, the decimals actually used, and the signs per transaction type where the table has one. Then
per table the tests of formulas and rounding that its columns suggest: a computed value compared with the stored one
under several rounding modes, an inequality between two quantities, or a copy of a value held elsewhere. Writes one
evidence file per table into its evidence folder; counts only, no rows.

    python prototypes/information_analysis/measures.py

Reads the extract IA_DAY (default 2016-06-01) and the catalogue summaries in scratch/ia_profile/.
"""
import collections
import inspect
import json
import os
import sys
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_DOWN, ROUND_HALF_DOWN

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from profile_tables import ROOT, DAY, reader, write, blob, now, sha, RAW  # noqa: E402
from relations import load_catalogues  # noqa: E402
import ia_lib as ia  # noqa: E402

SCRIPT = "prototypes/information_analysis/measures.py"
SOURCE = "wwi"
AUDIT = {"LastEditedBy", "LastEditedWhen", "ValidFrom", "ValidTo"}
NUMERIC = {"decimal", "numeric", "int", "bigint", "smallint", "tinyint", "float", "real", "money"}
MODES = {"half_up": ROUND_HALF_UP, "half_even": ROUND_HALF_EVEN, "half_down": ROUND_HALF_DOWN, "truncate": ROUND_DOWN}
CENT = Decimal("0.01")


def rows_of(t):
    f, head, rows = reader(DAY, t)
    out = [dict(zip(head, r)) for r in rows]
    f.close()
    return out


def D(v):
    return Decimal(v) if v != "" else None


def decimals(v):
    if "." not in v:
        return 0
    return len(v.split(".")[1].rstrip("0"))


def rounding(exact, stored):
    """How often a computed exact value, rounded to cents by each mode, equals the stored value."""
    out = {"compared": 0, "exact": 0}
    for m in MODES:
        out[m] = 0
    worst = Decimal(0)
    for e, s in zip(exact, stored):
        if e is None or s is None:
            continue
        out["compared"] += 1
        out["exact"] += e == s
        for m, mode in MODES.items():
            out[m] += e.quantize(CENT, mode) == s
        worst = max(worst, abs(e - s))
    out["largest_difference"] = str(worst)
    return out


def columns(t, cat, rows, types):
    """Profile of the numeric non-key columns of one table."""
    c = cat["catalogue"]
    pk = {k["column_name"] for k in c["keys"] if k["is_primary_key"] == "1"}
    fk = {k["column_name"] for k in c["foreign_keys_out"]}
    out = {}
    for x in c["columns"]:
        n = x["column_name"]
        if x["type_name"] not in NUMERIC or n in pk | fk | AUDIT:
            continue
        vals = [r[n] for r in rows if r[n] != ""]
        nums = [Decimal(v) for v in vals]
        col = {"type": x["type_name"], "precision": int(x["precision"]), "scale": int(x["scale"]), "description": x["description"],
               "rows": len(rows), "filled": len(vals), "distinct": len(set(nums)),
               "min": str(min(nums)) if nums else None, "max": str(max(nums)) if nums else None,
               "negative": sum(1 for v in nums if v < 0), "zero": sum(1 for v in nums if v == 0),
               "positive": sum(1 for v in nums if v > 0), "max_decimals_used": max((decimals(v) for v in vals), default=0),
               "non_integer": sum(1 for v in nums if v != v.to_integral_value())}
        if col["distinct"] <= 12:
            col["values"] = {str(k): v for k, v in sorted(collections.Counter(nums).items())}
        if "TransactionTypeID" in rows[0] if rows else False:
            by = collections.defaultdict(lambda: collections.Counter())
            for r in rows:
                v = D(r[n])
                by[types.get(r["TransactionTypeID"], r["TransactionTypeID"])]["empty" if v is None else
                                                                              "negative" if v < 0 else "zero" if v == 0 else "positive"] += 1
            col["sign_by_transaction_type"] = {k: dict(v) for k, v in sorted(by.items())}
        out[n] = col
    return out


def t_invoice_lines(rows, ref):
    q = [D(r["Quantity"]) for r in rows]
    up = [D(r["UnitPrice"]) for r in rows]
    tr = [D(r["TaxRate"]) for r in rows]
    tax = [D(r["TaxAmount"]) for r in rows]
    ext = [D(r["ExtendedPrice"]) for r in rows]
    lp = [D(r["LineProfit"]) for r in rows]
    si, h = ref["Warehouse.StockItems"], ref["Warehouse.StockItemHoldings"]
    cost = [h.get(r["StockItemID"], {}).get("LastCostPrice") for r in rows]
    return {
        "TaxAmount = Quantity x UnitPrice x TaxRate / 100": rounding([a * b * c / 100 for a, b, c in zip(q, up, tr)], tax),
        "ExtendedPrice = Quantity x UnitPrice + TaxAmount": sum(a * b + c == e for a, b, c, e in zip(q, up, tax, ext)),
        "LineProfit = Quantity x (UnitPrice - current LastCostPrice of the item)": sum(
            1 for a, b, c, p in zip(q, up, cost, lp) if c is not None and a * (b - Decimal(c)) == p),
        "LineProfit sign": dict(collections.Counter("negative" if p < 0 else "zero" if p == 0 else "positive" for p in lp)),
        "UnitPrice equals the item's current UnitPrice": sum(1 for r, b in zip(rows, up) if D(si[r["StockItemID"]]["UnitPrice"]) == b),
        "TaxRate equals the item's current TaxRate": sum(1 for r, c in zip(rows, tr) if D(si[r["StockItemID"]]["TaxRate"]) == c),
        "lines": len(rows)}


def t_order_lines(rows, ref):
    si = ref["Warehouse.StockItems"]
    picked = [r for r in rows if r["PickingCompletedWhen"] != ""]
    open_ = [r for r in rows if r["PickingCompletedWhen"] == ""]
    return {
        "lines": len(rows), "picked lines (PickingCompletedWhen filled)": len(picked),
        "picked lines with PickedQuantity = Quantity": sum(r["PickedQuantity"] == r["Quantity"] for r in picked),
        "picked lines with PickedQuantity < Quantity": sum(int(r["PickedQuantity"]) < int(r["Quantity"]) for r in picked),
        "unpicked lines with PickedQuantity = 0": sum(r["PickedQuantity"] == "0" for r in open_),
        "unpicked lines with 0 < PickedQuantity < Quantity": sum(0 < int(r["PickedQuantity"]) < int(r["Quantity"]) for r in open_),
        "UnitPrice equals the item's current UnitPrice": sum(D(si[r["StockItemID"]]["UnitPrice"]) == D(r["UnitPrice"]) for r in rows),
        "TaxRate equals the item's current TaxRate": sum(D(si[r["StockItemID"]]["TaxRate"]) == D(r["TaxRate"]) for r in rows),
        "columns holding an amount": [c for c in rows[0] if c in ("TaxAmount", "ExtendedPrice", "LineTotal", "LineProfit")]}


def t_ledger(rows, ref, types):
    by = collections.defaultdict(collections.Counter)
    tax15 = collections.defaultdict(lambda: [[], []])
    for r in rows:
        k = types[r["TransactionTypeID"]]
        a, tx, t, ob = D(r["AmountExcludingTax"]), D(r["TaxAmount"]), D(r["TransactionAmount"]), D(r["OutstandingBalance"])
        b = by[k]
        b["rows"] += 1
        b["TransactionAmount = AmountExcludingTax + TaxAmount"] += a + tx == t
        b["OutstandingBalance = 0"] += ob == 0
        b["OutstandingBalance = TransactionAmount"] += ob == t and ob != 0
        b["OutstandingBalance other"] += ob != 0 and ob != t
        b["IsFinalized = 1"] += r["IsFinalized"] == "1"
        b["IsFinalized = 1 and OutstandingBalance = 0"] += r["IsFinalized"] == "1" and ob == 0
        tax15[k][0].append(a * Decimal("0.15"))
        tax15[k][1].append(tx)
    party = "CustomerID" if "CustomerID" in rows[0] else "SupplierID"
    tot, ob = collections.Counter(), collections.Counter()
    for r in rows:
        tot[r[party]] += D(r["TransactionAmount"])
        ob[r[party]] += D(r["OutstandingBalance"])
    return {"parties": len(tot), "parties whose TransactionAmount sums to their OutstandingBalance sum": sum(tot[k] == ob[k] for k in tot),
            "by_transaction_type": {k: dict(v) for k, v in sorted(by.items())},
            "TaxAmount = 15% of AmountExcludingTax": {k: rounding(*v) for k, v in sorted(tax15.items())}}


def t_purchase_order_lines(rows, ref):
    si, h = ref["Warehouse.StockItems"], ref["Warehouse.StockItemHoldings"]
    fin = [r for r in rows if r["IsOrderLineFinalized"] == "1"]
    open_ = [r for r in rows if r["IsOrderLineFinalized"] != "1"]
    per_outer_price = sum(D(si[r["StockItemID"]]["UnitPrice"]) * int(si[r["StockItemID"]]["QuantityPerOuter"]) == D(r["ExpectedUnitPricePerOuter"]) for r in rows)
    per_outer_cost = sum(D(h[r["StockItemID"]]["LastCostPrice"]) * int(si[r["StockItemID"]]["QuantityPerOuter"]) == D(r["ExpectedUnitPricePerOuter"]) for r in rows)
    return {"lines": len(rows), "finalized lines": len(fin),
            "finalized lines with ReceivedOuters = OrderedOuters": sum(r["ReceivedOuters"] == r["OrderedOuters"] for r in fin),
            "open lines with ReceivedOuters = 0": sum(r["ReceivedOuters"] == "0" for r in open_),
            "lines with 0 < ReceivedOuters < OrderedOuters": sum(0 < int(r["ReceivedOuters"]) < int(r["OrderedOuters"]) for r in rows),
            "lines with ReceivedOuters > OrderedOuters": sum(int(r["ReceivedOuters"]) > int(r["OrderedOuters"]) for r in rows),
            "ExpectedUnitPricePerOuter = item UnitPrice x QuantityPerOuter": per_outer_price,
            "ExpectedUnitPricePerOuter = item LastCostPrice x QuantityPerOuter": per_outer_cost}


def t_stock_items(rows, ref):
    ratio = collections.Counter()
    for r in rows:
        up, rrp = D(r["UnitPrice"]), D(r["RecommendedRetailPrice"])
        ratio[str((rrp / up).quantize(Decimal("0.0001")))] += 1
    rrp_rule = rounding([D(r["UnitPrice"]) * Decimal("1.3") * (1 + D(r["TaxRate"]) / 100) for r in rows],
                        [D(r["RecommendedRetailPrice"]) for r in rows])
    h = ref["Warehouse.StockItemHoldings"]
    from fractions import Fraction
    cost_ratio = collections.Counter(str((D(h[r["StockItemID"]]["LastCostPrice"]) / D(r["UnitPrice"])).quantize(Decimal("0.01")))
                                     for r in rows if r["StockItemID"] in h)
    exact = {Fraction(h[r["StockItemID"]]["LastCostPrice"]) / Fraction(r["UnitPrice"]) for r in rows if r["StockItemID"] in h}
    return {"items": len(rows), "RecommendedRetailPrice / UnitPrice, 4 decimals": dict(ratio.most_common(5)),
            "RecommendedRetailPrice = UnitPrice x 1.3 x (1 + TaxRate / 100)": rrp_rule,
            "LastCostPrice / UnitPrice, 2 decimals (most common)": dict(cost_ratio.most_common(5)),
            "distinct LastCostPrice / UnitPrice ratios, rounded to 2 decimals": len(cost_ratio),
            "distinct LastCostPrice / UnitPrice ratios, exact": len(exact)}


def t_holdings(rows, ref):
    return {"items": len(rows),
            "QuantityOnHand = LastStocktakeQuantity": sum(r["QuantityOnHand"] == r["LastStocktakeQuantity"] for r in rows),
            "ReorderLevel <= TargetStockLevel": sum(int(r["ReorderLevel"]) <= int(r["TargetStockLevel"]) for r in rows),
            "QuantityOnHand < ReorderLevel": sum(int(r["QuantityOnHand"]) < int(r["ReorderLevel"]) for r in rows)}


def t_special_deals(rows, ref):
    return {"deals": len(rows), "filled pattern (DiscountAmount, DiscountPercentage, UnitPrice)": dict(collections.Counter(
        "".join("x" if r[c] != "" else "-" for c in ("DiscountAmount", "DiscountPercentage", "UnitPrice")) for r in rows))}


def t_population(rows, ref):
    """Does a parent's LatestRecordedPopulation equal the sum over its children?"""
    out = {}
    for child, key, parent, pkey in (("Application.Cities", "StateProvinceID", "Application.StateProvinces", "StateProvinceID"),
                                     ("Application.StateProvinces", "CountryID", "Application.Countries", "CountryID")):
        tot = collections.Counter()
        for r in ref["rows:" + child]:
            if r["LatestRecordedPopulation"] != "":
                tot[r[key]] += int(r["LatestRecordedPopulation"])
        par = {r[pkey]: r["LatestRecordedPopulation"] for r in ref["rows:" + parent]}
        cmp_ = [(k, int(par[k]), v) for k, v in tot.items() if par.get(k, "") != ""]
        out["%s vs sum over %s" % (parent, child)] = {"parents compared": len(cmp_), "equal": sum(a == b for _, a, b in cmp_),
                                                      "parent greater": sum(a > b for _, a, b in cmp_), "parent smaller": sum(a < b for _, a, b in cmp_)}
    return out


TESTS = {"Sales.InvoiceLines": t_invoice_lines, "Sales.OrderLines": t_order_lines,
         "Sales.CustomerTransactions": "ledger", "Purchasing.SupplierTransactions": "ledger",
         "Purchasing.PurchaseOrderLines": t_purchase_order_lines, "Warehouse.StockItems": t_stock_items,
         "Warehouse.StockItemHoldings": t_holdings, "Sales.SpecialDeals": t_special_deals,
         "Application.StateProvinces": t_population, "Application.Countries": t_population}


def main():
    cats = load_catalogues()
    types = {r["TransactionTypeID"]: r["TransactionTypeName"] for r in rows_of("Application.TransactionTypes")}
    ref = {"Warehouse.StockItems": {r["StockItemID"]: r for r in rows_of("Warehouse.StockItems")},
           "Warehouse.StockItemHoldings": {r["StockItemID"]: r for r in rows_of("Warehouse.StockItemHoldings")}}
    for t in ("Application.Cities", "Application.StateProvinces", "Application.Countries"):
        ref["rows:" + t] = rows_of(t)
    code = "\n".join(inspect.getsource(f) for f in (rows_of, decimals, rounding, columns, t_invoice_lines, t_order_lines, t_ledger,
                                                    t_purchase_order_lines, t_stock_items, t_holdings, t_special_deals, t_population))
    done = {}
    for t, cat in sorted(cats.items()):
        rows = rows_of(t)
        cols = columns(t, cat, rows, types)
        if not cols:
            continue
        test = TESTS.get(t)
        tests = (t_ledger(rows, ref, types) if test == "ledger" else test(rows, ref) if test else {})
        rec = {"kind": "profile", "tool": SCRIPT, "tool_version": blob(SCRIPT), "code": code,
               "inputs": {"source": SOURCE, "extract": DAY, "manifest_sha256": sha(os.path.join(RAW, DAY, "manifest.json")), "table": t},
               "ran_at": now(), "result": {"columns": cols, "tests": tests}}
        s, n = t.split(".")
        h = write(os.path.join(ROOT, "analysis", SOURCE, "tables", ia.escape(s), ia.escape(n), "evidence"), rec)
        done[t] = h
        print(t, h)
    with open(os.path.join(ROOT, "scratch", "ia_measures_index.json"), "w") as f:
        json.dump(done, f, indent=1)


if __name__ == "__main__":
    main()
