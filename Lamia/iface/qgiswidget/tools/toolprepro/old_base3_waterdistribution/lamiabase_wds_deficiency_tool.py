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


from ..base3.lamiabase_deficiency_tool import BaseDeficiencyTool
from .lamiabase_wds_observation_tool import BaseWaterdistributionObservationTool


class BaseWaterdistributionDeficiencyTool(BaseDeficiencyTool):


    def __init__(self, **kwargs):
        super(BaseWaterdistributionDeficiencyTool, self).__init__(**kwargs)


    def initMainToolWidget(self):
        self.toolwidgetmain = UserUI()
        self.formtoolwidgetconfdictmain = {'deficiency' : {'linkfield' : 'id_deficiency',
                                                        'widgets' : {'deficiencycategory': self.toolwidgetmain.comboBox_groupedes,
                                                                    'deficiencytype': self.toolwidgetmain.comboBox_typedes,
                                                                    'deficiencyorigin': self.toolwidgetmain.comboBox_cause_des
                                                                    }},
                                            'object' : {'linkfield' : 'id_object',
                                                    'widgets' : {}}}

        self.toolwidgetmain.comboBox_groupedes.currentIndexChanged.connect(self.changeGroupe)
        # ****************************************************************************************
        # child widgets
        self.dbasechildwdgfield = []
        self.instancekwargs['parentwidget'] = self
        self.propertieswdgOBSERVATION = BaseWaterdistributionObservationTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgOBSERVATION)


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabase_wds_deficiency_tool_ui.ui')
        uic.loadUi(uipath, self)
