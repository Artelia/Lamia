# -*- coding: utf-8 -*-
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
import os, csv
import qgis
import sys, datetime
from collections import OrderedDict

from qgis.PyQt import uic, QtCore, QtGui
from qgis.PyQt.QtWidgets import (QWidget, QPushButton)
from ..base3.lamiabase_node_tool import BaseNodeTool





class BaseUrbandrainageNodeTool(BaseNodeTool):

    def __init__(self, **kwargs):
        super(BaseUrbandrainageNodeTool, self).__init__(**kwargs)



    def initMainToolWidget(self):
        
        self.toolwidgetmain = UserUI()
        self.formtoolwidgetconfdictmain = {'node' : {'linkfield' : 'id_node',
                                                    'widgets' : {}},
                                    'object' : {'linkfield' : 'id_object',
                                                'widgets' : {'name': self.toolwidgetmain.lineEdit_libelle}},
                                    'descriptionsystem' : {'linkfield' : 'id_descriptionsystem',
                                                'widgets' : {}}}
        

        self.model = QtGui.QStandardItemModel(self)
        



        self.toolwidgetmain.lineEdit_search.textChanged.connect(self.searchTxt)


        self.loadCsv()

        self.proxy = QtCore.QSortFilterProxyModel(self)
        self.proxy.setSourceModel(self.model)

        self.toolwidgetmain.tableView.setModel(self.proxy)

        # https://stackoverflow.com/questions/47201539/how-to-filter-multiple-column-in-qtableview


    def searchTxt(self, newtxt):
        print(newtxt)
        search = QtCore.QRegExp(  newtxt,
                                        QtCore.Qt.CaseInsensitive,
                                        QtCore.QRegExp.RegExp
                                        )
        self.proxy.setFilterKeyColumn(0)
        self.proxy.setFilterRegExp(search)


    def loadCsv(self, fileName=None):

        fileName = os.path.join(os.path.dirname(__file__),'Liste_bota_2020.csv' )

        with open(fileName, newline='') as fileInput:
            for row in csv.reader(fileInput):    
                items = [
                    QtGui.QStandardItem(field)
                    for field in row
                ]
                self.model.appendRow(items)



    def postSaveFeature(self, savedfeaturepk=None):
        super().postSaveFeature(savedfeaturepk)




class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabase_ff_node_tool_ui.ui')
        uic.loadUi(uipath, self)

