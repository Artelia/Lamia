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
class getDateDialog(QDialog):

    def __init__(self, parent=None):
        """Constructor."""
        super(getDateDialog, self).__init__(parent)
        #self.setupUi(self)
        path = os.path.join(os.path.dirname(__file__), 'InspectionDigue_getDate.ui')
        uic.loadUi(path, self)




        self.finished.connect(self.dialogIsFinished)

    def setDate(self,datetoset = None):
        if datetoset is None:
            date = QtCore.QDate.currentDate()
        else:
            date = QtCore.QDate.fromString(datetoset, 'yyyy-MM-dd')
        self.dateEdit.setDate(date)
        
    def dialogIsFinished(self):
        """
        return level list
        return color array like this : [stop in 0 < stop > 1 ,r,g,b]
        """
        if (self.result() == 1):
            return (self.dateEdit.date().toString('yyyy-MM-dd') )
        else:
            return None
            
            