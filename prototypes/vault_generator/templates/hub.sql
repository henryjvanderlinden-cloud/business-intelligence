{{ config(materialized='incremental', incremental_strategy='append', on_schema_change='fail', schema='raw_vault',
          pre_hook="$pre_hook") }}

-- Hub (143 section 5 item 1): each hash key once, with the business key as delivered and the earliest source version
-- that brought it.
with incoming as (
$incoming
),

first_seen as (
    select * from incoming
    qualify row_number() over (partition by $hk order by source_ts, source_seq, record_source) = 1
)

select $columns
from first_seen
{% if is_incremental() %}
where $hk not in (select $hk from {{ this }})
{% endif %}
