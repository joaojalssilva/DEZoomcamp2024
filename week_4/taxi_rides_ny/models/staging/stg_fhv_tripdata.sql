with 

source as (

    select * from {{ source('staging', 'fhv_tripdata') }}

),

filtered as (

    select *

    from source

    WHERE EXTRACT(YEAR FROM pickup_datetime) = 2019

)

select * from filtered
