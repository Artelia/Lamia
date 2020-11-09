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
from collections import OrderedDict


from qgis.PyQt import uic, QtCore
from qgis.PyQt.QtWidgets import QWidget


from ...base3.qgswidgets.lamia_form_deficiency import BaseDeficiencyTool
from .lamia_form_observation import BaseLeveeObservationTool


class BaseLeveeDeficiencyTool(BaseDeficiencyTool):
    def __init__(self, **kwargs):
        super(BaseLeveeDeficiencyTool, self).__init__(**kwargs)

    def initMainToolWidget(self):

        self.toolwidgetmain = UserUI()

        self.formtoolwidgetconfdictmain = {
            "deficiency": {
                "linkfield": "id_deficiency",
                "widgets": OrderedDict(
                    [
                        ("deficiencycategory", self.toolwidgetmain.comboBox_groupedes),
                        ("side", self.toolwidgetmain.comboBox_cote),
                        ("position", self.toolwidgetmain.comboBox_position),
                        ("deficiencytype", self.toolwidgetmain.comboBox_des_cat),
                        ("deficiencysubtype", self.toolwidgetmain.comboBox_des_type),
                        (
                            "deficiencysubsubtype",
                            self.toolwidgetmain.comboBox_sstypedes,
                        ),
                    ]
                ),
            },
            "object": {"linkfield": "id_object", "widgets": {}},
        }

        self.toolwidgetmain.comboBox_groupedes.currentIndexChanged.connect(
            self.changeGroupe
        )
        # ****************************************************************************************
        # child widgets
        self.dbasechildwdgfield = []
        self.instancekwargs["parentwidget"] = self

        self.propertieswdgOBSERVATION = BaseLeveeObservationTool(**self.instancekwargs)
        self.propertieswdgOBSERVATION.tooltreewidgetSUBCAT = "Observation"
        self.dbasechildwdgfield.append(self.propertieswdgOBSERVATION)

        if self.dbase.variante in ["SIRS"]:
            self.toolwidgetmain.comboBox_sstypedes.setEnabled(False)

    def postSelectFeature(self):
        super().postSelectFeature()

    def _checkSameGeomAsParentNode(self):
        pass

    def postSaveFeature(self, savedfeaturepk=None):
        super().postSaveFeature(savedfeaturepk)


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), "lamia_form_deficiency_ui.ui")
        uic.loadUi(uipath, self)
