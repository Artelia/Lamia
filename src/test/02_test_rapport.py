# -*- coding: utf-8 -*-

import os
import qgis
import qgis.gui
import shutil
from InspectionDigueV2.src.dialog.InspectionDigue_windowwidget import InspectiondigueWindowWidget


def testRapport(canvas, loadfile=True, typedb="spatialite",reporttype=None, pdffile=None ):

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
            path = os.path.normpath('C://000_testdigue//testBM//BD_Begles_ind0.sqlite')
            wind.dbase.loadQgisVectorLayers(path)

        elif typedb == "postgis":
            wind.dbase.loadQgisVectorLayers(dbasetype='postgis', dbname='PVR_test', schema='exportbm', user='postgres',
                                            host='localhost',
                                            password='PVR', port=5432)


    if True:
        wind.printRapport(reporttype=reporttype, pdffile=pdffile)

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
# Infrastructure lineaire   #  Equipements hydrauliques
# c://testrapport.pdf
testRapport(canvas,True,typedb="spatialite",reporttype="Equipements hydrauliques", pdffile="c://testrapport.pdf")


app.exec_()
qgis.core.QgsApplication.exitQgis()
print('ok')
