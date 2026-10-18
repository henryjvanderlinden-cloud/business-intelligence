"""Write round-1 dossiers (ADR-0017 to ADR-0019) from the evidence of profile_tables.py plus an agent's judgements.

Two kinds of claim go into each item file, and the file says which is which in its method line:
  - claims derived mechanically from the evidence (declared catalogue facts, observed counts), built by the
    functions below with fixed confidence rules;
  - claims of judgement (role, grain in business terms, interpretations, sensitivity readings), supplied per table
    in a specification module by the agent that wrote them.

    python prototypes/information_analysis/write_dossiers.py <spec module path> [Schema.Table ...]
"""
import importlib.util
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import ia_lib as ia  # noqa: E402

PROFILE_DIR = os.path.join(ROOT, "scratch", "ia_profile")
D, OBS = "2016-06-01", "2026-10-18"
AUDIT = {"LastEditedBy", "LastEditedWhen", "ValidFrom", "ValidTo"}
SENSITIVE = re.compile(r"(Name$|Email|Phone|Fax|Address|Password|Logon|Photo|Location|URL|Comments|Instructions|"
                       r"ReceivedBy|Bank|Preferences|CustomFields|Languages|Registration)")
RANK = ia.CONFIDENCE


def ascii_only(s):
    s = s.replace("—", "-").replace("–", "-").replace("’", "'").replace("“", '"').replace("”", '"')
    assert all(ord(ch) < 128 for ch in s), s
    return s


class Item:
    def __init__(self, nn):
        self.nn, self.claims = nn, []

    def add(self, typ, conf, ev, recheck, text, status="proposed"):
        self.claims.append((typ, status, conf, ev, recheck, ascii_only(text)))


def fmt_claims(claims, evmap):
    out = []
    for i, (typ, status, conf, ev, recheck, text) in enumerate(claims, 1):
        evs = ",".join(evmap[e] for e in ev if evmap.get(e)) or "none"
        out.append("- C%d | type=%s | status=%s | confidence=%s | effective=%s | observed=%s | checked=%s | "
                   "evidence=%s | recheck=%s | text: %s" % (i, typ, status, conf, D, OBS, OBS, evs, recheck, text))
    return out


def write_item(path, front, claims, evmap, reasoning, uncert, person):
    lines = fmt_claims(claims, evmap)
    live = [c for c in claims if c[1] not in ("superseded", "retracted")]
    front = dict(front, confidence=RANK[min(RANK.index(c[2]) for c in live)], claims=str(len(claims)))
    txt = "---\n" + "\n".join("%s: %s" % (k, front[k]) for k in ia.FRONT_KEYS) + "\n---\n\n## Claims\n\n" + \
        "\n".join(lines) + "\n\n## Reasoning\n\n" + ascii_only(reasoning.strip()) + "\n\n## Uncertainties\n\n" + \
        ascii_only(uncert.strip() or "None.") + "\n\n## For a person\n\n" + ascii_only(person.strip() or "None.") + "\n"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="ascii", newline="\n") as f:
        f.write(txt)


def plural(n, word):
    if n == 1:
        return "%s %s" % (format(n, ","), word)
    return "%s %s" % (format(n, ","), word[:-1] + "ies" if word.endswith("y") else word + "s")


# --------------------------------------------------------------------------- mechanical claims

def mech_granularity(it, d):
    keys = [k for k in d["catalogue"]["keys"] if k["is_primary_key"] == "1"]
    pk = [k["column_name"] for k in keys]
    if pk:
        it.add("declared", "high", ["catalogue"], "the primary key changes",
               "The declared primary key is %s (%s)." % (" + ".join(pk), keys[0]["index_name"]))
    p = d["profile"].get("pk")
    n = d["profile"]["rows"]
    if p:
        ok = p["distinct"] == n and p["empty"] == 0
        it.add("observed", "high", ["profile"], "the key stops being unique",
               "The key is %s over all %s, with %s." % ("unique" if ok else "NOT unique", plural(n, "row"),
                                                       "no empty values" if p["empty"] == 0 else "%d empty" % p["empty"]))
    return pk


