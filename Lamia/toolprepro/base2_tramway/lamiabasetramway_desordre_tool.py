# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore

try:
    from qgis.PyQt.QtGui import (QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget)



from ..base2.lamiabase_desordre_tool import BaseDesordreTool
#from .lamiabaseparking_observation_tool import BaseParkingObservationTool


import os
import datetime
import qgis




class BaseTramwayDesordreTool(BaseDesordreTool):

    #LOADFIRST = True
    dbasetablename = 'Desordre'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None, parentwidget=None, parent=None):
        super(BaseTramwayDesordreTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)
