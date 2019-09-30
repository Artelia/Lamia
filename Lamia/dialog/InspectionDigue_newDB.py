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
            
            