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
from ...base3.qgswidgets.lamia_form_topography import BaseTopographyTool
from qgis.PyQt.QtWidgets import QWidget
from qgis.PyQt import uic, QtCore
from .lamia_form_topographydata import BaseConstructionsiteTopographydataTool
from Lamia.iface.qgiswidget.tools.form_subwidgets.subwidget_gpsvalues import (
    GpsValuesWidget,
)


class BaseConstructionsiteTopographyTool(BaseTopographyTool):
    def __init__(self, **kwargs):
        super(BaseConstructionsiteTopographyTool, self).__init__(**kwargs)

    def initMainToolWidget(self):

        self.toolwidgetmain = UserUI()
        self.formtoolwidgetconfdictmain = {
            "topography": {"linkfield": "id_topography", "widgets": {}},
            "object": {"linkfield": "id_object", "widgets": {}},
            "resource": {
                "linkfield": "id_resource",
                "widgets": {
                    "file": self.toolwidgetmain.lineEdit_file,
                    "description": self.toolwidgetmain.lineEdit_nom,
                    "datetimeresource": self.toolwidgetmain.dateTimeEdit_date,
                },
            },
        }
        self.toolwidgetmain.pushButton_chooseph.clicked.connect(self.choosePhoto)
        self.toolwidgetmain.pushButton_open.clicked.connect(self.openFile)
        self.toolwidgetmain.pushButton_ajoutpointGPS.clicked.connect(self.ajoutPointGPS)
        self.toolwidgetmain.pushButton_importer.clicked.connect(self.importer)

        self.toolwidgetmain.pushButton_exportdxf.clicked.connect(self.DxfExport)

        typpointlist = [
            elem[0]
            for elem in self.dbase.dbasetables["topographydata"]["fields"][
                "topographydatacategory"
            ]["Cst"]
        ]
        self.toolwidgetmain.comboBox_typepoints.addItems(typpointlist)

        # typpointlist = [
        #     elem[0]
        #     for elem in self.dbase.dbasetables["topographydata"]["fields"][
        #         "topographydatasubtype"
        #     ]["Cst"]
        # ]
        # self.toolwidgetmain.comboBox_subtypepoints.addItems(typpointlist)

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
        # ****************************************************************************************
        # child widgets
        self.instancekwargs["parentwidget"] = self

        self.dbasechildwdgfield = []
        self.propertieswdgPOINTTOPO = BaseConstructionsiteTopographydataTool(
            **self.instancekwargs
        )
        self.propertieswdgPOINTTOPO.tooltreewidgetSUBCAT = QtCore.QCoreApplication.translate(
            "base3", "Topographic point"
        )

        self.toolwidgetmain.comboBox_typepoints.currentIndexChanged.connect(
            lambda comboindex: self.propertieswdgPOINTTOPO.formutils.comboparentValueChanged(
                comboindex,
                parenttablename="topographydata",
                parentfieldname="topographydatacategory",
                childfield="topographydatatype",
                combochild=self.toolwidgetmain.comboBox_subtypepoints,
            )
        )

        """
        self.propertieswdgPOINTTOPO.initMainToolWidget()
        confdicttopo = self.propertieswdgPOINTTOPO.formtoolwidgetconfdictmain[
            "topographydata"
        ]
        confdicttopo["widgets"]["topographydatatype"] = [
            confdicttopo["widgets"]["topographydatatype"],
            self.toolwidgetmain.comboBox_typepoints,
        ]

        confdicttopo["widgets"]["topographydatatype"] = [
            confdicttopo["widgets"]["topographydatatype"],
            self.toolwidgetmain.comboBox_subtypepoints,
        ]
        """

        self.dbasechildwdgfield.append(self.propertieswdgPOINTTOPO)

        # * gpswidget
        self.gpswidget = GpsValuesWidget(
            parentwdg=self, parentframe=self.toolwidgetmain.frame_gps
        )
        self.lamiawidgets.append(self.gpswidget)

    def postToolTreeWidgetCurrentItemChanged(self):
        self.toolwidgetmain.comboBox_typepoints.currentIndexChanged.emit(0)

    def ajoutPointGPS(self):
        self.propertieswdgPOINTTOPO.toolbarNew()
        self.propertieswdgPOINTTOPO.getGPSValues()
        self.propertieswdgPOINTTOPO.toolwidgetmain.comboBox_type.setCurrentIndex(
            self.toolwidgetmain.comboBox_typepoints.currentIndex()
        )
        self.propertieswdgPOINTTOPO.toolwidgetmain.comboBox_subtype.setCurrentIndex(
            self.toolwidgetmain.comboBox_subtypepoints.currentIndex()
        )
        # self.lastPhoto()
        # self.toolbarGeomAddGPS()
        self.propertieswdgPOINTTOPO.toolbarSave()


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), "lamia_form_topography_ui.ui")
        uic.loadUi(uipath, self)
