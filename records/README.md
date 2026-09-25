# Records

The project's step log: what was done, by whom, in what role, at what cost and with what result, recorded
as it happens so that a post-mortem can test the project's hypotheses against the work itself.

The specification is [520_record-keeping.md](../docs/50_process/520_record-keeping.md); the decision is
[ADR-0014](../docs/20_decisions/0014-step-log.md).

| File | Grain |
|---|---|
| [`vocabulary.json`](vocabulary.json) | allowed values for every classified field, and the known agents |
| [`sessions.jsonl`](sessions.jsonl) | one working session |
| [`sources.jsonl`](sources.jsonl) | one data source considered, used or rejected |
| `steps/<session>.jsonl` | one step |

Validated by `python tools/check_repo.py`. Load for analysis with, for example, DuckDB:
`select actor, work_class, count(*) from read_json_auto('records/steps/*.jsonl') group by all`.
