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
import qgis
try:
    from qgis.PyQt.QtGui import (QWidget, QVBoxLayout)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget, QVBoxLayout)
from qgis.PyQt.QtCore import Qt
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..base2.lamiabase_equipement_tool import BaseEquipementTool

from .lamiabasedigue_photo_tool import BaseDiguePhotoTool as BasePhotoTool
#from ..base.lamiabase_croquis_tool import BaseCroquisTool
from .lamiabasedigue_croquis_tool import BaseCroquisTool
from .lamiabasedigue_desordre_tool import BaseDigueDesordreTool


import os, logging, datetime

from ...toolgeneral.VoiceRecorder.main.AudioLogic.audioFactory import AudioFactory
from ...toolgeneral.VoiceRecorder.main.Ui.Widgets.RecorderWidget import RecorderWidget
from ...toolgeneral.VoiceRecorder.main.Ui.Controller.Mediator import Mediator

log = logging.getLogger("Lamia")
class BaseDigueEquipementTool(BaseEquipementTool):

    LOADFIRST = True
    dbasetablename = 'Equipement'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(BaseDigueEquipementTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)




    def initTool(self):
        super(BaseDigueEquipementTool,self).initTool()
        self.linkedgeom = [['Desordre', 'lid_descriptionsystem']]



    def initFieldUI(self):
        # ****************************************************************************************
        #   userui Field
        if self.dbase.variante in [None, 'Lamia']:
            if self.userwdgfield is None:
                # ****************************************************************************************
                # userui
                log.debug("init field UI")
                self.recorder = AudioFactory.create("recorder")                             
                self.mediator = Mediator.getinstance()
                #self.mediator.connect("stream_stop", self.saveFeature)            
                self.userwdgfield = UserUI(RecorderWidget(self.recorder, self.mediator))                
                
                self.linkuserwdgfield = {
                    'Equipement' : {
                        'linkfield' : 'id_equipement',
                        'widgets' : {
                            'categorie': self.userwdgfield.comboBox_cat,
                            'cote': self.userwdgfield.comboBox_cote,
                            'position': self.userwdgfield.comboBox_position,
                            'typeequipement': self.userwdgfield.comboBox_type,
                            'implantation': self.userwdgfield.comboBox_implantation,
                            'ecoulement': self.userwdgfield.comboBox_ecoulement,
                            'utilisation': self.userwdgfield.comboBox_utilisation,
                            'dimverti': [
                                self.userwdgfield.doubleSpinBox_dimvert,
                                self.userwdgfield.doubleSpinBox_dimvert_2],
                            'dimhori': [
                                self.userwdgfield.doubleSpinBox_dimhoriz,
                                self.userwdgfield.doubleSpinBox_dimhoriz2],
                            'soustype': self.userwdgfield.comboBox_soustype,
                            'fildeau': self.userwdgfield.doubleSpinBox_fildeau,
                            'securite': self.userwdgfield.comboBox_securite,
                        }
                    },
                    'Objet' : {
                        'linkfield' : 'id_objet',
                        'widgets' : {
                            'commentaire': self.userwdgfield.textBrowser_comm
                        }
                    },
                    'Descriptionsystem' : {
                        'linkfield' : 'id_descriptionsystem',
                            'widgets' : {

                            }
                    }
                }
                                
                self.userwdgfield.comboBox_cat.currentIndexChanged.connect(self.changeCategorie)

                self.userwdgfield.toolButton_calch.clicked.connect(
                    lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_dimvert))
                self.userwdgfield.toolButton__calcv.clicked.connect(
                    lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_dimhoriz))

                self.userwdgfield.toolButton_calch_2.clicked.connect(
                    lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_dimvert_2))
                self.userwdgfield.toolButton_dimhoriz2.clicked.connect(
                    lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_dimhoriz2))
                self.userwdgfield.toolButton_fildeau.clicked.connect(
                    lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_fildeau))

                self.userwdgfield.comboBox_type.currentIndexChanged.connect(self.typeponctuelChanged)

                # ****************************************************************************************
                # child widgets

                self.dbasechildwdgfield = []

                # if True:

                if self.parentWidget is None:
                    self.propertieswdgDesordre = BaseDigueDesordreTool(dbase=self.dbase, gpsutil=self.gpsutil, parentwidget=self)
                    self.propertieswdgDesordre.userwdgfield.frame_2.setParent(None)
                    self.propertieswdgDesordre.pushButton_addFeature.setEnabled(False)
                    self.propertieswdgDesordre.pushButton_delFeature.setEnabled(False)
                    self.propertieswdgDesordre.comboBox_featurelist.setEnabled(False)
                    self.propertieswdgDesordre.groupBox_geom.setParent(None)
                    self.dbasechildwdgfield.append(self.propertieswdgDesordre)

                    self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(dbase=self.dbase, gpsutil=self.gpsutil, parentwidget=self)
                    self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)

                    self.propertieswdgCROQUIS = BaseCroquisTool(dbase=self.dbase, parentwidget=self)
                    self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

                    self.propertieswdgEQUIPEMENT = BaseDigueEquipementTool(dbase=self.dbase, parentwidget=self)
                    self.dbasechildwdgfield.append(self.propertieswdgEQUIPEMENT)


                    self.userwdgfield.comboBox_type.currentIndexChanged.connect(self.propertieswdgDesordre.propertieswdgOBSERVATION2.equipementTypeChanged)

        elif self.dbase.variante in ['SIRS']:
            if self.userwdgfield is None:
                # ****************************************************************************************
                # userui
                self.userwdgfield = UserUISirs()
                self.linkuserwdgfield = {
                    "Equipement":{
                        "linkfield":"id_equipement",
                        "widgets":{
                            "categorie":"self.userwdgfield.comboBox_cat",
                            "cote":"self.userwdgfield.comboBox_cote",
                            "position":"self.userwdgfield.comboBox_position",
                            "typeequipement":"self.userwdgfield.comboBox_type",
                            "implantation":"self.userwdgfield.comboBox_implantation",
                            "ecoulement":"self.userwdgfield.comboBox_ecoulement",
                            "utilisation":"self.userwdgfield.comboBox_utilisation",
                            "dimverti":"self.userwdgfield.doubleSpinBox_dimvert",
                            "dimhori":"self.userwdgfield.doubleSpinBox_dimhoriz",
                            "securite":"self.userwdgfield.comboBox_securite",
                            "recorder": "self.userwdgfield.recorderWidget"
                        }
                    },
                    "Objet":{
                        "linkfield":"id_objet",
                        "widgets":{
                            "commentaire":"self.userwdgfield.textBrowser_comm"
                        }
                    },
                    "Descriptionsystem":{
                        "linkfield":"id_descriptionsystem",
                        "widgets":{

                        }
                    }
                }
                self.userwdgfield.comboBox_cat.currentIndexChanged.connect(self.changeCategorie)
                self.userwdgfield.toolButton_calch.clicked.connect(
                    lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_dimvert))
                self.userwdgfield.toolButton__calcv.clicked.connect(
                    lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_dimhoriz))

                # ****************************************************************************************
                # child widgets

                self.dbasechildwdgfield = []

                # if True:

                if self.parentWidget is None:
                    self.propertieswdgDesordre = BaseDigueDesordreTool(dbase=self.dbase, gpsutil=self.gpsutil,
                                                                       parentwidget=self)
                    self.propertieswdgDesordre.userwdgfield.frame_2.setParent(None)
                    self.propertieswdgDesordre.pushButton_addFeature.setEnabled(False)
                    self.propertieswdgDesordre.pushButton_delFeature.setEnabled(False)
                    self.propertieswdgDesordre.comboBox_featurelist.setEnabled(False)
                    self.propertieswdgDesordre.groupBox_geom.setParent(None)
                    self.dbasechildwdgfield.append(self.propertieswdgDesordre)

                    self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(dbase=self.dbase, gpsutil=self.gpsutil,
                                                                   parentwidget=self)
                    self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)

                    self.propertieswdgCROQUIS = BaseCroquisTool(dbase=self.dbase, parentwidget=self)
                    self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

                    self.propertieswdgEQUIPEMENT = BaseDigueEquipementTool(dbase=self.dbase, parentwidget=self)
                    self.dbasechildwdgfield.append(self.propertieswdgEQUIPEMENT)

                    self.userwdgfield.comboBox_type.currentIndexChanged.connect(
                        self.propertieswdgDesordre.propertieswdgOBSERVATION2.equipementTypeChanged)


    def postSaveFeature(self, boolnewfeature):

        # save a disorder on first creation
        if self.savingnewfeature and self.savingnewfeatureVersion == False:
            # categorie
            sql = "SELECT Categorie FROM Equipement WHERE pk_equipement = " + str(self.currentFeaturePK)
            categ = self.dbase.query(sql)[0][0]            
            if categ == 'OUH':
                pkobjet = self.dbase.createNewObjet()
                lastiddesordre = self.dbase.getLastId('Desordre') + 1
                geomtext, iddessys = self.dbase.getValuesFromPk('Equipement_qgis', ['ST_AsText(geom)', 'id_descriptionsystem'], self.currentFeaturePK)
                sql = self.dbase.createSetValueSentence(
                    type='INSERT',
                    tablename='Desordre',
                    listoffields=[
                        'id_desordre', 
                        'lpk_objet', 
                        'groupedesordre',
                        'lid_descriptionsystem', 
                        'geom'
                    ],
                    listofrawvalues=[
                        lastiddesordre,
                        pkobjet,
                        'EQP',
                        iddessys,
                        geomtext
                    ]
                )
                self.dbase.query(sql)

            currentrecording = self.recorder.currentrecording
            pkressource = self.dbase.getValuesFromPk('Audio_qgis', 'pk_ressource', self.currentFeaturePK)
            sqlquery = (
                "UPDATE Ressource "
                "SET file = '{0}' "            
                "WHERE pk_ressource = {1}"
            ).format(
                currentrecording.path + currentrecording.name + currentrecording.extension_type,
                pkressource
            )

            self.dbase.query(sqlquery)
            self.dbase.commit()


    def typeponctuelChanged(self, comboindex):
        if self.userwdgfield.comboBox_type.currentText() in ['Clapet', 'Vanne', 'Exutoire']:
            self.userwdgfield.stackedWidget_2.setCurrentIndex(0)
        else:
            self.userwdgfield.stackedWidget_2.setCurrentIndex(1)

    def changeCategorie(self,intcat):
        if 'Ponctuel' in self.userwdg.comboBox_cat.currentText():
            self.userwdg.stackedWidget.setCurrentIndex(1)
            self.pushButton_addPoint.setEnabled(True)
            self.pushButton_addLine.setEnabled(False)
        elif 'Lineaire' in self.userwdg.comboBox_cat.currentText():
            self.userwdg.stackedWidget.setCurrentIndex(0)
            self.pushButton_addPoint.setEnabled(False)
            self.pushButton_addLine.setEnabled(True)
        else:
            self.pushButton_addPoint.setEnabled(False)
            self.pushButton_addLine.setEnabled(False)



    def postInitFeatureProperties(self, feat):
        pass     

    def createParentFeature(self):
        #Insertion dans la table des ressource de  du lien à l'objet
        #INSERT INTO Ressource (id_ressource, lpk_objet) VALUES( str(lastressourceid) , str(pkobjet))
        pkobjet = self.dbase.createNewObjet()
        lastressourceid = self.dbase.getLastId('Ressource') + 1
        sqlquery = (
            "INSERT INTO Ressource (id_ressource, lpk_objet) "
            "VALUES ( {0}, {1})"
        ).format(
            lastressourceid,
            pkobjet
        )        
        self.dbase.query(sqlquery)
        self.dbase.commit()

        pkressource = self.dbase.getLastRowId('Ressource')
        pkaudio = self.currentFeaturePK
        lastidaudio = self.dbase.getLastId('Audio') + 1
        
        # Liaison de l'objet (ici de l'audio) à l'entrée précédente de la table ressource
        # UPDATE Audio SET id_audio = str(lastidaudio) ,lpk_ressource = str(pkres) WHERE pk_audio = str(pkaudio)
        sqlquery = (
            "UPDATE Audio SET id_audio = {0}, lpk_ressource = {1} "
            "WHERE pk_audio = {2}"
        ).format(
            lastidaudio,
            pkressource,
            pkaudio
        )        
        self.dbase.query(sqlquery)
        self.dbase.commit()
        
        # Ajout des référence pour le champs commentaire 
        sqlquery = (
            "UPDATE Audio SET id_commentaire = {0}, id_table = {1} "            
        ).format(
            self.userwdgfield.textBrowser_comm,
            "equipement",            
        )        
        self.dbase.query(sqlquery)
        self.dbase.commit()

class UserUI(QWidget):
    def __init__(self, widget, parent=None):
        super(UserUI, self).__init__(parent=parent)
        log.debug("Set Layout")
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabasedigue_equipement_tool_ui.ui')
        uic.loadUi(uipath, self)        

class UserUISirs(QWidget):
    def __init__(self, parent=None):
        super(UserUISirs, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabasedigue_equipement_tool_ui_SIRS.ui')
        uic.loadUi(uipath, self)