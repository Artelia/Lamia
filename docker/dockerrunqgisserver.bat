docker run -d -p 8380:80 ^
            -e DISPLAY=192.168.1.17:0.0 ^
            -e QGIS_SERVER_IGNORE_BAD_LAYERS='true' ^
            -e QUERY_STRING="MAP=/etc/qgisserver/project.qgs&SERVICE=WMS&REQUEST=GetCapabilities" ^
            --name ggisserver ^
            --mount source=C:\111_GitProjects\testreact\qgisproject,target=/etc/qgisserver,type=bind,consistency=delegated ^
            camptocamp/qgis-server:3.10

