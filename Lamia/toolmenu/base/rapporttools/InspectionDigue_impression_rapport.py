"""
This file is part of LAMIA.

    LAMIA is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    LAMIA is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Foobar.  If not, see <https://www.gnu.org/licenses/>.

"""
"""
  * Copyright (c) 2017-2020 ARTELIA Commit <lamia@arteliagroup.com>
  * 
  * SPDX-License-Identifier: GPL-3.0-or-later
  * License-Filename: LICENSING.md
 """


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
class ImpressionRapportDialog(QDialog):

    def __init__(self, windowsdialog, parent=None):
        """Constructor."""
        super(ImpressionRapportDialog, self).__init__(parent)
        #self.setupUi(self)
        path = os.path.join(os.path.dirname(__file__), 'InspectionDigue_impression_rapport.ui')
        uic.loadUi(path, self)

        self.windowsdialog = windowsdialog
        #self.qfiledlg = self.windowsdialog.QFileDialog()
        self.qfiledlg =  self.windowsdialog.qfiledlg
        #self.comboBox_type.addItems(['Infrastructure lineaire','Equipements hydrauliques','Desordres'])
        self.pushButton_filechoose.clicked.connect(self.chooseFile)
        self.finished.connect(self.dialogIsFinished)


    def chooseFile(self):
        reportfile = self.qfiledlg.getSaveFileName(self,
                                                   'InspectionDigue nouveau',
                                                   '',
                                                   'PDF (*.pdf)')
        if reportfile:
            if isinstance(reportfile, tuple):    # qt5
                reportfile = reportfile[0]
            self.lineEdit_nom.setText(reportfile)

    def dialogIsFinished(self):
        if self.result() == 1:
            return self.comboBox_type.currentText(), self.lineEdit_nom.text()
        else:
            return None, None
