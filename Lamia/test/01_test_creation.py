# -*- coding: utf-8 -*-


import os
import qgis
import qgis.gui
import shutil
#import time
#from pyspatialite import dbapi2 as db
from qgis.PyQt import QtGui

from InspectionDigueV2.src.dialog.InspectionDigue_dockwidget import InspectiondigueDockWidget
from Lamia.Lamia.dialog.InspectionDigue_windowwidget import InspectiondigueWindowWidget



def testDbaseCreation(canvas, typedb="spatialite"):
    print('begin')
    wind = InspectiondigueWindowWidget(canvas)
    crs = 3945

    if typedb == "spatialite":
        # Digue VNF  Assainissement
        typebase = 'Digue'
        if typebase == 'VNF':
            spatialitefile = 'C://000_testdigue//temp_VNF//test01.sqlite'
        elif typebase == 'Digue':
            spatialitefile = 'C://000_testdigue//temp_digue//test01.sqlite'
        elif typebase == 'Assainissement':
            spatialitefile = 'C://000_testdigue//temp_ass//test01.sqlite'

        #shutil.rmtree('c://000_testdigue//BDspatialite')

        originalfile = os.path.join(os.path.dirname(__file__), '..', 'DBASE', 'DBase_ind0.sqlite')
        shutil.copyfile(originalfile, spatialitefile)

        #wind.dbase.createDbase(file=spatialitefile, crs=crs, type='Digue', dbaseressourcesdirectory=spatialitedir)

        wind.dbase.createDbase(file=spatialitefile, crs=crs, type=typebase)

    elif typedb == "postgis":
        wind.dbase.createDbase(crs=crs, type='Digue', dbasetype='postgis', dbname='PVR_test', schema='diguebebe',
                               user='postgres', host='localhost',
                               password='PVR', dbaseressourcesdirectory='c://000_testdigue//BDpostgis')


    print('fin')



try:
    qgisversion_int = qgis.utils.QGis.QGIS_VERSION_INT
except AttributeError:  #qgis 3
    qgisversion_int = qgis.utils.Qgis.QGIS_VERSION_INT

print(qgisversion_int)

if int(str(qgisversion_int)[0:3]) < 220:
    qgis_path = "C://OSGeo4W64//apps//qgis-ltr"
else:
    qgis_path = "C://OSGeo4W64//apps//qgis"
    #os.environ["QT_QPA_PLATFORM"] = "offscreen"


"""
if False:
    qgis_path = "C://OSGeo4W64//apps//qgis"
else:
    qgis_path = "C://OSGeo4W64//apps//qgis-dev"
"""

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
