# -*- coding: utf-8 -*-

import qgis
import os

path = os.path.normpath('C:\\000_testdigue\\BM\\BD_SIJALAG_ind4.sqlite')
path = 'C:\\000_testdigue\\BM\\BD_SIJALAG_ind4.sqlite'
path = 'C://000_testdigue//BM//BD_SIJALAG_ind4.sqlite'

if False:
    df = qgis.core.QgsVirtualLayerDefinition()

    print(df)
    # dbname='I:\\FLUVIAL\\4352024_33_Conformite_digues_BM\\6_Reglementaire\\61_Calculs\\Basedonnees\\201708_SIJALAG\\BD_SIJALAG_ind4.sqlite' key='id_zonegeo' table="Zonegeo_qgis" (geom) sql="datecreation" <= '2018-02-12' AND CASE WHEN "datedestruction" IS NOT NULL  THEN "datedestruction" > '2018-02-12' ELSE 1 END
    df.addSource("vtab", path, "spatialite",'utf-8' )
    df.setQuery("SELECT * FROM Objet")

    print(df.toString())

    db = "?layer=spatialite:C://000_testdigue//BM//BD_SIJALAG_ind4.sqlite"
    db += '''?query="SELECT * FROM Objet"'''
    print(db)

    l1 = qgis.core.QgsVectorLayer( db,"myvlayer", "virtual" )

    print('ok')

if False:
    df = qgis.core.QgsVirtualLayerDefinition(path)
    df.setQuery("SELECT * FROM Infralineaire")

if True:
    df = qgis.core.QgsVirtualLayerDefinition()
    print(df.fields ())
    print('path', df.filePath () )
    print('geom',df.geometryField ())

    df.setFilePath(path)
    df.setQuery("SELECT * FROM Infralineaire")
    df.addSource("vtab", path, "spatialite",'utf-8')

    print(df.fields ())
    print('path', df.filePath () )
    print('geom',df.geometryField ())
    print('sourceLayers', df.sourceLayers() )
    for sourcelayer in df.sourceLayers():
        print(sourcelayer.name())
        print(sourcelayer.encoding ())
        print(sourcelayer.provider())
        print(sourcelayer.source() )

    print(df.toString())



if False:

    l1 = qgis.core.QgsVectorLayer('"' + path + "?query=SELECT * FROM Infralineaire" ,  "myvlayer"  ,        "virtual"    )


if False:
    for fet in l1.getFeatures():
        print(fet.attributes())



print('end')

