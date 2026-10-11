-- Smoke model for the runner's end-to-end test: Sales.Orders typed. The vault comes next.
select
    cast(OrderID as integer)                   as order_id,
    cast(CustomerID as integer)                as customer_id,
    cast(SalespersonPersonID as integer)       as salesperson_person_id,
    cast(OrderDate as date)                    as order_date,
    cast(ExpectedDeliveryDate as date)         as expected_delivery_date,
    cast(PickingCompletedWhen as timestamp)    as picking_completed_when,
    cast(LastEditedWhen as timestamp)          as last_edited_when,
    _nsdn_load_date                            as load_date
from {{ source('landing', 'sales__orders') }}
