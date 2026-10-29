"""Transcribe the ruled design of 147, 148 and 149 into declaration files under model/ (ARC-OP-29, proposed format).

One-off and re-runnable: it reads the tables of the three notes, which are the ruled text (ADR-0029, ADR-0031,
ADR-0033), and writes one file per hub, link, satellite and reference table, plus model/sources/wwi.md. Nothing is
decided here; where a note leaves something open the file says so. Run from the repository root:

    python prototypes/model_declarations/transcribe_wwi.py <step id> <written_at ISO timestamp>

The output is checked by tools/check_repo.py (model rules). Written in session S11.
"""
import json
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
N147 = "docs/10_architecture/147_wwi-concepts-keys-and-business-time.md"
N148 = "docs/10_architecture/148_wwi-relationships.md"
N149 = "docs/10_architecture/149_wwi-satellites.md"
TABLES = "analysis/wwi/tables"
ACROSS = "analysis/wwi/across"
AUTHOR = "claude-opus-5-5"

STEP, WRITTEN_AT = sys.argv[1], sys.argv[2]

HUBS = ["country", "state_province", "city", "person", "customer", "customer_category", "buying_group", "supplier",
        "stock_item", "stock_group", "special_deal", "sales_order", "sales_order_line", "invoice", "invoice_line",
        "purchase_order", "purchase_order_line", "customer_ledger_entry", "supplier_ledger_entry", "stock_movement",
        "cold_room_sensor", "vehicle"]
AREA = {"geography": ["country", "state_province", "city"],
        "parties": ["person", "customer", "customer_category", "buying_group", "supplier"],
        "products and deals": ["stock_item", "stock_group", "special_deal"],
        "sales": ["sales_order", "sales_order_line", "invoice", "invoice_line"],
        "purchasing": ["purchase_order", "purchase_order_line"],
        "ledgers": ["customer_ledger_entry", "supplier_ledger_entry", "stock_movement"],
        "sensors": ["cold_room_sensor", "vehicle"]}
AREA_OF = {h: a for a, hs in AREA.items() for h in hs}
AREA_SECTION = {"geography": "3.1", "parties": "3.2", "products and deals": "3.3", "sales": "3.4", "purchasing": "3.5",
                "ledgers": "3.6", "sensors": "3.7"}

LINK_ROLES = ["state_province", "country", "delivery_city", "postal_city", "bill_to_customer", "buying_group",
              "customer_category", "primary_contact", "alternate_contact", "delivery_city", "postal_city",
              "primary_contact", "alternate_contact", "supplier", "stock_group", "customer", "buying_group",
              "customer_category", "stock_item", "stock_group", "customer", "salesperson", "contact", "picker",
              "backorder", "sales_order", "stock_item", "sales_order", "customer", "bill_to_customer", "salesperson",
              "contact", "accounts_contact", "packer", "invoice", "stock_item", "supplier", "contact",
              "purchase_order", "stock_item", "bill_to_customer", "invoice", "supplier", "purchase_order",
              "stock_item", "customer", "invoice", "supplier", "purchase_order"]

# The naming event's own date per driving hub (147 section 5); lines have none of their own.
EVENT_DATE = {"sales_order": "Sales.Orders.OrderDate", "invoice": "Sales.Invoices.InvoiceDate",
              "purchase_order": "Purchasing.PurchaseOrders.OrderDate",
              "customer_ledger_entry": "Sales.CustomerTransactions.TransactionDate",
              "supplier_ledger_entry": "Purchasing.SupplierTransactions.TransactionDate",
              "stock_movement": "Warehouse.StockItemTransactions.TransactionOccurredWhen"}

REF = {"DeliveryMethodID": "ref_delivery_method__wwi", "PaymentMethodID": "ref_payment_method__wwi",
       "TransactionTypeID": "ref_transaction_type__wwi", "SupplierCategoryID": "ref_supplier_category__wwi",
       "ColorID": "ref_color__wwi", "PackageTypeID": "ref_package_type__wwi", "UnitPackageID": "ref_package_type__wwi",
       "OuterPackageID": "ref_package_type__wwi"}
