{{ config(materialized='incremental', incremental_strategy='append', on_schema_change='fail', schema='raw_vault',
          pre_hook="$pre_hook") }}

-- $kind_note
-- A source version is inserted when it is not yet here and its hashdiff differs from that of the version before it
-- in source order, across the rows already here and those delivered now (143 section 5). A version known but not
-- delivered now and not stored here takes the values of the stored row before it, so that a late arrival is followed
-- by a restatement of the next version (143 section 6 item 6).
with incoming as (
    select
        $hk_src                    as hk,
        load_date,
        batch_id,
        record_source,
        source_ts,
        source_seq,
        $valid_from                as valid_from,
        $hashdiff                  as hashdiff,
$payload_incoming
    from {{ ref('$staging') }}
    where $hk_src is not null
),

batch as (
    select any_value(load_date) as load_date, any_value(batch_id) as batch_id from {{ ref('$staging') }}
),

{% if is_incremental() %}
stored as (
    select $hk_out as hk, record_source, source_ts, source_seq, valid_from, hashdiff,
$payload_plain
    from {{ this }}
),
{% else %}
stored as (
    select hk, record_source, source_ts, source_seq, valid_from, hashdiff,
$payload_plain
    from incoming where false
),
{% endif %}

known as (
    select hk, record_source, source_ts, source_seq from incoming
    union
    select hk, record_source, source_ts, source_seq from stored$known_audit
),

ordered as (
    select
        k.hk, k.record_source, k.source_ts, k.source_seq,
        s.hashdiff as stored_hd,
        i.hashdiff as incoming_hd,
        last_value(s.hashdiff ignore nulls) over w_before as inherited_hd,
        last_value(case when s.hashdiff is not null then struct_pack(ts := k.source_ts, seq := k.source_seq) end ignore nulls)
            over w_before as inherited_from
    from known k
    left join stored s
        on s.hk = k.hk and s.record_source = k.record_source
       and s.source_ts is not distinct from k.source_ts and s.source_seq = k.source_seq
    left join incoming i
        on i.hk = k.hk and i.record_source = k.record_source
       and i.source_ts is not distinct from k.source_ts and i.source_seq = k.source_seq
    window w_before as (partition by k.hk order by k.source_ts, k.source_seq
                        rows between unbounded preceding and 1 preceding)
),

changes as (
    select
        *,
        coalesce(stored_hd, incoming_hd, inherited_hd, $null_hd) as effective_hd,
        coalesce(lag(coalesce(stored_hd, incoming_hd, inherited_hd, $null_hd))
                     over (partition by hk order by source_ts, source_seq), $null_hd) as previous_hd
    from ordered
)

select
    c.hk                                                         as $hk_out,
    b.load_date,
    b.batch_id,
    c.record_source,
    c.source_ts,
    c.source_seq,
    case when i.hk is not null then i.valid_from else s.valid_from end as valid_from,
    '$basis'                                                     as valid_from_basis,
    c.effective_hd                                               as hashdiff,
$payload_select
from changes c
cross join batch b
left join incoming i
    on i.hk = c.hk and i.record_source = c.record_source
   and i.source_ts is not distinct from c.source_ts and i.source_seq = c.source_seq
left join stored s
    on s.hk = c.hk and s.record_source = c.record_source
   and s.source_ts is not distinct from c.inherited_from.ts and s.source_seq = c.inherited_from.seq
where c.stored_hd is null
  and c.effective_hd is distinct from c.previous_hd
