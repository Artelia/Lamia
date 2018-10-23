# -*- coding: utf-8 -*-




from Lamia.Lamia.test.AbstractTest import Test
import os
import datetime


class TestMain(Test):

    def __init__(self):
        super(TestMain, self).__init__()


    def testMethod(self):
        self.createWin()

        path = os.path.normpath("C://Users//patrice.verchere//Documents//GitHub//Lamia//Lamia//test//02_test_export//BD_totale.sqlite")
        self.dbase.loadQgisVectorLayers(path)

        self.loadLayersInCanvas()

        self.createMainWin()

        # eventualy add new version
        if False:
            datesuppr = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            sql = "INSERT INTO Revision(datetimerevision, commentaire) VALUES('" + datesuppr + "','test')"
            self.dbase.query(sql)


        self.mainwin.exec_()


test = TestMain()
test.launchTest()


















import os
import qgis
import qgis.gui
import shutil
from Lamia.Lamia.dialog.InspectionDigue_windowwidget import InspectiondigueWindowWidget


def testImportExport(canvas, loadfile=True, typedb="spatialite"):

    print('begin')
    wind = InspectiondigueWindowWidget(canvas)
    wind.setParent(None)

    # export importnouvelle importterrain exporttotal
    testcherche = 'exporttotal'


    if loadfile:
        if typedb == "spatialite":
            if False:
                # shutil.copy("C://000_testdigue//convertBM2//TO//BD_SIJALAG_ind15.sqlite", "C://000_testdigue//convertBM2//TO//BD_SIJALAG_ind15_test.sqlite")
                path = "C://000_testdigue//convertBM2//import//BD_totale.sqlite"    #sijalag
            # path = os.path.normpath('C://000_testdigue//temp_base2_digue_terrain2//originalmodif//test01modif.sqlite')
            pathexport = os.path.join(os.path.dirname(__file__), '02_test_importdb', 'test01', '01_original', 'test01.sqlite')
            pathimportterrain = os.path.join(os.path.dirname(__file__),  '02_test_importdb', 'test01','03_fusion_modif_terrain','test01.sqlite' )

            if testcherche == 'export':
                wind.dbase.loadQgisVectorLayers(pathexport)

            elif testcherche == 'importterrain':

                pathmodif = os.path.join(os.path.dirname(__file__),  '02_test_importdb', 'test01','02_modif','test01.sqlite' )

                dirtodelete = os.path.dirname(pathimportterrain)
                shutil.rmtree(dirtodelete, ignore_errors=True)
                shutil.copytree(os.path.dirname(pathmodif), dirtodelete)

                wind.dbase.loadQgisVectorLayers(pathimportterrain)

            elif testcherche == 'importnouvelle':
                spatialitefile = os.path.join(os.path.dirname(__file__),  '02_test_importdb', 'test02','to','BD_totale.sqlite' )
                wind.dbase.createDbase(slfile=spatialitefile, crs=3945, worktype='Base2_digue')
                # wind.dbase.loadQgisVectorLayers(spatialitefile)

            elif testcherche == 'exporttotal':
                pathimportterrain = os.path.join(os.path.dirname(__file__),  '02_test_importdb', 'test03','from','BD_totale.sqlite' )
                wind.dbase.loadQgisVectorLayers(pathimportterrain)

                # wind.dbase.loadQgisVectorLayers(spatialitefile)

        elif typedb == "postgis":
            wind.dbase.loadQgisVectorLayers(dbasetype='postgis', dbname='PVR_test', schema='exportbm', user='postgres',
                                            host='localhost',
                                            password='PVR', port=5432)

        wind.dbase.printsql = False

        if testcherche == 'export':

            pathtoexport = os.path.join(os.path.dirname(__file__),  '02_test_importdb', 'test01','02_terrain', 'test01_terrain.sqlite' )
            wind.dbase.exportDbase(pathtoexport)

            pathmodif = os.path.join(os.path.dirname(__file__),  '02_test_importdb', 'test01','02_modif', 'test01_modif.sqlite' )
            dirtodelete = os.path.dirname(pathmodif)
            shutil.rmtree(dirtodelete, ignore_errors=True)
            shutil.copytree(os.path.dirname(pathexport), dirtodelete)

            print('finisehd')


        elif testcherche == 'exporttotal':

            pathtoexport = os.path.join(os.path.dirname(__file__),  '02_test_importdb', 'test03','to', 'test01_terrain.sqlite' )
            wind.dbase.exportDbase(pathtoexport)



            print('finisehd')

        elif testcherche == 'importterrain':
            pathterrain = os.path.join(os.path.dirname(__file__),  '02_test_importdb', 'test01','02_terrain', 'test01_terrain.sqlite' )
            wind.importDBase(slfile=pathterrain, typeimport='import_terrain')

        elif testcherche == 'importnouvelle':

            if True:
                path1 = os.path.join(os.path.dirname(__file__), '02_test_importdb', 'test02', 'from','BD_SIJALAG_ind15.sqlite')
                wind.importDBase(slfile=path1)
            if True:
                path1 = os.path.join(os.path.dirname(__file__),  '02_test_importdb', 'test02','from','BD_Begles_ind17.sqlite' )
                wind.importDBase(slfile=path1)
            if True:
                path1 = os.path.join(os.path.dirname(__file__), '02_test_importdb', 'test02', 'from', 'BD_Rivedroite_ind6.sqlite')
                wind.importDBase(slfile=path1)




        print("Finished")



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

app = qgis.core.QgsApplication([], True)
qgis.core.QgsApplication.setPrefixPath(qgis_path, True)
qgis.core.QgsApplication.initQgis()
canvas = qgis.gui.QgsMapCanvas()
canvas.enableAntiAliasing(True)


# spatialite   postgis
# Infrastructure lineaire   #  Equipements hydrauliques #Desordres
# c://testrapport.pdf
testImportExport(canvas,True,typedb="spatialite")


app.exec_()
qgis.core.QgsApplication.exitQgis()
print('ok')
