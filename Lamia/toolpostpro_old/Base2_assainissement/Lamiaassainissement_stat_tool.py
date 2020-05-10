# -*- coding: utf-8 -*-
import qgis
from qgis.PyQt import uic, QtGui, QtCore
try:
    from qgis.PyQt.QtGui import (QWidget, QLabel, QFrame, QTreeWidgetItem, QHeaderView)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget, QLabel, QFrame, QTreeWidgetItem, QHeaderView)

# from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
import os
import io
import glob

from ..Base2.lamia_stat_tool import StatTool

# ********************************************************************************************************************
# ********************************* Main Widget                *******************************************************
# ********************************************************************************************************************

class AssainissementStatTool(StatTool):

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(AssainissementStatTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil,parentwidget, parent=parent)


