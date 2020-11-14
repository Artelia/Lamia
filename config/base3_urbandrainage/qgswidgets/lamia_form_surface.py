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

from qgis.PyQt import uic, QtCore
from qgis.PyQt.QtWidgets import QWidget

from ...base3.qgswidgets.lamia_form_surface import BaseSurfaceTool

from .lamia_form_camera import BaseUrbandrainageCameraTool
from .lamia_form_sketch import BaseUrbandrainageSketchTool
from .lamia_form_graph import BaseUrbandrainageGraphTool
from .lamia_form_deficiency import BaseUrbandrainageDeficiencyTool

from Lamia.qgisiface.iface.qgiswidget.tools.form_subwidgets.subwidget_tcmanytomany import (
    TcmanytomanyChooserWidget,
)
from Lamia.qgisiface.iface.qgiswidget.tools.form_subwidgets.subwidget_lidchooser import (
    LidChooserWidget,
)


class BaseUrbandrainageSurfaceTool(BaseSurfaceTool):
    def __init__(self, **kwargs):
        super(BaseUrbandrainageSurfaceTool, self).__init__(**kwargs)

    def initMainToolWidget(self):
        self.toolwidgetmain = UserUI()
        self.formtoolwidgetconfdictmain = {
            "surface": {
                "linkfield": "id_surface",
                "widgets": {
                    "surfacetype": self.toolwidgetmain.surfacetype,
                    "surfacesubtype": self.toolwidgetmain.surfacesubtype,
                    "width": self.toolwidgetmain.width,
                    "lenght": self.toolwidgetmain.lenght,
                    "depth": self.toolwidgetmain.depth,
                    "volume": self.toolwidgetmain.volume,
                    "receivingenvironment": self.toolwidgetmain.receivingenvironment,
                    "flowcontrol": self.toolwidgetmain.flowcontrol,
                },
            },
            "descriptionsystem": {
                "linkfield": "id_descriptionsystem",
                "widgets": {
                    "networktype": self.toolwidgetmain.networktype,
                    "flowconditionupstream": self.toolwidgetmain.flowconditionupstream,
                    "flowconditiondownstream": self.toolwidgetmain.flowconditiondownstream,
                    "systemfunction": self.toolwidgetmain.systemfunction,
                    "city": self.toolwidgetmain.city,
                    "streetname": self.toolwidgetmain.streetname,
                    "structuralstate": self.toolwidgetmain.structuralstate,
                },
            },
            "object": {
                "linkfield": "id_object",
                "widgets": {"name": self.toolwidgetmain.name,},
            },
        }
        # self.toolwidgetmain.pushButton_currentPrestation.clicked.connect(self.defineCurrentPrestation)
        # self.toolwidgetmain.pushButton_defineinter.clicked.connect(self.manageLinkage)

        self.toolwidgetmain.toolButton_width.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.width)
        )
        self.toolwidgetmain.toolButton_lenght.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.lenght)
        )
        self.toolwidgetmain.toolButton_depth.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.depth)
        )
        self.toolwidgetmain.toolButton_volume.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.volume)
        )

        # ****************************************************************************************
        # child widgets
        self.dbasechildwdgfield = []
        self.instancekwargs["parentwidget"] = self

        self.propertieswdgPHOTO = BaseUrbandrainageCameraTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgPHOTO)

        self.propertieswdgDesordre = BaseUrbandrainageDeficiencyTool(
            **self.instancekwargsforchildwdg
        )
        self.propertieswdgDesordre.SKIP_LOADING_UI = True
        self.propertieswdgDesordre.initMainToolWidget()
        # self.propertieswdgDesordre.formtoolwidgetconfdictmain["deficiency"]["widgets"][
        #     "deficiencycategory"
        # ] = "NOD"
        self.propertieswdgDesordre.TABLEFILTERFIELD = {"deficiencycategory": "SUR"}
        self.dbasechildwdgfield.append(self.propertieswdgDesordre)

        if self.dbase.variante in [None, "Lamia"]:
            self.propertieswdgGRAPH = BaseUrbandrainageGraphTool(
                **self.instancekwargsforchildwdg
            )
            self.dbasechildwdgfield.append(self.propertieswdgGRAPH)
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

        self.tcsubwidget = TcmanytomanyChooserWidget(
            parentwdg=self,
            tcmanytomanyname="tcsurfacedescriptionsystem",
            childtablename="node",
            parentmanytomanyfield="id_surface",
            childmanytomanyfield="id_descriptionsystem",
            childdisplayfields=["id_node", "name", "nodetype"],
            tcmanytomanydisplayfields=[],
            parentframe=self.toolwidgetmain.frame_node,
        )

        self.lamiawidgets.append(self.tcsubwidget)


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), "lamia_form_surface_ui.ui")
        uic.loadUi(uipath, self)
