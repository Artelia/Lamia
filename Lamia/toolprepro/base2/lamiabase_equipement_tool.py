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
    from qgis.PyQt.QtGui import (QWidget, QVBoxLayout)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget, QVBoxLayout)
from qgis.PyQt.QtCore import Qt
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ...toolabstract.Lamia_abstract_tool import AbstractLamiaTool

from .lamiabase_photo_tool import BasePhotoTool
# from .lamiadigue_rapport_tool import RapportTool
# from .lamiadigue_tronconemprise_tool  import TronconEmpriseTool
from .lamiabase_croquis_tool import BaseCroquisTool
import os, logging, datetime

from ...toolgeneral.VoiceRecorder.main.AudioLogic.audioFactory import AudioFactory
from ...toolgeneral.VoiceRecorder.main.Ui.Widgets.RecorderWidget import RecorderWidget
from ...toolgeneral.VoiceRecorder.main.Ui.Controller.Mediator import Mediator

log = logging.getLogger("Lamia")
class BaseEquipementTool(AbstractLamiaTool):

    LOADFIRST = True
    dbasetablename = 'Equipement'
    specialfieldui = []

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(BaseEquipementTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)
        
    def initTool(self):
        # ****************************************************************************************
        # Main spec

        log.debug("init equipement tool")
        self.CAT = 'Description'
        self.NAME = 'Equipement'
        self.dbasetablename = 'Equipement'
        self.PointENABLED = True
        self.LineENABLED = True
        # self.PolygonENABLED = True
        # self.magicfunctionENABLED = True
        self.linkagespec = {
            'Equipement': {
                'tabletc': None,
                'idsource': 'lid_descriptionsystem_1',
                'idtcsource': None,
                'iddest': 'id_descriptionsystem',
                'idtcdest': None,
                'desttable': [
                        'Equipement',
                        'Noeud',
                        'Infralineaire'
                ]
            }
        }
        # self.pickTable = None
        self.debug = False
        self.iconpath = os.path.join(os.path.dirname(__file__), 'lamiabase_equipement_tool_icon.svg')

        # ****************************************************************************************
        #properties ui        

    def initFieldUI(self):
        # ****************************************************************************************
        #   userui Field
        if self.userwdgfield is None:
            # ****************************************************************************************
            # userui
            log.debug("init field UI")
            self.recorder = AudioFactory.create("recorder")                             
            self.mediator = Mediator.getinstance()
            self.mediator.connect("stream_stop", self.saveFeature)            
            self.userwdgfield = UserUI(RecorderWidget(self.recorder, self.mediator))            
            
            self.linkuserwdgfield = {
                "Equipement":{
                    "linkfield":"id_equipement",
                    "widgets":{
                        "categorie":"self.userwdgfield.comboBox_cat"
                    }
                },
                "Objet":{
                    "linkfield":"id_objet",
                    "widgets": {
                        "commentaire":"self.userwdgfield.textBrowser_comm",
                        "vocal": "self.userwdgfield.recorderWidget"
                    }
                },
                "Descriptionsystem":{
                    "linkfield":"id_descriptionsystem",
                    "widgets":{

                    }
                }
            }
            self.userwdgfield.comboBox_cat.currentIndexChanged.connect(self.changeCategorie)            

            # ****************************************************************************************
            # child widgets
            self.dbasechildwdgfield = []

            if self.parentWidget is None:
                self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(dbase=self.dbase, gpsutil=self.gpsutil, parentwidget=self)
                self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)

                self.propertieswdgCROQUIS = BaseCroquisTool(dbase=self.dbase, parentwidget=self)
                self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)




    def changeCategorie(self,intcat):

        pagecount = self.userwdg.stackedWidget.count()
        if intcat >= pagecount -1 :
            self.userwdg.stackedWidget.setCurrentIndex(pagecount -1)
        else:
            self.userwdg.stackedWidget.setCurrentIndex(intcat)


    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass


    def postloadIds(self,sqlin):
        strid = 'id_' + self.dbasetablename.lower()
        sqlin += ' ORDER BY ' + strid
        return sqlin



    def postInitFeatureProperties(self, feat):
        pass

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
        pkequip = self.currentFeaturePK
        lastidequip = self.dbase.getLastId('Equipement') + 1
        sql = "UPDATE Equipement SET id_equipement = " + str(lastidequip) + ","
        sql += "lpk_descriptionsystem = " + str(pksys)
        sql += " WHERE pk_equipement = " + str(pkequip) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()

        if  self.parentWidget is not None and self.parentWidget.currentFeature is not None:
            # if "lid_descriptionsystem" in self.dbase.dbasetables[self.parentWidget.dbasetablename]['fields'].keys():
            if 'Descriptionsystem' in self.dbase.getParentTable(self.parentWidget.dbasetablename):

                #parentid
                sql = "SELECT id_descriptionsystem FROM " + self.parentWidget.dbasetablename.lower() + "_qgis"
                sql += " WHERE pk_" + self.parentWidget.dbasetablename.lower() + " = " + str(self.parentWidget.currentFeaturePK)
                parentid = self.dbase.query(sql)[0][0]
                #currentparentlinkfield = self.parentWidget.currentFeature['id_descriptionsystem']
                sql = "UPDATE Equipement SET lid_descriptionsystem_1 = " + str(parentid)
                sql += " WHERE pk_equipement = " + str(pkequip)
                self.dbase.query(sql)
                self.dbase.commit()







    def postSaveFeature(self, boolnewfeature):
        pass


    def deleteParentFeature(self):

        sql = "SELECT pk_objet, pk_descriptionsystem FROM Equipement_qgis WHERE pk_equipement = " + str(self.currentFeaturePK)
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



class UserUI(QWidget):

    def __init__(self, widget, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabase_equipement_tool_ui.ui')
        uic.loadUi(uipath, self)
        self._layout = QVBoxLayout()
        self._layout.setAlignment(Qt.AlignVCenter)
        self._layout.addWidget(widget)
        # self.setLayout(self._layout)
        # self.focusWidget()
        self.recorderWidget.setLayout(self._layout)        
        log.debug("Set Layout")