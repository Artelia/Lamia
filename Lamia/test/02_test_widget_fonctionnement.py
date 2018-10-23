# -*- coding: utf-8 -*-

from Lamia.Lamia.test.AbstractTest import Test
import os
import datetime
import sys
import qgis

class TestMain(Test):

    def __init__(self):
        super(TestMain, self).__init__()


    def testMethod(self):
        self.createWin()

        print('DBase creation start')

        crs = 3945
        # Digue VNF  Assainissement  Default Assainissement2 Base Base_default Base_assainissement Base2_digue
        typebase = 'Base2_digue'
        # spatialite   postgis
        typedb = 'spatialite'
        spatialitefile = 'C://000_testdigue//temp_base2_digue//test01.sqlite'

        self.dbase.printsql = False
        self.dbase.createDbase(slfile=spatialitefile, crs=crs, worktype=typebase)



        if False:       # test of desktop version
            self.wind.loadUiDesktop()
            self.dbase.visualmode = 1


        self.dbase.printsql = True
        #test infralineaire widget
        if True:
            wdg = self.dbase.dbasetables['Infralineaire']['widget'][0]
            wdg.changePropertiesWidget()
            self.wind.MaintreeWidget.setCurrentItem(wdg.qtreewidgetitem)

            wdg.addFeature()
            wdg.setTempGeometry([qgis.core.QgsPoint(0,0),qgis.core.QgsPoint(1,1)])
            wdg.saveFeature()

        # test Equipement widget
        if True:
            wdg = self.dbase.dbasetables['Equipement']['widget'][0]
            wdg.changePropertiesWidget()
            self.wind.MaintreeWidget.setCurrentItem(wdg.qtreewidgetitem)

            wdg.addFeature()
            wdg.setTempGeometry([qgis.core.QgsPoint(-1,-1),qgis.core.QgsPoint(-1,-1)])
            indexequiptype = wdg.userwdgfield.comboBox_cat.findText('Ponctuel - Hydraulique')
            wdg.userwdgfield.comboBox_cat.setCurrentIndex(indexequiptype)
            wdg.saveFeature()

            wdg.propertieswdgDesordre.propertieswdgOBSERVATION2.addFeature()
            wdg.propertieswdgDesordre.propertieswdgOBSERVATION2.saveFeature()




        self.loadLayersInCanvas()

        self.createMainWin()

        self.mainwin.exec_()



test = TestMain()
test.launchTest()

