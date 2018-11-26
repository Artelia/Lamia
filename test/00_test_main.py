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
        # path = os.path.normpath("C://Users//patrice.verchere//Documents//GitHub//Lamia//test//02_test_importdb//test01//01_original//test01.sqlite")
        #path = "I://FLUVIAL//4352408_33_CCMA_VTA_Valeyrac//6_Reglementaire//62_Dessins//620_Qgis//total//vvvvv.sqlite"
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
        print('ok1')
        print(self.dbase.canvas.mapSettings().destinationCrs().authid())
        print(self.dbase.qgiscrs.authid())
        self.mainwin.exec_()


test = TestMain()
test.launchTest()

