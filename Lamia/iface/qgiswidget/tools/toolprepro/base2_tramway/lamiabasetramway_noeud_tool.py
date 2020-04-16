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
from collections import OrderedDict
import datetime
import sys

import qgis
from qgis.PyQt import uic, QtCore
from qgis.PyQt.QtWidgets import (QWidget, QPushButton)

from ..base2.lamiabase_noeud_tool import BaseNoeudTool
from .lamiabasetramway_photo_tool import BaseTramwayPhotoTool as BasePhotoTool
from .lamiabasetramway_croquis_tool import BaseTramwayCroquisTool as BaseCroquisTool
from .lamiabasetramway_equipement_tool import BaseTramwayEquipementTool as BaseEquipementTool
from .lamiabasetramway_desordre_tool import BaseTramwayDesordreTool


class BaseTramwayNoeudTool(BaseNoeudTool):


    def __init__(self, **kwargs):
        super(BaseTramwayNoeudTool, self).__init__(**kwargs)
        self.linkedgeom = [['Desordre', 'lid_descriptionsystem']]
        self.qtreewidgetfields = ['typenoeud']



    def initMainToolWidget(self):

        self.toolwidgetmain = UserUI()
        self.formtoolwidgetconfdictmain = {'Noeud' : {'linkfield' : 'id_noeud',
                                                            'widgets' : {
                                                                        'typenoeud' : self.toolwidgetmain.comboBox_typenoeud,
                                                                        'typeLigne': self.toolwidgetmain.comboBox_typeligne,
                                                                    'numLigne': self.toolwidgetmain.lineEdit_nomligne,

                                                                    'typelocal': self.toolwidgetmain.lineEdit_typelocal




                                                            }},
                                            'Objet' : {'linkfield' : 'id_objet',
                                                        'widgets' : {
                                                                    #'libelle': self.toolwidgetmain.lineEdit_libelle
                                                                    }},
                                            'Descriptionsystem' : {'linkfield' : 'id_descriptionsystem',
                                                        'widgets' : {}}}

        self.toolwidgetmain.comboBox_typenoeud.currentIndexChanged.connect(self.changeCategorie)
        # ****************************************************************************************
        # child widgets

        self.dbasechildwdgfield = []
        self.instancekwargs['parentwidget'] = self

        #if self.parentWidget is None:
        self.propertieswdgEQUIPEMENT = BaseEquipementTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgEQUIPEMENT)

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
        #self.toolwidgetmain.frame_observationlocal.layout().addWidget(self.propertieswdgDesordre)
        #self.propertieswdgDesordre.propertieswdgOBSERVATION2.userwdgfield.groupBox.setParent(None)
        self.dbasechildwdgfield.append(self.propertieswdgDesordre)



    def changeCategorie(self, combovalue=None):
        if self.toolwidgetmain.comboBox_typenoeud.currentText() == 'Station':
            self.toolwidgetmain.stackedWidget.setCurrentIndex(0)
        elif self.toolwidgetmain.comboBox_typenoeud.currentText() == 'Local':
            self.toolwidgetmain.stackedWidget.setCurrentIndex(1)


    def postSaveFeature(self, savedfeaturepk=None):

        # save a disorder on first creation
        #if self.savingnewfeature and self.savingnewfeatureVersion == False:
        if self.currentFeaturePK is None:
            if self.toolwidgetmain.comboBox_typenoeud.currentText() == 'Local':
                pkobjet = self.dbase.createNewObjet()
                lastiddesordre = self.dbase.getLastId('Desordre') + 1

                geomtext, iddessys = self.dbase.getValuesFromPk('Noeud_qgis',
                                                                ['ST_AsText(geom)', 'id_descriptionsystem'],
                                                                self.currentFeaturePK)
                if sys.version_info.major == 2:
                    qgspoint = qgis.core.QgsGeometry.fromWkt(geomtext).asPoint()
                    qgsline = qgis.core.QgsGeometry.fromPolyline([qgspoint,qgspoint])
                    geomtext = qgsline.exportToWkt()
                elif sys.version_info.major == 3:
                    qgspoint = qgis.core.QgsGeometry.fromWkt(geomtext).asPoint()
                    qgsline = qgis.core.QgsGeometry.fromPolylineXY([qgspoint,qgspoint])
                    geomtext = qgsline.asWkt()

                sql = self.dbase.createSetValueSentence(type='INSERT',
                                                        tablename='Desordre',
                                                        listoffields=['id_desordre', 'lpk_objet', 'groupedesordre',
                                                                      'lid_descriptionsystem', 'geom'],
                                                        listofrawvalues=[lastiddesordre, pkobjet, 'NO2', iddessys,
                                                                         geomtext])
                self.dbase.query(sql)


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabasetramway_noeud_tool_ui.ui')
        uic.loadUi(uipath, self)