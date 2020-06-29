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
from qgis.PyQt.QtWidgets import QWidget
from qgis.PyQt import uic, QtCore

from ...base3.qgswidgets.lamia_form_edge import BaseEdgeTool
from .lamia_form_graph import BaseUrbandrainageGraphTool
from Lamia.iface.qgiswidget.tools.form_subwidgets.subwidget_lidchooser import (
    LidChooserWidget,
)
from Lamia.iface.qgiswidget.tools.form_subwidgets.subwidget_edgetonode import (
    EdgeToNodeWidget,
)


class BaseUrbandrainageEdgeTool(BaseEdgeTool):
    def __init__(self, **kwargs):
        super(BaseUrbandrainageEdgeTool, self).__init__(**kwargs)

    def initMainToolWidget(self):
        if self.dbase.variante in [None, "Lamia", "2018_SNCF"]:
            self._initMainToolWidgetLamia()

        elif self.dbase.variante in ["CD41"]:
            self._initMainToolWidgetCD41()

        if self.dbase.variante in [None, "Lamia"]:
            self.propertieswdgGRAPH = BaseUrbandrainageGraphTool(
                **self.instancekwargsforchildwdg
            )
            self.dbasechildwdgfield.append(self.propertieswdgGRAPH)

        self.edgetonode = EdgeToNodeWidget(
            self,
            lateralfield="laterals",
            upstreamnodeidfield="lid_descriptionsystem_1",
            downstreamnodeidfield="lid_descriptionsystem_2",
            parentframe=self.toolwidgetmain.frame_edgetonode,
        )
        self.lamiawidgets.append(self.edgetonode)

    def _initMainToolWidgetLamia(self):
        self.toolwidgetmain = UserUIField()
        self.formtoolwidgetconfdictmain = {
            "edge": {
                "linkfield": "id_edge",
                "widgets": {
                    #'sewertype': self.toolwidgetmain.comboBox_typeReseau,
                    "pipetype": self.toolwidgetmain.comboBox_pipetype,
                    "pipesubtype": self.toolwidgetmain.comboBox_pipesubtype,
                    "laterals": self.toolwidgetmain.comboBox_branch,
                    "flowtype": self.toolwidgetmain.comboBox_typeecoul,
                    "pipeshape": self.toolwidgetmain.comboBox_formecana,
                    "material": self.toolwidgetmain.comboBox_materiau,
                    #'anPoseInf': self.toolwidgetmain.dateEdit_anneepose,
                    "nominaldiameter": self.toolwidgetmain.doubleSpinBox_diametreNominal,
                    "height": self.toolwidgetmain.doubleSpinBox_haut,
                    # 'largeur': self.toolwidgetmain.doubleSpinBox_larg,
                    # 'altAmont': self.toolwidgetmain.doubleSpinBox_altAmont,
                    # 'altAmont': self.toolwidgetmain.doubleSpinBox_altAval,
                    "depthup": self.toolwidgetmain.doubleSpinBox_profamont,
                    "depthdown": self.toolwidgetmain.doubleSpinBox_profaval,
                    # 'lid_descriptionsystem_1': self.toolwidgetmain.spinBox_lk_noeud1,
                    # 'lid_descriptionsystem_2': self.toolwidgetmain.spinBox_lk_noeud2
                },
            },
            "object": {
                "linkfield": "id_object",
                "widgets": {"comment": self.toolwidgetmain.textBrowser_commentaire},
            },
            "descriptionsystem": {
                "linkfield": "id_descriptionsystem",
                "widgets": {
                    "networktype": self.toolwidgetmain.comboBox_typeReseau,
                    "flowconditionupstream": self.toolwidgetmain.comboBox_inletflowcondition,
                    "flowconditiondownstream": self.toolwidgetmain.comboBox_outletflowcondition,
                    "systemfunction": self.toolwidgetmain.comboBox_systemfunction,
                    "dateoperationalcreation": self.toolwidgetmain.dateEdit_anneepose,
                },
            },
        }

        self.toolwidgetmain.toolButton_calc_diam.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_diametreNominal)
        )

        self.toolwidgetmain.toolButton_calc_haut.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_haut)
        )

        self.toolwidgetmain.toolButton_prof_amont.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_profamont)
        )

        self.toolwidgetmain.toolButton_prof_aval.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_profaval)
        )

        self.ownerwdg = LidChooserWidget(
            parentwdg=self,
            parentlidfield="lid_actor_1",
            parentframe=self.toolwidgetmain.frame_owner,
            searchdbase="actor",
            searchfieldtoshow=["actorname"],
        )
        self.lamiawidgets.append(self.ownerwdg)
        self.operatorwdg = LidChooserWidget(
            parentwdg=self,
            parentlidfield="lid_actor_2",
            parentframe=self.toolwidgetmain.frame_operator,
            searchdbase="actor",
            searchfieldtoshow=["actorname"],
        )
        self.lamiawidgets.append(self.operatorwdg)

    def _initMainToolWidgetCD41(self):
        self.toolwidgetmain = UserUIField_2()

        self.formtoolwidgetconfdictmain = {
            "edge": {
                "linkfield": "id_edge",
                "widgets": {
                    # "sewertype": self.toolwidgetmain.comboBox_typeReseau,
                    "laterals": self.toolwidgetmain.comboBox_branch,
                    "domain": self.toolwidgetmain.comboBox_domaine,
                    "location": self.toolwidgetmain.comboBox_implant,
                    "flowtype": self.toolwidgetmain.comboBox_typeecoul,
                    "material": self.toolwidgetmain.comboBox_materiau,
                    # 'anPoseInf': self.toolwidgetmain.dateEdit_anneepose,
                    "nominaldiameter": self.toolwidgetmain.doubleSpinBox_diametreNominal,
                    "height": self.toolwidgetmain.doubleSpinBox_haut,
                    # 'largeur': self.toolwidgetmain.doubleSpinBox_larg,
                    # 'altAmont': self.toolwidgetmain.doubleSpinBox_altAmont,
                    # 'altAmont': self.toolwidgetmain.doubleSpinBox_altAval,
                    "depthup": self.toolwidgetmain.doubleSpinBox_profamont,
                    "depthdown": self.toolwidgetmain.doubleSpinBox_profaval,
                    # 'lid_descriptionsystem_1': self.toolwidgetmain.spinBox_lk_noeud1,
                    # 'lid_descriptionsystem_2': self.toolwidgetmain.spinBox_lk_noeud2
                },
            },
            "object": {
                "linkfield": "id_object",
                "widgets": {"comment": self.toolwidgetmain.textBrowser_commentaire},
            },
            "descriptionsystem": {
                "linkfield": "id_descriptionsystem",
                "widgets": {
                    "networktype": self.toolwidgetmain.comboBox_typeReseau,
                    "dateoperationalcreation": self.toolwidgetmain.dateEdit_anneepose,
                    "systemfunction": self.toolwidgetmain.comboBox_fonction,
                },
            },
        }

        self.toolwidgetmain.toolButton_calc_diam.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_diametreNominal)
        )

        self.toolwidgetmain.toolButton_calc_haut.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_haut)
        )

        self.toolwidgetmain.toolButton_prof_amont.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_profamont)
        )

        self.toolwidgetmain.toolButton_prof_aval.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_profaval)
        )

    def initAdvancedToolWidget(self):
        pass

    def _____________________widgetspecificfunctions(self):
        pass

    def postSaveFeature(self, savedfeaturepk=None):
        pass


class UserUIField(QWidget):
    def __init__(self, parent=None):
        super(UserUIField, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), "lamia_form_edge_ui.ui")
        uic.loadUi(uipath, self)


class UserUIField_2(QWidget):
    def __init__(self, parent=None):
        super(UserUIField_2, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), "lamia_form_edge_ui_CD41.ui")
        uic.loadUi(uipath, self)
