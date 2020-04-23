# -*- coding: utf-8 -*-

from Lamia.test.AbstractTest import Test
import os
import datetime
import sys
import qgis

class TestMain(Test):

    def __init__(self):
        super(TestMain, self).__init__()


    def testMethod(self):
        self.createWin()

        path = "C://000_testdigue//0_bastien//LANDY.sqlite"

        self.dbase.xlsreader = True
        self.dbase.printsql = False

        self.dbase.loadQgisVectorLayers(path)
        self.loadLayersInCanvas()
        self.createMainWin()

        if True:       # test of desktop version
            self.wind.loadUiDesktop()
            self.dbase.visualmode = 4

        wdg = None
        for i, tool in enumerate(self.wind.tools):
            print(tool.__class__.__name__)
            if 'AmcTool' in tool.__class__.__name__:
                print('ok')
                wdg = self.wind.tools[i]
                break

        #wdg = self.dbase.dbasetables['Infralineaire']['widget'][0]
        wdg.changePropertiesWidget()

        self.wind.MaintreeWidget.setCurrentItem(wdg.qtreewidgetitem)

        wdg.userwdgfield.toolButton_editamc.clicked.emit(True)




        self.mainwin.exec_()



test = TestMain()
test.launchTest()

