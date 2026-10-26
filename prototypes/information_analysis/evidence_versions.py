"""Evidence for step A (handover 10): which columns of a system-versioned table ever change between the versions of
one row, and so whether a declared-unique name or code is stable enough to serve as a business key.

For each table that has a history table, the current rows and the earlier versions are grouped by the primary key,
and for every column the script counts the keys whose versions hold more than one distinct value. Audit and period
columns are counted like any other, so that a version created without a business change shows as such. Aggregates
only (analysis/README.md section 7); written into analysis/wwi/tables/<schema>/<table>/evidence/.

    python prototypes/information_analysis/evidence_versions.py
"""
import inspect
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from profile_tables import ROOT, RAW, reader, write, blob, now, sha  # noqa: E402
import ia_lib as ia  # noqa: E402

SCRIPT = "prototypes/information_analysis/evidence_versions.py"
DAY = os.environ.get("IA_DAY", "2016-06-02")
VERSIONED = {"Application.Cities": "CityID", "Application.Countries": "CountryID",
             "Application.DeliveryMethods": "DeliveryMethodID", "Application.PaymentMethods": "PaymentMethodID",
             "Application.People": "PersonID", "Application.StateProvinces": "StateProvinceID",
             "Application.TransactionTypes": "TransactionTypeID",
             "Purchasing.SupplierCategories": "SupplierCategoryID", "Purchasing.Suppliers": "SupplierID",
             "Sales.BuyingGroups": "BuyingGroupID", "Sales.CustomerCategories": "CustomerCategoryID",
             "Sales.Customers": "CustomerID", "Warehouse.Colors": "ColorID",
             "Warehouse.PackageTypes": "PackageTypeID", "Warehouse.StockGroups": "StockGroupID",
             "Warehouse.StockItems": "StockItemID"}


def column_changes(table, key):
    """Per column: the number of keys whose current and earlier versions hold more than one distinct value."""
    values = {}
    head = None
    versions = 0
    for t in (table, table + "_Archive"):
        f, h, rows = reader(DAY, t)
        if head is None:
            head = h
        idx = [h.index(c) for c in head]
        k = h.index(key)
        for r in rows:
            versions += 1
            per_key = values.setdefault(r[k], [set() for _ in head])
            for j, i in enumerate(idx):
                per_key[j].add(r[i])
        f.close()
    with_history = sum(1 for v in values.values() if len(v[head.index("ValidFrom")]) > 1)
    changed = {c: sum(1 for v in values.values() if len(v[j]) > 1) for j, c in enumerate(head)}
    return {"key": key, "keys": len(values), "versions": versions, "keys_with_earlier_versions": with_history,
            "keys_whose_column_changed": {c: n for c, n in changed.items() if n},
            "columns_never_changed": sorted(c for c, n in changed.items() if not n)}


def main():
    manifest = sha(os.path.join(RAW, DAY, "manifest.json"))
    for table, key in VERSIONED.items():
        rec = {"kind": "profile", "tool": SCRIPT, "tool_version": blob(SCRIPT), "code": inspect.getsource(column_changes),
               "inputs": {"source": "wwi", "extract": DAY, "manifest_sha256": manifest,
                          "tables": [table, table + "_Archive"]},
               "ran_at": now(), "result": column_changes(table, key)}
        s, n = table.split(".")
        h = write(os.path.join(ROOT, "analysis", "wwi", "tables", ia.escape(s), ia.escape(n), "evidence"), rec)
        r = rec["result"]
        print(h, table, r["keys"], r["versions"], r["keys_with_earlier_versions"], r["keys_whose_column_changed"])


if __name__ == "__main__":
    main()
