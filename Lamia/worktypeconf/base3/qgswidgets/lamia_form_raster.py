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


import os, sys
import datetime

import qgis
from qgis.PyQt import uic, QtCore
from qgis.PyQt.QtWidgets import QWidget

from Lamia.iface.qgiswidget.tools.lamia_abstractformtool import AbstractLamiaFormTool


class BaseRasterTool(AbstractLamiaFormTool):

    PREPROTOOLNAME = "rasters"
    DBASETABLENAME = "rasters"
    LOADFIRST = True

    tooltreewidgetCAT = QtCore.QCoreApplication.translate("base3", "Resources")
    tooltreewidgetSUBCAT = QtCore.QCoreApplication.translate("base3", "Background map")
    tooltreewidgetICONPATH = os.path.join(
        os.path.dirname(__file__), "lamia_form_raster_icon.png"
    )

    def __init__(self, **kwargs):
        super(BaseRasterTool, self).__init__(**kwargs)

    def initMainToolWidget(self):

        self.toolwidgetmain = UserUI()
        self.formtoolwidgetconfdictmain = {
            "rasters": {
                "linkfield": "id_rasters",
                "widgets": {"rastertype": self.toolwidgetmain.comboBox_type},
            },
            "object": {
                "linkfield": "id_object",
                "widgets": {"name": self.toolwidgetmain.lineEdit_libelle},
            },
            "resource": {
                "linkfield": "id_resource",
                "widgets": {
                    "file": self.toolwidgetmain.lineEdit_file,
                    "datetimeresource": self.toolwidgetmain.dateTimeEdit,
                },
            },
        }
        self.toolwidgetmain.pushButton_chooseph.clicked.connect(self.chooseFile)
        self.toolwidgetmain.pushButton_loadraster.clicked.connect(self.loadRaster)

    def loadRaster(self, feat=None):
        libelle = self.toolwidgetmain.lineEdit_libelle.text()
        rlayer = self.createMapLayer()

        qgis.core.QgsProject.instance().addMapLayer(rlayer, False)

        if self.mainifacewidget.qgiscanvas.qgislegendnode is not None:
            self.mainifacewidget.qgiscanvas.qgislegendnode.insertLayer(-1, rlayer)

    def createMapLayer(self, libelle=None):

        typefonddeplan = None
        if libelle is None:
            if self.currentFeaturePK is not None:
                sql = "SELECT file FROM rasters_qgis WHERE pk_rasters = " + str(
                    self.currentFeaturePK
                )
                query = self.dbase.query(sql)
                filetemp = [row[0] for row in query][0]
                layfile = self.dbase.completePathOfFile(filetemp)
            else:
                return
        else:
            sql = (
                "SELECT rastertype, file FROM rasters_qgis WHERE libelle = '"
                + str(libelle)
                + "'"
            )
            query = self.dbase.query(sql)
            typefonddeplan, filetemp = query[0]
            layfile = self.dbase.completePathOfFile(filetemp)

        basename = os.path.basename(layfile).split(".")[0]

        rlayer = None

        if libelle is not None:
            layername = libelle
            if typefonddeplan == "SHP":
                rlayer = qgis.core.QgsVectorLayer(layfile, "test", "ogr")
                qmlfile = os.path.splitext(layfile)[0] + ".qml"
                if os.path.isfile(qmlfile):
                    rlayer.loadNamedStyle(qmlfile)

        else:
            currentmaplayertype = self.toolwidgetmain.comboBox_type.currentText()
            if currentmaplayertype.split("-")[0] == "Raster":
                rlayer = qgis.core.QgsRasterLayer(layfile, basename)
            elif currentmaplayertype.split("-")[0] == "Vecteur":
                if self.toolwidgetmain.lineEdit_libelle.text() == "":
                    layername = basename
                else:
                    layername = self.toolwidgetmain.lineEdit_libelle.text()

                if currentmaplayertype.split("-")[1] == "Shapefile":
                    rlayer = qgis.core.QgsVectorLayer(layfile, layername, "ogr")
                    qmlfile = os.path.splitext(layfile)[0] + ".qml"
                    if os.path.isfile(qmlfile):
                        rlayer.loadNamedStyle(qmlfile)

        return rlayer

    def chooseFile(self):

        file, extension = self.mainifacewidget.qfiledlg.getOpenFileName(
            None,
            "Choose the file",
            self.mainifacewidget.imagedirectory,
            "All (*.*)",
            "",
        )
        if file:
            self.toolwidget.lineEdit_file.setText(os.path.normpath(file))

    def postSelectFeature(self):

        if self.currentFeaturePK is None:
            datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            self.formutils.applyResultDict({"datetimeressource": datecreation}, False)

    def postSaveFeature(self, savedfeaturepk=None):
        pass


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), "lamia_form_raster_ui.ui")
        uic.loadUi(uipath, self)
