# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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
import logging
from collections import OrderedDict

import qgis
from qgis.PyQt import uic, QtCore, QtGui
from qgis.PyQt.QtWidgets import (QWidget, QLabel, QFrame)

from ..base2.lamiabase_infralineaire_tool import BaseInfraLineaireTool
from .lamiabasetramway_photo_tool import BaseTramwayPhotoTool as BasePhotoTool
from .lamiabasetramway_croquis_tool import BaseTramwayCroquisTool as BaseCroquisTool
from .lamiabasetramway_desordre_tool import BaseTramwayDesordreTool





class BaseTramwayInfraLineaireTool(BaseInfraLineaireTool):


    def __init__(self, **kwargs):
        super(BaseTramwayInfraLineaireTool, self).__init__(**kwargs)
        self.linkedgeom = [['Desordre', 'lid_descriptionsystem']]


    """
    def initTool(self):
        super(BaseTramwayInfraLineaireTool,self).initTool()
        self.PointENABLED = True
        self.LineENABLED = True
    """


    def initMainToolWidget(self):

        self.toolwidgetmain = UserUIField()

        self.formtoolwidgetconfdictmain = {'Infralineaire': {'linkfield': 'id_infralineaire',
                                                                'widgets': {'typeSection' : self.toolwidgetmain.comboBox_typesection,
                                                                            'anneeMiseEnService' : self.toolwidgetmain.dateEdit_miseservice,
                                                                            'ligne': self.toolwidgetmain.lineEdit_ligne,
                                                                            'pk': self.toolwidgetmain.doubleSpinBox_pk,
                                                                            'vitesseExploitation': self.toolwidgetmain.doubleSpinBox_vitessseexploit,
                                                                            'circulation': self.toolwidgetmain.comboBox_circulation,
                                                                            'typeRevetement': self.toolwidgetmain.comboBox_typerevet,

                                                                            'tangentetxt': self.toolwidgetmain.lineEdit_tangente,
                                                                            'rayon': [self.toolwidgetmain.doubleSpinBox_rayon,
                                                                                        self.toolwidgetmain.doubleSpinBox_rayoncourbcourb],
                                                                            'deviationtype': self.toolwidgetmain.comboBox_devtype,
                                                                            'deviation': self.toolwidgetmain.doubleSpinBox_deviation,
                                                                            'manoeuvre': self.toolwidgetmain.comboBox_manoeuvre,

                                                                            }},
                                                'Objet': {'linkfield': 'id_objet',
                                                        'widgets': {'libelle': self.toolwidgetmain.lineEdit_nom,
                                                                    'commentaire': self.toolwidgetmain.textBrowser_commentaire}},
                                                'Descriptionsystem': {'linkfield': 'id_descriptionsystem',
                                                                    'widgets': {}}}

        self.toolwidgetmain.toolButton_pk.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_pk))
        self.toolwidgetmain.toolButton_vit.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_vitessseexploit))

        self.toolwidgetmain.toolButton_deviation.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_deviation))
        self.toolwidgetmain.toolButton_rayon.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_rayon))
        self.toolwidgetmain.toolButton_rayoncourb.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_rayoncourbcourb))

        self.toolwidgetmain.toolButton_angle.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_angle))




        self.dbasechildwdgfield = []
        self.instancekwargs['parentwidget'] = self

        #if self.parentWidget is None:
        self.propertieswdgDesordre = BaseTramwayDesordreTool(**self.instancekwargs)
        #self.propertieswdgDesordre.groupBox_elements.setParent(None)
        #self.propertieswdgDesordre.groupBox_geom.setParent(None)
        #self.propertieswdgDesordre.toolwidgetmain.frame_2.setParent(None)
        #self.propertieswdgDesordre.toolwidgetmain.stackedWidget.setParent(None)
        self.propertieswdgDesordre.initMainToolWidget()
        self.propertieswdgDesordre.propertieswdgOBSERVATION.initMainToolWidget()
        self.propertieswdgDesordre.SKIP_LOADING_UI = True
        #parenttab = self.tabWidget
        ##self.propertieswdgDesordre.tabWidgetmain = self.propertieswdgDesordre.propertieswdgOBSERVATION.tabWidgetmain
        #indexinserted = parenttab.addTab(self.propertieswdgDesordre.propertieswdgOBSERVATION.tabWidgetmain.widget(0),
        #                                        QtGui.QIcon(self.propertieswdgDesordre.propertieswdgOBSERVATION.tooltreewidgetICONPATH),
        #                                        self.propertieswdgDesordre.propertieswdgOBSERVATION.tooltreewidgetSUBCAT)
        #self.propertieswdgDesordre.tabWidget.removeTab(0)
        self.dbasechildwdgfield.append(self.propertieswdgDesordre)

        self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)

        self.propertieswdgCROQUIS = BaseCroquisTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

        self.toolwidgetmain.comboBox_typesection.currentIndexChanged.connect(self.typeSectionChanged)
        self.toolwidgetmain.comboBox_typerevet.currentIndexChanged.connect(self.typeRevetementChanged)


    def typeSectionChanged(self, combovalue=None):
        if self.toolwidgetmain.comboBox_typesection.currentText() in ['Courbe']:
            self.toolwidgetmain.stackedWidget.setCurrentIndex(0)
        elif self.toolwidgetmain.comboBox_typesection.currentText() in ['Appareil de voie']:
            self.toolwidgetmain.stackedWidget.setCurrentIndex(1)
        elif self.toolwidgetmain.comboBox_typesection.currentText() in ['Traversée oblique']:
            self.toolwidgetmain.stackedWidget.setCurrentIndex(2)
        else:
            self.toolwidgetmain.stackedWidget.setCurrentIndex(3)


        if self.toolwidgetmain.comboBox_typesection.currentText() in ['Appareil de voie']:
            self.propertieswdgDesordre.propertieswdgOBSERVATION.toolwidgetmain.tabWidget.setTabEnabled(3,True)
            self.propertieswdgDesordre.propertieswdgOBSERVATION.toolwidgetmain.stackedWidget_appareil.setCurrentIndex(1)
        elif self.toolwidgetmain.comboBox_typesection.currentText() in ['Appareil de dilatation']:
            self.propertieswdgDesordre.propertieswdgOBSERVATION.toolwidgetmain.tabWidget.setTabEnabled(3, True)
            self.propertieswdgDesordre.propertieswdgOBSERVATION.toolwidgetmain.stackedWidget_appareil.setCurrentIndex(2)
        else:
            self.propertieswdgDesordre.propertieswdgOBSERVATION.toolwidgetmain.tabWidget.setTabEnabled(3, False)
            self.propertieswdgDesordre.propertieswdgOBSERVATION.toolwidgetmain.stackedWidget_appareil.setCurrentIndex(0)

        if self.toolwidgetmain.comboBox_typesection.currentText() in ['Fin de voie']:
            self.propertieswdgDesordre.propertieswdgOBSERVATION.toolwidgetmain.tabWidget_2.setTabEnabled(2, True)
        else:
            self.propertieswdgDesordre.propertieswdgOBSERVATION.toolwidgetmain.tabWidget_2.setTabEnabled(2, False)

        if self.toolwidgetmain.comboBox_typesection.currentText() in ['Traversée oblique']:
            self.propertieswdgDesordre.propertieswdgOBSERVATION.toolwidgetmain.stackedWidget_4.setCurrentIndex(1)
        elif self.toolwidgetmain.comboBox_typesection.currentText() in ['Courbe']:
            self.propertieswdgDesordre.propertieswdgOBSERVATION.toolwidgetmain.stackedWidget_4.setCurrentIndex(2)
        else:
            self.propertieswdgDesordre.propertieswdgOBSERVATION.toolwidgetmain.stackedWidget_4.setCurrentIndex(0)

        if self.toolwidgetmain.comboBox_typesection.currentText() in ['Courbe']:
            self.propertieswdgDesordre.propertieswdgOBSERVATION.toolwidgetmain.stackedWidget_5.setCurrentIndex(1)
        else:
            self.propertieswdgDesordre.propertieswdgOBSERVATION.toolwidgetmain.stackedWidget_5.setCurrentIndex(0)


    def typeRevetementChanged(self, combovalue=None):

        if self.toolwidgetmain.comboBox_typerevet.currentText() == 'Mineral modulaire':
            self.propertieswdgDesordre.propertieswdgOBSERVATION.toolwidgetmain.stackedWidget_revet.setCurrentIndex(0)
        elif self.toolwidgetmain.comboBox_typerevet.currentText() == 'Mineral non modulaire':
            self.propertieswdgDesordre.propertieswdgOBSERVATION.toolwidgetmain.stackedWidget_revet.setCurrentIndex(1)
        elif self.toolwidgetmain.comboBox_typerevet.currentText() == u'Végétalisé':
            self.propertieswdgDesordre.propertieswdgOBSERVATION.toolwidgetmain.stackedWidget_revet.setCurrentIndex(2)
        elif self.toolwidgetmain.comboBox_typerevet.currentText() == 'Ballast':
            self.propertieswdgDesordre.propertieswdgOBSERVATION.toolwidgetmain.stackedWidget_revet.setCurrentIndex(3)
        elif self.toolwidgetmain.comboBox_typerevet.currentText() == 'Platelage':
            self.propertieswdgDesordre.propertieswdgOBSERVATION.toolwidgetmain.stackedWidget_revet.setCurrentIndex(4)
        else:
            self.propertieswdgDesordre.propertieswdgOBSERVATION.toolwidgetmain.stackedWidget_revet.setCurrentIndex(5)


    def postSaveFeature(self, savedfeaturepk=None):

        # save a disorder on first creation
        #if self.savingnewfeature and self.savingnewfeatureVersion == False:
        if self.currentFeaturePK is None:
            self.propertieswdgDesordre.toolbarNew()
            geomtext = self.dbase.getValuesFromPk('Infralineaire_qgis',
                                            'ST_AsText(geom)',
                                            savedfeaturepk)

            qgsgeom = qgis.core.QgsGeometry.fromWkt(geomtext).asPolyline()
            qgsgeomfordesordre = qgsgeom

            self.propertieswdgDesordre.setTempGeometry(qgsgeomfordesordre)

            self.currentFeaturePK = savedfeaturepk
            self.propertieswdgDesordre.toolbarSave()
            pkdesordre = self.propertieswdgDesordre.currentFeaturePK

            sql = "UPDATE Desordre SET groupedesordre = 'INF' WHERE pk_desordre = {}".format(pkdesordre)
            self.dbase.query(sql)
            """
            pkobjet = self.dbase.createNewObjet()
            lastiddesordre = self.dbase.getLastId('Desordre') + 1
            geomtext, iddessys = self.dbase.getValuesFromPk('Infralineaire_qgis',
                                                            ['ST_AsText(geom)', 'id_descriptionsystem'],
                                                            self.currentFeaturePK)
            sql = self.dbase.createSetValueSentence(type='INSERT',
                                                    tablename='Desordre',
                                                    listoffields=['id_desordre', 'lpk_objet', 'groupedesordre',
                                                                  'lid_descriptionsystem', 'geom'],
                                                    listofrawvalues=[lastiddesordre, pkobjet, 'INF', iddessys,
                                                                     geomtext])
            self.dbase.query(sql)
            """

class UserUIField(QWidget):
    def __init__(self, parent=None):
        super(UserUIField, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabasetramway_infralineaire_tool_ui.ui')
        uic.loadUi(uipath, self)
