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

import networkx
import numpy as np
from collections import OrderedDict
import glob, sys, logging, inspect, textwrap
import os
import re
import logging

import qgis
import qgis.core
from qgis.PyQt import QtGui, uic, QtCore, QtXml
from qgis.PyQt.QtPrintSupport import QPrinter
from qgis.PyQt.QtWidgets import (
    QProgressBar,
    QApplication,
    QAction,
    QWidget,
    QAbstractItemView,
)

# from ...libs import pyqtgraph as pg


# from ...Lamia_abstract_tool import AbstractLamiaTool
from Lamia.qgisiface.iface.qgiswidget.tools.lamia_abstracttool import AbstractLamiaTool
from Lamia.qgisiface.iface.qgiswidget.tools.general_subwidgets.abstractfilemanager import (
    AbstractFileManager,
)
from Lamia.api.libslamia.lamiareport.lamiareport import ReportCore


class ReportTool(AbstractLamiaTool):

    POSTPROTOOLNAME = ReportCore.POSTPROTOOLNAME

    tooltreewidgetCAT = QtCore.QCoreApplication.translate("base3", "Import/export")
    tooltreewidgetSUBCAT = QtCore.QCoreApplication.translate("base3", "Report printing")
    tooltreewidgetICONPATH = os.path.join(
        os.path.dirname(__file__), "lamia_tool_report_icon.png"
    )

    choosertreewidgetMUTIPLESELECTION = True

    def __init__(self, **kwargs):
        super(ReportTool, self).__init__(**kwargs)
        # self.postInit()
        self.qfiledlg = self.mainifacewidget.qfiledlg
        self.confdatamain = os.path.join(
            os.path.dirname(inspect.getsourcefile(self.__class__)), self.POSTPROTOOLNAME
        )
        self.confdataproject = os.path.join(
            self.dbase.dbaseressourcesdirectory, "config", self.POSTPROTOOLNAME
        )

        self.reporttool = ReportCore(
            dbaseparser=self.dbase, messageinstance=self.mainifacewidget.connector
        )

        self.filemanager = ExportRapportFileManager(
            self.mainifacewidget, self.reporttool, ".txt"
        )

    def initMainToolWidget(self):

        self.toolwidgetmain = UserUI()
        self.toolwidgetmain.toolButton_filechooser.clicked.connect(self.chooseFile)

        self.toolwidgetmain.groupBox_filemanager.layout().addWidget(self.filemanager)

        self.toolwidgetmain.pushButton_export.clicked.connect(self.launchRapport)

        if qgis.utils.iface is None:
            self.toolwidgetmain.lineEdit_nom.setText(
                "c://000_testdigue//test_rapport.pdf"
            )

        self.choosertreewidget = self.mainifacewidget.toolwidgets[
            "geoarea"
        ].choosertreewidget

    def chooseFile(self):
        reportfile = self.qfiledlg.getSaveFileName(
            self, "Lamia - impression rapport", "", "PDF (*.pdf)"
        )
        if reportfile:
            if isinstance(reportfile, tuple):  # qt5
                reportfile = reportfile[0]
            self.toolwidgetmain.lineEdit_nom.setText(reportfile)

    def postToolTreeWidgetCurrentItemChanged(self):
        # self.toolwidgetmain.setEnabled(True)
        self.filemanager.reset()

        # self.createconfData()

        # self.linkedtreewidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        # self.linkedtreewidget.itemSelectionChanged.connect(self.itemChanged)

    def launchRapport(self):
        pdffile = self.toolwidgetmain.lineEdit_nom.text()
        # reporttype = self.toolwidgetmain .comboBox_type.currentText()

        # print(self.confData.keys())

        reporttype = self.filemanager.getCurrentText()
        # tabletypepath = self.filemanager.getCurrentPath()

        # selectedzonegeoitems = self.choosertreewidget.treewidget.selectedItems()
        # ids = [int(item.text(0)) for item in selectedzonegeoitems]
        # pdids = self.choosertreewidget.ids
        # pks = [pdids.loc[pdids['id'] == id]['pk'].values[0] for id in ids]
        pks = self.choosertreewidget.getSelectedPks()

        self.reporttool.runReport(
            destinationfile=pdffile, reportconffilename=reporttype, pkzonegeos=pks
        )


class ExportRapportFileManager(AbstractFileManager):
    def __init__(self, mainwindows=None, parentwdg=None, fileext=None):
        super(ExportRapportFileManager, self).__init__(mainwindows, parentwdg, fileext)

    def new(self):

        # if not os.path.exists(self.confdataproject):
        #    os.mkdir(self.confdataproject)

        confpath, confext = self.qfiledialog.getSaveFileName(
            None, "Choose the file", self.confdataproject, "txt (*.txt)", ""
        )

        if confpath:
            self.parentwdg.new(confpath)

            if False:
                if confpath:
                    conf_file = open(confpath, "w", encoding="utf-8")
                    conftxt = """
                                ###atlaslayersql
                                # requete sql pour définir la table utilisée pour l'atlas
                                SELECT Desordre_now.* 
                                FROM Desordre_now
                                WHERE groupedesordre = 'INF'
                                ###atlaslayerid
                                # l'identifiant de l'atalslayer
                                id_desordre
                                ###spatial
                                # indique si l'atalslayer est une couche spatiale ou pas
                                True
                                ###ordering
                                # type d'ordonnancement si rien : par id croissant, sinon  autoalongpath
                                #type; constraint (qgis typo)
                                autoalongpath;
                                ###atlaslayerstyle
                                #un style particulier pour l'atlaslayer
                                Desordres_atlas.qml
                                ###atlasdrivemap
                                # caractéristiques de la carte (map) qui suit les objets de l'atlas
                                #itemname;   minscale;   typescale;      layers
                                map1;       2500;       Predefined      ;['atlaslayer','Infralineaire', 'ortho']
                                ###generalmap
                                # caractéristiques de la carte (map) générale
                                # itemname;   minscale;   typescale; layers
                                map0    ;           ;             ; ['Infralineaire','Equipement', 'scan25']
                                #map0    ;           ;             ; []
                                ###images
                                # traitement des éléments de type image
                                #itemname   ; type
                                logo;logo
                                ###childprint
                                # impression à la suite d'autres conf d'impression
                                #confname;                linkcolumn;             optionsql
                                Desordres_observation;    Observation_now.lid_desordre ; ORDER BY Observation_now.datetimeobservation DESC
                                """

                    conf_file.write(textwrap.dedent(conftxt))
                    conf_file.close()

            self.reset()

            txttofind = (
                self.projectcharacter + os.path.splitext(os.path.basename(confpath))[0]
            )
            indexcombo = self.comboBox_files.findText(txttofind)
            self.comboBox_files.setCurrentIndex(indexcombo)


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        # self.setupUi(self)
        uipath = os.path.join(os.path.dirname(__file__), "lamia_tool_report_ui.ui")
        uic.loadUi(uipath, self)
