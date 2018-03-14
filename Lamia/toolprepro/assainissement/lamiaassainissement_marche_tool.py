# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore

try:
    from qgis.PyQt.QtGui import (QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget)


#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..abstract.lamia_marche_tool import AbstractMarcheTool

# from .lamiadigue_rapport_tool import RapportTool
# from .lamiadigue_photos_tool import PhotosTool
# from .lamiadigue_topographie_tool import TopographieTool
# from .lamiadigue_ressource_tool import RessourceTool



import os
import datetime



class MarcheTool(AbstractMarcheTool):

    LOADFIRST = False
    dbasetablename = 'Marche'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(MarcheTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)
