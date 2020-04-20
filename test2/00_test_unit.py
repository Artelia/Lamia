# -*- coding: utf-8 -*-
import os
import sys
import qgis
import qgis.gui
import qgis.utils
from Lamia.Lamia.dialog.InspectionDigue_windowwidget import InspectiondigueWindowWidget



def testCoreParserValue(canvas, loadfile=True, typedb="spatialite"):

    print('begin')
    wind = InspectiondigueWindowWidget(canvas)
    wind.setParent(None)
    print('Windows widget created')


    if loadfile:
        if typedb == "spatialite":
            #path = os.path.normpath( 'I://FLUVIAL//4352024_33_Conformite_digues_BM//6_Reglementaire//61_Calculs//Basedonnees//201708_SIJALAG//BD_SIJALAG_ind10.sqlite')
            # path = os.path.normpath('I://FLUVIAL//4352024_33_Conformite_digues_BM//6_Reglementaire//61_Calculs//Basedonnees//201709_RD//BD_Rivedroite_ind4.sqlite')
            # path = os.path.normpath('I://FLUVIAL//4352024_33_Conformite_digues_BM//6_Reglementaire//61_Calculs//Basedonnees//201710_Begles//BD_Begles_ind10.sqlite')
            # path = os.path.normpath( 'C://Users//patrice.verchere//Desktop//VTA_Capa.sqlite')
            # path = os.path.normpath('C://000_testdigue//digues_BM//BD_SIJALAG_ind10.sqlite')
            # path = os.path.normpath('C://000_testdigue//temp_VNF//test01.sqlite')
            # path = os.path.normpath('C://000_testdigue//temp_digue//test01.sqlite')
            # path = os.path.normpath('C://000_testdigue//temp_ass//test01.sqlite')
            path = os.path.normpath('C://000_testdigue//temp_default//test01.sqlite')
            wind.dbase.loadQgisVectorLayers(path)
            print('qgis layers loaded')

        elif typedb == "postgis":
            wind.dbase.loadQgisVectorLayers(dbasetype='postgis', dbname='PVR_test', schema='exportbm', user='postgres',
                                            host='localhost',
                                            password='PVR', port=5432)
            print('qgis layers loaded')

    if False:
        ###Load layers in canvas
        canvas.setDestinationCrs(qgis.core.QgsCoordinateReferenceSystem(2154))
        layerstoadd = []
        #layert = wind.dbase.dbasetables['Infralineaire']['layerqgis']

        for tablename in wind.dbase.dbasetables.keys():
            if sys.version_info.major == 2:
                layerstoadd.append(qgis.gui.QgsMapCanvasLayer(wind.dbase.dbasetables[tablename]['layerqgis']))
            elif sys.version_info.major == 3:
                layerstoadd.append(wind.dbase.dbasetables[tablename]['layerqgis'])

        if sys.version_info.major == 2:
             canvas.setLayerSet(layerstoadd)
        else:
            canvas.setLayers(layerstoadd)
        canvas.setExtent(wind.dbase.dbasetables['Infralineaire']['layer'].extent())
        canvas.refresh()

        print('Layers loaded in canvas')

        #wind.dbase.printsql = True
        canvas.show()
        canvas.refresh()
        wind.show()

    #Creation test
    if True:
        wind.dbase.printsql = True
        #infralineaire
        infralineairewdg = wind.dbase.dbasetables['Infralineaire']['widget'][0]
        infralineairewdg.featureSelected(None)
        infralineairewdg.createorresetRubberband(0)
        infralineairewdg.setTempGeometry([qgis.core.QgsPoint(0,0),qgis.core.QgsPoint(1,1)])
        infralineairewdg.saveFeature()

        sql = "INSERT INTO Revision (commentaire ) VALUES('v2') "
        wind.dbase.query(sql)
        wind.dbase.commit()


        wind.dbase.currentrevision = 2
        wind.dbase.updateWorkingDate()







# *********************************************************************************************************************
# ******************************************   MAIN      *************************************************************
# *********************************************************************************************************************


try:
    qgisversion_int = qgis.utils.QGis.QGIS_VERSION_INT
except AttributeError:  #qgis 3
    qgisversion_int = qgis.utils.Qgis.QGIS_VERSION_INT
print('version qgis : ',qgisversion_int)

if int(str(qgisversion_int)[0:3]) < 220:
    qgis_path = "C://OSGeo4W64//apps//qgis-ltr"
else:
    qgis_path = "C://OSGeo4W64//apps//qgis"


app = qgis.core.QgsApplication([], True)
qgis.core.QgsApplication.setPrefixPath(qgis_path, True)
qgis.core.QgsApplication.initQgis()
canvas = qgis.gui.QgsMapCanvas()
canvas.enableAntiAliasing(True)

print('Qgis initialized')

# spatialite   postgis
if True:
    testCoreParserValue(canvas,True,"spatialite")
    app.exec_()
    qgis.core.QgsApplication.exitQgis()
print('ok')
