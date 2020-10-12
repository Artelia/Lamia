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
import logging

from qgis.PyQt import uic, QtCore, QtGui
from qgis.PyQt.QtWidgets import QWidget, QLabel, QFrame


from ...base3.qgswidgets.lamia_form_edge import BaseEdgeTool
from .lamia_form_camera import BaseWaterdistributionCameraTool
from .lamia_form_sketch import BaseWaterdistributionSketchTool
from lamiaqgisiface.iface.qgiswidget.tools.form_subwidgets.subwidget_edgetonode import (
    EdgeToNodeWidget,
)


class BaseWaterdistributionEdgeTool(BaseEdgeTool):
    def __init__(self, **kwargs):
        super(BaseWaterdistributionEdgeTool, self).__init__(**kwargs)

    def initMainToolWidget(self):
        # ****************************************************************************************
        #   userui Field
        if self.dbase.variante in [None, "Lamia"]:
            self.toolwidgetmain = UserUIField()

            self.formtoolwidgetconfdictmain = {
                "edge": {
                    "linkfield": "id_edge",
                    "widgets": {
                        "laterals": self.toolwidgetmain.comboBox_branchement,
                        "domain": self.toolwidgetmain.comboBox_domaine,
                        "diameterext": self.toolwidgetmain.doubleSpinBox_diametre,
                        "depthtoppipe": self.toolwidgetmain.doubleSpinBox_gene,
                        "material": self.toolwidgetmain.comboBox_materiau,
                        "joint": self.toolwidgetmain.comboBox_joint,
                        "cathodicprotection": self.toolwidgetmain.comboBox_protectioncatho,
                        "flowtype": self.toolwidgetmain.comboBox_modecircu,
                        "pipefunction": self.toolwidgetmain.comboBox_fonctioncan,
                    },
                },
                "object": {
                    "linkfield": "id_object",
                    "widgets": {"comment": self.toolwidgetmain.textBrowser_commentaire},
                },
                "descriptionsystem": {
                    "linkfield": "id_descriptionsystem",
                    "widgets": {"networktype": self.toolwidgetmain.comboBox_typeeau},
                },
            }

            self.toolwidgetmain.toolButton_diametre.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_diametre)
            )
            self.toolwidgetmain.toolButton_gene.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_gene)
            )

            self.dbasechildwdgfield = []
            self.instancekwargs["parentwidget"] = self
            self.propertieswdgPHOTOGRAPHIE = BaseWaterdistributionCameraTool(
                **self.instancekwargs
            )
            self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)
            self.propertieswdgCROQUIS = BaseWaterdistributionSketchTool(
                **self.instancekwargs
            )
            self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

            self.edgetonode = EdgeToNodeWidget(
                self,
                lateralfield="laterals",
                upstreamnodeidfield="lid_descriptionsystem_1",
                downstreamnodeidfield="lid_descriptionsystem_2",
                parentframe=self.toolwidgetmain.frame_edgetonode,
            )
            self.lamiawidgets.append(self.edgetonode)

        elif self.dbase.variante in ["urban_heating"]:
            self.toolwidgetmain = UserUIField2()

            self.formtoolwidgetconfdictmain = {
                "edge": {
                    "linkfield": "id_edge",
                    "widgets": {
                        "laterals": self.toolwidgetmain.comboBox_branchement,
                        "domain": self.toolwidgetmain.comboBox_domaine,
                        "diameterext": self.toolwidgetmain.doubleSpinBox_diametre,
                        "diameterint": self.toolwidgetmain.doubleSpinBox_diamint,
                        "depthtoppipe": self.toolwidgetmain.doubleSpinBox_gene,
                        "material": self.toolwidgetmain.comboBox_materiau,
                        "joint": self.toolwidgetmain.comboBox_joint,
                        "insulation": self.toolwidgetmain.comboBox_calor,
                        "insulationtype": self.toolwidgetmain.comboBox_calortype,
                        "insulationthickness": self.toolwidgetmain.spinBox_calorep,
                        "cathodicprotection": self.toolwidgetmain.comboBox_protectioncatho,
                        "flowtype": self.toolwidgetmain.comboBox_modecircu,
                        "pipefunction": self.toolwidgetmain.comboBox_fonctioncan,
                    },
                },
                "object": {
                    "linkfield": "id_object",
                    "widgets": {"comment": self.toolwidgetmain.textBrowser_commentaire},
                },
                "descriptionsystem": {
                    "linkfield": "id_descriptionsystem",
                    "widgets": {"networktype": self.toolwidgetmain.comboBox_typeeau},
                },
            }

            self.toolwidgetmain.toolButton_diametre.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_diametre)
            )
            self.toolwidgetmain.toolButton_diamint.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_diamint)
            )
            self.toolwidgetmain.toolButton_gene.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_gene)
            )
            self.toolwidgetmain.toolButton_calorep.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.spinBox_calorep)
            )

            self.dbasechildwdgfield = []
            self.instancekwargs["parentwidget"] = self
            self.propertieswdgPHOTOGRAPHIE = BaseWaterdistributionCameraTool(
                **self.instancekwargs
            )
            self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)
            self.propertieswdgCROQUIS = BaseWaterdistributionSketchTool(
                **self.instancekwargs
            )
            self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

            self.edgetonode = EdgeToNodeWidget(
                self,
                lateralfield="laterals",
                upstreamnodeidfield="lid_descriptionsystem_1",
                downstreamnodeidfield="lid_descriptionsystem_2",
                parentframe=self.toolwidgetmain.frame_edgetonode,
            )
            self.lamiawidgets.append(self.edgetonode)


class UserUIField(QWidget):
    def __init__(self, parent=None):
        super(UserUIField, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), "lamia_form_edge_ui.ui")
        uic.loadUi(uipath, self)


class UserUIField2(QWidget):
    def __init__(self, parent=None):
        super(UserUIField2, self).__init__(parent=parent)
        uipath = os.path.join(
            os.path.dirname(__file__), "lamia_form_edge_ui_heatingnetwork.ui"
        )
        uic.loadUi(uipath, self)
