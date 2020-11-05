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
import sys, inspect, logging, textwrap

import qgis
from qgis.PyQt import QtGui, uic, QtCore, QtXml
from qgis.PyQt.QtWidgets import QAction, QWidget

from Lamia.qgisiface.iface.qgiswidget.tools.lamia_abstracttool import AbstractLamiaTool
from Lamia.qgisiface.iface.qgiswidget.tools.general_subwidgets.abstractfilemanager import (
    AbstractFileManager,
)
from Lamia.api.libslamia.lamiaexportshp.lamiaexportshp import ExportShapefileCore


class ExportShapefileTool(AbstractLamiaTool):

    POSTPROTOOLNAME = ExportShapefileCore.POSTPROTOOLNAME

    tooltreewidgetCAT = QtCore.QCoreApplication.translate("base3", "Import/export")
    tooltreewidgetSUBCAT = QtCore.QCoreApplication.translate("base3", "Export shp")
    tooltreewidgetICONPATH = os.path.join(
        os.path.dirname(__file__), "lamia_tool_exportshp_icon.png"
    )

    choosertreewidgetMUTIPLESELECTION = True

    def __init__(self, **kwargs):
        super(ExportShapefileTool, self).__init__(**kwargs)

        self.qfiledlg = self.mainifacewidget.qfiledlg
        self.exporttool = ExportShapefileCore(
            dbaseparser=self.dbase, messageinstance=self.mainifacewidget.connector
        )
        self.filemanager = ExportShpfileManager(self.mainifacewidget, self.exporttool)

    def initMainToolWidget(self):
        self.toolwidgetmain = UserUI()
        self.toolwidgetmain.toolButton_filechooser.clicked.connect(self.chooseFile)

        self.toolwidgetmain.pushButton_export.clicked.connect(self.runExport)

        self.toolwidgetmain.groupBox_filemanager.layout().addWidget(self.filemanager)

        self.choosertreewidget = self.mainifacewidget.toolwidgets[
            "geoarea"
        ].choosertreewidget

    def chooseFile(self):
        reportfile = self.qfiledlg.getSaveFileName(
            self,
            QtCore.QCoreApplication.translate("base3", "Lamia new"),
            "",
            "Shapefile (*.shp)",
        )
        if reportfile:
            if isinstance(reportfile, tuple):  # qt5
                reportfile = reportfile[0]
            self.toolwidgetmain.lineEdit_nom.setText(reportfile)

    def postToolTreeWidgetCurrentItemChanged(self):
        self.filemanager.reset()

    def runExport(self):

        debug = False
        shpfile = self.toolwidgetmain.lineEdit_nom.text()
        tabletypepath = self.filemanager.getCurrentText()

        # selectedzonegeoitems = self.choosertreewidget.treewidget.selectedItems()
        # ids = [int(item.text(0)) for item in selectedzonegeoitems]
        # pdids = self.choosertreewidget.ids
        # pks = [pdids.loc[pdids['id'] == id]['pk'].values[0] for id in ids]
        pks = self.choosertreewidget.getSelectedPks()

        self.exporttool.runExport(
            destinationshapefile=shpfile,
            exportconffilepath=tabletypepath,
            pkzonegeos=pks,
        )


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), "lamia_tool_exportshp_ui.ui")
        uic.loadUi(uipath, self)


class ExportShpfileManager(AbstractFileManager):

    # def __init__(self,  mainwindows=None, parentwdg=None, fileext=None):
    def __init__(self, mainwindows=None, toolclass=None):
        super(ExportShpfileManager, self).__init__(mainwindows, toolclass)

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
                                # les lignes de commentaires commencent par #
                                
                                # la requete sql créée est formée ainsi :
                                #   SELECT [enumération des valeursql]
                                #   FROM [requete ecrite dans le ###main]
                                
                                # Le choix des champs à selectionner pour l'export se fait ainsi :
                                # ex :
                                # ###Noeud 
                                # #nom              ;type (Int, Double, String);  cst (nom du champ pour convertion trigamme); valeursql                    
                                # id_noeud;          Int;                      ;               id_noeud
                                
                                # avec :
                                # ###Noeud : nom de la table utilisée par convertir les trigrammes vers valeur texte
                                # nom : le nom du champ dans le shp
                                # type : le type dans le shp  : Int, Double, String
                                # champ de convertion : le nom du champ pour la convertion du trigramme vers du texte
                                # valeursql : la valeur (en sql) à prendre : peut etre un champ de la table, ou une requete sql
                                
                                # Pour choisir la géométrie considérée pour le shp 
                                # ###geom
                                # geom;         Int;               ;                  ST_AsText(Noeud_now.geom)
                                
                                # Enfin décrirer la requete FROM ..
                                # ###main 
                                # FROM Noeud_now
                                
                                # ici la requete utilisée pour la création du shp est 
                                # SELECT id_noeud FROM Noeud_now 
                                
                                # ex :

                                ###Noeud 
                                #nom              ;type     ;champ de convertion trigramme ? ; valeursql
                                id_noeud         ; Int      ;                                ; id_noeud
                                
                                ###geom
                                geom;         Int;               ;                  ST_AsText(Noeud_now.geom)
                                
                                ###main 
                                FROM Noeud_now
                                """
                    conf_file.write(textwrap.dedent(conftxt))
                    conf_file.close()

            self.reset()
            txttofind = (
                self.projectcharacter + os.path.splitext(os.path.basename(confpath))[0]
            )
            indexcombo = self.comboBox_files.findText(txttofind)
            self.comboBox_files.setCurrentIndex(indexcombo)

    def comboChanged(self, comboindex):
        super().comboChanged(comboindex)
        confname = self.comboBox_files.itemText(comboindex)
        tabletypepath = self.toolclass.getConfFilePath(confname)
        if tabletypepath:
            boolzonegeo = self.toolclass.testIfZonegeoPk(champsfile=tabletypepath)
            self.mainwindows.ElemtreeWidget.clearSelection()
            self.mainwindows.ElemtreeWidget.setEnabled(boolzonegeo)
