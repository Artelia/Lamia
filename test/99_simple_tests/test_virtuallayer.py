# -*- coding: utf-8 -*-

import qgis, os
import qgis.core
from qgis.PyQt import QtGui, uic, QtCore, QtXml
from pprint import pprint as pprint
from Lamia.Lamia.main.DBaseParser import DBaseParser

qgis_path = "C://Program Files//OSGeo4W64-310//apps//qgis"
app = qgis.core.QgsApplication([], True)
qgis.core.QgsApplication.setPrefixPath(qgis_path, True)
qgis.core.QgsApplication.initQgis()




path = str("c://testshape.shp")
temppathsqlite = "c://00_Affaires//testsqlite.sqlite"
pathsqlite = os.path.normpath( temppathsqlite )
temppathsqlitefile = "file:///" + pathsqlite

sql = " SELECT * FROM test "


if False:
    print('tete',pathsqlite)
    vlayerlayer = ''


    vlayerlayer += temppathsqlitefile
    #vlayerlayer += QtCore.QUrl.toPercentEncoding(pathsqlite).data().decode('utf-8')

    vlayerlayer += "?layer=ogr:"

    #vlayerlayer += QtCore.QUrl.toPercentEncoding(path).data().decode('utf-8')
    vlayerlayer += path

    vlayerlayer += ":" + 'test' + ":UTF8"


    sql = " SELECT * FROM test "
    vlayerlayer += '&query=' + QtCore.QUrl.toPercentEncoding(sql).data().decode('utf-8')

    print('***')
    print(vlayerlayer)

    testlayer = qgis.core.QgsVectorLayer( vlayerlayer, "myvlayer", "virtual" )


if True:
    df = qgis.core.QgsVirtualLayerDefinition()
    df.addSource("test", path, "ogr")
    df.addSource("test", "c://test1.shp", "ogr")
    df.setQuery(sql)
    df.setFilePath(temppathsqlite)

    testlayer = qgis.core.QgsVectorLayer( df.toString(),"myvlayer", "virtual" )
    print('*_*_*_*_*')



    print(df.toString())
    print(df.filePath() )

    print('*$*$*$*$*$*$')
    options = qgis.core.QgsVectorFileWriter.SaveVectorOptions()

    options.actionOnExistingFile = qgis.core.QgsVectorFileWriter.CreateOrOverwriteLayer
    options.layerName = "results"
    options.driverName = "sqlite"
    options.fileEncoding = "UTF-8"

    writer = qgis.core.QgsVectorFileWriter.writeAsVectorFormat(
        testlayer,
        temppathsqlite,
        options)
    print(writer)

    print('***parser***')
    pars = DBaseParser()
    pars.connectToDBase(slfile=temppathsqlite)
    print(pars.dbasetype)
    res = pars.query("SELECT * FROM results")
    pprint(res)


if False:
    testlayer = qgis.core.QgsVectorLayer(temppathsqlitefile, "myvlayer", "virtual")


print('')
print('*-*-*-*-*-*-*-*-**-*-*-*')
print(testlayer.isValid())
print(testlayer.getFeatures().__next__().attributes())
print('***')
print('exists : ' , os.path.isfile(pathsqlite) )