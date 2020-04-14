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
try:
    from qgis.PyQt.QtGui import (QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget)

from ..base2.lamiabase_observation_tool import BaseObservationTool
from .lamiabaseassainissement_photo_tool import BaseAssainissementPhotoTool as BasePhotoTool
from .lamiabaseassainissement_croquis_tool import BaseAssainissementCroquisTool as BaseCroquisTool


class BaseAssainissementObservationTool(BaseObservationTool):
    
    #specialfieldui = ['2']

    def __init__(self, **kwargs):
        super(BaseAssainissementObservationTool, self).__init__(**kwargs)

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

        if self.dbase.variante in [None, 'Lamia']:

            self.toolwidgetmain = UserUI()
            self.formtoolwidgetconfdictmain = {'Observation' : {'linkfield' : 'id_observation',
                                                'widgets' : {'datetimeobservation' : self.toolwidgetmain.dateTimeEdit,
                                                            #'nombre' : self.toolwidgetmain.spinBox_nombre,
                                                        'gravite': self.toolwidgetmain.comboBox_urgence,

                                                            # regard
                                                            'etattampon': [self.toolwidgetmain.comboBox_etattampon,
                                                                            self.toolwidgetmain.comboBox_PRetattampon],
                                                            'etatechelon': self.toolwidgetmain.comboBox_etatechelon,
                                                            'etatregard': self.toolwidgetmain.comboBox_etatregard,
                                                            'etatcunette': self.toolwidgetmain.comboBox_etatcunette,
                                                            'ECPPdepuisbranchement': self.toolwidgetmain.comboBox_ecpp,
                                                            'infiltration': self.toolwidgetmain.comboBox_infiltration,
                                                            'intrusionracine': self.toolwidgetmain.comboBox_racines,

                                                            'hdeuxs': self.toolwidgetmain.comboBox_h2s,
                                                            'depots': [self.toolwidgetmain.comboBox_depot,
                                                                        self.toolwidgetmain.comboBox_DSHencombrement],
                                                            'miseencharge': self.toolwidgetmain.comboBox_miseencharge,
                                                            'jugemententretien': self.toolwidgetmain.comboBox_entretiengeneral,

                                                            # DIV
                                                            'etatgeneral': self.toolwidgetmain.comboBox_DIVetatgeneral,

                                                            #'evolution': self.toolwidgetmain.textEdit_evolution,
                                                            #'commentaires': self.toolwidgetmain.textEdit_comm,
                                                            #'suite': self.toolwidgetmain.textEdit_suite,
                                                            'typesuite': self.toolwidgetmain.comboBox_typesuite,
                                                            'precisionsuite': self.toolwidgetmain.comboBox_precisionsuite


                                                            }},
                                'Objet' : {'linkfield' : 'id_objet',
                                            'widgets' : {'commentaire': self.toolwidgetmain.textEdit_comm}}}

            self.toolwidgetmain.toolButton_calc_nb.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.spinBox_nombre))

            # ****************************************************************************************
            # child widgets
            self.dbasechildwdgfield=[]
            self.instancekwargs['parentwidget'] = self
            if self.parentWidget is not None:
                self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(**self.instancekwargs)
                self.dbasechildwdgfield = [self.propertieswdgPHOTOGRAPHIE]
                self.propertieswdgCROQUIS = BaseCroquisTool(**self.instancekwargs)
                self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)
                    
        elif self.dbase.variante in ['2018_SNCF']:
            self.toolwidgetmain = UserUI_2()
            self.formtoolwidgetconfdictmain = {'Observation': {'linkfield': 'id_observation',
                                                        'widgets': {
                                                            'datetimeobservation': self.toolwidgetmain.dateTimeEdit,
                                                            # 'nombre' : self.toolwidgetmain.spinBox_nombre,
                                                            'gravite': self.toolwidgetmain.comboBox_urgence,

                                                            # regard
                                                            'etattampon': [self.toolwidgetmain.comboBox_etattampon,
                                                                            self.toolwidgetmain.comboBox_PRetattampon],
                                                            'etatechelon': self.toolwidgetmain.comboBox_etatechelon,
                                                            'etatregard': self.toolwidgetmain.comboBox_etatregard,
                                                            'etatcunette': self.toolwidgetmain.comboBox_etatcunette,
                                                            'hdeuxs': self.toolwidgetmain.comboBox_h2s,
                                                            'depots': [self.toolwidgetmain.comboBox_depot,
                                                                        self.toolwidgetmain.comboBox_DSHencombrement],
                                                            'miseencharge': self.toolwidgetmain.comboBox_miseencharge,
                                                            'jugemententretien': self.toolwidgetmain.comboBox_entretiengeneral,

                                                            # PR
                                                            # 'etattampon': self.toolwidgetmain.comboBox_PRetattampon,
                                                            'etatgeneral': [self.toolwidgetmain.comboBox_etatbache,
                                                                            self.toolwidgetmain.comboBox_DSHetageneral,
                                                                            self.toolwidgetmain.comboBox_DIVetatgeneral],
                                                            'etatasservissement': self.toolwidgetmain.comboBox_etatasservissement,

                                                            # DSH
                                                            # 'etatgeneral': self.toolwidgetmain.comboBox_DSHetageneral,
                                                            # 'ensablement': self.toolwidgetmain.comboBox_DSHencombrement,

                                                            # DIC
                                                            # 'etatgeneral': self.toolwidgetmain.comboBox_DIVetatgeneral,

                                                            }},
                                        'Objet': {'linkfield': 'id_objet',
                                                    'widgets': {'commentaire': self.toolwidgetmain.textEdit_comm}}}

            self.toolwidgetmain.toolButton_calc_nb.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.spinBox_nombre))

            self.dbasechildwdgfield = []
            self.instancekwargs['parentwidget'] = self
            if self.parentWidget is not None:
                self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(**self.instancekwargs)
                self.dbasechildwdgfield = [self.propertieswdgPHOTOGRAPHIE]
                self.propertieswdgCROQUIS = BaseCroquisTool(**self.instancekwargs)
                self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)


        elif self.dbase.variante in ['CD41']:
            
            self.toolwidgetmain = UserUI_3()
            self.formtoolwidgetconfdictmain = {'Observation': {'linkfield': 'id_observation',
                                                        'widgets': {
                                                            'datetimeobservation': self.toolwidgetmain.dateTimeEdit,
                                                            # 'nombre' : self.toolwidgetmain.spinBox_nombre,
                                                            'gravite': self.toolwidgetmain.comboBox_urgence,
                                                            'etatgeneral': self.toolwidgetmain.comboBox_etatgeneral,


                                                            # regard
                                                            'etattampon': self.toolwidgetmain.comboBox_etattampon,
                                                            'etatechelon': self.toolwidgetmain.comboBox_etatechelon,
                                                            'etatregard': self.toolwidgetmain.comboBox_etatregard,
                                                            'etatcunette': self.toolwidgetmain.comboBox_etatcunette,
                                                            'hdeuxs': self.toolwidgetmain.comboBox_h2s,
                                                            'depots': self.toolwidgetmain.comboBox_depot,
                                                            'miseencharge': self.toolwidgetmain.comboBox_miseencharge,
                                                            'jugemententretien': self.toolwidgetmain.comboBox_entretiengeneral,

                                                            #eqp
                                                            'ouvertureequipement': self.toolwidgetmain.comboBox_etatouv
                                                            #'etat': self.toolwidgetmain.comboBox_etatgeneral,



                                                            }},
                                        'Objet': {'linkfield': 'id_objet',
                                                    'widgets': {'commentaire': self.toolwidgetmain.textEdit_comm}}}

            self.toolwidgetmain.toolButton_calc_nb.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.spinBox_nombre))

            self.dbasechildwdgfield = []
            self.instancekwargs['parentwidget'] = self

            if self.parentWidget is not None:
                self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(**self.instancekwargs)
                

                #self.propertieswdgOBSERVATION2 = BaseAssainissementObservationTool(**self.instancekwargs)
                #self.propertieswdgOBSERVATION2.initMainToolWidget()
                #self.propertieswdgOBSERVATION2.NAME = None
                #self.toolwidgetmain.tabWidget.widget(1).layout().addWidget(self.propertieswdgPHOTOGRAPHIE)
                self.dbasechildwdgfield += [self.propertieswdgPHOTOGRAPHIE]
                self.propertieswdgCROQUIS = BaseCroquisTool(**self.instancekwargs)
                self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)
                #self.toolwidgetmain.tabWidget.widget(2).layout().addWidget(self.propertieswdgCROQUIS)
                #self.dbasechildwdgfield += [self.propertieswdgCROQUIS]


    # def postInitFeatureProperties(self, feat):
    def postSelectFeature(self):
        if self.currentFeaturePK is None:
            datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            # self.initFeatureProperties(feat, self.dbasetablename, 'datetimeobservation', datecreation)
            self.formutils.applyResultDict({'datetimeobservation': datecreation}, checkifinforgottenfield=False)
            #applyResultDict(self, resultdict, checkifinforgottenfield=True):

        self.updateObservationStackedWidget()


    def updateObservationStackedWidget(self):
        dbasetabledesordre = self.dbase.dbasetables['Desordre']
        if ('groupedesordre' in dbasetabledesordre['fields'].keys()  ):
            if self.parentWidget is not None and self.parentWidget.currentFeaturePK is not None:
                grpdes = self.dbase.getValuesFromPk(self.parentWidget.DBASETABLENAME,
                                                    'groupedesordre',
                                                    self.parentWidget.currentFeaturePK)

                grpdescst = [elem[1] for elem in dbasetabledesordre['fields']['groupedesordre']['Cst']]
                indexgrp = grpdescst.index(grpdes)
                try:
                    self.toolwidgetmain.stackedWidget.setCurrentIndex(indexgrp)
                except:
                    pass

                if self.dbase.variante in [None, 'Lamia']:
                    if grpdes == 'NOD' and self.parentWidget.parentWidget is not None and self.parentWidget.parentWidget.currentFeaturePK is not None:
                        if self.parentWidget.parentWidget.DBASETABLENAME == 'Noeud':
                            currenttext = self.parentWidget.parentWidget.toolwidgetmain.comboBox_typeOuvrageAss.currentText()
                            typenoeud = self.dbase.getConstraintRawValueFromText('Noeud', 'typeOuvrageAss', currenttext)

                            if typenoeud in ['60','70', '71']:
                                self.toolwidgetmain.stackedWidget_2.setCurrentIndex(0)
                            elif typenoeud == '10':
                                self.toolwidgetmain.stackedWidget_2.setCurrentIndex(1)
                            else:
                                self.toolwidgetmain.stackedWidget_2.setCurrentIndex(3)

                elif self.dbase.variante in ['2018_SNCF']:
                    if grpdes == 'NOD' and self.parentWidget.parentWidget is not None and self.parentWidget.parentWidget.currentFeaturePK is not None:
                        if self.parentWidget.parentWidget.DBASETABLENAME == 'Noeud':
                            currenttext = self.parentWidget.parentWidget.toolwidgetmain.comboBox_typeOuvrageAss.currentText()
                            typenoeud = self.dbase.getConstraintRawValueFromText('Noeud', 'typeOuvrageAss', currenttext)
                            if typenoeud in ['60','70', '71']:
                                self.toolwidgetmain.stackedWidget_2.setCurrentIndex(0)
                            elif typenoeud == '10':
                                self.toolwidgetmain.stackedWidget_2.setCurrentIndex(1)
                            elif typenoeud == '21':
                                self.toolwidgetmain.stackedWidget_2.setCurrentIndex(2)
                            else:
                                self.toolwidgetmain.stackedWidget_2.setCurrentIndex(3)

                elif self.dbase.variante in ['CD41']:
                    if grpdes == 'NOD' and self.parentWidget.parentWidget is not None and self.parentWidget.parentWidget.currentFeaturePK is not None:
                        if self.parentWidget.parentWidget.DBASETABLENAME == 'Noeud':
                            currenttext = self.parentWidget.parentWidget.toolwidgetmain.comboBox_typeOuvrageAss.currentText()
                            typenoeud = self.dbase.getConstraintRawValueFromText('Noeud', 'typeOuvrageAss', currenttext)
                            if typenoeud in ['60']:
                                self.toolwidgetmain.stackedWidget_2.setCurrentIndex(0)
                            else:
                                self.toolwidgetmain.stackedWidget_2.setCurrentIndex(1)



class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabaseassainissement_observation_tool_ui.ui')
        uic.loadUi(uipath, self)

class UserUI_2(QWidget):
    def __init__(self, parent=None):
        super(UserUI_2, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabaseassainissement_observation_tool_ui_2018SNCF.ui')
        uic.loadUi(uipath, self)

class UserUI_3(QWidget):
    def __init__(self, parent=None):
        super(UserUI_3, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabaseassainissement_observation_tool_ui_CD41.ui')
        uic.loadUi(uipath, self)