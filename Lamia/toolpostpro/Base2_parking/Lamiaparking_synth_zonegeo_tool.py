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
# from ...libs import pyqtgraph as pg
# from ...libs.pyqtgraph import exporters

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import networkx
import numpy as np
import shutil

from ..Base2.Lamia_synth_zonegeo_tool import SyntheseZonegeoTool

# ********************************************************************************************************************
# ********************************* Main Widget                *******************************************************
# ********************************************************************************************************************

class ParkingSyntheseZonegeoTool(SyntheseZonegeoTool):

    DBASES = ['digue','base_digue','base2_digue', 'base2_parking']

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(ParkingSyntheseZonegeoTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil,parentwidget, parent=parent)


    def initFieldUI(self):
        super(ParkingSyntheseZonegeoTool, self).initFieldUI()
        self.userwdgfield.tabWidget.removeTab(1)
        
