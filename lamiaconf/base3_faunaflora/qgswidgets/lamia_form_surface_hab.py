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
from qgis.PyQt.QtWidgets import QWidget, QPushButton
from ...base3.qgswidgets.lamia_form_surface import BaseSurfaceTool

from .lamia_form_camera import BaseFaunafloraCameraTool
from .lamia_form_sketch import BaseFaunafloraSketchTool

from Lamia.iface.qgiswidget.tools.form_subwidgets.subwidget_getfromcatalog import (
    CatalogWidget,
)


class BaseFaunafloraHABSurfaceTool(BaseSurfaceTool):

    PREPROTOOLNAME = "surface_habitat"
    tooltreewidgetCAT = QtCore.QCoreApplication.translate("base3", "Inventory")
    tooltreewidgetSUBCAT = QtCore.QCoreApplication.translate("base3", "Habitat")
    TABLEFILTERFIELD = {"surfacecategory": "HAB"}
    tooltreewidgetICONPATH = os.path.join(os.path.dirname(__file__), "habitat.png")

    def __init__(self, **kwargs):
        super(BaseFaunafloraHABSurfaceTool, self).__init__(**kwargs)

    def initMainToolWidget(self):
        self.toolwidgetmain = UserUI()
        self.formtoolwidgetconfdictmain = {
            "surface": {
                "linkfield": "id_surface",
                "widgets": {
                    "surfacecategory": self.toolwidgetmain.comboBox_category,
                    "habitatrepository": self.toolwidgetmain.lineEdit_habrepository,
                    "habitatname": self.toolwidgetmain.lineEdit_habname,
                    "habitatcode": self.toolwidgetmain.lineEdit_habcode,
                    "habitatwetland": self.toolwidgetmain.checkBox_wetland,
                },
            },
            "object": {
                "linkfield": "id_object",
                "widgets": {"comment": self.toolwidgetmain.textBrowser_comment,},
            },
            "descriptionsystem": {
                "linkfield": "id_descriptionsystem",
                "widgets": {
                    # 'orderclass': self.toolwidgetmain.lineEdit_orderclass,
                    # 'commonname':self.toolwidgetmain.lineEdit_commonname,
                    # 'scientificname':self.toolwidgetmain.lineEdit_scientificcname,
                },
            },
        }
        self.toolwidgetmain.comboBox_category.currentIndexChanged.connect(
            self.changeCategory
        )
        # self.toolwidgetmain.toolButton_number.clicked.connect(
        #     lambda: self.showNumPad(self.toolwidgetmain.spinBox_number))

        self.dbasechildwdgfield = []
        self.instancekwargs["parentwidget"] = self
        self.propertieswdgPHOTOGRAPHIE = BaseFaunafloraCameraTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)
        self.propertieswdgCROQUIS = BaseFaunafloraSketchTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

        self.catalogfinder = CatalogWidget(
            parentwdg=self,
            parentframe=self.toolwidgetmain.frame_catalog_hab,
            catalogtype="base3_faunaflora",
            catalogname="habitats_EUNIS_et_CORINE",
            catalogsheet=None,
            coltoshow=["LB_CODE", "LB_HAB_FR"],
            sheetfield="habitatrepository",
            valuefield=["habitatcode", "habitatname"],
        )
        self.lamiawidgets.append(self.catalogfinder)

    def _widgetClicked_manageToolBar(self):
        super()._widgetClicked_manageToolBar()

    def postSaveFeature(self, savedfeaturepk=None):
        super().postSaveFeature(savedfeaturepk)


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), "lamia_form_surface_ui.ui")
        uic.loadUi(uipath, self)
