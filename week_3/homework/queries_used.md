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