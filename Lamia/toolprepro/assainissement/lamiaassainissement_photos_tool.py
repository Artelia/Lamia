# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore, QtGui
try:
    from qgis.PyQt.QtGui import (QWidget, QLabel, QFrame)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget, QLabel, QFrame)

#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..abstract.lamia_photos_tool import AbstractPhotosTool
import os
import datetime
import glob

#FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), '..', 'dialog', 'InspectionDigue_propertieswidget.ui'))



class PhotosTool(AbstractPhotosTool):

    LOADFIRST = False
    dbasetablename = 'Photo'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None,gpsutil=None, parentwidget=None, parent=None):
        super(PhotosTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)
