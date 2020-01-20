# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import qgis
import sys
from qgis.PyQt import uic, QtGui, QtCore
try:
    from qgis.PyQt.QtGui import (QWidget, QLabel, QFrame, QTreeWidgetItem, QHeaderView)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget, QLabel, QFrame, QTreeWidgetItem, QHeaderView)

# from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
import os
import io
import glob

from ..Base2.Lamia_rapport_tool import RapportTool
from ..Base2.Lamia_rapport_tool import printPDFBaseWorker

# ********************************************************************************************************************
# ********************************* Main Widget                *******************************************************
# ********************************************************************************************************************

class ChantierRapportTool(RapportTool):

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(ChantierRapportTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil,parentwidget, parent=parent)




class printPDFBaseWorker(printPDFBaseWorker):


    def __init__(self, dbase, windowdialog=None, parentprintPDFworker=None, confData=None, pdffile=None, reporttype=None,templatedir=None, idlist=None):
        super(printPDFBaseWorker, self).__init__(dbase=dbase,
                                                 windowdialog=windowdialog,
                                                 parentprintPDFworker=parentprintPDFworker,
                                                 confData=confData,
                                                 pdffile=pdffile,
                                                 reporttype=reporttype,
                                                 templatedir=templatedir,
                                                 idlist=idlist)

