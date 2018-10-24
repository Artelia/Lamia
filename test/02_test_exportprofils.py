# -*- coding: utf-8 -*-

from Lamia.test.AbstractTest import Test
import os
import datetime
import sys

class TestMain(Test):

    def __init__(self):
        super(TestMain, self).__init__()

    def testMethod(self):
        self.createWin()

        path = os.path.normpath("C://Users//patrice.verchere//Documents//GitHub//Lamia//Lamia//test//02_test_export//BD_totale.sqlite")
        self.wind.dbase.loadQgisVectorLayers(path)
        self.wind.loadUiDesktop()

        exportdir = "C://000_testdigue//testexportprofil"

        sql= " SELECT id_infralineaire, lid_ressource_4 FROM Infralineaire_qgis WHERE lid_ressource_4 IS NOT NULL"
        results = self.dbase.query(sql)

        counter = 0
        for res in results:
            counter += 1
            if counter > 10:
                break

            id_infralineaire, id_ressource = res
            sql = "SELECT typegraphique, id_graphique FROM Graphique_qgis  WHERE id_ressource = " + str(id_ressource)
            query = self.dbase.query(sql)
            resulttemp = [row for row in query]
            if len(resulttemp) > 0:
                typegraphique, id_graphique = resulttemp[0]
                datas = self.dbase.dbasetables['Graphique']['widget'][0].getGraphData(id_graphique)
                exportfile = os.path.join(exportdir, 'profil_' + str(id_infralineaire)+'.png' )
                self.dbase.dbasetables['Graphique']['widget'][0].exportgraph(typegraphique,
                                                                             datas,
                                                                             exportfile,
                                                                             200,
                                                                             200)



test = TestMain()
test.launchTest()