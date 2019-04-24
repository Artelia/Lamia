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

        #common
        # path = "C://000_testdigue//temp_base2_digue//test01.sqlite"
        # path = "C://000_testdigue//temp_base2_parking//test01.sqlite"
        # path = "C://000_testdigue//temp_base2_ass2//test01.sqlite"
        # path = "C://000_testdigue//temp_base2_tram2//test01.sqlite"
        # path = "C://000_testdigue//temp_base2_aep//test01.sqlite"

        # spe
        # path = "M://FR//BOR//VT//FLUVIAL//4352024_33_Conformite_digues_BM//6_Reglementaire//61_Calculs//Basedonnees//BD_totale_ind6.sqlite"
        # path = "C://000_testdigue//0_bastien//LANDY.sqlite"
        # path = "C://000_testdigue//testdigue//BD_totale_ind6.sqlite"

        # choice
        path = "C://000_testdigue//0_bastien//LANDY.sqlite"

        self.dbase.xlsreader = True
        self.dbase.loadQgisVectorLayers(path)
        print('ok0')

        self.loadLayersInCanvas()

        # print(self.dbase.dbasetables['Infralineaire']['fields'])

        print('ok')

        self.createMainWin()
        self.mainwin.resize(QtCore.QSize(1000,800))

        if False:       # test of desktop version
            self.wind.loadUiDesktop()
            self.dbase.visualmode = 4
            self.wind.applyVisualMode()

        # eventualy add new version
        if False:
            datesuppr = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            sql = "INSERT INTO Revision(datetimerevision, commentaire) VALUES('" + datesuppr + "','test')"
            self.dbase.query(sql)

        try:
            user_paths = os.environ['PYTHONPATH'].split(os.pathsep)
        except KeyError:
            user_paths = []

        #print('PYTHONPATH', user_paths)
        #print( self.dbase.variantespossibles )

        self.dbase.printsql = False
        print('launch window')
        self.mainwin.exec_()


test = TestMain()
test.launchTest()

