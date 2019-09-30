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


# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore

try:
    from qgis.PyQt.QtGui import (QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget)



from ..base2.lamiabase_desordre_tool import BaseDesordreTool
from .lamiabasetramway_observation_tool import BaseTramwayObservationTool as BaseObservationTool


import os
import datetime
import qgis




class BaseTramwayDesordreTool(BaseDesordreTool):

    LOADFIRST = False
    dbasetablename = 'Desordre'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None, parentwidget=None, parent=None):
        super(BaseTramwayDesordreTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)


    def initFieldUI(self):
        # ****************************************************************************************
        #   userui Field
        if self.userwdgfield is None:
            # ****************************************************************************************
            # userui

            self.userwdgfield = UserUI()

            self.linkuserwdgfield = {'Desordre' : {'linkfield' : 'id_desordre',
                                             'widgets' : {'groupedesordre': self.userwdgfield.comboBox_groupedes
                                                          }},
                                'Objet' : {'linkfield' : 'id_objet',
                                          'widgets' : {}}}

            self.userwdgfield.comboBox_groupedes.currentIndexChanged.connect(self.changeGroupe)
            self.groupBox_attributes.setParent(None)

            # ****************************************************************************************
            # child widgets
            self.dbasechildwdgfield = []

            if self.parentWidget is None :

                self.propertieswdgOBSERVATION = BaseObservationTool(dbase=self.dbase, parentwidget=self)
                self.dbasechildwdgfield.append(self.propertieswdgOBSERVATION)


            self.propertieswdgOBSERVATION2 = BaseObservationTool(dbase=self.dbase, parentwidget=self)
            self.propertieswdgOBSERVATION2.NAME = None
            self.userwdgfield.tabWidget.widget(0).layout().addWidget(self.propertieswdgOBSERVATION2)
            self.dbasechildwdgfield.append(self.propertieswdgOBSERVATION2)

            self.userwdgfield.tabWidget.widget(1).layout().addWidget(self.propertieswdgOBSERVATION2.propertieswdgPHOTOGRAPHIE)
            self.userwdgfield.tabWidget.widget(2).layout().addWidget(self.propertieswdgOBSERVATION2.propertieswdgCROQUIS)







class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabasetramway_desordre_tool_ui.ui')
        uic.loadUi(uipath, self)