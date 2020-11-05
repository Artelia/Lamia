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
import logging
import time

from qgis.PyQt import uic, QtCore, QtGui
from qgis.PyQt.QtWidgets import QWidget, QLabel, QFrame

from Lamia.qgisiface.iface.qgiswidget.tools.lamia_abstractformtool import (
    AbstractLamiaFormTool,
)

from .lamia_form_camera import BaseCameraTool
from .lamia_form_sketch import BaseSketchTool


base3 = QtCore.QObject()


class BaseEdgeTool(AbstractLamiaFormTool):

    PREPROTOOLNAME = "edge"
    DBASETABLENAME = "edge"
    LOADFIRST = True

    tooltreewidgetCAT = QtCore.QCoreApplication.translate("base3", "Facilities")
    tooltreewidgetSUBCAT = QtCore.QCoreApplication.translate("base3", "Pipes")
    tooltreewidgetICONPATH = os.path.join(
        os.path.dirname(__file__), "lamia_form_edge_icon.svg"
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
        super(BaseEdgeTool, self).__init__(**kwargs)
        self.instancekwargs = kwargs  # depreciated
        self.instancekwargsforchildwdg = kwargs
        self.instancekwargsforchildwdg["parentwidget"] = self

    def initMainToolWidget(self):
        # ****************************************************************************************
        #   userui Field

        self.toolwidgetmain = UserUIField()

        self.formtoolwidgetconfdictmain = {
            "edge": {"linkfield": "id_edge", "widgets": {}},
            "object": {
                "linkfield": "id_object",
                "widgets": {
                    "name": self.toolwidgetmain.lineEdit_nom,
                    "comment": self.toolwidgetmain.textBrowser_commentaire,
                },
            },
            "descriptionsystem": {"linkfield": "id_descriptionsystem", "widgets": {}},
        }

        self.dbasechildwdgfield = []
        self.instancekwargs["parentwidget"] = self
        self.propertieswdgPHOTOGRAPHIE = BaseCameraTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)
        self.propertieswdgCROQUIS = BaseSketchTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

    def postSelectFeature(self):
        pass

    def changeCategory(self, intcat):

        pagecount = self.toolwidget.stackedWidget_category.count()
        if intcat >= pagecount - 1:
            self.toolwidget.stackedWidget_category.setCurrentIndex(pagecount - 1)
        else:
            self.toolwidget.stackedWidget_category.setCurrentIndex(intcat)


class UserUIField(QWidget):
    def __init__(self, parent=None):
        super(UserUIField, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), "lamia_form_edge_ui.ui")
        uic.loadUi(uipath, self)
