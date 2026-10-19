"""Write item 02 (meaning) for every column of every base table (ADR-0018 column folders, ADR-0020 as-is).

Mechanical claims come from the catalogue and profile evidence (declared description, type and keys; observed
filling, range, values). Judgement claims come from a notes module written by the agent, plus fixed readings for the
audit and system-time columns, which the source never describes.

    python prototypes/information_analysis/write_column_meanings.py <notes module> [Schema.Table ...]
"""
import importlib.util
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from write_dossiers import ROOT, PROFILE_DIR, Item, write_item, ascii_only, plural, SENSITIVE  # noqa: E402
import ia_lib as ia  # noqa: E402
from evidence_orders import blob  # noqa: E402

CODE_TYPES = {"int", "bigint", "smallint", "tinyint", "bit", "decimal", "numeric"}
# Fixed readings for the audit and system-time columns, which the source never describes: (type, text, confidence,
# evidence keys). Revised 2026-10-19 after sol's and astra's review: a reading from a name is low; the period columns'
# meaning is declared by the catalogue; what the data shows comes from the editors evidence (claims built in audit()).
AUDIT = {
    "LastEditedBy": ("intended", "By its name and its foreign key to Application.People: the person who last changed the row.", "low", ["catalogue"]),
    "LastEditedWhen": ("intended", "By its name: when the row was last changed.", "low", ["catalogue"]),
    "ValidFrom": ("declared", "The moment this version of the row became current: the period start of SQL Server's system-versioning, which the server sets from its own clock at the time of the change.", "high", ["catalogue"]),
    "ValidTo": ("declared", "The moment this version stopped being current: the period end of system-versioning; a current row carries the maximum value 9999-12-31 23:59:59.9999999.", "high", ["catalogue"]),
}
EXTRA_EVIDENCE = {"editors_and_system_time": "editors", "logon_names": "logon"}


def find_extra(evdir):
    """Evidence written by evidence_shared.py's column mode, found by the function it ran."""
    out = {}
    for f in sorted(os.listdir(evdir)) if os.path.isdir(evdir) else []:
        with open(os.path.join(evdir, f), encoding="utf-8") as fh:
            rec = json.load(fh)
        for fn, key in EXTRA_EVIDENCE.items():
            if (rec.get("code") or "").startswith("def %s(" % fn):
                if key not in out or rec["ran_at"] > out[key][1]:
                    out[key] = (f[:-5], rec["ran_at"], rec["result"])
    return out


def audit(it, col, extra, day):
    """Observed claims on the audit and system-time columns from the editors evidence."""
    ed = extra.get("editors")
    if not ed:
        return
    r = ed[2]
    if col == "LastEditedBy" and "last_edited_by" in r:
        k = r["last_edited_by"]["rows_by_editor_kind"]
        parts = ["%s rows by %s" % (format(v, ","), {"employee": "employees (IsEmployee = 1 in Application.People)",
                                                    "person 1": "person 1, whose FullName is %s" % r["last_edited_by"]["person_1_full_name"],
                                                    "not an employee": "people who are not employees",
                                                    "unknown person": "ids not in Application.People"}[n]) for n, v in sorted(k.items(), key=lambda x: -x[1])]
        it.add("observed", "high", ["editors"], "every new extract",
               "%s distinct editors: %s." % (r["last_edited_by"]["distinct_editors"], "; ".join(parts)))
    if col == "ValidFrom" and "valid_from" in r:
        v = r["valid_from"]
        if v["rows_after_the_extract_day"]:
            it.add("observed", "high", ["editors"], "every new extract",
                   "%s row(s) carry a ValidFrom after the extract's simulated date %s (latest %s): here system time is the clock of the change, not the simulated business time." % (v["rows_after_the_extract_day"], day, v["max"][:19]))
        else:
            it.add("observed", "high", ["editors"], "every new extract",
                   "Every ValidFrom lies on or before the extract's simulated date %s (from %s to %s)." % (day, v["min"][:19], v["max"][:19]))


