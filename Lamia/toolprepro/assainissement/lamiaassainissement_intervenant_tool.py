# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore

try:
    from qgis.PyQt.QtGui import (QWidget, QInputDialog)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget, QInputDialog)
# from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..abstract.lamia_intervenant_tool import AbstractIntervenantTool
import os
import datetime



class IntervenantTool(AbstractIntervenantTool):

    LOADFIRST = False
    dbasetablename = 'Intervenant'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(IntervenantTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil,parentwidget, parent=parent)
