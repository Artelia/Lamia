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
        # BM_Infralineaire Noeud
        # BM_Photo   BM_TcObjetRessource  BM_Equipement_ligne   BM_Desordres_ligne  BM_Graphdata   BM_Observation
        # 00_Desordres_observation_actif   00_Desordres_observation_total
        # Export_total
        typeexport = 'Noeud'

        if False:
            rootpath = "M://FR//BOR//VT//FLUVIAL//4352024_33_Conformite_digues_BM//6_Reglementaire//63_Rapports//20190200_BD_exportshp"
            exportfile = os.path.join(rootpath, typeexport + ".shp")
        if True:
            rootpath = "C://000_testdigue//temp"
            exportfile = os.path.join(rootpath, typeexport + ".shp")

        #exportfile = os.path.normpath("C://testshape.shp")
        # self.wind.dbase.dbasetables['Zonegeo']['layerqgis'].selectByIds([5])
        self.wind.menutools[indexrapport].prepareData(typeexport, exportfile)



test = TestMain()
test.launchTest()
sys.exit()

