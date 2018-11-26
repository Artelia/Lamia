# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore, QtGui

try:
    from qgis.PyQt.QtGui import (QWidget, QMainWindow, QSpinBox, QAction, QDialog, QFrame)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget,QMainWindow, QSpinBox, QAction, QDialog, QFrame)
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..base2.lamiabase_croquis_tool import BaseCroquisTool
import os
import qgis
import datetime
#from .lamiabase_photoviewer import PhotoViewer


# FORM_CLASS3, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'FreeHandEditorToolUser.ui'))


class BaseParkingCroquisTool(BaseCroquisTool):

    LOADFIRST = False
    dbasetablename = 'Photo'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None, parentwidget=None, parent=None):
        super(BaseParkingCroquisTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil, parentwidget, parent=parent)
