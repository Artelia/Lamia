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

from qgis.PyQt import QtGui, uic, QtCore
import os
try:
    from qgis.PyQt.QtGui import (QDialog, QTableWidget, QVBoxLayout, QHeaderView, QTableWidgetItem)
except ImportError:
    from qgis.PyQt.QtWidgets import (QDialog, QTableWidget, QVBoxLayout, QHeaderView, QTableWidgetItem)


class LamiaTableFieldDialog(QDialog):
    """
    the main window widget
    """


    def __init__(self, dbase=None, parent=None):
        """
        Constructor
        :param canvas : current qgsmapcanvas
        :param parent : pyqt widget parent
        """
        super(LamiaTableFieldDialog, self).__init__(parent)
        debug = False
        self.dbase = dbase

        path = os.path.join(os.path.dirname(__file__), 'lamia_tablefielddialog.ui')
        uic.loadUi(path, self)

        self.tablelist = ['Infralineaire', 'Equipement', 'Noeud', 'Desordre', 'Observation']

    def update(self):
        if self.dbase is None:
            return
        # ordercount = 0
        for tablename in  self.tablelist :
            contents = QTableWidget(self.tabWidget_main)
            headernames = ['Nom', 'Type', 'Description', 'Valeur de champ textuelle', 'Valeur de champ stocké']
            contents.setColumnCount(len(headernames))
            contents.setHorizontalHeaderLabels(headernames)
            header = contents.horizontalHeader()
            header.setSectionResizeMode(QHeaderView.Stretch)

            layout = QVBoxLayout(contents)
            # add other widgets to the contents layout here
            # i.e. layout.addWidget(widget), etc
            self.tabWidget_main.addTab(contents, tablename)

            tableparent = [tablename] + self.dbase.getParentTable(tablename)
            tableparent.reverse()
            for tablename2 in tableparent:
                dbasedict = self.dbase.dbasetables[tablename]
                for field in dbasedict['fields'].keys():
                    rownumber = contents.rowCount()
                    contents.insertRow(rownumber )
                    #name row 0
                    item = QTableWidgetItem(field)
                    contents.setItem(rownumber, 0, item)
                    # type row 1
                    item = QTableWidgetItem(dbasedict['fields'][field]['PGtype'])
                    contents.setItem(rownumber, 1, item)
                    # description row 2
                    # todo
                    #values
                    compteurvalue=0
                    if 'Cst' in  dbasedict['fields'][field].keys():
                        for elem in dbasedict['fields'][field]['Cst']:
                            if compteurvalue>0:
                                contents.insertRow(rownumber + compteurvalue)
                            item = QTableWidgetItem(elem[0])
                            contents.setItem(rownumber + compteurvalue, 3, item)
                            item = QTableWidgetItem(elem[1])
                            contents.setItem(rownumber + compteurvalue, 4, item)
                            compteurvalue += 1
