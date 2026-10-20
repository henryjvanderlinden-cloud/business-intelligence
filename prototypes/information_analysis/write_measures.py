"""Write items 8 (measures), 9 (derived columns) and 28 (arithmetic policy) per table from measures.py's evidence.

Item 8 gets one mechanical claim per numeric column (type, filling, range, signs, decimals used), then the reader's
claims from a notes module. Items 9 and 28 are written only where the notes module has claims for them. A claim in
the notes module is (type, confidence, uses the evidence, recheck, text), where text may be a function of the
column profiles C and the tests T, so that every number in it is read from the evidence.

    python prototypes/information_analysis/write_measures.py <notes module> [<source>, default wwi]
"""
import importlib.util
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from evidence_orders import blob  # noqa: E402
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import ia_lib as ia  # noqa: E402

TOOL = "prototypes/information_analysis/measures.py"
TOPIC = {"08": "measures", "09": "derived", "28": "arithmetic"}


def n(x):
    try:
        v = float(x)
    except (TypeError, ValueError):
        return str(x)
    return format(int(v), ",") if v.is_integer() and "." not in str(x) else str(x)


def column_claim(c, v):
    rng = "range %s to %s" % (v["min"], v["max"]) if v["filled"] else "never filled"
    signs = "%s negative, %s zero, %s positive" % (n(v["negative"]), n(v["zero"]), n(v["positive"]))
    vals = "; values %s" % ", ".join("%s (%s)" % (k, n(m)) for k, m in v["values"].items()) if v.get("values") else ""
    by = ""
    if v.get("sign_by_transaction_type"):
        by = "; by transaction type: %s" % "; ".join("%s %s" % (k, ", ".join("%s %s" % (s, n(m)) for s, m in sorted(x.items())))
                                                       for k, x in v["sign_by_transaction_type"].items())
    return ("%s: %s(%s,%s), filled on %s of %s rows, %s; %s; at most %s decimal(s) used%s%s." % (
        c, v["type"], v["precision"], v["scale"], n(v["filled"]), n(v["rows"]), rng, signs, v["max_decimals_used"],
        "" if v["type"] not in ("decimal", "numeric") or v["scale"] == 0 else ", %s non-integer value(s)" % n(v["non_integer"]), vals + by))


def latest(ev_dir):
    best = None
    for f in os.listdir(ev_dir):
        with open(os.path.join(ev_dir, f), encoding="utf-8") as fh:
            rec = json.load(fh)
        if rec.get("tool") == TOOL and (best is None or rec["ran_at"] > best["ran_at"]):
            best = rec
    return best


def main(argv):
    sp = importlib.util.spec_from_file_location("notes", argv[1])
    notes = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(notes)
    source = argv[2] if len(argv) > 2 else "wwi"
    written = 0
    for t, spec in notes.TABLES.items():
        s, nm = t.split(".")
        d = os.path.join(ROOT, "analysis", source, "tables", ia.escape(s), ia.escape(nm))
        rec = latest(os.path.join(d, "evidence"))
        h, C, T = rec["id"], rec["result"]["columns"], rec["result"]["tests"]
        prof = json.load(open(os.path.join(ROOT, "scratch", "ia_profile", t + ".json")))
        method = "measures by %s (blob %s), claims by write_measures.py (blob %s); readings by %s" % (
            TOOL, rec["tool_version"], blob("prototypes/information_analysis/write_measures.py"), notes.COMMON["written_by"])
        for item in ("08", "09", "28"):
            claims = []
            if item == "08":
                claims = [("observed", "high", True, "every new extract", column_claim(c, v)) for c, v in C.items()]
            claims += spec.get(item, [])
            if not claims:
                continue
            lines = []
            for i, (typ, cf, ev, rc, txt) in enumerate(claims, 1):
                txt = txt(C, T) if callable(txt) else txt
                lines.append("- C%d | type=%s | status=proposed | confidence=%s | effective=%s | observed=%s | checked=%s | evidence=%s | recheck=%s | text: %s"
                             % (i, typ, cf, rec["inputs"]["extract"], notes.NOW[:10], notes.NOW[:10], h if ev else "none", rc, txt))
            conf = ia.CONFIDENCE[min(ia.CONFIDENCE.index(c[1]) for c in claims)]
            front = dict(notes.COMMON, id="%s:object:%s" % (source, prof["catalogue"]["table"][0]["object_id"]),
                         subject="%s/tables/%s/%s" % (source, ia.escape(s), ia.escape(nm)), item=item, topic=TOPIC[item],
                         tier="best-effort", summary=spec["summary" + item], confidence=conf, claims=str(len(claims)), method=method,
                         input_extract=rec["inputs"]["extract"], input_manifest_sha256=rec["inputs"]["manifest_sha256"],
                         input_schema_sha256=prof["profile"]["schema_sha256"], last_checked_against=rec["inputs"]["extract"],
                         recheck_when="every new extract, or a schema change")
            txt = ("---\n" + "\n".join("%s: %s" % (k, front[k]) for k in ia.FRONT_KEYS) + "\n---\n\n## Claims\n\n" + "\n".join(lines) +
                   "\n\n## Reasoning\n\n" + spec.get("reasoning" + item, notes.REASONING[item]) + "\n\n## Uncertainties\n\n" +
                   (spec.get("uncertain" + item) or "None.") + "\n\n## For a person\n\nNone.\n")
            assert all(ord(ch) < 128 for ch in txt), (t, item)
            with open(os.path.join(d, "%s_%s.md" % (item, TOPIC[item])), "w", encoding="ascii", newline="\n") as f:
                f.write(txt)
            written += 1
    print("wrote", written, "files")


if __name__ == "__main__":
    main(sys.argv)
