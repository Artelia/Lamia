# -*- coding: utf-8 -*-



import os
import sys

import time

import qgis



import qgis.gui



import qgis.utils


import shutil

try:
    from qgis.PyQt.QtGui import (QApplication)
except ImportError:
    from qgis.PyQt.QtWidgets import (QApplication)



from Lamia.Lamia.dialog.InspectionDigue_windowwidget import InspectiondigueWindowWidget




def testCoreParserValue(canvas, loadfile=True, typedb="spatialite"):

    # spatialite   postgis
    typedb = "spatialite"


    print('begin')
    wind = InspectiondigueWindowWidget(canvas)
    wind.setParent(None)

    print('InspectiondigueWindowWidget loaded')

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
            # path = os.path.normpath('C://000_testdigue//temp_default//test01.sqlite')
            # path = os.path.normpath('C://000_testdigue//temp_basedefault//test01.sqlite')
            #path = os.path.normpath('C://000_testdigue//temp_baseassainissement//test01.sqlite')


            # path = os.path.normpath("C://000_testdigue//convertBM//TO//BD_SIJALAG_ind10.sqlite")
            # path = os.path.normpath("C://000_testdigue//URBAIN//TO//SLT.sqlite")
            #path = "I://URBAIN//4352260_87_ELAN_EtudeAEP_EU//5_Etude//01_SIG//Qgs//SQLITE//Nantiat2.sqlite"
            #path = "M://FR//BOR//EE//URBAIN//4352240_87_NOBLAT_EtudeAEP_EU_EP//5_Etude//01_SIG//sqlite//La_Geneytouse2.sqlite"
            path = "C://000_testdigue//temp_baseassainissement//test01.sqlite"


            wind.dbase.loadQgisVectorLayers(path)

        elif typedb == "postgis":
            wind.dbase.loadQgisVectorLayers(dbasetype='postgis', dbname='PVR_test', schema='lamia_default', user='postgres',
                                            host='localhost',
                                            password='PVR', port=5432)

    if True:
        print('loadQgisVectorLayers done')
        # canvas.setDestinationCrs(wind.dbase.dbasetables['Infralineaire']['layer'].crs())
        canvas.setDestinationCrs(qgis.core.QgsCoordinateReferenceSystem(2154))

        layerstoadd = []
        layert = wind.dbase.dbasetables['Infralineaire']['layerqgis']

        if True:
            for tablename in wind.dbase.dbasetables.keys():
                if sys.version_info.major == 2:
                    layerstoadd.append(qgis.gui.QgsMapCanvasLayer(wind.dbase.dbasetables[tablename]['layerqgis']))
                elif sys.version_info.major == 3:
                    layerstoadd.append(wind.dbase.dbasetables[tablename]['layerqgis'])

            if sys.version_info.major == 2:
                 canvas.setLayerSet(layerstoadd)
            else:
                canvas.setLayers(layerstoadd)
            # canvas.show()
            # canvas.setExtent(qgis.core.QgsRectangle(0, 0, 1, 1))
            canvas.setExtent(wind.dbase.dbasetables['Infralineaire']['layer'].extent())
            canvas.refresh()

        print('Layers loaded')
        print("versioning", wind.dbase.revisionwork)

        wind.dbase.printsql = False

        canvas.show()
        canvas.refresh()
        wind.show()

        # Infralineaire Noeud

        if True:
            noeudwdg = wind.dbase.dbasetables['Noeud']['widget'][0]
            noeudwdg.featureSelected(None)
            noeudwdg.setTempGeometry([qgis.core.QgsPoint(0, 0), qgis.core.QgsPoint(1, 1)])
            noeudwdg.saveFeature()


        if False:
            for i in range(1000):
                timestart = time.clock()
                noeudwdg = wind.dbase.dbasetables['Noeud']['widget'][0]
                noeudwdg.featureSelected(None)
                noeudwdg.setTempGeometry([qgis.core.QgsPoint(0,0),qgis.core.QgsPoint(1,1) ])
                noeudwdg.saveFeature()
                print('time ' , str( time.clock() - timestart),i )



        if False:
            noeudwdg = wind.dbase.dbasetables['Equipement']['widget'][0]
            noeudwdg.featureSelected(None)
            noeudwdg.setTempGeometry([qgis.core.QgsPoint(0,0),qgis.core.QgsPoint(1,1) ])
            noeudwdg.saveFeature()

        print('fin')


# *********************************************************************************************************************
# ******************************************   MAIN      *************************************************************
# *********************************************************************************************************************




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



print('ok0')
app = qgis.core.QgsApplication([], True)
print('ok1')
qgis.core.QgsApplication.setPrefixPath(qgis_path, True)
qgis.core.QgsApplication.initQgis()
print('ok2')
canvas = qgis.gui.QgsMapCanvas()
canvas.enableAntiAliasing(True)

print('begin1')



# spatialite   postgis
if True:
    testCoreParserValue(canvas,True,"spatialite")


    app.exec_()
    qgis.core.QgsApplication.exitQgis()
print('ok')
