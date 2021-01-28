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


class BaseCommentTool(AbstractLamiaFormTool):

    PREPROTOOLNAME = "comment"
    DBASETABLENAME = "comment"
    LOADFIRST = True

    tooltreewidgetCAT = QtCore.QCoreApplication.translate("base3", "Resources")
    tooltreewidgetSUBCAT = QtCore.QCoreApplication.translate("base3", "Comments")
    tooltreewidgetICONPATH = os.path.join(
        os.path.dirname(__file__), "lamia_form_edge_icon.svg"
    )



    def __init__(self, **kwargs):
        super(BaseCommentTool, self).__init__(**kwargs)
        self.instancekwargs = kwargs  # depreciated
        self.instancekwargsforchildwdg = kwargs
        self.instancekwargsforchildwdg["parentwidget"] = self

    def initMainToolWidget(self):
        # ****************************************************************************************
        #   userui Field

        self.toolwidgetmain = UserUIField()

        self.formtoolwidgetconfdictmain = {
            "comment": {"linkfield": "id_comment", "widgets": {}},
            "object": {
                "linkfield": "id_object",
                "widgets": {
                    "comment": self.toolwidgetmain.comment,
                },
            },

        }





class UserUIField(QWidget):
    def __init__(self, parent=None):
        super(UserUIField, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), "lamia_form_comment_ui.ui")
        uic.loadUi(uipath, self)
