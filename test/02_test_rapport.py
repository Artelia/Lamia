# -*- coding: utf-8 -*-





from Lamia.test.AbstractTest import Test
import os
import datetime
from qgis.PyQt import QtCore


class TestMain(Test):

    def __init__(self):
        super(TestMain, self).__init__()


    def testMethod(self):
        self.createWin()

        # path = os.path.normpath("C://Users//patrice.verchere//Documents//GitHub//Lamia//Lamia//test//02_test_export//BD_totale.sqlite")
        path = "C://000_testdigue//temp_base2_assainissement//test01.sqlite"
        #path = "I://FLUVIAL//4352408_33_CCMA_VTA_Valeyrac//6_Reglementaire//62_Dessins//620_Qgis//total//vvvvv.sqlite"
        path = "M://FR//BOR//VT//FLUVIAL//4352408_33_CCMA_VTA_Valeyrac//6_Reglementaire//61_Calculs//Lamia2//valeyrac_ind0.sqlite"
        #path = "M://FR//BOR//VT//URBAIN//4352329-33-GPMB-diag complet EU et EP-Bacalan, Le Verdon, Pauillac et Blaye//05-ETUDES//05-1-Dessins-plans//6-lamia//gpmb_ind0.sqlite"
        path = "M://FR//BOR//VT//FLUVIAL//4352408_33_CCMA_VTA_Valeyrac//6_Reglementaire//61_Calculs//Lamia2//valeyrac_ind0.sqlite"

        path = "C://000_testdigue//temp_base2_ass2//test01.sqlite"
        #path = "C://000_testdigue//Lamia2//valeyrac_ind0.sqlite"
        path = "M://FR//BOR//VT//FLUVIAL//4352409_33_ASA_Baurech_EDD//6_Reglementaire//61_Calculs//lamia//baurech.sqlite"
        path = "U://FR//BOR//VT//PVR//20_LAMIA//0_Github//Lamia//test//99_scriptqgis//baurech.sqlite"

        path = "M://FR//BOR//VT//FLUVIAL//4352024_33_Conformite_digues_BM//6_Reglementaire//61_Calculs//Basedonnees//BD_totale_ind6.sqlite"
        # path = "M://FR//BOR//VT//FLUVIAL//4352024_33_Conformite_digues_BM//6_Reglementaire//61_Calculs//Basedonneestest//BD_totale_ind6.sqlite"
        path = "C://000_testdigue//0_bastien//LANDY.sqlite"


        self.wind.dbase.loadQgisVectorLayers(path)
        self.wind.loadUiDesktop()

        self.loadLayersInCanvas()

        self.createMainWin()

        if True:       # test of desktop version
            self.wind.loadUiDesktop()
            self.dbase.visualmode = 4

        self.dbase.printsql = False

        if False:
            indexrapport = None
            for i, menutool in enumerate(self.wind.menutools):
                if 'printPDF' in menutool.__class__.__name__ :
                    indexrapport = i
                    break
            self.wind.dbase.dbasetables['Zonegeo']['layerqgis'].selectByIds([22,23,24])
            # Desordres Infralineaire Equipementhydraulique
            # 01regard 01deshuileur  01posterefoulement
            # self.wind.menutools[indexrapport].pdffile = "C://000_testdigue//Lamia2//testrapport.pdf"
            self.wind.menutools[indexrapport].pdffile = "C://testrapport.pdf"
            self.wind.menutools[indexrapport].reporttype = 'Desordres'
            self.wind.menutools[indexrapport].work()


        if True:
            wdg = None
            for i, tool in enumerate(self.wind.tools):
                print(tool.__class__.__name__)
                if 'RapportTool' in tool.__class__.__name__:
                    print('ok')
                    wdg = self.wind.tools[i]
                    break

            wdg.changePropertiesWidget()
            self.wind.MaintreeWidget.setCurrentItem(wdg.qtreewidgetitem)

            if True:
                # 01regard
                indexrapport = wdg.userwdgfield.comboBox_type.findText('01regardSNCF')
                wdg.userwdgfield.comboBox_type.setCurrentIndex(indexrapport)

                wdg.userwdgfield.pushButton_export.clicked.emit(True)

        #self.mainwin.exec_()






test = TestMain()
test.launchTest()

