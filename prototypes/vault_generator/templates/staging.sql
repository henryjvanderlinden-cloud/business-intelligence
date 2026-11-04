{{ config(materialized='view', schema='staging') }}

-- One source table as delivered in the latest extract, typed, keyed and hashed (143 section 9 item 2).
-- Source version (149 Rule 2; 143 section 4): record_source, source_ts, source_seq.
with delivered as (
$delivered
),

-- row_hash covers every delivered column except the end of the source's validity period, which moves when the
-- version is closed later and so is not part of the version (143 section 6 item 4). A row delivered twice in one
-- extract, identical in every column including that end, is kept once; a zero-length version, which differs from
-- the version that replaced it only in its end, is kept (ADR-0037 decision 2).
hashed as (
    select *, sha256($row_hash_input) as row_hash
    from delivered
    qualify row_number() over (partition by $pk_raw, row_hash$period_end_raw order by _is_history) = 1
),

typed as (
    select
        _is_history,
        _nsdn_load_date as load_date,
        '$source:' || strftime(_nsdn_load_date, '%Y-%m-%d') as batch_id,
        '$record_source' as record_source,
        $source_ts as source_ts,
        $source_end as source_end,
        row_hash,
$hashdiffs
$typed_columns
    from hashed
)

select
    *,
    -- Ties in source system time: ordered by end of validity (open end last), then by the whole-row hash (143 section 6 item 2).
    row_number() over (partition by $pk_typed, source_ts order by source_end nulls last, row_hash) as source_seq$hash_keys
from typed
