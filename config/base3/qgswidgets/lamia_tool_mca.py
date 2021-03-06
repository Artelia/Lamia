# -*- coding: utf-8 -*-

import qgis
import qgis.core
import os
import re
import logging

# from ..toolabstract.inspectiondigue_abstractworker import AbstractWorker
from qgis.PyQt import QtGui, uic, QtCore, QtXml

from qgis.PyQt.QtPrintSupport import QPrinter
from qgis.PyQt.QtWidgets import (
    QProgressBar,
    QApplication,
    QAction,
    QWidget,
    QAbstractItemView,
    QTableWidgetItem,
    QHeaderView,
    QToolButton,
    QMessageBox,
)

# from ...libs import pyqtgraph as pg
import networkx
import numpy as np
from collections import OrderedDict
import glob, sys, logging, inspect

from Lamia.qgisiface.iface.qgiswidget.tools.lamia_abstracttool import AbstractLamiaTool
from .mcawidgets.amcwindow import AMCWindow
from Lamia.qgisiface.iface.qgiswidget.tools.general_subwidgets.abstractfilemanager import (
    AbstractFileManager,
)
from Lamia.api.libslamia.lamiamca.lamiamca import McaCore


class McaTool(AbstractLamiaTool):

    POSTPROTOOLNAME = "lamiamca"

    tooltreewidgetCAT = QtCore.QCoreApplication.translate("base3", "Analytics")
    tooltreewidgetSUBCAT = QtCore.QCoreApplication.translate("base3", "MCA")

    def __init__(self, **kwargs):
        super(McaTool, self).__init__(**kwargs)
        self.mcacore = McaCore(
            dbaseparser=self.dbase,
            messageinstance=self.mainifacewidget.connector,
            qgiscanvas=self.mainifacewidget.qgiscanvas,
        )
        self.filemanager = AMCFileManager(self.mainifacewidget, self.mcacore)
        self.amcwindow = None

    # def __init__(
    #     self,
    #     dbase,
    #     dialog=None,
    #     linkedtreewidget=None,
    #     gpsutil=None,
    #     parentwidget=None,
    #     parent=None,
    # ):
    #     super(McaTool, self).__init__(
    #         dbase, dialog, linkedtreewidget, gpsutil, parentwidget, parent=parent
    #     )
    #     self.amcwindow = None

    """
    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = "Postpro"
        self.NAME = "AMC"
        # self.dbasetablename = 'Zonegeo'
        self.visualmode = [4]
        # self.PointENABLED = True
        # self.LineENABLED = True
        # self.PolygonEnabled = True
        # self.magicfunctionENABLED = True
        # self.linkagespec = None
        # self.pickTable = None
        # print(self.dbase.recentsdbase)
        self.multipleselection = True

        self.iconpath = os.path.join(
            os.path.dirname(__file__), "Lamia_rapport_tool_icon.png"
        )
        self.qtreewidgetfields = ["libelle"]

        # ****************************************************************************************
        # properties ui
        self.groupBox_geom.setParent(None)
        self.groupBox_elements.setParent(None)

        self.filemanager = AMCFileManager(self.windowdialog, self, ".json")

        #  SUPPRIME 20190812 JRO
        # currentJson = self.toolwidgetmain.comboBox_typeamc.currentText()
        # self.amcwindow = AMCWindow(dbase=self.dbase, json=currentJson)
        # self.amcwindow.setWindowModality(QtCore.Qt.ApplicationModal)

        """

    # def initFieldUI(self):
    def initMainToolWidget(self):
        self.toolwidgetmain = UserUI()
        # self.toolwidgetmain.toolButton_editamc.clicked.connect(self.editAMC)
        self.toolwidgetmain.pushButton_calcul.clicked.connect(self.launchCalcul)

        self.toolwidgetmain.groupBox_filemanager.layout().addWidget(self.filemanager)
        try:
            self.filemanager.toolButton_edit.clicked.disconnect()
        except:
            pass
        self.filemanager.toolButton_edit.clicked.connect(self.editAMC)

        # Load JSON files to comboBox
        # self.loadFiles()

    if False:

        def loadFiles(self):
            """
            Add all JSON to comboBox
            """
            print("| Enter {fct}".format(fct=inspect.stack()[0][3]))

            files = self.listFiles(
                self.dbase.dbaseressourcesdirectory + "/config/amcTools"
            )
            self.toolwidgetmain.comboBox_typeamc.addItems(files)

            print("| Exit {fct}".format(fct=inspect.stack()[0][3]))

        def listFiles(self, myPath):
            """
            Fetches all files within a specified directory
            :param myPath: str, path within which files should be saved
            :return: list, files within path
            """

            return [
                f for f in os.listdir(myPath) if os.path.isfile(os.path.join(myPath, f))
            ]

    # ---------- FILE MANAGEMENT ----------

    # def postOnActivation(self):
    #     self.filemanager.reset()

    def postToolTreeWidgetCurrentItemChanged(self):
        self.filemanager.reset()

    def postInitFeatureProperties(self, feat):
        pass

    def editAMC(self):
        # currentJson = self.toolwidgetmain.comboBox_typeamc.currentText()
        # currentJsonPath = self.filemanager.getCurrentPath()
        # tabletypepath = self.filemanager.getCurrentText()

        # currentJsonPath = self.mcacore.getConfFilePath(
        #     self.filemanager.getCurrentText()
        # )
        tabletypepath = self.filemanager.getCurrentText()

        # self.amcwindow = AMCWindow(dbase=self.dbase, jsonpath=currentJson)
        self.amcwindow = AMCWindow(
            dbase=self.dbase,
            confname=tabletypepath,
            mcacore=self.mcacore,
            qgiscanvas=self.mainifacewidget.qgiscanvas,
        )

        if qgis.utils.iface is not None:
            self.amcwindow.setWindowModality(QtCore.Qt.NonModal)
            self.amcwindow.show()
        else:
            self.amcwindow.exec_()

    def launchCalcul(self):
        # currentJson = self.toolwidgetmain.comboBox_typeamc.currentText()
        currentJsonPath = self.filemanager.getCurrentPath()
        self.amcwindow = AMCWindow(dbase=self.dbase, jsonpath=currentJsonPath)
        self.amcwindow.createdataframe.finished.connect(self.showCalculResults)
        self.amcwindow.createDataFrame()

    def showCalculResults(self):
        try:
            self.amcwindow.createdataframe.finished.disconnect(self.showCalculResults)
        except:
            pass
        self.amcwindow.visualisationPressed()
        self.dataFrameToTableWidget(self.amcwindow.result)

    def dataFrameToTableWidget(self, df):
        """
        Update self.twResult from df
        """

        # Reset table widget
        self.toolwidgetmain.twResult.setRowCount(0)
        header = self.toolwidgetmain.twResult.horizontalHeader()

        # Columns and rows names
        rowNr = len(df.values)

        # Set column's number to len(colNames) + 1 (ID) and row's number to len(rowNames)
        self.toolwidgetmain.twResult.setColumnCount(1)
        self.toolwidgetmain.twResult.setRowCount(rowNr)

        # Fill tableWidget with elements from self.dataFrame
        for row in range(rowNr):
            valueTmp = df[row]
            # Insert value
            self.toolwidgetmain.twResult.setItem(
                row, 0, QTableWidgetItem(str(valueTmp))
            )
            # Resize column
            header.setSectionResizeMode(0, QHeaderView.Stretch)


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        # self.setupUi(self)
        uipath = os.path.join(os.path.dirname(__file__), "lamia_tool_mca_ui.ui")
        uic.loadUi(uipath, self)


class AMCFileManager(AbstractFileManager):
    def __init__(self, mainwindows=None, toolclass=None):
        super(AMCFileManager, self).__init__(mainwindows, toolclass)

    def new(self):

        confpath, confext = self.qfiledialog.getSaveFileName(
            None,
            "Choose the file",
            self.toolclass.confdatadirproject,
            "json (*.json)",
            "",
        )

        if confpath:
            self.toolclass.new(confpath)
            self.reset()
            txttofind = (
                self.toolclass.projectcharacter
                + os.path.splitext(os.path.basename(confpath))[0]
            )
            indexcombo = self.comboBox_files.findText(txttofind)
            self.comboBox_files.setCurrentIndex(indexcombo)

