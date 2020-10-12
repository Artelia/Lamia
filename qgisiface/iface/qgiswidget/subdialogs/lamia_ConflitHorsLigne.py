from __future__ import unicode_literals
# -*- coding: utf-8 -*-
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




#unicode behaviour

# from PyQt4 import uic, QtGui
from qgis.PyQt import uic, QtCore, QtGui
try:
    from qgis.PyQt.QtGui import QDialog
except:
    from qgis.PyQt.QtWidgets import QDialog

import os

#FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'InspectionDigue_Connexion_PG.ui'))

#class ConflitHorsLigne(QDialog, FORM_CLASS):
class ConflitHorsLigne(QDialog):

    def __init__(self,  local, original, parent=None,):
        """Constructor."""
        super(ConflitHorsLigne, self).__init__(parent)
        #self.setupUi(self)
        path = os.path.join(os.path.dirname(__file__), 'lamia_ConflitHorsLigne.ui')
        uic.loadUi(path, self)



        self.label_label_3.setText(local)
        self.label_label_6.setText(original)



        self.finished.connect(self.dialogIsFinished)


    def dialogIsFinished(self):
        return self.result() == 1
