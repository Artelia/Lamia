# -*- coding: utf-8 -*-

from test.AbstractTest import Test
import os
import datetime
import sys
import qgis

class TestMain(Test):

    def __init__(self):
        super(TestMain, self).__init__()


    def testMethod(self):
        self.createWin()

        path = os.path.join(os.path.dirname(__file__), '99_stat_testfile','BD_totale_ind11.sqlite')

        self.dbase.loadQgisVectorLayers(path)
        print('ok0')

        self.loadLayersInCanvas()

        print('ok')

        self.createMainWin()



        if True:       # test of desktop version
            self.wind.loadUiDesktop()
            self.dbase.visualmode = 4


        if True:
            wdg = None
            for i, tool in enumerate(self.wind.tools):
                print(tool.__class__.__name__)
                if 'StatTool' in tool.__class__.__name__:
                    print('ok')
                    wdg = self.wind.tools[i]
                    break

            wdg.changePropertiesWidget()

            self.wind.MaintreeWidget.setCurrentItem(wdg.qtreewidgetitem)




        self.mainwin.exec_()



test = TestMain()
test.launchTest()

