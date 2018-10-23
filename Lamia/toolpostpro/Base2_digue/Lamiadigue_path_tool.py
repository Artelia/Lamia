# -*- coding: utf-8 -*-
import qgis
from qgis.PyQt import uic, QtGui, QtCore
try:
    from qgis.PyQt.QtGui import (QWidget, QLabel, QFrame, QTreeWidgetItem, QHeaderView)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget, QLabel, QFrame, QTreeWidgetItem, QHeaderView)

from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
import os
import io
from ...libs import pyqtgraph as pg
from ...libs.pyqtgraph import exporters

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import networkx
import numpy as np
import shutil

from ..Base.Lamia_path_tool import PathTool

# ********************************************************************************************************************
# ********************************* Main Widget                *******************************************************
# ********************************************************************************************************************

class DiguePathTool(PathTool):

    DBASES = ['digue','base_digue','base2_digue']

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(DiguePathTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil,parentwidget, parent=parent)

        
