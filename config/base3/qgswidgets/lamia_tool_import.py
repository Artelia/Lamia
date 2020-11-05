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
from collections import OrderedDict
import datetime
import decimal
import logging, sys, re
import numpy as np
from collections import OrderedDict
from pprint import pprint

import qgis, qgis.utils
from qgis.PyQt import QtGui, uic, QtCore, QtXml
from qgis.PyQt.QtWidgets import (
    QInputDialog,
    QTableWidgetItem,
    QComboBox,
    QAction,
    QProgressBar,
    QApplication,
    QWidget,
    QToolButton,
    QDialog,
    QGridLayout,
    QSplitter,
    QLabel,
    QFrame,
    QVBoxLayout,
)


# from .importtools.InspectionDigue_Import import ImportObjetDialog
from Lamia.qgisiface.iface.qgiswidget.tools.lamia_abstracttool import AbstractLamiaTool

# from Lamia.qgisiface.iface.qgiswidget.tools.lamia_abstracttool  import AbstractLamiaTool
from Lamia.api.libslamia.lamiaimport.lamiaimport import ImportCore

# from Lamia.main.DBaseParser import DBaseParser

from .lamia_tool_import_flowchart import FlowChartWidget


class ImportTool(AbstractLamiaTool):

    POSTPROTOOLNAME = ImportCore.POSTPROTOOLNAME

    tooltreewidgetCAT = QtCore.QCoreApplication.translate("base3", "Import/export")
    tooltreewidgetSUBCAT = QtCore.QCoreApplication.translate("base3", "Import")
    tooltreewidgetICONPATH = os.path.join(
        os.path.dirname(__file__), "lamia_tool_import_icon.png"
    )

    choosertreewidgetMUTIPLESELECTION = True

    def __init__(self, **kwargs):
        super(ImportTool, self).__init__(**kwargs)

        # self.importtool = ImportCore(dbaseparser=self.dbase,
        #                             messageinstance=self.mainifacewidget.connector)
        self.qfiledlg = self.mainifacewidget.qfiledlg
        self.flowchartdlg = FlowChartWidget(
            dbase=self.dbase,
            messageinstance=self.mainifacewidget.connector,
            mainifacewidget=self.mainifacewidget,
        )

        # self.postInit()

        # self.dialog = QDialog()
        # layout = QGridLayout()
        # self.dialog.setLayout(layout)

        self.flowqlabelmessage = None
        self.currentlayer = None

    def initMainToolWidget(self):

        self.toolwidgetmain = UserUI()
        self.toolwidgetmain.toolButton_update.clicked.connect(self._updateFromTables)

        items = ["edge", "node", "equipment", "media", "actor"]
        self.toolwidgetmain.comboBox_typeimport.addItems(items)

        # methode 1
        # self.toolwidgetmain.pushButton_import.clicked.connect(self.showTable)
        # self.toolwidgetmain.pushButton_importer.clicked.connect(self.work)
        # self.toolwidgetmain.pushButton_validimport.clicked.connect(self.validImport)
        # self.toolwidgetmain.pushButton_rollback.clicked.connect(self.rollbackImport)

        # flowchart
        self.toolwidgetmain.pushButton_flowchart.clicked.connect(self.showFlowChart)
        # self.dialogui = DialogUI()

    def postToolTreeWidgetCurrentItemChanged(self):
        self._updateFromTables()

    def _updateFromTables(self):

        self.toolwidgetmain.comboBox_tableimport.clear()
        if qgis.utils.iface is not None:
            layers = [
                tree_layer.layer()
                for tree_layer in qgis.core.QgsProject.instance()
                .layerTreeRoot()
                .findLayers()
            ]
            layqgisname = []
            for tablename in self.mainifacewidget.qgiscanvas.layers.keys():
                if (
                    "layerqgis"
                    in self.mainifacewidget.qgiscanvas.layers[tablename].keys()
                ):
                    layqgisname.append(
                        self.mainifacewidget.qgiscanvas.layers[tablename][
                            "layerqgis"
                        ].name()
                    )
            for lay in layers:
                if not lay.name() in layqgisname:
                    self.toolwidgetmain.comboBox_tableimport.addItems([lay.name()])

    def ___________________________________flowchartpart(self):
        pass

    def showFlowChart(self, qgslayer=None):
        self._defineCurrentLayer()

        tolayername = self.toolwidgetmain.comboBox_typeimport.currentText()
        fromqgslayer = self.currentlayer
        self.flowchartdlg.initFromandToLayers(fromqgslayer, tolayername)

        if qgis.utils.iface is not None:
            self.flowchartdlg.setWindowModality(QtCore.Qt.NonModal)
            self.flowchartdlg.show()
        else:
            self.flowchartdlg.exec_()

    def _defineCurrentLayer(self):
        item = self.toolwidgetmain.comboBox_typeimport.currentText()

        if qgis.utils.iface is not None:
            self.currentlayer = None
            layers = [
                tree_layer.layer()
                for tree_layer in qgis.core.QgsProject.instance()
                .layerTreeRoot()
                .findLayers()
            ]
            for lay in layers:
                if self.toolwidgetmain.comboBox_tableimport.currentText() == lay.name():
                    self.currentlayer = lay
                    break

            if self.currentlayer is None:
                return
        else:  # debug outside qgis
            if self.currentlayer is None:
                import Lamia.test

                lamiapath = os.path.normpath(os.path.dirname(lamiatest.__file__))
                layerdirpath = os.path.join(lamiapath, "datas", "shpforimporttest")
                if False:
                    layerpath = os.path.join(layerdirpath, "TRONCONS_TEST.shp")
                    # print("*********layerpath", layerpath)
                    self.currentlayer = qgis.core.QgsVectorLayer(
                        layerpath, "test", "ogr"
                    )
                if True:
                    layerpath = os.path.join(layerdirpath, "te.csv")
                    # print("*********layerpath", layerpath)
                    self.currentlayer = qgis.core.QgsVectorLayer(
                        layerpath, "test", "ogr"
                    )
                print(self.currentlayer.featureCount())

    def initProgressBar(self, lenprogress):
        """
        Initialise la progress bar d'avancement de la generation du rapport
        :param idsforreportdict:
        :return:
        """
        if qgis.utils.iface is not None:
            progressMessageBar = qgis.utils.iface.messageBar().createMessage(
                "import ..."
            )
            progress = QProgressBar()

            progress.setMaximum(lenprogress)
            progress.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
            progressMessageBar.layout().addWidget(progress)
            if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                qgis.utils.iface.messageBar().pushWidget(
                    progressMessageBar, qgis.utils.iface.messageBar().INFO
                )
            else:
                qgis.utils.iface.messageBar().pushWidget(
                    progressMessageBar, qgis.core.Qgis.Info
                )
        else:
            progress = None

        return progress

    def setLoadingProgressBar(self, progressbar, val):
        if progressbar is not None:
            progressbar.setValue(val)
        else:
            if qgis.utils.iface is None:
                if val % 100 == 0:
                    logging.getLogger("Lamia").info("Import de l item %d", val)
        QApplication.processEvents()

    def validImport(self):
        self.dbase.forcenocommit = False
        sql = "COMMIT"
        self.dbase.query(sql)

    def rollbackImport(self):
        self.dbase.forcenocommit = False
        sql = "ROLLBACK"
        self.dbase.query(sql)
        if list(self.inputs().keys())[0] == "dataIn":

            if debug:
                logging.getLogger("Lamia").debug("dataIn type")
            for termname in self.outputs().keys():
                results[termname] = []
                if args["dataIn"] is not None:
                    for data in args["dataIn"]:
                        if data == termname:
                            results[termname].append(data)
                        else:
                            results[termname].append(None)
            # return results

        # elif list(self.outputs().keys())[0] == 'dataOut' and len(list(self.inputs().keys())) > 0:
        elif list(self.outputs().keys())[0] == "dataOut":
            if debug:
                logging.getLogger("Lamia").debug("dataOut type")
            results["dataOut"] = []
            datainput = {}
            # print('***datain', dataIn)
            leninput = None
            for termname in self.inputs().keys():
                if args[termname] is not None:
                    leninput = len(args[termname])
                    datainput[termname] = args[termname]

            if leninput is not None:
                for i in range(leninput):
                    tempres = None
                    for termname in datainput.keys():
                        if datainput[termname][i] is not None:
                            # tempres = datainput[termname][i]
                            tempres = termname
                            break
                    results["dataOut"].append(tempres)

        if debug:
            logging.getLogger("Lamia").debug("Results : %s", str(results))
        return results

    def setLayers(self, currentlayer):
        self.currentlayer = currentlayer

    def setDbase(self, dbase):
        self.dbase = dbase


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        # self.setupUi(self)
        uipath = os.path.join(os.path.dirname(__file__), "lamia_tool_import_ui.ui")
        uic.loadUi(uipath, self)
