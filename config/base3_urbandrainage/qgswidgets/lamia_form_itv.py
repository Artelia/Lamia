# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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
import sys, inspect, logging, textwrap, platform, subprocess

import qgis
from qgis.PyQt import QtGui, uic, QtCore, QtXml
from qgis.PyQt.QtWidgets import QAction, QWidget

from Lamia.qgisiface.iface.qgiswidget.tools.lamia_abstractformtool import (
    AbstractLamiaFormTool,
)
from Lamia.api.libslamia.lamiaITVimport.lamiaITVimport import ITVImportCore


class UrbandrainageITVTool(AbstractLamiaFormTool):

    PREPROTOOLNAME = "itv"
    DBASETABLENAME = "itv"
    LOADFIRST = False

    tooltreewidgetCAT = QtCore.QCoreApplication.translate("base3", "Resources")
    tooltreewidgetSUBCAT = QtCore.QCoreApplication.translate("base3", "ITV")
    tooltreewidgetICONPATH = os.path.join(
        os.path.dirname(__file__), "lamia_form_itv_icon.png"
    )

    CHOOSERTREEWDGSPEC = {"colshow": ["name"]}

    def __init__(self, **kwargs):
        super(UrbandrainageITVTool, self).__init__(**kwargs)
        self.qfiledlg = self.mainifacewidget.qfiledlg
        self.itvcore = ITVImportCore(
            dbaseparser=self.dbase, messageinstance=self.mainifacewidget.connector
        )

    def initMainToolWidget(self):
        self.toolwidgetmain = UserUI()

        self.formtoolwidgetconfdictmain = {
            "itv": {"linkfield": "id_media", "widgets": {}},
            "object": {
                "linkfield": "id_object",
                "widgets": {"name": self.toolwidgetmain.name,},
            },
            "resource": {
                "linkfield": "id_resource",
                "widgets": {
                    # "file": self.toolwidgetmain.lineEdit_file,
                    # "resourceindex": self.toolwidgetmain.spinBox_numphoto,
                    # "datetimeresource": self.toolwidgetmain.dateTimeEdit_date,
                    "file": self.toolwidgetmain.file,
                },
            },
        }

        self.toolwidgetmain.toolButton_filechooser.clicked.connect(self.chooseFile)
        self.toolwidgetmain.pushButton_check.clicked.connect(self.checkAllNodesFound)
        self.toolwidgetmain.pushButton_viewcsv.clicked.connect(self.viewAsCsv)
        self.toolwidgetmain.pushButton_viewaslayer.clicked.connect(self.viewAsLayer)
        self.toolwidgetmain.pushButton_import.clicked.connect(self.runImport)

    def chooseFile(self):
        itvfile = self.qfiledlg.getOpenFileNames(
            None, "Choose the file", self.itvcore.confdatadirproject, "All (*.*)", "",
        )
        if itvfile:
            if isinstance(itvfile, tuple):  # qt5
                itvfile = itvfile[0]
            self.toolwidgetmain.file.setText(";".join(itvfile))

    def checkAllNodesFound(self):
        itvfiles = self.toolwidgetmain.file.text().split(";")
        itvfiles = [self.dbase.completePathOfFile(fl.strip()) for fl in itvfiles]

        noidinlamia, totalnode = self.itvcore.checkNodesExistInLamia(itvfiles)
        self.toolwidgetmain.label_nonodeinlamia.setText(
            f"Nodes not found : {len(noidinlamia)} / {totalnode}"
        )
        print("*", noidinlamia)

    def viewAsCsv(self):
        itvfiles = self.toolwidgetmain.file.text().split(";")
        itvfiles = [self.dbase.completePathOfFile(fl.strip()) for fl in itvfiles]

        csvfile = self.itvcore.getITVCsvFile(itvfiles)

        if platform.system() == "Linux":
            pass
        elif platform.system() == "Windows":
            subprocess.Popen(f'explorer "{os.path.realpath(csvfile)}"')

    def viewAsLayer(self):
        itvfiles = self.toolwidgetmain.file.text().split(";")
        itvfiles = [self.dbase.completePathOfFile(fl.strip()) for fl in itvfiles]

        layer = self.itvcore.getQgsLayer(itvfiles)
        project = qgis.core.QgsProject.instance()
        root = project.layerTreeRoot()
        project.addMapLayer(layer, True)

    def runImport(self):
        pass


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), "lamia_form_itv_ui.ui")
        uic.loadUi(uipath, self)
