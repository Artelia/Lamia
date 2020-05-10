# -*- coding: utf-8 -*-

try:
    from qgis.PyQt.QtGui import (QWidget, QMainWindow, QSpinBox, QAction, QDialog, QFrame)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget,QMainWindow, QSpinBox, QAction, QDialog, QFrame)

from ..base2.lamiabase_croquis_tool import BaseCroquisTool


class BaseEclairagePublicCroquisTool(BaseCroquisTool):

    LOADFIRST = False
    dbasetablename = 'Photo'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None, parentwidget=None, parent=None):
        super(BaseEclairagePublicCroquisTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil, parentwidget, parent=parent)
