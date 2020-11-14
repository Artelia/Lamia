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
from qgis.PyQt.QtWidgets import QWidget

from ...base3.qgswidgets.lamia_form_observation import BaseObservationTool

from .lamia_form_camera import BaseWaterdistributionCameraTool
from .lamia_form_sketch import BaseWaterdistributionSketchTool


class BaseWaterdistributionObservationTool(BaseObservationTool):
    def __init__(self, **kwargs):
        super(BaseWaterdistributionObservationTool, self).__init__(**kwargs)

    def initMainToolWidget(self):

        self.toolwidgetmain = UserUI()
        self.formtoolwidgetconfdictmain = {
            "observation": {
                "linkfield": "id_observation",
                "widgets": {
                    # general
                    "datetimeobservation": self.toolwidgetmain.datetimeobservation,
                    "gravity": self.toolwidgetmain.gravity,
                    # infra
                    "number": self.toolwidgetmain.number,
                    "progression": self.toolwidgetmain.progression,
                    # noeud
                    "conditioncover": self.toolwidgetmain.conditioncover,
                    "conditionmanhole": self.toolwidgetmain.conditionmanhole,
                    # equip
                    "conditionglobal": [
                        self.toolwidgetmain.conditionglobal,
                        self.toolwidgetmain.conditionglobal_2,
                        self.toolwidgetmain.conditionglobal_3,
                    ],
                    "watercountervalue": self.toolwidgetmain.watercountervalue,
                    "handlingtest": self.toolwidgetmain.handlingtest,
                    # general
                    "nextactiontype": self.toolwidgetmain.nextactiontype,
                    "nextactioncomment": self.toolwidgetmain.nextactioncomment,
                },
            },
            "object": {
                "linkfield": "id_object",
                "widgets": {"comment": self.toolwidgetmain.comment},
            },
        }

        self.toolwidgetmain.toolButton_calc_nb.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.number)
        )

        self.toolwidgetmain.toolButton_indexcompteur.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.watercountervalue)
        )

        # ****************************************************************************************
        # child widgets
        self.dbasechildwdgfield = []
        self.instancekwargs["parentwidget"] = self
        self.propertieswdgPHOTOGRAPHIE = BaseWaterdistributionCameraTool(
            **self.instancekwargs
        )
        self.dbasechildwdgfield = [self.propertieswdgPHOTOGRAPHIE]
        self.propertieswdgCROQUIS = BaseWaterdistributionSketchTool(
            **self.instancekwargs
        )
        self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

    # def postInitFeatureProperties(self, feat):
    def postSelectFeature(self):
        super(BaseWaterdistributionObservationTool, self).postSelectFeature()
        self.updateObservationStackedWidget()

    def updateObservationStackedWidget(self):

        if (
            "deficiencycategory"
            in self.dbase.dbasetables["deficiency"]["fields"].keys()
        ):
            if (
                self.parentWidget is not None
                and self.parentWidget.currentFeaturePK is not None
            ):
                grpdes = self.dbase.getValuesFromPk(
                    self.parentWidget.DBASETABLENAME,
                    "deficiencycategory",
                    self.parentWidget.currentFeaturePK,
                )
                grpdescst = [
                    elem[1]
                    for elem in self.dbase.dbasetables["deficiency"]["fields"][
                        "deficiencycategory"
                    ]["Cst"]
                ]
                indexgrp = grpdescst.index(grpdes)
                try:
                    self.toolwidgetmain.stackedWidget.setCurrentIndex(indexgrp)
                except:
                    pass

                if (
                    grpdes == "NOD"
                    and self.parentWidget.parentWidget is not None
                    and self.parentWidget.parentWidget.currentFeaturePK is not None
                ):
                    # print('nodeobs')
                    if self.parentWidget.parentWidget.DBASETABLENAME == "node":
                        currenttext = (
                            self.parentWidget.parentWidget.toolwidgetmain.nodetype.currentText()
                        )
                        typeeqp = self.dbase.getConstraintRawValueFromText(
                            "node", "nodetype", currenttext
                        )

                        if typeeqp in [
                            "VEN",
                            "VID",
                            "REG",
                            "HYD",
                            "CHL",
                            "RPC",
                            "SPE",
                            "AUT",
                            "IND",
                        ]:
                            self.toolwidgetmain.stackedWidget_2.setCurrentIndex(0)
                        elif typeeqp in ["COM", "DEB"]:
                            self.toolwidgetmain.stackedWidget_2.setCurrentIndex(1)
                        elif typeeqp in ["VAN"]:
                            self.toolwidgetmain.stackedWidget_2.setCurrentIndex(2)
                        else:
                            self.toolwidgetmain.stackedWidget_2.setCurrentIndex(3)

                if (
                    grpdes == "EQP"
                    and self.parentWidget.parentWidget is not None
                    and self.parentWidget.parentWidget.currentFeaturePK is not None
                ):
                    if self.parentWidget.parentWidget.DBASETABLENAME == "equipment":
                        currenttext = (
                            self.parentWidget.parentWidget.toolwidgetmain.equipmenttype.currentText()
                        )
                        typenoeud = self.dbase.getConstraintRawValueFromText(
                            "equipment", "equipmenttype", currenttext
                        )

                        if typenoeud in ["CHE"]:
                            self.toolwidgetmain.stackedWidget_3.setCurrentIndex(0)
                        else:
                            self.toolwidgetmain.stackedWidget_3.setCurrentIndex(1)


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), "lamia_form_observation_ui.ui")
        uic.loadUi(uipath, self)
