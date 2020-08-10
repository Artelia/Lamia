REM docker volume create pg_data
REM docker run --name=postgis -d -e POSTGRES_USER=pvr -e POSTGRES_PASS=pvr -e POSTGRES_DBNAME=gis -e ALLOW_IP_RANGE=0.0.0.0/0 -p 5432:5432 -v c:/000_Docker_rep/postgis:/var/lib/postgresql --restart=always kartoza/postgis:12.0
docker run --name=postgis2 -d -e POSTGRES_USER=pvr -e POSTGRES_PASS=pvr -e POSTGRES_DBNAME=gis -e ALLOW_IP_RANGE=0.0.0.0/0 -p 5432:5432 -v c:\000_Docker_rep\postgis:/var/lib/postgresql/data/pgdata --restart=always kartoza/postgis:12.0
