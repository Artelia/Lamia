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
from .lamia_form_camera import BaseUrbandrainageCameraTool
from .lamia_form_sketch import BaseUrbandrainageSketchTool


class BaseUrbandrainageObservationTool(BaseObservationTool):
    def __init__(self, **kwargs):
        super(BaseUrbandrainageObservationTool, self).__init__(**kwargs)

    def initMainToolWidget(self):

        if self.dbase.variante in [None, "Lamia"]:

            self.toolwidgetmain = UserUI()
            self.formtoolwidgetconfdictmain = {
                "observation": {
                    "linkfield": "id_observation",
                    "widgets": {
                        "datetimeobservation": self.toolwidgetmain.datetimeobservation,
                        #'nombre' : self.toolwidgetmain.spinBox_nombre,
                        "gravity": self.toolwidgetmain.gravity,
                        # regard
                        "conditioncover": [
                            self.toolwidgetmain.conditioncover,
                            self.toolwidgetmain.conditioncover_2,
                        ],
                        "conditionstep": self.toolwidgetmain.conditionstep,
                        "conditionmanhole": self.toolwidgetmain.conditionmanhole,
                        "conditionculvert": self.toolwidgetmain.conditionculvert,
                        "presenceinfiltrationtosewer": self.toolwidgetmain.presenceinfiltrationtosewer,
                        "presenceinfiltration": self.toolwidgetmain.presenceinfiltration,
                        "presenceroots": self.toolwidgetmain.presenceroots,
                        "presenceh2s": self.toolwidgetmain.presenceh2s,
                        "presencesediments": [
                            self.toolwidgetmain.presencesediments,
                            self.toolwidgetmain.presencesediments_2,
                        ],
                        "presencepressurizedflow": self.toolwidgetmain.presencepressurizedflow,
                        "maintenanceopinion": self.toolwidgetmain.maintenanceopinion,
                        # DIV
                        "conditionglobal": [
                            self.toolwidgetmain.conditionglobal,
                            self.toolwidgetmain.conditionglobal_2,
                            self.toolwidgetmain.conditionglobal_3,
                        ],
                        # PR
                        "conditioncontroller": self.toolwidgetmain.conditioncontroller,
                        #'evolution': self.toolwidgetmain.textEdit_evolution,
                        #'commentaires': self.toolwidgetmain.textEdit_comm,
                        # "suite": self.toolwidgetmain.textEdit_suite,
                        "nextactiontype": self.toolwidgetmain.nextactiontype,
                        "nextactioncomment": self.toolwidgetmain.nextactioncomment,
                        "nextactionsubtype": self.toolwidgetmain.nextactionsubtype,
                    },
                },
                "object": {
                    "linkfield": "id_object",
                    "widgets": {"comment": self.toolwidgetmain.comment},
                },
            }

            self.toolwidgetmain.toolButton_calc_nb.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.spinBox_nombre)
            )

            # ****************************************************************************************
            # child widgets
            self.dbasechildwdgfield = []
            self.instancekwargs["parentwidget"] = self
            if self.parentWidget is not None:
                self.propertieswdgPHOTOGRAPHIE = BaseUrbandrainageCameraTool(
                    **self.instancekwargs
                )
                self.dbasechildwdgfield = [self.propertieswdgPHOTOGRAPHIE]
                self.propertieswdgCROQUIS = BaseUrbandrainageSketchTool(
                    **self.instancekwargs
                )
                self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

        elif self.dbase.variante in ["2018_SNCF"]:
            self.toolwidgetmain = UserUI_2()
            self.formtoolwidgetconfdictmain = {
                "observation": {
                    "linkfield": "id_observation",
                    "widgets": {
                        "datetimeobservation": self.toolwidgetmain.datetimeobservation,
                        # 'nombre' : self.toolwidgetmain.spinBox_nombre,
                        "gravity": self.toolwidgetmain.gravity,
                        # regard
                        "conditioncover": [
                            self.toolwidgetmain.conditioncover,
                            self.toolwidgetmain.conditioncover_2,
                        ],
                        "conditionstep": self.toolwidgetmain.conditionstep,
                        "conditionmanhole": self.toolwidgetmain.conditionmanhole,
                        "conditionculvert": self.toolwidgetmain.conditionculvert,
                        "presenceh2s": self.toolwidgetmain.presenceh2s,
                        "presencesediments": [
                            self.toolwidgetmain.presencesediments,
                            self.toolwidgetmain.presencesediments_2,
                        ],
                        "presencepressurizedflow": self.toolwidgetmain.presencepressurizedflow,
                        "maintenanceopinion": self.toolwidgetmain.maintenanceopinion,
                        # PR
                        # 'etattampon': self.toolwidgetmain.comboBox_PRetattampon,
                        "conditionglobal": [
                            self.toolwidgetmain.conditionglobal,
                            self.toolwidgetmain.conditionglobal_2,
                            self.toolwidgetmain.conditionglobal_3,
                        ],
                        "conditioncontroller": self.toolwidgetmain.conditioncontroller,
                        # DSH
                        # 'etatgeneral': self.toolwidgetmain.comboBox_DSHetageneral,
                        # 'ensablement': self.toolwidgetmain.comboBox_DSHencombrement,
                        # DIC
                        # 'etatgeneral': self.toolwidgetmain.comboBox_DIVetatgeneral,
                    },
                },
                "object": {
                    "linkfield": "id_object",
                    "widgets": {"comment": self.toolwidgetmain.comment},
                },
            }

            self.toolwidgetmain.toolButton_calc_nb.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.spinBox_nombre)
            )

            self.dbasechildwdgfield = []
            self.instancekwargs["parentwidget"] = self
            if self.parentWidget is not None:
                self.propertieswdgPHOTOGRAPHIE = BaseUrbandrainageCameraTool(
                    **self.instancekwargs
                )
                self.dbasechildwdgfield = [self.propertieswdgPHOTOGRAPHIE]
                self.propertieswdgCROQUIS = BaseUrbandrainageSketchTool(
                    **self.instancekwargs
                )
                self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)
        elif self.dbase.variante in ["CD41"]:

            self.toolwidgetmain = UserUI_3()
            self.formtoolwidgetconfdictmain = {
                "observation": {
                    "linkfield": "id_observation",
                    "widgets": {
                        "datetimeobservation": self.toolwidgetmain.datetimeobservation,
                        # 'nombre' : self.toolwidgetmain.spinBox_nombre,
                        "gravity": self.toolwidgetmain.gravity,
                        "conditionglobal": self.toolwidgetmain.conditionglobal,
                        # regard
                        "conditioncover": self.toolwidgetmain.conditioncover,
                        "conditionstep": self.toolwidgetmain.conditionstep,
                        "conditionmanhole": self.toolwidgetmain.conditionmanhole,
                        "conditionculvert": self.toolwidgetmain.conditionculvert,
                        "presenceh2s": self.toolwidgetmain.presenceh2s,
                        "presencesediments": self.toolwidgetmain.presencesediments,
                        "presencepressurizedflow": self.toolwidgetmain.presencepressurizedflow,
                        "maintenanceopinion": self.toolwidgetmain.maintenanceopinion,
                        # eqp
                        "equipmentopenclose": self.toolwidgetmain.equipmentopenclose
                        #'etat': self.toolwidgetmain.comboBox_etatgeneral,
                    },
                },
                "object": {
                    "linkfield": "id_object",
                    "widgets": {"comment": self.toolwidgetmain.comment},
                },
            }

            self.toolwidgetmain.toolButton_calc_nb.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.spinBox_nombre)
            )

            self.dbasechildwdgfield = []
            self.instancekwargs["parentwidget"] = self

            if self.parentWidget is not None:
                self.propertieswdgPHOTOGRAPHIE = BaseUrbandrainageCameraTool(
                    **self.instancekwargs
                )
                self.dbasechildwdgfield = [self.propertieswdgPHOTOGRAPHIE]
                self.propertieswdgCROQUIS = BaseUrbandrainageSketchTool(
                    **self.instancekwargs
                )
                self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

    # def postInitFeatureProperties(self, feat):
    def postSelectFeature(self):
        super(BaseUrbandrainageObservationTool, self).postSelectFeature()
        self.updateObservationStackedWidget()

    def updateObservationStackedWidget(self):
        dbasetabledesordre = self.dbase.dbasetables["deficiency"]
        if "deficiencycategory" in dbasetabledesordre["fields"].keys():
            if (
                self.parentWidget is not None
                and self.parentWidget.currentFeaturePK is not None
            ):

                grpdes = self.dbase.getValuesFromPk(
                    self.parentWidget.DBASETABLENAME,
                    "deficiencycategory",
                    self.parentWidget.currentFeaturePK,
                )
                """
                grpdescst = [elem[1] for elem in dbasetabledesordre['fields']['groupedesordre']['Cst']]
                indexgrp = grpdescst.index(grpdes)
                try:
                    self.toolwidgetmain.stackedWidget.setCurrentIndex(indexgrp)
                except:
                    pass
                """
                if self.dbase.variante in [None, "Lamia"]:
                    if (
                        grpdes == "NOD"
                        and self.parentWidget.parentWidget is not None
                        and self.parentWidget.parentWidget.currentFeaturePK is not None
                    ):
                        if self.parentWidget.parentWidget.DBASETABLENAME == "node":
                            currenttext = (
                                self.parentWidget.parentWidget.toolwidgetmain.nodetype.currentText()
                            )
                            typenoeud = self.dbase.getConstraintRawValueFromText(
                                "node", "nodetype", currenttext
                            )

                            if typenoeud in ["60", "70", "71"]:
                                self.toolwidgetmain.stackedWidget_2.setCurrentIndex(0)
                            elif typenoeud == "10":
                                self.toolwidgetmain.stackedWidget_2.setCurrentIndex(1)
                            else:
                                self.toolwidgetmain.stackedWidget_2.setCurrentIndex(3)

                elif self.dbase.variante in ["2018_SNCF"]:
                    if (
                        grpdes == "NOD"
                        and self.parentWidget.parentWidget is not None
                        and self.parentWidget.parentWidget.currentFeaturePK is not None
                    ):
                        if self.parentWidget.parentWidget.DBASETABLENAME == "node":
                            currenttext = (
                                self.parentWidget.parentWidget.toolwidgetmain.nodetype.currentText()
                            )
                            typenoeud = self.dbase.getConstraintRawValueFromText(
                                "node", "nodetype", currenttext
                            )
                            if typenoeud in ["60", "70", "71"]:
                                self.toolwidgetmain.stackedWidget_2.setCurrentIndex(0)
                            elif typenoeud == "10":
                                self.toolwidgetmain.stackedWidget_2.setCurrentIndex(1)
                            elif typenoeud == "21":
                                self.toolwidgetmain.stackedWidget_2.setCurrentIndex(2)
                            else:
                                self.toolwidgetmain.stackedWidget_2.setCurrentIndex(3)

                elif self.dbase.variante in ["CD41"]:
                    if (
                        grpdes == "NOD"
                        and self.parentWidget.parentWidget is not None
                        and self.parentWidget.parentWidget.currentFeaturePK is not None
                    ):
                        if self.parentWidget.parentWidget.DBASETABLENAME == "node":
                            currenttext = (
                                self.parentWidget.parentWidget.toolwidgetmain.nodetype.currentText()
                            )
                            typenoeud = self.dbase.getConstraintRawValueFromText(
                                "node", "nodetype", currenttext
                            )
                            if typenoeud in ["60"]:
                                self.toolwidgetmain.stackedWidget_2.setCurrentIndex(0)
                            else:
                                self.toolwidgetmain.stackedWidget_2.setCurrentIndex(1)


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), "lamia_form_observation_ui.ui")
        uic.loadUi(uipath, self)


class UserUI_2(QWidget):
    def __init__(self, parent=None):
        super(UserUI_2, self).__init__(parent=parent)
        uipath = os.path.join(
            os.path.dirname(__file__), "lamia_form_observation_ui_2018SNCF.ui"
        )
        uic.loadUi(uipath, self)


class UserUI_3(QWidget):
    def __init__(self, parent=None):
        super(UserUI_3, self).__init__(parent=parent)
        uipath = os.path.join(
            os.path.dirname(__file__), "lamia_form_observation_ui_CD41.ui"
        )
        uic.loadUi(uipath, self)
