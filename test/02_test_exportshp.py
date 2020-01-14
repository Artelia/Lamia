# -*- coding: utf-8 -*-





from Lamia.test.AbstractTest import Test
import os
import sys
import datetime


class TestMain(Test):

    def __init__(self):
        super(TestMain, self).__init__()


    def testMethod(self):
        self.createWin()

        path = os.path.normpath("C://Users//patrice.verchere//Documents//GitHub//Lamia//test//02_test_export//BD_totale1.sqlite")
        path = "C://000_testdigue//temp_base2_assainissement//test01.sqlite"
        path = "M://FR//BOR//VT//URBAIN//4352329-33-GPMB-diag complet EU et EP-Bacalan, Le Verdon, Pauillac et Blaye//05-ETUDES//05-1-Dessins-plans//6-lamia//gpmb_ind0.sqlite"
        path = "M://FR//BOR//VT//FLUVIAL//4352024_33_Conformite_digues_BM//6_Reglementaire//61_Calculs//Basedonnees//BD_totale_ind6.sqlite"

        path ="M://FR//BOR//VT//FLUVIAL//4352408_33_CCMA_VTA_Valeyrac//6_Reglementaire//61_Calculs//Lamia2//valeyrac_ind0.sqlite"
        path = "M://FR//BOR//VT//FLUVIAL//4352408_33_CCMA_VTA_Valeyrac//6_Reglementaire//61_Calculs//Lamia2//valeyrac_ind0.sqlite"
        path = 'C://000_testdigue//temp_base2_parking//test01.sqlite'
        path = "C://000_testdigue//temp_base2_ass2//test01.sqlite"
        path = "C://000_testdigue//testdigue//BD_totale_ind6.sqlite"

        path = "M://FR//BOR//VT//FLUVIAL//4352024_33_Conformite_digues_BM//6_Reglementaire//61_Calculs//Basedonnees//BD_totale_ind6.sqlite"

        path = "C://000_testdigue//0_bastien//LANDY.sqlite"
        path = "C://000_testdigue//Manon_AEP//EAU POTABLE S1.sqlite"
        path = "C://000_testdigue//temp_base2_tram2//test01.sqlite"
        path = "C://000_testdigue//0_bastien//LANDY.sqlite"
        path = "M://FR//BOR//VT//URBAIN//4352502-87-CDC_HLEM//5_ETUDES//51_SIG//SQLITE//Berneuil//Berneuil.sqlite"
        path = "C://000_testdigue//000_test_virginie//ROMORANTIN BDD.sqlite"

        self.wind.dbase.loadQgisVectorLayers(path)
        self.wind.loadUiDesktop()

        self.createMainWin()



        if True:       # test of desktop version
            self.wind.loadUiDesktop()
            self.dbase.visualmode = 4

        self.dbase.printsql = False


        wdg = None
        for i, tool in enumerate(self.wind.tools):
            print(tool.__class__.__name__)
            if 'ExportShapefile' in tool.__class__.__name__:
                print('ok')
                wdg = self.wind.tools[i]
                break
        wdg.changePropertiesWidget()
        self.wind.MaintreeWidget.setCurrentItem(wdg.qtreewidgetitem)

        # BM_Infralineaire    BM_Equipement_point       BM_Equipement_ligne
        # BM_Photo   BM_TcObjetRessource  BM_Graphdata   BM_TcObjetRessource
        #  BM_Desordres_ligne    BM_Desordres_point   BM_Observation
        # 00_Desordres_observation_actif   00_Desordres_observation_total  00_Equipement_observation_actif
        # Export_total      Infralineaire    Noeud      Equipement      Export_total
        typeexport = 'Infralineaire'

        if False:
            rootpath = "M://FR//BOR//VT//FLUVIAL//4352024_33_Conformite_digues_BM//6_Reglementaire//63_Rapports//20190200_BD_exportshp//20190415_ind1"
            exportfile = os.path.join(rootpath, typeexport + ".shp")
        if False:
            rootpath = "C://000_testdigue//temp"

            exportfile = os.path.join(rootpath, typeexport + ".shp")

        if False:
            rootpath = "C:"
            exportfile = os.path.join(rootpath, typeexport + ".shp")

        exportfile = os.path.normpath("C://000_testdigue//testshape.shp")
        # self.wind.dbase.dbasetables['Zonegeo']['layerqgis'].selectByIds([5])
        wdg.userwdgfield.lineEdit_nom.setText(exportfile)

        #indextypeexport = wdg.userwdgfield.comboBox_type.findText(typeexport)
        #wdg.userwdgfield.comboBox_type.setCurrentIndex(indextypeexport)

        indextypeexport = wdg.filemanager.comboBox_files.findText(typeexport)
        wdg.filemanager.comboBox_files.setCurrentIndex(indextypeexport)


        # self.mainwin.exec_()

        wdg.prepareData()







test = TestMain()
test.launchTest()
sys.exit()

