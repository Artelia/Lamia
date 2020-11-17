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


from qgis.PyQt import uic, QtCore
from qgis.PyQt.QtWidgets import QWidget

from ...base3.qgswidgets.lamia_form_deficiency import BaseDeficiencyTool
from .lamia_form_observation import BaseCarparkObservationTool

import os
import datetime
import qgis


class BaseCarparkDeficiencyTool(BaseDeficiencyTool):

    tooltreewidgetSUBCAT = QtCore.QCoreApplication.translate(
        "base3_cp", "Recognition campain"
    )

    def __init__(self, **kwargs):
        super(BaseCarparkDeficiencyTool, self).__init__(**kwargs)

    def initMainToolWidget(self):

        self.toolwidgetmain = UserUI()
        self.formtoolwidgetconfdictmain = {
            "deficiency": {
                "linkfield": "id_deficiency",
                "widgets": {
                    "deficiencycategory": self.toolwidgetmain.deficiencycategory,
                    "rotationnumber": self.toolwidgetmain.rotationnumber,
                },
            },
            "object": {"linkfield": "id_object", "widgets": {}},
        }

        self.toolwidgetmain.toolButton_num_rot.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.rotationnumber)
        )

        self.dbasechildwdgfield = []
        self.instancekwargs["parentwidget"] = self

        self.dbasechildwdgfield = []
        self.propertieswdgObservation = BaseCarparkObservationTool(
            **self.instancekwargs
        )
        self.dbasechildwdgfield.append(self.propertieswdgObservation)

    def postSaveFeature(self, featurepk=None):
        pass

    def postSelectFeature(self):
        self.updateDateCampagne()

    def updateDateCampagne(self):
        if self.currentFeaturePK is not None:
            liddesordre = self.dbase.getValuesFromPk(
                "deficiency_qgis", ["id_deficiency"], self.currentFeaturePK
            )
            if not liddesordre:
                self.resetCampagneDateTime()
                return

            sql = "SELECT MIN(datetimeobservation), MAX(datetimeobservation) FROM observation"
            sql += " WHERE lid_deficiency = " + str(liddesordre)
            res = self.dbase.query(sql)

            if res:
                mindate, maxdate = res[0]
                if mindate and maxdate:
                    self.toolwidgetmain.dateTimeEdit_start.setDateTime(
                        QtCore.QDateTime.fromString(mindate, "yyyy-MM-dd hh:mm:ss")
                    )
                    self.toolwidgetmain.dateTimeEdit_end.setDateTime(
                        QtCore.QDateTime.fromString(maxdate, "yyyy-MM-dd hh:mm:ss")
                    )
                else:
                    self.resetCampagneDateTime()
            else:
                self.resetCampagneDateTime()
        else:
            self.resetCampagneDateTime()

    def resetCampagneDateTime(self):
        self.toolwidgetmain.dateTimeEdit_start.setSpecialValueText(" ")
        self.toolwidgetmain.dateTimeEdit_start.setDateTime(
            QtCore.QDateTime.fromString("01/01/0001 00:00:00", "dd/MM/yyyy hh:mm:ss")
        )
        self.toolwidgetmain.dateTimeEdit_end.setSpecialValueText(" ")
        self.toolwidgetmain.dateTimeEdit_end.setDateTime(
            QtCore.QDateTime.fromString("01/01/0001 00:00:00", "dd/MM/yyyy hh:mm:ss")
        )


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), "lamia_form_deficiency_ui.ui")
        uic.loadUi(uipath, self)
