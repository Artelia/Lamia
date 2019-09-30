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
    from qgis.PyQt.QtGui import (QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget)
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ...toolabstract.Lamia_abstract_tool import AbstractLamiaTool

from .lamiabase_observation_tool import BaseObservationTool
import os
import datetime
import qgis




class BaseDesordreTool(AbstractLamiaTool):

    LOADFIRST = True
    dbasetablename = 'Desordre'
    specialfieldui = []

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None, parentwidget=None, parent=None):
        super(BaseDesordreTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)
        
    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Desordre'
        self.NAME = 'Desordre'
        self.dbasetablename = 'Desordre'
        #self.visualmode = [1, 2]
        self.PointENABLED = True
        self.LineENABLED = True
        # self.PolygonEnabled = True
        self.magicfunctionENABLED = True
        """
        self.linkagespec = {'Tcdesordredescriptionsystem' : {'tabletc' : 'Tcdesordredescriptionsystem',
                                              'idsource' : 'id_desordre',
                                            'idtcsource' : 'id_tcdesordre',
                                           'iddest' : 'id_descriptionsystem',
                                           'idtcdest' : 'id_tcdescriptionsystem',
                                           'desttable' : ['Infralineaire']}}
        """
        self.linkagespec = {'Descriptionsystem' : {'tabletc' : None,
                                              'idsource' : 'lid_descriptionsystem',
                                            'idtcsource' : None,
                                           'iddest' : 'id_descriptionsystem',
                                           'idtcdest' : None,
                                           'desttable' : ['Infralineaire','Equipement','Noeud']}}


        self.pickTable = {'LkDesSys': {'TRONCON': 'IdSys'}}
        self.iconpath = os.path.join(os.path.dirname(__file__), 'lamiabase_desordre_tool_icon.png')

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

            self.linkuserwdgfield = {'Desordre' : {'linkfield' : 'id_desordre',
                                             'widgets' : {'groupedesordre': self.userwdgfield.comboBox_groupedes
                                                          }},
                                'Objet' : {'linkfield' : 'id_objet',
                                          'widgets' : {}}}

            self.userwdgfield.comboBox_groupedes.currentIndexChanged.connect(self.changeGroupe)


            # ****************************************************************************************
            # child widgets
            self.dbasechildwdgfield = []

            if self.parentWidget is None :

                self.propertieswdgOBSERVATION = BaseObservationTool(dbase=self.dbase, parentwidget=self)
                self.dbasechildwdgfield.append(self.propertieswdgOBSERVATION)


            self.propertieswdgOBSERVATION2 = BaseObservationTool(dbase=self.dbase, parentwidget=self)
            self.propertieswdgOBSERVATION2.NAME = None
            self.userwdgfield.tabWidget.widget(0).layout().addWidget(self.propertieswdgOBSERVATION2)
            self.dbasechildwdgfield.append(self.propertieswdgOBSERVATION2)

            self.userwdgfield.tabWidget.widget(1).layout().addWidget(self.propertieswdgOBSERVATION2.propertieswdgPHOTOGRAPHIE)
            self.userwdgfield.tabWidget.widget(2).layout().addWidget(self.propertieswdgOBSERVATION2.propertieswdgCROQUIS)



    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass

    def magicFunction(self):
        self.featureSelected()
        self.addGPSPoint()
        self.saveFeature()
        self.propertieswdgOBSERVATION2.featureSelected()
        self.propertieswdgOBSERVATION2.saveFeature()


    def postInitFeatureProperties(self, feat):
        if feat is not None:
            self.userwdgfield.comboBox_groupedes.setEnabled(False)
        else:
            self.userwdgfield.comboBox_groupedes.setEnabled(True)


    def changeGroupe(self,intcat):
        self.userwdg.stackedWidget.setCurrentIndex(intcat)


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
        pkdesordre = self.currentFeaturePK
        lastiddes = self.dbase.getLastId('Desordre') + 1
        sql = "UPDATE Desordre SET id_desordre = " + str(lastiddes) + ","
        sql += "lpk_objet = " + str(pkobjet)
        sql += " WHERE pk_desordre = " + str(pkdesordre) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()



        if self.parentWidget is not None and self.parentWidget.currentFeature is not None:
            #currentparentlinkfield = self.parentWidget.currentFeature['id_descriptionsystem']

            #parent id_descriptionsystem
            sqltemp = "SELECT id_descriptionsystem FROM " + self.parentWidget.dbasetablename.lower() + "_qgis"
            sqltemp += " WHERE pk_"+ self.parentWidget.dbasetablename.lower() + " = " + str(self.parentWidget.currentFeaturePK)
            result = self.dbase.query(sqltemp)

            if result is not None:
                currentparentlinkfield = result[0][0]

                sql = "UPDATE Desordre SET lid_descriptionsystem = " + str(currentparentlinkfield)

                if self.parentWidget.dbasetablename in ['Infralineaire']:
                    sql += ",groupedesordre = 'INF'"
                elif self.parentWidget.dbasetablename in ['Noeud']:
                    sql += ",groupedesordre = 'NOD'"
                elif self.parentWidget.dbasetablename in ['Equipement']:
                    sql += ",groupedesordre = 'EQP'"
                else:
                    sql += ",groupedesordre = 'INF'"
                sql += " WHERE pk_desordre = " + str(pkdesordre)
                self.dbase.query(sql)
                self.dbase.commit()

            else:
                sql = "UPDATE Desordre SET groupedesordre = 'INF'  WHERE pk_desordre = " + str(pkdesordre)
                self.dbase.query(sql)
                self.dbase.commit()

        else:
            sql = "UPDATE Desordre SET groupedesordre = 'INF'  WHERE pk_desordre = " + str(pkdesordre)
            self.dbase.query(sql)
            self.dbase.commit()



    def postSaveFeature(self, boolnewfeature):
        pass


    def deleteParentFeature(self):


        sql = "SELECT pk_objet FROM Desordre_qgis WHERE pk_desordre = " + str(self.currentFeaturePK)
        pkobjet = self.dbase.query(sql)[0][0]
        #idobjet = self.currentFeature['id_objet']
        #idressource = self.currentFeature['id_ressource']

        sql = "DELETE FROM Objet WHERE pk_objet = " + str(pkobjet)
        query = self.dbase.query(sql)
        self.dbase.commit()

        sql = "SELECT id_desordre FROM Desordre WHERE pk_desordre = " + str(self.currentFeaturePK)
        iddesordre = self.dbase.query(sql)[0][0]

        sql = "DELETE FROM Observation WHERE lid_desordre = " + str(iddesordre)
        self.dbase.query(sql)


        if False:
            idobjet = self.currentFeature['id_objet']

            sql = "DELETE FROM Objet WHERE id_objet = " + str(idobjet) + ";"
            query = self.dbase.query(sql)
            self.dbase.commit()

            sql = "DELETE FROM Descriptionsystem WHERE id_objet = " + str(idobjet) + ";"
            query = self.dbase.query(sql)
            self.dbase.commit()

            iddesordre = self.currentFeature['id_desordre']
            sql = "DELETE FROM Observation WHERE lk_desordre = " +str(iddesordre)

        return True


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabase_desordre_tool_ui.ui')
        uic.loadUi(uipath, self)
