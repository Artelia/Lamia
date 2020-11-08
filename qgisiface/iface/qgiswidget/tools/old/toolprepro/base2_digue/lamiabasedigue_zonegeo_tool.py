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




from qgis.PyQt import uic, QtCore

try:
    from qgis.PyQt.QtGui import (QWidget, QTableWidgetItem)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget,QTableWidgetItem)
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..base2.lamiabase_zonegeo_tool import BaseZonegeoTool
import os
import datetime



class BaseDigueZonegeoTool(BaseZonegeoTool):


    def __init__(self, **kwargs):
        super(BaseDigueZonegeoTool, self).__init__(**kwargs)

    def initFieldUI(self):

        self.toolwidgetmain = UserUI()
        self.formtoolwidgetconfdictmain = {'Zonegeo' : {'linkfield' : 'id_zonegeo',
                                                            'widgets' : {'typezonegeo':self.toolwidgetmain.comboBox_type,

                                                                        'BV_superficie':self.toolwidgetmain.doubleSpinBox_superf,
                                                                        'BV_cheminhydrau': self.toolwidgetmain.doubleSpinBox_chem,
                                                                        'BV_pente': self.toolwidgetmain.doubleSpinBox_pente,
                                                                'BV_coefruissellement': self.toolwidgetmain.doubleSpinBox_coef,

                                                                'BV_capacite': self.toolwidgetmain.doubleSpinBox_perret,


                                                                    }},
                                            'Objet' : {'linkfield' : 'id_objet',
                                                        'widgets' : {
                                                                    'libelle' : self.toolwidgetmain.lineEdit_nom,
                                                            'commentaire': self.toolwidgetmain.textBrowser_com,
                                                                    }}}

        # rem : il sera affiné le select avec le champ datetimecreation trouvé dans la requete
        # il faut que zone geo soit présent dans la requete
        self.stats = [['Infralineaire lineaire',
                        ''' SELECT SUM(ST_Length(ST_MakeValid(Infralineaire_now.geom))) 
                            FROM Infralineaire_now, Zonegeo 
                            WHERE ST_WITHIN(ST_MakeValid(Infralineaire_now.geom), ST_MakeValid(Zonegeo.geom)) ''']
                        ]

        self.toolwidgetmain.tableWidget_stats.setRowCount(0)
        self.toolwidgetmain.tableWidget_stats.setColumnCount(2)
        self.toolwidgetmain.tableWidget_stats.horizontalHeader().setStretchLastSection(True)
        for i, stat in enumerate(self.stats):
            rowPosition = self.toolwidgetmain.tableWidget_stats.rowCount()
            self.toolwidgetmain.tableWidget_stats.insertRow(rowPosition)
            itemfield = QTableWidgetItem(stat[0])
            itemfield.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.toolwidgetmain.tableWidget_stats.setItem(rowPosition, 0, itemfield)



        self.toolwidgetmain.toolButton_superf.clicked.connect(
            lambda: self.windowdialog.showNumPad(self.toolwidgetmain.doubleSpinBox_superf))
        self.toolwidgetmain.toolButton_chem.clicked.connect(
            lambda: self.windowdialog.showNumPad(self.toolwidgetmain.doubleSpinBox_chem))
        self.toolwidgetmain.toolButton_pente.clicked.connect(
            lambda: self.windowdialog.showNumPad(self.toolwidgetmain.doubleSpinBox_pente))
        self.toolwidgetmain.toolButton_coef.clicked.connect(
            lambda: self.windowdialog.showNumPad(self.toolwidgetmain.doubleSpinBox_coef))
        self.toolwidgetmain.toolButton_perret.clicked.connect(
            lambda: self.windowdialog.showNumPad(self.toolwidgetmain.doubleSpinBox_perret))

        self.toolwidgetmain.comboBox_type.currentIndexChanged.connect(self.combotypeChanged)
        self.toolwidgetmain.comboBox_type.currentIndexChanged.emit(0)



    def combotypeChanged(self, currentindex):
        if self.toolwidgetmain.comboBox_type.currentText() == 'Bassin versant':
            self.toolwidgetmain.stackedWidget.setCurrentIndex(1)
        else:
            self.toolwidgetmain.stackedWidget.setCurrentIndex(0)


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabasedigue_zonegeo_tool_ui.ui')
        uic.loadUi(uipath, self)