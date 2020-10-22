REM docker build -t lamia_webservice -f arteliasitedocker/Dockerfile https://github.com/Artelia/Lamia.git#develop
cd ..
docker build -t 710412343115.dkr.ecr.eu-west-3.amazonaws.com/lamia-qgisserver:latest -f arteliasitedocker/Dockerfile_qgisserver .