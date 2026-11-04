{{ config(materialized='incremental', incremental_strategy='append', on_schema_change='fail', schema='raw_vault',
          pre_hook="$pre_hook") }}

-- $title: a row only when a key's status changes between complete
-- extracts. 'deletion-confirmed' is not generated (143 section 12). Where the source is system-versioned and has closed
-- the last version of an absent key, the end it delivered is kept as source_closed_at, as text (143 section 13 item 5).
with present as (
    select $hk as hk$kept_present from {{ ref('$staging') }}
    where not _is_history and $hk is not null
    group by all
),

closed as (
    select $hk as hk, max(source_end) as source_closed_at from {{ ref('$staging') }}
    where $hk is not null
    group by all
),

-- The batch is named by the runner's variable, not read from the rows, so it is right also when the table is empty
-- in this extract (second review, finding 5).
batch as (
    select cast('{{ var('load_date') }}' as date) as load_date, '$source:{{ var('load_date') }}' as batch_id
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
    end                   as status,
    case when p.hk is null then c.source_closed_at end as source_closed_at,$kept_select
    '{{ invocation_id }}' as load_run
from present p
full join latest l on p.hk = l.hk
cross join batch b
left join closed c on c.hk = coalesce(p.hk, l.hk)
where l.hk is null
   or (p.hk is null and l.status <> 'absent-unresolved')
   or (p.hk is not null and l.status = 'absent-unresolved')
