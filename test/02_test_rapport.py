# -*- coding: utf-8 -*-





from Lamia.test.AbstractTest import Test
import os
import datetime


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

        self.wind.dbase.loadQgisVectorLayers(path)
        self.wind.loadUiDesktop()

        #self.loadLayersInCanvas()

        #self.createMainWin()

        #self.dbase.printsql = True
        indexrapport = None
        for i, menutool in enumerate(self.wind.menutools):
            if 'printPDF' in menutool.__class__.__name__ :
                indexrapport = i
                break

        #self.wind.dbase.dbasetables['Zonegeo']['layerqgis'].selectByIds([1])
        # Desordres Infralineaire Equipementhydraulique
        # 01regard 01deshuileur  01posterefoulement
        self.wind.menutools[indexrapport].pdffile = "C://000_testdigue//Lamia2//testrapport.pdf"
        self.wind.menutools[indexrapport].reporttype = '01regard'
        self.wind.menutools[indexrapport].work()




test = TestMain()
test.launchTest()

