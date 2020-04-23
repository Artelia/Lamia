# -*- coding: utf-8 -*-





from Lamia.test.AbstractTest import Test
import os
import datetime
import qgis.core
from qgis.PyQt import  QtCore
from Lamia.Lamia.toolgeneral.SIRS_to_LAMIA.FDtL import *
from Lamia.Lamia.toolgeneral.LAMIA_to_SIRS.LtFD import *



class TestMain(Test):

    def __init__(self):
        super(TestMain, self).__init__()


    def testMethod(self):
        self.createWin()



        path = "C://000_testdigue//testdigue//BD_totale_ind6.sqlite"

        self.dbase.xlsreader = True
        self.dbase.loadQgisVectorLayers(path)

        query = "SELECT * FROM Infra"


        #script = "/myvlayer.sqlite"

        script = "?layer=spatialite:"
        script += str(QtCore.QUrl.toPercentEncoding("dbname='" + path + "' key ='pk_infralineaire' " + 'table="Infralineaire_qgis" (geom) sql='))
        script += ":Infra:UTF8"
        script += "&query=" + str(QtCore.QUrl.toPercentEncoding(query))

        if False:
            script = "/myvlayer.sqlite?layer=spatialite:dbname='" + path + "' key ='pk_infralineaire' " + 'table="Infralineaire_qgis" (geom) '
            script += "sql="
            script += ":Infra:UTF8"
            script += "&query=" + str(QtCore.QUrl.toPercentEncoding(query)) + query



        print(script)

        vlayer = qgis.core.QgsVectorLayer(str(script), "vlayer", "virtual")
        print('vlayer', vlayer.isValid())

        for fet in vlayer.getFeatures():
            print(fet.attributes())

        print('ok')


test = TestMain()
test.launchTest()

"""
?layer=spatialite:dbname%3D%27C%3A%2F%2F000_testdigue%2F%2Ftestdigue%2F%2FBD_totale_ind6.sqlite%27%20key%3D%27pk_infralineaire%27%20table%3D%22Infralineaire_qgis%22%20%28geom%29%20sql%3D:test:UTF-8&query=Select%20*%20FROM%20test

"""