def mech_temporal(it, d, zone=True):
    c = d["catalogue"]
    tb = c["table"][0]
    tt = tb["temporal_type_desc"]
    if tt == "SYSTEM_VERSIONED_TEMPORAL_TABLE":
        it.add("declared", "high", ["catalogue"], "the temporal type changes",
               "The table is system-versioned: SQL Server keeps every earlier version of a row in %s, with the "
               "period columns ValidFrom and ValidTo." % tb["history_table"])
    elif tt == "HISTORY_TABLE":
        it.add("declared", "high", ["catalogue"], "the temporal type changes", "This is a history table of system-versioning.")
    else:
        it.add("declared", "high", ["catalogue"], "the temporal type changes",
               "The table is not system-versioned, so the source keeps no history of its own.")
    tr = d.get("transition")
    if tr and "rows_from" in tr:
        upd = ", ".join("%s (%d)" % kv for kv in sorted(tr["updated_columns"].items(), key=lambda kv: -kv[1])) or "none"
        it.add("observed", "medium", ["transition"], "every new extract",
               "Between the extracts of 31 May and 1 June 2016: %s inserted, %s deleted, %s updated; columns updated: %s."
               % (format(tr["inserted"], ","), format(tr["deleted"], ","), format(tr["updated"], ","), upd))
    cols = {x["column_name"]: x for x in c["columns"]}
    dt = [n for n, x in cols.items() if x["type_name"] in ("datetime2", "datetime", "datetimeoffset") and n not in ("ValidFrom", "ValidTo")]
    dd = [n for n, x in cols.items() if x["type_name"] == "date"]
    per = [n for n in ("ValidFrom", "ValidTo") if n in cols]
    if dd or dt or per:
        it.add("declared", "high", ["catalogue"], "a column type changes",
               "Date columns: %s; date-and-time columns without a time zone: %s%s." % (
                   ", ".join(dd) or "none", ", ".join(dt) or "none",
                   "; system-time period columns, datetime2 without a zone, set by SQL Server: " + ", ".join(per) if per else ""))
    if zone and dt and not any(x["type_name"] == "datetimeoffset" for x in cols.values()):
        it.add("observed", "unknown", [], "a time zone is found in documentation",
               "The time zone of %s is not established; the catalogue states none." % ", ".join(dt))


def mech_role(it, d):
    tb = d["catalogue"]["table"][0]
    if tb.get("description"):
        it.add("declared", "high", ["catalogue"], "the description changes", "The source describes the table as \"%s\"." % tb["description"].strip())
    out = sorted(set("%s.%s" % (f["ref_schema"], f["ref_table"]) for f in d["catalogue"]["foreign_keys_out"]))
    inn = sorted(set("%s.%s" % (f["schema_name"], f["table_name"]) for f in d["catalogue"]["foreign_keys_in"]))
    it.add("declared", "high", ["catalogue"], "a foreign key changes",
           "It refers to %s and is referred to by %s." % (", ".join(out) or "no table", ", ".join(inn) or "no table"))


def mech_keys(it, d):
    c = d["catalogue"]
    uq = {}
    for k in c["keys"]:
        if k["is_unique"] == "1" and k["is_primary_key"] != "1":
            uq.setdefault(k["index_name"], []).append(k["column_name"])
    if uq:
        it.add("declared", "high", ["catalogue"], "a unique constraint changes",
               "Declared unique besides the primary key: %s." % "; ".join("%s (%s)" % (n, ", ".join(v)) for n, v in sorted(uq.items())))
    p = d["profile"].get("pk")
    if p and "gaps" in p:
        it.add("observed", "high", ["profile"], "the key range changes",
               "The key runs from %s to %s with %s." % (format(p["min"], ","), format(p["max"], ","),
                                                        "no gap" if p["gaps"] == 0 else plural(p["gaps"], "unused number")))
    fks = {}
    for f in c["foreign_keys_out"]:
        fks.setdefault(f["fk_name"], []).append(f)
    if fks:
        bad = [n for n, fs in fks.items() if fs[0]["is_disabled"] == "1" or fs[0]["is_not_trusted"] == "1"]
        it.add("declared", "high", ["catalogue"], "a foreign key changes",
               "%s, %s: %s." % (plural(len(fks), "declared foreign key"),
                                "all enabled and trusted" if not bad else "disabled or untrusted: " + ", ".join(bad),
                                "; ".join("%s -> %s.%s.%s" % (", ".join(x["column_name"] for x in fs), fs[0]["ref_schema"], fs[0]["ref_table"],
                                                              ", ".join(x["ref_column"] for x in fs)) for n, fs in sorted(fks.items()))))


