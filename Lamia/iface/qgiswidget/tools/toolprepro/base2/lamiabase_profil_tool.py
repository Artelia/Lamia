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
    from qgis.PyQt.QtGui import (QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget)
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ...toolabstract.Lamia_abstract_tool import AbstractLamiaTool
from .lamiabase_photo_tool import BasePhotoTool

from .lamiabase_croquis_tool import BaseCroquisTool
from .lamiabase_graphique_tool import BaseGraphiqueTool

import os
import datetime




class BaseProfilTool(AbstractLamiaTool):

    LOADFIRST = False
    dbasetablename = 'Profil'
    specialfieldui = []

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(BaseProfilTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)
        
    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Description'
        self.NAME = 'Profil'
        self.dbasetablename = 'Profil'
        self.visualmode = [1, 2]
        # self.PointEnabled = True
        self.LineENABLED = True
        # self.PolygonEnabled = True
        """
        self.linkagespec = {'Infralineaire' : {'tabletc' : None,
                                              'idsource' : 'lk_objet',
                                            'idtcsource' : None,
                                           'iddest' : 'id_objet',
                                           'idtcdest' : None,
                                           'desttable' : ['Infralineaire']} }
        """
        self.linkagespec = {'Infralineaire' : {'tabletc' : None,
                                              'idsource' : 'lid_descriptionsystem',
                                            'idtcsource' : None,
                                           'iddest' : 'id_descriptionsystem',
                                           'idtcdest' : None,
                                           'desttable' : ['Infralineaire']} }
        # self.pickTable = None
        self.iconpath = os.path.join(os.path.dirname(__file__), 'lamiabase_profil_tool_icon.svg')
        # ****************************************************************************************
        #properties ui
        pass

    def initFieldUI(self):
        # ****************************************************************************************
        #   userui Field
        if self.userwdgfield is None:
            # ****************************************************************************************
            # userui

            self.userwdgfield = UserUI()
            self.linkuserwdgfield = {'Profil' : {'linkfield' : 'id_profil',
                                             'widgets' : {'dateprofil': self.userwdgfield.dateEdit,
                                                          'type': self.userwdgfield.comboBox_type}},
                                'Objet' : {'linkfield' : 'id_objet',
                                          'widgets' : {}},
                                'Descriptionsystem' : {'linkfield' : 'id_descriptionsystem',
                                          'widgets' : {}}}

            self.userwdgfield.comboBox_type.currentIndexChanged.connect(self.changeType)


            # ****************************************************************************************


            # ****************************************************************************************
            # child widgets
            self.dbasechildwdgfield = []

            if True:
                self.propertieswdgGRAPH = BaseGraphiqueTool(dbase=self.dbase, parentwidget=self)
                self.propertieswdgGRAPH.NAME = None
                #self.userwdgfield.tabWidget.widget(0).layout().addWidget(self.propertieswdgCROQUIS)
                #self.userwdgfield.frame_graph.layout().addWidget(self.propertieswdgGRAPH)
                self.userwdgfield.stackedWidget.widget(0).layout().addWidget(self.propertieswdgGRAPH)
                self.dbasechildwdgfield.append(self.propertieswdgGRAPH)



            if True:
                self.propertieswdgCROQUIS = BaseCroquisTool(dbase=self.dbase, parentwidget=self)
                self.propertieswdgCROQUIS.NAME = None
                #self.userwdgfield.tabWidget.widget(0).layout().addWidget(self.propertieswdgCROQUIS)
                #self.userwdgfield.frame_cr.layout().addWidget(self.propertieswdgCROQUIS)
                self.userwdgfield.stackedWidget.widget(1).layout().addWidget(self.propertieswdgCROQUIS)
                self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

            if True:
                self.propertieswdgPHOTO = BasePhotoTool(dbase=self.dbase, parentwidget=self)
                self.propertieswdgPHOTO.NAME = None
                #self.userwdgfield.tabWidget.widget(0).layout().addWidget(self.propertieswdgCROQUIS)
                #self.userwdgfield.frame_cr.layout().addWidget(self.propertieswdgPHOTO)
                self.userwdgfield.stackedWidget.widget(2).layout().addWidget(self.propertieswdgPHOTO)
                self.dbasechildwdgfield.append(self.propertieswdgPHOTO)





    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass

    def setAsDefault(self):
        if self.parentWidget.currentFeature is not None:
            if self.userwdgfield.stackedWidget.currentIndex() == 0:
                currentwdg = self.propertieswdgCROQUIS
            elif self.userwdgfield.stackedWidget.currentIndex() == 1:
                currentwdg = self.propertieswdgGRAPH

            if currentwdg.currentFeature is not None:
                #idressoruce
                sql = "SELECT id_ressource FROM " + currentwdg.dbasetablename.lower() + "_qgis"
                sql += " WHERE pk_" + currentwdg.dbasetablename.lower() + " = " + str(self.currentwdg.currentFeaturePK)
                idressource = self.dbase.query(sql)[0][0]

                pkparentfeature = self.parentWidget.currentFeaturePK

                sql = "UPDATE " + str(self.parentWidget.dbasetablename.lower()) + " SET  lid_ressource_4 = " + str(idressource)
                sql += " WHERE pk_"+ str(self.parentWidget.dbasetablename.lower()) + " = " + str(pkparentfeature)

                if False:
                    idressource = currentwdg.currentFeature['id_ressource']
                    idparentfeature=self.parentWidget.currentFeature['id_objet']
                    # print('setDefaultPhoto',idphoto,idparentfeature)
                    sql = "UPDATE " + str(self.parentWidget.dbasetablename) + " SET  lk_profil = " + str(idressource) + " WHERE id_objet = " + str(idparentfeature) + ";"

                query = self.dbase.query(sql)
                self.dbase.commit()

    def changeType(self,comboint):
        self.userwdgfield.stackedWidget.setCurrentIndex(comboint)


    def postInitFeatureProperties(self, feat):
        if self.currentFeature is None:
            #datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
            #self.initFeatureProperties(feat, 'Date', datecreation)

            datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
            self.initFeatureProperties(feat, self.dbasetablename, 'date', datecreation)

            if self.parentWidget is not None:
                if self.parentWidget.dbasetablename == 'Infralineaire' and self.parentWidget.currentFeature is not None:
                    #parent id_dessys
                    sql = "SELECT id_descriptionsystem FROM Infralineaire_qgis WHERE pk_infralineaire = " + str(self.parentWidget.currentFeaturePK)
                    pkdessys = self.dbase.query(sql)[0][0]
                    self.initFeatureProperties(self.currentFeature,'Profil', 'lid_descriptionsystem', pkdessys)


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

        # sql = "INSERT INTO Descriptionsystem (id_objet) VALUES(" + str(idobjet) + ");"
        lastdescriptionsystemid = self.dbase.getLastId('Descriptionsystem') + 1
        sql = "INSERT INTO Descriptionsystem (id_descriptionsystem, lpk_objet) "
        sql += "VALUES(" + str(lastdescriptionsystemid) + "," + str(pkobjet) + ");"
        query = self.dbase.query(sql)
        self.dbase.commit()
        pksys = self.dbase.getLastRowId('Descriptionsystem')

        # idnoeud = self.currentFeature.id()
        pkprofil = self.currentFeaturePK
        lastidprofil = self.dbase.getLastId('Profil') + 1
        sql = "UPDATE Profil SET id_profil = " + str(lastidprofil) + ","
        sql += "lpk_descriptionsystem = " + str(pksys)
        sql += " WHERE pk_profil = " + str(pkprofil)
        query = self.dbase.query(sql)
        self.dbase.commit()



        if self.parentWidget is not None and self.parentWidget.currentFeature is not None:
            if self.parentWidget.dbasetablename == 'Infralineaire':
                # print(self.parentWidget.currentFeature.attributes())
                #currentparentlinkfield = self.parentWidget.currentFeature['id_descriptionsystem']
                #currentparentlinkfield
                sql = "SELECT id_descriptionsystem FROM Profil_qgis WHERE pk_profil = " + str(pkprofil)
                currentparentlinkfield = self.dabse.query(sql)[0][0]

                sql = "UPDATE Profil SET lid_descriptionsystem = " + str(currentparentlinkfield) + " WHERE pk_profil = " + str(pkprofil) + ";"
                query = self.dbase.query(sql)
                self.dbase.commit()





    def postSaveFeature(self, boolnewfeature):
        pass





class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabase_profil_tool_ui.ui')
        uic.loadUi(uipath, self)
