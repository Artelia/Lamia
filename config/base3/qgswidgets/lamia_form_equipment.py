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

from Lamia.qgisiface.iface.qgiswidget.tools.lamia_abstractformtool import (
    AbstractLamiaFormTool,
)
from .lamia_form_camera import BaseCameraTool
from .lamia_form_sketch import BaseSketchTool

base3 = QtCore.QObject()


class BaseEquipmentTool(AbstractLamiaFormTool):

    PREPROTOOLNAME = "equipment"
    DBASETABLENAME = "equipment"
    LOADFIRST = True

    tooltreewidgetCAT = QtCore.QCoreApplication.translate("base3", "Facilities")
    tooltreewidgetSUBCAT = QtCore.QCoreApplication.translate("base3", "Equipment")
    tooltreewidgetICONPATH = os.path.join(
        os.path.dirname(__file__), "lamia_form_equipment_icon.svg"
    )

    tempparentjoin = {}
    linkdict = {
        "colparent": "id_descriptionsystem",
        "colthistable": "lid_descriptionsystem_1",
        "tctable": None,
        "tctablecolparent": None,
        "tctablecolthistable": None,
    }
    for tablename in ["node", "edge", "equipment"]:
        tempparentjoin[tablename] = linkdict
    PARENTJOIN = tempparentjoin

    def __init__(self, **kwargs):
        super(BaseEquipmentTool, self).__init__(**kwargs)
        self.instancekwargs = kwargs

    def initMainToolWidget(self):

        self.toolwidgetmain = UserUI()
        self.formtoolwidgetconfdictmain = {
            "equipment": {
                "linkfield": "id_equipment",
                "widgets": {"equipmenttype": self.toolwidgetmain.comboBox_cat},
            },
            "object": {
                "linkfield": "id_object",
                "widgets": {"comment": self.toolwidgetmain.textBrowser_comm},
            },
            "descriptionsystem": {"linkfield": "id_descriptionsystem", "widgets": {}},
        }
        self.toolwidgetmain.comboBox_cat.currentIndexChanged.connect(
            self.changeCategorie
        )

        # ****************************************************************************************
        # child widgets
        self.dbasechildwdgfield = []

        if self.parentWidget is None:
            self.instancekwargs["parentwidget"] = self

            self.propertieswdgPHOTOGRAPHIE = BaseCameraTool(**self.instancekwargs)
            self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)

            self.propertieswdgCROQUIS = BaseSketchTool(**self.instancekwargs)
            self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

    def changeCategorie(self, intcat):

        pagecount = self.toolwidget.stackedWidget.count()
        if intcat >= pagecount - 1:
            self.toolwidget.stackedWidget.setCurrentIndex(pagecount - 1)
        else:
            self.toolwidget.stackedWidget.setCurrentIndex(intcat)

    def postSelectFeature(self):
        pass

    def postSaveFeature(self, savedfeaturepk=None):
        pass


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), "lamia_form_equipment_ui.ui")
        uic.loadUi(uipath, self)