def mech_population(it, d, date_col):
    c, p = d["catalogue"], d["profile"]
    n = p["rows"]
    if date_col:
        s = p["columns"][date_col]
        it.add("observed", "high", ["profile"], "every new extract",
               "%s, with %s from %s to %s." % (plural(n, "row"), date_col, s.get("min", "")[:10], s.get("max", "")[:10]))
    else:
        it.add("observed", "high", ["profile"], "every new extract", "%s in the extract." % plural(n, "row"))
    same = c["rows_seen_by_owner"] == c["rows_seen_by_nsdn_reader"] == c["rows_in_extract"]
    it.add("observed", "high", ["catalogue"], "a security policy or a count difference appears",
           "Extraction visibility (R15): the owner, the read-only account nsdn_reader and the extract each see %s%s."
           % (plural(c["rows_in_extract"], "row"), "" if same else " - NOT the same: owner %s, reader %s" % (c["rows_seen_by_owner"], c["rows_seen_by_nsdn_reader"])))
    if c["masked_columns"]:
        it.add("declared", "high", ["catalogue"], "a masking rule changes",
               "Dynamic data masking hides %s from ordinary readers (%s); the extract, made as owner, holds the unmasked values."
               % (", ".join(m["column_name"] for m in c["masked_columns"]), c["masked_columns"][0]["masking_function"]))
    else:
        it.add("declared", "high", ["catalogue"], "a masking rule appears", "No column is masked.")
    it.add("declared", "unknown", ["catalogue"], "permission to read security policies is granted",
           "Whether a row-level security policy exists is not established: the catalogue shows nsdn_reader none, which it may not be allowed to see; the equal row counts above show none takes effect on this account.")
    if "LastEditedBy" in p["columns"] and "values" in p["columns"]["LastEditedBy"]:
        k = p["columns"]["LastEditedBy"]["values"].get("1")
        if k:
            it.add("observed", "high", ["profile"], "the technical user's share changes",
                   "%s last edited by person 1, Data Conversion Only, a technical user." % plural(k, "row"))


def mech_sensitivity(it, d):
    c = d["catalogue"]
    cols = [x["column_name"] for x in c["columns"]]
    sig = [x for x in cols if SENSITIVE.search(x)]
    if sig:
        it.add("declared", "medium", ["catalogue"], "a column is added or renamed",
               "Columns whose names or descriptions point to personal, contact, location, credential or free-text content: %s." % ", ".join(sig))
    else:
        it.add("declared", "medium", ["catalogue"], "a column is added or renamed",
               "No column name points to personal, contact, location, credential or free-text content.")
    if any(f["column_name"] == "LastEditedBy" and f["ref_table"] == "People" for f in c["foreign_keys_out"]):
        it.add("declared", "high", ["catalogue"], "a foreign key changes",
               "Every row names the person who last edited it (LastEditedBy -> Application.People): attribution of work to identifiable staff, employee data whatever the table's content.")
    ppl = [f["column_name"] for f in c["foreign_keys_out"] if f["ref_table"] == "People" and f["column_name"] != "LastEditedBy"]
    if ppl:
        it.add("declared", "high", ["catalogue"], "a foreign key changes",
               "Columns referring to people in Application.People (names, contact details): %s, besides the audit column LastEditedBy." % ", ".join(ppl))
    if c["masked_columns"]:
        it.add("declared", "high", ["catalogue"], "a masking rule changes",
               "The source masks %s from ordinary readers, a declaration that they are sensitive; the extract holds them unmasked."
               % ", ".join(m["column_name"] for m in c["masked_columns"]))


