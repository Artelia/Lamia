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

# qgis pyqt import
from qgis.PyQt import QtGui, uic, QtCore
from unicodedata import normalize
from qgis.PyQt.QtCore import pyqtSignal, QCoreApplication
try:
    from qgis.PyQt.QtGui import (QDockWidget, QMainWindow, QFileDialog, QLabel, QInputDialog,
                                 QComboBox,QTableWidgetItem,QProgressBar,QApplication,QToolBar,
                                 QPushButton,QToolButton,QWidget, QMessageBox, QAction)
except ImportError:
    from qgis.PyQt.QtWidgets import (QDockWidget, QMainWindow, QFileDialog, QLabel, QInputDialog,
                                     QComboBox,QTableWidgetItem, QProgressBar,QApplication,QToolBar,
                                     QPushButton,QToolButton,QWidget, QMessageBox, QAction)


# other libs import
import os
import qgis
import shutil
import datetime
import sys
import logging
import math
import platform
import subprocess

debugtime = False


import glob, importlib, inspect
from pprint import pprint

from Lamia.dbasemanager.dbaseparserfactory import DBaseParserFactory

from ..ifaceabstractwidget import LamiaIFaceAbstractWidget
from ..qgsconnector.ifaceqgisconnector import QgisConnector
from ..qgscanvas.ifaceqgiscanvas import QgisCanvas

from .subdialogs.lamia_Connexion_PG import ConnexionPGDialog
from .subdialogs.lamia_ConflitHorsLigne import ConflitHorsLigne
from .subdialogs.lamia_iconsize import IconSizeDialog
from .subdialogs.lamia_newDB import newDBDialog
from .subdialogs.lamia_getDate import getDateDialog
from .subdialogs.lamia_tablefield_dialog import LamiaTableFieldDialog

from .tools.subwidgets.lamia_numpad import NumPadDialog


import Lamia, time
from Lamia.libslamia.gps.GPSutil import GpsUtil
from Lamia.maptool.mapTools import mapToolCapture, mapToolEdit


