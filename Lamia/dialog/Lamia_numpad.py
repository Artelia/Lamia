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
    from qgis.PyQt.QtGui import QDialog, QPushButton
except:
    from qgis.PyQt.QtWidgets import QDialog, QPushButton

import os

class NumPadDialog(QDialog):

    def __init__(self, parent=None):
        super(NumPadDialog, self).__init__(parent)
        path = os.path.join(os.path.dirname(__file__), 'Lamia_numpad.ui')
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
            result = float(self.textresult)
            self.lineEdit.clear()
            return result
        else:
            self.lineEdit.clear()
            return None
        


