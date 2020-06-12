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


import os, sys, datetime
import xlrd

from qgis.PyQt import uic, QtCore
from qgis.PyQt.QtWidgets import (
    QWidget,
    QTabWidget,
    QHeaderView,
    QTableWidgetItem,
    QComboBox,
    QTextBrowser,
)

from ...base3.qgswidgets.lamia_form_observation import BaseObservationTool
from Lamia.libslamia.constructionsitesubobservation.cssubobservationparser import (
    SubObservationParser,
)


class BaseConstructionsiteSubObservationTool(BaseObservationTool):

    PREPROTOOLNAME = "subobservation"
    tooltreewidgetSUBCAT = None
    tempparentjoin = {}
    PARENTJOIN = {
        "observation": {
            "colparent": "id_observation",
            "colthistable": "lid_observation",
            "tctable": None,
            "tctablecolparent": None,
            "tctablecolthistable": None,
        }
    }

    CHOOSERTREEWDGSPEC = {"colshow": ["name"]}

    def __init__(self, **kwargs):
        super(BaseConstructionsiteSubObservationTool, self).__init__(**kwargs)
        self.sheetparser = SubObservationParser("orange")
        self.sousfichesdict = self.sheetparser.createDictionnary()

    def initMainToolWidget(self):

        if self.dbase.variante in ["Orange"]:

            self.toolwidgetmain = UserUI()
            self.formtoolwidgetconfdictmain = {
                "observation": {
                    "linkfield": "id_observation",
                    "widgets": {
                        "datetimeobservation": self.toolwidgetmain.dateTimeEdit_datetimeobservation,
                    },
                },
                "object": {"linkfield": "id_object", "widgets": {}},
            }
            listcomboitems = []
            for fichekey in self.sousfichesdict.keys():
                listcomboitems.append(
                    fichekey + " " + self.sousfichesdict[fichekey]["name"]
                )
            # typessousfiches = self.sousfichesdict.keys()
            self.toolwidgetmain.comboBox_fichetype.addItems(listcomboitems)
            self.toolwidgetmain.comboBox_fichetype.currentIndexChanged.connect(
                self.SousFicheTypeChanged
            )
            self.toolwidgetmain.comboBox_fichetype.currentIndexChanged.emit(0)

            # self.frame_editing.setVisible(False)
            # self.frame_editing.setParent(None)

    def SousFicheTypeChanged(self, comboindex):
        currentcombotext = self.toolwidgetmain.comboBox_fichetype.currentText()
        currentdict = self.sousfichesdict[currentcombotext.split(" ")[0]]

        self.toolwidgetmain.tableWidget.setRowCount(0)
        self.toolwidgetmain.tableWidget.clear()
        self.toolwidgetmain.tableWidget.setColumnCount(4)

        self.toolwidgetmain.tableWidget.setHorizontalHeaderLabels(
            ["N°", "Critere", "Contrôle", "Observation"]
        )

        header = self.toolwidgetmain.tableWidget.horizontalHeader()

        for dataindex in currentdict["datas"].keys():
            rowPosition = self.toolwidgetmain.tableWidget.rowCount()
            self.toolwidgetmain.tableWidget.insertRow(rowPosition)

            if (
                currentdict["datas"][dataindex]["description"] is not None
            ):  # it is not a comment
                item = QTableWidgetItem(dataindex)
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.toolwidgetmain.tableWidget.setItem(rowPosition, 0, item)

                item = QTableWidgetItem(currentdict["datas"][dataindex]["description"])
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.toolwidgetmain.tableWidget.setItem(rowPosition, 1, item)

                if currentdict["datas"][dataindex]["type"] is None:
                    wdg = QComboBox()
                    wdg.addItems(["Avec réserve", "sans réserve", "sans objet"])
                    self.toolwidgetmain.tableWidget.setCellWidget(rowPosition, 2, wdg)
                else:
                    item = QTableWidgetItem()
                    self.toolwidgetmain.tableWidget.setItem(rowPosition, 2, item)
                    item.setBackground(QtCore.Qt.gray)
                    item.setFlags(QtCore.Qt.NoItemFlags)

                wdg = QTextBrowser()
                wdg.setMinimumHeight(30)
                wdg.setMaximumHeight(50)
                wdg.setReadOnly(False)
                self.toolwidgetmain.tableWidget.setCellWidget(rowPosition, 3, wdg)
            else:
                item = QTableWidgetItem(dataindex)
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.toolwidgetmain.tableWidget.setItem(rowPosition, 1, item)

            self.toolwidgetmain.tableWidget.setWordWrap(True)
            self.toolwidgetmain.tableWidget.resizeColumnToContents(0)
            self.toolwidgetmain.tableWidget.setColumnWidth(1, 200)
            self.toolwidgetmain.tableWidget.resizeRowsToContents()
            header.setStretchLastSection(True)

    # def postInitFeatureProperties(self, feat):
    def postSelectFeature(self):
        if self.currentFeaturePK is None:
            self.toolwidgetmain.comboBox_fichetype.setEnabled(True)
            self.toolwidgetmain.comboBox_fichetype.setCurrentIndex(0)
            self.toolwidgetmain.comboBox_fichetype.currentIndexChanged.emit(0)
            if (
                self.parentWidget is not None
                and self.parentWidget.currentFeaturePK is not None
            ):  # copy last obs text
                # datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                # self.initFeatureProperties(feat, self.DBASETABLENAME, 'datetimeobservation', datecreation)
                datecreation = str(
                    datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                )
                self.formutils.applyResultDict(
                    {"datetimeobservation": datecreation}, checkifinforgottenfield=False
                )

        else:
            self.toolwidgetmain.comboBox_fichetype.setEnabled(False)
            self.loadTableFeature()

    def postSaveFeature(self, savedfeaturepk=None):
        self.saveTableFeature(savedfeaturepk)
        currentcombotext = self.toolwidgetmain.comboBox_fichetype.currentText()
        # currentdict = self.sousfichesdict[currentcombotext.split(' ')[0]]

        pkobject = self.dbase.getValuesFromPk(
            "observation_qgis", "pk_object", savedfeaturepk
        )
        sql = f"UPDATE object SET name = '{currentcombotext}' WHERE pk_object = {pkobject}"
        self.dbase.query(sql)
        # self.dbase.dbasetables['Desordre']['layerqgis'].triggerRepaint()
        self.mainifacewidget.qgiscanvas.layers["deficiency"][
            "layerqgis"
        ].triggerRepaint()

    def loadTableFeature(self):
        # get typeobservation
        sql = (
            "SELECT observationcategory FROM Observation WHERE pk_observation = "
            + str(self.currentFeaturePK)
        )
        res = self.dbase.query(sql)[0][0]

        # for nomsousfiche in self.sousfichesdict.keys():
        #     if nomsousfiche.split(' ')[0] == res:
        #         self.toolwidgetmain.comboBox_fichetype.setCurrentText(nomsousfiche)
        #         break

        if res not in self.sousfichesdict.keys():
            return

        self.toolwidgetmain.comboBox_fichetype.setCurrentText(
            res + " " + self.sousfichesdict[res]["name"]
        )

        for i in range(self.toolwidgetmain.tableWidget.rowCount()):

            item = self.toolwidgetmain.tableWidget.item(i, 0)
            if item is not None:
                itemtext0 = item.text().split(".")[-1]
                sql = (
                    "SELECT item_type_"
                    + str(itemtext0)
                    + " , item_obs_"
                    + str(itemtext0)
                    + " FROM observation "
                )
                sql += " WHERE pk_observation = " + str(self.currentFeaturePK)

                itemtype, itemobs = self.dbase.query(sql)[0]
                if not self.dbase.utils.isAttributeNull(itemtype):
                    self.toolwidgetmain.tableWidget.cellWidget(i, 2).setCurrentIndex(
                        itemtype
                    )
                self.toolwidgetmain.tableWidget.cellWidget(i, 3).setPlainText(itemobs)

    def saveTableFeature(self, featurepk):
        sqlupdate = []

        # typeobservation
        sqlupdate.append(
            "observationcategory = '"
            + self.toolwidgetmain.comboBox_fichetype.currentText().split(" ")[0]
            + "'"
        )

        # table values
        for i in range(self.toolwidgetmain.tableWidget.rowCount()):
            item = self.toolwidgetmain.tableWidget.item(i, 0)
            if item is not None:
                itemtext0 = item.text().split(".")[-1]
                indexitem = int(itemtext0)

                if self.toolwidgetmain.tableWidget.cellWidget(i, 2) is not None:
                    columname = "item_type_" + str(indexitem)
                    value = self.toolwidgetmain.tableWidget.cellWidget(
                        i, 2
                    ).currentIndex()
                    sqlupdate.append(columname + " = " + str(value))

                columname = "item_obs_" + str(indexitem)
                value = self.toolwidgetmain.tableWidget.cellWidget(i, 3).toPlainText()
                sqlupdate.append(columname + " = '" + str(value) + "'")

        sql = " UPDATE observation SET " + ", ".join(sqlupdate)
        sql += " WHERE pk_observation = " + str(featurepk)

        self.dbase.query(sql)


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(
            os.path.dirname(__file__), "lamia_form_subobservation_ui.ui"
        )
        uic.loadUi(uipath, self)
