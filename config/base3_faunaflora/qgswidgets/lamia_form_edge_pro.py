# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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
import os, csv
import qgis
import sys, datetime
from collections import OrderedDict

from qgis.PyQt import uic, QtCore, QtGui
from qgis.PyQt.QtWidgets import QWidget, QPushButton
from ...base3.qgswidgets.lamia_form_edge import BaseEdgeTool

from .lamia_form_camera import BaseFaunafloraCameraTool
from .lamia_form_sketch import BaseFaunafloraSketchTool
from .lamia_form_surface_flo import BaseFaunafloraFLOSurfaceTool
from .lamia_form_node_fau import BaseFaunafloraFaunaNodeTool


class BaseFaunafloraEdgePROTool(BaseEdgeTool):

    PREPROTOOLNAME = "edge_protocol"
    tooltreewidgetCAT = QtCore.QCoreApplication.translate("base3", "Inventory")
    tooltreewidgetSUBCAT = QtCore.QCoreApplication.translate("base3", "Protocol")
    TABLEFILTERFIELD = {"edgecategory": "PRO"}
    tooltreewidgetICONPATH = os.path.join(os.path.dirname(__file__), "protocol.png")

    def __init__(self, **kwargs):
        super(BaseFaunafloraEdgePROTool, self).__init__(**kwargs)

    def initMainToolWidget(self):
        self.toolwidgetmain = UserUI()
        self.formtoolwidgetconfdictmain = {
            "edge": {
                "linkfield": "id_surface",
                "widgets": {
                    "edgecategory": self.toolwidgetmain.edgecategory,
                    "edgetype": self.toolwidgetmain.edgetype,
                    "edgesubtype": self.toolwidgetmain.edgesubtype,
                    "edgenumber": self.toolwidgetmain.edgenumber,
                },
            },
            "object": {
                "linkfield": "id_object",
                "widgets": {"comment": self.toolwidgetmain.comment,},
            },
            "descriptionsystem": {"linkfield": "id_descriptionsystem", "widgets": {}},
        }
        self.toolwidgetmain.edgecategory.currentIndexChanged.connect(
            self.changeCategory
        )
        self.toolwidgetmain.edgetype.currentIndexChanged.connect(
            self.changeSubType
        )
        self.toolwidgetmain.toolButton_edgenumber.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.edgenumber)
        )

        self.dbasechildwdgfield = []
        self.instancekwargs["parentwidget"] = self

        self.propertieswdgFlora = BaseFaunafloraFLOSurfaceTool(**self.instancekwargs)
        self.propertieswdgFlora.GEOMETRYSKIP = True
        self.dbasechildwdgfield.append(self.propertieswdgFlora)

        self.propertieswdgFauna = BaseFaunafloraFaunaNodeTool(**self.instancekwargs)
        self.propertieswdgFauna.GEOMETRYSKIP = True
        self.dbasechildwdgfield.append(self.propertieswdgFauna)

        self.propertieswdgPHOTOGRAPHIE = BaseFaunafloraCameraTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)
        self.propertieswdgCROQUIS = BaseFaunafloraSketchTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

    def _widgetClicked_manageToolBar(self):
        super()._widgetClicked_manageToolBar()
        self.mainifacewidget.actiontoobargeomnewpoint.setEnabled(True)

    def changeSubType(self):
        currenttxt = self.toolwidgetmain.edgetype.currentText()
        curvalue = self.dbase.getConstraintRawValueFromText('edge', 'edgetype', currenttxt)
        if curvalue in ['PED']:
            self.toolwidgetmain.stackedWidget_edgetype.setCurrentIndex(0)
        else:
            self.toolwidgetmain.stackedWidget_edgetype.setCurrentIndex(1)       




class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), "lamia_form_edge_ui.ui")
        uic.loadUi(uipath, self)