REF_TABLES = {"ref_delivery_method__wwi": ("Application.DeliveryMethods", "DeliveryMethodID"),
              "ref_payment_method__wwi": ("Application.PaymentMethods", "PaymentMethodID"),
              "ref_transaction_type__wwi": ("Application.TransactionTypes", "TransactionTypeID"),
              "ref_supplier_category__wwi": ("Purchasing.SupplierCategories", "SupplierCategoryID"),
              "ref_color__wwi": ("Warehouse.Colors", "ColorID"),
              "ref_package_type__wwi": ("Warehouse.PackageTypes", "PackageTypeID"),
              "ref_system_parameters__wwi": ("Application.SystemParameters", "SystemParameterID")}


def read(path):
    with open(os.path.join(ROOT, path), encoding="utf-8") as f:
        return f.read()


def table_rows(text, start, stop):
    """Rows of every markdown table between two headings, as lists of cells."""
    seg = text[text.index(start):text.index(stop)]
    rows = []
    for ln in seg.split("\n"):
        if ln.startswith("|") and not ln.startswith("|---"):
            cells = [c.strip() for c in ln.strip().strip("|").split(" | ")]
            if cells[0] in ("#", "Satellite", "Table"):
                continue
            rows.append(cells)
    return rows


def catalogue():
    """{ 'Schema.Table': {'columns': [...], 'pk': [...]} } from the catalogue evidence of each table."""
    out = {}
    for sch in sorted(os.listdir(os.path.join(ROOT, TABLES))):
        for tab in sorted(os.listdir(os.path.join(ROOT, TABLES, sch))):
            ev = os.path.join(ROOT, TABLES, sch, tab, "evidence")
            for fn in sorted(os.listdir(ev)) if os.path.isdir(ev) else []:
                with open(os.path.join(ev, fn), encoding="utf-8") as f:
                    d = json.load(f)
                if d.get("kind") == "catalogue query" and isinstance(d.get("result"), dict) \
                        and "columns" in d["result"]:
                    cols = sorted(d["result"]["columns"], key=lambda c: int(c["column_id"]))
                    out["%s.%s" % (sch, tab)] = {"columns": [c["column_name"] for c in cols], "evidence": fn[:-5]}
    return out


# ---------- citations ----------

def claim_exists(path):
    p, _, c = path.partition("#")
    full = os.path.join(ROOT, p)
    if not os.path.isfile(full):
        return False
    return not c or ("- %s |" % c) in read(p)


def expand(cell, table_dir=None, rel_dir=None):
    """Backticked citations of one evidence cell as repository paths; ranges `#C1` to `#C3` expanded."""
    toks = re.findall(r"`([^`]+)`|(\bto\b)|(\b0\d#C\d+\b)", cell)
    out, last, pending_range = [], None, False
    for tick, to, short in toks:
        if to:
            pending_range = last is not None
            continue
        if short:
            if rel_dir:
                n, c = short.split("#")
                f = [x for x in os.listdir(os.path.join(ROOT, rel_dir)) if x.startswith(n + "_")]
                out.append("%s/%s#%s" % (rel_dir, f[0], c) if f else "%s/%s?#%s" % (rel_dir, n, c))
            continue
        t = tick
        if not ("#C" in t or t.endswith(".md")):
            continue
        if t.startswith("#C"):
            if last is None:
                continue
            base = last.split("#")[0]
            if pending_range:
                a = int(last.split("#C")[1]) if "#C" in last else 1
                b = int(t[2:])
                out.extend("%s#C%d" % (base, i) for i in range(a + 1, b + 1))
                pending_range = False
                last = "%s#C%d" % (base, b)
                continue
            t = base + t
        elif t.startswith("across/"):
            t = ACROSS + t[len("across"):]
        elif t.startswith("analysis/"):
            pass
        elif re.match(r"^(Application|Sales|Purchasing|Warehouse)/", t):
            t = TABLES + "/" + t
        elif table_dir:
            t = table_dir + "/" + t
        out.append(t)
        last = t
        pending_range = False
    seen, res = set(), []
    for t in out:
        if t not in seen:
            seen.add(t)
            res.append(t)
    return res


def table_dir(qualified):
    s, t = qualified.split(".")
    return "%s/%s/%s" % (TABLES, s, t)


# ---------- writing ----------

FILES = {}


