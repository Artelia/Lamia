REM docker build -t lamia_webservice -f arteliasitedocker/Dockerfile https://github.com/Artelia/Lamia.git#develop
cd ..
docker build -t lamia_qgisserver -f arteliasitedocker/Dockerfile_qgisserver .