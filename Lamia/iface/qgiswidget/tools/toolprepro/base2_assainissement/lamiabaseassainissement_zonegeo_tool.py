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
    dbasetablename = 'Zonegeo'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(BaseAssainissementZonegeoTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil,parentwidget, parent=parent)

        if False:
            self.statgrpbox = QGroupBox('Statistiques')
            self.Form.layout().insertWidget(self.statgrpbox)
            layout = QGridLayout()

            layout.setColumnStretch(1, 4)
            self.statgrpbox.setLayout(layout)

    def initFieldUI(self):
        # ****************************************************************************************
        # userui Desktop
        if self.userwdgfield is None:

            # ****************************************************************************************
            # userui
            self.userwdgfield = UserUI()
            self.linkuserwdgfield = {'Zonegeo' : {'linkfield' : 'id_zonegeo',
                                             'widgets' : {
                                                          'typezonegeo':self.userwdgfield.comboBox_type
                                                        }},
                                'Objet' : {'linkfield' : 'id_objet',
                                          'widgets' : {
                                                        'libelle' : self.userwdgfield.lineEdit_nom
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

            self.userwdgfield.tableWidget_stats.setRowCount(0)
            self.userwdgfield.tableWidget_stats.setColumnCount(2)
            self.userwdgfield.tableWidget_stats.horizontalHeader().setStretchLastSection(True)
            for i, stat in enumerate(self.stats):
                rowPosition = self.userwdgfield.tableWidget_stats.rowCount()
                self.userwdgfield.tableWidget_stats.insertRow(rowPosition)
                itemfield = QTableWidgetItem(stat[0])
                itemfield.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.userwdgfield.tableWidget_stats.setItem(rowPosition, 0, itemfield)




    """
    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Gestion'
        self.NAME = 'Zone geographique'
        self.dbasetablename = 'Zonegeo'
        self.visualmode = [ 1, 2]
        # self.PointENABLED = True
        # self.LineENABLED = True
        self.PolygonENABLED = True
        # self.magicfunctionENABLED = True
        self.linkagespec = {'Tcobjetzonegeo' : {'tabletc' : 'Tcobjetzonegeo',
                                              'idsource' : 'id_zonegeo',
                                            'idtcsource' : 'id_tczonegeo',
                                           'iddest' : 'id_objet',
                                           'idtcdest' : 'id_tcobjet',
                                           'desttable' : ['Infralineaire']}}
        # self.pickTable = None
        self.iconpath = os.path.join(os.path.dirname(__file__), 'lamiadefault_zonegeo_tool_icon.svg')
        self.qtreewidgetfields = ['nom']
        # ****************************************************************************************
        #properties ui
        pass

    def initFieldUI(self):
        # ****************************************************************************************
        # userui Desktop
        if self.userwdgfield is None:

            # ****************************************************************************************
            # userui
            self.userwdgfield = UserUI()
            self.linkuserwdgfield = {'Zonegeo' : {'linkfield' : 'id_zonegeo',
                                             'widgets' : {'nom' : self.userwdgfield.lineEdit_nom,
                                                          'type_zonegeo':self.userwdgfield.comboBox_type }},
                                'Objet' : {'linkfield' : 'id_objet',
                                          'widgets' : {}}}


    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass




    def createParentFeature(self):

        lastrevision = self.dbase.getLastPk('Revision')
        datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
        lastobjetid = self.dbase.getLastId('Objet') + 1
        sql = "INSERT INTO Objet (id_objet, id_revisionbegin, datecreation ) "
        sql += "VALUES(" + str(lastobjetid ) + "," + str(lastrevision) +  ",'" + datecreation + "');"
        query = self.dbase.query(sql)
        self.dbase.commit()

        pkzonegeo = self.currentFeature.id()
        lastidzonegeo = self.dbase.getLastId('Zonegeo') + 1

        sql = "UPDATE Zonegeo SET id_objet = " + str(lastobjetid)  + ","
        sql += "id_zonegeo = " + str(lastidzonegeo) + ","
        sql += "id_revisionbegin = " + str(lastrevision)
        sql += " WHERE pk_zonegeo = " + str(pkzonegeo) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()


        #self.initLinkageFromGeometry('Tcobjetzonegeo', pkzonegeo)

    def postSaveFeature(self, boolnewfeature):
        pass

    """
class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabaseassainissement_zonegeo_tool_ui.ui')
        uic.loadUi(uipath, self)