# Catalogue pass for PostgreSQL

**Question.** Can the structural part of an information analysis (129, items 05 and 06, the catalogue facts of 02) be
taken from any PostgreSQL database with nothing installed on the database side, written into an analysis record in the
shape the Wide World Importers record uses, and navigated in the schema viewer before any model exists?

Written in session S11 for the author's first client, a PostgreSQL database of about 100 tables with two further
sources delivering daily extracts. Tested against the reference case: `test_against_wwi.py` rebuilds the structure of
WWI's 48 tables in PostgreSQL from WWI's own catalogue evidence and checks that the pass gives it back (48 tables, 557
columns, 48 keys, 98 foreign-key columns, 280 descriptions), plus a view, a trigger, a partition, a unique expression
index and a `NULLS NOT DISTINCT` index, with the pass run as a login that may read no table. Reviewed on sol, which
failed the first version ([XREV](../../docs/30_research/notes/XREV_2026-10-29_catalogue-pass_sol.md)); the corrections
are tested but unreviewed. Tested on PostgreSQL 16 only.

## What it reads, and what it does not

`catalogue_postgres.sql` reads only the system catalogue, in a read-only transaction: schemas, tables, views,
partitions, columns with types, nullability, defaults, identity and generated columns, primary keys, unique
constraints and unique indexes, foreign keys, check constraints, triggers, view definitions and the tables each view
reads, comments, and the planner's estimated row counts. It reads **no row of any user table**, so it puts no load on
a production database beyond a few catalogue queries, and it holds no business data. What it writes is still the
client's metadata: table and column names and comments can be confidential, and whether they may leave the client's
premises, or be read by a model, is the client's decision.

## Running it at a client

1. In an empty folder, as any login that may connect; it needs no privilege on the tables, so ask for the least the
   client allows:

   ```
   psql -X -v ON_ERROR_STOP=1 -h <host> -p <port> -U <user> -d <database> -f <nsdn>/prototypes/catalogue_pass/catalogue_postgres.sql
   ```

   It writes `manifest.csv`, `tables.csv`, `columns.csv`, `keys.csv`, `foreign_keys.csv`, `checks.csv`,
   `triggers.csv`, `views.csv` and `view_dependencies.csv`. The DBA can read the SQL first; it is one file.

2. From the root of the client's repository, with Python 3 and nothing else:

   ```
   python <nsdn>/prototypes/catalogue_pass/ingest_catalogue.py --source <code> <folder with the CSV files>
   ```

   It writes one catalogue evidence per table and view under `analysis/<code>/tables/<schema>/<table>/evidence/`, and a
   source-wide one under `analysis/<code>/_source/evidence/`, each named by its content hash and written once. A later
   pass writes new evidence beside the old; readers take the newest.

3. To navigate it:

   ```
   python <nsdn>/prototypes/schema_viewer/build.py --root . --source <code> --out <folder>
   ```

   and open `<folder>/schema_viewer.html`.

The item files of the analysis (granularity, meaning, keys, temporal behaviour…) are not written here: they carry
judgement, cite this evidence, and are the agent's work under ADR-0017 to ADR-0019.

## Testing it

```
python prototypes/catalogue_pass/test_against_wwi.py --host <host> --port <port> --user <user> --db <empty database> --reader <new login>
```

SQL Server types are mapped to their nearest PostgreSQL types (`datetime2(7)` to `timestamp(6)`, PostgreSQL's
maximum); the eight computed columns of WWI are created as plain columns and reported as allowed differences.
