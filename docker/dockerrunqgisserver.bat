docker run -d -p 8380:80 ^
            -e DISPLAY=10.20.75.139:0.0 ^
            -e QGIS_SERVER_IGNORE_BAD_LAYERS='true' ^
            --name ggisserver ^
            --mount source=C:\111_GitProjects\Lamia\arteliasite\qgisserverprojects,target=/etc/qgisserver,type=bind,consistency=delegated ^
            camptocamp/qgis-server:3.10

