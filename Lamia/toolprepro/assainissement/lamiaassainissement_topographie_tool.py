# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore

try:
    from qgis.PyQt.QtGui import (QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget)
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..abstract.lamia_topographie_tool import AbstractTopographieTool
import os
import datetime

from .lamiadigue_pointtopo_tool import PointtopoTool

"""
ne permettre de la renseigner qu en etant une classe fille de leve topo - sinon pas de datecreation
ca fout la merde....

"""


class TopographieTool(AbstractTopographieTool):

    LOADFIRST = True
    dbasetablename = 'Topographie'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None,gpsutil=None, parentwidget=None, parent=None):
        super(TopographieTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil,parentwidget, parent=parent)
