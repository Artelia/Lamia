# -*- coding: utf-8 -*-


from Lamia.test.AbstractTest import Test
import os
import datetime
from qgis.PyQt import  QtCore

class TestMain(Test):

    def __init__(self):
        super(TestMain, self).__init__()


    def testMethod(self):
        self.createWin()
        path = "M://FR//BOR//VT//FLUVIAL//4352024_33_Conformite_digues_BM//6_Reglementaire//61_Calculs//Basedonnees//BD_totale_ind6.sqlite"
        self.dbase.loadQgisVectorLayers(path)
        #print('ok0')
        #self.loadLayersInCanvas()
        #print('ok')
        #self.createMainWin()
        #self.mainwin.resize(QtCore.QSize(1000,800))

        self.dbase.printsql = False
        self.scriptBM()
        #self.mainwin.exec_()
        
    def scriptBM(self):
        sql = "SELECT lpk_graphique FROM Graphiquedata GROUP BY lpk_graphique"
        res = self.dbase.query(sql)
        for lpk_graphique in res:
            print(lpk_graphique)
            sqltemp = "SELECT pk_graphiquedata, index1 FROM Graphiquedata WHERE lpk_graphique = " + str(lpk_graphique[0])
            sqltemp += " ORDER BY pk_graphiquedata"
            restemp = self.dbase.query(sqltemp)
            cretedepasse = False
            for pk_graphiquedata, index1 in restemp:
                print(pk_graphiquedata, index1)
                if index1 != 'CRE' and not cretedepasse:
                    sqltempp = "UPDATE Graphiquedata SET index4 = 'TER' WHERE pk_graphiquedata = " + str(pk_graphiquedata)
                    self.dbase.query(sqltempp)
                elif index1 == 'CRE':
                    cretedepasse = True
                    sqltempp = "UPDATE Graphiquedata SET index4 = 'CRE' WHERE pk_graphiquedata = " + str(pk_graphiquedata)
                    self.dbase.query(sqltempp)
                elif index1 != 'CRE' and cretedepasse:
                    sqltempp = "UPDATE Graphiquedata SET index4 = 'RIV' WHERE pk_graphiquedata = " + str(pk_graphiquedata)
                    self.dbase.query(sqltempp)



test = TestMain()
test.launchTest()

