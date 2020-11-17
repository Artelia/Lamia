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

from qgis.PyQt import uic, QtCore
from qgis.PyQt.QtWidgets import (QWidget)

from ..base2.lamiabase_observation_tool import BaseObservationTool
from .lamiabasedigue_photo_tool import BaseDiguePhotoTool as BasePhotoTool
from .lamiabasedigue_croquis_tool import BaseCroquisTool



class BaseDigueObservationTool(BaseObservationTool):

    tooltreewidgetSUBCAT = None

    def __init__(self, **kwargs):
        super(BaseDigueObservationTool, self).__init__(**kwargs)

    """
    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Desordre'
        self.NAME = 'Observation'
        self.dbasetablename = 'Observation'
        #self.visualmode = [1, 2]
        self.visualmode = []
        # self.PointENABLED = True
        # self.LineENABLED = True
        # self.PolygonENABLED = True
        # self.magicfunctionENABLED = True
        self.linkagespec = {'Desordre' : {'tabletc' : None,
                                           'idsource' : 'lk_desordre',
                                       'idtcsource' : None,
                                           'iddest' : 'id_desordre',
                                       'idtcdest' : None,
                                           'desttable' : ['Desordre']},
                            'Marche' :{'tabletc' : None,
                                              'idsource' : 'lk_marche',
                                            'idtcsource' : None,
                                           'iddest' : 'id_marche',
                                           'idtcdest' : None,
                                           'desttable' : ['Marche']} }
        self.iconpath = os.path.join(os.path.dirname(__file__), 'lamiadefault_observation_tool_icon.png')

        # ****************************************************************************************
        #properties ui
        pass
    
    """
    def initMainToolWidget(self):
        # ****************************************************************************************
        # userui Desktop
        if self.dbase.variante in [None, 'Lamia']:

            self.toolwidgetmain = UserUI()
            self.formtoolwidgetconfdictmain = {'Observation': {'linkfield': 'id_observation',
                                                                'widgets': {
                                                                    'datetimeobservation': self.toolwidgetmain.dateTimeEdit,
                                                                    'nombre': self.toolwidgetmain.spinBox_nombre,
                                                                    'longueurdes': self.toolwidgetmain.doubleSpinBox_longueur,
                                                                    'gravite': self.toolwidgetmain.comboBox_urgence,

                                                                    'oh_etatgeneral': self.toolwidgetmain.comboBox_etatgen,
                                                                    'oh_etatgeneralcom': self.toolwidgetmain.textBrowser_etatgencom,

                                                                    'oh_etatvantellerie': self.toolwidgetmain.comboBox_etatvantellerie,
                                                                    'oh_etatvantelleriecom': self.toolwidgetmain.textBrowser_vanteleriecom,
                                                                    'oh_etatgeniecivil': [self.toolwidgetmain.comboBox_etatGC,
                                                                                        self.toolwidgetmain.comboBox_etatGC_2],
                                                                    'oh_etatgeniecivilcom': [
                                                                        self.toolwidgetmain.textBrowser_etatGC,
                                                                        self.toolwidgetmain.textBrowser_etatGC_2],
                                                                    'oh_testmanoeuvre': self.toolwidgetmain.comboBox_manoeuvre,
                                                                    'oh_testmanoeuvrecom': self.toolwidgetmain.textBrowser_manoeuvre,
                                                                    'oh_etancheite': self.toolwidgetmain.checkBox_etancheite,
                                                                    'oh_etancheitecom': self.toolwidgetmain.textBrowser__etancheite,
                                                                    'oh_ecoulement': [self.toolwidgetmain.comboBox_envas,
                                                                                    self.toolwidgetmain.comboBox_envas2],
                                                                    'oh_ecoulementcom': [
                                                                        self.toolwidgetmain.textBrowser_envascom,
                                                                        self.toolwidgetmain.textBrowser_envascom2],

                                                                    'evolution': self.toolwidgetmain.textEdit_evolution,
                                                                    'typesuite': self.toolwidgetmain.comboBox_typesuite,
                                                                    'commentairesuite': self.toolwidgetmain.textEdit_suite}},
                                                'Objet': {'linkfield': 'id_objet',
                                                        'widgets': {'commentaire': self.toolwidgetmain.textEdit_comm}}}

            self.toolwidgetmain.toolButton_calc_nb.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.spinBox_nombre))
            self.toolwidgetmain.toolButton_longueur.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_longueur))

            # ****************************************************************************************
            # child widgets
            self.dbasechildwdgfield=[]
            self.instancekwargs['parentwidget'] = self
            # if self.parentWidget is not None:
            #if self.parentWidget is None or self.parentWidget is not None and self.parentWidget.dbasetablename == 'Desordre':
            self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(**self.instancekwargs)
            self.dbasechildwdgfield = [self.propertieswdgPHOTOGRAPHIE]
            self.propertieswdgCROQUIS = BaseCroquisTool(**self.instancekwargs)
            self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)







        elif self.dbase.variante in ['SIRS']:

            self.toolwidgetmain = UserUISirs()

            self.formtoolwidgetconfdictmain = {'Observation' : {'linkfield' : 'id_observation',
                                                        'widgets' : {'datetimeobservation' : self.toolwidgetmain.dateTimeEdit,
                                                                    'nombre' : self.toolwidgetmain.spinBox_nombre,
                                                                'gravite': self.toolwidgetmain.comboBox_urgence,

                                                                'oh_etatvantellerie' : self.toolwidgetmain.comboBox_etatvantellerie,
                                                                'oh_etatvantelleriecom': self.toolwidgetmain.textBrowser_vanteleriecom,
                                                                    'oh_etatgeniecivil': self.toolwidgetmain.comboBox_etatGC,
                                                                    'oh_etatgeniecivilcom': self.toolwidgetmain.textBrowser_etatGC,
                                                                    'oh_testmanoeuvre': self.toolwidgetmain.comboBox_manoeuvre,
                                                                    'oh_testmanoeuvrecom': self.toolwidgetmain.textBrowser_manoeuvre,
                                                                    'oh_etancheite': self.toolwidgetmain.checkBox_etancheite,
                                                                    'oh_etancheitecom': self.toolwidgetmain.textBrowser__etancheite,


                                                                'evolution': self.toolwidgetmain.textEdit_evolution,
                                                                'typesuite': self.toolwidgetmain.comboBox_typesuite,
                                                                'commentairesuite': self.toolwidgetmain.textEdit_suite}},
                                        'Objet' : {'linkfield' : 'id_objet',
                                                    'widgets' : {'commentaire': self.toolwidgetmain.textEdit_comm}}}


            self.toolwidgetmain.toolButton_calc_nb.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.spinBox_nombre))


            # ****************************************************************************************
            # child widgets
            self.dbasechildwdgfield=[]
            self.instancekwargs['parentwidget'] = self
            # if self.parentWidget is not None:
            #if self.parentWidget is None or self.parentWidget is not None and self.parentWidget.dbasetablename == 'Desordre':
            self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(**self.instancekwargs)
            self.dbasechildwdgfield = [self.propertieswdgPHOTOGRAPHIE]
            self.propertieswdgCROQUIS = BaseCroquisTool(**self.instancekwargs)
            self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)




    def equipementTypeChanged(self, currentindex):
        if self.toolwidgetmain is None:
            return
        currenttext = self.parentWidget.parentWidget.toolwidgetmain.comboBox_type.currentText()
        if currenttext in ['Vanne', 'Clapet']:
            self.toolwidgetmain.stackedWidget_2.setCurrentIndex(1)
        elif currenttext in ['Exutoire']:
            self.toolwidgetmain.stackedWidget_2.setCurrentIndex(2)
        else :
            self.toolwidgetmain.stackedWidget_2.setCurrentIndex(0)

    # def postInitFeatureProperties(self, feat):
    def postSelectFeature(self):
        super(BaseDigueObservationTool, self).postSelectFeature()
        if self.currentFeaturePK is not None:
            iddesordre = self.dbase.getValuesFromPk('Observation_qgis', 'lid_desordre', self.currentFeaturePK)
            if iddesordre is not None:
                sql = """
                        SELECT Equipement_now.typeequipement FROM Equipement_now, Desordre_now 
                        WHERE Desordre_now.lid_descriptionsystem = Equipement_now.id_descriptionsystem
                        AND Desordre_now.id_desordre = 
                        """
                sql+= str(iddesordre)
                sql = self.dbase.updateQueryTableNow(sql)
                res = self.dbase.query(sql)
                if res and len(res)>0:
                    currenttext = res[0][0]
                    if currenttext in ['VAN', 'CLA']:
                        self.toolwidgetmain.stackedWidget_2.setCurrentIndex(1)
                    elif currenttext in ['EXU']:
                        self.toolwidgetmain.stackedWidget_2.setCurrentIndex(2)
                    else :
                        self.toolwidgetmain.stackedWidget_2.setCurrentIndex(0)


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabasedigue_observation_tool_ui.ui')
        uic.loadUi(uipath, self)

class UserUISirs(QWidget):
    def __init__(self, parent=None):
        super(UserUISirs, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabasedigue_observation_tool_ui_SIRS.ui')
        uic.loadUi(uipath, self)
