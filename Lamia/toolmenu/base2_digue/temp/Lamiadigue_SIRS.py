# -*- coding: utf-8 -*-

import qgis
import os
# from ..toolabstract.inspectiondigue_abstractworker import AbstractWorker
from qgis.PyQt import QtGui, uic, QtCore, QtXml
from collections import OrderedDict
import datetime
import decimal
import numpy as np
import glob

try:
    from qgis.PyQt.QtGui import (QAction)
except ImportError:
    from qgis.PyQt.QtWidgets import (QAction)

from ...toolgeneral.SIRS_to_LAMIA.FDtL import *
from ...toolgeneral.LAMIA_to_SIRS.LtFD import *

#class exportShapefileWorker(AbstractWorker):


class lamiaSIRS(object):


    def __init__(self, dbase=None, windowdialog=None):
        self.windowdialog = windowdialog
        try:
            lauchaction1 = QAction(QtGui.QIcon(), 'Export vers SIRS Digues',self.windowdialog.menuPreferences)
            lauchaction1.triggered.connect(export_sirs)
            self.windowdialog.menuOutils.addAction(lauchaction1)
            
            lauchaction2 = QAction(QtGui.QIcon(), 'Importer depuis SIRS Digues',self.windowdialog.menuPreferences)
            lauchaction2.triggered.connect(import_sirs)
            self.windowdialog.menuOutils.addAction(lauchaction2)
        except  Exception as e:
            print(e)



