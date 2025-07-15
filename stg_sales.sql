with raw_sales as (

    select
        order_id,
        order_date,
        product_id,
        quantity,
        sales_amount
    from {{ source('raw', 'retail_sales') }}

)

select
    order_id,
    order_date,
    product_id,
    quantity,
    sales_amount
from raw_sales
