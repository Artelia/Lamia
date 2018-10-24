# -*- coding: utf-8 -*-



import os
import sys



import qgis

import datetime

import qgis.gui



import qgis.utils


import shutil
from qgis.PyQt import uic, QtCore


from Lamia.Lamia.dialog.InspectionDigue_windowwidget import InspectiondigueWindowWidget

try:
    from qgis.PyQt.QtGui import (QWidget,QDialog,QMainWindow)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget,QDialog,QMainWindow)

"""
class UserUI(QMainWindow):

    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'mainwindows.ui')
        uic.loadUi(uipath, self)
"""


class UserUI(QDialog):

    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'mainwindows_1.ui')
        uic.loadUi(uipath, self)




class mainClass(QtCore.QObject):

    def __init__(self  ):
        QtCore.QObject.__init__(self)

    def run(self,canvas, loadfile=True, typedb="spatialite"):
        # postgis  spatialite

        typedb = "spatialite"

        print('begin')
        wind = InspectiondigueWindowWidget(canvas)

        stylesheet = """
                    QMainWindow{
                                background-color: rgba(0, 55, 90,80);
                                }
                    """
        stylesheet = ''
        wind.setStyleSheet(stylesheet)


        wind.setParent(None)

        print('InspectiondigueWindowWidget loaded')

        if loadfile:
            if typedb == "spatialite":
                # path = os.path.normpath( 'I://FLUVIAL//4352024_33_Conformite_digues_BM//6_Reglementaire//61_Calculs//Basedonnees//201708_SIJALAG//BD_SIJALAG_ind10.sqlite')
                # path = os.path.normpath('I://FLUVIAL//4352024_33_Conformite_digues_BM//6_Reglementaire//61_Calculs//Basedonnees//201709_RD//BD_Rivedroite_ind4.sqlite')
                # path = os.path.normpath('I://FLUVIAL//4352024_33_Conformite_digues_BM//6_Reglementaire//61_Calculs//Basedonnees//201710_Begles//BD_Begles_ind10.sqlite')
                # path = os.path.normpath( 'C://Users//patrice.verchere//Desktop//VTA_Capa.sqlite')
                # path = os.path.normpath('C://000_testdigue//digues_BM//BD_SIJALAG_ind10.sqlite')
                # path = os.path.normpath('C://000_testdigue//temp_VNF//test01.sqlite')
                # path = os.path.normpath('C://000_testdigue//temp_digue//test01.sqlite')
                # path = os.path.normpath('C://000_testdigue//temp_ass//test01.sqlite')
                # path = os.path.normpath('C://000_testdigue//temp_default//test01.sqlite')
                # path = os.path.normpath('C://000_testdigue//temp_basedefault//test01.sqlite')
                # path = os.path.normpath('C://000_testdigue//temp_baseassainissement//test01.sqlite')

                # path = os.path.normpath("C://000_testdigue//convertBM//TO//BD_SIJALAG_ind10.sqlite")
                # path = os.path.normpath("C://000_testdigue//URBAIN//TO//SLT.sqlite")
                # path = "I://URBAIN//4352260_87_ELAN_EtudeAEP_EU//5_Etude//01_SIG//Qgs//SQLITE//Nantiat3.sqlite"
                # path = "M://FR//BOR//EE//URBAIN//4352240_87_NOBLAT_EtudeAEP_EU_EP//5_Etude//01_SIG//sqlite//La_Geneytouse2.sqlite"
                # path = "C://000_testdigue//URBAIN//Nantiat2.sqlite"
                # path = "C://000_testdigue//URBAIN//autre//SLT1.sqlite"
                # path = "C://000_testdigue//temp_base//test01.sqlite"
                #path = os.path.normpath("C://000_testdigue//201710_Begles//BD_Begles_ind13.sqlite")
                # path = os.path.normpath("C://000_testdigue//voncent//Plaisance_ind0.sqlite")

                # path = "C://000_testdigue//URBAIN//La_Geneytouse2.sqlite"
                # path = os.path.normpath('C://000_testdigue//temp_VNF//bief2 roanne//bief2 roanne.sqlite')
                #path = os.path.normpath('C://000_testdigue//temp_VNF//test03new.sqlite')
                path = os.path.normpath('C://000_testdigue//temp_base2_digue//test01.sqlite')
                path = os.path.normpath('C://000_testdigue//temp_base2_assainissement//test01.sqlite')
                # path = "C://000_testdigue//URBAIN//La_Geneytouse2.sqlite"
                # path = os.path.normpath('I:\\URBAIN\\4352260_87_ELAN_EtudeAEP_EU\\5_Etude\\01_SIG\\SQLITE\\Compreignac\\Compreignac.sqlite')
                # path = "C://000_testdigue//convertBM2//TO//BD_Begles_ind17.sqlite"

                # path = "C://000_testdigue//convertBM2//TO//BD_Rivedroite_ind6.sqlite"

                # path = "C://000_testdigue//convertBM2//TO//BD_Begles_ind17_test.sqlite"
                # path = "C://000_testdigue//convertBM2//TO//BD_SIJALAG_ind15.sqlite"
                # path = "C://000_testdigue//convertBM2//TO//BD_BMtotal_ind0.sqlite"
                # path = "C://000_testdigue//convertBM2//TO//export2.sqlite"
                # path = "C://000_testdigue//convertBM2//TO//BD_Rivedroite_ind6.sqlite"

                # path = "c://000_testdigue//convertBM2//Export//BdRiveDroite//export3.sqlite"
                # path = "c://000_testdigue//convertBM2//importest//BD_totale.sqlite"

                #path = os.path.normpath('C://000_testdigue//temp_base2_digue//test01.sqlite')
                #path = os.path.normpath('C://000_testdigue//temp_base2_digue_terrain//original//test01.sqlite')
                #path = os.path.normpath('C://000_testdigue//temp_base2_digue_terrain//originalmodifie//test01modif.sqlite')
                #path = os.path.normpath('C://000_testdigue//temp_base2_digue_terrain//terrain//terrain.sqlite')
                #path = os.path.normpath('C://000_testdigue//temp_base2_digue//test01_importterrain.sqlite')

                #path = os.path.normpath('C://000_testdigue//temp_base2_digue_terrain2//original//test02.sqlite')
                #path = os.path.normpath('C://000_testdigue//temp_base2_digue_terrain2//terrain//test02terrain.sqlite')
                # path = os.path.normpath('C://000_testdigue//temp_base2_digue_terrain2//originalmodif//test01modif.sqlite')
                # path = os.path.normpath('C://000_testdigue//temp_base2_digue_terrain2//terrain2//test02terrain.sqlite')
                # path = os.path.normpath('C://000_testdigue//temp_base2_digue_terrain2//originalmodif2//test02modif.sqlite')

                path = "C://Users//patrice.verchere//Documents//GitHub//Lamia//Lamia//test//02_test_importdb//test01//02_modif//test01.sqlite"
                #path = "C://Users//patrice.verchere//Documents//GitHub//Lamia//Lamia//test//02_test_importdb//test01//03_fusion_modif_terrain//test01.sqlite"
                # path = os.path.normpath('C://000_testdigue//temp_base2_assainissement//test1.sqlite')
                #path = os.path.normpath('C://Users//patrice.verchere//Documents//GitHub//Lamia//Lamia//test//02_test_importdb//test03//to//test01_terrain.sqlite')
                path = os.path.normpath("C://Users//patrice.verchere//Documents//GitHub//Lamia//Lamia//test//02_test_importdb//test04//01_original//terrain.sqlite")
                #path = os.path.normpath("C://Users//patrice.verchere//Documents//GitHub//Lamia//Lamia//test//02_test_importdb//test04//02_terrain//test01.sqlite")
                # path = os.path.normpath("C://Users//patrice.verchere//Documents//GitHub//Lamia//Lamia//test//02_test_importdb//test04//03_fusion_modif_terrain//test01.sqlite")

                path = os.path.normpath("C://Users//patrice.verchere//Documents//GitHub//Lamia//Lamia//test//02_test_export//BD_totale.sqlite")
                wind.dbase.loadQgisVectorLayers(path)

            elif typedb == "postgis":
                wind.dbase.loadQgisVectorLayers(dbasetype='postgis', dbname='PVR_test', schema='lamia_base2_digue',
                                                user='postgres',
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
            # print("versioning", wind.dbase.revisionwork)

            wind.dbase.printsql = False

            if True:

                mainwin = UserUI()

                mainwin.frame.layout().addWidget(canvas)
                mainwin.frame_2.layout().addWidget(wind)
                if False:
                    wind.loadUiDesktop()
                    wind.applyVisualMode()

                mainwin.setParent(None)


                if False:
                    wind.dbase.createNewLineVersion('Infralineaire',3)

                    sys.exit()

                # wind.menutools[0].Noeud('c://test1.shp')
                #wind.menutools[1].launchDialog()

                if False:
                    # sql = "SELECT MAX(pk_revision) FROM Revision"
                    # maxverswind.dbase.query(sql)
                    datesuppr = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                    sql = "INSERT INTO Revision(datetimerevision, commentaire) VALUES('" + datesuppr + "','test')"
                    wind.dbase.query(sql)

                print('iface',wind.dbase.qgsiface)
                print('ver', wind.dbase.qgisversion_int)

                if False:
                    res1, res2 = wind.dbase.searchChildfeatureFromPkObjet(5)
                    print('result', res1, res2)

                #mainwin.show()
                mainwin.exec_()
                canvas.refresh()

                print('ok')

            if False:
                canvas.show()
                canvas.refresh()
                wind.show()



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
            # path = "I://URBAIN//4352260_87_ELAN_EtudeAEP_EU//5_Etude//01_SIG//Qgs//SQLITE//Nantiat3.sqlite"
            # path = "M://FR//BOR//EE//URBAIN//4352240_87_NOBLAT_EtudeAEP_EU_EP//5_Etude//01_SIG//sqlite//La_Geneytouse2.sqlite"
            # path = "C://000_testdigue//URBAIN//Nantiat2.sqlite"
            path = "C://000_testdigue//URBAIN//autre//SLT1.sqlite"
            # path = "C://000_testdigue//temp_base//test01.sqlite"



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

        # wind.dbase.printsql = True

        if True:

            mainwin = UserUI()

            mainwin.frame.layout().addWidget(canvas)
            mainwin.frame_2.layout().addWidget(wind)
            if False:
                wind.loadUiDesktop()
                wind.applyVisualMode()

            mainwin.setParent(None)
            mainwin.show()
            #mainwin.exec_()
            canvas.refresh()

            print('ok')


        if False:
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
if False:
    testCoreParserValue(canvas,True,"spatialite")
    app.exec_()
    qgis.core.QgsApplication.exitQgis()

if True:
    program = mainClass()
    program.run(canvas, True, "spatialite")
    app.exec_()
    qgis.core.QgsApplication.exitQgis()

print('ok')
