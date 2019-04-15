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

        #path = os.path.normpath("C://Users//patrice.verchere//Documents//GitHub//Lamia//test//02_test_export//BD_totale1.sqlite")
        # path = os.path.normpath("C://Users//patrice.verchere//Documents//GitHub//Lamia//test//02_test_importdb//test01//01_original//test01.sqlite")
        #path = "I://FLUVIAL//4352408_33_CCMA_VTA_Valeyrac//6_Reglementaire//62_Dessins//620_Qgis//total//vvvvv.sqlite"
        path = os.path.normpath("C://000_testdigue//temp_base2_parking//test01.sqlite")
        path =  "M://FR//BOR//VT//FLUVIAL//4352409_33_ASA_Baurech_EDD//6_Reglementaire//61_Calculs//lamia//baurech.sqlite"
        #path =  "C://000_testdigue//testdigue//BD_totale_ind6.sqlite"
        path = "M://FR//BOR//VT//FLUVIAL//4352024_33_Conformite_digues_BM//6_Reglementaire//61_Calculs//Basedonnees//BD_totale_ind6.sqlite"

        self.dbase.loadQgisVectorLayers(path)
        print('ok0')

        self.loadLayersInCanvas()

        print('ok')

        self.createMainWin()



        if True:       # test of desktop version
            self.wind.loadUiDesktop()
            self.dbase.visualmode = 4



        # self.dbase.printsql = True
        timestart = self.dbase.getTimeNow()

        if True:

            wdg = None
            for i, tool in enumerate(self.wind.tools):
                print(tool.__class__.__name__)
                if 'CostTool' in tool.__class__.__name__:
                    print('ok')
                    wdg = self.wind.tools[i]
                    break

            #wdg = self.dbase.dbasetables['Infralineaire']['widget'][0]
            wdg.changePropertiesWidget()

            self.wind.MaintreeWidget.setCurrentItem(wdg.qtreewidgetitem)


            if False:
                self.wind.dbase.dbasetables['Zonegeo']['layerqgis'].selectByIds([14])

                #print(self.wind.dbase.currentrevision)

                wdg.userwdgfield.toolButton_calcul.clicked.emit(True)


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

                        #wdg.userwdgfield.lineEdit_option.setText('date=31/12/2017,now')
                        #wdg.userwdgfield.lineEdit_option.returnPressed.emit()

                        wdgitem2 = wdg.userwdgfield.treeWidget_desordres_2.invisibleRootItem().child(1)
                        wdg.userwdgfield.treeWidget_desordres_2.setCurrentItem(wdgitem2)


        print('time', self.dbase.getTimeNow() - timestart)

        self.mainwin.exec_()



test = TestMain()
test.launchTest()

