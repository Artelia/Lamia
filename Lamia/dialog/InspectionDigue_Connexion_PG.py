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
    from qgis.PyQt.QtGui import QDialog
except:
    from qgis.PyQt.QtWidgets import QDialog

import os

#FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'InspectionDigue_Connexion_PG.ui'))

#class ConnexionPGDialog(QDialog, FORM_CLASS):
class ConnexionPGDialog(QDialog):

    def __init__(self, parent=None):
        """Constructor."""
        super(ConnexionPGDialog, self).__init__(parent)
        #self.setupUi(self)
        path = os.path.join(os.path.dirname(__file__), 'InspectionDigue_Connexion_PG.ui')
        uic.loadUi(path, self)


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
            return (self.lineEdit_adresse.text(),
                    int(self.lineEdit_port.text() ),
                    self.lineEdit_nom.text(),
                    self.lineEdit_schema.text(),
                    self.lineEdit_user.text(),
                    self.lineEdit_password.text())
        else:
            return (None,None,None,None,None,None)

