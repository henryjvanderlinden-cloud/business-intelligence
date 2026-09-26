"""Check PAR-OSM proposals against sector registers (S06-112).

For OSM businesses at an address that a sector register lists (postcode + house number), the register
confirms the kind of business there. The check asks whether the matcher's proposal, under the
unique-only policy, points at a PAR establishment of that kind. For childcare the register also gives a
registration date: a centre registered after PAR's reference date (1 April 2022) cannot be in PAR, so
any proposal for it is wrong by construction. Home-based childminders (VGO) and agencies (GOB) are
excluded: their addresses are private homes. No personal columns are read.
Usage: python check.py <repo root>
"""
import csv, os, re, sys, collections, datetime
R = sys.argv[1]
def pc(s): return re.sub(r"[^0-9A-Z]", "", (s or "").upper())
def num(s):
    m = re.match(r"\s*(\d+)", s or ""); return m.group(1) if m else ""
REF = datetime.date(2022, 4, 1)
reg = collections.defaultdict(dict)   # (postcode, number) -> {register: info}
for r in csv.DictReader(open(os.path.join(R, "data/raw/LRK/export_opendata_lrk.csv"), encoding="utf-8", errors="replace"), delimiter=";"):
    if r["type_oko"] not in ("KDV", "BSO"): continue
    m = re.search(r"(\d+)\D*$", r["opvanglocatie_adres"].strip()) or re.search(r"\s(\d+)", r["opvanglocatie_adres"])
    key = (pc(r["opvanglocatie_postcode"]), m.group(1) if m else "")
    d = datetime.datetime.strptime(r["inschrijfdatum"], "%d-%m-%Y").date()
    prev = reg[key].get("LRK")
    reg[key]["LRK"] = min(prev, d) if prev else d          # oldest registration at the address
for f in ("dcc9c9a5-6d01-410b-967f-810557588ba4.csv", "5187f8d5-ff9c-4284-8e06-4311f0354956.csv"):
    for r in csv.DictReader(open(os.path.join(R, "data/raw/DUO", f), encoding="utf-8", errors="replace")):
        if r["PROVINCIE"] == "Utrecht": reg[(pc(r["POSTCODE"]), num(r["HUISNUMMER-TOEVOEGING"]))]["DUO"] = True
for r in csv.DictReader(open(os.path.join(R, "data/raw/RDW/Open_Data_RDW__Erkende_Bedrijven_20260926.csv"), encoding="utf-8", errors="replace")):
    reg[(pc(r["Postcode numeriek"].replace(".", "") + r["Postcode alfanumeriek"]), num(r["Huisnummer"]))]["RDW"] = True
TARGET = {
 "LRK": {"osm": {"amenity=childcare", "amenity=kindergarten"}, "par": {"Kinderopvang en peuterspeelzaalwerk"}},
 "DUO": {"osm": {"amenity=school"}, "par": {"Primair en speciaal onderwijs", "Algemeen vormend voortgezet onderwijs"}},
 "RDW": {"osm": {"shop=car", "shop=car_repair", "shop=motorcycle", "shop=tyres", "shop=car_parts"},
         "par": {"Handel in en reparatie van personenauto's", "Gespecialiseerde reparatie van auto's",
                 "Handel in en reparatie v. motorfietsen en onderdelen daarvan", "Detailhandel in auto-onderdelen en -accessoires",
                 "Handel in en reparatie van zwaardere bedrijfsauto's"}}}
out = collections.defaultdict(collections.Counter)
dates = []
for r in csv.DictReader(open(os.path.join(R, "data/derived/match/par_osm_candidates_v3.csv"), encoding="utf-8")):
    cat = r["cat_key"] + "=" + r["cat_value"]
    info = reg.get((pc(r["addr_postcode"]), num(r["addr_housenumber"])), {})
    for name, t in TARGET.items():
        if cat not in t["osm"]: continue
        o = out[name]; o["osm_in_category"] += 1
        if name not in info: continue
        o["confirmed_by_register"] += 1
        proposed = r["match_class"].startswith("unique")
        post = name == "LRK" and info["LRK"] > REF
        if post: o["registered_after_PAR_date"] += 1
        if not proposed:
            o["abstained" + ("_post" if post else "")] += 1
        elif r["par_sbi_class"] in t["par"]:
            o["proposed_right_kind" + ("_post" if post else "")] += 1
            if name == "LRK" and not post and r["par_start"]:
                dates.append((info["LRK"], datetime.date.fromisoformat(r["par_start"])))
        else:
            o["proposed_wrong_kind" + ("_post" if post else "")] += 1
for name, o in out.items():
    print(name, dict(o))
# date agreement for childcare proposals (PAR 1985-05-01 is a floor value for old establishments)
agree = sum(1 for l, p in dates if abs((l - p).days) <= 366)
floor = sum(1 for l, p in dates if p == datetime.date(1985, 5, 1))
print("LRK date check: proposals", len(dates), "within one year", agree, "PAR floor date 1985-05-01", floor)
