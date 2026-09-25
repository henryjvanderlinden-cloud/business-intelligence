# OSM business extract

Answers one question: which named features in the OpenStreetMap Utrecht extract plausibly host paid
work, and where are they, in the coordinate system of the province's jobs register (PAR, EPSG:28992)?

`python extract.py <utrecht.osm.pbf> <out.csv>` needs `osmium` and `pyproj`, which install in the cloud
workspace but not on the author's machine's shell. Phone numbers and e-mail addresses are deliberately not
extracted. The choice of which tags count as business is a decision, recorded as step S06-066 in
[`../../records/steps/S06.jsonl`](../../records/steps/S06.jsonl).
