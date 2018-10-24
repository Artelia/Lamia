# -*- coding: utf-8 -*-


from Lamia.test.AbstractTest import Test
import os
import datetime


class TestMain(Test):

    def __init__(self):
        super(TestMain, self).__init__()


    def testMethod(self):
        self.createWin()

        path = os.path.normpath("C://Users//patrice.verchere//Documents//GitHub//Lamia//test//02_test_export//BD_totale.sqlite")
        self.dbase.loadQgisVectorLayers(path)

        self.loadLayersInCanvas()

        self.createMainWin()

        # eventualy add new version
        if False:
            datesuppr = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            sql = "INSERT INTO Revision(datetimerevision, commentaire) VALUES('" + datesuppr + "','test')"
            self.dbase.query(sql)


        self.mainwin.exec_()


test = TestMain()
test.launchTest()

