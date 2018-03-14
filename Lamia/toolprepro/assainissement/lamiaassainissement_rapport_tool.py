# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore, QtGui
try:
    from qgis.PyQt.QtGui import (QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget)
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..abstract.lamia_rapport_tool import AbstractRapportTool
import os
import datetime




class RapportTool(AbstractRapportTool):

    LOADFIRST = False
    dbasetablename = 'Rapport'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None,gpsutil=None, parentwidget=None, parent=None):
        super(RapportTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil,parentwidget, parent=parent)
