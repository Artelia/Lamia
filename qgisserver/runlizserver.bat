docker run -p 8080:8080 ^
--name lizserver ^
       -v /path/to/qgis/projects:/projects ^
       -e github=https://github.com/3liz/py-qgis-server.git
       -e QGSRV_SERVER_WORKERS=2 ^
       -e QGSRV_LOGGING_LEVEL=DEBUG  ^
       -e QGSRV_CACHE_ROOTDIR=/projects ^
       -e QGSRV_CACHE_SIZE=10 ^
       --mount source=C:\111_GitProjects\Lamia\qgisserver\projects,target=/etc/qgisserver,type=bind,consistency=delegated ^
       https://github.com/3liz/docker-qgis-server