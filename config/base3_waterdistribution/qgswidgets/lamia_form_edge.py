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
from Lamia.qgisiface.iface.qgiswidget.tools.form_subwidgets.subwidget_edgetonode import (
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
                        "laterals": self.toolwidgetmain.laterals,
                        "domain": self.toolwidgetmain.domain,
                        "diameterext": self.toolwidgetmain.diameterext,
                        "depthtoppipe": self.toolwidgetmain.depthtoppipe,
                        "material": self.toolwidgetmain.material,
                        "joint": self.toolwidgetmain.joint,
                        "cathodicprotection": self.toolwidgetmain.cathodicprotection,
                        "flowtype": self.toolwidgetmain.flowtype,
                        "pipefunction": self.toolwidgetmain.pipefunction,
                    },
                },
                "object": {
                    "linkfield": "id_object",
                    "widgets": {"comment": self.toolwidgetmain.comment},
                },
                "descriptionsystem": {
                    "linkfield": "id_descriptionsystem",
                    "widgets": {"networktype": self.toolwidgetmain.networktype},
                },
            }

            self.toolwidgetmain.toolButton_diametre.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.diameterext)
            )
            self.toolwidgetmain.toolButton_gene.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.depthtoppipe)
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
                        "laterals": self.toolwidgetmain.laterals,
                        "domain": self.toolwidgetmain.domain,
                        "diameterext": self.toolwidgetmain.diameterext,
                        "diameterint": self.toolwidgetmain.diameterint,
                        "depthtoppipe": self.toolwidgetmain.depthtoppipe,
                        "material": self.toolwidgetmain.material,
                        "joint": self.toolwidgetmain.joint,
                        "insulation": self.toolwidgetmain.insulation,
                        "insulationtype": self.toolwidgetmain.insulationtype,
                        "insulationthickness": self.toolwidgetmain.insulationthickness,
                        "cathodicprotection": self.toolwidgetmain.cathodicprotection,
                        "flowtype": self.toolwidgetmain.flowtype,
                        "pipefunction": self.toolwidgetmain.pipefunction,
                    },
                },
                "object": {
                    "linkfield": "id_object",
                    "widgets": {"comment": self.toolwidgetmain.comment},
                },
                "descriptionsystem": {
                    "linkfield": "id_descriptionsystem",
                    "widgets": {"networktype": self.toolwidgetmain.networktype},
                },
            }

            self.toolwidgetmain.toolButton_diametre.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_diametre)
            )
            self.toolwidgetmain.toolButton_diamint.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.diameterint)
            )
            self.toolwidgetmain.toolButton_gene.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.depthtoppipe)
            )
            self.toolwidgetmain.toolButton_calorep.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.insulationthickness)
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
