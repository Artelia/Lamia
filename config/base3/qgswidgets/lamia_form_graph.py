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
import datetime
import sys

import matplotlib

matplotlib.use("agg")
import matplotlib.pyplot as plt

font = {"family": "normal", "weight": "bold", "size": 8}
matplotlib.rc("font", **font)
# matplotlib.rc('xtick', labelsize=20)
# matplotlib.rc('ytick', labelsize=20)
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar,
)


from qgis.PyQt import uic, QtCore
from qgis.PyQt.QtWidgets import (
    QWidget,
    QComboBox,
    QDoubleSpinBox,
    QSpinBox,
    QHeaderView,
    QTableWidgetItem,
)

from Lamia.qgisiface.iface.qgiswidget.tools.lamia_abstractformtool import (
    AbstractLamiaFormTool,
)
from Lamia.api.libslamia.lamiagraph.lamiagraph import GraphMaker


class BaseGraphTool(AbstractLamiaFormTool):

    PREPROTOOLNAME = "graphdb"
    DBASETABLENAME = "graph"
    LOADFIRST = False

    tooltreewidgetCAT = QtCore.QCoreApplication.translate("base3", "Resources")
    tooltreewidgetSUBCAT = QtCore.QCoreApplication.translate("base3", "Graph")
    tooltreewidgetICONPATH = os.path.join(
        os.path.dirname(__file__), "lamia_form_graph_icon.png"
    )

    tempparentjoin = {}
    linkdict = {
        "colparent": "id_object",
        "colthistable": "id_resource",
        "tctable": "tcobjectresource",
        "tctablecolparent": "lid_object",
        "tctablecolthistable": "lid_resource",
    }
    for tablename in ["profile", "node", "edge", "surface", "facility"]:
        tempparentjoin[tablename] = linkdict
    PARENTJOIN = tempparentjoin
    TABLEFILTERFIELD = {"graphtype": "TAB"}

    def __init__(self, **kwargs):
        super(BaseGraphTool, self).__init__(**kwargs)

        self.graphmaker = GraphMaker(self.dbase)
        self.figuretype = self.graphmaker.figuretype
        self.mplfigure = FigureCanvas(self.figuretype)
        self.graphspec = self.graphmaker.graphspec

    def initMainToolWidget(self):
        # ****************************************************************************************
        #   userui Field

        self.toolwidgetmain = UserUI()
        self.formtoolwidgetconfdictmain = {
            "graph": {
                "linkfield": "id_graph",
                "widgets": {"graphsubtype": self.toolwidgetmain.comboBox_graphtype},
            },
            "object": {"linkfield": "id_object", "widgets": {}},
            "resource": {"linkfield": "id_resource", "widgets": {}},
        }

        self.toolwidgetmain.pushButton_addline.clicked.connect(self.addrow)
        self.toolwidgetmain.pushButton_delline.clicked.connect(self.removerow)
        self.enableTypeComboBox()

        self.toolwidgetmain.frame_graph.layout().addWidget(self.mplfigure)
        self.toolbar = NavigationToolbar(
            self.mplfigure, self.toolwidgetmain.frame_graph
        )
        self.toolwidgetmain.frame_graph.layout().addWidget(self.toolbar)

    def postSelectFeature(self):
        self._disableSubtypeNotInSpec()
        self.toolwidgetmain.tableWidget.setRowCount(0)

        if self.currentFeaturePK is None:
            datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            self.formutils.applyResultDict(
                {"datetimeresource": datecreation}, checkifinforgottenfield=False
            )
            self.toolwidgetmain.tableWidget.setRowCount(0)

        else:
            graphtype = self._getGraphType()
            typetext = self.dbase.getConstraintTextFromRawValue(
                self.DBASETABLENAME, "graphsubtype", graphtype
            )
            self.toolwidgetmain.comboBox_graphtype.setCurrentIndex(
                self.toolwidgetmain.comboBox_graphtype.findText(typetext)
            )
            graphdatas = self.graphmaker.getGraphData(self.currentFeaturePK)
            self._fillTableWidgetWithDatas(graphdatas)

        self.graphmaker.showGraph(self.currentFeaturePK)
        self.enableTypeComboBox()

    def _disableSubtypeNotInSpec(self):

        subtypes = self.dbase.dbasetables[self.DBASETABLENAME]["fields"][
            "graphsubtype"
        ]["Cst"]

        for i, elem in enumerate(subtypes):
            if self.toolwidgetmain.comboBox_graphtype.model().item(i):
                if elem[1] not in list(self.graphspec.keys()):
                    self.toolwidgetmain.comboBox_graphtype.model().item(i).setEnabled(
                        False
                    )
                else:
                    self.toolwidgetmain.comboBox_graphtype.model().item(i).setEnabled(
                        True
                    )

    def postSaveFeature(self, savedfeaturepk=None):

        valuestosave = []
        for i, row in enumerate(range(self.toolwidgetmain.tableWidget.rowCount())):
            # get values
            typetext = self.toolwidgetmain.comboBox_graphtype.currentText()
            graphtype = self.dbase.getConstraintRawValueFromText(
                self.DBASETABLENAME, "graphsubtype", typetext
            )
            listchamp = ",".join(self.graphspec[graphtype].keys())
            values = []
            for column, field in enumerate(self.graphspec[graphtype]):
                if self.toolwidgetmain.tableWidget.cellWidget(row, column) is not None:
                    columnwdg = self.toolwidgetmain.tableWidget.cellWidget(row, column)
                    if isinstance(columnwdg, QComboBox):
                        value = (
                            "'"
                            + self.dbase.getConstraintRawValueFromText(
                                "graphdata", field, columnwdg.currentText()
                            )
                            + "'"
                        )
                    elif isinstance(columnwdg, QDoubleSpinBox) or isinstance(
                        columnwdg, QSpinBox
                    ):
                        value = str(columnwdg.value())
                        if value is None:
                            value = "0.0"
                    else:
                        value = "NULL"
                values.append(value)
            valuestosave.append(values)

        self.graphmaker.saveGraphData(savedfeaturepk, valuestosave)

    def addrow(self):
        introw = self.toolwidgetmain.tableWidget.currentRow()
        self.toolwidgetmain.tableWidget.insertRow(introw + 1)
        typegraph = self._getGraphType()
        self.toolwidgetmain.tableWidget.setColumnCount(len(self.graphspec[typegraph]))

        if typegraph in self.graphspec.keys():
            for i, field in enumerate(self.graphspec[typegraph]):
                graphiquedataelemfields = self.dbase.dbasetables["graphdata"]["fields"][
                    field
                ]
                if "Cst" in graphiquedataelemfields.keys():
                    combobox = QComboBox()
                    itemlist = [elem[0] for elem in graphiquedataelemfields["Cst"]]
                    combobox.addItems(itemlist)
                    self.toolwidgetmain.tableWidget.setCellWidget(
                        introw + 1, i, combobox
                    )
                elif graphiquedataelemfields["PGtype"] == "NUMERIC":
                    spinbox = QDoubleSpinBox()
                    spinbox.setSingleStep(0.5)
                    spinbox.setRange(-9999, 9999)
                    self.toolwidgetmain.tableWidget.setCellWidget(
                        introw + 1, i, spinbox
                    )
                elif graphiquedataelemfields["PGtype"] == "INTEGER":
                    spinbox = QSpinBox()
                    spinbox.setRange(-9999, 9999)
                    self.toolwidgetmain.tableWidget.setCellWidget(
                        introw + 1, i, spinbox
                    )

        header = self.toolwidgetmain.tableWidget.horizontalHeader()
        header.resizeSections(QHeaderView.ResizeToContents)
        header.setStretchLastSection(True)

        self.enableTypeComboBox()

    def removerow(self):
        introw = self.toolwidgetmain.tableWidget.currentRow()
        self.toolwidgetmain.tableWidget.removeRow(introw)

        self.enableTypeComboBox()

    def enableTypeComboBox(self):
        if self.toolwidgetmain.tableWidget.rowCount() == 0:
            self.toolwidgetmain.comboBox_graphtype.setEnabled(True)
        else:
            self.toolwidgetmain.comboBox_graphtype.setEnabled(False)

    def _fillTableWidgetWithDatas(self, graphdatas):
        self.toolwidgetmain.tableWidget.setRowCount(0)
        graphtype = self._getGraphType()
        header = list(self.graphspec[graphtype].values())
        self.toolwidgetmain.tableWidget.setHorizontalHeaderLabels(header)

        if graphdatas is None:
            return

        for row in graphdatas:
            self.addrow()
            lastrow = self.toolwidgetmain.tableWidget.rowCount() - 1
            self.toolwidgetmain.tableWidget.setCurrentCell(lastrow, 0)
            for col, field in enumerate(self.graphspec[graphtype].keys()):
                graphiquedataelemfields = self.dbase.dbasetables["graphdata"]["fields"][
                    field
                ]
                if "Cst" in graphiquedataelemfields.keys():
                    combo = self.toolwidgetmain.tableWidget.cellWidget(lastrow, col)
                    indexcombo = combo.findText(row[col])
                    if indexcombo >= 0:
                        combo.setCurrentIndex(indexcombo)
                elif graphiquedataelemfields["PGtype"] in ["NUMERIC", "INTEGER"]:
                    spinbox = self.toolwidgetmain.tableWidget.cellWidget(lastrow, col)
                    spinbox.setValue(row[col])

    def _getGraphType(self):
        if self.currentFeaturePK is not None:
            graphtype = self.dbase.getValuesFromPk(
                self.DBASETABLENAME, "graphsubtype", self.currentFeaturePK
            )
        else:
            typetext = self.toolwidgetmain.comboBox_graphtype.currentText()
            graphtype = self.dbase.getConstraintRawValueFromText(
                self.DBASETABLENAME, "graphsubtype", typetext
            )
        return graphtype


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), "lamia_form_graph_ui.ui")
        uic.loadUi(uipath, self)
