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
    from qgis.PyQt.QtGui import (QWidget, QInputDialog)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget, QInputDialog)
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..base2.lamiabase_intervenant_tool import BaseIntervenantTool
import os
import datetime



class BaseDigueIntervenantTool(BaseIntervenantTool):

    LOADFIRST = False
    dbasetablename = 'Intervenant'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(BaseDigueIntervenantTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil,parentwidget, parent=parent)


    """
    def initTool(self):
        # ****************************************************************************************
        # Main spec

        self.CAT = 'Gestion'
        self.NAME = 'Intervenants'
        self.dbasetablename = 'Intervenant'
        self.visualmode = [1, 2]
        # self.PointEnabled = True
        # self.LineENABLED = True
        # self.PolygonENABLED = True
        # self.magicfunctionENABLED = True
        self.linkagespec = {'Tcobjetintervenant' : {'tabletc' : 'Tcobjetintervenant',
                                              'idsource' : 'id_intervenant',
                                            'idtcsource' : 'id_tcintervenant',
                                           'iddest' : 'id_objet',
                                           'idtcdest' : 'id_tcobjet',
                                           'desttable' : ['Infralineaire','Prestation']}
                                            }
        # self.pickTable = None
        self.iconpath = os.path.join(os.path.dirname(__file__), 'lamiadefault_intervenant_tool_icon.png')
        self.qtreewidgetfields = ['nom']
        # ****************************************************************************************
        #properties ui
        pass

    def initDesktopUI(self):
        # ****************************************************************************************
        #   userui Field
        if self.userwdgdesktop is None:
            # ****************************************************************************************
            # userui
            self.userwdgdesktop = UserUI()

            self.linkuserwdgdesktop = {'Intervenant': {'linkfield': 'id_intervenant',
                                                  'widgets': {'nom' : self.userwdgdesktop.lineEdit_nom,
                                                              'societe': self.userwdgdesktop.lineEdit_societe,
                                                              'adresse': self.userwdgdesktop.lineEdit_adresse,
                                                              'fax': self.userwdgdesktop.lineEdit_mail,
                                                              'tel': self.userwdgdesktop.lineEdit_tel,}},
                                'Objet': {'linkfield': 'id_objet',
                                          'widgets': {}}}




    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass


    def postInitFeatureProperties(self, feat):
        pass

    def createParentFeature(self):

        lastrevision = self.dbase.getLastPk('Revision')
        datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
        lastobjetid = self.dbase.getLastId('Objet') + 1
        sql = "INSERT INTO Objet (id_objet, id_revisionbegin, datecreation ) "
        sql += "VALUES(" + str(lastobjetid ) + "," + str(lastrevision) +  ",'" + datecreation + "');"
        query = self.dbase.query(sql)
        self.dbase.commit()

        pkintervenant = self.currentFeature.id()
        lastidintervenant = self.dbase.getLastId('Intervenant') + 1

        sql = "UPDATE Intervenant SET id_objet = " + str(lastobjetid)  + ","
        sql += "id_intervenant = " + str(lastidintervenant) + ","
        sql += "id_revisionbegin = " + str(lastrevision)
        sql += " WHERE pk_intervenant = " + str(pkintervenant) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()


        if self.parentWidget is not None and self.parentWidget.currentFeature is not None:
            if self.parentWidget.dbasetablename == 'Marche':
                items = [elem[0] for elem in self.dbasetable['fields']['fonction']['Cst']]
                item, ok = QInputDialog.getItem(self, "Choisir la fonction",
                                                "Choisir la fonction", items, 0, False)
                print(item,ok)
                if ok:
                    fonctionvalue = self.dbase.getConstraintRawValueFromText(self.tablename,'fonction',item)
                    currentparentlinkfield = self.parentWidget.currentFeature['id_objet']
                    currentlinkfield = self.currentFeature['id_intervenant']
                    sql = "INSERT INTO Tcobjetintervenant(id_tcintervenant, id_tcobjet,fonction) VALUES( " + str(currentlinkfield + "," + currentparentlinkfield + "," + fonctionvalue + ");")
                    #sql = "UPDATE OBSERVATION SET LkDesordre = " + str(currentparentlinkfield) + " WHERE id = " + str(idobservation) + ";"
                    query = self.dbase.query(sql)
                    self.dbase.commit()

    def postSaveFeature(self, boolnewfeature):
        pass
        
    """

"""
class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiadefault_intervenant_tool_ui.ui')
        uic.loadUi(uipath, self)
"""