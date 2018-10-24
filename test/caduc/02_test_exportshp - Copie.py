# -*- coding: utf-8 -*-

import os
import qgis
import qgis.gui
import shutil
from Lamia.Lamia.dialog.InspectionDigue_windowwidget import InspectiondigueWindowWidget


def testRapport(canvas, loadfile=True, typedb="spatialite",tabletype=None, pdffile=None ):

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
            # path = os.path.normpath('C://000_testdigue//temp//test01.sqlite')
            # path = os.path.normpath( 'I://FLUVIAL//4352024_33_Conformite_digues_BM//6_Reglementaire//61_Calculs//Basedonnees//201708_SIJALAG//BD_SIJALAG_ind8.sqlite')
            # path = os.path.normpath('C://000_testdigue//temp//BD_Rivedroite_ind1.sqlite')
            #path = os.path.normpath('I://FLUVIAL//4352024_33_Conformite_digues_BM//6_Reglementaire//61_Calculs//Basedonnees//201710_Begles//BD_Begles_ind9.sqlite')
            #path = os.path.normpath('I://FLUVIAL//4352024_33_Conformite_digues_BM//6_Reglementaire//61_Calculs//Basedonnees//201709_RD//BD_Rivedroite_ind2.sqlite')
            path = os.path.normpath("C://000_testdigue//201710_Begles//BD_Begles_ind16.sqlite")
            path = os.path.normpath("C://000_testdigue//URBAIN//La_Geneytouse2.sqlite")
            path = os.path.normpath("C://Users//patrice.verchere//Documents//GitHub//Lamia//Lamia//test//02_test_export//BD_totale.sqlite")


            wind.dbase.loadQgisVectorLayers(path)
            wind.loadUiDesktop()

        elif typedb == "postgis":
            wind.dbase.loadQgisVectorLayers(dbasetype='postgis', dbname='PVR_test', schema='exportbm', user='postgres',
                                            host='localhost',
                                            password='PVR', port=5432)


    if False:
        wind.exportShapefile(tabletype=tabletype, pdffile=pdffile )

        print('fin')

    if True:
        wind.dbase.printsql = False
        indexrapport = None
        for i, menutool in enumerate(wind.menutools):
            #print('ook', menutool.__class__.__name__)
            if 'exportShapefile' in menutool.__class__.__name__ :
                #print('oooo',i)
                indexrapport = i
                break
        # Infralineaire_BM Equipement_point_BM Photo_BM Graphdata_BM Desordres_ligne_BM
        shp = os.path.normpath("C://Users//patrice.verchere//Documents//GitHub//Lamia//Lamia//test//02_test_export//testshape.shp")

        wind.dbase.dbasetables['Zonegeo']['layerqgis'].selectByIds([19])

        wind.menutools[indexrapport].prepareData('Infralineaire_BM', shp)



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

app = qgis.core.QgsApplication([], True)
qgis.core.QgsApplication.setPrefixPath(qgis_path, True)
qgis.core.QgsApplication.initQgis()
canvas = qgis.gui.QgsMapCanvas()
canvas.enableAntiAliasing(True)


# spatialite   postgis
# Infrastructure lineaire           Dernieres observations      Graphiques digue

# c://testexport.shp
testRapport(canvas,True,typedb="spatialite",tabletype="Infralineaire", pdffile="c://testexport.shp")


app.exec_()
qgis.core.QgsApplication.exitQgis()
print('ok')
