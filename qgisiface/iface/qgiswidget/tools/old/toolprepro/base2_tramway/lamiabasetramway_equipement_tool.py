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

import qgis
from qgis.PyQt import uic, QtCore
from qgis.PyQt.QtWidgets import (QWidget)

from ..base2.lamiabase_equipement_tool import BaseEquipementTool
from .lamiabasetramway_photo_tool import BaseTramwayPhotoTool as BasePhotoTool
from .lamiabasetramway_croquis_tool import BaseTramwayCroquisTool as BaseCroquisTool
from .lamiabasetramway_desordre_tool import BaseTramwayDesordreTool



class BaseTramwayEquipementTool(BaseEquipementTool):


    def __init__(self, **kwargs):
        super(BaseTramwayEquipementTool, self).__init__(**kwargs)
        self.linkedgeom = [['Desordre', 'lid_descriptionsystem']]
        self.qtreewidgetfields = ['souscategorie']


    def initMainToolWidget(self):

        self.toolwidgetmain = UserUI()
        self.formtoolwidgetconfdictmain = {'Equipement' : {'linkfield' : 'id_equipement',
                                                        'widgets' : {
                                                            'categorie': self.toolwidgetmain.comboBox_cat,
                                                            'souscategorie': self.toolwidgetmain.comboBox_souscat,

                                                            # general
                                                            'dateMiseService': self.toolwidgetmain.dateEdit_miseenservice,
                                                            'dureeVie': self.toolwidgetmain.spinBox_dureevie,
                                                            'numSerie': self.toolwidgetmain.lineEdit_numserie,
                                                            'frequenceMaintenance': self.toolwidgetmain.spinBox_freqmaintenance,
                                                            'frequencePannes': self.toolwidgetmain.spinBox_freqpannes,
                                                            'frequenceRenouvellement': self.toolwidgetmain.spinBox_freqrenouv,
                                                            'expoClimat': self.toolwidgetmain.comboBox_expoconditionclim,

                                                            #BIV
                                                            'lisibiliteInformation': self.toolwidgetmain.comboBox_lisibilite,

                                                            #abris
                                                            'typeMaintenance': self.toolwidgetmain.lineEdit_typemaintenance,

                                                            #sono
                                                            'couvSono': self.toolwidgetmain.comboBox_couvsonore,
                                                            'adaptationBruit': self.toolwidgetmain.comboBox_adaptbruits,
                                                            'audibiliteInfos': self.toolwidgetmain.comboBox_audibinfo,

                                                            #cameras
                                                            'typezonemanoeuvre': self.toolwidgetmain.lineEdit_zonemanoeuvre,
                                                            'typeCam': self.toolwidgetmain.comboBox_typecamera,
                                                            'technoUtilisee': self.toolwidgetmain.comboBox_technocamera,
                                                            'couvZone': self.toolwidgetmain.comboBox_couvvideo,
                                                            'clareteImages': self.toolwidgetmain.spinBox_clarteimages




                                                        }},
                                        'Objet' : {'linkfield' : 'id_objet',
                                                    'widgets' : {
                                                                    'commentaire': self.toolwidgetmain.textBrowser_comm}},
                                        'Descriptionsystem' : {'linkfield' : 'id_descriptionsystem',
                                                    'widgets' : {}}}
        self.toolwidgetmain.comboBox_cat.currentIndexChanged.connect(self.changeCategorie)
        self.toolwidgetmain.comboBox_souscat.currentIndexChanged.connect(self.changeSubCategorie)


        # ****************************************************************************************
        # child widgets
        self.dbasechildwdgfield = []
        self.instancekwargs['parentwidget'] = self

        #if self.parentWidget is None:

        self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)

        self.propertieswdgCROQUIS = BaseCroquisTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

        self.propertieswdgDesordre = BaseTramwayDesordreTool(**self.instancekwargs)
        #self.propertieswdgDesordre.NAME = None
        #self.propertieswdgDesordre.groupBox_elements.setParent(None)
        #self.propertieswdgDesordre.groupBox_geom.setParent(None)
        #self.propertieswdgDesordre.userwdgfield.frame_2.setParent(None)
        #self.propertieswdgDesordre.userwdgfield.stackedWidget.setParent(None)
        #self.toolwidgetmain.frame_desordres.layout().addWidget(self.propertieswdgDesordre)
        #self.propertieswdgDesordre.propertieswdgOBSERVATION2.userwdgfield.groupBox.setParent(None)
        self.dbasechildwdgfield.append(self.propertieswdgDesordre)


    def changeSubCategorie(self, comboindex=None):
        currentcombotext = self.toolwidgetmain.comboBox_souscat.currentText()
        if currentcombotext in ['BIV', 'Sonorisation', 'Cameras zones de manoeuvre']:
            self.toolwidgetmain.stackedWidget_2.setCurrentIndex(0)
            if currentcombotext == 'BIV':
                self.toolwidgetmain.stackedWidget_3.setCurrentIndex(0)
            elif currentcombotext == 'Sonorisation':
                self.toolwidgetmain.stackedWidget_3.setCurrentIndex(1)
            elif currentcombotext == 'Cameras zones de manoeuvre':
                self.toolwidgetmain.stackedWidget_3.setCurrentIndex(2)
        elif currentcombotext in ['Abris modulaires']:
            self.toolwidgetmain.stackedWidget_2.setCurrentIndex(1)





    # def postInitFeatureProperties(self, feat):
    def postSelectFeature(self):

        self.toolwidgetmain.comboBox_cat.currentIndexChanged.emit(-1)

        if self.parentWidget is not None and self.parentWidget.currentFeaturePK is not None:
            if self.parentWidget.DBASETABLENAME == 'Noeud':
                parentcat = self.parentWidget.toolwidgetmain.comboBox_typenoeud.currentText()
                if parentcat == 'Station':
                    self.toolwidgetmain.comboBox_cat.setCurrentIndex(0)
                elif parentcat == 'Local':
                    self.toolwidgetmain.comboBox_cat.setCurrentIndex(1)


                    #noeudfet = self.dbase.getLayerFeatureByPk('Noeud', self.parentWidget.currentFeaturePK)
                    noeudfet = self.mainifacewidget.qgiscanvas.layers['Noeud']['layer'].getFeature(self.parentWidget.currentFeaturePK)
                    neudfetgeom = noeudfet.geometry().asPoint()
                    self.mainifacewidget.qgiscanvas.createorresetRubberband(1)
                    self.setTempGeometry([neudfetgeom,neudfetgeom], False,False)



    def postSaveFeature(self, savedfeaturepk=None):

        # save a disorder on first creation
        #if self.savingnewfeature and self.savingnewfeatureVersion == False:
        if self.currentFeaturePK is None:
            typeequdict = {'Station': 'EQ1',
                        'Local': 'EQ2'}
            typeequ = self.toolwidgetmain.comboBox_cat.currentText()
            
            if typeequ in typeequdict.keys():
                self.propertieswdgDesordre.toolbarNew()
                geomtext = self.dbase.getValuesFromPk('Equipement_qgis',
                                                'ST_AsText(geom)',
                                                savedfeaturepk)

                qgsgeom = qgis.core.QgsGeometry.fromWkt(geomtext).asPolyline()
                qgsgeomfordesordre = qgsgeom

                self.propertieswdgDesordre.setTempGeometry(qgsgeomfordesordre)

                self.currentFeaturePK = savedfeaturepk
                self.propertieswdgDesordre.toolbarSave()
                pkdesordre = self.propertieswdgDesordre.currentFeaturePK

                sql = "UPDATE Desordre SET groupedesordre = '{}' WHERE pk_desordre = {}".format(typeequdict[typeequ],
                                                                                               pkdesordre)
                self.dbase.query(sql)
            """
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
                
            elif self.toolwidgetmain.comboBox_cat.currentText() == 'Local':
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
            """









class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabasetramway_equipement_tool_ui.ui')
        uic.loadUi(uipath, self)
