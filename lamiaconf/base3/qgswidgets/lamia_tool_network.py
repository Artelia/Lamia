# -*- coding: utf-8 -*-

"""
This file is part of LAMIA.

    LAMIA is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    LAMIA is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Foobar.  If not, see <https://www.gnu.org/licenses/>.

"""
"""
  * Copyright (c) 2017-2020 ARTELIA Commit <lamia@arteliagroup.com>
  * 
  * SPDX-License-Identifier: GPL-3.0-or-later
  * License-Filename: LICENSING.md
 """

import os
import io
import sys

import qgis
from qgis.PyQt import uic, QtGui, QtCore
from qgis.PyQt.QtWidgets import (
    QWidget,
    QLabel,
    QFrame,
    QTreeWidgetItem,
    QHeaderView,
    QAbstractItemView,
    QTableWidgetItem,
)

from Lamia.iface.qgiswidget.tools.lamia_abstracttool import AbstractLamiaTool
from Lamia.libslamia.lamianetworkx.lamianetworkx import NetWorkCore

from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar,
)

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import networkx
import numpy as np
import shutil
import logging


# ********************************************************************************************************************
# ********************************* Main Widget                *******************************************************
# ********************************************************************************************************************

# class PathTool(AbstractInspectionDigueTool):
class NetworkTool(AbstractLamiaTool):

    # DBASES = ["digue", "base_digue"]
    # TOOLNAME = "Networktool"

    POSTPROTOOLNAME = "networktool"

    tooltreewidgetCAT = QtCore.QCoreApplication.translate("base3", "Network")
    tooltreewidgetSUBCAT = QtCore.QCoreApplication.translate("base3", "Networktools")
    tooltreewidgetICONPATH = os.path.join(
        os.path.dirname(__file__), "lamia_tool_network_icon.png"
    )

    def __init__(self, **kwargs):
        super(NetworkTool, self).__init__(**kwargs)

        self.qgiscanvas = self.mainifacewidget.qgiscanvas

        self.networkcore = NetWorkCore(
            self.dbase,
            messageinstance=self.dbase.messageinstance,
            qgiscanvas=self.qgiscanvas,
        )

        # rubberband var
        self.rubberBand = qgis.gui.QgsRubberBand(
            self.qgiscanvas.canvas,
            self.qgiscanvas.layers["edge"]["layer"].geometryType(),
        )
        self.rubberBand.setWidth(5)
        self.rubberBand.setColor(QtGui.QColor("magenta"))

    """
    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = "Synthese"
        self.NAME = "Chemins"
        self.visualmode = [4]
        # self.PointENABLED = True
        # self.LineENABLED = True
        # self.PolygonEnabled = True
        # self.magicfunctionENABLED = True
        # self.linkagespec = None
        # self.pickTable = None
        # print(self.dbase.recentsdbase)

        return  # TODO

        if self.dbase.dbasetype == "spatialite":
            fielpathname = (
                "path_" + os.path.basename(self.dbase.spatialitefile).split(".")[0]
            )
        elif self.dbase.dbasetype == "postgis":
            fielpathname = (
                "path_"
                + str(self.dbase.pghost)
                + "_"
                + str(self.dbase.pgdb)
                + "_"
                + str(self.dbase.pgschema)
            )
        self.dbasetablename = os.path.join(
            os.path.dirname(__file__), "..", "config", fielpathname + ".txt"
        )
        # networkx var
        self.nxgraph = None
        self.ids = None
        self.indexnoeuds = None
        self.infralinfaces = None
        self.reverseinfralinfaces = None
        self.indexnoeuds = None
        # rubberband var
        self.rubberBand = qgis.gui.QgsRubberBand(
            self.canvas, self.dbase.dbasetables["Infralineaire"]["layer"].geometryType()
        )
        self.rubberBand.setWidth(5)
        self.rubberBand.setColor(QtGui.QColor("magenta"))

        self.rubberbandtrack = qgis.gui.QgsVertexMarker(self.canvas)
        self.rubberbandtrack.setColor(QtGui.QColor(QtCore.Qt.red))
        self.rubberbandtrack.setIconSize(5)
        self.rubberbandtrack.setIconType(
            qgis.gui.QgsVertexMarker.ICON_BOX
        )  # or ICON_CROSS, ICON_X
        self.rubberbandtrack.setPenWidth(3)
        # matplotlib var
        self.figuretype = plt.figure()
        self.axtype = self.figuretype.add_subplot(111)

        self.postOnActivation()

        self.iconpath = os.path.join(
            os.path.dirname(__file__), "Lamia_path_tool_icon.png"
        )

        # ****************************************************************************************
        # properties ui
        self.groupBox_elements.setParent(None)
        self.frame_editing.setParent(None)
    """

    # def initFieldUI(self):
    def initMainToolWidget(self):

        # userui

        self.toolwidgetmain = UserUI()
        self.analysistypedict = {
            QtCore.QCoreApplication.translate("base3", "Geographic"): "geographic",
            QtCore.QCoreApplication.translate("base3", "Topologic"): "topologic",
        }

        self.toolwidgetmain.comboBox_analysistype.addItems(
            list(self.analysistypedict.keys())
        )

        """
        self.linkuserwdgfield = [
            self.userwdgfield.lineEdit_nom,
            self.userwdgfield.lineEdit_start,
            self.userwdgfield.lineEdit_end,
        ]

        self.linkuserwdgfield = {
            self.dbasetablename: [
                self.userwdgfield.lineEdit_nom,
                self.userwdgfield.lineEdit_start,
                self.userwdgfield.lineEdit_end,
            ]
        }

        """
        # * compute graph
        self.toolwidgetmain.pushButton_computegraph.clicked.connect(self.computeNxGraph)
        self.toolwidgetmain.comboBox_analysistype.currentIndexChanged.connect(
            self.comboTypeChanged
        )
        self.toolwidgetmain.doubleSpinBox_analysisaccuracy.valueChanged.connect(
            self.comboTypeChanged
        )

        # * Shortest Path
        self.toolwidgetmain.pushButton_pickstart.clicked.connect(self.getPickResult)
        self.toolwidgetmain.pushButton_pickend.clicked.connect(self.getPickResult)

        # * subdomains

        self.headerfields = ["Graph index", "Edges pk"]
        self.toolwidgetmain.tableWidget_subdomains.setRowCount(0)
        self.toolwidgetmain.tableWidget_subdomains.setColumnCount(
            len(self.headerfields)
        )
        self.toolwidgetmain.tableWidget_subdomains.setHorizontalHeaderLabels(
            self.headerfields
        )

        self.toolwidgetmain.tableWidget_subdomains.setSelectionBehavior(
            QAbstractItemView.SelectRows
        )
        self.toolwidgetmain.tableWidget_subdomains.itemSelectionChanged.connect(
            self._subDomainsCellChanged
        )
        self.toolwidgetmain.pushButton_analysesubdomains.clicked.connect(
            self.analyseSubdomains
        )

        """
        # plot
        if False:
            self.plotWdg = pg.PlotWidget()
            datavline = pg.InfiniteLine(
                0, angle=90, pen=pg.mkPen("r", width=1), name="cross_vertical"
            )
            datahline = pg.InfiniteLine(
                0, angle=0, pen=pg.mkPen("r", width=1), name="cross_horizontal"
            )
            self.plotWdg.addItem(datavline)
            self.plotWdg.addItem(datahline)
            self.userwdgfield.frame_chart.layout().addWidget(self.plotWdg)
            self.userwdgfield.checkBox_track.stateChanged.connect(
                self.activateMouseTracking
            )
            self.doTracking = True
            self.showcursor = True

            self.userwdgfield.comboBox_chart_theme.addItems(["Profil"])
            self.userwdgfield.comboBox_chart_theme.currentIndexChanged.connect(
                self.computeGraph
            )
        if True:
            self.figuretype = plt.figure()
            self.axtype = self.figuretype.add_subplot(111)
            self.mplfigure = FigureCanvas(self.figuretype)
            self.userwdgfield.frame_chart.layout().addWidget(self.mplfigure)
            self.toolbar = NavigationToolbar(
                self.mplfigure, self.userwdgfield.frame_chart
            )
            self.userwdgfield.frame_chart.layout().addWidget(self.toolbar)

            self.userwdgfield.comboBox_chart_theme.currentIndexChanged.connect(
                self.computeGraph
            )


        """

    def ________________GraphCompute():
        pass

    def postToolTreeWidgetCurrentItemChanged(self):
        self.toolwidgetmain.pushButton_computegraph.setStyleSheet("")
        self.toolwidgetmain.tabWidget.setEnabled(False)

    def computeNxGraph(self):
        analysistype, tolerance = self._getAnalysisSpec()
        self.networkcore.computeNXGraph(graphtype=analysistype, tolerance=tolerance)
        self.toolwidgetmain.pushButton_computegraph.setStyleSheet(
            "background-color: green"
        )
        self.toolwidgetmain.tabWidget.setEnabled(True)

    def comboTypeChanged(self):
        self.toolwidgetmain.pushButton_computegraph.setStyleSheet("")
        self.toolwidgetmain.tabWidget.setEnabled(False)
        self.toolwidgetmain.tableWidget_subdomains.setRowCount(0)

    def _getAnalysisSpec(self):

        analysistype = self.toolwidgetmain.comboBox_analysistype.currentText()
        analysistype = self.analysistypedict[analysistype]
        tolerance = self.toolwidgetmain.doubleSpinBox_analysisaccuracy.value()
        return analysistype, tolerance

    def unloadWidgetInToolFrame(self):
        self.rubberBand.reset(1)
        self.mainifacewidget.qgiscanvas.layers["edge"]["layerqgis"].removeSelection()
        self.toolwidgetmain.tableWidget_subdomains.setRowCount(0)

    def ________________ShortestPathFunctions():
        pass

    def getPickResult(self):

        if self.sender() == self.toolwidgetmain.pushButton_pickstart:
            self.tempbutton = "start"
        elif self.sender() == self.toolwidgetmain.pushButton_pickend:
            self.tempbutton = "end"

        pointemitter = self.qgiscanvas.pointEmitter
        try:
            pointemitter.canvasClicked.disconnect(self.selectPathPickedFeature)
        except TypeError:
            pass
        # try:
        #     self.qgiscanvas.canvas.mapToolSet.disconnect(self.qgiscanvas.toolsetChanged)
        # except TypeError:
        #     pass
        pointemitter.canvasClicked.connect(self.selectPathPickedFeature)
        # self.qgiscanvas.canvas.mapToolSet.connect(self.qgiscanvas.toolsetChanged)
        self.qgiscanvas.canvas.setMapTool(pointemitter)

    def selectPathPickedFeature(self, point):

        point = self.qgiscanvas.xformreverse.transform(point)
        indexnode, nodegeom = self.networkcore.nearestNode(point)
        point2 = qgis.core.QgsPointXY(nodegeom[0], nodegeom[1])

        self.rubberBand.reset(self.qgiscanvas.layers["edge"]["layer"].geometryType())
        try:
            self.pointEmitter.canvasClicked.disconnect(self.selectPathPickedFeature)
        except:
            pass

        if self.tempbutton == "start":
            self.toolwidgetmain.lineEdit_start.setText(
                str(point2.x()) + "," + str(point2.y())
            )
        elif self.tempbutton == "end":
            self.toolwidgetmain.lineEdit_end.setText(
                str(point2.x()) + "," + str(point2.y())
            )
        self.displayShortestPath()

    def displayShortestPath(self):
        point1, point2 = self._getPointFromLineedit()
        if point1 is None or point2 is None:
            return

        qgisgeom, shortestpks = self.networkcore.getQgisgeomBetweenPoints(
            point1, point2
        )
        if qgisgeom is None:
            return

        geomforrubberband = qgis.core.QgsGeometry(qgisgeom)
        geomforrubberband.transform(self.qgiscanvas.xform)
        self.rubberBand.addGeometry(geomforrubberband, None)

        self.toolwidgetmain.textBrowser_pathpks.setPlainText(str(shortestpks))

    def _getPointFromLineedit(self):
        try:
            point1 = [
                float(elem1)
                for elem1 in self.toolwidgetmain.lineEdit_start.text().split(",")
            ]

            point2 = [
                float(elem1)
                for elem1 in self.toolwidgetmain.lineEdit_end.text().split(",")
            ]

        except ValueError:
            print("ValueError")
            return None, None

        return point1, point2

    def ________________SubdomainsFunctions():
        pass

    def analyseSubdomains(self):

        self.subdomainedgelist = self.networkcore.getSubGraphsEdgePks()

        self.toolwidgetmain.tableWidget_subdomains.setRowCount(0)
        for i, row in enumerate(self.subdomainedgelist):
            self.toolwidgetmain.tableWidget_subdomains.insertRow(i)
            item = QTableWidgetItem(str(i))
            self.toolwidgetmain.tableWidget_subdomains.setItem(i, 0, item)
            item = QTableWidgetItem(str(row))
            self.toolwidgetmain.tableWidget_subdomains.setItem(i, 1, item)

    def _subDomainsCellChanged(self):

        self.mainifacewidget.qgiscanvas.layers["edge"]["layerqgis"].removeSelection()

        rowindexes = [
            row.row()
            for row in self.toolwidgetmain.tableWidget_subdomains.selectionModel().selectedRows()
        ]

        for currentRow in rowindexes:
            pkedges = self.subdomainedgelist[currentRow]
            self.mainifacewidget.qgiscanvas.layers["edge"]["layerqgis"].select(pkedges)

    def selectPickedFeature(self, point):
        nearestpk, dist = self.mainifacewidget.qgiscanvas.getNearestPk(
            "edge", point, comefromcanvas=True, fieldconstraint=None
        )
        for i, pksublist in enumerate(self.subdomainedgelist):
            if nearestpk in pksublist:
                self.toolwidgetmain.tableWidget_subdomains.selectRow(i)

    def computeGraph(self):
        # print('computeGraph')
        # self.plotwdg = self.plotWdg

        self.axtype.clear()

        if False:
            pitems = self.plotWdg.getPlotItem().listDataItems()
            for item in pitems:
                self.plotWdg.removeItem(item)
            try:
                self.plotWdg.scene().sigMouseMoved.disconnect(self.mouseMoved)
            except:
                pass

        datas = self.getGraphData()
        # print('datas', datas)
        # x=[0, self.geomfinal.length()]
        # y = [0,0]
        # self.plotWdg.plot(x, y, pen=pg.mkPen(model1.item(i, 1).data(Qt.BackgroundRole), width=2), name=tmp_name)
        if False:
            self.plotWdg.addLegend()
            for dataname in datas.keys():
                # print(dataname.split('-')[1])
                if dataname.split("-")[1] == "CRE":
                    penforgraph = pg.mkPen(
                        color="k", width=3, style=QtCore.Qt.SolidLine
                    )
                elif dataname.split("-")[1] == "TNT":
                    penforgraph = pg.mkPen(
                        color="g", width=3, style=QtCore.Qt.SolidLine
                    )
                else:
                    penforgraph = pg.mkPen(color="b", width=3, style=QtCore.Qt.DashLine)
                datavalues = datas[dataname]
                self.plotWdg.plot(
                    datavalues["x"], datavalues["y"], name=dataname, pen=penforgraph
                )

            self.plotWdg.getViewBox().autoRange(
                items=self.plotWdg.getPlotItem().listDataItems()
            )
            self.plotWdg.getViewBox().disableAutoRange()

        if True:
            for dataname in datas.keys():
                # print(dataname.split('-')[1])
                if False:
                    if dataname.split("-")[1] == "CRE":
                        penforgraph = pg.mkPen(
                            color="k", width=3, style=QtCore.Qt.SolidLine
                        )
                    elif dataname.split("-")[1] == "TNT":
                        penforgraph = pg.mkPen(
                            color="g", width=3, style=QtCore.Qt.SolidLine
                        )
                    else:
                        penforgraph = pg.mkPen(
                            color="b", width=3, style=QtCore.Qt.DashLine
                        )
                datavalues = datas[dataname]

                self.axtype.plot(datavalues["x"], datavalues["y"])
                # self.axtype.grid()
            self.figuretype.canvas.draw()
        # self.plotWdg.addLegend()

    def resizewidget(self, w, h):

        if False:
            self.plotWdg.resize(w, h)
        if True:
            win = pg.GraphicsWindow()
            win.resize(w, h)
        if True:
            export_area = pg.GraphicsLayoutWidget(border=(50, 50, 50))
            export_area.setBackground("w")
            export_area.resize(w, h)
            export_area.setVisible(True)
            export_area.setVisible(False)


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        # self.setupUi(self)
        uipath = os.path.join(os.path.dirname(__file__), "lamia_tool_network_ui.ui")
        uic.loadUi(uipath, self)
