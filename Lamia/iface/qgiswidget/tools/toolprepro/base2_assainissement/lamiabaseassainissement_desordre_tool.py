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
from qgis.PyQt.QtWidgets import (QWidget)
from qgis.PyQt import uic, QtCore

from ..base2.lamiabase_desordre_tool import BaseDesordreTool
from .lamiabaseassainissement_observation_tool import BaseAssainissementObservationTool


class BaseAssainissementDesordreTool(BaseDesordreTool):

    DBASETABLENAME = 'Desordre'

    def __init__(self, **kwargs):
        super(BaseAssainissementDesordreTool, self).__init__(**kwargs)

    """
    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Desordre'
        self.NAME = 'Desordre'
        self.dbasetablename = 'Desordre'
        #self.visualmode = [1, 2]
        self.PointENABLED = True
        self.LineENABLED = True
        # self.PolygonEnabled = True
        self.magicfunctionENABLED = True

        self.linkagespec = {'Descriptionsystem' : {'tabletc' : None,
                                              'idsource' : 'lk_descriptionsystem',
                                            'idtcsource' : None,
                                           'iddest' : 'id_descriptionsystem',
                                           'idtcdest' : None,
                                           'desttable' : ['Infralineaire','Equipement','Noeud']}}


        self.pickTable = {'LkDesSys': {'TRONCON': 'IdSys'}}
        self.iconpath = os.path.join(os.path.dirname(__file__), 'lamiadefault_desordre_tool_icon.png')

        # ****************************************************************************************
        #properties ui
        pass
    """

    def initMainToolWidget(self):

        self.toolwidgetmain = UserUI()

        self.formtoolwidgetconfdictmain = {'Desordre' : {'linkfield' : 'id_desordre',
                                                        'widgets' : {'groupedesordre': self.toolwidgetmain.comboBox_groupedes
                                                        }},
                                            'Objet' : {'linkfield' : 'id_objet',
                                                        'widgets' : {}}}

        self.toolwidgetmain.comboBox_groupedes.currentIndexChanged.connect(self.changeGroupe)
        # ****************************************************************************************
        # child widgets
        self.dbasechildwdgfield = []
        self.instancekwargs['parentwidget'] = self
        #if self.parentWidget is None :
        if True:

            self.propertieswdgOBSERVATION = BaseAssainissementObservationTool(**self.instancekwargs)
            self.dbasechildwdgfield.append(self.propertieswdgOBSERVATION)

        """
        self.propertieswdgOBSERVATION2 = BaseAssainissementObservationTool(**self.instancekwargs)
        #self.propertieswdgOBSERVATION2.initMainToolWidget()
        #self.propertieswdgOBSERVATION2.NAME = None
        #self.toolwidgetmain.framechildtoolwidg.layout().addWidget(self.propertieswdgOBSERVATION2)
        self.dbasechildwdgfield.append(self.propertieswdgOBSERVATION2)

        #self.toolwidgetmain.tabWidget.widget(1).layout().addWidget(self.propertieswdgOBSERVATION2.propertieswdgPHOTOGRAPHIE)
        #self.toolwidgetmain.tabWidget.widget(2).layout().addWidget(self.propertieswdgOBSERVATION2.propertieswdgCROQUIS)
        """


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabaseassainissement_desordre_tool_ui.ui')
        uic.loadUi(uipath, self)