def mech_peculiarities(it, d):
    p = d["profile"]
    n = p["rows"]
    if p.get("streaming_profile"):
        it.add("observed", "unknown", [], "a full profile is run", "Too large for the full profile; peculiarity tests not run.")
        return
    it.add("observed", "high", ["profile"], "the empty-column patterns change",
           "Test 8: %s distinct pattern%s of empty columns; the most common: %s."
           % (p["empty_patterns_distinct"], "" if p["empty_patterns_distinct"] == 1 else "s",
              "; ".join("%s rows with %s empty" % (format(e["rows"], ","), ", ".join(e["empty"]) or "none") for e in p["empty_patterns"][:3])))
    for col, v in sorted((p.get("empty_rows_by_low_cardinality_value") or {}).items()):
        if p["columns"][col]["distinct"] > max(2, min(12, n // 3)) or col in AUDIT:
            continue
        parts = []
        exact = True
        for val, cnt in sorted(v["rows_per_value"].items(), key=lambda kv: -kv[1]):
            e = v["empty_rows_by_value"]
            always = [o for o, ct in e.items() if ct.get(val) == cnt and o != col]
            never = [o for o, ct in e.items() if ct.get(val) == 0 and o != col]
            mixed = ["%s (%s empty)" % (o, format(ct.get(val), ",")) for o, ct in e.items() if 0 < ct.get(val, 0) < cnt and o != col]
            exact = exact and not mixed
            parts.append("%s=%s (%s rows): empty %s; filled %s%s" % (col, val or "(empty)", format(cnt, ","), ", ".join(always) or "-",
                                                                   ", ".join(never) or "-", "; partly empty " + ", ".join(mixed) if mixed else ""))
        it.add("observed", "high", ["profile"], "the pattern changes",
               "Test 8, by %s%s: %s." % (col, " (exact)" if exact else " (partial)", " | ".join(parts)))
    fds = p.get("functional_dependencies") or []
    if isinstance(fds, list):
        core = [f for f in fds if not (set(x.strip() for x in f.split("->")) & AUDIT)]
        it.add("observed", "high", ["profile"], "a row breaks a dependency",
               "Test 1: %s between non-key columns over the whole extract (%s involving audit columns, a batch-edit signature, not listed)%s"
               % (plural(len(core), "functional dependency"), len(fds) - len(core),
                  (": " + "; ".join(core[:10]) + ("; and %d more in the evidence" % (len(core) - 10) if len(core) > 10 else "") + ".") if core else "."))
    js = [c for c, s in p["columns"].items() if "json" in s]
    geo = [c for c, s in p["columns"].items() if "geometry_rows" in s]
    if js or geo:
        bits = []
        for c in js:
            j = p["columns"][c]["json"]
            bits.append("%s holds JSON in %s rows, %s of which parse" % (c, format(j["rows"], ","), format(j["parsed"], ",")))
        for c in geo:
            bits.append("%s holds geography" % c)
        it.add("observed", "high", ["profile"], "the structured columns change", "Test 6: " + "; ".join(bits) + ".")
    ff = [c for c, s in p["columns"].items() if s.get("far_future") and c != "ValidTo"]
    if ff:
        it.add("observed", "high", ["profile"], "a far-future date appears or disappears",
               "Far-future dates (9999) in %s." % ", ".join(ff))
    td = p.get("column_names_with_trailing_digits") or []
    it.add("observed", "high", ["profile"], "a column is added",
           "Test 16: %s." % ("columns ending in digits, possible repeating groups: " + ", ".join(td) if td else "no column name ends in a digit"))


# --------------------------------------------------------------------------- assembly

ITEMS = [("01", "granularity"), ("03", "temporal"), ("05", "role"), ("06", "keys"), ("07", "population"),
         ("19", "sensitivity"), ("27", "peculiarities")]


def build(table, spec, common):
    with open(os.path.join(PROFILE_DIR, table + ".json"), encoding="utf-8") as f:
        d = json.load(f)
    schema, name = table.split(".", 1)
    base = os.path.join(ROOT, "analysis", "wwi", "tables", ia.escape(schema), ia.escape(name))
    evmap = dict(d["evidence"])
    evmap.update(spec.get("extra_evidence", {}))
    oid = d["catalogue"]["table"][0]["object_id"]
    front0 = dict(common, id="wwi:object:%s" % oid, subject="wwi/tables/%s/%s" % (ia.escape(schema), ia.escape(name)),
                  input_schema_sha256=d["profile"]["schema_sha256"])
    hist = d["catalogue"]["table"][0]["temporal_type_desc"] == "HISTORY_TABLE"
    items = [("05", "role")] if hist else ITEMS + [tuple(x) for x in spec.get("extra_items", [])]
    for nn, slug in items:
        it = Item(nn)
        if nn == "01":
            mech_granularity(it, d)
        elif nn == "03":
            mech_temporal(it, d)
        elif nn == "05":
            mech_role(it, d)
            if hist:
                mech_temporal(it, d, zone=False)
        elif nn == "06":
            mech_keys(it, d)
        elif nn == "07":
            mech_population(it, d, spec.get("date_col"))
        elif nn == "19":
            mech_sensitivity(it, d)
        elif nn == "27":
            mech_peculiarities(it, d)
        s = spec.get(nn, {})
        for cl in s.get("claims", []):
            it.add(*cl)
        front = dict(front0, item=nn, topic=slug, tier="minimum" if nn in ia.MINIMUM or nn == "27" else "best-effort",
                     summary=ascii_only(s.get("summary", "TODO")),
                     recheck_when=ascii_only(s.get("recheck_when", "every new extract, or a schema change")))
        write_item(os.path.join(base, "%s_%s.md" % (nn, slug)), front, it.claims, evmap,
                   s.get("reasoning", "Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence."),
                   s.get("uncertainties", ""), s.get("person", ""))
    for col, cs in spec.get("columns", {}).items():
        cid = next(x["column_id"] for x in d["catalogue"]["columns"] if x["column_name"] == col)
        for nn, slug, cspec in cs:
            it = Item(nn)
            for cl in cspec["claims"]:
                it.add(*cl)
            front = dict(front0, id="wwi:object:%s:column:%s" % (oid, cid),
                         subject="wwi/tables/%s/%s/columns/%s" % (ia.escape(schema), ia.escape(name), ia.escape(col)),
                         item=nn, topic=slug, tier="minimum" if nn in ia.MINIMUM else "best-effort",
                         summary=ascii_only(cspec["summary"]), recheck_when=ascii_only(cspec.get("recheck_when", "every new extract")))
            write_item(os.path.join(base, "columns", ia.escape(col), "%s_%s.md" % (nn, slug)), front, it.claims, evmap,
                       cspec.get("reasoning", ""), cspec.get("uncertainties", ""), cspec.get("person", ""))


def main(argv):
    path = argv[1]
    sp = importlib.util.spec_from_file_location("specs", path)
    mod = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(mod)
    wanted = set(argv[2:])
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from evidence_orders import blob
    versions = "; script blobs: write_dossiers.py %s, profile_tables.py %s, evidence_shared.py %s" % tuple(
        blob("prototypes/information_analysis/%s" % f) for f in ("write_dossiers.py", "profile_tables.py", "evidence_shared.py"))
    mod.COMMON = dict(mod.COMMON, method=mod.COMMON["method"] + versions)
    for table, spec in mod.SPECS.items():
        if wanted and table not in wanted:
            continue
        build(table, spec, mod.COMMON)
        print("wrote", table)


if __name__ == "__main__":
    main(sys.argv)
