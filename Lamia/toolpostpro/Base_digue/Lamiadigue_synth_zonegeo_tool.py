# -*- coding: utf-8 -*-
import qgis
from qgis.PyQt import uic, QtGui, QtCore
try:
    from qgis.PyQt.QtGui import (QWidget, QLabel, QFrame, QTreeWidgetItem, QHeaderView,QComboBox)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget, QLabel, QFrame, QTreeWidgetItem, QHeaderView,QComboBox)

from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
import os
if False:
    from ..toolprepro.InspectionDigue_photos_tool import PhotosTool
    from ..toolprepro.InspectionDigue_observation_tool import ObservationTool
    from ..toolabstract.inspectiondigue_abstractworker import AbstractWorker
if True:
    from ...toolprepro.base.lamiabase_photo_tool  import BasePhotoTool
    from ...toolprepro.base.lamiabase_observation_tool import BaseObservationTool
    #from ...toolabstract.inspectiondigue_abstractworker import AbstractWorker
import io
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from ..Base.Lamia_synth_zonegeo_tool import SyntheseZonegeoTool


# ********************************************************************************************************************
# ********************************* Main Widget                *******************************************************
# ********************************************************************************************************************

class SyntheseDigueZonegeoTool(SyntheseZonegeoTool):

    DBASES = ['base_digue']

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(SyntheseDigueZonegeoTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil,parentwidget, parent=parent)

 