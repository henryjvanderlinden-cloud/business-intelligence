{{ config(materialized='incremental', incremental_strategy='append', on_schema_change='fail', schema='raw_vault',
          pre_hook="$pre_hook") }}

-- Reading satellite (143 section 5 item 5; 149 Rule 10): one row per reading, keyed by the parent and the reading's own
-- key, inserted once and never superseded. No hashdiff.
with incoming as (
    select
        $hk_src as hk,
        load_date,
        batch_id,
        record_source,
        source_ts,
        source_seq,
        $valid_from as valid_from,
$payload
    from {{ ref('$staging') }}
    where $hk_src is not null
    qualify row_number() over (partition by $hk_src, $reading_key order by source_ts, source_seq) = 1
)

select
    hk as $hk_out,
    load_date,
    batch_id,
    record_source,
    source_ts,
    source_seq,
    valid_from,
    '$basis' as valid_from_basis,
    '{{ invocation_id }}' as load_run,
$payload_out
from incoming i
{% if is_incremental() %}
where not exists (select 1 from {{ this }} t where t.$hk_out = i.hk and t.$reading_key = i.$reading_key)
{% endif %}
