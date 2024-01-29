docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v /workspaces/DEZoomcamp2024/week_1/2_docker_sql/ny_taxi_postgres_data:/var/lib/postgresql/data \
  -p 5432:5432 \
  postgres:13
  
docker stop [container id or container name]

docker start container [container id or container name]
  
  
pgcli -h localhost -p 5432 -u root -d ny_taxi
 
 
jupyter notebook
 
 
docker run -it \
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com"\
  -e PGADMIN_DEFAULT_PASSWORD="root" \
  -p 8080:80 \
  dpage/pgadmin4
  
  
  
 ## Network
  
docker network create pg-network

docker network inspect pg-network
  
  
docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v /workspaces/DEZoomcamp2024/week_1/2_docker_sql/ny_taxi_postgres_data:/var/lib/postgresql/data \
  -p 5432:5432 \
  --network=pg-network \
  --name pg-database \
  postgres:13
  
docker start pg-database
  
  
  
docker run -it \
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com"\
  -e PGADMIN_DEFAULT_PASSWORD="root" \
  -p 8080:80 \
  --network=pg-network \
  --name pgadmin \
  dpage/pgadmin4
  
docker start pgadmin
 
 
 
python ingest_data.py \
	--user=root \
    --password=root \
    --host=localhost \
    --port=5432 \
    --db=ny_taxi \
    --table_name=yellow_taxi_data \
    --url=https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz
	
	
	
	
docker build -t taxi_ingest:v001 .

docker run -it \
	--network=pg-network \
	taxi_ingest:v001 \
	--user=root \
    --password=root \
    --host=pg-database \
    --port=5432 \
    --db=ny_taxi \
    --table_name=yellow_taxi_data \
    --url=https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz
	
	
	

	  
docker-compose up

OR

docker-compose up -d

docker-compose down
