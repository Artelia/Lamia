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
from ..main.DBaseParser import DBaseParser
try:
    from qgis.PyQt.QtGui import QDialog
except:
    from qgis.PyQt.QtWidgets import QDialog
    
import os


#FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'InspectionDigue_newDB.ui'))

#class newDBDialog(QDialog, FORM_CLASS):
class newDBDialog(QDialog):

    def __init__(self, parent=None):
        """Constructor."""
        super(newDBDialog, self).__init__(parent)
        #self.setupUi(self)
        path = os.path.join(os.path.dirname(__file__), 'InspectionDigue_newDB.ui')
        uic.loadUi(path, self)

        self.varlist=[]
        self.dbase = DBaseParser()
        
        self.comboBox_type.currentIndexChanged.connect(self.searchVar)
        self.comboBox_type.currentIndexChanged.emit(0)

        self.finished.connect(self.dialogIsFinished)
        
    def searchVar(self, comboindex):

        if self.dbase is  None:
            return self.varlist

        typebase = self.comboBox_type.currentText()
        self.dbase.variantespossibles = []
        self.dbase.variante = None
        self.dbase.createDBDictionary2(typebase, chekupdate=False)
        self.varlist = self.dbase.variantespossibles
        self.comboBox_var.clear()
        self.comboBox_var.addItems(self.varlist)



        if False:
            dirtypedb = os.path.join(os.path.dirname(__file__),'..','DBASE', 'create')
            listdirectories = os.listdir(dirtypedb)
            finaldirname=''
            for dirname in listdirectories:
                totalname = os.path.join(dirtypedb, dirname)
                if os.path.isdir(totalname):
                    #print(dirname)
                    if dirname[0:len(combotxt)] == combotxt:
                        #print(dirname, finaldirname,dirname > finaldirname )
                        if dirname > finaldirname:
                            finaldirname = dirname

            # print('***', finaldirname)
            vardir = os.path.join(dirtypedb, finaldirname)

            self.comboBox_var.clear()
            #self.comboBox_var.addItems(['Lamia'])
            self.varlist = [['Lamia', None]]
            listdirectories = os.listdir(vardir)
            for dirname in listdirectories:
                #print(dirname)
                if os.path.isdir(os.path.join(vardir,dirname)):
                    self.varlist.append([dirname, os.path.join(vardir,dirname) ])

            self.comboBox_var.addItems([elem[0] for elem in self.varlist])


        

        
    def dialogIsFinished(self):
        """
        return level list
        return color array like this : [stop in 0 < stop > 1 ,r,g,b]
        """
        #combovarindex = self.comboBox_var.currentIndex()
        #vardir = self.varlist[combovarindex][1]

        if (self.result() == QDialog.Accepted):
            return (self.comboBox_dbtype.currentText(),
                    self.comboBox_type.currentText(),
                    self.comboBox_var.currentText())
        else:
            return (None,None,None)
            
            