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



from ..base2.lamiabase_desordre_tool import BaseDesordreTool
from .lamiabaseparking_observation_tool import BaseParkingObservationTool


import os
import datetime
import qgis




class BaseParkingDesordreTool(BaseDesordreTool):

    #LOADFIRST = True
    dbasetablename = 'Desordre'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None, parentwidget=None, parent=None):
        super(BaseParkingDesordreTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)

    def initTool(self):
        super(BaseParkingDesordreTool, self).initTool()
        self.NAME = 'Campagne de reconnaissance'
        #self.qtreewidgetfields = ['libelle']
        #self.linkedgeom = [['Desordre', 'lid_descriptionsystem']]
        self.visualmode = [1]

    """
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

        self.linkagespec = {'Descriptionsystem' : {'tabletc' : None,
                                              'idsource' : 'lk_descriptionsystem',
                                            'idtcsource' : None,
                                           'iddest' : 'id_descriptionsystem',
                                           'idtcdest' : None,
                                           'desttable' : ['Infralineaire','Equipement','Noeud']}}


        self.pickTable = {'LkDesSys': {'TRONCON': 'IdSys'}}
        self.iconpath = os.path.join(os.path.dirname(__file__), 'lamiadefault_desordre_tool_icon.png')

        # ****************************************************************************************
        #properties ui
        pass
    """

    def initFieldUI(self):
        # ****************************************************************************************
        #   userui Field
        if self.userwdgfield is None:
            # ****************************************************************************************
            # userui

            self.userwdgfield = UserUI()

            self.linkuserwdgfield = {'Desordre' : {'linkfield' : 'id_desordre',
                                             'widgets' : {'groupedesordre': self.userwdgfield.comboBox_groupedes,
                                                          'numrotation': self.userwdgfield.spinBox_num_rot
                                                          }},
                                'Objet' : {'linkfield' : 'id_objet',
                                          'widgets' : {}}}

            self.userwdgfield.frame_2.setParent(None)
            self.groupBox_geom.setParent(None)
            #self.userwdgfield.stackedWidget.setParent(None)

            self.userwdgfield.toolButton_num_rot.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.spinBox_num_rot))


            #self.userwdgfield.comboBox_groupedes.currentIndexChanged.connect(self.changeGroupe)
            # ****************************************************************************************
            # child widgets
            self.dbasechildwdgfield = []
            if True:
                if False and self.parentWidget is None :

                    self.propertieswdgOBSERVATION = BaseParkingObservationTool(dbase=self.dbase, parentwidget=self)
                    self.dbasechildwdgfield.append(self.propertieswdgOBSERVATION)


                self.propertieswdgOBSERVATION2 = BaseParkingObservationTool(dbase=self.dbase, parentwidget=self)
                self.propertieswdgOBSERVATION2.NAME = None
                self.userwdgfield.tabWidget.widget(0).layout().addWidget(self.propertieswdgOBSERVATION2)
                self.dbasechildwdgfield.append(self.propertieswdgOBSERVATION2)

                self.userwdgfield.tabWidget.widget(1).layout().addWidget(self.propertieswdgOBSERVATION2.propertieswdgPHOTOGRAPHIE)
                self.userwdgfield.tabWidget.widget(2).layout().addWidget(self.propertieswdgOBSERVATION2.propertieswdgCROQUIS)



    def postSaveFeature(self, boolnewfeature):
        pass


    """
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


    """
    def postInitFeatureProperties(self, feat):

        self.updateDateCampagne()

        if feat is  None and self.parentWidget is not None and self.parentWidget.currentFeature is not None:
            if self.parentWidget.dbasetablename in ['Infralineaire']:
                parentgeom = self.parentWidget.currentFeature.geometry()
                # print(parentgeom.asPolyline())
                self.setTempGeometry(parentgeom.asPolyline(),comefromcanvas=False, showinrubberband=False)


    def updateDateCampagne(self):
        if self.currentFeature is not None:
            liddesordre = self.dbase.getValuesFromPk('Desordre_qgis',
                                                     ['id_desordre'],
                                                     self.currentFeaturePK)
            if not liddesordre:
                self.resetCampagneDateTime()
                return


            sql = "SELECT MIN(datetimeobservation), MAX(datetimeobservation) FROM Observation"
            sql += " WHERE lid_desordre = " + str(liddesordre)
            res = self.dbase.query(sql)

            if res:
                mindate, maxdate = res[0]
                if mindate and maxdate:
                    self.userwdgfield.dateTimeEdit_start.setDateTime(QtCore.QDateTime.fromString(mindate, 'yyyy-MM-dd hh:mm:ss'))
                    self.userwdgfield.dateTimeEdit_end.setDateTime(QtCore.QDateTime.fromString(maxdate, 'yyyy-MM-dd hh:mm:ss'))
                else:
                    self.resetCampagneDateTime()
            else:
                self.resetCampagneDateTime()
        else:
            self.resetCampagneDateTime()



    def resetCampagneDateTime(self):
        self.userwdgfield.dateTimeEdit_start.setSpecialValueText(" ")
        self.userwdgfield.dateTimeEdit_start.setDateTime(QtCore.QDateTime.fromString("01/01/0001 00:00:00", "dd/MM/yyyy hh:mm:ss"))
        self.userwdgfield.dateTimeEdit_end.setSpecialValueText(" ")
        self.userwdgfield.dateTimeEdit_end.setDateTime(QtCore.QDateTime.fromString("01/01/0001 00:00:00", "dd/MM/yyyy hh:mm:ss"))

    """


    def createParentFeature(self):
        lastrevision = self.dbase.getLastPk('Revision')
        datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
        lastobjetid = self.dbase.getLastId('Objet') + 1
        sql = "INSERT INTO Objet (id_objet, id_revisionbegin, datecreation ) "
        sql += "VALUES(" + str(lastobjetid ) + "," + str(lastrevision) +  ",'" + datecreation + "');"
        query = self.dbase.query(sql)
        self.dbase.commit()

        pkdesordre = self.currentFeature.id()
        lastiddesordre = self.dbase.getLastId('Desordre') + 1

        sql = "UPDATE Desordre SET id_objet = " + str(lastobjetid)  + ","
        sql += "id_desordre = " + str(lastiddesordre) + ","
        sql += "id_revisionbegin = " + str(lastrevision)
        sql += " WHERE pk_desordre = " + str(pkdesordre) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()

        if self.parentWidget is not None and self.parentWidget.currentFeature is not None:

            currentparentlinkfield = self.parentWidget.currentFeature['id_descriptionsystem']
            sql = "UPDATE Desordre SET lk_descriptionsystem = " + str(currentparentlinkfield)

            if self.parentWidget.dbasetablename in ['Infralineaire']:
                sql += ',groupedesordre = INF'
            elif self.parentWidget.dbasetablename in ['Noeud']:
                sql += ',groupedesordre = NOD'
            elif self.parentWidget.dbasetablename in ['Equipement']:
                sql += ',groupedesordre = EQP'
            else:
                sql += ',groupedesordre = INF'
            sql += " WHERE pk_desordre = " + str(pkdesordre)
            self.dbase.query(sql)
            self.dbase.commit()

        else:
            sql = "UPDATE Desordre SET groupedesordre = 'INF'  WHERE pk_desordre = " + str(pkdesordre)
            self.dbase.query(sql)
            self.dbase.commit()



    def postSaveFeature(self, boolnewfeature):
        pass

    """

class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabaseparking_desordre_tool_ui.ui')
        uic.loadUi(uipath, self)
