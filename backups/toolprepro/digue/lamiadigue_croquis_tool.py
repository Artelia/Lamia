# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore, QtGui

try:
    from qgis.PyQt.QtGui import (QWidget, QMainWindow, QSpinBox, QAction, QDialog, QLabel, QFrame)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget,QMainWindow, QSpinBox, QAction, QDialog, QLabel, QFrame)
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..abstract.lamia_croquis_tool import AbstractCroquisTool
import os
import qgis
import datetime


#FORM_CLASS3, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'FreeHandEditorToolUser.ui'))


class CroquisTool(AbstractCroquisTool):

    LOADFIRST = False
    dbasetablename = 'Photo'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None, parentwidget=None, parent=None):
        super(CroquisTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil, parentwidget, parent=parent)
