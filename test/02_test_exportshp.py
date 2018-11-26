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
        self.wind.dbase.loadQgisVectorLayers(path)
        self.wind.loadUiDesktop()

        #self.loadLayersInCanvas()

        #self.createMainWin()

        self.dbase.printsql = False
        indexrapport = None
        for i, menutool in enumerate(self.wind.menutools):
            if 'exportShapefile' in menutool.__class__.__name__ :
                indexrapport = i
                break
        # Infralineaire_BM Equipement_point_BM Photo_BM Graphdata_BM Desordres_ligne_BM
        shp = os.path.normpath("C://Users//patrice.verchere//Documents//GitHub//Lamia//Lamia//test//02_test_export//testshape.shp")
        shp = os.path.normpath("C://testshape.shp")
        # self.wind.dbase.dbasetables['Zonegeo']['layerqgis'].selectByIds([5])
        self.wind.menutools[indexrapport].prepareData('Desordres_ligne_BM', shp)



test = TestMain()
test.launchTest()
sys.exit()