def emit(path, front, sections, prose):
    lines = ["---"] + ["%s: %s" % (k, v) for k, v in front.items()] + ["---", ""]
    for title, items in sections:
        if not items:
            continue
        lines += ["## " + title, ""] + items + [""]
    if prose:
        lines += ["## Notes", ""] + prose + [""]
    FILES[path] = "\n".join(lines)


def common(kind, name, ident, defined_in, ruled_in, status="accepted"):
    return {"id": ident, "kind": kind, "name": name, "status": status, "ruled_in": ruled_in,
            "defined_in": defined_in, "written_by": AUTHOR, "written_at": WRITTEN_AT, "step": STEP,
            "method": "transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note"}


def main():
    cat = catalogue()
    n147, n148, n149 = read(N147), read(N148), read(N149)

    # ---- hubs (147 section 3)
    hub_rows = table_rows(n147, "## 3. The hubs proposed", "Notes on single rows")
    assert len(hub_rows) == 22, len(hub_rows)
    hub_table = {}
    for i, r in enumerate(hub_rows):
        num, concept, src, key, space, grain, ev = r
        slug = HUBS[i]
        src = src.strip()
        keycol = re.match(r"`(\w+)`", key).group(1)
        hub_table[slug] = src
        kind = "record-identifier" if "record identifier" in key else (
            "governed" if space.startswith("ISO") else "source-key")
        ks = "iso3166-1" if space.startswith("ISO") else space.strip("`")
        cites = expand(ev, table_dir(src))
        front = common("hub", "hub_" + slug, "nsdn:rv:hub:" + slug,
                       "%s#3 item %s" % (N147, num), "ADR-0029, ADR-0030" + (", ADR-0028" if slug in
                                                                          ("country", "cold_room_sensor", "vehicle") else ""))
        front.update({"concept": concept, "grain": grain, "subject_area": AREA_OF[slug]})
        emit("model/raw_vault/hubs/hub_%s.md" % slug, front,
             [("Business key", ["- %s.%s | key_space=%s | key_kind=%s" % (src, keycol, ks, kind)]),
              ("Evidence", ["- " + c for c in cites])],
             [])

    # ---- links (148 section 3)
    link_rows = table_rows(n148, "## 3. The links proposed", "## 4. Relationships derived")
    assert len(link_rows) == 49, len(link_rows)
    hub_by_concept = {}
    for i, r in enumerate(hub_rows):
        hub_by_concept[r[1].split(" (")[0]] = HUBS[i]
    links = {}
    for i, r in enumerate(link_rows):
        num, label, fromto, rel, optional, eff, ev = r
        m = re.match(r"(.+?) (?:\(.*?\) )?(?:→|↔) (.+?)(?: \(.*\))?$", fromto)
        a, b = m.group(1).strip(), m.group(2).strip()
        a = re.sub(r" \(.*\)$", "", a)
        fh, th = hub_by_concept[a], hub_by_concept[b]
        name = "lnk_%s__%s" % (fh, LINK_ROLES[i])
        rels = re.findall(r"`([^`]+)`", rel)
        cols = []
        for rr in rels:
            child = rr.split("__")[0]
            parts = child.split(".")
            cols.append("%s.%s.%s" % tuple(parts[:3]))
        driving = "none" if "↔" in fromto else "hub_" + fh
        # "Optional means the naming column may be empty" (148 section 3): a nullable column is optional even where the
        # data never leaves it empty (link 28), as 149 Rule 5 reads it by keeping Sales.Invoices.OrderID as delivered.
        opt = "yes" if optional.startswith("yes") or "nullable" in optional else "no"
        opt_note = optional
        eff_kind = eff
        if eff == "event":
            start = EVENT_DATE.get(fh, "unknown")
        elif eff == "milestone":
            start = "Sales.Orders.PickingCompletedWhen"
        elif eff == "absence":
            start = "presence in a complete extract"
        else:
            start = "load"
        cites = []
        for rr in rels:
            cites += expand(ev, rel_dir="%s/relations/%s" % (ACROSS, rr))
            if len(rels) > 1:
                break
        front = common("link", name, "nsdn:rv:link:" + name[4:], "%s#3 link %s" % (N148, num), "ADR-0031, ADR-0030")
        front.update({"label": label, "from": "hub_" + fh, "to": "hub_" + th, "driving": driving,
                      "optional": opt, "effectivity": eff_kind, "effectivity_start": start,
                      "subject_area": AREA_OF[fh]})
        if opt == "yes" and optional != "yes":
            front["optional_note"] = optional[len("yes"):].strip(" ()")
        elif optional not in ("yes", "no"):
            front["optional_note"] = optional
        colsec = ["- %s | names=hub_%s" % (cols[0], th if driving != "none" else fh)] if driving != "none" else \
            ["- %s | names=hub_%s" % (cols[0], fh), "- %s | names=hub_%s" % (cols[1], th)]
        if driving == "none":
            colsec.append("- Warehouse.StockItemStockGroups.StockItemStockGroupID | kept=effectivity satellite, as delivered")
        prose = []
        if eff == "event" and start == "unknown":
            prose.append("148 gives this link an event start, but its driving hub, a line, has no event date of its own"
                         " (147 section 5), so the start is unknown until the author rules; see ARC-OP-29.")
        links[name] = (fh, th, cols)
        emit("model/raw_vault/links/%s.md" % name, front,
             [("Columns", colsec), ("Relations", ["- %s/relations/%s" % (ACROSS, rr) for rr in rels]),
              ("Evidence", ["- " + c for c in cites])], prose)

    # ---- satellites (149 section 3)
    sat_rows = table_rows(n149, "## 3. Satellites on the hubs", "## 4. Links, reference tables")
    link_by_col = {}
    for name, (fh, th, cols) in links.items():
        for c in cols:
            link_by_col[c] = name
    for r in sat_rows:
        sname, colcell, split, vt, cls, ev = r
        sname = sname.strip("`")
        parent = re.match(r"sat_(.+?)__wwi", sname).group(1)
        src = hub_table[parent]
        if parent == "stock_item" and sname.endswith("__holding"):
            src = "Warehouse.StockItemHoldings"
        pk = {"Warehouse.StockItemHoldings": "StockItemID"}.get(src)
        if pk is None:
            hubfile = FILES["model/raw_vault/hubs/hub_%s.md" % parent]
            pk = re.search(r"^- [\w]+\.[\w]+\.(\w+) \|", hubfile, re.M).group(1)
        if parent == "country":
            pk = "IsoAlpha3Code"
        # columns
        cols = []
        for group in colcell.split("; "):
            delivered = group.endswith(" as delivered")
            g = group[:-len(" as delivered")] if delivered else group
            for piece in re.split(r", | and ", g):
                piece = piece.strip()
                ann = re.findall(r"\(([^)]*)\)", piece)
                cname = re.sub(r"\s*\(.*?\)", "", piece).strip()
                if not cname:
                    continue
                cols.append((cname, ann, delivered))
        colsec = []
        known = cat[src]["columns"]
        for cname, ann, delivered in cols:
            flags = []
            if cname not in known:
                flags.append("ERROR=not in the source catalogue")
            lk = link_by_col.get("%s.%s" % (src, cname))
            if delivered and lk:
                # "as delivered" in 149 qualifies the relationship columns of its group (149 Rule 5)
                flags.append("as_delivered=%s" % lk)
            elif delivered and cname.endswith("ID") and cname not in REF:
                flags.append("as_delivered=UNRESOLVED")
            if any(a.startswith("code") for a in ann):
                flags.append("code=%s" % REF.get(cname, "UNRESOLVED"))
            if any("reading key" in a for a in ann):
                flags.append("reading_key=yes")
            if cname == "HashedPassword":
                flags.append("load=never (ADR-0033 decision 2)")
            if sname == "sat_vehicle__wwi__position" and cname in ("VehicleTemperatureID", "RecordedWhen"):
                flags.append("repeats=sat_vehicle__wwi__chiller_reading")
            if sname == "sat_purchase_order__wwi" and cname == "IsOrderFinalized":
                flags.append("valid_time=unknown (finalisation undated)")
            colsec.append("- " + " | ".join([cname] + flags))
        if split in ("—", "-"):
            split_reason = "none (main satellite)"
        else:
            split_reason = split
        sk = "payload"
        if split.startswith("milestone"):
            sk = "milestone"
        if "reading series" in split:
            sk = "reading"
        if sname == "sat_vehicle__wwi__position":
            sk = "reading"
        vt_decl = vt
        m = re.match(r"^`(\w+)`", vt)
        if m:
            vt_decl = "%s.%s" % (src, m.group(1))
            if "unknown" in vt:
                vt_decl += " (the undated finalisation: unknown)"
        cls_main = cls.split(";")[0].strip()
        cls_cond = cls.split(";", 1)[1].strip() if ";" in cls else ""
        if cls_main.startswith("personal where"):
            cls_cond, cls_main = cls_main, "internal"
        area = AREA_OF[parent]
        front = common("satellite", sname, "nsdn:rv:sat:" + sname[4:],
                       "%s#%s" % (N149, AREA_SECTION[area]), "ADR-0033" + (", ADR-0028" if sk == "milestone" else ""))
        front.update({"parent": "hub_" + parent, "source": "wwi", "source_table": src,
                      "parent_key": "%s.%s" % (src, pk), "satellite_kind": sk, "split_reason": split_reason,
                      "valid_time": vt_decl, "class": cls_main})
        if cls_cond:
            front["class_condition"] = cls_cond
        front["subject_area"] = area
        emit("model/raw_vault/satellites/wwi/%s.md" % sname, front,
             [("Columns", colsec), ("Evidence", ["- " + c for c in expand(ev, table_dir(src))])], [])

    # ---- reference tables (149 section 4)
    for name, (src, key) in REF_TABLES.items():
        known = cat[src]["columns"]
        rest = [c for c in known if c != key and c not in ("ValidFrom", "ValidTo", "LastEditedWhen")]
        front = common("reference", name, "nsdn:rv:ref:" + name[4:], "%s#4" % N149, "ADR-0029, ADR-0033")
        hist = src + "_Archive" if (src + "_Archive") in cat else "none"
        front.update({"source": "wwi", "source_table": src, "key": "%s.%s" % (src, key), "key_space": "wwi",
                      "history": hist, "class": "internal" if name.endswith("system_parameters__wwi") else "open",
                      "subject_area": "reference"})
        emit("model/raw_vault/reference/wwi/%s.md" % name, front,
             [("Columns", ["- " + c for c in rest]),
              ("Evidence", ["- %s/06_keys.md#C5" % table_dir(src)] if claim_exists("%s/06_keys.md#C5" % table_dir(src))
               else ["- %s/06_keys.md" % table_dir(src)])], [])

    # ---- the source
    base = sorted(t for t in cat if not t.endswith("_Archive"))
    lines = []
    for t in base:
        cs = cat[t]["columns"]
        st = "ValidFrom, ValidTo" if "ValidFrom" in cs else ("LastEditedWhen" if "LastEditedWhen" in cs else "none")
        hist = t + "_Archive" if t + "_Archive" in cat else "none"
        audit = "LastEditedBy" if "LastEditedBy" in cs else "none"
        lines.append("- %s | system_time=%s | audit=%s | history=%s | catalogue=%s/evidence/%s.json"
                     % (t, st, audit, hist, table_dir(t), cat[t]["evidence"]))
    front = {"id": "nsdn:source:wwi", "kind": "source", "name": "wwi", "status": "accepted",
             "ruled_in": "ADR-0015, ADR-0027, ADR-0029, ADR-0033", "defined_in": "%s#2 and %s#2" % (N147, N149),
             "written_by": AUTHOR, "written_at": WRITTEN_AT, "step": STEP,
             "method": "transcribed by prototypes/model_declarations/transcribe_wwi.py",
             "title": "Wide World Importers, one database instance", "key_space": "wwi",
             "extract": "full, daily, with a manifest of row counts and hashes",
             "by_rule": "LastEditedBy to the hub's audit satellite (kept in reference tables); ValidFrom, ValidTo, "
                        "LastEditedWhen as source system time"}
    emit("model/sources/wwi.md", front, [("Base tables", lines)],
         ["The 31 base tables of the source and, for each, the columns handled by rule rather than declared: its "
          "source system time (149 Rule 2), its audit column (149 Rule 3) and its history table, loaded on the first "
          "day (ADR-0027 decision 2). The 17 history tables yield nothing of their own (147 section 4)."])

    for p, text in sorted(FILES.items()):
        full = os.path.join(ROOT, p)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
    print("%d files written" % len(FILES))


if __name__ == "__main__":
    main()
