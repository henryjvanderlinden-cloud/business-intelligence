"""Propose PAR establishments for OSM businesses by distance and sector (S06-076).

Deterministic: the only judgement is in crosswalk.json and the radius, both logged as decisions.
Usage: python match.py <par.csv> <osm.csv> <crosswalk.json> <radius_m> <out.csv>
"""
import csv, json, math, sys, collections
par_path, osm_path, cw_path, radius, out_path = sys.argv[1], sys.argv[2], sys.argv[3], float(sys.argv[4]), sys.argv[5]
cw = json.load(open(cw_path, encoding="utf-8"))
par = []
for r in csv.DictReader(open(par_path, encoding="utf-8")):
    x, y = r["SHAPE"][7:-1].split()
    par.append((float(x), float(y), r))
C = radius; grid = collections.defaultdict(list)
for i, (x, y, _) in enumerate(par):
    grid[(int(x // C), int(y // C))].append(i)
def allowed(key, value):
    return cw["values"].get("%s=%s" % (key, value), cw["defaults"].get(key, ["ANY"]))
FIELDS = ["osm_type", "osm_id", "name", "cat_key", "cat_value", "addr_street", "addr_housenumber", "addr_postcode",
          "addr_city", "website", "match_class", "weak_sector", "n_within", "n_compatible", "par_fid", "distance_m",
          "second_distance_m", "par_sbi_section", "par_sbi_class", "par_size_code", "par_start", "par_place"]
stats = collections.Counter(); par_hits = collections.Counter()
with open(out_path, "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh); w.writerow(FIELDS)
    for o in csv.DictReader(open(osm_path, encoding="utf-8")):
        secs = allowed(o["cat_key"], o["cat_value"])
        base = [o[f] for f in FIELDS[:10]]
        if secs == []:
            stats["excluded"] += 1; continue
        x, y = float(o["rd_x"]), float(o["rd_y"]); cx, cy = int(x // C), int(y // C)
        near = []
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                for i in grid.get((cx + dx, cy + dy), ()):
                    d = math.hypot(par[i][0] - x, par[i][1] - y)
                    if d <= radius: near.append((d, i))
        near.sort()
        weak = "ANY" in secs
        comp = [(d, i) for d, i in near if weak or par[i][2]["SBI_SECTIE"] in secs]
        if not near: cls = "no-candidate"
        elif not comp: cls = "sector-mismatch"
        elif len(comp) == 1: cls = "unique"
        else: cls = "ambiguous"
        stats[cls + ("-weak" if weak and comp else "")] += 1
        best = comp[0] if comp else (near[0] if near else None)
        row = base + [cls, int(weak), len(near), len(comp)]
        if best:
            p = par[best[1]][2]
            if comp: par_hits[p["FID"]] += 1
            row += [p["FID"], round(best[0], 1), round(comp[1][0], 1) if len(comp) > 1 else "", p["SBI_SECTIE"],
                    p["SBI_KLASS2"], p["GRTKLASN"], p["DATUMSTART"][:10], p["PLAATSLANG"]]
        else:
            row += [""] * 8
        w.writerow(row)
stats["par_claimed_by_more_than_one_osm"] = sum(1 for v in par_hits.values() if v > 1)
stats["distinct_par_proposed"] = len(par_hits)
print(json.dumps(dict(sorted(stats.items())), indent=1))
