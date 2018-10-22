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

    def __init__(self, dialog, parent=None):
        """Constructor."""
        super(getDateDialog, self).__init__(parent)
        #self.setupUi(self)
        self.dialog = dialog
        path = os.path.join(os.path.dirname(__file__), 'InspectionDigue_getDate.ui')
        uic.loadUi(path, self)
        self.previousdate = None




        self.finished.connect(self.dialogIsFinished)

    def setDate(self,datetoset = None):

        self.previousdate = str(self.dialog.dbase.workingdate)


        if False:
            if datetoset is None:
                date = QtCore.QDate.currentDate()
            else:
                date = QtCore.QDate.fromString(datetoset, 'yyyy-MM-dd')
            self.dateEdit.setDate(date)

        if True:
            todaydate = QtCore.QDate.currentDate()

            if self.previousdate is not None:
                self.dateEdit.setDate(QtCore.QDate.fromString(self.previousdate, 'yyyy-MM-dd') )
            else:
                self.dateEdit.setDate(todaydate)

            self.label_end.setText(todaydate.toString('yyyy-MM-dd'))
            self.dateEdit_end.setDate(todaydate)



            if self.dialog.dbase.version is None or self.dialog.dbase.version == '':
                sql = "SELECT MIN(datecreation) FROM Objet"
            else:
                sql = "SELECT MIN(datetimecreation) FROM Objet"

            query = self.dialog.dbase.query(sql)
            startdate = [row[0] for row in query]

            if self.dialog.dbase.version is None or self.dialog.dbase.version == '':
                if len(startdate) > 0:
                    # (QtCore.QDateTime.fromString(valuetoset, 'yyyy-MM-dd hh:mm:ss'))
                    date2 = QtCore.QDate.fromString(startdate[0], 'yyyy-MM-dd')
                else:
                    date2 = todaydate
            else:
                if len(startdate) > 0:
                    date2 = QtCore.QDateTime.fromString(startdate[0], 'yyyy-MM-dd hh:mm:ss').date()
                    #date2 = QtCore.QDate.fromString(startdate[0], 'yyyy-MM-dd')
                else:
                    date2 = todaydate




            self.label_start.setText(date2.toString('yyyy-MM-dd'))
            self.dateEdit_start.setDate(date2)

            self.dateLimitchanged()

            sliderpos = self.dateEdit_start.date().daysTo(self.dateEdit.date())
            self.horizontalSlider_date.setValue(sliderpos)

            self.horizontalSlider_date.valueChanged.connect(self.dateSliderAction)
            self.dateEdit_start.dateChanged.connect(self.dateLimitchanged)
            self.dateEdit_end.dateChanged.connect(self.dateLimitchanged)



    def dateSliderAction(self, sliderint):
        begindate = QtCore.QDate.fromString(self.label_start.text(), 'yyyy-MM-dd')
        datetoset = begindate.addDays(sliderint)

        self.dateEdit.setDate(datetoset)
        self.dialog.dbase.workingdate = datetoset.toString('yyyy-MM-dd')
        self.dialog.dbase.updateWorkingDate()

    def dateLimitchanged(self):
        dif = self.dateEdit_start.date().daysTo(self.dateEdit_end.date())
        # dif = todaydate - date2
        self.horizontalSlider_date.setRange(0, dif)
        self.horizontalSlider_date.setSingleStep(1)
        self.horizontalSlider_date.setPageStep(1)


    def dialogIsFinished(self):
        """
        return level list
        return color array like this : [stop in 0 < stop > 1 ,r,g,b]
        """
        if True:
            try:
                self.horizontalSlider_date.valueChanged.disconnect(self.dateSliderAction)
            except :
                pass
            try:
                self.dateEdit_start.dateChanged.disconnect(self.dateLimitchanged)
                self.dateEdit_end.dateChanged.disconnect(self.dateLimitchanged)
            except:
                pass

        if (self.result() == 1):
            return (self.dateEdit.date().toString('yyyy-MM-dd') )
        else:
            #self.previousdate = str(self.dbase.workingdate)
            self.dialog.dbase.workingdate = self.previousdate
            self.dialog.dbase.updateWorkingDate()
            return None
            
            