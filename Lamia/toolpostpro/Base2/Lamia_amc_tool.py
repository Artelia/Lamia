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
    from qgis.PyQt.QtGui import (QProgressBar, QApplication,QAction, QWidget, QAbstractItemView)
    #except ImportError:
except ImportError as e:
    from qgis.PyQt.QtPrintSupport import QPrinter
    from qgis.PyQt.QtWidgets import  (QProgressBar, QApplication,QAction, QWidget, QAbstractItemView)
# from ...libs import pyqtgraph as pg
import networkx
import numpy as np
from collections import OrderedDict
import glob, sys, logging, inspect

from ...toolabstract.Lamia_abstract_tool import AbstractLamiaTool
from .amctools.amcwindow import AMCWindow

#test gitignore



class AmcTool(AbstractLamiaTool):
    TOOLNAME = 'amctools'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None, parentwidget=None, parent=None):
        super(AmcTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil, parentwidget, parent=parent)

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

        self.amcwindow = AMCWindow(dbase=self.dbase)
        self.amcwindow.setWindowModality(QtCore.Qt.ApplicationModal)



    def initFieldUI(self):
        if self.userwdgfield is None:

            # ****************************************************************************************
            # userui

            self.userwdgfield = UserUI()
            self.userwdgfield.toolButton_editamc.clicked.connect(self.editAMC)
            self.userwdgfield.pushButton_calcul.clicked.connect(self.launchCalcul)







    def postOnActivation(self):
        pass

    def postInitFeatureProperties(self, feat):
        pass




    def editAMC(self):
        self.amcwindow.show()



    def launchCalcul(self):
        print('calcul')





class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        # self.setupUi(self)
        uipath = os.path.join(os.path.dirname(__file__), 'Lamia_amc_tool.ui')
        uic.loadUi(uipath, self)


