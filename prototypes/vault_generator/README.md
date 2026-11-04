# The vault generator

**Question.** Can the raw vault declared in `model/` be generated as plain-SQL dbt models that load the sandbox's
daily extracts in DuckDB deterministically, idempotently and append-only, with every delivered version
reconstructable? ([143](../../docs/10_architecture/143_the-vault-generator.md), ADR-0032, ADR-0037.)

**Answer, first evidence (2026-11-04, session 12).** Yes for four source tables (`scope.txt`): 35 raw-vault tables and
their staging views, loaded from the three kept extracts (2016-05-31 to 06-02). In the cloud suite all five checks
pass: a clean three-day load with every generated test passing; loading the last extract twice changes no row; a
batch that fails halfway with a wrong model leaves nothing once rebuilt; every one of 158,011 delivered versions
reconstructs exactly from the satellites (a planted defect is caught); a constructed late arrival is followed by the
restatement of the next version. Not yet run on the author's machine at the time of writing.

## The pieces

- `generate.py` — reads the declarations, the source file and the catalogue; writes `models/staging/wwi/`,
  `models/raw_vault/` and `tests/generated/` in `prototypes/wwi_sandbox/dbt/`. Standard library only, deterministic,
  no dates in any file. `--check` fails on a missing, edited or stray generated file.
- `templates/` — one SQL template per kind (Python `string.Template`; `$name` is the generator's, `{{ }}` is dbt's).
- `scope.txt` — the source tables generated so far. A pattern not yet supported stops the generator (143 §13 item 4).
- `test_load.py` — the cloud suite. Lands extracts with the runner's own code and profile and runs `dbt build` as
  the runner does. `python test_load.py --root <repo> --extracts <dir with dated extract folders>`; a folder may hold
  only the files of the tables in scope.

Run the generator, then the suite, then commit the generated files with the generator's change: the runner takes the
dbt project live within a minute (143 §9 item 3). Needs dbt-core 1.12.5, dbt-duckdb 1.11.0 and DuckDB 1.5.6, the
runner's versions.
