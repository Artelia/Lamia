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
    from qgis.PyQt.QtGui import (QWidget, QLabel, QFrame)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget, QLabel, QFrame)

from ...lamia_abstractformtool import AbstractLamiaFormTool

from .lamiabase_photo_tool import BasePhotoTool
from .lamiabase_croquis_tool import BaseCroquisTool

import os
import datetime
import logging
import time
debugtime = False



class BaseInfraLineaireTool(AbstractLamiaFormTool):

    PREPROTOOLNAME = 'Infralineaire'
    DBASETABLENAME = 'Infralineaire'
    LOADFIRST = True

    tooltreewidgetCAT = 'Description'
    tooltreewidgetSUBCAT = 'Troncon'
    tooltreewidgetICONPATH = os.path.join(os.path.dirname(__file__), 'lamiabase_infralineaire_tool_icon.svg')


    def __init__(self, **kwargs):
        super(BaseInfraLineaireTool, self).__init__(**kwargs)
        self.instancekwargs = kwargs

    def initTool(self):
        # ****************************************************************************************
        # Main spec
        #timestart = self.dbase.getTimeNow()
        #if debugtime: logging.getLogger('Lamia').debug('Start init %s',str(round(self.dbase.getTimeNow()  - timestart, 3)))

        self.CAT = 'Description'
        self.NAME = 'Troncon'
        self.dbasetablename = 'Infralineaire'
        # self.visualmode = [0, 1, 2]
        # self.PointEnabled = True
        self.LineENABLED = True
        # self.PolygonEnabled = True
        # self.magicfunctionENABLED = True
        self.linkagespec = {'Tcobjetintervenant' : {'tabletc' : 'Tcobjetintervenant',
                                              'idsource' : 'id_objet',
                                            'idtcsource' : 'id_tcobjet',
                                           'iddest' : 'id_intervenant',
                                           'idtcdest' : 'id_tcintervenant',
                                           'desttable' : ['Intervenant']}

                                            }
        self.pickTable = {'LkZoneGeo': {'ZONEGEO': 'ID'}}
        self.debug = False
        self.qtreewidgetfields = ['lpk_revision_begin']

        self.iconpath = os.path.join(os.path.dirname(__file__), 'lamiabase_infralineaire_tool_icon.svg')


        # ****************************************************************************************
        #properties ui
        pass

    def initMainToolWidget(self):
        # ****************************************************************************************
        #   userui Field

        self.toolwidgetmain = UserUIField()

        self.formtoolwidgetconfdictmain = {'Infralineaire': {'linkfield': 'id_infralineaire',
                                                    'widgets': {}},
                                            'Objet': {'linkfield': 'id_objet',
                                                    'widgets': {'libelle': self.toolwidgetmain.lineEdit_nom,
                                                                'commentaire': self.toolwidgetmain.textBrowser_commentaire}},
                                            'Descriptionsystem': {'linkfield': 'id_descriptionsystem',
                                                                'widgets': {}}}

        self.dbasechildwdgfield = []
        self.instancekwargs['parentwidget'] = self
        #if self.parentWidget is None:
        self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)


        self.propertieswdgCROQUIS = BaseCroquisTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)


    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass

    def postloadIds(self,sqlin):
        strid = 'id_' + self.DBASETABLENAME.lower()
        sqlin += ' ORDER BY ' + strid
        return sqlin



    def postInitFeatureProperties(self, feat):
        pass

    def createParentFeature(self):
        pkobjet = self.dbase.createNewObjet()

        if False:

            # lastrevision = self.dbase.maxrevision
            #datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
            datecreation =  str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            lastobjetid = self.dbase.getLastId('Objet') + 1
            sql = "INSERT INTO Objet (id_objet, lpk_revision_begin, datetimecreation ) "
            sql += "VALUES(" + str(lastobjetid ) + "," + str(self.dbase.maxrevision) +  ",'" + datecreation + "');"
            query = self.dbase.query(sql)
            self.dbase.commit()
            pkobjet = self.dbase.getLastRowId('Objet')



        #sql = "INSERT INTO Descriptionsystem (id_objet) VALUES(" + str(idobjet) + ");"
        lastdescriptionsystemid = self.dbase.getLastId('Descriptionsystem') + 1
        sql = "INSERT INTO Descriptionsystem (id_descriptionsystem, lpk_objet) "
        sql += "VALUES(" + str(lastdescriptionsystemid) +   "," + str(pkobjet) + ");"
        query = self.dbase.query(sql)
        self.dbase.commit()
        pksys = self.dbase.getLastRowId('Descriptionsystem')

        #idnoeud = self.currentFeature.id()
        pkinfra = self.currentFeaturePK
        lastidinfra = self.dbase.getLastId('Infralineaire') + 1
        sql = "UPDATE Infralineaire SET id_infralineaire = " + str(lastidinfra)  + ","
        sql += "lpk_descriptionsystem = " + str(pksys)
        sql += " WHERE pk_infralineaire = " + str(pkinfra) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()



    def deleteParentFeature(self):

        sql = "SELECT pk_objet, pk_descriptionsystem FROM Infralineaire_qgis WHERE pk_infralineaire = " + str(self.currentFeaturePK)
        pkobjet, pkdes = self.dbase.query(sql)[0]
        #idobjet = self.currentFeature['id_objet']
        #idressource = self.currentFeature['id_ressource']

        sql = "DELETE FROM Objet WHERE pk_objet = " + str(pkobjet)
        query = self.dbase.query(sql)
        self.dbase.commit()

        sql = "DELETE FROM Descriptionsystem WHERE pk_descriptionsystem = " + str(pkdes)
        query = self.dbase.query(sql)
        self.dbase.commit()



        return True




class UserUIField(QWidget):
    def __init__(self, parent=None):
        super(UserUIField, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabase_infralineaire_tool_ui.ui')
        uic.loadUi(uipath, self)

