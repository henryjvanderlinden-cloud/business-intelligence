{{ config(materialized='table', schema='staging') }}
-- A table, rebuilt on every load, so that the hashing is done once and not again by every model that reads it.

-- One source table as delivered in the latest extract, typed, keyed and hashed (143 section 9 item 2).
-- Source version (149 Rule 2; 143 section 4): record_source, source_ts, source_seq.
$history_block
with delivered as (
$delivered
),

-- row_hash covers every delivered column except the end of the source's validity period, which moves when the
-- version is closed later and so is not part of the version (143 section 6 item 4). Only a history row identical in
-- every column, its end included, to a row of the current table is taken as the same row delivered twice (149
-- section 5); rows within one table are all kept, however alike, since two of them can be two source events
-- (second review, finding 2), and a zero-length version is kept (ADR-0037 decision 2).
hashed as (
    select *, sha256($row_hash_input) as row_hash
    from delivered
    qualify not (_is_history and sum(case when _is_history then 0 else 1 end)
                     over (partition by $pk_raw, row_hash$period_end_raw) > 0)
),

typed as (
    select
        _is_history,
        _nsdn_load_date as load_date,
        '$source:' || strftime(_nsdn_load_date, '%Y-%m-%d') as batch_id,
        '$record_source' as record_source,
        $source_ts as source_ts,
        $source_end as source_end,
        $history_from_column as _history_from,
        row_hash,
$hashdiffs
$typed_columns
    from hashed
)

select
    $select_all,
    -- Ties in source system time: ordered by end of validity (open end last), then by the whole-row hash (143 section 6 item 2).
    row_number() over (partition by $pk_typed, source_ts order by source_end nulls last, row_hash) as source_seq$hash_keys
from typed$lookups
