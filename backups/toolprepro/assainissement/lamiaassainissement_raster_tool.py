# -*- coding: utf-8 -*-
import qgis
from qgis.PyQt import uic, QtCore
try:
    from qgis.PyQt.QtGui import (QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget)
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..abstract.lamia_raster_tool import AbstractRasterTool
import os
import datetime



class RasterTool(AbstractRasterTool):

    LOADFIRST = True
    dbasetablename = 'Rasters'
    
    def __init__(self, dbase, dialog=None, linkedtreewidget=None,gpsutil=None, parentwidget=None, parent=None):
        super(RasterTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil,parentwidget, parent=parent)
