# -*- coding: utf-8 -*-
import qgis
from qgis.PyQt import uic, QtGui, QtCore
try:
    from qgis.PyQt.QtGui import (QWidget, QLabel, QFrame, QTreeWidgetItem, QHeaderView, QComboBox, QAbstractItemView)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget, QLabel, QFrame, QTreeWidgetItem, QHeaderView, QComboBox, QAbstractItemView)

#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
# from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
#from ...toolabstract.Lamia_abstract_tool import AbstractLamiaTool
from ...toolabstract.Lamia_abstract_tool import AbstractLamiaTool
import os
import io
import sys
if False:
    if sys.version_info.major == 2:
        from ...libs import pyqtgraph as pg
        from ...libs.pyqtgraph import exporters
    elif sys.version_info.major == 3:
        from ...libs import pyqtgraph as pg
        pg.setConfigOption('background', 'w')

if sys.version_info.major == 2:
    from matplotlib.backends.backend_qt4agg import (FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
elif sys.version_info.major == 3:
    from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import networkx
import numpy as np
import shutil
import logging


# ********************************************************************************************************************
# ********************************* Main Widget                *******************************************************
# ********************************************************************************************************************

class CostTool(AbstractLamiaTool):

    DBASES = ['digue','base_digue']

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(CostTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil,parentwidget, parent=parent)

        
    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Synthese'
        self.NAME = 'Couts'
        self.visualmode = [4]
        # self.PointENABLED = True
        # self.LineENABLED = True
        # self.PolygonEnabled = True
        # self.magicfunctionENABLED = True
        # self.linkagespec = None
        # self.pickTable = None
        # print(self.dbase.recentsdbase)

        self.iconpath = os.path.join(os.path.dirname(__file__), 'lamiabase_croquis_tool_icon.png')

        # ****************************************************************************************
        # properties ui
        self.groupBox_geom.setParent(None)
        self.groupBox_elements.setParent(None)


        if False:
            if self.dbase.dbasetype == 'spatialite':
                fielpathname = 'path_' + os.path.basename(self.dbase.spatialitefile).split('.')[0]
            elif self.dbase.dbasetype == 'postgis':
                fielpathname = 'path_' + str(self.dbase.pghost)+ '_' + str(self.dbase.pgdb) + '_' + str(self.dbase.pgschema)
            self.dbasetablename = os.path.join(os.path.dirname(__file__), '..', 'config', fielpathname + '.txt')
            #networkx var
            self.nxgraph = None
            self.ids = None
            self.indexnoeuds = None
            self.infralinfaces = None
            self.reverseinfralinfaces = None
            self.indexnoeuds = None
            # rubberband var
            self.rubberBand = qgis.gui.QgsRubberBand(self.canvas,self.dbase.dbasetables['Infralineaire']['layer'].geometryType())
            self.rubberBand.setWidth(5)
            self.rubberBand.setColor(QtGui.QColor("magenta"))

            self.rubberbandtrack = qgis.gui.QgsVertexMarker(self.canvas)
            self.rubberbandtrack.setColor(QtGui.QColor(QtCore.Qt.red))
            self.rubberbandtrack.setIconSize(5)
            self.rubberbandtrack.setIconType(qgis.gui.QgsVertexMarker.ICON_BOX) # or ICON_CROSS, ICON_X
            self.rubberbandtrack.setPenWidth(3)
            # matplotlib var
            self.figuretype = plt.figure()
            self.axtype = self.figuretype.add_subplot(111)

            self.postOnActivation()



            # ****************************************************************************************
            # properties ui
            self.groupBox_geom.setParent(None)
            # self.groupBox_elements.setParent(None)

    def initFieldUI(self):

        # ****************************************************************************************
        # userui Desktop
        if self.userwdgfield is None:

            # ****************************************************************************************
            # userui

            self.userwdgfield = UserUI()

            if True:
                self.combowdg = QComboBox()

            if False:
                self.linkuserwdgfield = [self.userwdgfield.lineEdit_nom,
                                    self.userwdgfield.lineEdit_start,
                                    self.userwdgfield.lineEdit_end]

                self.linkuserwdgfield = {self.dbasetablename: [self.userwdgfield.lineEdit_nom,
                                                            self.userwdgfield.lineEdit_start,
                                                            self.userwdgfield.lineEdit_end]}

                self.userwdgfield.pushButton_pickstart.clicked.connect(self.getPickResult)
                self.userwdgfield.pushButton_pickend.clicked.connect(self.getPickResult)

                # plot
                if False:
                    self.plotWdg = pg.PlotWidget()
                    datavline = pg.InfiniteLine(0, angle=90, pen=pg.mkPen('r', width=1), name='cross_vertical')
                    datahline = pg.InfiniteLine(0, angle=0, pen=pg.mkPen('r', width=1), name='cross_horizontal')
                    self.plotWdg.addItem(datavline)
                    self.plotWdg.addItem(datahline)
                    self.userwdgfield.frame_chart.layout().addWidget(self.plotWdg)
                    self.userwdgfield.checkBox_track.stateChanged.connect(self.activateMouseTracking)
                    self.doTracking = True
                    self.showcursor = True

                    self.userwdgfield.comboBox_chart_theme.addItems(['Profil'])
                    self.userwdgfield.comboBox_chart_theme.currentIndexChanged.connect(self.computeGraph)
                if True:
                    self.figuretype = plt.figure()
                    self.axtype = self.figuretype.add_subplot(111)
                    self.mplfigure = FigureCanvas(self.figuretype)
                    self.userwdgfield.frame_chart.layout().addWidget(self.mplfigure)
                    self.toolbar = NavigationToolbar(self.mplfigure, self.userwdgfield.frame_chart)
                    self.userwdgfield.frame_chart.layout().addWidget(self.toolbar)

                    self.userwdgfield.comboBox_chart_theme.currentIndexChanged.connect(self.computeGraph)



    def postOnActivation(self):

        if True:
            self.disconnectIdsGui()
            self._clearLinkedTreeWidget()
            #self.userwdgfield.treeWidget_desordres.clear()

            # self.combowdg = QComboBox()
            self.combowdg.addItems(['Zone geographique','Troncon'])
            self.windowdialog.frame_4.layout().insertWidget(0,self.combowdg )
            self.combowdg.currentIndexChanged.connect(self.comboWidgetTypeChanged)
            self.combowdg.currentIndexChanged.emit(0)

            self.linkedtreewidget.setSelectionMode(QAbstractItemView.ExtendedSelection)

            self.linkedtreewidget.itemSelectionChanged.connect(self.itemChanged)



            self.connectIdsGui()

        if True:
            self.bordereau = self.readBordereau()


    def readBordereau(self):
        pathbpu = os.path.join(os.path.dirname(__file__), 'costtool', 'bordereau.csv')

        file = open(pathbpu, "r")
        lines = file.readlines()
        file.close()
        for line in lines:
            print(line)


    def postOnDesactivation(self):

        self.combowdg.setParent(None)

        self.linkedtreewidget.setSelectionMode(QAbstractItemView.SingleSelection)
        if False:
            try:
                self.userwdg.treeWidget_desordres.currentItemChanged.disconnect(self.showDesordres)
            except:
                pass

        try:
            self.linkedtreewidget.itemSelectionChanged.disconnect(self.itemChanged)
        except:
            pass



    def comboWidgetTypeChanged(self, index ):
        if False:
            self.loadFeaturesinTreeWdg()
            self.disconnectIdsGui()
        if True:
            self.disconnectIdsGui()
            self._clearLinkedTreeWidget()


            headerlist = list(self.qtreewidgetfields)
            headerlist.insert(0, 'ID')
            self.linkedtreewidget.setColumnCount(len(headerlist))
            self.linkedtreewidget.header().setVisible(True)
            self.linkedtreewidget.setHeaderItem(QTreeWidgetItem(headerlist))
            header = self.linkedtreewidget.header()
            lenheaderlist = len(headerlist)
            if sys.version_info.major == 2:
                for i in range(lenheaderlist):
                    header.setResizeMode(i, QHeaderView.ResizeToContents)
                header.setResizeMode(lenheaderlist-1, QHeaderView.Stretch)
            elif  sys.version_info.major == 3:
                for i in range(lenheaderlist):
                    header.setSectionResizeMode(i, QHeaderView.ResizeToContents)
                header.setSectionResizeMode(lenheaderlist-1, QHeaderView.Stretch)


            parentitem = self.linkedtreewidget.invisibleRootItem()

            if self.combowdg.currentText() == 'Troncon':
                sql = "SELECT id_infralineaire "
                if len(self.qtreewidgetfields) > 0:
                    sql += "," + ','.join(self.qtreewidgetfields)
                sql += " FROM Infralineaire_now"

            elif self.combowdg.currentText() == 'Zone geographique':
                sql = "SELECT id_zonegeo "
                if len(self.qtreewidgetfields) > 0:
                    sql += "," + ','.join(self.qtreewidgetfields)
                sql += " FROM zonegeo_qgis WHERE lpk_revision_end IS NULL"

            sql = self.dbase.updateQueryTableNow(sql)
            query = self.dbase.query(sql)
            ids = [list(row) for row in query]

            lenqtreewidg = len(self.qtreewidgetfields) + 1
            self.treefeatlist = [[id[0], QTreeWidgetItem([str(id[i]) for i in range(lenqtreewidg)])] for id in ids]
            parentitem.addChildren([elem[1] for elem in self.treefeatlist])



            # self.propertieswdgDESORDRE.reloadgraphtype()


            self.connectIdsGui()


    def postInitFeatureProperties(self, feat):
        pass


    def itemChanged(self,item1=None, item2=None):
        print('itemChanged',item1, item2 )






class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        # self.setupUi(self)
        uipath = os.path.join(os.path.dirname(__file__), 'Lamia_cost_tool.ui')
        uic.loadUi(uipath, self)

