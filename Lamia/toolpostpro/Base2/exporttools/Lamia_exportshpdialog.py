# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PostTelemac
                                 A QGIS plugin
 Post Traitment or Telemac
                              -------------------
        begin                : 2015-07-07
        git sha              : $Format:%H$
        copyright            : (C) 2015 by Artelia
        email                : patrice.Verchere@arteliagroup.com
 ***************************************************************************/
 
 ***************************************************************************/
 Implementation of QgsPluginLayer class, used to show selafin res
 
Versions :
Impl
0.0 : debut

 ***************************************************************************/
"""
#unicode behaviour
from __future__ import unicode_literals
# from PyQt4 import uic, QtGui
from qgis.PyQt import uic, QtCore, QtGui
try:
    from qgis.PyQt.QtGui import QDialog, QFileDialog
except:
    from qgis.PyQt.QtWidgets import QDialog, QFileDialog
    
import os

#FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'InspectionDigue_impression_rapport.ui'))

#class ConnexionPGDialog(QDialog, FORM_CLASS):
class ExportShapefileDialog(QDialog):

    def __init__(self, windowsdialog, parent=None):
        """Constructor."""
        super(ExportShapefileDialog, self).__init__(parent)
        #self.setupUi(self)
        path = os.path.join(os.path.dirname(__file__), 'Lamia_exportshpdialog.ui')
        uic.loadUi(path, self)

        #self.qfiledlg = QFileDialog()
        self.windowsdialog = windowsdialog
        self.qfiledlg = self.windowsdialog.qfiledlg

        self.comboBox_type.addItems(['Infralineaire',
                                     'Noeud',
                                     'Observations',
                                     'Dernieres observations',
                                     'Equipement','Photo',
                                     'Graphiques digue'])
        # self.comboBox_type.setCurrentIndex(2)
        self.lineEdit_nom.setText('c://testshapeile.shp')
        self.pushButton_filechoose.clicked.connect(self.chooseFile)
        self.finished.connect(self.dialogIsFinished)


    def chooseFile(self):
        reportfile = self.qfiledlg.getSaveFileName(self,
                                                   'InspectionDigue nouveau',
                                                   '',
                                                   'Shapefile (*.shp)')
        if reportfile:
            if isinstance(reportfile, tuple):    # qt5
                reportfile = reportfile[0]
            self.lineEdit_nom.setText(reportfile)

    def dialogIsFinished(self):
        if self.result() == 1:
            return self.comboBox_type.currentText(), self.lineEdit_nom.text()
        else:
            return None, None
