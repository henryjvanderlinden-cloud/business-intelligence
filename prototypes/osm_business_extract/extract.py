import osmium, csv, sys, collections
from pyproj import Transformer
T = Transformer.from_crs("EPSG:4326", "EPSG:28992", always_xy=True)
SRC = sys.argv[1]; OUT = sys.argv[2]
KEYS = ["shop", "office", "craft", "healthcare", "amenity", "tourism", "leisure", "industrial", "company"]
AMENITY_SKIP = set("""parking bench bicycle_parking waste_basket recycling toilets drinking_water post_box
vending_machine charging_station shelter telephone fountain clock bbq hunting_stand parking_entrance
parking_space motorcycle_parking atm waste_disposal grit_bin letter_box bicycle_repair_station
compressed_air water_point give_box public_bookcase lounger picnic_table dog_toilet table
parcel_locker device_charging_station ticket_validator watering_place feeding_place loading_dock
bicycle_rental car_sharing taxi bus_station ferry_terminal grave_yard""".split())
TOURISM_KEEP = {"hotel", "hostel", "guest_house", "motel", "apartment", "museum", "camp_site", "chalet", "attraction", "gallery", "zoo", "theme_park", "information"}
LEISURE_KEEP = {"fitness_centre", "sports_centre", "dance", "bowling_alley", "escape_game", "amusement_arcade", "sauna", "water_park", "golf_course", "horse_riding", "marina", "indoor_play", "trampoline_park", "adult_gaming_centre", "hackerspace"}
FIELDS = ["osm_type", "osm_id", "name", "cat_key", "cat_value", "brand", "operator", "website",
          "addr_street", "addr_housenumber", "addr_postcode", "addr_city", "ref_kvk",
          "lat", "lon", "rd_x", "rd_y", "n_business_keys"]
def classify(t):
    hits = []
    for k in KEYS:
        v = t.get(k)
        if not v: continue
        if k == "amenity" and v in AMENITY_SKIP: continue
        if k == "tourism" and v not in TOURISM_KEEP: continue
        if k == "leisure" and v not in LEISURE_KEEP: continue
        hits.append((k, v))
    return hits
stats = collections.Counter()
class H(osmium.SimpleHandler):
    def __init__(s, w): super().__init__(); s.w = w
    def emit(s, typ, o, lat, lon):
        t = {k: v for k, v in o.tags}
        stats["tagged_seen"] += 1
        hits = classify(t)
        if not hits: return
        if not t.get("name"):
            stats["business_no_name"] += 1; return
        k, v = hits[0]
        x, y = T.transform(lon, lat)
        kvk = t.get("ref:kvk") or t.get("kvk") or t.get("ref:KvK") or ""
        s.w.writerow([typ, o.id, t["name"], k, v, t.get("brand", ""), t.get("operator", ""),
                      t.get("website") or t.get("contact:website") or "",
                      t.get("addr:street", ""), t.get("addr:housenumber", ""), t.get("addr:postcode", ""),
                      t.get("addr:city", ""), kvk, round(lat, 7), round(lon, 7), round(x, 2), round(y, 2), len(hits)])
        stats["written_" + typ] += 1
    def node(s, n):
        if len(n.tags) == 0 or not n.location.valid(): return
        s.emit("node", n, n.location.lat, n.location.lon)
    def way(s, w):
        if len(w.tags) == 0: return
        pts = [(nd.location.lat, nd.location.lon) for nd in w.nodes if nd.location.valid()]
        if not pts: stats["way_no_loc"] += 1; return
        lat = sum(p[0] for p in pts) / len(pts); lon = sum(p[1] for p in pts) / len(pts)
        s.emit("way", w, lat, lon)
with open(OUT, "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh); w.writerow(FIELDS)
    H(w).apply_file(SRC, locations=True, idx="flex_mem")
print(dict(stats))
