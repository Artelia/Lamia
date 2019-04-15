# -*- coding: utf-8 -*-
"""


import datetime
import logging
import time
debugtime = False
"""
from __future__ import unicode_literals
from qgis.PyQt import uic, QtCore, QtGui

try:
    from qgis.PyQt.QtGui import (QWidget, QLabel, QFrame)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget, QLabel, QFrame)
import os
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..base2.lamiabase_infralineaire_tool import BaseInfraLineaireTool
import logging
# from ..base.lamiabase_photo_tool import BasePhotoTool
from .lamiabasetramway_photo_tool import BaseTramwayPhotoTool as BasePhotoTool
from .lamiabasetramway_croquis_tool import BaseTramwayCroquisTool as BaseCroquisTool
from .lamiabasetramway_desordre_tool import BaseTramwayDesordreTool
from collections import OrderedDict




class BaseTramwayInfraLineaireTool(BaseInfraLineaireTool):


    LOADFIRST = True
    dbasetablename = 'Infralineaire'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(BaseTramwayInfraLineaireTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)
        self.linkedgeom = [['Desordre', 'lid_descriptionsystem']]



    def initTool(self):
        super(BaseTramwayInfraLineaireTool,self).initTool()
        self.PointENABLED = True
        self.LineENABLED = True



    def initFieldUI(self):
        # ****************************************************************************************
        #   userui Field
        if self.userwdgfield is None:
            self.userwdgfield = UserUIField()

            self.linkuserwdgfield = {'Infralineaire': {'linkfield': 'id_infralineaire',
                                                       'widgets': {'typeSection' : self.userwdgfield.comboBox_typesection,
                                                                   'anneeMiseEnService' : self.userwdgfield.dateEdit_miseservice,
                                                                   'ligne': self.userwdgfield.lineEdit_ligne,
                                                                   'pk': self.userwdgfield.doubleSpinBox_pk,
                                                                   'vitesseExploitation': self.userwdgfield.doubleSpinBox_vitessseexploit,
                                                                   'circulation': self.userwdgfield.comboBox_circulation,
                                                                   'typeRevetement': self.userwdgfield.comboBox_typerevet,

                                                                   'tangente': self.userwdgfield.doubleSpinBox_tangente,
                                                                   'rayon': self.userwdgfield.doubleSpinBox_rayon,
                                                                   'deviation': self.userwdgfield.doubleSpinBox_deviation,
                                                                   'manoeuvre': self.userwdgfield.comboBox_manoeuvre,

                                                                   }},
                                     'Objet': {'linkfield': 'id_objet',
                                               'widgets': {'libelle': self.userwdgfield.lineEdit_nom,
                                                           'commentaire': self.userwdgfield.textBrowser_commentaire}},
                                     'Descriptionsystem': {'linkfield': 'id_descriptionsystem',
                                                           'widgets': {}}}

            self.userwdgfield.toolButton_pk.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_pk))
            self.userwdgfield.toolButton_vit.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_vitessseexploit))

            self.userwdgfield.toolButton_tangente.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_tangente))
            self.userwdgfield.toolButton_deviation.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_deviation))
            self.userwdgfield.toolButton_rayon.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_rayon))



            self.dbasechildwdgfield = []

            if self.parentWidget is None:
                self.propertieswdgDesordre = BaseTramwayDesordreTool(dbase=self.dbase, gpsutil=self.gpsutil, parentwidget=self)
                self.propertieswdgDesordre.groupBox_elements.setParent(None)
                self.propertieswdgDesordre.groupBox_geom.setParent(None)
                self.propertieswdgDesordre.userwdgfield.frame_2.setParent(None)
                self.propertieswdgDesordre.userwdgfield.stackedWidget.setParent(None)
                self.dbasechildwdgfield.append(self.propertieswdgDesordre)


                self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(dbase=self.dbase, gpsutil=self.gpsutil, parentwidget=self)
                self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)


                self.propertieswdgCROQUIS = BaseCroquisTool(dbase=self.dbase, parentwidget=self)
                self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)





            self.userwdgfield.comboBox_typesection.currentIndexChanged.connect(self.typeSectionChanged)
            self.userwdgfield.comboBox_typerevet.currentIndexChanged.connect(self.typeRevetementChanged)


    def typeSectionChanged(self, combovalue=None):
        if self.userwdgfield.comboBox_typesection.currentText() == 'Appareil de voie':
            self.userwdgfield.stackedWidget.setCurrentIndex(1)
        else:
            self.userwdgfield.stackedWidget.setCurrentIndex(0)

    def typeRevetementChanged(self, combovalue=None):

        if self.userwdgfield.comboBox_typerevet.currentText() == 'Mineral modulaire':
            self.propertieswdgDesordre.propertieswdgOBSERVATION2.userwdgfield.stackedWidget_revet.setCurrentIndex(0)
        elif self.userwdgfield.comboBox_typerevet.currentText() == 'Mineral non modulaire':
            self.propertieswdgDesordre.propertieswdgOBSERVATION2.userwdgfield.stackedWidget_revet.setCurrentIndex(1)
        elif self.userwdgfield.comboBox_typerevet.currentText() == u'Végétalisé':
            self.propertieswdgDesordre.propertieswdgOBSERVATION2.userwdgfield.stackedWidget_revet.setCurrentIndex(2)
        elif self.userwdgfield.comboBox_typerevet.currentText() == 'Ballast':
            self.propertieswdgDesordre.propertieswdgOBSERVATION2.userwdgfield.stackedWidget_revet.setCurrentIndex(3)
        else:
            self.propertieswdgDesordre.propertieswdgOBSERVATION2.userwdgfield.stackedWidget_revet.setCurrentIndex(4)


    def postSaveFeature(self, boolnewfeature):

        # save a disorder on first creation
        if self.savingnewfeature and self.savingnewfeatureVersion == False:
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


class UserUIField(QWidget):
    def __init__(self, parent=None):
        super(UserUIField, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabasetramway_infralineaire_tool_ui.ui')
        uic.loadUi(uipath, self)
