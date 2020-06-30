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
import qgis
from qgis.PyQt import uic, QtGui, QtCore
from qgis.PyQt.QtWidgets import QWidget

from Lamia.iface.qgiswidget.tools.lamia_abstractformtool import AbstractLamiaFormTool
from Lamia.iface.qgiswidget.tools.form_subwidgets.subwidget_gpsvalues import (
    GpsValuesWidget,
)


class BaseTopographydataTool(AbstractLamiaFormTool):

    PREPROTOOLNAME = "topographydata"
    DBASETABLENAME = "topographydata"
    LOADFIRST = False

    tooltreewidgetCAT = QtCore.QCoreApplication.translate("base3", "Resources")
    tooltreewidgetSUBCAT = None
    tooltreewidgetICONPATH = None

    PARENTJOIN = {
        "topography": {
            "colparent": "pk_topography",
            "colthistable": "lpk_topography",
            "tctable": None,
            "tctablecolparent": None,
            "tctablecolthistable": None,
        }
    }

    def __init__(self, **kwargs):
        super(BaseTopographydataTool, self).__init__(**kwargs)

    def initMainToolWidget(self):
        self.toolwidgetmain = UserUI()

        self.formtoolwidgetconfdictmain = {
            "topographydata": {
                "linkfield": "id_topographiedata",
                "widgets": {
                    "topographydatatype": self.toolwidgetmain.comboBox_position,
                    "x": self.toolwidgetmain.doubleSpinBox_X,
                    "y": self.toolwidgetmain.doubleSpinBox_Y,
                    "zmngf": self.toolwidgetmain.doubleSpinBox_Z,
                    "dx": self.toolwidgetmain.doubleSpinBox_dX,
                    "dy": self.toolwidgetmain.doubleSpinBox_dY,
                    "dz": self.toolwidgetmain.doubleSpinBox_dZ,
                    "zwgs84": self.toolwidgetmain.doubleSpinBox_Zwgs84,
                    "zgps": self.toolwidgetmain.doubleSpinBox_Zgps,
                    "raf09": self.toolwidgetmain.doubleSpinBox_raf09,
                    "rodheight": self.toolwidgetmain.doubleSpinBox_hautperche,
                },
            }
        }

        self.toolwidgetmain.pushButton_catchvalues.clicked.connect(self.getGPSValues)

        """
        self.gpswidget = {
            "x": {"widget": self.toolwidgetmain.label_X, "gga": "Xcrs"},
            "y": {"widget": self.toolwidgetmain.label_Y, "gga": "Ycrs"},
            "zmngf": {"widget": self.toolwidgetmain.label_Z, "gga": "zmNGF"},
            "dx": {"widget": self.toolwidgetmain.label_dX, "gst": "xprecision"},
            "dy": {"widget": self.toolwidgetmain.label_dY, "gst": "yprecision"},
            "dz": {"widget": self.toolwidgetmain.label_dZ, "gst": "zprecision"},
            "zgps": {"widget": self.toolwidgetmain.label_zgps, "gga": "elevation"},
            "zwgs84": {"widget": self.toolwidgetmain.label_zwgs84, "gga": "deltageoid"},
            "raf09": {"widget": self.toolwidgetmain.label_raf09, "gga": "RAF09"},
            "hauteurperche": {
                "widget": self.toolwidgetmain.label_hautperche,
                "gga": "hauteurperche",
            },
        }
        """

        # * gpswidget
        self.gpswidget = GpsValuesWidget(
            parentwdg=self, parentframe=self.toolwidgetmain.frame_gps
        )
        self.lamiawidgets.append(self.gpswidget)

    def postSelectFeature(self):
        pass

    def enablePropertiesButtons(self, boolvalue):
        pass

    def magicFunction(self):
        self.featureSelected()
        self.userwdg.comboBox_position.setCurrentIndex(
            self.userwdg.comboBox_position.findText("Crete")
        )
        success = self.getGPSValues()
        if success:
            self.saveFeature()

    def deleteParentFeature(self):
        return True

    def postSaveFeature(self, boolnewfeature):
        pass

    def getGPSValues(self):
        if self.mainifacewidget.gpsutil is not None:
            if self.mainifacewidget.gpsutil.currentpoint is None:
                self.mainifacewidget.errorMessage(
                    QtCore.QCoreApplication.translate("base3", "GPS not connected")
                )
                return False

            self.assignValue(
                self.gpswidget.label_X, self.toolwidgetmain.doubleSpinBox_X
            )
            self.assignValue(
                self.gpswidget.label_dX, self.toolwidgetmain.doubleSpinBox_dX
            )
            self.assignValue(
                self.gpswidget.label_Y, self.toolwidgetmain.doubleSpinBox_Y
            )
            self.assignValue(
                self.gpswidget.label_dY, self.toolwidgetmain.doubleSpinBox_dY
            )
            self.assignValue(
                self.gpswidget.label_Z, self.toolwidgetmain.doubleSpinBox_Z
            )
            self.assignValue(
                self.gpswidget.label_dZ, self.toolwidgetmain.doubleSpinBox_dZ
            )
            # **
            self.assignValue(
                self.gpswidget.label_zgps, self.toolwidgetmain.doubleSpinBox_Zgps
            )
            self.assignValue(
                self.gpswidget.label_hautperche,
                self.toolwidgetmain.doubleSpinBox_hautperche,
            )
            self.assignValue(
                self.gpswidget.label_zwgs84, self.toolwidgetmain.doubleSpinBox_Zwgs84
            )
            self.assignValue(
                self.gpswidget.label_raf09, self.toolwidgetmain.doubleSpinBox_raf09
            )
            """
            for i, fieldname in enumerate(self.gpswidget.keys()):
                try:
                    value = float(self.gpswidget[fieldname]["widget"].text())
                except ValueError:
                    value = None
                if value is not None:
                    self.formtoolwidgetconfdict[self.dbasetablename]["widgets"][
                        fieldname
                    ].setValue(value)
                else:
                    self.formtoolwidgetconfdict[self.dbasetablename]["widgets"][
                        fieldname
                    ].setValue(-1.0)

            self.mainifacewidget.qgiscanvas.createorresetRubberband(0)
            """
            self.setTempGeometry([self.mainifacewidget.gpsutil.currentpoint], False)
            return True
        else:
            self.errorMessage(
                QtCore.QCoreApplication.translate("base3", "GPS not connected")
            )
            return False

    def assignValue(self, wdgfrom, wdgto):
        if self.isfloat(wdgfrom.text()):
            wdgto.setValue(float(wdgfrom.text()))

    def isfloat(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(
            os.path.dirname(__file__), "lamia_form_topographydata_ui.ui"
        )
        uic.loadUi(uipath, self)
