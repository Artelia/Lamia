# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtGui
try:
    from qgis.PyQt.QtGui import (QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget)
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..abstract.lamia_pointtopo_tool import AbstractPointtopoTool
import os
import qgis





class PointtopoTool(AbstractPointtopoTool):

    LOADFIRST = False
    dbasetablename = 'Pointtopo'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(PointtopoTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)
