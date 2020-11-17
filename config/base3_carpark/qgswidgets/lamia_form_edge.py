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


"""


import datetime
import logging
import time
debugtime = False
"""

from qgis.PyQt import uic, QtCore, QtGui

from qgis.PyQt.QtWidgets import QWidget, QLabel, QFrame
import os
import logging

from ...base3.qgswidgets.lamia_form_edge import BaseEdgeTool
from .lamia_form_sketch import BaseCarparkSketchTool
from .lamia_form_camera import BaseCarparkCameraTool
from .lamia_form_deficiency import BaseCarparkDeficiencyTool


class BaseCarparkEdgeTool(BaseEdgeTool):

    tooltreewidgetSUBCAT = QtCore.QCoreApplication.translate("base3_cp", "Parking site")
    CHOOSERTREEWDGSPEC = {"colshow": ["edge_now.name"]}

    def __init__(self, **kwargs):
        super(BaseCarparkEdgeTool, self).__init__(**kwargs)

    def initMainToolWidget(self):

        self.toolwidgetmain = UserUI()
        self.formtoolwidgetconfdictmain = {
            "edge": {
                "linkfield": "id_edge",
                "widgets": {
                    "location": self.toolwidgetmain.location,
                    "parkingtype": self.toolwidgetmain.parkingtype,
                    "zoning": self.toolwidgetmain.zoning,
                    "zoningother": self.toolwidgetmain.zoningother,
                    "parkingplacenumber": self.toolwidgetmain.parkingplacenumber,
                    "parity": self.toolwidgetmain.parity,
                    "idseg": self.toolwidgetmain.idseg,
                },
            },
            "object": {
                "linkfield": "id_object",
                "widgets": {
                    "name": self.toolwidgetmain.name,
                    #'commentaire':self.toolwidgetmain.textBrowser_commentaire
                    "importid": self.toolwidgetmain.importid,
                },
            },
            "descriptionsystem": {
                "linkfield": "id_descriptionsystem",
                "widgets": {
                    "streetname": self.toolwidgetmain.streetname,
                    "streetupname": self.toolwidgetmain.streetupname,
                    "streetdownname": self.toolwidgetmain.streetdownname,
                    "streetcomment": self.toolwidgetmain.streetcomment,
                },
            },
        }

        self.dbasechildwdgfield = []

        self.toolwidgetmain.toolButton_nbreplace.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.parkingplacenumber)
        )

        self.dbasechildwdgfield = []
        self.instancekwargs["parentwidget"] = self

        self.propertieswdgDesordre = BaseCarparkDeficiencyTool(**self.instancekwargs)
        self.propertieswdgDesordre.GEOMETRYSKIP = True
        self.dbasechildwdgfield.append(self.propertieswdgDesordre)

        self.propertieswdgPHOTOGRAPHIE = BaseCarparkCameraTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)
        self.propertieswdgCROQUIS = BaseCarparkSketchTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

    def postSaveFeature(self, featurepk=None):
        pass


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), "lamia_form_edge_ui.ui")
        uic.loadUi(uipath, self)

