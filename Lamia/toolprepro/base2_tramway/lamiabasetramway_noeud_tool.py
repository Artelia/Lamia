# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore

try:
    from qgis.PyQt.QtGui import (QWidget, QPushButton)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget, QPushButton)
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..base2.lamiabase_noeud_tool import BaseNoeudTool

import os
import qgis
from collections import OrderedDict
import datetime
# from ..base.lamiabase_photo_tool import BasePhotoTool
from .lamiabasetramway_photo_tool import BaseTramwayPhotoTool as BasePhotoTool
from .lamiabasetramway_croquis_tool import BaseTramwayCroquisTool as BaseCroquisTool
from .lamiabasetramway_equipement_tool import BaseTramwayEquipementTool as BaseEquipementTool
from .lamiabasetramway_desordre_tool import BaseTramwayDesordreTool
#from ..base.lamiabase_croquis_tool import BaseCroquisTool
#from .lamiabaseassainissement_desordre_tool import BaseAssainissementDesordreTool
#from .lamiabaseassainissement_equipement_tool import BaseAssainissementEquipementTool
import sys



class BaseTramwayNoeudTool(BaseNoeudTool):


    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(BaseTramwayNoeudTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)
        self.linkedgeom = [['Desordre', 'lid_descriptionsystem']]
        self.qtreewidgetfields = ['typenoeud']



    def initFieldUI(self):
        # ****************************************************************************************
        # userui Desktop
        if self.userwdgfield is None:

            # ****************************************************************************************
            # userui
            self.userwdgfield = UserUI()
            self.linkuserwdgfield = {'Noeud' : {'linkfield' : 'id_noeud',
                                             'widgets' : {
                                                          'typenoeud' : self.userwdgfield.comboBox_typenoeud,
                                                         'typeLigne': self.userwdgfield.comboBox_typeligne,
                                                        'numLigne': self.userwdgfield.lineEdit_nomligne,

                                                        'typelocal': self.userwdgfield.lineEdit_typelocal




                                             }},
                                'Objet' : {'linkfield' : 'id_objet',
                                          'widgets' : {
                                                      #'libelle': self.userwdgfield.lineEdit_libelle
                                                      }},
                                'Descriptionsystem' : {'linkfield' : 'id_descriptionsystem',
                                          'widgets' : {}}}

            self.userwdgfield.comboBox_typenoeud.currentIndexChanged.connect(self.changeCategorie)
            # ****************************************************************************************
            # child widgets

            self.dbasechildwdgfield = []

            if self.parentWidget is None:
                self.propertieswdgEQUIPEMENT = BaseEquipementTool(dbase=self.dbase, gpsutil=self.gpsutil, parentwidget=self)
                self.dbasechildwdgfield.append(self.propertieswdgEQUIPEMENT)

                self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(dbase=self.dbase, gpsutil=self.gpsutil, parentwidget=self)
                self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)


                self.propertieswdgCROQUIS = BaseCroquisTool(dbase=self.dbase, parentwidget=self)
                self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

                self.propertieswdgDesordre = BaseTramwayDesordreTool(dbase=self.dbase, gpsutil=self.gpsutil, parentwidget=self)
                self.propertieswdgDesordre.NAME = None
                self.propertieswdgDesordre.groupBox_elements.setParent(None)
                self.propertieswdgDesordre.groupBox_geom.setParent(None)
                self.propertieswdgDesordre.userwdgfield.frame_2.setParent(None)
                self.propertieswdgDesordre.userwdgfield.stackedWidget.setParent(None)
                self.userwdgfield.frame_observationlocal.layout().addWidget(self.propertieswdgDesordre)
                self.propertieswdgDesordre.propertieswdgOBSERVATION2.userwdgfield.groupBox.setParent(None)
                self.dbasechildwdgfield.append(self.propertieswdgDesordre)



    def changeCategorie(self, combovalue=None):
        if self.userwdgfield.comboBox_typenoeud.currentText() == 'Station':
            self.userwdgfield.stackedWidget.setCurrentIndex(0)
        elif self.userwdgfield.comboBox_typenoeud.currentText() == 'Local':
            self.userwdgfield.stackedWidget.setCurrentIndex(1)


    def postSaveFeature(self, boolnewfeature):

        # save a disorder on first creation
        if self.savingnewfeature and self.savingnewfeatureVersion == False:
            if self.userwdgfield.comboBox_typenoeud.currentText() == 'Local':
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