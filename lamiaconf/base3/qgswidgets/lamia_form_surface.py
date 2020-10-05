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


import datetime, os

from qgis.PyQt import uic, QtCore
from qgis.PyQt.QtWidgets import QWidget

from Lamia.iface.qgiswidget.tools.lamia_abstractformtool import AbstractLamiaFormTool
from .lamia_form_camera import BaseCameraTool
from .lamia_form_sketch import BaseSketchTool
from Lamia.iface.qgiswidget.tools.form_subwidgets.subwidget_tcmanytomany import (
    TcmanytomanyChooserWidget,
)
from Lamia.iface.qgiswidget.tools.form_subwidgets.subwidget_lidchooser import (
    LidChooserWidget,
)
from .lamia_form_graphcsv import BaseGraphcsvTool


class BaseSurfaceTool(AbstractLamiaFormTool):

    PREPROTOOLNAME = "surface"
    DBASETABLENAME = "surface"
    LOADFIRST = True

    tooltreewidgetCAT = QtCore.QCoreApplication.translate("base3", "Facilities")
    tooltreewidgetSUBCAT = QtCore.QCoreApplication.translate("base3", "Surface")
    tooltreewidgetICONPATH = os.path.join(
        os.path.dirname(__file__), "lamia_form_surface_icon.svg"
    )

    PARENTJOIN = {
        "facility": {
            "colparent": "id_facility",
            "colthistable": "lid_facility",
            "tctable": None,
            "tctablecolparent": None,
            "tctablecolthistable": None,
        }
    }

    def __init__(self, **kwargs):
        super(BaseSurfaceTool, self).__init__(**kwargs)
        self.instancekwargs = kwargs  # depreciated
        self.instancekwargsforchildwdg = kwargs
        self.instancekwargsforchildwdg["parentwidget"] = self

    def initMainToolWidget(self):

        self.toolwidgetmain = UserUI()
        self.formtoolwidgetconfdictmain = {
            "surface": {
                "linkfield": "id_delivery",
                "widgets": {
                    "surfacetype": self.toolwidgetmain.comboBox_type,
                    "surfacesubtype": self.toolwidgetmain.comboBox_subtype,
                },
            },
            "object": {"linkfield": "id_object", "widgets": {}},
        }
        # self.toolwidgetmain.pushButton_currentPrestation.clicked.connect(self.defineCurrentPrestation)
        # self.toolwidgetmain.pushButton_defineinter.clicked.connect(self.manageLinkage)

        self.toolwidgetmain.comboBox_category.currentIndexChanged.connect(
            self.changeCategory
        )

        # ****************************************************************************************
        # child widgets
        self.dbasechildwdgfield = []
        self.instancekwargs["parentwidget"] = self

        self.propertieswdgPHOTO = BaseCameraTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgPHOTO)

        self.propertieswdgGRAPHcsv = BaseGraphcsvTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgGRAPHcsv)

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

    def postSelectFeature(self):
        pass

    def postSaveFeature(self, boolnewfeature):
        pass

    def changeCategory(self, intcat):

        pagecount = self.toolwidget.stackedWidget_category.count()
        if intcat >= pagecount - 1:
            self.toolwidget.stackedWidget_category.setCurrentIndex(pagecount - 1)
        else:
            self.toolwidget.stackedWidget_category.setCurrentIndex(intcat)


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), "lamia_form_surface_ui.ui")
        uic.loadUi(uipath, self)
