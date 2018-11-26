# -*- coding: utf-8 -*-





from Lamia.test.AbstractTest import Test
import os
import datetime


class TestMain(Test):

    def __init__(self):
        super(TestMain, self).__init__()


    def testMethod(self):
        self.createWin()

        path = os.path.normpath("C://Users//patrice.verchere//Documents//GitHub//Lamia//Lamia//test//02_test_export//BD_totale.sqlite")
        #path = "I://FLUVIAL//4352408_33_CCMA_VTA_Valeyrac//6_Reglementaire//62_Dessins//620_Qgis//total//vvvvv.sqlite"
        self.wind.dbase.loadQgisVectorLayers(path)
        self.wind.loadUiDesktop()

        #self.loadLayersInCanvas()

        #self.createMainWin()

        self.dbase.printsql = True
        indexrapport = None
        for i, menutool in enumerate(self.wind.menutools):
            if 'printPDF' in menutool.__class__.__name__ :
                indexrapport = i
                break

        self.wind.dbase.dbasetables['Zonegeo']['layerqgis'].selectByIds([1])
        # Desordres Infralineaire Equipementhydraulique
        self.wind.menutools[indexrapport].pdffile = "c://testrapport.pdf"
        self.wind.menutools[indexrapport].reporttype = 'Desordres'
        self.wind.menutools[indexrapport].work()




test = TestMain()
test.launchTest()

