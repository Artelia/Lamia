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
from .lamiabaseeclairagepublic_photo_tool import BaseEclairagePublicPhotoTool as BasePhotoTool
from .lamiabaseeclairagepublic_croquis_tool import BaseCroquisTool



class BaseEclairagePublicObservationTool(BaseObservationTool):


    def __init__(self, **kwargs):
        super(BaseEclairagePublicObservationTool, self).__init__(**kwargs)

    def initMainToolWidget(self):

        if self.dbase.variante in [None, 'Lamia']:

            self.toolwidgetmain = UserUI()

            self.formtoolwidgetconfdictmain = {'Observation': {'linkfield': 'id_observation',
                                                            'widgets': {
                                                                'datetimeobservation': self.toolwidgetmain.dateTimeEdit,
                                                                'nombre': self.toolwidgetmain.spinBox_nombre,
                                                                #'longueurdes': self.toolwidgetmain.doubleSpinBox_longueur,
                                                                'gravite': self.toolwidgetmain.comboBox_urgence,

                                                                #infralin
                                                                'etatgeneral': [self.toolwidgetmain.comboBox_etatgen,
                                                                                self.toolwidgetmain.comboBox_etatgen2],

                                                                #node
                                                                'etatsupport': self.toolwidgetmain.comboBox_etatsupport,
                                                                'etatraccordement': self.toolwidgetmain.comboBox_etatraccordement,
                                                                'etatcrosse': self.toolwidgetmain.comboBox_etatcrosse,

                                                                #eqp
                                                                #'etatgeneral': self.toolwidgetmain.comboBox_etatgen2,




                                                                'evolution': self.toolwidgetmain.textEdit_evolution,
                                                                'typesuite': self.toolwidgetmain.comboBox_typesuite,
                                                                'commentairesuite': self.toolwidgetmain.textEdit_suite}},
                                            'Objet': {'linkfield': 'id_objet',
                                                    'widgets': {'commentaire': self.toolwidgetmain.textEdit_comm}}}


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




        # def postInitFeatureProperties(self, feat):
    def postSelectFeature(self):
        super(BaseEclairagePublicObservationTool, self).postSelectFeature()
        self.updateObservationStackedWidget()

    def updateObservationStackedWidget(self):

        if ('groupedesordre' in self.dbase.dbasetables['Desordre']['fields'].keys()  ):
            if self.parentWidget is not None and self.parentWidget.currentFeaturePK is not None:
                #grpdes = self.parentWidget.currentFeature['groupedesordre']
                grpdes = self.dbase.getValuesFromPk(self.parentWidget.DBASETABLENAME,
                                                     'groupedesordre',
                                                      self.parentWidget.currentFeaturePK )
                grpdescst = [elem[1] for elem in self.dbase.dbasetables['Desordre']['fields']['groupedesordre']['Cst']]
                indexgrp = grpdescst.index(grpdes)
                try:
                    self.toolwidgetmain.stackedWidget.setCurrentIndex(indexgrp)
                except:
                    pass
                if (grpdes == 'EQP' and self.parentWidget.parentWidget is not None 
                        and self.parentWidget.parentWidget.currentFeaturePK is not None):
                    if self.parentWidget.parentWidget.DBASETABLENAME == 'Equipement':
                        #typenoeud = self.parentWidget.parentWidget.currentFeature['typeOuvrageAss']
                        currenttext = self.parentWidget.parentWidget.toolwidgetmain.comboBox_cat.currentText()
                        # typenoeud = self.parentWidget.parentWidget.currentFeature['typeOuvrageAss']
                        typeeqp = self.dbase.getConstraintRawValueFromText('Equipement', 'categorie', currenttext)

                        if typeeqp in ['FOY']:
                            self.toolwidgetmain.stackedWidget_2.setCurrentIndex(0)
                        else:
                            self.toolwidgetmain.stackedWidget_2.setCurrentIndex(1)

                if (grpdes == 'NOD' and self.parentWidget.parentWidget is not None 
                        and self.parentWidget.parentWidget.currentFeaturePK is not None):
                    if self.parentWidget.parentWidget.DBASETABLENAME == 'Noeud':
                        #typenoeud = self.parentWidget.parentWidget.currentFeature['typeOuvrageAss']
                        currenttext = self.parentWidget.parentWidget.toolwidgetmain.comboBox_typenoeud.currentText()
                        # typenoeud = self.parentWidget.parentWidget.currentFeature['typeOuvrageAss']
                        typenoeud = self.dbase.getConstraintRawValueFromText('Noeud', 'typenoeud', currenttext)

                        if typenoeud in ['LOC']:
                            self.toolwidgetmain.stackedWidget_3.setCurrentIndex(0)
                        else:
                            self.toolwidgetmain.stackedWidget_3.setCurrentIndex(1)







class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabaseeclairagepublic_observation_tool_ui.ui')
        uic.loadUi(uipath, self)


