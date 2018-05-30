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

#FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'InspectionDigue_newDB.ui'))

#class newDBDialog(QDialog, FORM_CLASS):
class IconSizeDialog(QDialog):

    def __init__(self, dialog, parent=None):
        """Constructor."""
        super(IconSizeDialog, self).__init__(parent)
        #self.setupUi(self)
        self.dialog = dialog
        path = os.path.join(os.path.dirname(__file__), 'Lamia_iconsize.ui')
        uic.loadUi(path, self)

        self.spinBox.valueChanged.connect(self.dialog.themechanged)


        self.finished.connect(self.dialogIsFinished)

        
    def dialogIsFinished(self):
        """
        return level list
        return color array like this : [stop in 0 < stop > 1 ,r,g,b]
        """

        if (self.result() == 1):
            return None
        else:
            return None
            
            