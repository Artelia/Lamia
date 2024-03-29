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



import os, datetime
from qgis.PyQt import uic, QtCore

from qgis.PyQt.QtWidgets import (QWidget,QGroupBox,QGridLayout,QLabel,QTableWidgetItem)

from ...lamia_abstractformtool import AbstractLamiaFormTool




class BaseZonegeoTool(AbstractLamiaFormTool):

    PREPROTOOLNAME = 'Zonegeo'
    DBASETABLENAME = 'Zonegeo'
    LOADFIRST = False

    tooltreewidgetCAT = 'Gestion'
    tooltreewidgetSUBCAT = 'Zone geographique'
    tooltreewidgetICONPATH = os.path.join(os.path.dirname(__file__), 'lamiabase_zonegeo_tool_icon.svg')

    # CHOOSERTREEWDG_COLSHOW = ['libelle']
    CHOOSERTREEWDGSPEC = {'colshow': ['libelle']}
    def __init__(self, **kwargs):
        super(BaseZonegeoTool, self).__init__(**kwargs)

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
        self.iconpath = os.path.join(os.path.dirname(__file__), 'lamiabase_zonegeo_tool_icon.svg')
        self.qtreewidgetfields = ['libelle']
        # ****************************************************************************************
        #properties ui
        pass
        """

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



    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass


    #def postInitFeatureProperties(self, feat):
    def postSelectFeature(self):
        #if feat is not None and not hasattr(self,'TOOLNAME'):
        #stat fill
        if self.currentFeaturePK is not None:
            for i, stat in enumerate(self.stats) :

                featpk = self.currentFeaturePK
                sql = stat[1]
                if sql != '':
                    sql += ' AND Zonegeo.pk_zonegeo = ' + str(featpk)
                    sql = self.dbase.updateQueryTableNow(sql)
                    query = self.dbase.query(sql)
                    if query:
                        result = query[0][0]
                    else:
                        result = 'Error'
                    itemresult = QTableWidgetItem(str(result))
                    itemresult.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                    self.toolwidgetmain.tableWidget_stats.setItem(i, 1, itemresult)



    """
    def createParentFeature(self):
        pkobjet = self.dbase.createNewObjet()

        if False:


            # lastrevision = self.dbase.maxrevision
            # datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
            datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            lastobjetid = self.dbase.getLastId('Objet') + 1
            sql = "INSERT INTO Objet (id_objet, lpk_revision_begin, datetimecreation ) "
            sql += "VALUES(" + str(lastobjetid) + "," + str(self.dbase.maxrevision) + ",'" + datecreation + "');"
            query = self.dbase.query(sql)
            self.dbase.commit()
            pkobjet = self.dbase.getLastRowId('Objet')

        # idnoeud = self.currentFeature.id()
        pkzonegeo = self.currentFeaturePK
        lastidzonegeo = self.dbase.getLastId('Zonegeo') + 1
        sql = "UPDATE Zonegeo SET id_zonegeo = " + str(lastidzonegeo) + ","
        sql += "lpk_objet = " + str(pkobjet)
        sql += " WHERE pk_zonegeo = " + str(pkzonegeo) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()




    def postSaveFeature(self, boolnewfeature):
        pass


    def deleteParentFeature(self):


        sql = "SELECT pk_objet FROM Zonegeo_qgis WHERE pk_zonegeo = " + str(self.currentFeaturePK)
        pkobjet = self.dbase.query(sql)[0][0]
        #idobjet = self.currentFeature['id_objet']
        #idressource = self.currentFeature['id_ressource']

        sql = "DELETE FROM Objet WHERE pk_objet = " + str(pkobjet)
        query = self.dbase.query(sql)
        self.dbase.commit()


        return True
    """

class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabase_zonegeo_tool_ui.ui')
        uic.loadUi(uipath, self)