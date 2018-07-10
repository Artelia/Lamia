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

#from .tools.Lamia_exportshpdialog import ExportShapefileDialog
#from ..base.Lamiabase_import import importShapefileBaseWorker
from ..base.Lamiabase_exportshp import exportShapefileBaseWorker

#class exportShapefileWorker(AbstractWorker):


class exportShapefileAssainissementWorker(exportShapefileBaseWorker):


    def __init__(self, dbase=None, windowdialog=None, reporttype=None, pdffile=None):
        # AbstractWorker.__init__(self)

        super(exportShapefileAssainissementWorker, self).__init__(dbase, windowdialog, reporttype, pdffile)


    def postInit(self):
        createfilesdir = os.path.join(os.path.dirname(__file__), 'exporttools')
        for filename in glob.glob(os.path.join(createfilesdir, '*.txt')):
            basename = os.path.basename(filename).split('.')[0]
            self.exportshapefiledialog.comboBox_type.addItems([basename])




