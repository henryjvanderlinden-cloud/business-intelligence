# XREV 2026-10-29 — the PostgreSQL catalogue pass — sol

```yaml
object:        prototypes/catalogue_pass/catalogue_postgres.sql, first version, uncommitted (copied to scratch/ for the
               review).
reviewer:      gpt-5.6-sol, via the Codex MCP server on the author's desktop, reasoning effort medium, workspace-write
               sandbox, no browsing; answer written to the ignored scratch/ folder with apply_patch; confined to the one
               file, it wrote in under 2 minutes.
assignment:    assume an experienced PostgreSQL DBA rejects the script, judged against four stated standards (reads only
               the catalogue and changes nothing; safe on a busy production server; captures the complete structure
               listed; runs on versions 12 to 17 with ordinary read privileges); up to five findings with failure cases;
               naming, CSV choices and later use excluded; praise, summary and general assessment forbidden.
second reader: assignment set by Claude Opus 5.5, which drafted the object in session 11 on 2026-10-29; the corrections
               are tested (test_against_wwi.py) but unreviewed by construction.
verdict:       FAILS [column metadata is suppressed unless the runner has SELECT privileges on every user-table column].
               Resolved in the corrected script, unreviewed.
```

## sol's answer, verbatim

1. Quoted SQL: `AND has_column_privilege(c.oid, a.attnum, 'SELECT')`

   What is wrong: PostgreSQL exposes catalogue metadata independently of `SELECT` privilege on each user-table column, but this predicate deliberately suppresses that metadata. Thus an ordinary catalogue-reading account cannot produce the required complete structure unless it is also granted data-reading privileges on every table; granting those privileges would undermine the intended least-privilege catalogue pass.

   Concrete failure case: Let `app.customer(id bigint, email text)` be owned by `app_owner`, and run the script as a monitoring role that can connect and read the system catalogues but has no `SELECT` on `app.customer`. `tables.csv` contains `app.customer`, while `columns.csv` contains neither `id` nor `email`.

   Minimal correction: Remove the `has_column_privilege(...)` predicate. `pg_attribute`, `pg_attrdef`, and the deparser functions used here can provide this metadata without reading a row of the table.

   Confidence: High.

2. Quoted SQL: `c.relispartition AS is_partition, COALESCE((SELECT pn.nspname || '.' || pc.relname ...), '') AS partition_of`

   What is wrong: This records that a relation is a partition and names its parent, but never records its partition bound. The bound is essential structural metadata, so the extraction cannot distinguish partitions with different ranges, lists, hash remainders, or a default partition.

   Concrete failure case: For `sales_2025 PARTITION OF sales FOR VALUES FROM ('2025-01-01') TO ('2026-01-01')`, the output says only that `sales_2025` is a partition of `sales`; it omits the `FROM`/`TO` bound entirely. A default partition and an explicitly bounded partition otherwise having the same columns are not structurally distinguishable in the output.

   Minimal correction: Add a field such as `CASE WHEN c.relispartition THEN pg_get_expr(c.relpartbound, c.oid, true) ELSE '' END AS partition_bound` to the tables query. These catalogue fields and `pg_get_expr` are available throughout PostgreSQL 12--17.

   Confidence: High.

3. Quoted SQL: `COALESCE(a.attname, '(expression)')`

   What is wrong: A unique expression index is reported merely as the literal placeholder `(expression)`, so its defining expression is lost. Different unique indexes can consequently produce identical structural rows.

   Concrete failure case: `CREATE UNIQUE INDEX users_email_ci_uq ON app.users (lower(email));` produces a key row whose `column_name` is `(expression)` and contains no `lower(email)` anywhere. An index on `upper(email)` would produce the same key description.

   Minimal correction: For each key ordinal, emit `pg_get_indexdef(i.indexrelid, u.ord::integer, true)` (optionally alongside the simple column name) so expression and column keys are both represented accurately.

   Confidence: High.

4. Quoted SQL: `SELECT n.nspname AS schema_name, c.relname AS table_name, k.conname AS index_name, CASE WHEN k.contype = 'p' THEN 1 ELSE 0 END AS is_primary_key, 1 AS is_unique, ...` and `SELECT n.nspname, c.relname, ic.relname, 0, 1, 0, ... FROM pg_index i`

   What is wrong: Neither branch captures PostgreSQL 15+'s `NULLS NOT DISTINCT` property. It therefore describes two unique constraints or indexes with different uniqueness semantics identically.

   Concrete failure case: On PostgreSQL 15, `CREATE UNIQUE INDEX account_external_uq ON account(external_id) NULLS NOT DISTINCT;` permits at most one null, but the output is indistinguishable from a conventional unique index that permits multiple nulls.

   Minimal correction: Add a `nulls_not_distinct` output derived from the backing `pg_index.indnullsnotdistinct` on PostgreSQL 15--17, and emit `false` on 12--14. Because the column does not exist before 15, select the version-appropriate query with psql `\if`/`\elif` logic (or separate version-specific statements); an unconditional reference is not cross-version compatible.

   Confidence: High.

5. Quoted SQL: `WHERE k.contype IN ('p', 'u') AND n.nspname NOT IN ('pg_catalog', 'information_schema', 'pg_toast')` (with the same exact-name-only exclusion in the foreign-key, check, trigger, view, and view-dependency queries)

   What is wrong: Unlike the tables and columns queries, these queries do not exclude `pg_temp_%` and `pg_toast_temp_%` schemas. They can output system-temporary objects that are outside the stated scope, including rows whose owning relation is absent from `tables.csv`.

   Concrete failure case: In the psql session, create `TEMP TABLE stage(id integer PRIMARY KEY, value integer CHECK (value > 0));` before running the script. `tables.csv` omits `pg_temp_N.stage`, but `keys.csv` and `checks.csv` include its primary key and check constraint, producing orphaned and out-of-scope metadata.

   Minimal correction: Apply the same `n.nspname NOT LIKE 'pg_temp_%' AND n.nspname NOT LIKE 'pg_toast_temp_%'` predicates consistently to every object query (and the equivalent predicate for referenced/view namespaces where scope requires it).

   Confidence: High.

VERDICT: FAILS [column metadata is suppressed unless the runner has `SELECT` privileges on every user-table column].

## Dispositions

1. **Accepted, and confirmed.** For a login with only `CONNECT`, the removed filter returned 0 of WWI's 557 columns;
   without it all come back. `test_against_wwi.py --reader` now runs the pass as such a login.
2. **Accepted.** `tables.csv` carries `partition_bound`; tested on a range partition.
3. **Accepted.** An expression part of a unique index is given in `key_expression`, from `pg_get_indexdef`; tested on
   `lower("EmailAddress")`.
4. **Accepted, by another means than proposed.** Instead of version branches with `\if`, `nulls_not_distinct` is read
   as `to_jsonb(i) ->> 'indnullsnotdistinct'`, which is the flag on 15 and later and absent, read as false, on 12 to 14,
   so one query serves every version; tested on PostgreSQL 16. Versions 12 to 15 were not run.
5. **Accepted.** Every object query leaves out `pg_temp_%` and `pg_toast_temp_%`; the test checks the script for it.
