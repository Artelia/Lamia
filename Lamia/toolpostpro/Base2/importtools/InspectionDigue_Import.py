# -*- coding: utf-8 -*-
#unicode behaviour
from __future__ import unicode_literals

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



# from PyQt4 import uic, QtGui
from qgis.PyQt import uic, QtCore, QtGui
try:
    from qgis.PyQt.QtGui import QDialog
except:
    from qgis.PyQt.QtWidgets import QDialog
    
import os

#FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'InspectionDigue_Connexion_PG.ui'))

#class ConnexionPGDialog(QDialog, FORM_CLASS):
class ImportObjetDialog(QDialog):

    def __init__(self, parent=None):
        """Constructor."""
        super(ImportObjetDialog, self).__init__(parent)
        #self.setupUi(self)
        path = os.path.join(os.path.dirname(__file__), 'InspectionDigue_import.ui')
        uic.loadUi(path, self)

        """
        self.adresse = None
        self.port = None
        self.name = None
        self.user = None
        self.password = None

        self.lineEdit_adresse.setText('localhost')
        self.lineEdit_port.setText('5432')
        self.lineEdit_nom.setText('PVR_test')
        self.lineEdit_schema.setText('digue')
        self.lineEdit_user.setText('postgres')
        self.lineEdit_password.setText('PVR')
        """
        self.finished.connect(self.dialogIsFinished)
    """
    def setXandY(self,xtranslate = 0, ytranslate = 0):
        self.xtranslate = xtranslate
        self.ytranslate = ytranslate
        self.doubleSpinBox_x.setValue(self.xtranslate)
        self.doubleSpinBox_y.setValue(self.ytranslate)
    """
        
    def dialogIsFinished(self):
        """
        return level list
        return color array like this : [stop in 0 < stop > 1 ,r,g,b]
        """
        if (self.result() == 1):
            return self.tableWidget
        else:
            return None
            
            