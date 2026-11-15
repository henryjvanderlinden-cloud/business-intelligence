# The vault generator

**Question.** Can the raw vault declared in `model/` be generated as plain-SQL dbt models that load the sandbox's
daily extracts in DuckDB deterministically, idempotently and append-only, with every delivered version
reconstructable? ([143](../../docs/10_architecture/143_the-vault-generator.md), ADR-0032, ADR-0037.)

**Answer, first evidence (2026-11-04, session 12).** Yes for four source tables (the first `scope.txt`): 35 raw-vault tables and
their staging views, loaded from the three kept extracts (2016-05-31 to 06-02). In the cloud suite all five checks
pass: a clean three-day load with every generated test passing; loading the last extract twice changes no row; a
batch that fails halfway with a wrong model leaves nothing once rebuilt; every one of 158,011 delivered versions
reconstructs exactly from the satellites (a planted defect is caught); a constructed late arrival is followed by the
restatement of the next version. **On the author's machine** (2026-11-04, 13:07 to 13:12 UTC), after the old warehouse was set aside as `data/warehouse_pre-vault_2026-11-04/`, the runner replayed the three extracts with the generated project (123 tests passing per load, 74 to 104 s each) and published a vault identical, table by table and row by row, to the cloud suite's clean load.

**Second evidence (2026-11-04, evening): all 31 base tables.** After sol's second review
([XREV](../../docs/30_research/notes/XREV_2026-11-04_143-generated-sql_sol.md)) and its fixes (143 §13 items 5 to 8),
the generator 0.2.0 writes the whole WWI raw vault: 216 tables, 510 files, 777 tests per load. The cloud suite, on
the three complete extracts, passes all eight checks: the five above, a failed rebuild of a date that had succeeded,
a deletion closed by the source, and a table delivered empty; 5,360,224 delivered versions reconstruct exactly. A
load takes about 3 to 6 minutes in the cloud workspace. **On the author's machine** (2026-11-04, 17:58 to 18:37 UTC),
with the 0.1.0 warehouse set aside as `data/warehouse_vault-0.1.0_2026-11-04/`, the runner replayed the three
extracts: every load ok with all tests passing, in 522, 893 and 905 seconds, and the published vault equals the
cloud suite's clean load in all 216 tables (17,346,219 rows; content fingerprints without `load_run`).

**Third evidence (2026-11-15): generator 0.3.0 reads engine-kept histories from a watermark**
([equivalence/030](../../docs/30_research/equivalence/030_incremental-capture.md) §7). In the cloud workspace a day
loads in about 105 seconds instead of 320; the five-day vault equals the full-read vault in all 216 tables; the eight
checks pass. The whole history is still read on the first load, on Sundays and with `--vars '{full_history: true}'`.

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
