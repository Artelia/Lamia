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
    from qgis.PyQt.QtGui import QDialog, QPushButton
except:
    from qgis.PyQt.QtWidgets import QDialog, QPushButton

import os

class NumPadDialog(QDialog):

    def __init__(self, parent=None):
        super(NumPadDialog, self).__init__(parent)
        path = os.path.join(os.path.dirname(__file__), 'lamia_numpad.ui')
        uic.loadUi(path, self)
        self.finished.connect(self.dialogIsFinished)
        for wdg in self.children():
            if isinstance(wdg, QPushButton):
                wdg.clicked.connect(self.buttonClicked)
        self.textresult = ''

    def buttonClicked(self):
        wdgsource = self.sender()

        if wdgsource.text().isdigit() or wdgsource.text() in ['.','-']:

            if ( self.isfloat(self.lineEdit.text() + wdgsource.text())
                    or ( len(self.lineEdit.text()) == 0 and wdgsource.text() == '-' ) ):
                self.lineEdit.insert(wdgsource.text())
        elif wdgsource.text() == 'Del':
            self.lineEdit.setText(self.lineEdit.text()[0:-1])
        elif wdgsource.text() == 'Clear':
            self.lineEdit.clear()

        self.textresult = self.lineEdit.text()


    def isfloat(self,value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def dialogIsFinished(self):

        if self.result() == 1:
            # print('rrrr', self.textresult)
            try:
                result = float(self.textresult)
                self.lineEdit.clear()
                return result
            except ValueError as e:
                print('numpad error', e)
                self.lineEdit.clear()
                return None
        else:
            self.lineEdit.clear()
            return None
        


