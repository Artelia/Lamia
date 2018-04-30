# -*- coding: utf-8 -*-



import os
import sys



import qgis



import qgis.gui



import qgis.utils


import shutil



from Lamia.Lamia.dialog.InspectionDigue_windowwidget import InspectiondigueWindowWidget




def testCoreParserValue(canvas, loadfile=True, typedb="spatialite"):

    print('begin')
    wind = InspectiondigueWindowWidget(canvas)
    wind.setParent(None)

    print('ok')

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
            # path = os.path.normpath('I://FLUVIAL//4352024_33_Conformite_digues_BM//6_Reglementaire//61_Calculs//Basedonnees//201710_Begles//BD_Begles_ind8.sqlite')
            # path = os.path.normpath( 'C://000_testdigue//temp//test01.sqlite')
            # path = os.path.normpath( 'I://FLUVIAL//4352024_33_Conformite_digues_BM//6_Reglementaire//61_Calculs//Basedonnees//201708_SIJALAG//BD_SIJALAG_ind4.sqlite')
            #path = os.path.normpath('C://000_testdigue//BM//BD_SIJALAG_ind4.sqlite')
            # path = os.path.normpath('C://000_testdigue//temp01//test01.sqlite')
            #path = os.path.normpath('C://000_testdigue//BD_Begles_ind8.sqlite')
            # path = os.path.normpath('C://000_testdigue//temp2//test01.sqlite')
            #path = os.path.normpath('C://00_Affaires//BM_digues//Base_donnees//Begles//BD_Begles_ind8.sqlite')
            # path = os.path.normpath( 'I://FLUVIAL//4352024_33_Conformite_digues_BM//6_Reglementaire//61_Calculs//Basedonnees//201708_SIJALAG//BD_SIJALAG_ind7.sqlite')
            path = os.path.normpath('C://000_testdigue//temp_VNF//test01.sqlite')
            # path = os.path.normpath('C://000_testdigue//temp_digue//test01.sqlite')

            wind.dbase.loadQgisVectorLayers(path)

        elif typedb == "postgis":
            wind.dbase.loadQgisVectorLayers(dbasetype='postgis', dbname='PVR_test', schema='exportbm', user='postgres',
                                            host='localhost',
                                            password='PVR', port=5432)

    if True:
        print('ok00')
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
            print('ok0')
            if sys.version_info.major == 2:
                 canvas.setLayerSet(layerstoadd)
            else:
                canvas.setLayers(layerstoadd)
            # canvas.show()
            # canvas.setExtent(qgis.core.QgsRectangle(0, 0, 1, 1))
            canvas.setExtent(wind.dbase.dbasetables['Infralineaire']['layer'].extent())
            canvas.refresh()

        print('ok1')

        canvas.show()
        canvas.refresh()
        wind.show()

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
