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
                        "datetimeobservation": self.toolwidgetmain.dateTimeEdit,
                        #'nombre' : self.toolwidgetmain.spinBox_nombre,
                        "gravity": self.toolwidgetmain.comboBox_urgence,
                        # regard
                        "conditioncover": [
                            self.toolwidgetmain.comboBox_etattampon,
                            self.toolwidgetmain.comboBox_PRetattampon,
                        ],
                        "conditionstep": self.toolwidgetmain.comboBox_etatechelon,
                        "conditionmanhole": self.toolwidgetmain.comboBox_etatregard,
                        "conditionculvert": self.toolwidgetmain.comboBox_etatcunette,
                        "presenceinfiltrationtosewer": self.toolwidgetmain.comboBox_ecpp,
                        "presenceinfiltration": self.toolwidgetmain.comboBox_infiltration,
                        "presenceroots": self.toolwidgetmain.comboBox_racines,
                        "presenceh2s": self.toolwidgetmain.comboBox_h2s,
                        "presencesediments": [
                            self.toolwidgetmain.comboBox_depot,
                            self.toolwidgetmain.comboBox_DSHencombrement,
                        ],
                        "presencepressurizedflow": self.toolwidgetmain.comboBox_miseencharge,
                        "maintenanceopinion": self.toolwidgetmain.comboBox_entretiengeneral,
                        # DIV
                        "conditionglobal": self.toolwidgetmain.comboBox_DIVetatgeneral,
                        #'evolution': self.toolwidgetmain.textEdit_evolution,
                        #'commentaires': self.toolwidgetmain.textEdit_comm,
                        #'suite': self.toolwidgetmain.textEdit_suite,
                        "nextactiontype": self.toolwidgetmain.comboBox_typesuite,
                        "nextactioncomment": self.toolwidgetmain.comboBox_precisionsuite,
                    },
                },
                "object": {
                    "linkfield": "id_object",
                    "widgets": {"comment": self.toolwidgetmain.textEdit_comm},
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
                        "datetimeobservation": self.toolwidgetmain.dateTimeEdit,
                        # 'nombre' : self.toolwidgetmain.spinBox_nombre,
                        "gravity": self.toolwidgetmain.comboBox_urgence,
                        # regard
                        "conditioncover": [
                            self.toolwidgetmain.comboBox_etattampon,
                            self.toolwidgetmain.comboBox_PRetattampon,
                        ],
                        "conditionstep": self.toolwidgetmain.comboBox_etatechelon,
                        "conditionmanhole": self.toolwidgetmain.comboBox_etatregard,
                        "conditionculvert": self.toolwidgetmain.comboBox_etatcunette,
                        "presenceh2s": self.toolwidgetmain.comboBox_h2s,
                        "presencesediments": [
                            self.toolwidgetmain.comboBox_depot,
                            self.toolwidgetmain.comboBox_DSHencombrement,
                        ],
                        "presencepressurizedflow": self.toolwidgetmain.comboBox_miseencharge,
                        "maintenanceopinion": self.toolwidgetmain.comboBox_entretiengeneral,
                        # PR
                        # 'etattampon': self.toolwidgetmain.comboBox_PRetattampon,
                        "conditionglobal": [
                            self.toolwidgetmain.comboBox_etatbache,
                            self.toolwidgetmain.comboBox_DSHetageneral,
                            self.toolwidgetmain.comboBox_DIVetatgeneral,
                        ],
                        "conditioncontroller": self.toolwidgetmain.comboBox_etatasservissement,
                        # DSH
                        # 'etatgeneral': self.toolwidgetmain.comboBox_DSHetageneral,
                        # 'ensablement': self.toolwidgetmain.comboBox_DSHencombrement,
                        # DIC
                        # 'etatgeneral': self.toolwidgetmain.comboBox_DIVetatgeneral,
                    },
                },
                "object": {
                    "linkfield": "id_object",
                    "widgets": {"comment": self.toolwidgetmain.textEdit_comm},
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
                        "datetimeobservation": self.toolwidgetmain.dateTimeEdit,
                        # 'nombre' : self.toolwidgetmain.spinBox_nombre,
                        "gravity": self.toolwidgetmain.comboBox_urgence,
                        "conditionglobal": self.toolwidgetmain.comboBox_etatgeneral,
                        # regard
                        "conditioncover": self.toolwidgetmain.comboBox_etattampon,
                        "conditionstep": self.toolwidgetmain.comboBox_etatechelon,
                        "conditionmanhole": self.toolwidgetmain.comboBox_etatregard,
                        "conditionculvert": self.toolwidgetmain.comboBox_etatcunette,
                        "presenceh2s": self.toolwidgetmain.comboBox_h2s,
                        "presencesediments": self.toolwidgetmain.comboBox_depot,
                        "presencepressurizedflow": self.toolwidgetmain.comboBox_miseencharge,
                        "maintenanceopinion": self.toolwidgetmain.comboBox_entretiengeneral,
                        # eqp
                        "equipmentopenclose": self.toolwidgetmain.comboBox_etatouv
                        #'etat': self.toolwidgetmain.comboBox_etatgeneral,
                    },
                },
                "object": {
                    "linkfield": "id_object",
                    "widgets": {"comment": self.toolwidgetmain.textEdit_comm},
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
                                self.parentWidget.parentWidget.toolwidgetmain.comboBox_typeOuvrageAss.currentText()
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
                                self.parentWidget.parentWidget.toolwidgetmain.comboBox_typeOuvrageAss.currentText()
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
                                self.parentWidget.parentWidget.toolwidgetmain.comboBox_typeOuvrageAss.currentText()
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
