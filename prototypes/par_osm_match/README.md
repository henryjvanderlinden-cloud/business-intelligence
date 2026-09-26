# PAR–OSM match

Answers one question: for each OpenStreetMap business in Utrecht province, which establishment in the
province's jobs register (PAR) is it, judged by location and sector alone?

`python match.py <par.csv> <osm.csv> crosswalk.json 30 <out.csv>`, plain Python. The radius and the
sector crosswalk are the only judgement in it; both are logged as decisions (S06-074, S06-075) in
[`../../records/steps/S06.jsonl`](../../records/steps/S06.jsonl). The blind answer key drawn from its
output is TI-005 in [`../../records/task_instances.jsonl`](../../records/task_instances.jsonl).
