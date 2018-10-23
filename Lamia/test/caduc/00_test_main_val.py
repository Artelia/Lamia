# -*- coding: utf-8 -*-

import os
import qgis
import qgis.gui
import shutil
from Lamia.Lamia.dialog.InspectionDigue_windowwidget import InspectiondigueWindowWidget


def testCoreParserValue(canvas, loadfile=True, typedb="spatialite"):

    print('begin')
    wind = InspectiondigueWindowWidget(canvas)
    wind.setParent(None)

    if loadfile:
        if typedb == "spatialite":
            # path = os.path.normpath('C://Users//patrice.verchere//Documents//GitHub//InspectionDigue//DBASE//test1.sqlite')
            # path = os.path.normpath('c://000_testdigue//testdbase.sqlite')
            # path = os.path.normpath('C://000_testimportBM//BD_BM_ind1.sqlite')
            # path = os.path.normpath('C://000_testimportBM//BD_BM_ind3.sqlite')
            #path = os.path.normpath('C://001_travail_BM//BD_SIJALAG_ind0_travail2.sqlite')
            #path = os.path.normpath('I://FLUVIAL//4352024_33_Conformite_digues_BM//6_Reglementaire//61_Calculs//Basedonnees//201710_Begles//BD_Begles_ind0.sqlite')
            # path = os.path.normpath('C://000_testdigue//testBM//BD_Begles_ind0_JRS - Copie.sqlite')
            #path = os.path.normpath('C://000_testdigue//testBM//BD_Begles_ind3.sqlite')
            #path = os.path.normpath('C://000_testdigue//testBM//BD_Begles_ind0.sqlite')
            #path = os.path.normpath('C://Users//valentin.anjou//Desktop//BD_SIJALAG_ind7.sqlite')
            path = os.path.normpath('C://Users//valentin.anjou//Desktop//test.sqlite')


            wind.dbase.loadQgisVectorLayers(path)

        elif typedb == "postgis":
            wind.dbase.loadQgisVectorLayers(dbasetype='postgis', dbname='PVR_test', schema='exportbm', user='postgres',
                                            host='localhost',
                                            password='PVR', port=5432)

    if True:
        # canvas.setDestinationCrs(wind.dbase.dbasetables['Infralineaire']['layer'].crs())
        canvas.setDestinationCrs(qgis.core.QgsCoordinateReferenceSystem(2154))

        layerstoadd = []
        layert = wind.dbase.dbasetables['Infralineaire']['layerqgis']


        for tablename in wind.dbase.dbasetables.keys():
            layerstoadd.append(qgis.gui.QgsMapCanvasLayer(wind.dbase.dbasetables[tablename]['layerqgis']))

        canvas.setLayerSet(layerstoadd)
        # canvas.show()
        # canvas.setExtent(qgis.core.QgsRectangle(0, 0, 1, 1))
        canvas.setExtent(wind.dbase.dbasetables['Infralineaire']['layer'].extent())
        canvas.refresh()

        canvas.show()
        canvas.refresh()
        wind.show()

# *********************************************************************************************************************
# ******************************************   MAIN      *************************************************************
# *********************************************************************************************************************


if True:
    qgis_path = "C://OSGeo4W64//apps//qgis"
else:
    qgis_path = "C://OSGeo4W64//apps//qgis-dev"

app = qgis.core.QgsApplication([], True)
qgis.core.QgsApplication.setPrefixPath(qgis_path, True)
qgis.core.QgsApplication.initQgis()
canvas = qgis.gui.QgsMapCanvas()
canvas.enableAntiAliasing(True)


# spatialite   postgis
testCoreParserValue(canvas,True,"spatialite")


app.exec_()
qgis.core.QgsApplication.exitQgis()
print('ok')
