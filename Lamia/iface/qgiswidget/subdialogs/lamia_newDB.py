# -*- coding: utf-8 -*-

# unicode behaviour
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
import os
import Lamia

from qgis.PyQt import uic, QtCore, QtGui
from qgis.PyQt.QtWidgets import QDialog

from Lamia.dbasemanager.dbaseparserabstract import AbstractDBaseParser


class newDBDialog(QDialog):
    def __init__(self, parent=None):
        """Constructor."""
        super(newDBDialog, self).__init__(parent)
        # self.setupUi(self)
        path = os.path.join(os.path.dirname(__file__), "lamia_newDB.ui")
        uic.loadUi(path, self)

        self.varlist = []
        # self.dbase = DBaseParser()
        self.dbase = AbstractDBaseParser()
        self.searchDBases()

        self.comboBox_type.currentIndexChanged.connect(self.searchVar)
        self.comboBox_type.currentIndexChanged.emit(0)

        self.finished.connect(self.dialogIsFinished)

    def searchDBases(self):
        wrktypedir = os.path.join(os.path.dirname(Lamia.__file__), "worktypeconf")
        worktypes = os.listdir(wrktypedir)
        finalworktype = []
        for worktype in worktypes:
            if worktype[0] == "_" or len(worktype.split("_")) < 2:
                continue
            basepath = os.path.join(wrktypedir, worktype, "dbase")
            if os.path.isdir(basepath):
                finalworktype.append(worktype)
        print(finalworktype)
        self.comboBox_type.addItems(finalworktype)

    def searchVar(self, comboindex):

        if self.dbase is None:
            return self.varlist

        typebase = self.comboBox_type.currentText()
        self.dbase.variantespossibles = []
        self.dbase.variante = None
        self.dbase.dbconfigreader.createDBDictionary(typebase)
        self.varlist = self.dbase.dbconfigreader.variantespossibles
        self.comboBox_var.clear()
        self.comboBox_var.addItems(self.varlist)

    def dialogIsFinished(self):
        """
        return level list
        return color array like this : [stop in 0 < stop > 1 ,r,g,b]
        """
        # combovarindex = self.comboBox_var.currentIndex()
        # vardir = self.varlist[combovarindex][1]

        if self.result() == QDialog.Accepted:
            return (
                self.comboBox_dbtype.currentText(),
                self.comboBox_type.currentText(),
                self.comboBox_var.currentText(),
            )
        else:
            return (None, None, None)

