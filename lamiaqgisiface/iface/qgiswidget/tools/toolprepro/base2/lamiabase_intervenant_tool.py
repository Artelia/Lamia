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



import os
import datetime

from qgis.PyQt import uic, QtCore
from qgis.PyQt.QtWidgets import (QWidget, QInputDialog)

from ...lamia_abstractformtool import AbstractLamiaFormTool




class BaseIntervenantTool(AbstractLamiaFormTool):

    PREPROTOOLNAME = 'Intervenant'
    DBASETABLENAME = 'Intervenant'
    LOADFIRST = False

    tooltreewidgetCAT = 'Gestion'
    tooltreewidgetSUBCAT = 'Intervenants'
    tooltreewidgetICONPATH = os.path.join(os.path.dirname(__file__), 'lamiabase_intervenant_tool_icon.png')

    tempparentjoin = {}
    linkdict = {'colparent': 'id_objet',
                'colthistable': 'id_intervenant',
                    'tctable': 'Tcobjetintervenant',
                    'tctablecolparent':'lid_objet',
                    'tctablecolthistable':'lid_intervenant'}
    for tablename in ['Infralineaire','Marche']:
        tempparentjoin[tablename] = linkdict
    PARENTJOIN = tempparentjoin
    #CHOOSERTREEWDG_COLSHOW = ['societe', 'nom']
    CHOOSERTREEWDGSPEC = {'colshow': ['societe', 'nom']}

    def __init__(self, **kwargs):
        super(BaseIntervenantTool, self).__init__(**kwargs)

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
                                            'idtcsource' : 'lid_intervenant',
                                           'iddest' : 'id_objet',
                                           'idtcdest' : 'lid_objet',
                                           'desttable' : ['Infralineaire','Prestation']}
                                            }
        # self.pickTable = None
        self.iconpath = os.path.join(os.path.dirname(__file__), 'lamiabase_intervenant_tool_icon.png')
        self.qtreewidgetfields = ['nom']
        # ****************************************************************************************
        #properties ui
        pass
    """

    def initMainToolWidget(self):

        self.toolwidgetmain = UserUI()

        self.formtoolwidgetconfdictmain = {'Intervenant': {'linkfield': 'id_intervenant',
                                                        'widgets': {'nom' : self.toolwidgetmain.lineEdit_nom,
                                                                    'societe': self.toolwidgetmain.lineEdit_societe,
                                                                    'fonction': self.toolwidgetmain.lineEdit_fonction,
                                                                    'adresse': self.toolwidgetmain.lineEdit_adresse,
                                                                    'tel': self.toolwidgetmain.lineEdit_tel,
                                                                    'courriel': self.toolwidgetmain.lineEdit_mail,
                                                                    'fax': self.toolwidgetmain.lineEdit_fax,
                                                                    }},
                                    'Objet': {'linkfield': 'id_objet',
                                                'widgets': {}}}




    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass


    # def postInitFeatureProperties(self, feat):
    def postSelectFeature(self):
        pass

    """
    def createParentFeature(self):
        pkobjet = self.dbase.createNewObjet()

        if False:



            datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            lastobjetid = self.dbase.getLastId('Objet') + 1
            sql = "INSERT INTO Objet (id_objet, lpk_revision_begin, datetimecreation ) "
            sql += "VALUES(" + str(lastobjetid) + "," + str(self.dbase.maxrevision) + ",'" + datecreation + "');"
            query = self.dbase.query(sql)
            self.dbase.commit()
            pkobjet = self.dbase.getLastRowId('Objet')


        # idnoeud = self.currentFeature.id()
        pkintervenant = self.currentFeaturePK
        lastidintervenant  = self.dbase.getLastId('Intervenant') + 1
        sql = "UPDATE Intervenant SET id_intervenant = " + str(lastidintervenant) + ","
        sql += "lpk_objet = " + str(pkobjet)
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

    """




    def postSaveFeature(self, savedfeaturepk=None):
        pass

    """
    def deleteParentFeature(self):


        sql = "SELECT pk_objet FROM Intervenant_qgis WHERE pk_intervenant = " + str(self.currentFeaturePK)
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
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabase_intervenant_tool_ui.ui')
        uic.loadUi(uipath, self)