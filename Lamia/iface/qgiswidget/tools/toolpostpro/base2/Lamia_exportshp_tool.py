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
from qgis.PyQt.QtWidgets import (QAction, QWidget)

from ...lamia_abstracttool import AbstractLamiaTool
from ...subwidgets.abstractfilemanager import AbstractFileManager
from Lamia.libslamia.lamiaexportshp.lamiaexportshp import ExportShapefileCore


class ExportShapefileTool(AbstractLamiaTool):

    POSTPROTOOLNAME = ExportShapefileCore.POSTPROTOOLNAME

    tooltreewidgetCAT = 'Import/export'
    tooltreewidgetSUBCAT = 'Export shp'
    tooltreewidgetICONPATH = os.path.join(os.path.dirname(__file__), 'Lamia_exportshp_tool_icon.png')

    choosertreewidgetMUTIPLESELECTION = True

    def __init__(self, **kwargs):
        super(ExportShapefileTool, self).__init__(**kwargs)

        self.qfiledlg = self.mainifacewidget.qfiledlg
        #self.confdatamain = os.path.join(os.path.dirname(inspect.getsourcefile(self.__class__)), self.POSTPROTOOLNAME)
        #self.confdataproject = os.path.join(self.dbase.dbaseressourcesdirectory, 'config',self.POSTPROTOOLNAME)

        self.exporttool = ExportShapefileCore(dbaseparser=self.dbase,
                                              messageinstance=self.mainifacewidget.connector)
        self.filemanager = ExportShpfileManager(self.mainifacewidget, self.exporttool , '.txt')

    """
    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Import/export'
        self.NAME = 'Export shp'
        self.visualmode = [4]
        # self.PointENABLED = True
        # self.LineENABLED = True
        # self.PolygonEnabled = True
        # self.magicfunctionENABLED = True
        # self.linkagespec = None
        # self.pickTable = None
        # print(self.dbase.recentsdbase)

        self.iconpath = os.path.join(os.path.dirname(__file__), 'Lamia_exportshp_tool_icon.png')
        #self.qtreewidgetfields = ['libelle']

        # ****************************************************************************************
        # properties ui
        self.groupBox_elements.setParent(None)
        self.frame_editing.setParent(None)

        self.filemanager = ExportShpfileManager(self.windowdialog, self, '.txt')




        self.qfiledlg = self.windowdialog.qfiledlg

        self.confdatamain = os.path.join(os.path.dirname(inspect.getsourcefile(self.__class__)), self.TOOLNAME)
        self.confdataproject = os.path.join(self.dbase.dbaseressourcesdirectory, 'config',self.TOOLNAME)
    """

    def initMainToolWidget(self):

        self.toolwidgetmain = UserUI()
        self.toolwidgetmain.toolButton_filechooser.clicked.connect(self.chooseFile)

        self.toolwidgetmain.pushButton_export.clicked.connect(self.runExport)

        self.toolwidgetmain.groupBox_filemanager.layout().addWidget(self.filemanager)

        self.choosertreewidget = self.mainifacewidget.toolwidgets['toolprepro']['Zone geographique'][0].choosertreewidget



    def chooseFile(self):
        reportfile = self.qfiledlg.getSaveFileName(self,
                                                   'InspectionDigue nouveau',
                                                   '',
                                                   'Shapefile (*.shp)')
        if reportfile:
            if isinstance(reportfile, tuple):    # qt5
                reportfile = reportfile[0]
            self.toolwidgetmain.lineEdit_nom.setText(reportfile)


    def postToolTreeWidgetCurrentItemChanged(self):
        self.filemanager.reset()


    def runExport(self):

        debug = False
        shpfile = self.toolwidgetmain.lineEdit_nom.text()
        tabletypepath = self.filemanager.getCurrentPath()


        # selectedzonegeoitems = self.choosertreewidget.treewidget.selectedItems()
        # ids = [int(item.text(0)) for item in selectedzonegeoitems]
        # pdids = self.choosertreewidget.ids
        # pks = [pdids.loc[pdids['id'] == id]['pk'].values[0] for id in ids]
        pks = self.choosertreewidget.getSelectedPks()

        self.exporttool.runExport(destinationshapefile=shpfile, 
                                    exportconffilepath=tabletypepath, 
                                    pkzonegeos=pks)


        #prepareData(destinationshapefile, tablepath, postfunc = None):
        


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'Lamia_exportshp_tool.ui')
        uic.loadUi(uipath, self)


class ExportShpfileManager(AbstractFileManager):

    #def __init__(self,  mainwindows=None, parentwdg=None, fileext=None):
    def __init__(self,  mainwindows=None, toolclass=None, fileext=None):
        super(ExportShpfileManager, self).__init__(mainwindows, toolclass, fileext)


    def new(self):

        #if not os.path.exists(self.confdataproject):
        #    os.mkdir(self.confdataproject)

        confpath , confext= self.qfiledialog.getSaveFileName(None, 'Choose the file', self.confdataproject,
                                                                    'txt (*.txt)', '')
        
        if confpath:
            self.parentwdg.new(confpath)

            if False:
                if confpath:
                    conf_file = open(confpath, 'w', encoding="utf-8")
                    conftxt =   """
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
            txttofind = self.projectcharacter + os.path.splitext(os.path.basename(confpath))[0]
            indexcombo = self.comboBox_files.findText(txttofind)
            self.comboBox_files.setCurrentIndex(indexcombo)

    def comboChanged(self, comboindex):
        super().comboChanged(comboindex)
        tabletypepath = self.getCurrentPath()
        if tabletypepath:
            boolzonegeo = self.toolclass.testIfZonegeoPk(champsfile=tabletypepath)
            self.mainwindows.ElemtreeWidget.clearSelection()
            self.mainwindows.ElemtreeWidget.setEnabled(boolzonegeo)



        