class LamiaWindowWidget(QMainWindow,LamiaIFaceAbstractWidget):
    """
    the main window widget

    ******************      self           ************************
    ***************************************************************
    *                      toolbarForm                            *
    ***************************************************************
    *           *                                                 *
    * tool      *                                                 *
    * treewidget*           tools                                 *
    *           *                                                 *
    *           *                                                 *
    *           *                                                 *
    *************                                                 *
    *           *                                                 *
    * chooser   *                                                 *
    * treewidget*                                                 *
    *           *                                                 *
    *           *                                                 *
    ***************************************************************
    ***************************************************************

    """
    closingPlugin = pyqtSignal()


 



    def __init__(self, canvas=None, dockwgt=None, parent=None):
        """
        Constructor
        :param canvas : current qgsmapcanvas
        :param parent : pyqt widget parent
        """
        #super(LamiaWindowWidget, self).__init__(parent)
        #super(LamiaWindowWidget, self).__init__(parent)
        LamiaIFaceAbstractWidget.__init__(self)
        QMainWindow.__init__(self,parent)
        debug = False

        if debug: logging.getLogger('Lamia').debug('start')

        path = os.path.join(os.path.dirname(__file__), 'ifaceqgswidget.ui')
        uic.loadUi(path, self)

        # connector and canvas
        self.connector = QgisConnector()
        self.connector.widget = self
        self.qgiscanvas = QgisCanvas()
        self.gpsutil = GpsUtil()
        self.gpsutil.hauteurperche = 2.0 

        #statusbar
        self.GPSlabel = QLabel(self.tr('GPS non connecté'))
        self.statusBar().addWidget(self.GPSlabel)
        self.GPSlabelprecision = QLabel(self.tr('Précision'))
        self.statusBar().addWidget(self.GPSlabelprecision)

        # interfacemode
        # old :self.dbase.visualmode
        self.interfacemode = None
        self.wdgclasses={}  #dict containing all tools classes (prepro / postpro)
        self.toolwidgets={} #dict containing all tools widgets (prepro / postpro)
        self.toolwidgets['desktop_loaded'] = False      #used to store desktoptools are arlready loaded 

        #behaviour var
        self.currenttoolwidget = None
        self.imagedirectory = None
        self.currentchoosertreewidget = None

        # subdialogs
        self.newDBDialog = newDBDialog()
        self.crsselector = qgis.gui.QgsProjectionSelectionDialog()
        self.qfiledlg = QFileDialog()
        self.connPGDialog = ConnexionPGDialog()

        # camera path
        if QtCore.QSettings().value("Lamia/picturepath") is not None:
            self.imagedirectory = os.path.normpath(QtCore.QSettings().value("Lamia/picturepath"))
        else:
            self.imagedirectory = None

        # ***************************************************************
        # ******************   Variables def ****************************
        # ***************************************************************
        if False:
            # current the qgsmapcanvas
            self.canvas = canvas
            # list containing the tools widget
            self.tools = []
            # list containing the menu tools classes
            self.menutools = []
            # the pick maptool
            # self.pointEmitter = None
            self.pointEmitter = qgis.gui.QgsMapToolEmitPoint(self.canvas)
            # The DBase parser
            self.dbase = None
            self.importexportdbase = None
            self.recentsdbase = []
            # The GPS util
            self.gpsutil = GpsUtil()
            self.gpsutil.hauteurperche = 2.0    #defaultvalue
            # The main qfiledialog
            self.qfiledlg = QFileDialog()
            # the working date dialog
            self.dateDialog = getDateDialog(self)
            # the new db dialog
            self.newDBDialog = newDBDialog()
            #numpad dialog
            self.numpaddialog = NumPadDialog()
            # the postgis connection dialog
            self.connDialog = ConnexionPGDialog()
            #table/field dialog
            self.tablefielddialog = LamiaTableFieldDialog(self.dbase)
            #iconsize
            self.iconsizedialog = IconSizeDialog(self)
            # for printing reports
            #self.printrapportdialog = ImpressionRapportDialog()
            # self.exportshapefiledialog = ExportShapefileDialog()
            # self.importobjetdialog =ImportObjetDialog()
            #qgis legend node
            self.qgislegendnode = None

            #ui classes
            self.uifields = []
            self.uidesktop = []
            self.uipostpro = []
            self.menuclasses = []
            self.desktopuiloaded = False


            if sys.version_info.major == 2:
                self.crsselector = qgis.gui.QgsGenericProjectionSelector()
            else:
                self.crsselector = qgis.gui.QgsProjectionSelectionDialog()
            self.dockwgt = dockwgt

            # the qgis editing maptool
            self.cadwdg = qgis.gui.QgsAdvancedDigitizingDockWidget(self.canvas)
            if sys.version_info.major == 2:
                self.mtoolpoint = mapToolCapture(self.canvas, self.cadwdg,
                                                qgis.gui.QgsMapToolAdvancedDigitizing.CapturePoint)
                self.mtoolline = mapToolCapture(self.canvas, self.cadwdg,
                                                qgis.gui.QgsMapToolAdvancedDigitizing.CaptureLine)
                self.mtoolpolygon = mapToolCapture(self.canvas, self.cadwdg,
                                                qgis.gui.QgsMapToolAdvancedDigitizing.CapturePolygon)
            elif sys.version_info.major == 3:
                self.mtoolpoint = mapToolCapture(self.canvas, self.cadwdg,
                                                qgis.gui.QgsMapToolCapture.CapturePoint)
                self.mtoolline = mapToolCapture(self.canvas, self.cadwdg,
                                                qgis.gui.QgsMapToolCapture.CaptureLine)
                self.mtoolpolygon = mapToolCapture(self.canvas, self.cadwdg,
                                                qgis.gui.QgsMapToolCapture.CapturePolygon)

            self.mtooledit = mapToolEdit(canvas=self.canvas)
            self.editfeatureworking = False
            self.editfeaturelayer = None

            self.currentprestationlabel = QLabel(self.tr(u'Prestation inactif'))
            self.statusBar().addWidget(self.currentprestationlabel, 1)

            self.GPSlabel = QLabel(self.tr('GPS non connecté'))
            self.statusBar().addWidget(self.GPSlabel)
            self.GPSlabelprecision = QLabel(self.tr('Précision'))
            self.statusBar().addWidget(self.GPSlabelprecision)

            if debug: logging.getLogger('Lamia').debug('step1')

        if False:
            # ***************************************************************
            # ******************   Actions  ****************************
            # ***************************************************************
            self.MaintreeWidget.expandAll()
            self.MaintreeWidget.currentItemChanged.connect(self.closeEditFeature)
            self.actionModeTerrain.setChecked(True)

            # ***************************************************************
            # ******************   Signals ****************************
            # ***************************************************************


            # QT signals
            self.actionNouvelle_base.triggered.connect(self.newDbase)
            self.actionSpatialite.triggered.connect(self.loadSLDbase)
            self.actionPostgis.triggered.connect(self.loadPGDbase)
            self.actionAide.triggered.connect(self.openHelp)
            self.actionTables_et_champs.triggered.connect(self.openTableFieldDialog)
            self.menuBases_recentes.triggered.connect(self.openFileFromMenu)
            # self.actionExporter_base.triggered.connect(self.exportBase)
            # self.actionImprimer_rapport.triggered.connect(self.printRapport)
            # self.actionExport_shapefile.triggered.connect(self.exportShapefile)
            #self.actionImport.triggered.connect(self.importObjet)
            self.actionVersion.triggered.connect(self.setVersion)
            #self.actionExporter_vers_SIRS_Digues.triggered.connect(export_sirs)
            #self.actionImporter_depuis_SIRS_Digues.triggered.connect(import_sirs)



            """
            if self.dbase.dbasetype == 'postgis':
                self.actionMode_hors_ligne_Reconnexion.setEnabled(True)
            else:
                #self.actionMode_hors_ligne_Reconnexion.setEnabled(True)
                self.actionMode_hors_ligne_Reconnexion.setEnabled(True)
            self.actionMode_hors_ligne_Reconnexion.triggered.connect(self.modeHorsLigne)
            """

            #self.pushButton_zoomFeature.clicked.connect(self.zoomToFeature)
            self.pushButton_selectfeat.clicked.connect(self.selectFeature)
            #self.toolButton_edit.clicked.connect(self.editFeature)
            self.action_Repertoire_photo.triggered.connect(self.setImageDir)
            #self.actionDate_de_travail.triggered.connect(self.setWorkingDate)
            self.toolButton_date.clicked.connect(self.setWorkingDate)
            if True:
                self.actionModeExpert.triggered.connect(self.setVisualMode)
                self.actionTTC.triggered.connect(self.setVisualMode)
                self.actionModeTerrain.triggered.connect(self.setVisualMode)
                self.actionPosttraitement.triggered.connect(self.setVisualMode)

            self.actionReinitialier_prestation_courante.triggered.connect(self.reinitCurrentPrestation)
            self.actionHauteur_de_perche_GPS.triggered.connect(self.setHauteurPerche)
            self.action_taille_icone.triggered.connect(self.setLamiaIconSize)
            self.action_GPSConnection.triggered.connect(self.connectToGPS)
            # other
            self.gpsutil.GPSConnected.connect(self.GPSconnected)
            # init
            self._readRecentDBase()
            self._updateRecentDBaseMenu()
            self.splitter_2.setSizes([80, 200])

        # ************** Init actions ******************
        self._connectMenuAndOthers()
        self._connectToolBar()
        self._readRecentDBase()
        self._updateRecentDBaseMenu()
        
        self.splitter_2.setSizes([80, 200])
        if debug: logging.getLogger('Lamia').debug('end')



    # ***********************************************************
    # **************** File menu actions ***********************
    # ***********************************************************

    def ____________________________________FileMenuActions(self):
        pass

    def newDBase(self):
        """
        pass
        """
        # dialog with dbtype, worktype, vartype  chooser
        self.newDBDialog.comboBox_type.currentIndexChanged.emit(0)
        self.newDBDialog.exec_()
        dbtype, worktype, vartype = self.newDBDialog.dialogIsFinished()
        if dbtype is None :
            return
        
        # dialog for crs selector
        self.crsselector.exec_()
        crs = self.crsselector.crs().authid()
        crsnumber = int(crs.split(':')[1])

        # dialog for ressources directory
        if dbtype == 'postgis':
            resdir = self.qfiledlg.getExistingDirectory(self, "Selectionner le repertoire des ressources")
            if resdir:
                resdir = str(resdir)
            else:
                return
        else:
            resdir = None

        # dialogs finished - reinit base TODO
        """
        self.dbase.reInitDBase()
        reset dbase
        self.createDBase() 
        """

        # dialog for dbase spec
        if dbtype == 'spatialite':
            spatialitefile, fileext = self.qfiledlg.getSaveFileName(self, 'Lamia nouveau', '', '*.sqlite')
            # self.createDBase() TODO
            if spatialitefile:
                if self.connector:
                    self.connector.showNormalMessage(' Creation de la base de donnees...')

                self.dbase = DBaseParserFactory('spatialite').getDbaseParser()
                self.dbase.createDBase(crs=crsnumber, 
                                        worktype=worktype, 
                                        dbaseressourcesdirectory=resdir, 
                                        variante=vartype,
                                        slfile=spatialitefile)
                self.dbase.loadDBase(slfile=spatialitefile)


        elif dbtype == 'postgis':
            self.connDialog.exec_()
            adresse, port, nom, schema, user, password = self.connDialog.dialogIsFinished()
            if adresse is not None and port is not None and nom is not None and user is not None and password is not None:
                # self.createDBase()
                databaseexists, schemaexists = self.dbase.checkIfPGShcemaExists(host=adresse, dbname=nom, schema=schema,
                                                                                user=user, password=password)
                if  schemaexists :
                    print('schema existe deja - choisir un autre schema')
                else:
                    if self.connector:
                        self.connector.showNormalMessage('Creation de la base de donnees...')
                    # reset dbase
                    #self.createDBase()
                    # QApplication.processEvents()

                    #resdir = self.createRessourcesDir(dbtype, resdir,vardir=vardir)

                    #self.dbase.createDbase(crs=crsnumber, worktype=worktype, dbasetype='postgis', dbname=nom, schema=schema,
                    #                       user=user, host=adresse, password=password, dbaseressourcesdirectory=resdir,
                    #                       port=port,variante=vartype)
                    self.dbase = DBaseParserFactory('postgis').getDbaseParser()
                    self.dbase.createDBase(crs=crsnumber, 
                                            worktype=worktype, 
                                            dbaseressourcesdirectory=resdir, 
                                            variante=vartype,
                                            host=adresse, 
                                            port=port, 
                                            dbname=nom, 
                                            schema=schema, 
                                            user=user,  
                                            password=password)
                    self.dbase.loadDBase(host=adresse, 
                                            port=port, 
                                            dbname=nom, 
                                            schema=schema, 
                                            user=user,  
                                            password=password)

    def loadDBase(self, **kwargs):
        """[summary]
        kwargs contains either var:
        - dbtype : 'Postgis' or 'Spatialite'
        - slfile (optionnal)
        - host port dbname schema userpassword (optionnal)
        """

        if 'dbtype' not in kwargs.keys():   #case come from qt event
            kwargs['dbtype'] = self.sender().objectName()[6:]
        success = self._loadDBaseParser(**kwargs)
        if not success:
            return
        
        self._loadVectorLayers()
        self._loadStyles()
        self._AddDbaseInRecentsDBase(self.dbase)
        self.loadToolsClasses()
        self.loadToolsWidgets()
        self.setVisualMode(visualmode=0)
        self.qgiscanvas.updateWorkingDate(dbaseparser=self.dbase)


    def pullDBase(self):    #for offline mode
        pass

    def pushDBase(self):    #for offline mode
        pass

    def addDBase(self):
        pass

    def _loadDBaseParser(self, **kwargs):
        success = False
        if 'dbtype' in kwargs.keys():
            dbtype = kwargs.get('dbtype')
            if dbtype == 'Postgis':
                neededkwargs = set(['host', 'port', 'dbname', 'schema', 'user', 'password'])
                if (not neededkwargs.issubset(set(list(kwargs.keys())))   ):
                    self.connDialog = ConnexionPGDialog()
                    self.connDialog.exec_()
                    host, port, dbname, schema, user, password = self.connDialog.dialogIsFinished()
                else:
                    host, port, dbname, schema, user, password = kwargs.get('host'), kwargs.get('port'),kwargs.get('dbname'), kwargs.get('schema'), kwargs.get('user'), kwargs.get('password')
                
                if (host is not None and port is not None and dbname is not None 
                        and user is not None and password is not None):
                    # reset dbase
                    #self.createDBase()
                    self.dbase = DBaseParserFactory('postgis').getDbaseParser()
                    self.dbase.loadDBase(host=host, port=port, dbname=dbname, schema=schema, 
                                        user=user, password=password)

                    #self.dbase.loadQgisVectorLayers(file=None, dbasetype='postgis', host=adresse, port=port, dbname=nom,
                    #                                schema=schema, user=user, password=password)
                    success = True
            elif dbtype == 'Spatialite':
                if not 'slfile' in kwargs.keys():
                    slfile , extension= self.qfiledlg.getOpenFileName(None, 'Choose the file', '',
                                                                            'Spatialite (*.sqlite)', '')
                else:
                    slfile = kwargs.get('slfile')

                if slfile:
                    # reset dbase
                    #self.reinitDBase()
                    # reset dbase
                    #self.createDBase()
                    self.dbase = DBaseParserFactory('spatialite').getDbaseParser()
                    self.dbase.loadDBase(slfile=slfile)
                    #self.dbase.loadQgisVectorLayers(file)
                    success = True

            else:
                pass
        return success

    def _loadVectorLayers(self):
        self.qgiscanvas.createLayers(self.dbase)
        self.qgiscanvas.loadLayersInCanvas(self.dbase)

    def _updateRecentDBaseMenu(self):
        try:
            self.menuBases_recentes.triggered.disconnect(self._openFileFromMenu)
        except Exception as e:
            print(e)
        self.menuBases_recentes.clear()
        for telem in self.recentsdbase:
            self.menuBases_recentes.addAction(telem)
        self.menuBases_recentes.triggered.connect(self._openFileFromMenu)

    def _readRecentDBase(self):
        """
        Lit le fichier des bases de données recentes et rempli le  menu//Fichier//base de données recentes
        """
        pathrecentproject = os.path.join(os.path.dirname(Lamia.__file__),  'config', 'recentprojects.txt')
        try:
            file = open(pathrecentproject, "r")
            lines = file.readlines()
            file.close()
            self.recentsdbase = []
            for line in lines:
                if os.path.isfile(line.strip()):
                    self.recentsdbase.append(line.strip())
                elif len(line.split(';')) == 3:
                    self.recentsdbase.append(line.strip())
        except :
            pass
        # self.recentDBaseChanged.emit()
        self._updateRecentDBaseMenu()

    def _AddDbaseInRecentsDBase(self, dbaseparser):                   
        """
        Methode appelée lors du chargement d'une BD lamia
        Ajoute le chemin dans le fichier chargé dans Menu//Fichier//base de données recentes
        """
        #if self.dbase.dbasetype == 'spatialite':
        if dbaseparser.__class__.__name__ == 'SpatialiteDBaseParser':
            spatialitefile = dbaseparser.spatialitefile
            if spatialitefile in self.recentsdbase:
                index = self.recentsdbase.index(spatialitefile)
                del self.recentsdbase[index]
            self.recentsdbase.insert(0, spatialitefile)
            self._saveRecentDBase()
            # self.recentDBaseChanged.emit()
            self._updateRecentDBaseMenu()
        #elif self.dbase.dbasetype == 'postgis':
        elif dbaseparser.__class__.__name__ == 'PostGisDBaseParser':
            #name = dbname + '.' +schema  + '@' + host + ':' + str(port) + ';' + user + ';' + password
            name = dbaseparser.pgdb + '.' + dbaseparser.pgschema  
            name += '@' + str(dbaseparser.pghost) + ':' + str(dbaseparser.pgport) + ';'
            name += dbaseparser.pguser + ';' + dbaseparser.pgpassword
            if name in self.recentsdbase:
                index = self.recentsdbase.index(name)
                del self.recentsdbase[index]
            self.recentsdbase.insert(0, name)
            self._saveRecentDBase()
            # self.recentDBaseChanged.emit()
            self._updateRecentDBaseMenu()

    def _saveRecentDBase(self):
        """
        Sauve le path de la BD lamia en cours d'utilisation dans le ficier employé dans
        menu//Fichier//base de données recentes
        """
        pathrecentproject = os.path.join(os.path.dirname(Lamia.__file__), 'config', 'recentprojects.txt')
        file = open(pathrecentproject, "w")
        for i, path in enumerate(self.recentsdbase):
            if i > 10:
                break
            if not path == '':
                file.write(path + '\n')
        file.close()
        self._updateRecentDBaseMenu()


    def _openFileFromMenu(self, action):
        """
        pass
        """
        filetoopen = action.text()
        if len(filetoopen.split(';')) == 1:
            #self.createDBase()
            #self.dbase.loadQgisVectorLayers(filetoopen)
            self.loadDBase(dbtype='Spatialite', slfile=filetoopen)
        else:
            # self.createDBase()
            db, user, password = filetoopen.split(';')
            nom, schema = db.split('@')[0].split('.')
            adresse, port = db.split('@')[1].split(':')
            #self.dbase.loadQgisVectorLayers(dbasetype='postgis', host=adresse, port=int(port), dbname=nom,
            #                                schema=schema, user=user, password=password)
            self.loadDBase(dbtype='Postgis',host=adresse, port=int(port), dbname=nom, schema=schema, user=user, password=password)


    def _loadStyles(self):
        try:
            self.comboBox_style.currentIndexChanged.disconnect(self.comboStyleChanged)
        except:
            pass
        self.comboBox_style.clear()
        stylepath = os.path.join(os.path.dirname(Lamia.__file__),'DBASE', 'style', self.dbase.worktype)
        styledirs = [x[1] for x in os.walk(stylepath) if len(x[1])>0]
        if len(styledirs)>0:
            styledirs = styledirs[0]
            self.comboBox_style.addItems(styledirs)
            self.comboBox_style.currentIndexChanged.connect(self.comboStyleChanged)
            self.comboBox_style.currentIndexChanged.emit(0)

    def comboStyleChanged(self,comboindex):
        """
        Listener on style combobox changed
        :param comboindex:
        :return:
        """
        styledir = self.comboBox_style.currentText()
        # stylerep = os.path.join(os.path.dirname(Lamia.__file__), 'DBASE', 'style', self.dbase.worktype, styledir )
        self.qgiscanvas.applyStyle(self.dbase.worktype, styledir)


    # ***********************************************************
    # **************** Interface mode actions ***********************
    # ***********************************************************
    def ____________________________________InterfacemodeActions(self):
        pass
    
    
    #def setVisualMode(self, tempres=None, reset=False):
    def setVisualMode(self, **kwargs):
        """
        pass
        """
        visualmodedict = {0: 'actionModeTerrain',
                           1: 'actionTTC',
                            2: 'actionModeExpert',
                            4: 'actionPosttraitement'}

        reset = kwargs.get('reset', None)
        visualmode = kwargs.get('visualmode', None)

        if isinstance(self.sender(), QAction):
            actionname = self.sender().objectName()
        else:
            if visualmode is not None:
                actionname = visualmodedict[visualmode]
            else:
                return
        
        qactionchild = self.menuMode.actions()
        for qact in qactionchild:
            qact.setChecked(False)
            if not reset and qact.objectName() == actionname:
                qact.setChecked(True)

        if actionname == visualmodedict[0]:
            self.interfacemode = 0
        elif actionname == visualmodedict[1]:
            self.interfacemode = 1
            if not self.toolwidgets['desktop_loaded'] :
                # self.loadUiDesktop()
                self.loadToolsWidgets(fullloading=True)
        elif actionname == visualmodedict[2]:
            self.interfacemode = 2
        elif actionname == visualmodedict[4]:
            self.interfacemode = 4
            if not self.toolwidgets['desktop_loaded'] :
                #self.loadUiDesktop()
                self.loadToolsWidgets(fullloading=True)

        self._applyVisualMode()
 


    def _applyVisualMode(self, actiontext=None):
        for tooltype in self.toolwidgets.keys():
            if tooltype == 'desktop_loaded':
                continue

            for toolname in self.toolwidgets[tooltype].keys():
                toowdg = self.toolwidgets[tooltype][toolname]
                if isinstance(toowdg, list):
                    for wdg in toowdg:
                        #tool dep
                        if hasattr(wdg, 'changeInterfaceMode'):
                            wdg.changeInterfaceMode()
                        else:
                            wdg.changePropertiesWidget()
                else:
                        #tool dep
                        if hasattr(wdg, 'changeInterfaceMode'):
                            wdg.changeInterfaceMode()
                        else:
                            wdg.changePropertiesWidget()
        """
        if self.dbase.dbasetables is not None:
            for tool in self.tools:
                tool.changePropertiesWidget(actiontext)

            for tablename in self.dbase.dbasetables.keys():
                if 'widget' in self.dbase.dbasetables[tablename].keys():
                    if isinstance(self.dbase.dbasetables[tablename]['widget'], list):
                        for wdg in self.dbase.dbasetables[tablename]['widget']:
                            wdg.changePropertiesWidget(actiontext)
                    else:
                        self.dbase.dbasetables[tablename]['widget'].changePropertiesWidget(actiontext)
        """

    def loadToolsClasses(self):
        """
        Load layers and put them in a legend group in qgis
        Load all modules (prepro, postpro and menu)
        Show field ui

        :return:
        """

        debug = False
        if debug: logging.getLogger('Lamia').debug('start')

        tooltypestoload = ['toolprepro', 'toolpostpro']
        for tooltypetoload in tooltypestoload:
            self.wdgclasses[tooltypetoload]={}

            path = os.path.join(os.path.dirname(__file__), 'tools', tooltypetoload, self.dbase.worktype.lower())
            modules = glob.glob(path + "/*.py")
            __all__ = [os.path.basename(f)[:-3] for f in modules if os.path.isfile(f)]
            interfacefielduisup=[]
            for x in __all__:
                if debug: logging.getLogger('Lamia_unittest').debug('x %s', x)
                parentmodulename = '.'.join(__name__.split('.')[:-1])
                modulename = parentmodulename + '.tools.' + tooltypetoload + '.' + self.dbase.worktype.lower()
                exec('import ' + modulename)
                moduletemp = importlib.import_module('.' + str(x), modulename )

                for name, obj in inspect.getmembers(moduletemp, inspect.isclass):
                    if moduletemp.__name__ == obj.__module__:
                        if tooltypetoload == 'toolpostpro' and hasattr(obj,'TOOLNAME'):
                            self.wdgclasses[tooltypetoload][obj.TOOLNAME] = obj
                        elif tooltypetoload == 'toolprepro' and  hasattr(obj,'dbasetablename') :   #tool dep
                            self.wdgclasses[tooltypetoload][obj.dbasetablename] = obj
                        elif (tooltypetoload == 'toolprepro' and hasattr(obj,'DBASETABLENAME')
                                and hasattr(obj,'tooltreewidgetSUBCAT') and obj.tooltreewidgetSUBCAT is not None) :
                            self.wdgclasses[tooltypetoload][obj.tooltreewidgetSUBCAT] = obj

        if debug: logging.getLogger('Lamia_unittest').debug('x %s', str(self.wdgclasses))


    def loadToolsWidgets(self, fullloading=False):

        debug = False
        typeswdg = ['toolprepro', 'toolpostpro']

        toopreprodict = self.wdgclasses['toolprepro']
        lenprogresspartialloading = len([name for name in toopreprodict.keys() 
                                    if hasattr(toopreprodict[name], 'LOADFIRST') 
                                    and toopreprodict[name].LOADFIRST])
        lenprogressfullloading = len(self.wdgclasses['toolprepro']) + len(self.wdgclasses['toolpostpro'])

        if fullloading:
            self.connector.createProgressBar('Loading widgets...', lenprogressfullloading - lenprogresspartialloading )
        else:
            self.connector.createProgressBar('Loading widgets...', lenprogresspartialloading)

        
        i = 0
        for typewdg in typeswdg:
            if not fullloading and typewdg == 'toolpostpro':
                continue
            if not typewdg in self.toolwidgets.keys():
                self.toolwidgets[typewdg] = {}
            for toolname in self.wdgclasses[typewdg].keys():
                if toolname in self.toolwidgets[typewdg].keys():
                    continue
                if debug: logging.getLogger("Lamia_unittest").debug('loading %s',toolname )
                self.toolwidgets[typewdg][toolname] = []
                toolwdglist = self.toolwidgets[typewdg][toolname]
                toolwdgcls = self.wdgclasses[typewdg][toolname]
                try:
                    if hasattr(self.wdgclasses[typewdg][toolname],'DBASETABLENAME') and not fullloading:
                        toolwdglist.append( toolwdgcls(dbaseparser = self.dbase,
                                                        mainifacewidget = self,
                                                        choosertreewidget = self.ElemtreeWidget,
                                                        parentwidget = None) )
                    elif hasattr(self.wdgclasses[typewdg][toolname],'LOADFIRST') and not fullloading:
                        toolwdglist.append( toolwdgcls(dbase = self.dbase,
                                                        dialog = self,
                                                        linkedtreewidget = self.ElemtreeWidget,
                                                        gpsutil = self.gpsutil) )
                    else:       # tool dep
                        toolwdglist.append( toolwdgcls(dbase = self.dbase,
                                                        dialog = self,
                                                        linkedtreewidget = self.ElemtreeWidget,
                                                        gpsutil = self.gpsutil) )
                except TypeError as e:
                    print(toolname, e)
                    #raise TypeError
                i += 1
                self.connector.updateProgressBar(i)
        
        if not self.toolwidgets['desktop_loaded'] and fullloading:
            self.toolwidgets['desktop_loaded'] = True
        self.connector.closeProgressBar()


        # init progress bar
        """
        if self.dbase.qgsiface is not None:
            progressMessageBar = self.dbase.qgsiface.messageBar().createMessage("Loading widget...")
            progress = QProgressBar()
            progress.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
            progressMessageBar.layout().addWidget(progress)
            if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                self.dbase.qgsiface.messageBar().pushWidget(progressMessageBar, self.dbase.qgsiface.messageBar().INFO)
            else:
                self.dbase.qgsiface.messageBar().pushWidget(progressMessageBar, qgis.core.Qgis.Info)
            lenuifields = len(self.uifields)
            progress.setMaximum(lenuifields)
        else:
            progress = None
        """
        """
        #load ui fields
        i = 0
        for uifield in self.uifields:
            if debugtime: logger.debug(' start %s %.3f', uifield.dbasetablename, self.dbase.getTimeNow() - timestart)
            dbasename = uifield.dbasetablename
            self.dbase.dbasetables[dbasename]['widget'].append( uifield(dbase = self.dbase,
                                                                     dialog = self,
                                                                     linkedtreewidget = self.ElemtreeWidget,
                                                                     gpsutil = self.gpsutil) )

            if debugtime: logger.debug(' end %s %.3f', uifield.dbasetablename, self.dbase.getTimeNow()  - timestart)
            i += 1
            self.setLoadingProgressBar(progress, i)

        if progress is not None: self.dbase.qgsiface.messageBar().clearWidgets()
        """

    def loadUiDesktop(self, fullloading=False):

        debug = False

        # init progress bar
        lenuifields = len(self.uidesktop)
        lenuipostpro = len(self.uipostpro)
        lenmenutool = len(self.menuclasses)
        self.connector.createProgressBar('Loading widgets...',lenuifields + lenuipostpro + lenmenutool )
        if self.dbase.qgsiface is not None:
            progressMessageBar = self.dbase.qgsiface.messageBar().createMessage("Loading widget...")
            progress = QProgressBar()
            progress.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
            progressMessageBar.layout().addWidget(progress)
            if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                self.dbase.qgsiface.messageBar().pushWidget(progressMessageBar, self.dbase.qgsiface.messageBar().INFO)
            else:
                self.dbase.qgsiface.messageBar().pushWidget(progressMessageBar, qgis.core.Qgis.Info)

        else:
            progress = None

        # load menu ui
        i = 0
        for menuclasse in self.menuclasses:
            self.menutools.append(menuclasse(dbase=self.dbase, windowdialog=self))
            i += 1
            self.setLoadingProgressBar(progress, i)
            if debug : logger.debug(' loading %s', str(menuclasse))

        # load postpro ui
        for uidpostpr in self.uipostpro:
            # print('uidpostpr', uidpostpr)
            strtoexec = ('self.' + uidpostpr.__name__.lower() + " = uidpostpr(dbase = self.dbase, dialog = self,linkedtreewidget = self.ElemtreeWidget, gpsutil = self.gpsutil)")
            # print(strtoexec)
            exec(strtoexec)
            # print('test', eval('self.' + uidpostpr.__name__.lower()))
            strtoexec = 'self.tools.append(' + 'self.' + uidpostpr.__name__.lower() + ')'
            # print(strtoexec)
            exec(strtoexec)

            if debug: logger.debug(' loading %s', str(uidpostpr.__name__))
            # print('ok')


            if False:
                self.tools.append( uidpostpr(dbase = self.dbase,
                                             dialog = self,
                                             linkedtreewidget = self.ElemtreeWidget,
                                             gpsutil = self.gpsutil)
                               )
            i += 1
            self.setLoadingProgressBar(progress, i)

        # load uidesktop ui
        for uidesktop in self.uidesktop:
            try:
                dbasename = uidesktop.dbasetablename
                self.dbase.dbasetables[dbasename]['widget'].append(uidesktop(dbase = self.dbase,
                                                                         dialog = self,
                                                                         linkedtreewidget = self.ElemtreeWidget,
                                                                         gpsutil = self.gpsutil))
                i += 1
                self.setLoadingProgressBar(progress, i)

            except AttributeError:
                pass

        if progress is not None: self.dbase.qgsiface.messageBar().clearWidgets()
        self.desktopuiloaded = True

    #*************************************************************
    # Settings menu
    #*************************************************************

    def ____________________________________SettingsMenuActions(self):
        pass

    def connectToGPS(self):
        success = self.gpsutil.connectToGPS()
        """
        if False:
            if not success:
                print('gps connection failed')
                self.GPSConnected.emit(False)
            else:
                self.GPSConnected.emit(True)
        """

    def GPSconnected(self,success):
        if success:
            self.GPSlabel.setStyleSheet("QLabel { background-color : rgb(85, 255, 0);  }")  #vert
            self.GPSlabel.setText(u'GPS connecté')
            self.GPSlabelprecision.setStyleSheet("QLabel { background-color : red;  }")
            self.GPSlabelprecision.setText(u'Précision : erreur')
            self.gpsutil.gstsentence.connect(self.displayGPSPrecision)
        else:
            self.GPSlabel.setStyleSheet("QLabel { background-color : rgba(0, 0, 0, 0);  }")
            self.GPSlabel.setText(u'GPS non connecté')
            self.GPSlabelprecision.setStyleSheet("QLabel { background-color : rgba(0, 0, 0, 0);  }")
            self.GPSlabelprecision.setText(u'Précision : Off')
            try:
                self.gpsutil.gstsentence.disconnect(self.displayGPSPrecision)
            except:
                pass

    def displayGPSPrecision(self, gpsdict):
        xprecision = gpsdict['xprecision']
        yprecision = gpsdict['yprecision']
        zprecision = gpsdict['zprecision']

        try:
            totalprecision = round(math.sqrt(xprecision**2 + yprecision**2 + zprecision**2),2)
            if totalprecision < 0.1:
                self.GPSlabelprecision.setStyleSheet("QLabel { background-color : rgb(85, 255, 0);  }") #vert
            elif totalprecision < 0.4:
                self.GPSlabelprecision.setStyleSheet("QLabel { background-color : yellow;  }")
            elif totalprecision < 1.5:
                self.GPSlabelprecision.setStyleSheet("QLabel { background-color : rgb(255, 170, 0);  }")
            else:
                self.GPSlabelprecision.setStyleSheet("QLabel { background-color : red;  }")
            self.GPSlabelprecision.setText(u'Précision : ' + str(totalprecision) + ' m')

        except:
            self.GPSlabelprecision.setStyleSheet("QLabel { background-color : red;  }")
            self.GPSlabelprecision.setText(u'Précision : erreur')

    def setHauteurPerche(self):
        num, ok = QInputDialog.getDouble(self,
                                         "Hauteur de perche",
                                         "Rentrer la hauteur de perche GPS",
                                         self.gpsutil.hauteurperche,
                                         decimals=2)
        if ok:
            # self.dbase.hauteurperche = num
            self.gpsutil.hauteurperche = num

    def setImageDir(self):
        file = self.qfiledlg.getExistingDirectory(self, "Select Directory",self.dbase.imagedirectory, QFileDialog.ShowDirsOnly)
        if file:
            self.imagedirectory = file
            QtCore.QSettings().setValue("Lamia/picturepath", file)

    #*************************************************************
    # About menu
    #*************************************************************

    def ____________________________________AboutMenuActions(self):
        pass

    def openHelp(self):
        path = os.path.join(os.path.dirname(Lamia.__file__),'doc_html','index.html')
        if platform.system() == 'Linux':
            r = subprocess.call(('xdg-open', path))
        elif platform.system() == 'Windows':
            os.startfile(path)


    #*************************************************************
    # toolbar
    #*************************************************************

    def ____________________________________ToolBarActions(self):
        pass

    def _connectToolBar(self):
        self.actiontoolbarnew.triggered.connect(self.toolbarNew)
        self.actiontoolbarundo.triggered.connect(self.toolbarUndo)
        self.actiontoolbardelete.triggered.connect(self.toolbarDelete)
        self.actiontoolbarsave.triggered.connect(self.toolbarSave)

        self.actiontoobargeomnewpoint.triggered.connect(self.toolbarGeom)
        self.actiontoobargeomnewline.triggered.connect(self.toolbarGeom)
        self.actiontoobargeomnewpolygon.triggered.connect(self.toolbarGeom)
        self.actiontoobargeomaddpoint.triggered.connect(self.toolbarGeom)
        self.actiontoobargeomaddGPSpoint.triggered.connect(self.toolbarGeomAddGPS)



    def toolbarNew(self):
        logging.getLogger("Lamia_unittest").info('called')
        if self.currenttoolwidget and hasattr(self.currenttoolwidget,'toolbarNew'):
            self.currenttoolwidget.toolbarNew()
        if self.currentchoosertreewidget:
            self.currentchoosertreewidget.toolbarNew()

    def toolbarUndo(self):
        logging.getLogger("Lamia_unittest").info('called')
        if self.currenttoolwidget and hasattr(self.currenttoolwidget,'toolbarUndo'):
            self.currenttoolwidget.toolbarUndo()
        if self.currentchoosertreewidget:
            self.currentchoosertreewidget.toolbarUndo()

    def toolbarDelete(self):
        logging.getLogger("Lamia_unittest").info('called')
        if self.currenttoolwidget and hasattr(self.currenttoolwidget,'toolbarDelete'):
            self.currenttoolwidget.toolbarDelete()
        if self.currentchoosertreewidget:
            self.currentchoosertreewidget.toolbarDelete()

    def toolbarSave(self):
        logging.getLogger("Lamia_unittest").info('called')
        if self.currenttoolwidget and hasattr(self.currenttoolwidget,'toolbarSave'):
            self.currenttoolwidget.toolbarSave()
        if self.currentchoosertreewidget:
            self.currentchoosertreewidget.toolbarSave()


    def toolbarGeom(self):
        logging.getLogger("Lamia_unittest").info('called')
        if self.currenttoolwidget and hasattr(self.currenttoolwidget,'toolbarGeom'):
            self.currenttoolwidget.toolbarGeom()
    
    def toolbarGeomAddGPS(self):
        logging.getLogger("Lamia_unittest").info('called')
        if self.currenttoolwidget and hasattr(self.currenttoolwidget,'toolbarGeomAddGPS'):
            self.currenttoolwidget.toolbarGeomAddGPS()


    #*************************************************************
    # menu
    #*************************************************************

    def ____________________________________MenuActions(self):
        pass

    def _connectMenuAndOthers(self):
        #file menu
        self.actionNouvelle_base.triggered.connect(self.newDBase)
        self.actionSpatialite.triggered.connect(self.loadDBase)
        self.actionPostgis.triggered.connect(self.loadDBase)
        self.actionImporter_et_ajouter_la_base.triggered.connect(self.addDBase)
        self.actionImporter_et_mettre_jour_la_base.triggered.connect(self.pushDBase)
        self.actionExporter_la_base.triggered.connect(self.pullDBase)

        #visual mode menu
        self.actionModeExpert.triggered.connect(self.setVisualMode)
        self.actionTTC.triggered.connect(self.setVisualMode)
        self.actionModeTerrain.triggered.connect(self.setVisualMode)
        self.actionPosttraitement.triggered.connect(self.setVisualMode)
        #settings menu
        self.gpsutil.GPSConnected.connect(self.GPSconnected)
        self.action_Repertoire_photo.triggered.connect(self.setImageDir)
        #about menu
        self.actionAide.triggered.connect(self.openHelp)

        #others
        self.pushButton_selectfeat.clicked.connect(self.selectFeature)


    def selectFeature(self):
        pointemitter = self.qgiscanvas.pointEmitter
        try:
            pointemitter.canvasClicked.disconnect(self.selectPickedFeature)
        except TypeError:
            pass
        try:
            self.qgiscanvas.canvas.mapToolSet.disconnect(self.qgiscanvas.toolsetChanged)
        except TypeError:
            pass
        pointemitter.canvasClicked.connect(self.selectPickedFeature)
        self.qgiscanvas.canvas.mapToolSet.connect(self.qgiscanvas.toolsetChanged)
        self.qgiscanvas.canvas.setMapTool(pointemitter)



    def selectPickedFeature(self, point, tablename = None):

        debug = False
        if debug: logging.getLogger("Lamia_unittest").debug('Start %s', str(point))

        addselection = False
        modifiers = QApplication.keyboardModifiers()
        #print('modif')
        #if modifiers == QtCore.Qt.ShiftModifier:
        if modifiers == QtCore.Qt.ControlModifier:
            # print('Ctrl+Click')
            addselection = True

        # get parent
        parentwdg = self.currenttoolwidget
        while parentwdg.parentWidget is not None:
            parentwdg = parentwdg.parentWidget
        
        if not (hasattr(parentwdg, 'DBASETABLENAME') 
                and parentwdg.DBASETABLENAME is not None):
            return
        # getCurrentLayer
        tablename = parentwdg.DBASETABLENAME
        #qgslayer = self.qgiscanvas.layers[tablename]['layerqgis']
        #point2 = self.qgiscanvas.pointEmitter.toLayerCoordinates(qgslayer, point)
        nearestpk, dist = self.qgiscanvas.getNearestPk(tablename,
                                                        point,  #former point2
                                                        comefromcanvas=True)
        if nearestpk is None:   #no element in table
            return

        parentwdg.selectFeature(pk=nearestpk)
        if parentwdg.choosertreewidget is not None:
            parentwdg.choosertreewidget.selectFeature(pk=nearestpk)
        self.currenttoolwidget.widgetClicked()
        """
        if not (hasattr(self.currenttoolwidget, 'DBASETABLENAME') 
                and self.currenttoolwidget.DBASETABLENAME is not None):
            return
        # getCurrentLayer
        tablename = self.currenttoolwidget.DBASETABLENAME
        #qgslayer = self.qgiscanvas.layers[tablename]['layerqgis']
        #point2 = self.qgiscanvas.pointEmitter.toLayerCoordinates(qgslayer, point)
        nearestpk, dist = self.qgiscanvas.getNearestPk(tablename,
                                                        point,  #former point2
                                                        comefromcanvas=True)
        if nearestpk is None:   #no element in table
            return

        self.currenttoolwidget.selectFeature(pk=nearestpk)

        if self.currentchoosertreewidget is not None:
            self.currentchoosertreewidget.selectFeature(pk=nearestpk)
        """



        if False:
            pass
            """
            if self.stackedWidget_main.currentIndex() == 0  :

                wdg = self.MaintabWidget.widget(0).layout().itemAt(0).widget()
                layer = wdg.dbasetable['layerqgis']

                if debug: logging.getLogger("Lamia").debug('dabsetable %s', str(wdg.dbasetablename))

                point2 = self.pointEmitter.toLayerCoordinates(wdg.dbasetable['layerqgis'], point)

                nearestpk, dist = self.dbase.getNearestPk(wdg.dbasetable,
                                                        wdg.dbasetablename,
                                                        point2,
                                                        False)

                if debug: logging.getLogger("Lamia").debug('nearest pk %s , dist %s', str(nearestpk), str(dist))

                if nearestpk is None:   #no element in table
                    return

                if self.dbase.revisionwork:
                    feat = self.dbase.getLayerFeatureByPk(wdg.dbasetablename, nearestpk)
                    featid = feat['id_' + wdg.dbasetablename]
                    # print('sel',featid)
                else:
                    featid = nearestpk

                if wdg.linkedtreewidget is not None:
                    items = wdg.linkedtreewidget.findItems(str(featid),QtCore.Qt.MatchExactly | QtCore.Qt.MatchRecursive)
                    for item in items:
                        if item.parent() is not None and item.parent().text(0) == wdg.dbasetablename:
                            wdg.linkedtreewidget.setCurrentItem(item)
                            #wdg.linkedtreewidget.setItemSelected(item, True)
                            # print('ok')
                            break

                    # print('item', item.text(0))
                    #self.linkedtreewidget.setSelectionMode(QAbstractItemView.ExtendedSelection)


                if False:
                    itemindex = wdg.comboBox_featurelist.findText(str(featid))
                    wdg.comboBox_featurelist.setCurrentIndex(itemindex)



            elif self.stackedWidget_main.currentIndex() == 1:

                wdg = self.stackedWidget_main.widget(1).layout().itemAt(0).widget()
                if False:
                    wdg.selectPickedFeature(point)

                layer = self.dbase.dbasetables[wdg.dbasetablename]['layerqgis']

                point2 = self.pointEmitter.toLayerCoordinates(layer, point)

                nearestpk, dist = self.dbase.getNearestPk(self.dbase.dbasetables[wdg.dbasetablename],
                                                        wdg.dbasetablename,
                                                        point2,
                                                        False)

                if debug: logging.getLogger("Lamia").debug('nearest pk %s , dist %s', str(nearestpk), str(dist))

                if self.dbase.revisionwork:
                    feat = self.dbase.getLayerFeatureByPk(wdg.dbasetablename, nearestpk)
                    featid = feat['id_' + wdg.dbasetablename]
                    # print('sel',featid)
                else:
                    featid = nearestpk

                if wdg.linkedtreewidget is not None:
                    items = wdg.linkedtreewidget.findItems(str(featid), QtCore.Qt.MatchExactly | QtCore.Qt.MatchRecursive)
                    for item in items:
                        if item.parent() is not None and item.parent().text(0) == wdg.dbasetablename:
                            wdg.linkedtreewidget.setCurrentItem(item)
                            # wdg.linkedtreewidget.setItemSelected(item, True)
                            #print('ok')
                            break

                    #print('item', item.text(0))
            """


