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

#class ConflitHorsLigne(QDialog, FORM_CLASS):
class ConflitHorsLigne(QDialog):

    def __init__(self, parent=None, local, original):
        """Constructor."""
        super(ConflitHorsLigne, self).__init__(parent)
        #self.setupUi(self)
        path = os.path.join(os.path.dirname(__file__), 'InspectionDigue_ConflitHorsLigne.ui')
        uic.loadUi(path, self)



        self.label_label_3.setText(local)
        self.label_label_6.setText(original)



        self.finished.connect(self.dialogIsFinished)


    def dialogIsFinished(self):
        return self.result() == 1
