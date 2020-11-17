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

from ...base3.qgswidgets.lamia_form_delivery import BaseDeliveryTool


class BaseConstructionsiteDeliveryTool(BaseDeliveryTool):

    LOADFIRST = True
    TABLEFILTERFIELD = {"deliverycategory": "WOR"}

    def __init__(self, **kwargs):
        super(BaseConstructionsiteDeliveryTool, self).__init__(**kwargs)

    def initMainToolWidget(self):
        if self.dbase.variante in [None, "Lamia"]:
            super().initMainToolWidget()
            self.toolwidgetmain.comboBox_deliverycategory.setEnabled(False)
        elif self.dbase.variante in ["Orange"]:
            # for orange
            self.toolwidgetmain = UserUI()
            self.formtoolwidgetconfdictmain = {
                "delivery": {
                    "linkfield": "id_delivery",
                    "widgets": {
                        "contractref": self.toolwidgetmain.lineEdit_nummarche,
                        "datedeliverystarting": self.toolwidgetmain.dateEdit_startdate,
                        "dateestimatedenddelivery": self.toolwidgetmain.dateEdit_enddate,
                        "contractor": self.toolwidgetmain.comboBox_society,
                    },
                },
                "object": {
                    "linkfield": "id_object",
                    "widgets": {"name": self.toolwidgetmain.lineEdit_nom},
                },
            }

            # child widgets
            self.dbasechildwdgfield = []
            self.instancekwargs["parentwidget"] = self

    def postSelectFeature(self):
        if self.currentFeaturePK is None:
            datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d"))
            self.formutils.applyResultDict(
                {
                    "datedeliverystarting": datecreation,
                    "dateestimatedenddelivery": datecreation,
                },
                checkifinforgottenfield=False,
            )


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(
            os.path.dirname(__file__), "lamia_form_delivery_ui_orange.ui"
        )
        uic.loadUi(uipath, self)
