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
import qgis
try:
    from qgis.PyQt.QtGui import (QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget)
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..base2.lamiabase_equipement_tool import BaseEquipementTool

from .lamiabasetramway_photo_tool import BaseTramwayPhotoTool as BasePhotoTool
from .lamiabasetramway_croquis_tool import BaseTramwayCroquisTool as BaseCroquisTool
from .lamiabasetramway_desordre_tool import BaseTramwayDesordreTool

#from .lamiabasedigue_desordre_tool import BaseDigueDesordreTool


import os
import datetime


class BaseTramwayEquipementTool(BaseEquipementTool):

    LOADFIRST = False
    dbasetablename = 'Equipement'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(BaseTramwayEquipementTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)
        self.linkedgeom = [['Desordre', 'lid_descriptionsystem']]
        self.qtreewidgetfields = ['souscategorie']


    def initFieldUI(self):
        # ****************************************************************************************
        #   userui Field
        if self.userwdgfield is None:
            # ****************************************************************************************
            # userui
            self.userwdgfield = UserUI()
            self.linkuserwdgfield = {'Equipement' : {'linkfield' : 'id_equipement',
                                             'widgets' : {
                                                 'categorie': self.userwdgfield.comboBox_cat,
                                                 'souscategorie': self.userwdgfield.comboBox_souscat,

                                                  # general
                                                 'dateMiseService': self.userwdgfield.dateEdit_miseenservice,
                                                 'dureeVie': self.userwdgfield.spinBox_dureevie,
                                                 'numSerie': self.userwdgfield.lineEdit_numserie,
                                                 'frequenceMaintenance': self.userwdgfield.spinBox_freqmaintenance,
                                                 'frequencePannes': self.userwdgfield.spinBox_freqpannes,
                                                 'frequenceRenouvellement': self.userwdgfield.spinBox_freqrenouv,
                                                 'expoClimat': self.userwdgfield.comboBox_expoconditionclim,

                                                 #BIV
                                                 'lisibiliteInformation': self.userwdgfield.comboBox_lisibilite,

                                                 #abris
                                                 'typeMaintenance': self.userwdgfield.lineEdit_typemaintenance,

                                                 #sono
                                                 'couvSono': self.userwdgfield.comboBox_couvsonore,
                                                 'adaptationBruit': self.userwdgfield.comboBox_adaptbruits,
                                                 'audibiliteInfos': self.userwdgfield.comboBox_audibinfo,

                                                 #cameras
                                                 'typezonemanoeuvre': self.userwdgfield.lineEdit_zonemanoeuvre,
                                                 'typeCam': self.userwdgfield.comboBox_typecamera,
                                                 'technoUtilisee': self.userwdgfield.comboBox_technocamera,
                                                 'couvZone': self.userwdgfield.comboBox_couvvideo,
                                                 'clareteImages': self.userwdgfield.spinBox_clarteimages




                                             }},
                                'Objet' : {'linkfield' : 'id_objet',
                                          'widgets' : {
                                                          'commentaire': self.userwdgfield.textBrowser_comm}},
                                'Descriptionsystem' : {'linkfield' : 'id_descriptionsystem',
                                          'widgets' : {}}}
            self.userwdgfield.comboBox_cat.currentIndexChanged.connect(self.changeCategorie)
            self.userwdgfield.comboBox_souscat.currentIndexChanged.connect(self.changeSubCategorie)


            # ****************************************************************************************
            # child widgets
            self.dbasechildwdgfield = []

            if self.parentWidget is None:

                self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(dbase=self.dbase, gpsutil=self.gpsutil, parentwidget=self)
                self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)

                self.propertieswdgCROQUIS = BaseCroquisTool(dbase=self.dbase, parentwidget=self)
                self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

            self.propertieswdgDesordre = BaseTramwayDesordreTool(dbase=self.dbase, gpsutil=self.gpsutil,
                                                                 parentwidget=self)
            self.propertieswdgDesordre.NAME = None
            self.propertieswdgDesordre.groupBox_elements.setParent(None)
            self.propertieswdgDesordre.groupBox_geom.setParent(None)
            self.propertieswdgDesordre.userwdgfield.frame_2.setParent(None)
            self.propertieswdgDesordre.userwdgfield.stackedWidget.setParent(None)
            self.userwdgfield.frame_desordres.layout().addWidget(self.propertieswdgDesordre)
            self.propertieswdgDesordre.propertieswdgOBSERVATION2.userwdgfield.groupBox.setParent(None)
            self.dbasechildwdgfield.append(self.propertieswdgDesordre)


    def changeSubCategorie(self, comboindex=None):
        currentcombotext = self.userwdgfield.comboBox_souscat.currentText()
        if currentcombotext in ['BIV', 'Sonorisation', 'Cameras zones de manoeuvre']:
            self.userwdgfield.stackedWidget_2.setCurrentIndex(0)
            if currentcombotext == 'BIV':
                self.userwdgfield.stackedWidget_3.setCurrentIndex(0)
            elif currentcombotext == 'Sonorisation':
                self.userwdgfield.stackedWidget_3.setCurrentIndex(1)
            elif currentcombotext == 'Cameras zones de manoeuvre':
                self.userwdgfield.stackedWidget_3.setCurrentIndex(2)
        elif currentcombotext in ['Abris modulaires']:
            self.userwdgfield.stackedWidget_2.setCurrentIndex(1)





    def postInitFeatureProperties(self, feat):

        self.userwdgfield.comboBox_cat.currentIndexChanged.emit(-1)

        if self.parentWidget is not None and self.parentWidget.currentFeaturePK is not None:
            if self.parentWidget.dbasetablename == 'Noeud':
                parentcat = self.parentWidget.userwdgfield.comboBox_typenoeud.currentText()
                if parentcat == 'Station':
                    self.userwdgfield.comboBox_cat.setCurrentIndex(0)
                elif parentcat == 'Local':
                    self.userwdgfield.comboBox_cat.setCurrentIndex(1)


                    noeudfet = self.dbase.getLayerFeatureByPk('Noeud', self.parentWidget.currentFeaturePK)
                    neudfetgeom = noeudfet.geometry().asPoint()
                    self.createorresetRubberband(1)
                    self.setTempGeometry([neudfetgeom,neudfetgeom], False,False)



    def postSaveFeature(self, boolnewfeature):

        # save a disorder on first creation
        if self.savingnewfeature and self.savingnewfeatureVersion == False:


            if self.userwdgfield.comboBox_cat.currentText() == 'Station':
                pkobjet = self.dbase.createNewObjet()
                lastiddesordre = self.dbase.getLastId('Desordre') + 1
                geomtext, iddessys = self.dbase.getValuesFromPk('Equipement_qgis',
                                                                ['ST_AsText(geom)', 'id_descriptionsystem'],
                                                                self.currentFeaturePK)


                sql = self.dbase.createSetValueSentence(type='INSERT',
                                                        tablename='Desordre',
                                                        listoffields=['id_desordre', 'lpk_objet', 'groupedesordre',
                                                                      'lid_descriptionsystem', 'geom'],
                                                        listofrawvalues=[lastiddesordre, pkobjet, 'EQ1', iddessys,
                                                                         geomtext])
                self.dbase.query(sql)

            elif self.userwdgfield.comboBox_cat.currentText() == 'Local':
                pkobjet = self.dbase.createNewObjet()
                lastiddesordre = self.dbase.getLastId('Desordre') + 1
                geomtext, iddessys = self.dbase.getValuesFromPk('Equipement_qgis',
                                                                ['ST_AsText(geom)', 'id_descriptionsystem'],
                                                                self.currentFeaturePK)


                sql = self.dbase.createSetValueSentence(type='INSERT',
                                                        tablename='Desordre',
                                                        listoffields=['id_desordre', 'lpk_objet', 'groupedesordre',
                                                                      'lid_descriptionsystem', 'geom'],
                                                        listofrawvalues=[lastiddesordre, pkobjet, 'EQ2', iddessys,
                                                                         geomtext])
                self.dbase.query(sql)










class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabasetramway_equipement_tool_ui.ui')
        uic.loadUi(uipath, self)
