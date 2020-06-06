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



import os, sys, datetime
from qgis.PyQt import uic, QtCore, QtGui
from qgis.PyQt.QtWidgets import (QWidget)

from ...lamia_abstractformtool import AbstractLamiaFormTool


class BaseRapportTool(AbstractLamiaFormTool):

    PREPROTOOLNAME = 'Rapport'
    DBASETABLENAME = 'Rapport'
    LOADFIRST = False

    tooltreewidgetCAT = 'Ressources'
    tooltreewidgetSUBCAT = 'Rapport'
    tooltreewidgetICONPATH = os.path.join(os.path.dirname(__file__), 'lamiabase_rapport_tool_icon.png')

    tempparentjoin = {}
    linkdict = {'colparent': 'id_objet',
                'colthistable': 'id_ressource',
                    'tctable': 'Tcobjetressource',
                    'tctablecolparent':'lid_objet',
                    'tctablecolthistable':'lid_ressource'}
    for tablename in ['Observation', 'Noeud', 'Infralineaire', 'Equipement']:
        tempparentjoin[tablename] = linkdict
    PARENTJOIN = tempparentjoin


    def __init__(self, **kwargs):
        super(BaseRapportTool, self).__init__(**kwargs)
        self.instancekwargs = kwargs

    """
    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Ressources'
        self.NAME = 'Rapport'
        self.dbasetablename = 'Rapport'
        self.visualmode = [1, 2]
        # self.PointENABLED = True
        # self.LineENABLED = True
        self.PolygonENABLED = True
        # self.magicfunctionENABLED = True
        self.linkagespec = {'Tcobjetressource' : {'tabletc' : 'Tcobjetressource',
                                           'idsource' : 'id_ressource',
                                       'idtcsource' : 'lid_ressource',
                                           'iddest' : 'id_objet',
                                       'idtcdest' : 'lid_objet',
                                           'desttable' : ['Infralineaire','Equipement','Observation']},
                            'Marche': {'tabletc': None,
                                           'idsource': 'lk_marche',
                                           'idtcsource': None,
                                           'iddest': 'id_marche',
                                           'idtcdest': None,
                                           'desttable': ['Marche']},
                            'Rapport': {'tabletc': 'within',
                                                   'idsource': 'id_rapport',
                                                   'idtcsource': None,
                                                   'iddest': 'id_rapport',
                                                   'idtcdest': None,
                                                   'desttable': ['Infralineaire','Noeud','Equipement']}
                            }

        # ****************************************************************************************
        #properties ui
        self.iconpath = os.path.join(os.path.dirname(__file__), 'lamiabase_rapport_tool_icon.png')
        self.qtreewidgetfields = ['libelle']
    """


    def initMainToolWidget(self):

        self.toolwidgetmain = UserUI()
        self.toolwidgetmain.pushButton_chooseph.clicked.connect(self.choosePhoto)
        self.toolwidgetmain.pushButton_openph.clicked.connect(self.openFile)

        self.formtoolwidgetconfdictmain = {'Rapport' : {'linkfield' : 'id_rapport',
                                                            'widgets' : { }},
                                            'Objet' : {'linkfield' : 'id_objet',
                                                        'widgets' : {'libelle' : self.toolwidgetmain.lineEdit_nom}},
                                            'Ressource' : {'linkfield' : 'id_ressource',
                                                        'widgets' : {'file': self.toolwidgetmain.lineEdit_file,
                                                                    'description': self.toolwidgetmain.lineEdit_description,
                                                                    'datetimeressource': self.toolwidgetmain.dateTimeEdit}}}



    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass

    def openFile(self):
        filepath = self.dbase.completePathOfFile(self.toolwidget.lineEdit_file.text())
        if filepath != '':
            os.startfile(filepath)


    def choosePhoto(self):

        file , extension= self.mainifacewidget.qfiledlg.getOpenFileName(None, 'Choose the file', self.mainifacewidget.imagedirectory,
                                                                    'All (*.*)', '')

        if file:
            self.toolwidget.lineEdit_file.setText(os.path.normpath(file))


    #def postInitFeatureProperties(self, feat):
    def postSelectFeature(self):
        if self.currentFeaturePK is None:
            datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            #self.initFeatureProperties(feat, 'Ressource', 'datetimeressource', datecreation)
            self.formutils.applyResultDict({'datetimeressource': datecreation}, False)


    """
    def createParentFeature(self):
        pkobjet = self.dbase.createNewObjet()

        lastressourceid = self.dbase.getLastId('Ressource') + 1
        sql = "INSERT INTO Ressource (id_ressource, lpk_objet) "
        sql += "VALUES(" + str(lastressourceid) +   "," + str(pkobjet) + ");"
        query = self.dbase.query(sql)
        self.dbase.commit()
        pkres = self.dbase.getLastRowId('Ressource')

        pkrapport = self.currentFeaturePK
        lastidrapport = self.dbase.getLastId('Rapport') + 1
        sql = "UPDATE Rapport SET id_rapport = " + str(lastidrapport)  + ","
        sql += "lpk_ressource = " + str(pkres)
        sql += " WHERE pk_rapport = " + str(pkrapport)
        query = self.dbase.query(sql)
        self.dbase.commit()

        if self.parentWidget is not None and self.parentWidget.currentFeature is not None:

            #get parent id_objet
            sql = " SELECT id_objet FROM " + self.parentWidget.dbasetablename.lower() + "_qgis"
            sql += " WHERE pk_" + self.parentWidget.dbasetablename.lower() + " = " + str(self.parentWidget.currentFeaturePK)
            currentparentlinkfield = self.dbase.query(sql)[0][0]

            #currentparentlinkfield = self.parentWidget.currentFeature['id_objet']
            sql = "INSERT INTO Tcobjetressource(lpk_revision_begin, lid_objet, lid_ressource) "
            sql += " VALUES(" + str(self.dbase.maxrevision) + "," + str(currentparentlinkfield) + ',' + str(lastressourceid) + ")"
            query = self.dbase.query(sql)
            self.dbase.commit()
    """

    """
    def deleteParentFeature(self):

        sql = "SELECT pk_objet, pk_ressource, id_ressource FROM Rapport_qgis WHERE pk_rapport= " + str(self.currentFeaturePK)
        pkobjet, pkressource, idressource = self.dbase.query(sql)[0]
        #idobjet = self.currentFeature['id_objet']
        #idressource = self.currentFeature['id_ressource']

        sql = "DELETE FROM Objet WHERE pk_objet = " + str(pkobjet)
        query = self.dbase.query(sql)
        self.dbase.commit()

        sql = "DELETE FROM Ressource WHERE pk_ressource = " + str(pkressource)
        query = self.dbase.query(sql)
        self.dbase.commit()

        sql = "DELETE FROM Tcobjetressource WHERE id_tcressource = " + str(idressource)
        sql += " AND lpk_revision_begin <= " + str(self.dbase.maxrevision)
        sql += " AND lpk_revision_end IS  NULL "


        query = self.dbase.query(sql)
        self.dbase.commit()

        return True
    """



    def postSaveFeature(self, boolnewfeature):
        pass



class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabase_rapport_tool_ui.ui')
        uic.loadUi(uipath, self)