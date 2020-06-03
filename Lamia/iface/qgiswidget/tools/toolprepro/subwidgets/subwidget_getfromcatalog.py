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
import os, logging

from qgis.PyQt.QtWidgets import (QWidget, QVBoxLayout, QAbstractItemView, QHeaderView)
from qgis.PyQt import uic, QtCore, QtGui

from .subwidget_abstract import AbstractSubWidget
from Lamia.libslamia.lamiatabcatalog.lamiatabcatalog import TabCatalog

class CatalogWidget(AbstractSubWidget):

    UIPATH = os.path.join(os.path.dirname(__file__), 'subwidget_getfromcatalog_ui.ui')

    def __init__(self, 
                parentwdg=None,  
                parentframe=None, 
                catalogtype=None,
                catalogname=None,
                catalogsheet=None,
                coltoshow=None,
                sheetfield=None,
                valuefield=None):
        super(CatalogWidget, self).__init__(parentwdg=parentwdg,
                                                parentframe=parentframe)

        self.tableView.setFont(QtGui.QFont("Times",7))
        self.tableView.setStyleSheet("QTableView { padding: 5px;}")
        

        self.catalogname = catalogname
        self.coltoshow = coltoshow
        self.valuefield = valuefield
        self.sheetfield = sheetfield
        self.ffcatalog = TabCatalog.getInstance(catalogtype)
        self.pddatas = self.ffcatalog.pddatas

        if catalogsheet:
            pandasformodel = self.pddatas[catalogname][catalogsheet][coltoshow]
            self.frame_sheet.setVisible(False)
            self.model = PandasModel(data = pandasformodel)
        else:
            sheets = list(self.pddatas[catalogname].keys())
            for sheet in sheets:
                if self._testColsinSheet(sheet):
                    self.comboBox_sheet.addItem(sheet)

            self.comboBox_sheet.currentIndexChanged.connect(self.updateTableModel)
            self.updateTableModel(0)
        
        self.proxy = SortFilterProxyModel(self)
        self.proxy.setSourceModel(self.model)
        self.tableView.setModel(self.proxy)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)

        self._resizeHeader()

        # https://stackoverflow.com/questions/47201539/how-to-filter-multiple-column-in-qtableview

        self.lineEdit_search.textChanged.connect(self.searchTxt)
        self.pushButton.clicked.connect(self.applyResults)


    def postSelectFeature(self):
        self.lineEdit_search.setText('')


    def applyResults(self):
        if len(self.tableView.selectionModel().selectedRows()) == 0 :
            return

        proxysel = self.tableView.selectionModel().selection() 
        modelsel = self.proxy.mapSelectionToSource(proxysel)
        rowindex = modelsel.indexes()[0].row()

        dicttoapply={}
        for i, fieldname in enumerate(self.valuefield):
            dicttoapply[fieldname] = self.model.row(rowindex)[i]
        if self.sheetfield:
            dicttoapply[self.sheetfield] = self.comboBox_sheet.currentText()

        self.parentwdg.formutils.applyResultDict(dicttoapply, checkifinforgottenfield=False)

    def updateTableModel(self, comboindex):
        combotext = self.comboBox_sheet.itemText(comboindex)
        pandasformodel = self.pddatas[self.catalogname][combotext][self.coltoshow]
        # pandasformodel = self.pddatas[self.catalogname][combotext]

        self.model = PandasModel(data = pandasformodel)

        if hasattr(self,'proxy'):
            self.proxy.setSourceModel(self.model)
            self.tableView.setModel(self.proxy)
            self.lineEdit_search.setText('')
        self._resizeHeader()

    def _resizeHeader(self):
        header = self.tableView.horizontalHeader()
        header.resizeSections(QHeaderView.ResizeToContents)
        self.tableView.verticalHeader().resizeSections(QHeaderView.ResizeToContents)

    def _testColsinSheet(self,sheetname):
        # for sheetname in list(self.pddatas[self.catalogname].keys()):
        pandasformodeltotalcols = self.pddatas[self.catalogname][sheetname].columns.tolist()
        if all(elem in pandasformodeltotalcols  for elem in self.coltoshow ): 
            return True
        else:
            return False

    def loadCatalogInTable(self, sheetname=None, coltoshow=None):

        for row in csv.reader(fileInput):    
            items = [
                QtGui.QStandardItem(field)
                for field in row
            ]
            self.model.appendRow(items)




    def searchTxt(self, newtxt):
        # search = QtCore.QRegExp(  newtxt,
        #                                 QtCore.Qt.CaseInsensitive,
        #                                 QtCore.QRegExp.RegExp
        #                                 )


        self.proxy.setFilterStringandColumn(newtxt, [0,1])



class PandasModel(QtCore.QAbstractTableModel):
    """
    Class to populate a table view with a pandas dataframe
    """
    def __init__(self, data, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data.values)

    def columnCount(self, parent=None):
        return self._data.columns.size

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid():
            if role == QtCore.Qt.DisplayRole:
                return str(self._data.values[index.row()][index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self._data.columns[col]
        return None

    def row(self, rowindex):
        return self._data.iloc[rowindex].values


class SortFilterProxyModel(QtCore.QSortFilterProxyModel):
    def __init__(self, *args, **kwargs):
        QtCore.QSortFilterProxyModel.__init__(self, *args, **kwargs)
        self.filterString = ''
        self.filterColumns = []

    def setFilterStringandColumn(self, searchstr,cols):
        self.filterString = searchstr.lower()
        self.filterColumns = cols
        self.invalidateFilter()


    def filterAcceptsRow(self, source_row, source_parent):

        model = self.sourceModel()  # the underlying model, 
                                    # implmented as a python array
        colcount = model.columnCount()
        row = model.row(source_row)
        if self.filterColumns:
            tests = [self.filterString in str(row[col]).lower()
                    for col in self.filterColumns]
        else:
            tests = [self.filterString in str(row[col]).lower()
                    for col in range(colcount)]

        return True in tests        # accepts row if any column
                                    # contains filterString

