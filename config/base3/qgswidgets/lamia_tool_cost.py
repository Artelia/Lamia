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
    QComboBox,
    QAbstractItemView,
    QTableWidgetItem,
    QApplication,
    QTableWidget,
)


# from ...Lamia_abstract_tool import AbstractLamiaTool

from Lamia.qgisiface.iface.qgiswidget.tools.lamia_abstracttool import AbstractLamiaTool
from Lamia.qgisiface.iface.qgiswidget.tools.general_subwidgets.abstractfilemanager import (
    AbstractFileManager,
)
from Lamia.api.libslamia.lamiacost.lamiacost import CostCore


class CostTool(AbstractLamiaTool):

    POSTPROTOOLNAME = CostCore.POSTPROTOOLNAME

    tooltreewidgetCAT = QtCore.QCoreApplication.translate("base3", "Overview")
    tooltreewidgetSUBCAT = QtCore.QCoreApplication.translate("base3", "Costs")
    tooltreewidgetICONPATH = os.path.join(
        os.path.dirname(__file__), "lamia_tool_cost_icon.png"
    )

    choosertreewidgetMUTIPLESELECTION = True

    def __init__(self, **kwargs):
        super(CostTool, self).__init__(**kwargs)
        self.costtool = CostCore(
            dbaseparser=self.dbase, messageinstance=self.mainifacewidget.connector
        )
        self.filemanager = CostfileManager(self.mainifacewidget, self.costtool)

    def initMainToolWidget(self):

        self.toolwidgetmain = UserUI()

        self.combowdg = QComboBox()
        self.mainifacewidget.frame_4.layout().insertWidget(0, self.combowdg)
        self.combowdg.setVisible(False)

        self.toolwidgetmain.frame_filemanager.layout().addWidget(self.filemanager)

        self.toolwidgetmain.tableWidget.installEventFilter(self)

        self.toolwidgetmain.toolButton_calcul.clicked.connect(self.launchCostCalculus)

        self.toolwidgetmain.toolButton_copier.clicked.connect(self.copier)
        self.toolwidgetmain.toolButton_selected.clicked.connect(self.goToSelectedId)
        self.toolwidgetmain.toolButton_selected.setEnabled(False)

        self.choosertreewidget = self.mainifacewidget.toolwidgets[
            "geoarea"
        ].choosertreewidget

    def launchCostCalculus(self):
        filename = self.filemanager.getCurrentText()

        selectedzonegeoitems = self.choosertreewidget.treewidget.selectedItems()
        ids = [int(item.text(0)) for item in selectedzonegeoitems]
        pdids = self.choosertreewidget.ids
        pks = [pdids.loc[pdids["id"] == id]["pk"].values[0] for id in ids]

        bordereau, sqlresult, pricelist = self.costtool.runCost(
            costfilepath=filename, pkzonegeos=pks
        )

        self.writeResultsInTable(bordereau, sqlresult, pricelist)

    def postToolTreeWidgetCurrentItemChanged(self):
        self.filemanager.reset()

    def writeResultsInTable(self, bordereau, sqlresult, pricelist):

        self.toolwidgetmain.tableWidget.clear()
        columnlenght = len(bordereau["fields"]) + 1
        self.toolwidgetmain.tableWidget.setColumnCount(columnlenght)
        header = bordereau["fields"] + ["Prix"]
        self.toolwidgetmain.tableWidget.setHorizontalHeaderLabels(header)

        self.toolwidgetmain.tableWidget.setRowCount(0)

        for i, resfin in enumerate(sqlresult):
            lastrow = self.toolwidgetmain.tableWidget.rowCount()
            self.toolwidgetmain.tableWidget.insertRow(lastrow)

            for j, field in enumerate(bordereau["fields"]):
                tablename = None
                fieldname = None
                valuetoinsert = ""
                try:
                    tablename = field.split(".")[0].split("_")[0]
                    fieldname = field.split(".")[1]
                except:
                    pass
                if tablename is not None:
                    # print(tablename, fieldname, resfin[j])
                    if sys.version_info.major == 2:
                        if not isinstance(resfin[j], unicode):
                            valuetoinsert = str(
                                self.dbase.getConstraintTextFromRawValue(
                                    tablename, fieldname, resfin[j]
                                )
                            )
                        else:
                            valuetoinsert = self.dbase.getConstraintTextFromRawValue(
                                tablename, fieldname, resfin[j]
                            )

                    else:
                        valuetoinsert = str(
                            self.dbase.getConstraintTextFromRawValue(
                                tablename, fieldname, resfin[j]
                            )
                        )

                else:
                    valuetoinsert = resfin[j]

                self.toolwidgetmain.tableWidget.setItem(
                    lastrow, j, QTableWidgetItem(valuetoinsert)
                )

            # price
            self.toolwidgetmain.tableWidget.setItem(
                lastrow, columnlenght - 1, QTableWidgetItem(str(pricelist[i]))
            )

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.KeyPress and event.matches(
            QtGui.QKeySequence.Copy
        ):
            self.copier()
            return True
        # return True
        return super(CostTool, self).eventFilter(source, event)

    def copier(self, var=None):
        """copier la zone sélectionnée dans le clipboard
        """
        # emplacement sélectionné pour copier dans le clipboard

        texte = ""

        # copy header
        lenheader = self.toolwidgetmain.tableWidget.columnCount()
        for i in range(lenheader):
            texte += (
                self.toolwidgetmain.tableWidget.horizontalHeaderItem(i).text() + "\t"
            )
        texte = texte[:-1] + "\n"

        selected = self.toolwidgetmain.tableWidget.selectedRanges()

        beginrow = 0
        endrow = 0
        begincolumn = 0
        encolumn = 0

        if len(selected) > 0:
            beginrow = selected[0].topRow()
            endrow = selected[0].bottomRow() + 1
            begincolumn = selected[0].leftColumn()
            encolumn = selected[0].rightColumn() + 1
        else:
            beginrow = 0
            endrow = self.toolwidgetmain.tableWidget.rowCount()
            begincolumn = 0
            encolumn = self.toolwidgetmain.tableWidget.columnCount()

        # construction du texte à copier, ligne par ligne et colonne par colonne

        # for i in range(selected[0].topRow(), selected[0].bottomRow() + 1):
        for i in range(beginrow, endrow):
            # for j in range(selected[0].leftColumn(), selected[0].rightColumn() + 1):
            for j in range(begincolumn, encolumn):
                try:
                    texte += self.toolwidgetmain.tableWidget.item(i, j).text() + "\t"
                except AttributeError:
                    # quand une case n'a jamais été initialisée
                    texte += "\t"
            texte = texte[:-1] + "\n"  # le [:-1] élimine le '\t' en trop

        # enregistrement dans le clipboard
        QApplication.clipboard().setText(texte)

    def goToSelectedId(self):
        pass


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        # self.setupUi(self)
        uipath = os.path.join(os.path.dirname(__file__), "lamia_tool_cost_ui.ui")
        uic.loadUi(uipath, self)


class CostfileManager(AbstractFileManager):
    def __init__(self, mainwindows=None, parentwdg=None):
        super(CostfileManager, self).__init__(mainwindows, parentwdg)
