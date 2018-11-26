# -*- coding: utf-8 -*-


from Lamia.test.AbstractTest import Test
import os
import datetime


class TestMain(Test):

    def __init__(self):
        super(TestMain, self).__init__()


    def testMethod(self):
        self.createWin()

        path = os.path.normpath("C://Users//patrice.verchere//Documents//GitHub//Lamia//test//02_test_export//BD_totale1.sqlite")
        path = os.path.normpath("C://000_testdigue//temp_base2_parking//test01.sqlite")

        self.dbase.loadQgisVectorLayers(path)
        print('ok0')

        self.loadLayersInCanvas()

        print('ok')

        self.createMainWin()

        # eventualy add new version
        if False:
            datesuppr = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            sql = "INSERT INTO Revision(datetimerevision, commentaire) VALUES('" + datesuppr + "','test')"
            self.dbase.query(sql)




        # self.dbase.printsql = True
        print('launch window')
        self.mainwin.exec_()


test = TestMain()
test.launchTest()

