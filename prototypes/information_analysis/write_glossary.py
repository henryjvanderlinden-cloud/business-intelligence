"""Write round-2 terms (item 25) and entities (item 26) under analysis/wwi/across/ (analysis/README.md section 9).

These files measure nothing new: each claim reads findings that other files own and links to them (path#Cn), as the
manual's "each fact is stated once" asks; their evidence is therefore none and their confidence is that of the reading.
The content is the agent's, from a notes module.

    python prototypes/information_analysis/write_glossary.py <notes module>
"""
import importlib.util
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from evidence_orders import blob  # noqa: E402
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import ia_lib as ia  # noqa: E402

ACROSS = os.path.join(ROOT, "analysis", "wwi", "across")
DAY = "2016-06-01"


def main(argv):
    sp = importlib.util.spec_from_file_location("notes", argv[1])
    notes = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(notes)
    method = ("readings by %s linking the claims that own each fact; written by %s (blob %s)"
              % (notes.COMMON["written_by"], "prototypes/information_analysis/write_glossary.py", blob("prototypes/information_analysis/write_glossary.py")))
    count = 0
    for kind, nn, topic, entries in (("terms", "25", "terms", notes.TERMS), ("entities", "26", "entities", notes.ENTITIES)):
        for slug, e in entries.items():
            claims = e["claims"]
            conf = ia.CONFIDENCE[min(ia.CONFIDENCE.index(c[1]) for c in claims)]
            lines = ["- C%d | type=%s | status=proposed | confidence=%s | effective=%s | observed=%s | checked=%s | evidence=none | recheck=%s | text: %s"
                     % (i, typ, cf, DAY, notes.NOW[:10], notes.NOW[:10], rc, t) for i, (typ, cf, rc, t) in enumerate(claims, 1)]
            front = dict(notes.COMMON, id="wwi:%s:%s" % (kind[:-1] if kind != "entities" else "entity", slug),
                         subject="wwi/across/%s/%s" % (kind, slug), item=nn, topic=topic, tier="best-effort", summary=e["summary"],
                         confidence=conf, claims=str(len(claims)), method=method, input_schema_sha256="none",
                         recheck_when="a linked claim changes")
            txt = ("---\n" + "\n".join("%s: %s" % (k, front[k]) for k in ia.FRONT_KEYS) + "\n---\n\n## Claims\n\n" + "\n".join(lines) +
                   "\n\n## Reasoning\n\n" + e.get("reasoning", "Each claim links the files that own the facts it reads.") +
                   "\n\n## Uncertainties\n\n" + (e.get("uncertainties") or "None.") + "\n\n## For a person\n\n" + (e.get("person") or "None.") + "\n")
            assert all(ord(ch) < 128 for ch in txt), slug
            d = os.path.join(ACROSS, kind, slug)
            os.makedirs(d, exist_ok=True)
            with open(os.path.join(d, "%s_%s.md" % (nn, topic)), "w", encoding="ascii", newline="\n") as f:
                f.write(txt)
            count += 1
    print("wrote", count, "term and entity files")


if __name__ == "__main__":
    main(sys.argv)
