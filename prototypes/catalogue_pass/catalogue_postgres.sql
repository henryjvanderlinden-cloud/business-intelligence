-- nsdn catalogue pass for PostgreSQL: read-only queries on the system catalogue, one CSV file per query.
--
-- What it reads: the structure of the database (schemas, tables, views, columns, types, keys, foreign keys, checks,
-- indexes, triggers, comments, the planner's row estimates). What it does not read: any row of any user table.
-- It runs in a read-only transaction and changes nothing. Written in nsdn session S11 (prototypes/catalogue_pass/).
--
-- Run it from an empty folder, which receives the CSV files:
--
--     psql -X -v ON_ERROR_STOP=1 -h <host> -p <port> -U <read-only user> -d <database> -f catalogue_postgres.sql
--
-- Each query writes the file named in the \o line before it. Schemas pg_catalog, information_schema and pg_toast and
-- the temporary schemas are left out of every query. The catalogue is readable without any privilege on the tables
-- themselves, so a login that may connect, and read nothing else, sees the whole structure. One query serves
-- PostgreSQL 12 to 17: a column that only newer versions have is read through to_jsonb() of its catalogue row.

\set QUIET on
\pset footer off
BEGIN TRANSACTION READ ONLY;

-- @query manifest
\o manifest.csv
COPY (
  SELECT current_database() AS database, current_user AS run_as, version() AS server_version,
         current_setting('server_version_num') AS server_version_num,
         to_char(now() AT TIME ZONE 'UTC', 'YYYY-MM-DD"T"HH24:MI:SS"Z"') AS extracted_at,
         current_setting('TimeZone') AS server_time_zone
) TO STDOUT WITH (FORMAT csv, HEADER);

-- @query tables
\o tables.csv
COPY (
  SELECT c.oid AS object_id, n.nspname AS schema_name, c.relname AS table_name,
         CASE c.relkind WHEN 'r' THEN 'table' WHEN 'p' THEN 'partitioned table' WHEN 'v' THEN 'view'
                        WHEN 'm' THEN 'materialized view' WHEN 'f' THEN 'foreign table' END AS table_kind,
         COALESCE(obj_description(c.oid, 'pg_class'), '') AS description,
         c.reltuples::bigint AS estimated_rows, c.relispartition AS is_partition,
         COALESCE((SELECT pn.nspname || '.' || pc.relname FROM pg_inherits i JOIN pg_class pc ON pc.oid = i.inhparent
                   JOIN pg_namespace pn ON pn.oid = pc.relnamespace WHERE i.inhrelid = c.oid LIMIT 1), '') AS partition_of,
         CASE WHEN c.relispartition THEN COALESCE(pg_get_expr(c.relpartbound, c.oid, true), '') ELSE '' END AS partition_bound,
         c.relrowsecurity AS row_level_security, pg_get_userbyid(c.relowner) AS owner
  FROM pg_class c JOIN pg_namespace n ON n.oid = c.relnamespace
  WHERE c.relkind IN ('r', 'p', 'v', 'm', 'f')
    AND n.nspname NOT IN ('pg_catalog', 'information_schema', 'pg_toast') AND n.nspname NOT LIKE 'pg_temp_%'
    AND n.nspname NOT LIKE 'pg_toast_temp_%'
  ORDER BY 2, 3
) TO STDOUT WITH (FORMAT csv, HEADER);

-- @query columns
\o columns.csv
COPY (
  SELECT c.oid AS object_id, n.nspname AS schema_name, c.relname AS table_name,
         row_number() OVER (PARTITION BY c.oid ORDER BY a.attnum) AS column_id, a.attnum AS attnum,
         a.attname AS column_name, format_type(a.atttypid, a.atttypmod) AS type_name, t.typname AS base_type,
         CASE WHEN a.atttypmod > 4 AND t.typname IN ('varchar', 'bpchar') THEN a.atttypmod - 4 END AS max_length,
         CASE WHEN t.typname = 'numeric' AND a.atttypmod > 4 THEN ((a.atttypmod - 4) >> 16) & 65535 END AS precision,
         CASE WHEN t.typname = 'numeric' AND a.atttypmod > 4 THEN (a.atttypmod - 4) & 65535 END AS scale,
         CASE WHEN a.attnotnull THEN 0 ELSE 1 END AS is_nullable,
         CASE WHEN a.attidentity <> '' THEN 1 ELSE 0 END AS is_identity, a.attidentity AS identity_kind,
         CASE WHEN a.attgenerated <> '' THEN 1 ELSE 0 END AS is_computed,
         CASE WHEN a.attgenerated = '' THEN COALESCE(pg_get_expr(d.adbin, d.adrelid), '') ELSE '' END AS default_definition,
         CASE WHEN a.attgenerated <> '' THEN COALESCE(pg_get_expr(d.adbin, d.adrelid), '') ELSE '' END AS computed_definition,
         COALESCE(col_description(c.oid, a.attnum), '') AS description,
         COALESCE(co.collname, '') AS collation
  FROM pg_attribute a
  JOIN pg_class c ON c.oid = a.attrelid JOIN pg_namespace n ON n.oid = c.relnamespace
  JOIN pg_type t ON t.oid = a.atttypid
  LEFT JOIN pg_attrdef d ON d.adrelid = a.attrelid AND d.adnum = a.attnum
  LEFT JOIN pg_collation co ON co.oid = a.attcollation AND a.attcollation <> 0 AND co.collname <> 'default'
  WHERE a.attnum > 0 AND NOT a.attisdropped AND c.relkind IN ('r', 'p', 'v', 'm', 'f')
    AND n.nspname NOT IN ('pg_catalog', 'information_schema', 'pg_toast') AND n.nspname NOT LIKE 'pg_temp_%'
    AND n.nspname NOT LIKE 'pg_toast_temp_%'
  ORDER BY 2, 3, 5
) TO STDOUT WITH (FORMAT csv, HEADER);

-- @query keys
\o keys.csv
COPY (
  -- primary keys and unique constraints, then unique indexes that back no constraint; an expression part of a key
  -- is given by its expression, and nulls_not_distinct is read from pg_index where the version has it (15 and later)
  SELECT n.nspname AS schema_name, c.relname AS table_name, k.conname AS index_name,
         CASE WHEN k.contype = 'p' THEN 1 ELSE 0 END AS is_primary_key, 1 AS is_unique,
         CASE WHEN k.contype = 'u' THEN 1 ELSE 0 END AS is_unique_constraint,
         u.ord AS key_ordinal, a.attname AS column_name, '' AS key_expression, '' AS filter_definition,
         COALESCE((to_jsonb(i) ->> 'indnullsnotdistinct')::boolean, false) AS nulls_not_distinct
  FROM pg_constraint k JOIN pg_class c ON c.oid = k.conrelid JOIN pg_namespace n ON n.oid = c.relnamespace
  LEFT JOIN pg_index i ON i.indexrelid = k.conindid
  CROSS JOIN LATERAL unnest(k.conkey) WITH ORDINALITY AS u(attnum, ord)
  JOIN pg_attribute a ON a.attrelid = c.oid AND a.attnum = u.attnum
  WHERE k.contype IN ('p', 'u') AND n.nspname NOT IN ('pg_catalog', 'information_schema', 'pg_toast')
    AND n.nspname NOT LIKE 'pg_temp_%' AND n.nspname NOT LIKE 'pg_toast_temp_%'
  UNION ALL
  SELECT n.nspname, c.relname, ic.relname, 0, 1, 0, u.ord, COALESCE(a.attname, ''),
         CASE WHEN u.attnum = 0 THEN pg_get_indexdef(i.indexrelid, u.ord::integer, true) ELSE '' END,
         COALESCE(pg_get_expr(i.indpred, i.indrelid), ''),
         COALESCE((to_jsonb(i) ->> 'indnullsnotdistinct')::boolean, false)
  FROM pg_index i JOIN pg_class ic ON ic.oid = i.indexrelid JOIN pg_class c ON c.oid = i.indrelid
  JOIN pg_namespace n ON n.oid = c.relnamespace
  CROSS JOIN LATERAL unnest(i.indkey::int2[]) WITH ORDINALITY AS u(attnum, ord)
  LEFT JOIN pg_attribute a ON a.attrelid = c.oid AND a.attnum = u.attnum AND u.attnum > 0
  WHERE i.indisunique AND NOT EXISTS (SELECT 1 FROM pg_constraint k WHERE k.conindid = i.indexrelid)
    AND u.ord <= i.indnkeyatts AND n.nspname NOT IN ('pg_catalog', 'information_schema', 'pg_toast')
    AND n.nspname NOT LIKE 'pg_temp_%' AND n.nspname NOT LIKE 'pg_toast_temp_%'
  ORDER BY 1, 2, 3, 7
) TO STDOUT WITH (FORMAT csv, HEADER);

-- @query foreign_keys
\o foreign_keys.csv
COPY (
  SELECT k.conname AS fk_name, n.nspname AS schema_name, c.relname AS table_name, a.attname AS column_name,
         u.ord AS constraint_column_id, rn.nspname AS ref_schema, rc.relname AS ref_table, ra.attname AS ref_column,
         CASE k.confdeltype WHEN 'a' THEN 'NO_ACTION' WHEN 'r' THEN 'RESTRICT' WHEN 'c' THEN 'CASCADE'
                            WHEN 'n' THEN 'SET_NULL' WHEN 'd' THEN 'SET_DEFAULT' END AS delete_referential_action_desc,
         CASE k.confupdtype WHEN 'a' THEN 'NO_ACTION' WHEN 'r' THEN 'RESTRICT' WHEN 'c' THEN 'CASCADE'
                            WHEN 'n' THEN 'SET_NULL' WHEN 'd' THEN 'SET_DEFAULT' END AS update_referential_action_desc,
         0 AS is_disabled, CASE WHEN k.convalidated THEN 0 ELSE 1 END AS is_not_trusted,
         CASE WHEN k.condeferrable THEN 1 ELSE 0 END AS is_deferrable
  FROM pg_constraint k
  JOIN pg_class c ON c.oid = k.conrelid JOIN pg_namespace n ON n.oid = c.relnamespace
  JOIN pg_class rc ON rc.oid = k.confrelid JOIN pg_namespace rn ON rn.oid = rc.relnamespace
  CROSS JOIN LATERAL unnest(k.conkey, k.confkey) WITH ORDINALITY AS u(attnum, refnum, ord)
  JOIN pg_attribute a ON a.attrelid = c.oid AND a.attnum = u.attnum
  JOIN pg_attribute ra ON ra.attrelid = rc.oid AND ra.attnum = u.refnum
  WHERE k.contype = 'f' AND n.nspname NOT IN ('pg_catalog', 'information_schema', 'pg_toast')
    AND n.nspname NOT LIKE 'pg_temp_%' AND n.nspname NOT LIKE 'pg_toast_temp_%'
  ORDER BY 2, 3, 1, 5
) TO STDOUT WITH (FORMAT csv, HEADER);

-- @query checks
\o checks.csv
COPY (
  SELECT n.nspname AS schema_name, c.relname AS table_name, k.conname AS check_name,
         COALESCE((SELECT string_agg(a.attname, ', ' ORDER BY a.attnum) FROM pg_attribute a
                   WHERE a.attrelid = c.oid AND a.attnum = ANY (k.conkey)), '') AS column_name,
         pg_get_constraintdef(k.oid) AS definition, 0 AS is_disabled, CASE WHEN k.convalidated THEN 0 ELSE 1 END AS is_not_trusted
  FROM pg_constraint k JOIN pg_class c ON c.oid = k.conrelid JOIN pg_namespace n ON n.oid = c.relnamespace
  WHERE k.contype = 'c' AND n.nspname NOT IN ('pg_catalog', 'information_schema', 'pg_toast')
    AND n.nspname NOT LIKE 'pg_temp_%' AND n.nspname NOT LIKE 'pg_toast_temp_%'
  ORDER BY 1, 2, 3
) TO STDOUT WITH (FORMAT csv, HEADER);

-- @query triggers
\o triggers.csv
COPY (
  SELECT n.nspname AS schema_name, c.relname AS table_name, t.tgname AS trigger_name,
         pn.nspname || '.' || p.proname AS function_name, t.tgenabled AS enabled,
         pg_get_triggerdef(t.oid) AS definition
  FROM pg_trigger t JOIN pg_class c ON c.oid = t.tgrelid JOIN pg_namespace n ON n.oid = c.relnamespace
  JOIN pg_proc p ON p.oid = t.tgfoid JOIN pg_namespace pn ON pn.oid = p.pronamespace
  WHERE NOT t.tgisinternal AND n.nspname NOT IN ('pg_catalog', 'information_schema', 'pg_toast')
    AND n.nspname NOT LIKE 'pg_temp_%' AND n.nspname NOT LIKE 'pg_toast_temp_%'
  ORDER BY 1, 2, 3
) TO STDOUT WITH (FORMAT csv, HEADER);

-- @query views
\o views.csv
COPY (
  SELECT n.nspname AS schema_name, c.relname AS view_name, pg_get_viewdef(c.oid, true) AS definition
  FROM pg_class c JOIN pg_namespace n ON n.oid = c.relnamespace
  WHERE c.relkind IN ('v', 'm') AND n.nspname NOT IN ('pg_catalog', 'information_schema', 'pg_toast')
    AND n.nspname NOT LIKE 'pg_temp_%' AND n.nspname NOT LIKE 'pg_toast_temp_%'
  ORDER BY 1, 2
) TO STDOUT WITH (FORMAT csv, HEADER);

-- @query view_dependencies
\o view_dependencies.csv
COPY (
  SELECT DISTINCT vn.nspname AS schema_name, v.relname AS view_name, tn.nspname AS ref_schema, t.relname AS ref_table
  FROM pg_rewrite r JOIN pg_class v ON v.oid = r.ev_class JOIN pg_namespace vn ON vn.oid = v.relnamespace
  JOIN pg_depend d ON d.objid = r.oid AND d.classid = 'pg_rewrite'::regclass AND d.refclassid = 'pg_class'::regclass
  JOIN pg_class t ON t.oid = d.refobjid JOIN pg_namespace tn ON tn.oid = t.relnamespace
  WHERE v.relkind IN ('v', 'm') AND t.oid <> v.oid AND t.relkind IN ('r', 'p', 'v', 'm', 'f')
    AND vn.nspname NOT IN ('pg_catalog', 'information_schema', 'pg_toast')
    AND vn.nspname NOT LIKE 'pg_temp_%' AND vn.nspname NOT LIKE 'pg_toast_temp_%'
  ORDER BY 1, 2, 3, 4
) TO STDOUT WITH (FORMAT csv, HEADER);

\o
COMMIT;
