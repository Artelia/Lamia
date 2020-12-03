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
import qgis
from qgis.PyQt.QtWidgets import QWidget

from ...base3.qgswidgets.lamia_form_equipment import BaseEquipmentTool
from .lamia_form_camera import BaseLeveeCameraTool
from .lamia_form_sketch import BaseLeveeSketchTool
from .lamia_form_deficiency import BaseLeveeDeficiencyTool

# from Lamia.qgisiface.iface.qgiswidget.tools.form_subwidgets.subwidget_createsubfeature import (
#     CreateSubFeatureWidget,
# )


class BaseLeveeEquipmentTool(BaseEquipmentTool):
    def __init__(self, **kwargs):
        super(BaseLeveeEquipmentTool, self).__init__(**kwargs)

    def initMainToolWidget(self):

        # if self.dbase.variante in [None, "Lamia"]:
        self.initMainToolWidgetLamia()

        if self.dbase.variante in ["SIRS"]:
            self.initMainToolWidgetSirs()

        self.dbasechildwdgfield = []
        self.instancekwargs["parentwidget"] = self

        if self.dbase.variante in [None, "Lamia"]:
            self.propertieswdgDesordre = BaseLeveeDeficiencyTool(**self.instancekwargs)
            self.propertieswdgDesordre.SKIP_LOADING_UI = True
            self.propertieswdgDesordre.TABLEFILTERFIELD = {"deficiencycategory": "EQP"}
            self.propertieswdgDesordre.initMainToolWidget()
            self.toolwidgetmain.equipmenttype.currentIndexChanged.connect(
                self.propertieswdgDesordre.propertieswdgOBSERVATION.equipementTypeChanged
            )
            self.dbasechildwdgfield.append(self.propertieswdgDesordre)

            # self.createdeficiencywdg = CreateSubFeatureWidget(
            #     self, self.propertieswdgDesordre, condition="equipmentcategory='OUH'"
            # )
            # self.lamiawidgets.append(self.createdeficiencywdg)

        self.propertieswdgPHOTOGRAPHIE = BaseLeveeCameraTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)

        self.propertieswdgCROQUIS = BaseLeveeSketchTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

        if self.parentWidget is None:
            self.propertieswdgEQUIPEMENT = BaseLeveeEquipmentTool(**self.instancekwargs)
            self.dbasechildwdgfield.append(self.propertieswdgEQUIPEMENT)

    def initMainToolWidgetLamia(self):
        self.toolwidgetmain = UserUI()
        self.formtoolwidgetconfdictmain = {
            "equipment": {
                "linkfield": "id_equipement",
                "widgets": {
                    "equipmentcategory": self.toolwidgetmain.equipmentcategory,
                    "side": self.toolwidgetmain.side,
                    "position": self.toolwidgetmain.position,
                    "equipmenttype": self.toolwidgetmain.equipmenttype,
                    "location": self.toolwidgetmain.location,
                    "flowtype": self.toolwidgetmain.flowtype,
                    "usage": self.toolwidgetmain.usage,
                    "height": [
                        self.toolwidgetmain.height,
                        self.toolwidgetmain.height_2,
                    ],
                    "width": [self.toolwidgetmain.width, self.toolwidgetmain.width_2,],
                    "equipmentsubtype": self.toolwidgetmain.equipmentsubtype,
                    "invert": self.toolwidgetmain.invert,
                    "safety": self.toolwidgetmain.safety,
                },
            },
            "object": {
                "linkfield": "id_object",
                "widgets": {
                    "comment": self.toolwidgetmain.comment,
                    "name": self.toolwidgetmain.name,
                },
            },
            "descriptionsystem": {"linkfield": "id_descriptionsystem", "widgets": {}},
        }

        self.toolwidgetmain.equipmentcategory.currentIndexChanged.connect(
            self.changeCategorie
        )

        self.toolwidgetmain.toolButton_calch.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.height)
        )
        self.toolwidgetmain.toolButton__calcv.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.width)
        )
        self.toolwidgetmain.toolButton_calch_2.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.height_2)
        )
        self.toolwidgetmain.toolButton_dimhoriz2.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.width_2)
        )
        self.toolwidgetmain.toolButton_fildeau.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.invert)
        )

        self.toolwidgetmain.equipmenttype.currentIndexChanged.connect(
            self.typeponctuelChanged
        )

    def initMainToolWidgetSirs(self):
        self.toolwidgetmain.safety.setEnabled(False)
        try:
            self.toolwidgetmain.equipmenttype.currentIndexChanged.disconnect(
                self.typeponctuelChanged
            )
        except:
            pass
        self.toolwidgetmain.stackedWidget_2.setCurrentIndex(1)

    def initMainToolWidgetSirs_old(self):
        self.toolwidgetmain = UserUISirs()
        self.formtoolwidgetconfdictmain = {
            "equipment": {
                "linkfield": "id_equipment",
                "widgets": {
                    "equipmentcategory": self.toolwidgetmain.equipmentcategory,
                    "side": self.toolwidgetmain.side,
                    "position": self.toolwidgetmain.position,
                    "equipmenttype": self.toolwidgetmain.equipmenttype,
                    "location": self.toolwidgetmain.location,
                    "flowtype": self.toolwidgetmain.flowtype,
                    "usage": self.toolwidgetmain.usage,
                    "height": self.toolwidgetmain.height,
                    "width": self.toolwidgetmain.width,
                    "safety": self.toolwidgetmain.safety,
                },
            },
            "object": {
                "linkfield": "id_object",
                "widgets": {"comment": self.toolwidgetmain.comment},
            },
            "descriptionsystem": {"linkfield": "id_descriptionsystem", "widgets": {}},
        }

        self.toolwidgetmain.equipmentcategory.currentIndexChanged.connect(
            self.changeCategorie
        )

        self.toolwidgetmain.toolButton_calch.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.height)
        )
        self.toolwidgetmain.toolButton__calcv.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.width)
        )

    def postSaveFeature(self, savedfeaturepk=None):
        pass

    def typeponctuelChanged(self, comboindex):

        currenttext = self.toolwidgetmain.equipmenttype.currentText()
        currentval = self.dbase.getConstraintRawValueFromText(
            "equipment", "equipmenttype", currenttext
        )

        if currentval in ["CLA", "VAN", "EXU", "FLO"]:
            self.toolwidgetmain.stackedWidget_2.setCurrentIndex(0)
        else:
            self.toolwidgetmain.stackedWidget_2.setCurrentIndex(1)

    def changeCategorie(self, intcat=None):
        combotxt = self.toolwidget.equipmentcategory.currentText()
        catval = self.dbase.getConstraintRawValueFromText(
            "equipment", "equipmentcategory", combotxt
        )

        if catval[0] == "O":
            self.toolwidget.stackedWidget.setCurrentIndex(1)
            self.mainifacewidget.actiontoobargeomnewpoint.setEnabled(True)
            self.mainifacewidget.actiontoobargeomnewline.setEnabled(False)

        elif catval[0] == "R":
            self.toolwidget.stackedWidget.setCurrentIndex(0)
            self.mainifacewidget.actiontoobargeomnewpoint.setEnabled(False)
            self.mainifacewidget.actiontoobargeomnewline.setEnabled(True)
        else:
            pass

    def postSelectFeature(self):
        super().postSelectFeature()
        self.changeCategorie()


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), "lamia_form_equipment_ui.ui")
        uic.loadUi(uipath, self)

