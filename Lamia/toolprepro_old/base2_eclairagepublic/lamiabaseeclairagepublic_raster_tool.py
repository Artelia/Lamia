# -*- coding: utf-8 -*-
import qgis
from qgis.PyQt import uic, QtCore
try:
    from qgis.PyQt.QtGui import (QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget)
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..base2.lamiabase_raster_tool import BaseRasterTool
import os
import datetime



class BaseEaupotableRasterTool(BaseRasterTool):

    LOADFIRST = True
    dbasetablename = 'Rasters'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None,gpsutil=None, parentwidget=None, parent=None):
        super(BaseEaupotableRasterTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil,parentwidget, parent=parent)
