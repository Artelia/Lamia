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
from qgis.PyQt.QtWidgets import QWidget
from qgis.PyQt import uic, QtCore

from ...base3.qgswidgets.lamia_form_deficiency import BaseDeficiencyTool
from .lamia_form_observation import BaseUrbandrainageObservationTool


class BaseUrbandrainageDeficiencyTool(BaseDeficiencyTool):

    DBASETABLENAME = "deficiency"

    def __init__(self, **kwargs):
        super(BaseUrbandrainageDeficiencyTool, self).__init__(**kwargs)

    def initMainToolWidget(self):
        super().initMainToolWidget()
        """
        self.toolwidgetmain = UserUI()

        self.formtoolwidgetconfdictmain = {'Desordre' : {'linkfield' : 'id_desordre',
                                                        'widgets' : {'groupedesordre': self.toolwidgetmain.comboBox_groupedes
                                                        }},
                                            'Objet' : {'linkfield' : 'id_objet',
                                                        'widgets' : {}}}

        self.toolwidgetmain.comboBox_groupedes.currentIndexChanged.connect(self.changeGroupe)
        """

        # child widgets
        self.dbasechildwdgfield = []
        self.instancekwargs["parentwidget"] = self

        self.propertieswdgOBSERVATION = BaseUrbandrainageObservationTool(
            **self.instancekwargs
        )
        self.dbasechildwdgfield.append(self.propertieswdgOBSERVATION)
