{{ config(materialized='incremental', incremental_strategy='append', on_schema_change='fail', schema='raw_vault',
          pre_hook="$pre_hook") }}

-- Status-tracking satellite (143 section 5 item 7; 149 Rule 7): a row only when a key's status changes between complete
-- extracts. 'deletion-confirmed' is not generated (143 section 12).
with present as (
    select distinct $hk as hk from {{ ref('$staging') }}
    where not _is_history and $hk is not null
),

batch as (
    select any_value(load_date) as load_date, any_value(batch_id) as batch_id from {{ ref('$staging') }}
),

{% if is_incremental() %}
latest as (
    select $hk as hk, status from {{ this }}
    qualify row_number() over (partition by $hk order by load_date desc) = 1
)
{% else %}
latest as (
    select cast(null as varchar) as hk, cast(null as varchar) as status where false
)
{% endif %}

select
    coalesce(p.hk, l.hk)  as $hk,
    b.load_date,
    b.batch_id,
    '$record_source'      as record_source,
    case
        when l.hk is null then 'present'
        when p.hk is null then 'absent-unresolved'
        else 'reappeared'
    end                   as status
from present p
full join latest l on p.hk = l.hk
cross join batch b
where l.hk is null
   or (p.hk is null and l.status <> 'absent-unresolved')
   or (p.hk is not null and l.status = 'absent-unresolved')
