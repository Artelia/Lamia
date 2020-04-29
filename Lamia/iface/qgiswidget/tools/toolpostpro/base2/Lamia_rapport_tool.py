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
from qgis.PyQt.QtWidgets import  (QProgressBar, QApplication,QAction, QWidget, QAbstractItemView)
# from ...libs import pyqtgraph as pg


#from ...Lamia_abstract_tool import AbstractLamiaTool
from ...lamia_abstracttool import AbstractLamiaTool
from ...subwidgets.abstractfilemanager import AbstractFileManager
from Lamia.libslamia.lamiareport.lamiareport import ReportCore


class RapportTool(AbstractLamiaTool):

    POSTPROTOOLNAME = ReportCore.POSTPROTOOLNAME

    tooltreewidgetCAT = 'Import/export'
    tooltreewidgetSUBCAT = 'Impression rapport'
    tooltreewidgetICONPATH = os.path.join(os.path.dirname(__file__), 'Lamia_rapport_tool_icon.png')

    choosertreewidgetMUTIPLESELECTION = True

    def __init__(self, **kwargs):
        super(RapportTool, self).__init__(**kwargs)
        # self.postInit()
        self.qfiledlg = self.mainifacewidget.qfiledlg
        self.confdatamain = os.path.join(os.path.dirname(inspect.getsourcefile(self.__class__)), self.POSTPROTOOLNAME)
        self.confdataproject = os.path.join(self.dbase.dbaseressourcesdirectory, 'config',self.POSTPROTOOLNAME)

        self.reporttool = ReportCore(dbaseparser=self.dbase,
                                     messageinstance=self.mainifacewidget.connector)

        self.filemanager = ExportRapportFileManager(self.mainifacewidget, self.reporttool , '.txt')

    """
    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Import/export'
        self.NAME = 'Impression rapport'
        self.dbasetablename = 'Zonegeo'
        self.visualmode = [4]
        # self.PointENABLED = True
        # self.LineENABLED = True
        # self.PolygonEnabled = True
        # self.magicfunctionENABLED = True
        # self.linkagespec = None
        # self.pickTable = None
        # print(self.dbase.recentsdbase)
        self.multipleselection = True

        self.iconpath = os.path.join(os.path.dirname(__file__), 'Lamia_rapport_tool_icon.png')
        self.qtreewidgetfields = ['libelle']

        # ****************************************************************************************
        # properties ui
        self.groupBox_elements.setParent(None)
        self.frame_editing.setParent(None)

        self.filemanager = ExportRapportFileManager(self.windowdialog, self, '.txt')

        self.qfiledlg = self.windowdialog.qfiledlg
        self.confData = None

        self.confdatamain = os.path.join(os.path.dirname(inspect.getsourcefile(self.__class__)), self.TOOLNAME)
        self.confdataproject = os.path.join(self.dbase.dbaseressourcesdirectory, 'config',self.TOOLNAME)

        if False:
            print(inspect.getmodule(self))
            #self.impressionpdfworker = inspect.getmodule(self).printPDFBaseWorker(dbase=self.dbase)
            self.impressionpdfworker = printPDFBaseWorker(dbase=self.dbase)
            print(self.impressionpdfworker.NAME )
    """


    def initMainToolWidget(self):

        self.toolwidgetmain  = UserUI()
        self.toolwidgetmain .toolButton_filechooser.clicked.connect(self.chooseFile)

        self.toolwidgetmain .groupBox_filemanager.layout().addWidget(self.filemanager)

        self.toolwidgetmain .pushButton_export.clicked.connect(self.launchRapport)

        if qgis.utils.iface is None:
            self.toolwidgetmain .lineEdit_nom.setText('c://000_testdigue//test_rapport.pdf')

        self.choosertreewidget = self.mainifacewidget.toolwidgets['toolprepro']['Zone geographique'][0].choosertreewidget


    def chooseFile(self):
        reportfile = self.qfiledlg.getSaveFileName(self,
                                                   'Lamia - impression rapport',
                                                   '',
                                                   'PDF (*.pdf)')
        if reportfile:
            if isinstance(reportfile, tuple):    # qt5
                reportfile = reportfile[0]
            self.toolwidgetmain .lineEdit_nom.setText(reportfile)


    def postToolTreeWidgetCurrentItemChanged(self):
        #self.toolwidgetmain.setEnabled(True)
        self.filemanager.reset()

        #self.createconfData()

        #self.linkedtreewidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        #self.linkedtreewidget.itemSelectionChanged.connect(self.itemChanged)



    def launchRapport(self):
        pdffile = self.toolwidgetmain.lineEdit_nom.text()
        # reporttype = self.toolwidgetmain .comboBox_type.currentText()

        # print(self.confData.keys())

        reporttype = self.filemanager.getCurrentText()
        #tabletypepath = self.filemanager.getCurrentPath()

        # selectedzonegeoitems = self.choosertreewidget.treewidget.selectedItems()
        # ids = [int(item.text(0)) for item in selectedzonegeoitems]
        # pdids = self.choosertreewidget.ids
        # pks = [pdids.loc[pdids['id'] == id]['pk'].values[0] for id in ids]
        pks = self.choosertreewidget.getSelectedPks()

        self.reporttool.runReport(destinationfile=pdffile, 
                                    reportconffilename=reporttype, 
                                    pkzonegeos=pks)
        
        """
        if reporttype[0] == self.filemanager.projectcharacter:
            createfilesdir = self.confdataproject
            reporttype = reporttype[1:]
        else:
            createfilesdir = self.confdatamain

        self.impressionpdfworker = inspect.getmodule(self).printPDFBaseWorker(dbase=self.dbase,
                                                                             windowdialog=self.windowdialog,
                                                                             parentprintPDFworker=None,
                                                                             confData=self.confData,
                                                                             pdffile=pdffile,
                                                                             reporttype=reporttype,
                                                                              templatedir=createfilesdir ,
                                                                              idlist=None)

        self.impressionpdfworker.work()
        """

    """
    def postOnActivation(self):

        self.toolwidgetmain .setEnabled(True)
        self.filemanager.reset()

        self.createconfData()

        #self.linkedtreewidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.linkedtreewidget.itemSelectionChanged.connect(self.itemChanged)


    def postInitFeatureProperties(self, feat):
        pass





    def itemChanged(self, itemplus=None, itemmoins=None):
        pass
        #print(itemplus,itemmoins )

        #print('treewdg', self.linkedtreewidget.selectedItems())
        #print([it.text(0) for it in self.linkedtreewidget.selectedItems()])

    """


