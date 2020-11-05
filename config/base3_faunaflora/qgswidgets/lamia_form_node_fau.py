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
from ...base3.qgswidgets.lamia_form_node import BaseNodeTool

from .lamia_form_camera import BaseFaunafloraCameraTool
from .lamia_form_sketch import BaseFaunafloraSketchTool

from Lamia.qgisiface.iface.qgiswidget.tools.form_subwidgets.subwidget_getfromcatalog import (
    CatalogWidget,
)


class BaseFaunafloraFaunaNodeTool(BaseNodeTool):

    PREPROTOOLNAME = "node_fauna"
    tooltreewidgetCAT = QtCore.QCoreApplication.translate("base3", "Inventory")
    tooltreewidgetSUBCAT = QtCore.QCoreApplication.translate("base3", "Fauna")
    TABLEFILTERFIELD = {"nodecategory": "FAU"}

    tooltreewidgetICONPATH = os.path.join(os.path.dirname(__file__), "fauna.png")

    linkdict = {
        "colparent": "id_descriptionsystem",
        "colthistable": "lid_descriptionsystem_1",
        "tctable": None,
        "tctablecolparent": None,
        "tctablecolthistable": None,
    }
    for tablename in ["node", "edge", "equipment"]:
        BaseNodeTool.PARENTJOIN[tablename] = linkdict

    CHOOSERTREEWDGSPEC = {"colshow": ["node_now.scientificname"]}

    def __init__(self, **kwargs):
        super(BaseFaunafloraFaunaNodeTool, self).__init__(**kwargs)

    def initMainToolWidget(self):
        self.toolwidgetmain = UserUI()
        self.formtoolwidgetconfdictmain = {
            "node": {
                "linkfield": "id_node",
                "widgets": {
                    "nodecategory": self.toolwidgetmain.comboBox_nodecategory,
                    "faunadevstage": self.toolwidgetmain.comboBox_faunadevstage,
                    "number": self.toolwidgetmain.spinBox_number,
                    "faunachar1": self.toolwidgetmain.comboBox_faunachar1,
                    "faunainvasive": self.toolwidgetmain.checkBox_invasive,
                },
            },
            "object": {
                "linkfield": "id_object",
                "widgets": {"comment": self.toolwidgetmain.textBrowser_comment,},
            },
            "descriptionsystem": {
                "linkfield": "id_descriptionsystem",
                "widgets": {
                    "orderclass": self.toolwidgetmain.lineEdit_orderclass,
                    "commonname": self.toolwidgetmain.lineEdit_commonname,
                    "scientificname": self.toolwidgetmain.lineEdit_scientificcname,
                },
            },
        }
        self.toolwidgetmain.comboBox_nodecategory.currentIndexChanged.connect(
            self.changeCategory
        )
        self.toolwidgetmain.toolButton_number.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.spinBox_number)
        )

        self.dbasechildwdgfield = []
        self.instancekwargs["parentwidget"] = self
        self.propertieswdgPHOTOGRAPHIE = BaseFaunafloraCameraTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)
        self.propertieswdgCROQUIS = BaseFaunafloraSketchTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)
        self.catalogfinder = CatalogWidget(
            parentwdg=self,
            parentframe=self.toolwidgetmain.frame_catalog,
            catalogtype="base3_faunaflora",
            catalogname="LISTE_faune_2019",
            catalogsheet=None,
            coltoshow=["Nom français", "Nom latin"],
            sheetfield="orderclass",
            valuefield=["commonname", "scientificname"],
        )
        self.lamiawidgets.append(self.catalogfinder)

    def postSaveFeature(self, savedfeaturepk=None):
        super().postSaveFeature(savedfeaturepk)


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), "lamia_form_node_ui.ui")
        uic.loadUi(uipath, self)
