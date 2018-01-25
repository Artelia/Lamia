# -*- coding: utf-8 -*-


import os
import qgis
import qgis.gui
import shutil
#import time
from pyspatialite import dbapi2 as db
from qgis.PyQt import QtGui

from InspectionDigueV2.src.dialog.InspectionDigue_dockwidget import InspectiondigueDockWidget
from Lamia.src.dialog.InspectionDigue_windowwidget import InspectiondigueWindowWidget



def testDbaseCreation(canvas, typedb="spatialite"):
    print('begin')
    wind = InspectiondigueWindowWidget(canvas)
    crs = 3945

    if typedb == "spatialite":
        spatialitefile = 'C://000_testdigue//tesvalentin//test03.sqlite'
        #spatialitedir = 'C://000_testimportBM//BDspatialite'

        #shutil.rmtree('c://000_testdigue//BDspatialite')

        originalfile = os.path.join(os.path.dirname(__file__), '..', 'DBASE', 'DBase_ind0.sqlite')
        shutil.copyfile(originalfile, spatialitefile)

        #wind.dbase.createDbase(file=spatialitefile, crs=crs, type='Digue', dbaseressourcesdirectory=spatialitedir)
        wind.dbase.createDbase(file=spatialitefile, crs=crs, type='Digue')

    elif typedb == "postgis":
        wind.dbase.createDbase(crs=crs, type='Digue', dbasetype='postgis', dbname='PVR_test', schema='diguebebe',
                               user='postgres', host='localhost',
                               password='PVR', dbaseressourcesdirectory='c://000_testdigue//BDpostgis')


    print('fin')




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
testDbaseCreation(canvas,typedb="spatialite")

app.exec_()
qgis.core.QgsApplication.exitQgis()
print('ok')
