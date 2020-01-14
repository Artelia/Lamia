# -*- coding: utf-8 -*-


from Lamia.test.AbstractTest import Test
import os
import datetime
from qgis.PyQt import  QtCore


class TestMain(Test):

    def __init__(self):
        super(TestMain, self).__init__()


    def testMethod(self):
        self.createWin()
        # self.createMainWin()

        #common
        # path = "C://000_testdigue//temp_base2_digue//test01.sqlite"
        # path = "C://000_testdigue//temp_base2_parking//test01.sqlite"
        # path = "C://000_testdigue//temp_base2_ass2//test01.sqlite"
        # path = "C://000_testdigue//temp_base2_tram2//test01.sqlite"
        # path = "C://000_testdigue//temp_base2_aep//test01.sqlite"
        # path = "C://000_testdigue//temp_base2_eclairagepublic//test01.sqlite"

        # spe
        # path = "M://FR//BOR//VT//FLUVIAL//4352024_33_Conformite_digues_BM//6_Reglementaire//61_Calculs//Basedonnees//BD_totale_ind7.sqlite"
        # path = "M://FR//BOR//VT//URBAIN//4352329-33-GPMB-diag complet EU et EP-Bacalan, Le Verdon, Pauillac et Blaye//05-ETUDES//05-1-Dessins-plans//6-lamia//BASSENS//Travail PLA.sqlite"
        # path = "C://000_testdigue//0_bastien//LANDY.sqlite"
        # path = "C://000_testdigue//testdigue//BD_totale_ind6.sqlite"
        # path = "U://FR//BOR//VT//PVR//20_LAMIA//1_DOC//tramway//sauvegarde_190507//SMTCG_Inspection_Voie.sqlite"
        # path = "C://000_testdigue//Manon_AEP//EAU POTABLE S1.sqlite"

        # path = "M://FR//BOR//VT//URBAIN//4352329-33-GPMB-diag complet EU et EP-Bacalan, Le Verdon, Pauillac et Blaye//05-ETUDES//05-1-Dessins-plans//6-lamia//Verdon Terminal conteneur//GPMB Verdon Terminal conteneur.sqlite"
        # path = "C://000_testdigue//Manon_AEP//EAU POTABLE S1.sqlite"
        # path = "C://000_testdigue//0_caroline//La_Geneytouse3.sqlite"
        # path = "C://000_testdigue//tram_bordeaux//Tram.sqlite

        # choice
        path = "C://000_Modwenne//Lamia//test01.sqlite"
        self.dbase.loadQgisVectorLayers(path)

        self.dbase.printsql = False
        #import tool
        if False:
            from Lamia.Lamia.toolpostpro.Base2.Lamia_import_tool import ImportTool
            self.widget = ImportTool(self.dbase, dialog=self.wind)
        #amctool
        if True:
            from Lamia.toolpostpro.Base2.Lamia_amc_tool import AmcTool
            self.widget = AmcTool(self.dbase, dialog=self.wind)
            self.widget.filemanager.reset()
            self.widget.editAMC()

        self.widget.show()




test = TestMain()
test.launchTest()

