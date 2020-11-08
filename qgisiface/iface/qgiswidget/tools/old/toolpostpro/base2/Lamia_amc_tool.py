# -*- coding: utf-8 -*-

import qgis
import qgis.core
import os
import re
import logging
# from ..toolabstract.inspectiondigue_abstractworker import AbstractWorker
from qgis.PyQt import QtGui, uic, QtCore, QtXml
try:
    from qgis.PyQt.QtGui import QPrinter
    from qgis.PyQt.QtGui import (QProgressBar, QApplication,QAction, QWidget, QAbstractItemView, QTableWidgetItem,
                                 QHeaderView, QToolButton, QMessageBox)
    #except ImportError:
except ImportError as e:
    from qgis.PyQt.QtPrintSupport import QPrinter
    from qgis.PyQt.QtWidgets import (QProgressBar, QApplication,QAction, QWidget, QAbstractItemView, QTableWidgetItem,
                                      QHeaderView, QToolButton, QMessageBox)
# from ...libs import pyqtgraph as pg
import networkx
import numpy as np
from collections import OrderedDict
import glob, sys, logging, inspect

from ...Lamia_abstract_tool import AbstractLamiaTool
from .amctools.amcwindow import AMCWindow
from ...lamiautils.abstractfilemanager import AbstractFileManager

import pandas as pd

#test gitignore
#test gitignore


class AmcTool(AbstractLamiaTool):
    TOOLNAME = 'amctools'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None, parentwidget=None, parent=None):
        super(AmcTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil, parentwidget, parent=parent)
        self.amcwindow = None


    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Postpro'
        self.NAME = 'AMC'
        #self.dbasetablename = 'Zonegeo'
        self.visualmode = [4]
        # self.PointENABLED = True
        # self.LineENABLED = True
        # self.PolygonEnabled = True
        # self.magicfunctionENABLED = True
        # self.linkagespec = None
        # self.pickTable = None
        # print(self.dbase.recentsdbase)
        self.multipleselection = True

        self.iconpath = os.path.join(os.path.dirname(__file__), 'Lamia_rapport_tool_icon.png')
        self.qtreewidgetfields = ['libelle']

        # ****************************************************************************************
        # properties ui
        self.groupBox_geom.setParent(None)
        self.groupBox_elements.setParent(None)

        self.filemanager = AMCFileManager(self.windowdialog, self, '.json')


        """ SUPPRIME 20190812 JRO
        currentJson = self.userwdgfield.comboBox_typeamc.currentText()
        self.amcwindow = AMCWindow(dbase=self.dbase, json=currentJson)
        self.amcwindow.setWindowModality(QtCore.Qt.ApplicationModal)"""

    def initFieldUI(self):
        if self.userwdgfield is None:

            # ****************************************************************************************
            # userui

            self.userwdgfield = UserUI()
            # self.userwdgfield.toolButton_editamc.clicked.connect(self.editAMC)
            self.userwdgfield.pushButton_calcul.clicked.connect(self.launchCalcul)

            self.userwdgfield.groupBox_filemanager.layout().addWidget(self.filemanager)
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

            files = self.listFiles(self.dbase.dbaseressourcesdirectory + "/config/amcTools")
            self.userwdgfield.comboBox_typeamc.addItems(files)

            print("| Exit {fct}".format(fct=inspect.stack()[0][3]))

    def listFiles(self, myPath):
        """
        Fetches all files within a specified directory
        :param myPath: str, path within which files should be saved
        :return: list, files within path
        """

        return [f for f in os.listdir(myPath) if os.path.isfile(os.path.join(myPath, f))]

    # ---------- FILE MANAGEMENT ----------

    def postOnActivation(self):
        self.filemanager.reset()


    def postInitFeatureProperties(self, feat):
        pass

    def editAMC(self):
        # currentJson = self.userwdgfield.comboBox_typeamc.currentText()
        currentJsonPath = self.filemanager.getCurrentPath()

        #self.amcwindow = AMCWindow(dbase=self.dbase, jsonpath=currentJson)
        self.amcwindow = AMCWindow(dbase=self.dbase, jsonpath=currentJsonPath)

        if self.dbase.qgsiface is not None:
            self.amcwindow.setWindowModality(QtCore.Qt.NonModal)
            self.amcwindow.show()
        else:
            self.amcwindow.exec_()



    def launchCalcul(self):
        # currentJson = self.userwdgfield.comboBox_typeamc.currentText()
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
        self.userwdgfield.twResult.setRowCount(0)
        header = self.userwdgfield.twResult.horizontalHeader()

        # Columns and rows names
        rowNr = len(df.values)

        # Set column's number to len(colNames) + 1 (ID) and row's number to len(rowNames)
        self.userwdgfield.twResult.setColumnCount(1)
        self.userwdgfield.twResult.setRowCount(rowNr)

        # Fill tableWidget with elements from self.dataFrame
        for row in range(rowNr):
            valueTmp = df[row]
            # Insert value
            self.userwdgfield.twResult.setItem(row, 0, QTableWidgetItem(str(valueTmp)))
            # Resize column
            header.setSectionResizeMode(0, QHeaderView.Stretch)


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        # self.setupUi(self)
        uipath = os.path.join(os.path.dirname(__file__), 'Lamia_amc_tool.ui')
        uic.loadUi(uipath, self)


class AMCFileManager(AbstractFileManager):

    def __init__(self, mainwindows=None, parentwdg=None, fileext=None):
        super(AMCFileManager, self).__init__(mainwindows, parentwdg, fileext)

    def new(self):

        if not os.path.exists(self.confdataproject):
            os.mkdir(self.confdataproject)

        if sys.version_info.major == 2:
            confpath, confext = self.qfiledialog.getSaveFileName(None, 'Choose the file', self.confdataproject,
                                                                 'json (*.json)', '')
        elif sys.version_info.major == 3:
            confpath, confext = self.qfiledialog.getSaveFileName(None, 'Choose the file', self.confdataproject,
                                                                 'json (*.json)', '')

        if confpath:
            conf_file = open(confpath, 'w', encoding="utf-8")
            conf_file.close()

            self.reset()
            txttofind = self.projectcharacter + os.path.splitext(os.path.basename(confpath))[0]
            indexcombo = self.comboBox_files.findText(txttofind)
            self.comboBox_files.setCurrentIndex(indexcombo)