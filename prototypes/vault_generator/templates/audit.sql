{{ config(materialized='incremental', incremental_strategy='append', on_schema_change='fail', schema='raw_vault',
          pre_hook="$pre_hook") }}

-- Audit satellite (143 section 5 item 6; 149 Rule 3): every source version once, with no change detection, so that it
-- is the source's version log. One row per version of every source table that describes this $owner_kind, told apart
-- by record_source.
with incoming as (
$incoming
)

select * from incoming i
{% if is_incremental() %}
where not exists (
    select 1 from {{ this }} t
    where t.$hk = i.$hk and t.record_source = i.record_source
      and t.source_ts is not distinct from i.source_ts and t.source_seq = i.source_seq
)
{% endif %}
