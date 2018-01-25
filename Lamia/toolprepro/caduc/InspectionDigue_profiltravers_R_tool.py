# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtGui
from InspectionDigueV2.src.toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
#from .InspectionDigue_photos_tool import PhotosTool
#from .InspectionDigue_rapport_tool import RapportTool
#from .InspectionDigue_tronconemprise_tool  import TronconEmpriseTool
import os

from ..libs import pyqtgraph as pg
# from .InspectionDigue_photos_tool import PhotosTool
# from .InspectionDigue_rapport_tool import RapportTool
# from .InspectionDigue_tronconemprise_tool  import TronconEmpriseTool
import os

from qgis.PyQt import uic, QtGui

from InspectionDigueV2.src.toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..libs import pyqtgraph as pg

pg.setConfigOption('background', 'w')

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), '..', 'dialog', 'InspectionDigue_propertieswidget.ui'))
FORM_CLASS2, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'ProfilTraversRToolUser.ui'))


class ProfilTraversRTool(AbstractInspectionDigueTool, FORM_CLASS):

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(ProfilTraversRTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil,parentwidget, parent=parent)
        
    def initTool(self):
        self.setupUi(self)
        self.CAT = 'Topographie'
        self.NAME = 'Profil Travers Relatif'
        self.dbasetablename = 'PROFILTRAVERSR'

        self.userwdg = UserUI()

        self.userwdg.pushButton_addline.clicked.connect(self.addrow)
        self.userwdg.pushButton_delline.clicked.connect(self.removerow)

        self.idstoload = {'PROFILTRAVERS' : ['IdProfTr','ID' ]}

        #Tools tab - temporal graph
        self.pyqtgraphwdg = pg.PlotWidget()
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.pyqtgraphwdg)
        self.vb = self.pyqtgraphwdg.getViewBox()
        self.userwdg.frame_graph.setLayout(layout)
        self.plotitem = []


    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass

    def addrow(self):
        introw = self.userwdg.tableWidget.currentRow()
        self.userwdg.tableWidget.insertRow(introw + 1)

        spinboxX = QtGui.QDoubleSpinBox()
        spinboxX.setSingleStep(0.5)
        spinboxX.setRange(0,999)
        spinboxZ = QtGui.QDoubleSpinBox()
        spinboxZ.setSingleStep(0.5)
        spinboxZ.setRange(-999,999)

        self.userwdg.tableWidget.setCellWidget(introw + 1, 0, spinboxX)
        self.userwdg.tableWidget.setCellWidget(introw + 1, 1, spinboxZ)


    def removerow(self):
        introw = self.userwdg.tableWidget.currentRow()
        self.userwdg.tableWidget.removeRow(introw)
        if False and introw != 0 and introw != (self.userwdg.tableWidget.rowCount()):
            self.userwdg.tableWidget.setItem(introw, 1, QtGui.QTableWidgetItem(self.userwdg.tableWidget.item(introw - 1, 2)))


    def postInitFeatureProperties(self, feat):
        for row in range(self.userwdg.tableWidget.rowCount() +1):
            self.userwdg.tableWidget.removeRow(0)

        if len(self.plotitem)>0:
            for plot in self.plotitem:
                self.pyqtgraphwdg.removeItem(plot[0])
        self.plotitem = []

        if self.currentFeature is not None:
            X = self.currentFeature['X'].split(';')
            Z = self.currentFeature['Z'].split(';')
            lenvalues = len(X)
            for row in range(lenvalues):
                self.addrow()
                self.userwdg.tableWidget.cellWidget(row, 0).setValue(float(X[row]))
                self.userwdg.tableWidget.cellWidget(row, 1).setValue(float(Z[row]))
                self.userwdg.tableWidget.setCurrentCell(row, 0)

            self.showGraph()




    def showGraph(self):
        # print('showGraph')

        X = self.currentFeature['X'].split(';')
        Z = self.currentFeature['Z'].split(';')

        Xgraph = [0.0]
        Zgraph = [0.0]

        for i in range(len(X)):
            Xgraph.append(Xgraph[-1] + float(X[i]))
            Zgraph.append(Zgraph[-1] + float(Z[i]))


        self.plotitem.append([self.pyqtgraphwdg.plot(Xgraph, Zgraph, pen=pg.mkPen('b', width=2)), Xgraph, Zgraph])
        self.pyqtgraphwdg.autoRange()


    def createParentFeature(self):
        # idprofiltraversr = self.currentFeature.id()
        idprofiltraversr = self.currentFeature.id()
        idprofiltravers = self.parentWidget.currentFeature.id()
        sql = "UPDATE PROFILTRAVERSR SET IdProfTr = " + str(idprofiltravers) + " WHERE id = " + str(idprofiltraversr) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()

    def postSaveFeature(self, boolnewfeature):
        idprofiltraversr = self.currentFeature.id()
        if False:
            if boolnewfeature:
                #idprofiltraversr = self.currentFeature.id()
                idprofiltravers = self.parentWidget.currentFeature.id()
                sql = "UPDATE PROFILTRAVERSR SET IdProfTr = " + str(idprofiltravers) + " WHERE id = " + str(idprofiltraversr) + ";"
                query = self.dbase.query(sql)
                self.dbase.commit()

        X = []
        Z = []
        for row in range(self.userwdg.tableWidget.rowCount() ):
            X.append(str(self.userwdg.tableWidget.cellWidget(row,0).value()))
            Z.append(str(self.userwdg.tableWidget.cellWidget(row,1).value()))

        X = ';'.join(X)
        Z = ';'.join(Z)

        sql = "UPDATE PROFILTRAVERSR SET X = '" + X + "' WHERE id = " + str(idprofiltraversr) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()

        sql = "UPDATE PROFILTRAVERSR SET Z = '" + Z + "' WHERE id = " + str(idprofiltraversr) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()


class UserUI(QtGui.QWidget, FORM_CLASS2):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        self.setupUi(self)
