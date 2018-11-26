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

        path = os.path.normpath("C://Users//patrice.verchere//Documents//GitHub//Lamia//test//02_test_export//BD_totale1.sqlite")
        # path = os.path.normpath("C://Users//patrice.verchere//Documents//GitHub//Lamia//test//02_test_importdb//test01//01_original//test01.sqlite")
        #path = "I://FLUVIAL//4352408_33_CCMA_VTA_Valeyrac//6_Reglementaire//62_Dessins//620_Qgis//total//vvvvv.sqlite"
        self.dbase.loadQgisVectorLayers(path)
        print('ok0')

        self.loadLayersInCanvas()

        print('ok')

        self.createMainWin()



        if True:       # test of desktop version
            self.wind.loadUiDesktop()
            self.dbase.visualmode = 4


        # self.dbase.printsql = True
        #test infralineaire widget
        if False:
            wdg = self.dbase.dbasetables['Infralineaire']['widget'][0]
            wdg.changePropertiesWidget()
            self.wind.MaintreeWidget.setCurrentItem(wdg.qtreewidgetitem)

            wdg.addFeature()
            wdg.setTempGeometry([qgis.core.QgsPoint(0,0),qgis.core.QgsPoint(1,1)])
            wdg.saveFeature()

        # test Equipement widget
        if False:
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

        if True:

            wdg = None
            for i, tool in enumerate(self.wind.tools):
                if 'SyntheseZonegeoTool' in tool.__class__.__name__:
                    wdg = self.wind.tools[i]

            #wdg = self.dbase.dbasetables['Infralineaire']['widget'][0]
            wdg.changePropertiesWidget()
            self.wind.MaintreeWidget.setCurrentItem(wdg.qtreewidgetitem)
            if True:
                #wdg.userwdgfield.treeWidget_desordres.
                if False:
                    print(wdg.linkedtreewidget.invisibleRootItem().childCount())
                    for i in range(wdg.linkedtreewidget.invisibleRootItem().childCount()):
                        item = wdg.linkedtreewidget.invisibleRootItem().child(i)
                        #item.setExpanded(True)
                        print(item.text(0))

                wdgitem = wdg.linkedtreewidget.invisibleRootItem().child(0)
                #print(wdgitem.text(0))
                wdg.linkedtreewidget.setCurrentItem(wdgitem)

                wdg.userwdgfield.lineEdit_option.setText('date=31/12/2017,now')
                #wdg.userwdgfield.lineEdit_option.returnPressed.emit()

                wdgitem2 = wdg.userwdgfield.treeWidget_desordres_2.invisibleRootItem().child(0)
                wdg.userwdgfield.treeWidget_desordres_2.setCurrentItem(wdgitem2)






        self.mainwin.exec_()



test = TestMain()
test.launchTest()

