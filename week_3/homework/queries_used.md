CREATE OR REPLACE EXTERNAL TABLE `fine-rookery-412515.ny_taxi.green-tripdata2022`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://mage-zoomcamp-jals/green_tripdata_2022-*.parquet']
);


CREATE OR REPLACE TABLE `fine-rookery-412515.ny_taxi.green_tripdata2022_non_partitioned`
AS SELECT * FROM `fine-rookery-412515.ny_taxi.green_tripdata2022_external`;


SELECT COUNT (*) FROM `fine-rookery-412515.ny_taxi.green_tripdata2022_non_partitioned`;


SELECT count(*) FROM `fine-rookery-412515.ny_taxi.green_tripdata2022_partitioned` where fare_amount = 0;


CREATE OR REPLACE TABLE `fine-rookery-412515.ny_taxi.green_tripdata2022_partitioned`
PARTITION BY DATE(lpep_pickup_datetime)
AS SELECT * FROM `fine-rookery-412515.ny_taxi.green_tripdata2022_external`;


CREATE OR REPLACE TABLE `fine-rookery-412515.ny_taxi.green_tripdata2022_partitioned_clustered`
PARTITION BY DATE(lpep_pickup_datetime)
CLUSTER BY VendorID
AS SELECT * FROM `fine-rookery-412515.ny_taxi.green_tripdata2022_external`;


SELECT distinct (PUlocationID)
FROM `fine-rookery-412515.ny_taxi.green_tripdata2022_non_partitioned`
WHERE lpep_pickup_datetime BETWEEN '2022-06-01' and '2022-06-30'


SELECT distinct (PUlocationID)
FROM `fine-rookery-412515.ny_taxi.green_tripdata2022_partitioned_clustered`
WHERE lpep_pickup_datetime BETWEEN '2022-06-01' and '2022-06-30'