class ExportRapportFileManager(AbstractFileManager):

    def __init__(self, mainwindows=None, parentwdg=None, fileext=None):
        super(ExportRapportFileManager, self).__init__(mainwindows, parentwdg, fileext)


    def new(self):

        #if not os.path.exists(self.confdataproject):
        #    os.mkdir(self.confdataproject)

        confpath, confext = self.qfiledialog.getSaveFileName(None, 'Choose the file', self.confdataproject,
                                                                'txt (*.txt)', '')

        if confpath:
            self.parentwdg.new(confpath)
            
            if False:
                if confpath:
                    conf_file = open(confpath, 'w', encoding="utf-8")
                    conftxt =   """
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

            txttofind = self.projectcharacter+ os.path.splitext(os.path.basename(confpath))[0]
            indexcombo = self.comboBox_files.findText(txttofind)
            self.comboBox_files.setCurrentIndex(indexcombo)



"""
    def createconfData(self):
       


        debug = False

        if debug: logging.getLogger("Lamia").debug('started')

        self.confData = {}
        # self.toolwidgetmain .comboBox_type.clear()



        for workdir in [self.confdatamain, self.confdataproject ]:
            for filename in glob.glob(os.path.join(workdir, '*.txt')):
                basename = os.path.basename(filename).split('.')[0]
                if debug: logging.getLogger("Lamia").debug('basename %s',basename )
                self.confData[basename] = {}
                if sys.version_info.major == 2:
                    filetoread = open(filename, 'r')
                elif sys.version_info.major == 3:
                    filetoread = open(filename, 'r',encoding="utf-8")
                compt = 0
                for line in filetoread:
                    if line[0:3] == '###':  # new field
                        actualdictkey = line[3:].strip()
                        if actualdictkey in ['atlaslayersql','atlaslayerid' ,'atlaslayerstyle','ordering']:
                            self.confData[basename][actualdictkey] = ''
                        else:
                            self.confData[basename][actualdictkey] = {}
                    elif line[0:1] == '#':
                        continue
                    elif line.strip() == '' :
                        continue
                    else:
                        if actualdictkey == 'atlaslayersql':
                            self.confData[basename][actualdictkey] += line.strip() + ' '
                        elif actualdictkey in ['atlaslayerid','atlaslayerstyle','ordering'] :
                            self.confData[basename][actualdictkey] = line.strip()
                        elif actualdictkey in ['atlasdrivemap','generalmap']:
                            speclist = line.split(';')
                            self.confData[basename][actualdictkey][speclist[0].strip()] = {}
                            if speclist[1].strip() != '':
                                minscale = int(speclist[1].strip())
                            else:
                                minscale = None

                            typescale = speclist[2].strip()
                            if typescale != '':
                                if False:    #qgis 2 version
                                    toexec = "typescale = qgis.core.QgsComposerMap." + typescale
                                    exec(toexec)
                                else:
                                    typescale = eval("qgis.core.QgsLayoutItemMap." + typescale)

                            self.confData[basename][actualdictkey][speclist[0].strip()]['minscale'] = minscale
                            self.confData[basename][actualdictkey][speclist[0].strip()]['typescale'] = typescale
                            self.confData[basename][actualdictkey][speclist[0].strip()]['layers'] = eval(speclist[3].strip())
                        elif actualdictkey in ['spatial']:
                            self.confData[basename][actualdictkey] = eval(line.strip())
                        elif actualdictkey in ['childprint']:
                            speclist = line.split(';')
                            self.confData[basename][actualdictkey]['confname'] = speclist[0].strip()
                            self.confData[basename][actualdictkey]['linkcolumn'] = speclist[1].strip()
                            self.confData[basename][actualdictkey]['optionsql'] = speclist[2].strip()
                        elif actualdictkey in ['images']:
                            speclist = line.split(';')
                            self.confData[basename][actualdictkey][speclist[0].strip()] = speclist[1].strip()

                filetoread.close()

                if False and self.toolwidgetmain  is not None:
                    if len(basename.split('_')) == 1:
                        if workdir == self.confdataproject:
                            basename = '*' + basename
                        self.toolwidgetmain .comboBox_type.addItems([basename])

        if False:
            # Update dialog
            if self.toolwidgetmain  is not None:
                self.toolwidgetmain .comboBox_type.clear()
                for typerapport in self.confData.keys():
                    if len(typerapport.split('_')) == 1:
                        self.toolwidgetmain .comboBox_type.addItems([typerapport])

        if debug: logging.getLogger("Lamia").debug('confData : %s',self.confData )




    def launchRapport(self):
        pdffile = self.toolwidgetmain .lineEdit_nom.text()
        # reporttype = self.toolwidgetmain .comboBox_type.currentText()

        # print(self.confData.keys())

        reporttype = self.filemanager.getCurrentText()

        if reporttype[0] == self.filemanager.projectcharacter:
            createfilesdir = self.confdataproject
            reporttype = reporttype[1:]
        else:
            createfilesdir = self.confdatamain

        self.impressionpdfworker = inspect.getmodule(self).printPDFBaseWorker(dbase=self.dbase,
                                                                             windowdialog=self.windowdialog,
                                                                             parentprintPDFworker=None,
                                                                             confData=self.confData,
                                                                             pdffile=pdffile,
                                                                             reporttype=reporttype,
                                                                              templatedir=createfilesdir ,
                                                                              idlist=None)

        self.impressionpdfworker.work()

"""



class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        # self.setupUi(self)
        uipath = os.path.join(os.path.dirname(__file__), 'Lamia_rapport_tool.ui')
        uic.loadUi(uipath, self)




