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
import platform
import subprocess

from qgis.PyQt import uic, QtCore
from qgis.PyQt.QtWidgets import QWidget

from lamiaapi.libslamia.lamiadxfexport.lamiadxfexport import ExporDxfCore

from lamiaqgisiface.iface.qgiswidget.tools.lamia_abstractformtool import (
    AbstractLamiaFormTool,
)
from .lamia_form_topographydata import BaseTopographydataTool
from lamiaqgisiface.iface.qgiswidget.tools.form_subwidgets.subwidget_gpsvalues import (
    GpsValuesWidget,
)


base3 = QtCore.QObject()


class BaseTopographyTool(AbstractLamiaFormTool):

    PREPROTOOLNAME = "topography"
    DBASETABLENAME = "topography"
    LOADFIRST = True

    tooltreewidgetCAT = QtCore.QCoreApplication.translate("base3", "Resources")
    tooltreewidgetSUBCAT = QtCore.QCoreApplication.translate("base3", "Topography")
    tooltreewidgetICONPATH = os.path.join(
        os.path.dirname(__file__), "lamia_form_topography_icon.png"
    )

    PARENTJOIN = {
        "delivery": {
            "colparent": "id_delivery",
            "colthistable": "lid_delivery",
            "tctable": None,
            "tctablecolparent": None,
            "tctablecolthistable": None,
        }
    }

    def __init__(self, **kwargs):
        super(BaseTopographyTool, self).__init__(**kwargs)
        self.instancekwargs = kwargs
        self.lamiadxfexport = ExporDxfCore(self.dbase)

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

        typpointlist = [
            elem[0]
            for elem in self.dbase.dbasetables["topographydata"]["fields"][
                "topographydatatype"
            ]["Cst"]
        ]
        self.toolwidgetmain.comboBox_typepoints.addItems(typpointlist)

        # * child widgets
        self.instancekwargs["parentwidget"] = self

        self.dbasechildwdgfield = []
        self.propertieswdgPOINTTOPO = BaseTopographydataTool(**self.instancekwargs)
        self.propertieswdgPOINTTOPO.tooltreewidgetSUBCAT = QtCore.QCoreApplication.translate(
            "base3", "Topographic point"
        )
        self.dbasechildwdgfield.append(self.propertieswdgPOINTTOPO)

        # * gpswidget
        self.gpswidget = GpsValuesWidget(
            parentwdg=self, parentframe=self.toolwidgetmain.frame_gps
        )
        self.lamiawidgets.append(self.gpswidget)

    def postSaveFeature(self, savedfeaturepk=None):

        if (
            self.currentFeaturePK is not None
            and self.currentFeaturePK != savedfeaturepk
        ):  # new version of feature
            # fieldstoappend
            pointtopofields = list(
                self.dbase.dbasetables["topographiedata"]["fields"].keys()
            )
            pointtopofields.remove("pk_topographydata")
            indexpktopo = pointtopofields.index("lpk_topography")
            pointtopofields.insert(-1, "ST_AsText(geom)")

            sql = (
                "SELECT "
                + ",".join(pointtopofields)
                + " FROM topographydata WHERE lpk_topography = "
                + str(self.currentFeaturePK)
            )
            results = self.dbase.query(sql)
            results = [list(res) for res in results]

            for i, res in enumerate(results):
                results[i][indexpktopo] = self.currentFeaturePK

            pointtopofields[pointtopofields.index("ST_AsText(geom)")] = "geom"

            for res in results:
                sql = self.dbase.createSetValueSentence(
                    type="INSERT",
                    tablename="topographydata",
                    listoffields=pointtopofields,
                    listofrawvalues=res,
                )

                self.dbase.query(sql, docommit=False)

            self.dbase.commit()

    def openFile(self):
        filepath = self.completePathOfFile(self.userwdg.lineEdit_file.text())
        if filepath != "":
            os.startfile(filepath)

    def ajoutPointGPS(self):
        self.propertieswdgPOINTTOPO.toolbarNew()
        self.propertieswdgPOINTTOPO.getGPSValues()
        self.propertieswdgPOINTTOPO.toolwidgetmain.comboBox_position.setCurrentIndex(
            self.toolwidgetmain.comboBox_typepoints.currentIndex()
        )
        self.propertieswdgPOINTTOPO.toolbarSave()

    def importer(self):
        pass

    def choosePhoto(self):
        file, extension = self.mainifacewidget.qfiledlg.getOpenFileNameAndFilter(
            None, "Choose the file", self.dbase.imagedirectory, "All (*.*)", ""
        )
        if file:
            self.userwdg.lineEdit_file.setText(os.path.normpath(file))

    # def postInitFeatureProperties(self, feat):
    def postSelectFeature(self):
        if self.currentFeaturePK is None:  # first creation
            datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            self.formutils.applyResultDict(
                {"datetimeresource": datecreation}, checkifinforgottenfield=False
            )

    def DxfExport(self):
        if self.currentFeaturePK:
            currentid = self.dbase.getValuesFromPk(
                "topography", "id_topography", self.currentFeaturePK
            )
            date = str(datetime.datetime.now().strftime("%Y%m%d_%H%M%S"))
            dxffilename = str(currentid) + "_topography_" + date + ".dxf"

            filepath = self.lamiadxfexport.exportTopography(
                self.currentFeaturePK, dxffilename
            )

            if platform.system() == "Windows":
                subprocess.Popen(
                    f'explorer "{os.path.realpath(os.path.abspath(os.path.dirname(filepath)))}"'
                )


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), "lamia_form_topography_ui.ui")
        uic.loadUi(uipath, self)
