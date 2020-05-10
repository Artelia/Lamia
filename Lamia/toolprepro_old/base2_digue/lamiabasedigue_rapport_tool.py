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




from qgis.PyQt import uic, QtCore, QtGui
try:
    from qgis.PyQt.QtGui import (QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget)
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..base2.lamiabase_rapport_tool import BaseRapportTool

import os
import datetime




class BaseDigueRapportTool(BaseRapportTool):

    LOADFIRST = False
    dbasetablename = 'Rapport'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None,gpsutil=None, parentwidget=None, parent=None):
        super(BaseDigueRapportTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil,parentwidget, parent=parent)

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
                                       'idtcsource' : 'id_tcressource',
                                           'iddest' : 'id_objet',
                                       'idtcdest' : 'id_tcobjet',
                                           'desttable' : ['Infralineaire','Equipement']},
                            'Marche': {'tabletc': None,
                                           'idsource': 'lk_marche',
                                           'idtcsource': None,
                                           'iddest': 'id_marche',
                                           'idtcdest': None,
                                           'desttable': ['Marche']}}

        # ****************************************************************************************
        #properties ui
        self.iconpath = os.path.join(os.path.dirname(__file__), 'lamiadefault_rapport_tool_icon.png')
        self.qtreewidgetfields = ['nomrapport']

    def initDesktopUI(self):
        # ****************************************************************************************
        # userui Desktop
        if self.userwdgdesktop is None:
            # ****************************************************************************************
            # userui
            self.userwdgdesktop = UserUI()
            self.userwdgdesktop.pushButton_chooseph.clicked.connect(self.choosePhoto)
            self.userwdgdesktop.pushButton_openph.clicked.connect(self.openFile)

            self.linkuserwdgdesktop = {'Rapport' : {'linkfield' : 'id_rapport',
                                             'widgets' : {'nomrapport' : self.userwdgdesktop.lineEdit_nom }},
                                'Objet' : {'linkfield' : 'id_objet',
                                          'widgets' : {}},
                                'Ressource' : {'linkfield' : 'id_ressource',
                                          'widgets' : {'file': self.userwdgdesktop.lineEdit_file,
                                                        'description': self.userwdgdesktop.lineEdit_description,
                                                        'dateressource': self.userwdgdesktop.dateEdit}}}

            # ****************************************************************************************
            # child widgets



    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass

    def openFile(self):
        filepath = self.completePathOfFile(self.userwdg.lineEdit_file.text())
        if filepath != '':
            os.startfile(filepath)


    def choosePhoto(self):
        file, extension = self.windowdialog.qfiledlg.getOpenFileNameAndFilter(None, 'Choose the file', self.dbase.imagedirectory,
                                                                 'All (*.*)', '')
        if file:
            self.userwdg.lineEdit_file.setText(os.path.normpath(file))


    def postInitFeatureProperties(self, feat):
        if self.currentFeature is None:
            datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
            self.initFeatureProperties(feat, 'Ressource', 'dateressource', datecreation)



    def createParentFeature(self):

        lastrevision = self.dbase.getLastPk('Revision')
        datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
        lastobjetid = self.dbase.getLastId('Objet') + 1
        sql = "INSERT INTO Objet (id_objet, id_revisionbegin, datecreation ) "
        sql += "VALUES(" + str(lastobjetid ) + "," + str(lastrevision) +  ",'" + datecreation + "');"
        query = self.dbase.query(sql)
        self.dbase.commit()
        #idobjet = self.dbase.getLastRowId('Objet')


        lastressourceid = self.dbase.getLastId('Ressource') + 1
        sql = "INSERT INTO Ressource (id_ressource, id_revisionbegin, id_objet) "
        sql += "VALUES(" + str(lastressourceid) + "," + str(lastrevision) +  "," + str(lastobjetid) + ");"
        query = self.dbase.query(sql)
        self.dbase.commit()


        idrapport = self.currentFeature.id()
        lastidrapport = self.dbase.getLastId('Rapport') + 1




        sql = "UPDATE Rapport SET id_objet = " + str(lastobjetid)  + ","
        sql += "id_ressource = " + str(lastressourceid)   + ","
        sql += "id_rapport = " + str(lastidrapport)  + ","
        sql += "id_revisionbegin = " + str(lastrevision)
        sql += " WHERE pk_rapport = " + str(idrapport) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()



        # self.initLinkageFromGeometry('Tcobjetressource',idres)



    def postSaveFeature(self, boolnewfeature):
        pass
    """

"""
class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiadefault_rapport_tool_ui.ui')
        uic.loadUi(uipath, self)
"""