def mech(it, d, col):
    c = d["catalogue"]
    x = next(r for r in c["columns"] if r["column_name"] == col)
    s = d["profile"]["columns"].get(col, {})
    n = d["profile"]["rows"]
    desc = (x.get("description") or "").strip()
    if desc:
        it.add("declared", "medium", ["catalogue"], "the description changes",
               "The source describes it as \"%s\" (declared, not verified against behaviour beyond the claims below)." % desc)
    elif col not in AUDIT:
        it.add("declared", "unknown", ["catalogue"], "a description or documentation is found", "The source gives no description.")
    t = x["type_name"]
    if t in ("nvarchar", "varchar", "varbinary", "nchar", "char"):
        ln = int(x["max_length"])
        t += "(max)" if ln == -1 else "(%d)" % (ln // 2 if t.startswith("n") else ln)
    elif t in ("decimal", "numeric"):
        t += "(%s,%s)" % (x["precision"], x["scale"])
    bits = [t, "nullable" if x["is_nullable"] == "1" else "not nullable"]
    if x["is_identity"] == "1":
        bits.append("identity")
    if x["is_computed"] == "1":
        bits.append("computed")
    if x["is_masked"] == "1":
        bits.append("masked for ordinary readers")
    g = x.get("generated_always_type_desc") or ""
    if g.startswith("AS_ROW"):
        bits.append("system-time " + ("period start" if "START" in g else "period end"))
    it.add("declared", "high", ["catalogue"], "a column type changes", "Declared as %s." % ", ".join(bits))
    pk = [k for k in c["keys"] if k["is_primary_key"] == "1" and k["column_name"] == col]
    if pk:
        refs = sorted(set("%s.%s.%s" % (f["schema_name"], f["table_name"], f["column_name"]) for f in c["foreign_keys_in"]
                          if f["ref_column"] == col))
        it.add("declared", "high", ["catalogue"], "a key changes",
               "Part of the primary key %s%s." % (pk[0]["index_name"], "; referred to by " + ", ".join(refs) if refs else ""))
    for f in c["foreign_keys_out"]:
        if f["column_name"] == col:
            it.add("declared", "high", ["catalogue"], "a foreign key changes",
                   "Refers to %s.%s.%s (%s, %s)." % (f["ref_schema"], f["ref_table"], f["ref_column"], f["fk_name"],
                                                     "enabled and trusted" if f["is_disabled"] == "0" and f["is_not_trusted"] == "0" else "disabled or untrusted"))
    if not s:
        return
    filled = n - s["empty"]
    parts = ["filled on %s of %s" % (format(filled, ","), plural(n, "row")), plural(s["distinct"] - (1 if s["empty"] else 0), "distinct value")]
    if "numeric" in s:
        nu = s["numeric"]
        fmt = lambda v: format(int(v), ",") if float(v).is_integer() else str(v)
        parts.append("from %s to %s" % (fmt(nu["min"]), fmt(nu["max"])))
        if nu["negative"]:
            parts.append("%s negative" % format(nu["negative"], ","))
    if "time_parts" in s:
        parts.append("from %s to %s" % (s.get("min", "")[:19], s.get("max", "")[:19]))
        if s.get("time_parts_distinct") == 1 and list(s["time_parts"])[0] == "T00:00:00":
            parts.append("always at midnight")
    if "json" in s:
        parts.append("JSON on %s rows, %s parse" % (format(s["json"]["rows"], ","), format(s["json"]["parsed"], ",")))
    if "geometry_rows" in s:
        parts.append("geography values")
    safe = x["type_name"] in CODE_TYPES and not SENSITIVE.search(col)
    if s["distinct"] == 1 and filled == n and safe and "values" in s:
        parts.append("the same value in every row: %s" % list(s["values"])[0])
    elif s["distinct"] <= 6 and safe and "values" in s and "time_parts" not in s:
        parts.append("values " + ", ".join("%s (%s)" % (v or "empty", format(k, ",")) for v, k in s["values"].items()))
    it.add("observed", "high", ["profile"], "every new extract", ascii_only("Observed: %s." % "; ".join(parts)))
    if filled == 0:
        it.add("observed", "high", ["profile"], "the column fills", "Always empty in this extract, so the declared meaning cannot be observed.")


def main(argv):
    sp = importlib.util.spec_from_file_location("notes", argv[1])
    notes = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(notes)
    wanted = set(argv[2:])
    method = notes.METHOD + "; script blob write_column_meanings.py %s" % blob("prototypes/information_analysis/write_column_meanings.py")
    count = 0
    for f in sorted(os.listdir(PROFILE_DIR)):
        table = f[:-5]
        if wanted and table not in wanted:
            continue
        with open(os.path.join(PROFILE_DIR, f), encoding="utf-8") as fh:
            d = json.load(fh)
        tb = d["catalogue"]["table"][0]
        if tb["temporal_type_desc"] == "HISTORY_TABLE":
            continue
        schema, name = table.split(".", 1)
        base = os.path.join(ROOT, "analysis", "wwi", "tables", ia.escape(schema), ia.escape(name))
        evmap = dict(d["evidence"])
        evmap.update(notes.EVIDENCE.get(table, {}))
        evmap["doc"] = notes.DOC
        extra = find_extra(os.path.join(base, "evidence"))
        evmap.update({k: v[0] for k, v in extra.items()})
        for x in d["catalogue"]["columns"]:
            col = x["column_name"]
            if (table, col) in notes.SKIP:
                continue
            it = Item("02")
            mech(it, d, col)
            note = notes.NOTES.get((table, col), {})
            if col in AUDIT and not note.get("replace_audit"):
                typ, text, conf, ev = AUDIT[col]
                it.add(typ, conf, ev, "a description is found", text)
            if col in AUDIT:
                audit(it, col, extra, notes.COMMON["input_extract"])
            for cl in note.get("claims", []):
                it.add(*cl)
            summary = note.get("summary")
            if not summary:
                summary = (x.get("description") or "").strip() or (AUDIT[col][1] if col in AUDIT else "No description; see the claims.")
            front = dict(notes.COMMON, method=method, id="wwi:object:%s:column:%s" % (tb["object_id"], x["column_id"]),
                         subject="wwi/tables/%s/%s/columns/%s" % (ia.escape(schema), ia.escape(name), ia.escape(col)),
                         input_schema_sha256=d["profile"]["schema_sha256"], item="02", topic="meaning", tier="best-effort",
                         summary=ascii_only(summary), recheck_when=ascii_only(note.get("recheck_when", "the description changes, or every new extract")))
            write_item(os.path.join(base, "columns", ia.escape(col), "02_meaning.md"), front, it.claims, evmap,
                       note.get("reasoning", "Mechanical claims from the catalogue and profile; any reading is the writer's, with its confidence."),
                       note.get("uncertainties", ""), "")
            count += 1
    print("wrote", count, "column meaning files")


if __name__ == "__main__":
    main(sys.argv)
