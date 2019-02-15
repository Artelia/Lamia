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

        path = os.path.normpath("C://000_testdigue//BM//BD_totale3.sqlite")
        #path = os.path.normpath("C://000_testdigue//temp_base2_parking//test01.sqlite")
        #path = os.path.normpath("C://000_testdigue//valeyrac//vvvvv.sqlite")
        #path = os.path.normpath("M://FR//BOR//VT//FLUVIAL//4352024_33_Conformite_digues_BM//6_Reglementaire//61_Calculs//Basedonnees_terrains//20181128_SIJALAG//sijalag.sqlite")
        #path = "C://000_testdigue//temp_base2_assainissement//test01.sqlite"
        path = "M://FR//BOR//VT//FLUVIAL//4352408_33_CCMA_VTA_Valeyrac//6_Reglementaire//61_Calculs//Lamia2//valeyrac_ind0.sqlite"
        #path = "M://FR//BOR//VT//URBAIN//4352329-33-GPMB-diag complet EU et EP-Bacalan, Le Verdon, Pauillac et Blaye//05-ETUDES//05-1-Dessins-plans//6-lamia//gpmb_ind1.sqlite"
        path = "C://00_Affaires//GPMB//lamia//gpmb_ind1.sqlite"

        #path = "C://000_testdigue//temp_base2_ass2//test01.sqlite"
        path = "C://000_testdigue//temp_base2_ass2//Mirepoix_Test01.sqlite"
        #path = "M://FR//BOR//VT//FLUVIAL//4352409_33_ASA_Baurech_EDD//6_Reglementaire//61_Calculs//lamia//baurech.sqlite"

        path = "M://FR//BOR//VT//FLUVIAL//4352024_33_Conformite_digues_BM//6_Reglementaire//61_Calculs//Basedonnees_terrains//20181212_Jalle_Blanquefort//BD_totale_ind4.sqlite"
        path = "M://FR//BOR//VT//FLUVIAL//4352024_33_Conformite_digues_BM//6_Reglementaire//61_Calculs//Basedonnees//BD_totale_ind6.sqlite"


        # path = 'C://000_testdigue//temp_base2_parking//test01.sqlite'
        # path = "C://000_testdigue//BM//BD_totale_ind6_backup2.sqlite"
        # path = "M://FR//BOR//VT//FLUVIAL//4352408_33_CCMA_VTA_Valeyrac//6_Reglementaire//61_Calculs//Lamia2//valeyrac_ind0.sqlite"
        path = "C://000_testdigue//Lamia2//valeyrac_ind0.sqlite"
        path = "C://000_testdigue//temp_base2_tram2//test01.sqlite"
        # path = "C://000_testdigue//temp_base2_ass2//test01.sqlite"

        self.dbase.loadQgisVectorLayers(path)
        print('ok0')

        self.loadLayersInCanvas()

        print('ok')

        self.createMainWin()
        self.mainwin.resize(QtCore.QSize(1000,800))

        # eventualy add new version
        if False:
            datesuppr = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            sql = "INSERT INTO Revision(datetimerevision, commentaire) VALUES('" + datesuppr + "','test')"
            self.dbase.query(sql)




        self.dbase.printsql = False
        print('launch window')
        self.mainwin.exec_()


test = TestMain()
test.launchTest()

