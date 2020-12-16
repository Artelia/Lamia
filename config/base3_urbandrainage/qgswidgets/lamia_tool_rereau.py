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
import io
import sys

import qgis
from qgis.PyQt import uic, QtGui, QtCore
from qgis.PyQt.QtWidgets import (
    QWidget,
    QLabel,
    QFrame,
    QTreeWidgetItem,
    QHeaderView,
    QAbstractItemView,
    QTableWidgetItem,
)

from Lamia.qgisiface.iface.qgiswidget.tools.lamia_abstracttool import AbstractLamiaTool
from Lamia.api.libslamia.lamiaITVimport.lamiaITVimport import ITVImportCore
from Lamia.qgisiface.iface.qgiswidget.tools.general_subwidgets.abstractfilemanager import (
    AbstractFileManager,
)
import numpy as np
import shutil, platform, subprocess
import logging


# ********************************************************************************************************************
# ********************************* Main Widget                *******************************************************
# ********************************************************************************************************************

# class PathTool(AbstractInspectionDigueTool):
class RereauTool(AbstractLamiaTool):

    # DBASES = ["digue", "base_digue"]
    # TOOLNAME = "Networktool"

    POSTPROTOOLNAME = ITVImportCore.POSTPROTOOLNAME

    tooltreewidgetCAT = QtCore.QCoreApplication.translate("base3", "Analytics")
    tooltreewidgetSUBCAT = QtCore.QCoreApplication.translate("base3", "Rer'eau")
    tooltreewidgetICONPATH = os.path.join(
        os.path.dirname(__file__), "lamia_tool_network_icon.png"
    )
    choosertreewidgetMUTIPLESELECTION = True

    def __init__(self, **kwargs):
        super(RereauTool, self).__init__(**kwargs)

        self.itvcore = ITVImportCore(
            dbaseparser=self.dbase, messageinstance=self.mainifacewidget.connector
        )

        self.filemanager = RereaufileManager(self.mainifacewidget, self.itvcore)

    def initMainToolWidget(self):

        # userui

        self.toolwidgetmain = UserUI()

        self.toolwidgetmain.groupBox_filemanager.layout().addWidget(self.filemanager)
        self.choosertreewidget = self.mainifacewidget.toolwidgets[
            "itv"
        ].choosertreewidget

        self.toolwidgetmain.pushButton_analysis.clicked.connect(self.computeRereau)


    def computeRereau(self):
        tabletypepath = self.filemanager.getCurrentText()

        pks = self.choosertreewidget.getSelectedPks()

        csvfile = self.itvcore.getComputeNotationCsvFile(tabletypepath, pks)

        if platform.system() == "Linux":
            pass
        elif platform.system() == "Windows":
            subprocess.Popen(f'explorer "{os.path.realpath(csvfile)}"')

    def postToolTreeWidgetCurrentItemChanged(self):
        self.filemanager.reset()


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), "lamia_tool_rereau_ui.ui")
        uic.loadUi(uipath, self)


class RereaufileManager(AbstractFileManager):

    # def __init__(self,  mainwindows=None, parentwdg=None, fileext=None):
    def __init__(self, mainwindows=None, toolclass=None):
        super(RereaufileManager, self).__init__(mainwindows, toolclass)

    def new(self):

        # if not os.path.exists(self.confdataproject):
        #    os.mkdir(self.confdataproject)

        confpath, confext = self.qfiledialog.getSaveFileName(
            None,
            "Choose the file",
            self.toolclass.confdatadirproject,
            "csv (*.csv)",
            "",
        )

        if confpath:
            self.toolclass.newNotation(confpath)

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
            if platform.system() == "Linux":
                pass
            elif platform.system() == "Windows":
                subprocess.Popen(f'explorer "{os.path.realpath(confpath)}"')

            # txttofind = (
            #     self.toolclass.projectcharacter
            #     + os.path.splitext(os.path.basename(confpath))[0]
            # )
            # indexcombo = self.comboBox_files.findText(txttofind)
            # self.comboBox_files.setCurrentIndex(indexcombo)

    # def comboChanged(self, comboindex):
    #     super().comboChanged(comboindex)
    #     confname = self.comboBox_files.itemText(comboindex)
    #     tabletypepath = self.toolclass.getConfFilePath(confname)
    #     if tabletypepath:
    #         boolzonegeo = self.toolclass.testIfZonegeoPk(champsfile=tabletypepath)
    #         self.mainwindows.ElemtreeWidget.clearSelection()
    #         self.mainwindows.ElemtreeWidget.setEnabled(boolzonegeo)
