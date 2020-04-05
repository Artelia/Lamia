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


# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore

try:
    from qgis.PyQt.QtGui import (QWidget, QGroupBox,QGridLayout,QLabel,QTableWidgetItem)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget,QGroupBox,QGridLayout,QLabel,QTableWidgetItem)
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..base2.lamiabase_zonegeo_tool import BaseZonegeoTool
import os
import datetime



class BaseAssainissementZonegeoTool(BaseZonegeoTool):

    LOADFIRST = False

    def __init__(self, **kwargs):
        super(BaseAssainissementZonegeoTool, self).__init__(**kwargs)


    def initMainToolWidget(self):

        self.toolwidgetmain = UserUI()
        self.formtoolwidgetconfdictmain = {'Zonegeo' : {'linkfield' : 'id_zonegeo',
                                            'widgets' : {
                                                        'typezonegeo':self.toolwidgetmain.comboBox_type
                                                    }},
                                            'Objet' : {'linkfield' : 'id_objet',
                                                        'widgets' : {
                                                                    'libelle' : self.toolwidgetmain.lineEdit_nom
                                                                    }}}


        self.stats = [['EU - lineaire gravitaire', ''' SELECT SUM(ST_Length(ST_MakeValid(Infralineaire_now.geom))) 
                                        FROM Infralineaire_now, Zonegeo 
                                        WHERE ST_WITHIN(ST_MakeValid(Infralineaire_now.geom), ST_MakeValid(Zonegeo.geom))
                                            AND Infralineaire_now.typeReseau = 'USE' AND Infralineaire_now.modeCirculation = 1 
                                            AND branchement = 0 '''],

                        ['EU - lineaire refoulement', ''' SELECT SUM(ST_Length(ST_MakeValid(Infralineaire_now.geom))) 
                                                    FROM Infralineaire_now, Zonegeo 
                                                    WHERE ST_WITHIN(ST_MakeValid(Infralineaire_now.geom), ST_MakeValid(Zonegeo.geom))
                                                        AND Infralineaire_now.typeReseau = 'USE' AND Infralineaire_now.modeCirculation = 2 
                                                        AND branchement = 0  '''],

                        ['EU - regards ', ''' SELECT COUNT(*) 
                                                            FROM Noeud_now, Zonegeo 
                                                            WHERE ST_WITHIN(ST_MakeValid(Noeud_now.geom), ST_MakeValid(Zonegeo.geom))
                                                                AND Noeud_now.typeOuvrageAss = '60' AND Noeud_now.typeReseau = 'USE' '''],

                        ['EU - branchements ', ''' SELECT COUNT(*) 
                                                FROM Noeud_now, Zonegeo 
                                                WHERE ST_WITHIN(ST_MakeValid(Noeud_now.geom), ST_MakeValid(Zonegeo.geom))
                                                AND Noeud_now.typeOuvrageAss = '61'  AND Noeud_now.typeReseau = 'USE'  '''],

                        ['EU - Postes de refoulement ', ''' SELECT COUNT(*) 
                                            FROM Noeud_now, Zonegeo 
                                            WHERE ST_WITHIN(ST_MakeValid(Noeud_now.geom), ST_MakeValid(Zonegeo.geom))
                                            AND Noeud_now.typeOuvrageAss = '10'  AND Noeud_now.typeReseau = 'USE'   '''],


                        ['EU - Deversoirs d orage ', ''' SELECT COUNT(*) 
                                                        FROM Noeud_now, Zonegeo 
                                                        WHERE ST_WITHIN(ST_MakeValid(Noeud_now.geom), ST_MakeValid(Zonegeo.geom))
                                                            AND Noeud_now.typeOuvrageAss = '40'  AND Noeud_now.typeReseau = 'USE'  '''],

                        ['EU - STEP ', ''' SELECT COUNT(*) 
                                                            FROM Noeud_now, Zonegeo 
                                                            WHERE ST_WITHIN(ST_MakeValid(Noeud_now.geom), ST_MakeValid(Zonegeo.geom))
                                                                AND Noeud_now.typeOuvrageAss = '20' '''],

                        ['EP - lineaire collecteurs', ''' SELECT SUM(ST_Length(ST_MakeValid(Infralineaire_now.geom))) 
                                        FROM Infralineaire_now, Zonegeo 
                                        WHERE ST_WITHIN(ST_MakeValid(Infralineaire_now.geom), ST_MakeValid(Zonegeo.geom))
                                            AND Infralineaire_now.typeReseau = 'PLU' AND branchement = 0  
                                            AND Infralineaire_now.formecanalisation IN ('CIR', 'AQU', 'OVO') '''],

                        ['EP - lineaire fosses-caniveaux', ''' SELECT SUM(ST_Length(ST_MakeValid(Infralineaire_now.geom))) 
                                                                FROM Infralineaire_now, Zonegeo 
                                                                WHERE ST_WITHIN(ST_MakeValid(Infralineaire_now.geom), ST_MakeValid(Zonegeo.geom))
                                                                AND Infralineaire_now.typeReseau = 'PLU' AND branchement = 0  
                                                                AND Infralineaire_now.formecanalisation IN ('FOS', 'FOB') '''],


                        ['EP - regards ', ''' SELECT COUNT(*) 
                                                FROM Noeud_now, Zonegeo 
                                                WHERE ST_WITHIN(ST_MakeValid(Noeud_now.geom), ST_MakeValid(Zonegeo.geom))
                                                AND Noeud_now.typeOuvrageAss = '60'  AND Noeud_now.typeReseau = 'PLU'  '''],

                        ['EP - branchements ', ''' SELECT COUNT(*) 
                                                FROM Noeud_now, Zonegeo 
                                                WHERE ST_WITHIN(ST_MakeValid(Noeud_now.geom), ST_MakeValid(Zonegeo.geom))
                                                    AND Noeud_now.typeOuvrageAss = '61'  AND Noeud_now.typeReseau = 'PLU'  '''],

                        ['EP - grilles - avaloirs ', ''' SELECT COUNT(*) 
                                                        FROM Noeud_now, Zonegeo 
                                                        WHERE ST_WITHIN(ST_MakeValid(Noeud_now.geom), ST_MakeValid(Zonegeo.geom))
                                                            AND Noeud_now.typeOuvrageAss IN ('70','71','72')  AND Noeud_now.typeReseau = 'PLU'  '''],


                        ['UN - lineaire gravitaire', ''' SELECT SUM(ST_Length(ST_MakeValid(Infralineaire_now.geom))) 
                                            FROM Infralineaire_now, Zonegeo 
                                            WHERE ST_WITHIN(ST_MakeValid(Infralineaire_now.geom), ST_MakeValid(Zonegeo.geom))
                                            AND Infralineaire_now.typeReseau = 'UNI' AND Infralineaire_now.modeCirculation = 1 
                                            AND branchement = 0  '''],

                        ['UN - lineaire refoulement', ''' SELECT SUM(ST_Length(ST_MakeValid(Infralineaire_now.geom))) 
                                                        FROM Infralineaire_now, Zonegeo 
                                                        WHERE ST_WITHIN(ST_MakeValid(Infralineaire_now.geom), ST_MakeValid(Zonegeo.geom))
                                                            AND Infralineaire_now.typeReseau = 'UNI' AND Infralineaire_now.modeCirculation = 2 
                                                            AND branchement = 0  '''],

                        ['UN - regards ', ''' SELECT COUNT(*) 
                                            FROM Noeud_now, Zonegeo 
                                            WHERE ST_WITHIN(ST_MakeValid(Noeud_now.geom), ST_MakeValid(Zonegeo.geom))
                                                AND Noeud_now.typeOuvrageAss = '60'  AND Noeud_now.typeReseau = 'UNI'  '''],

                        ['regards mixtes', ''' SELECT COUNT(*) /2 
                                FROM Noeud_now, Zonegeo 
                                WHERE ST_WITHIN(ST_MakeValid(Noeud_now.geom), ST_MakeValid(Zonegeo.geom))
                                AND Noeud_now.typeOuvrageAss = '62'   '''],


                        ['UN - branchements ', ''' SELECT COUNT(*) 
                                                FROM Noeud_now, Zonegeo 
                                                WHERE ST_WITHIN(ST_MakeValid(Noeud_now.geom), ST_MakeValid(Zonegeo.geom))
                                                    AND Noeud_now.typeOuvrageAss = '61'  AND Noeud_now.typeReseau = 'UNI'  '''],

                        ['UN - Postes de refoulement ', ''' SELECT COUNT(*) 
                                                        FROM Noeud_now, Zonegeo 
                                                        WHERE ST_WITHIN(ST_MakeValid(Noeud_now.geom), ST_MakeValid(Zonegeo.geom))
                                                            AND Noeud_now.typeOuvrageAss = '10'  AND Noeud_now.typeReseau = 'UNI'   '''],

                        ['UN - Deversoirs d orage ', ''' SELECT COUNT(*) 
                                                            FROM Noeud_now, Zonegeo 
                                                            WHERE ST_WITHIN(ST_MakeValid(Noeud_now.geom), ST_MakeValid(Zonegeo.geom))
                                                            AND Noeud_now.typeOuvrageAss = '40'  AND Noeud_now.typeReseau = 'UNI'  '''],

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


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabaseassainissement_zonegeo_tool_ui.ui')
        uic.loadUi(uipath, self)