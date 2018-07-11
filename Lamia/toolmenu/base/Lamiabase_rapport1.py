# -*- coding: utf-8 -*-

import qgis
import os
#from ..toolabstract.inspectiondigue_abstractworker import AbstractWorker
from qgis.PyQt import QtGui, uic, QtCore, QtXml
from collections import OrderedDict
import datetime
import decimal

from .rapporttools.InspectionDigue_impression_rapport import ImpressionRapportDialog


try:
    from qgis.PyQt.QtGui import (QInputDialog,QTableWidgetItem,QComboBox)
except ImportError:
    from qgis.PyQt.QtWidgets import (QInputDialog,QTableWidgetItem,QComboBox)


class rapportWorker(object):

    #def __init__(self, dbase, importtable, results):
    def __init__(self, dbase=None, windowdialog=None):
        #AbstractWorker.__init__(self)
        self.dbase = dbase
        #self.importtable = importtable
        #self.results = results
        self.windowdialog = windowdialog

        self.printrapportdialog = ImpressionRapportDialog()

        lauchaction = QtGui.QAction(QtGui.QIcon(), 'Impression rapport',self.windowdialog.menuPreferences)
        lauchaction.triggered.connect(self.launchDialog)
        self.windowdialog.menuOutils.addAction(lauchaction)


        self.postInit()




    def postInit(self):
        pass


    def launchDialog(self):
        # def printRapport(self, reporttype=None, pdffile=None):
        if reporttype is None or pdffile is None:
            self.printrapportdialog.exec_()
            reporttype, pdffile = self.printrapportdialog.dialogIsFinished()
            # print(reporttype, pdffile)

        if reporttype is not None and pdffile is not None and pdffile != '':
            if False:
                self.worker = printPDFWorker(self.dbase, qgis.core.QgsProject.instance(), self.canvas, reporttype,
                                             pdffile, self)
                self.thread = QtCore.QThread()
                self.worker.moveToThread(self.thread)
                self.worker.finished.connect(self.exportPDFFinished)
                self.worker.error.connect(self.printError)
                self.worker.message.connect(self.printMessage)
                self.worker.finished.connect(self.exportPDFFinished)
                self.worker.finished.connect(self.worker.deleteLater)
                self.thread.finished.connect(self.thread.deleteLater)
                self.worker.finished.connect(self.thread.quit)

                self.thread.started.connect(self.worker.run)

                self.thread.start()
            if False:
                self.worker = printPDFWorker(self.dbase, qgis.core.QgsProject.instance(), self.canvas, reporttype,
                                             pdffile, self)
                self.worker.finished.connect(self.exportPDFFinished)
                self.worker.error.connect(self.printError)
                self.worker.message.connect(self.printMessage)
                self.worker.run()
            if True:
                self.worker = printPDFWorker(self.dbase, qgis.core.QgsProject.instance(), self.canvas, reporttype,
                                             pdffile, self)
                self.worker.work()







