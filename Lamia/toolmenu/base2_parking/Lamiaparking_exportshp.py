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
import shutil

#from .tools.Lamia_exportshpdialog import ExportShapefileDialog
from ..base2.Lamiabase_exportshp import exportShapefileBaseWorker


#class exportShapefileWorker(AbstractWorker):


class exportShapefileParkingWorker(exportShapefileBaseWorker):


    def __init__(self, dbase=None, windowdialog=None, reporttype=None, pdffile=None):
        # AbstractWorker.__init__(self)

        super(exportShapefileParkingWorker, self).__init__(dbase, windowdialog, reporttype, pdffile)


    def postInit(self):
        self.createfilesdir = os.path.join(os.path.dirname(__file__), 'exporttools')
        for filename in glob.glob(os.path.join(self.createfilesdir, '*.txt')):
            basename = os.path.basename(filename).split('.')[0]
            if basename != 'README':
                self.exportshapefiledialog.comboBox_type.addItems([basename])


