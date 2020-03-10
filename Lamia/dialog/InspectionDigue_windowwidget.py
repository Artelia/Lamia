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
logger = logging.getLogger("Lamia")
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(module)s :: %(funcName)s :: %(message)s')
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

debugtime = False


import glob, importlib, inspect

try:
    from pyspatialite import dbapi2 as db
    from pyspatialite.dbapi2 import *
except ImportError:
    import sqlite3
    from sqlite3 import *
    print('spatialite not enabled')


# plugin import
from ..main.DBaseParser import DBaseParser
from .InspectionDigue_Connexion_PG import ConnexionPGDialog
from .InspectionDigue_ConflitHorsLigne import ConflitHorsLigne
# from .InspectionDigue_impression_rapport import ImpressionRapportDialog
# from .InspectionDigue_exportShapefile import ExportShapefileDialog
#from .InspectionDigue_Import import ImportObjetDialog
from .Lamia_numpad import NumPadDialog
from .Lamia_iconsize import IconSizeDialog

from .InspectionDigue_newDB import newDBDialog
from .InspectionDigue_getDate import getDateDialog
from .lamia_tablefield_dialog import LamiaTableFieldDialog

# from ..toolgeneral.InspectionDigue_rapport import printPDFWorker
# from ..toolgeneral.InspectionDigue_exportshp import exportShapefileWorker
# from ..toolgeneral.InspectionDigue_import import ImportObjectWorker
"""
from ..toolgeneral.SIRS_to_LAMIA.FDtL import *
from ..toolgeneral.LAMIA_to_SIRS.LtFD import *
"""


import time

from ..gps.GPSutil import GpsUtil
from ..maptool.mapTools import mapToolCapture, mapToolEdit


class InspectiondigueWindowWidget(QMainWindow):
    """
    the main window widget
    """
    closingPlugin = pyqtSignal()


    def __init__(self, canvas, dockwgt=None, parent=None):
        """
        Constructor
        :param canvas : current qgsmapcanvas
        :param parent : pyqt widget parent
        """
        super(InspectiondigueWindowWidget, self).__init__(parent)
        debug = False



        if debug: logging.getLogger('Lamia').debug('start')

        if False:
            self.setupUi(self)
        else:
            path = os.path.join(os.path.dirname(__file__), 'InspectionDigue_windowwidget_base.ui')
            uic.loadUi(path, self)

        # ***************************************************************
        # ******************   Variables def ****************************
        # ***************************************************************
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

        self.actionImporter_et_ajouter_la_base.triggered.connect(self.importDBase)
        self.actionImporter_et_mettre_jour_la_base.triggered.connect(self.importDBase)
        self.actionExporter_la_base.triggered.connect(self.exportDBase)

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
        self.updateRecentDBaseMenu()
        self.splitter_2.setSizes([80, 200])


        if debug: logging.getLogger('Lamia').debug('end')


    def createDBase(self):

        self.dbase = DBaseParser(self.canvas)

        #clear all
        self.MaintreeWidget.clear()
        self.ElemtreeWidget.clear()

        self.setVisualMode(reset=True)
        self.desktopuiloaded = False

        self.uifields = []
        self.uidesktop = []
        self.uipostpro = []
        self.menuclasses = []
        self.tools = []
        self.menutools = []

        if self.dbase.dbasetype is not None:
            if False:
                root = qgis.core.QgsProject.instance().layerTreeRoot()
                #root.addGroup('Lamia')
                if self.dbasetype == "spatialite":
                    groupname = 'Lamia_' + os.path.basename(self.spatialitefile)
                elif self.dbasetype == "postgis":
                    groupname = 'Lamia_' + self.pgschema

                lamialegendgroup =  root.findGroup(groupname)

                if lamialegendgroup is not None:
                    lamialegendgroup.removeAllChildren()

        self.cleanLayerTree()


        # DBase signals
        # self.dbase.recentDBaseChanged.connect(self.updateRecentDBaseMenu)
        self.dbase.dBaseLoaded.connect(self.DBaseLoaded)
        self.dbase.errorMessage.connect(self.errorMessage)
        self.dbase.errorquerymessage.connect(self.errorMessage)
        self.dbase.normalMessage.connect(self.normalMessage)


        self._readRecentDBase()

        #qgis signals
        if sys.version_info.major == 2:
            self.canvas.destinationCrsChanged.connect(self.dbase.updateQgsCoordinateTransformFromLayerToCanvas)
        elif sys.version_info.major == 3:
            qgis.core.QgsProject.instance().crsChanged.connect(self.dbase.updateQgsCoordinateTransformFromLayerToCanvas)


        # camera path
        if QtCore.QSettings().value("InspectionDigue/picturepath") is not None:
            self.dbase.imagedirectory = os.path.normpath(QtCore.QSettings().value("InspectionDigue/picturepath"))
        else:
            self.dbase.imagedirectory = None




    def themechanged(self, iconwidth):
        if isinstance(iconwidth, int):
            newsize = QtCore.QSize(iconwidth, iconwidth)
        elif isinstance(iconwidth, QtCore.QSize):
            newsize = iconwidth
        newsizeicon = QtCore.QSize(newsize)
        newsizeicon.scale(newsize.width() * 0.8, newsize.width() * 0.8, QtCore.Qt.KeepAspectRatio)

        butttons = self.findChildren(QPushButton)
        for button in butttons:
            # print('button', button.icon())
            if button.icon() is not None:
                button.setIconSize(newsizeicon)
                button.setBaseSize(newsize)
                button.setFixedSize(newsize)
        butttons = self.findChildren(QToolButton)
        for button in butttons:
            if button.icon() is not None:
                button.setIconSize(newsizeicon)
                button.setBaseSize(newsize)
                button.setFixedSize(newsize)


        for dbasetablename in self.dbase.dbasetables.keys():
            wgds = self.dbase.dbasetables[dbasetablename]['widget']
            # print('changed', dbasetablename,wgd )
            if not isinstance(wgds, list):
                listwdg = [wgds]
            else:
                listwdg = wgds

            for wdg in listwdg:
                wdg.themechanged(iconwidth)




    def setWorkingDate(self):
        """
        pass
        """
        if False:
            if self.dbase.workingdate is None:
                self.dateDialog.setDate()
            else:
                self.dateDialog.setDate(self.dbase.workingdate)

            todaydate = QtCore.QDate.currentDate()
            self.dateDialog.label_end.setText( todaydate.toString('yyyy-MM-dd') )
            sql = "SELECT MIN(datecreation) FROM Objet"
            query = self.dbase.query(sql)
            startdate = [row[0] for row in query]
            if len(startdate)>0:
                date2 = QtCore.QDate.fromString(startdate[0], 'yyyy-MM-dd')
            else:
                date2 = todaydate
            self.dateDialog.label_start.setText(date2.toString('yyyy-MM-dd'))
            dif = date2.daysTo(todaydate)
            #dif = todaydate - date2
            self.dateDialog.horizontalSlider_date.setRange(0, dif)

            self.dateDialog.horizontalSlider_date.valueChanged.connect(self.dateSliderAction)


        self.dateDialog.setDate()
        self.dateDialog.exec_()
        if False:
            date = self.dateDialog.dialogIsFinished()
            if date is not None:
                self.dbase.workingdate = date
                self.dbase.updateWorkingDate()







    def closeEvent(self, event):
        """
        PyQt closeEvent - called when the windowdialog is closed
        Unloads the tools widgets
        """
        if True:
            for tool in self.tools:
                del tool
        self.closingPlugin.emit()
        try:
            self.dbase.canvas.renderStarting.disconnect(self.dbaserenderStarts)
        except:
            pass
        event.accept()

    def connectToGPS(self):
        success = self.gpsutil.connectToGPS()
        if False:
            if not success:
                print('gps connection failed')
                self.GPSConnected.emit(False)
            else:
                self.GPSConnected.emit(True)

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



    def unloadTools(self):
        """!
        Clears self.tools and clear the ui (tools widget and windowswidget)
        Called before loadTools
        """
        self.MaintreeWidget.clear()

        if False:
            try:
                # self.MaintreeWidget.clear()
                for i in range(self.stackedWidgetTool.count()):
                    widg = self.stackedWidgetTool.widget(i)
                    self.stackedWidgetTool.removeWidget(widg)
                self.tools = []
            except Exception as e:
                # self.errorMessage('Eror unloading tools : ', e)
                print('Eror unloading tools : ', e)
        pass

    # **********************************************************************************************
    # ********************************    MENU    ********************************************
    # **********************************************************************************************

    def setVisualMode(self, tempres=None, reset=False):
        """
        pass
        """

        if not isinstance(self.sender(), QAction):
            return

        actionname = self.sender().objectName()
        actiontext = self.sender().text()

        qactionchild = self.menuMode.actions()
        for qact in qactionchild:
            qact.setChecked(False)
            if not reset and qact.text() == actiontext:
                qact.setChecked(True)

        if reset:
            self.dbase.visualmode = 0
            self.actionModeTerrain.setChecked(True)
            return

        if "Terrain" in actiontext:
            self.dbase.visualmode = 0
        elif "Bureau" in actiontext:
            self.dbase.visualmode = 1
            if not self.desktopuiloaded:
                self.loadUiDesktop()
        elif "Expert" in actiontext:
            self.dbase.visualmode = 2
        elif "Post traitement" in actiontext:
            self.dbase.visualmode = 4
            if not self.desktopuiloaded:
                self.loadUiDesktop()

        self.applyVisualMode(actiontext)



    def applyVisualMode(self, actiontext=None):
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






    def reinitCurrentPrestation(self):
        if self.dbase is not None:
            self.dbase.currentprestationid = None
            self.currentprestationlabel.setText('Prestation inactif')



    def setHauteurPerche(self):
        num, ok = QInputDialog.getDouble(self,
                                         "Hauteur de perche",
                                         "Rentrer la hauteur de perche GPS",
                                         self.gpsutil.hauteurperche,
                                         decimals=2)
        if ok:
            # self.dbase.hauteurperche = num
            self.gpsutil.hauteurperche = num


    def setVersion(self):
        num, ok = QInputDialog.getInteger(self,
                                         "Version",
                                         "Version à afficher",
                                         value = self.dbase.currentrevision,
                                          min = 1,
                                          max = self.dbase.maxrevision)
        if ok:
            self.dbase.currentrevision = num
            self.dbase.updateWorkingDate()

            self.MaintreeWidget.currentItemChanged.emit(self.MaintreeWidget.currentItem(),self.MaintreeWidget.currentItem())



    def setLamiaIconSize(self):
        self.iconsizedialog.exec_()



    def newDbase(self):
        """
        pass
        """
        # print(self.sender().objectName())
        # print(self.sender().text())
        # new db dialog

        #self.newDBDialog.dbase = self.dbase
        self.newDBDialog.comboBox_type.currentIndexChanged.emit(0)
        self.newDBDialog.exec_()
        dbtype, worktype, vartype = self.newDBDialog.dialogIsFinished()

        # print('**',dbtype,worktype, vartype  )
        if dbtype is None :
            return
        # crs selector
        self.crsselector.exec_()
        if sys.version_info.major == 2:
            crs = self.crsselector.selectedAuthId()
            crsnumber = int(crs.split(':')[1])
        elif sys.version_info.major == 3:
            crs = self.crsselector.crs().authid()
            crsnumber = int(crs.split(':')[1])
        # ressources directory
        if dbtype == 'postgis':
            resdir = self.qfiledlg.getExistingDirectory(self, "Selectionner le repertoire des ressources")
            if resdir:
                resdir = str(resdir)
            else:
                return
        else:
            resdir = None

        # dialogs finished - reinit base
        #self.dbase.reInitDBase()
        #reset dbase
        #self.createDBase()


        # create database
        if dbtype == 'spatialite':
            if sys.version_info.major == 2:
                spatialitefile = self.qfiledlg.getSaveFileName(self, 'Lamia nouveau', '', '*.sqlite')
            elif sys.version_info.major == 3:
                spatialitefile, fileext = self.qfiledlg.getSaveFileName(self, 'Lamia nouveau', '', '*.sqlite')
            #print('spatialitefile', spatialitefile)
            if False and sys.version_info.major == 3 and len(spatialitefile)>0:
                spatialitefile = spatialitefile[0]
            self.createDBase()

            if spatialitefile:
                # reset dbase
                # self.createDBase()
                # originalfile = os.path.join(os.path.dirname(__file__), '..', 'DBASE', 'DBase_ind0.sqlite')
                # shutil.copyfile(originalfile, spatialitefile)

                self.normalMessage(' Creation de la base de donnees...')
                QApplication.processEvents()
                #resdir = self.createRessourcesDir(dbtype,resdir, spatialitefile, vardir=vardir )


                self.dbase.createDbase(slfile=spatialitefile, crs=crsnumber, worktype=worktype, dbasetype='spatialite',
                                       dbaseressourcesdirectory = resdir, variante=vartype)
                if False:
                    self.loadQgisVectorLayers(file=self.dbase.spatialitefile, dbasetype=self.dbase.dbasetype,
                                              host=self.dbase.pghost, port=self.dbase.pgport, dbname=self.dbase.pgdb, schema=self.dbase.pgschema,
                                              user=self.dbase.pguser, password=self.dbase.pgpassword)


        elif dbtype == 'postgis':
            self.connDialog.exec_()
            adresse, port, nom, schema, user, password = self.connDialog.dialogIsFinished()
            if adresse is not None and port is not None and nom is not None and user is not None and password is not None:
                self.createDBase()
                databaseexists, schemaexists = self.dbase.checkIfPGShcemaExists(host=adresse, dbname=nom, schema=schema,
                                                                                user=user, password=password)
                if  schemaexists :
                    print('schema existe deja - choisir un autre schema')
                else:
                    self.normalMessage('Creation de la base de donnees...')
                    # reset dbase
                    #self.createDBase()
                    QApplication.processEvents()

                    #resdir = self.createRessourcesDir(dbtype, resdir,vardir=vardir)

                    self.dbase.createDbase(crs=crsnumber, worktype=worktype, dbasetype='postgis', dbname=nom, schema=schema,
                                           user=user, host=adresse, password=password, dbaseressourcesdirectory=resdir,
                                           port=port,variante=vartype)



                    if False:
                        self.loadQgisVectorLayers(file=self.dbase.spatialitefile, dbasetype=self.dbase.dbasetype,
                                                  host=self.dbase.pghost, port=self.dbase.pgport, dbname=self.dbase.pgdb, schema=self.dbase.pgschema,
                                                  user=self.dbase.pguser, password=self.dbase.pgpassword)



    def createRessourcesDir(self, dbasetype,dbaseressourcesdirectory, slfile=None,vardir=None):
        dbaseressourcesdirectorytemp = None

        if dbaseressourcesdirectory is None and dbasetype == 'spatialite':
            dbaseressourcesdirectorytemp = os.path.join(os.path.dirname(slfile), u'DBspatialite')
        else:
            dbaseressourcesdirectorytemp = dbaseressourcesdirectory

        if not os.path.isdir(dbaseressourcesdirectorytemp):
            os.makedirs(dbaseressourcesdirectorytemp)
            configdir = os.path.join(dbaseressourcesdirectorytemp, 'config')
            os.makedirs(configdir)
            # tool dir
            dbasedir = os.path.join(configdir, 'dbase')
            os.makedirs(dbasedir)

            rapportdir = os.path.join(configdir, 'rappporttools')
            os.makedirs(rapportdir)
            styledir = os.path.join(configdir, 'styles')
            os.makedirs(styledir)
            importdir = os.path.join(configdir, 'importtools')
            os.makedirs(importdir)

        if vardir is not None:
            dirfiles = [f for f in os.listdir(vardir) if os.path.isfile(os.path.join(vardir, f))]
            for dirfile in dirfiles:
                fromfile = os.path.join(vardir, dirfile)
                tofile = os.path.join(dbaseressourcesdirectorytemp,'config','dbase', dirfile)
                shutil.copy(fromfile, tofile)



        return dbaseressourcesdirectorytemp



    def openFileFromMenu(self, action):
        """
        pass
        """

        #reset dbase
        #reset dbase


        filetoopen = action.text()
        if len(filetoopen.split(';')) == 1:
            self.createDBase()
            self.dbase.loadQgisVectorLayers(filetoopen)
        else:
            self.createDBase()
            db, user, password = filetoopen.split(';')
            nom, schema = db.split('@')[0].split('.')
            adresse, port = db.split('@')[1].split(':')
            self.dbase.loadQgisVectorLayers(dbasetype='postgis', host=adresse, port=int(port), dbname=nom,
                                            schema=schema, user=user, password=password)

    #
    def loadSLDbase(self):

        if sys.version_info.major == 2:
            file, extension = self.qfiledlg.getOpenFileNameAndFilter(None, 'Choose the file', '',
                                                                     'Spatialite (*.sqlite)', '')
        elif sys.version_info.major == 3:
            file , extension= self.qfiledlg.getOpenFileName(None, 'Choose the file', '',
                                                                     'Spatialite (*.sqlite)', '')
            print(file)
        if file:
            # reset dbase
            #self.reinitDBase()
            # reset dbase
            self.createDBase()
            self.dbase.loadQgisVectorLayers(file)

    def loadPGDbase(self):
        self.connDialog = ConnexionPGDialog()
        self.connDialog.exec_()
        adresse, port, nom, schema, user, password = self.connDialog.dialogIsFinished()
        if adresse is not None and port is not None and nom is not None and user is not None and password is not None:
            # reset dbase
            # reset dbase
            self.createDBase()

            self.dbase.loadQgisVectorLayers(file=None, dbasetype='postgis', host=adresse, port=port, dbname=nom,
                                            schema=schema, user=user, password=password)

    def updateRecentDBaseMenu(self):
        self.menuBases_recentes.triggered.disconnect(self.openFileFromMenu)
        self.menuBases_recentes.clear()
        for telem in self.recentsdbase:
            self.menuBases_recentes.addAction(telem)
        self.menuBases_recentes.triggered.connect(self.openFileFromMenu)


    def _readRecentDBase(self):
        """
        Lit le fichier des bases de données recentes et rempli le  menu//Fichier//base de données recentes
        """
        pathrecentproject = os.path.join(os.path.dirname(__file__), '..', 'config', 'recentprojects.txt')
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
        self.updateRecentDBaseMenu()

    def _AddDbaseInRecentsDBase(self, spatialitefile=None, host='localhost',
                                port=None, dbname=None, schema=None, user=None, password=None):
        """
        Methode appelée lors du chargement d'une BD lamia
        Ajoute le chemin dans le fichier chargé dans Menu//Fichier//base de données recentes
        """
        if self.dbase.dbasetype == 'spatialite':
            if spatialitefile in self.recentsdbase:
                index = self.recentsdbase.index(spatialitefile)
                del self.recentsdbase[index]
            self.recentsdbase.insert(0, spatialitefile)
            self._saveRecentDBase()
            # self.recentDBaseChanged.emit()
            self.updateRecentDBaseMenu()
        elif self.dbase.dbasetype == 'postgis':
            name = dbname + '.' +schema  + '@' + host + ':' + str(port) + ';' + user + ';' + password
            if name in self.recentsdbase:
                index = self.recentsdbase.index(name)
                del self.recentsdbase[index]
            self.recentsdbase.insert(0, name)
            self._saveRecentDBase()
            # self.recentDBaseChanged.emit()
            self.updateRecentDBaseMenu()


    def _saveRecentDBase(self):
        """
        Sauve le path de la BD lamia en cours d'utilisation dans le ficier employé dans
        menu//Fichier//base de données recentes
        """
        pathrecentproject = os.path.join(os.path.dirname(__file__), '..', 'config', 'recentprojects.txt')
        file = open(pathrecentproject, "w")
        for i, path in enumerate(self.recentsdbase):
            if i > 10:
                break
            if not path == '':
                file.write(path + '\n')
        file.close()
        # self.recentDBaseChanged.emit()
        self.updateRecentDBaseMenu()







    def DBaseLoaded(self):
        """
        Load layers and put them in a legend group in qgis
        Load all modules (prepro, postpro and menu)
        Show field ui

        :return:
        """

        debug = False
        if debug: logging.getLogger('Lamia').debug('start')

        if False:
            qgis.utils.uninstallErrorHook()  # for standart output
            qgis.utils.uninstallErrorHook()  # for standart output
            sys.excepthook = sys.__excepthook__
            print(sys.excepthook)
            print(sys.stderr)
            'okok'.decode('utf-8')

        self._AddDbaseInRecentsDBase(spatialitefile=self.dbase.spatialitefile,
                                     host=self.dbase.pghost,
                                     port=self.dbase.pgport,
                                     dbname=self.dbase.pgdb,
                                     schema=self.dbase.pgschema,
                                     user=self.dbase.pguser,
                                     password=self.dbase.pgpassword)

        self.gpsutil.setCRS(self.dbase.qgiscrs)
        self.dbase.updateWorkingDate()
        timestart = self.dbase.getTimeNow()

        self.MaintreeWidget.setStyleSheet("")
        self.ElemtreeWidget.setStyleSheet("")

        if debugtime: logger.debug(' progress bar done %.3f', self.dbase.getTimeNow() - timestart)

        # ************************** Define qgis legend gourp and dock widget title ***********************************

        root = qgis.core.QgsProject.instance().layerTreeRoot()
        #root.addGroup('Lamia')
        if self.dbase.dbasetype == "spatialite":
            groupname = 'Lamia_' + os.path.basename(self.dbase.spatialitefile)
        elif self.dbase.dbasetype == "postgis":
            groupname = 'Lamia_' + self.dbase.pgschema

        #lamialegendgroup =  root.findGroup('Lamia')
        lamialegendgroup = root.findGroup(groupname)
        if lamialegendgroup is None:
            lamialegendgroup = root.insertGroup(0, groupname)
        self.qgislegendnode = lamialegendgroup

        if self.dockwgt is not None:
            self.dockwgt.setWindowTitle(groupname)

        # ************************** LOAD LAYERS AND STYLES ***********************************

        for tablename in self.dbase.dbasetables:
            if self.dbase.dbasetables[tablename]['showinqgis']:

                if True:
                    if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                        qgis.core.QgsMapLayerRegistry.instance().addMapLayer(self.dbase.dbasetables[tablename]['layerqgis'],
                                                                             False)
                    else:
                        qgis.core.QgsProject.instance().addMapLayer(self.dbase.dbasetables[tablename]['layerqgis'], False)


                lamialegendgroup.addLayer(self.dbase.dbasetables[tablename]['layerqgis'])
            else:
                if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                    qgis.core.QgsMapLayerRegistry.instance().addMapLayer(self.dbase.dbasetables[tablename]['layer'],
                                                                         False)
                else:
                    qgis.core.QgsProject.instance().addMapLayer(self.dbase.dbasetables[tablename]['layer'],
                                                                False)


        self.loadStyle()

        # ************************** LOAD prepro MODULES ********************************************
        if True:
            path = os.path.join(os.path.dirname(__file__), '..', 'toolprepro', self.dbase.type.lower())
            modules = glob.glob(path + "/*.py")
            __all__ = [os.path.basename(f)[:-3] for f in modules if os.path.isfile(f)]
            interfacefielduisup=[]

            for x in __all__:
                if debug: logging.getLogger('Lamia').debug('x %s', x)
                if self.dbase.qgsiface is not None:
                    #   if not self.dbase.standalone:
                    exec('import Lamia.toolprepro.' + self.dbase.type.lower())
                    moduletemp = importlib.import_module('.' + str(x), 'Lamia.toolprepro.' + self.dbase.type.lower() )
                    # moduletemp = importlib.import_module('.' + str(x), 'Lamia.toolprepro.' + self.dbase.type.lower())
                    # moduletemp = importlib.import_module('.' + str(x), '..toolprepro.' + self.dbase.type.lower())
                else:
                    exec('import Lamia.toolprepro.' + self.dbase.type.lower())
                    moduletemp = importlib.import_module('.' + str(x), 'Lamia.toolprepro.' + self.dbase.type.lower())

                for name, obj in inspect.getmembers(moduletemp, inspect.isclass):
                    if moduletemp.__name__ == obj.__module__:

                        try:
                            tempspecialfieldui = obj.specialfieldui
                            for elem in tempspecialfieldui:
                                if elem not in interfacefielduisup:
                                    interfacefielduisup.append(elem)
                        except Exception:
                            pass
                        try:
                            if obj.LOADFIRST:
                                self.uifields.append(obj)
                            else:
                                self.uidesktop.append(obj)
                        except AttributeError:
                            pass

            if debug: logging.getLogger('Lamia').debug('step1')

        # add field ui in interface menu
        for elem in interfacefielduisup :
            tempaction = QAction("Terrain_" + elem , self)
            tempaction.setCheckable(True)
            self.menuMode.insertAction(self.actionTTC, tempaction)
            tempaction.triggered.connect(self.setVisualMode)


        # ************************** LOAD postpro MODULES ********************************************
        if True:
            path = os.path.join(os.path.dirname(__file__), '..', 'toolpostpro',self.dbase.type)
            modules = glob.glob(path + "/*.py")
            __all__ = [os.path.basename(f)[:-3] for f in modules if os.path.isfile(f)]
            for x in __all__:
                if self.dbase.qgsiface is not None:
                    #if not self.dbase.standalone:
                    exec('import Lamia.toolpostpro.' + self.dbase.type)
                    moduletemp = importlib.import_module('.' + str(x), 'Lamia.toolpostpro.' + self.dbase.type )
                else:
                    exec('import Lamia.toolpostpro.' + self.dbase.type )
                    moduletemp = importlib.import_module('.' + str(x), 'Lamia.toolpostpro.' + self.dbase.type)
                for name, obj in inspect.getmembers(moduletemp, inspect.isclass):
                    if moduletemp.__name__ == obj.__module__:
                        if hasattr(obj,'TOOLNAME'):
                            self.uipostpro.append(obj)
                            # print(type(obj), obj.__class__)
                        if False:
                            try:
                                if self.dbase.type.lower() in obj.DBASES:
                                    self.uipostpro.append(obj)
                            except AttributeError:
                                pass

            if debugtime: logger.debug('applyVisualMode %.3f', time.clock() - timestart)



        # ************************** Show fields ui ********************************************
        self.loadUiField()



    def loadStyle(self):
        try:
            self.comboBox_style.currentIndexChanged.disconnect(self.comboStyleChanged)
        except:
            pass
        self.comboBox_style.clear()
        stylepath = os.path.join(os.path.dirname(__file__), '..','DBASE', 'style', self.dbase.type)
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
        stylerep = os.path.join(os.path.dirname(__file__), '..', 'DBASE', 'style', self.dbase.type, styledir )

        allfiles = [x[2] for x in os.walk(stylerep)][0]
        qmlfiles = [uknfile.split('.')[0] for uknfile in allfiles if uknfile.split('.')[1] == 'qml']


        for dbasetablename in self.dbase.dbasetables.keys():
            if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                if qgis.utils.iface is not None:
                    lgdiface = qgis.utils.iface.legendInterface()
                else:
                    lgdiface = None

                if dbasetablename in qmlfiles:
                    if lgdiface:
                        lgdiface.setLayerVisible(self.dbase.dbasetables[dbasetablename]['layerqgis'],True)
                    stylepath = os.path.join(stylerep,dbasetablename + '.qml' )
                    self.dbase.dbasetables[dbasetablename]['layerqgis'].loadNamedStyle(stylepath)
                else:
                    if lgdiface:
                        lgdiface.setLayerVisible(self.dbase.dbasetables[dbasetablename]['layerqgis'], False)
            else:
                if 'layerqgis' in self.dbase.dbasetables[dbasetablename].keys() :
                    ltl = qgis.core.QgsProject.instance().layerTreeRoot().findLayer(self.dbase.dbasetables[dbasetablename]['layerqgis'].id())
                    if dbasetablename in qmlfiles:
                        if ltl:
                            ltl.setItemVisibilityChecked(True)
                        stylepath = os.path.join(stylerep, dbasetablename + '.qml')
                        self.dbase.dbasetables[dbasetablename]['layerqgis'].loadNamedStyle(stylepath)
                    else:
                        if ltl:
                            ltl.setItemVisibilityChecked(False)

        if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
            self.canvas.refresh()
        else:
            self.canvas.refreshAllLayers()



    def loadUiField(self):

        timestart = self.dbase.getTimeNow()
        if debugtime: logger.debug(' start %.3f', self.dbase.getTimeNow() - timestart)

        # init progress bar
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


    def loadUiDesktop(self):

        debug = False

        # init progress bar
        if self.dbase.qgsiface is not None:
            progressMessageBar = self.dbase.qgsiface.messageBar().createMessage("Loading widget...")
            progress = QProgressBar()
            progress.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
            progressMessageBar.layout().addWidget(progress)
            if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                self.dbase.qgsiface.messageBar().pushWidget(progressMessageBar, self.dbase.qgsiface.messageBar().INFO)
            else:
                self.dbase.qgsiface.messageBar().pushWidget(progressMessageBar, qgis.core.Qgis.Info)
            lenuifields = len(self.uidesktop)
            lenuipostpro = len(self.uipostpro)
            lenmenutool = len(self.menuclasses)
            progress.setMaximum(lenuifields + lenuipostpro + lenmenutool)
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



    #**********************************************************************************************
    #********************************    Tree widget    ********************************************
    #**********************************************************************************************

    def zoomToFeature(self):
        wdg = self.stackedWidgetTool.currentWidget()
        wdg.zoomToFeature()

    def copyFeature(self):
        wdg = self.stackedWidgetTool.currentWidget()
        wdg.copyFeature()

    def addFeature(self):
        wdg = self.stackedWidgetTool.currentWidget()
        wdg.addFeature()

    def deleteToFeature(self):
        wdg = self.stackedWidgetTool.currentWidget()
        wdg.deleteFeature()

    def selectFeature(self):
        if False:
            if self.pointEmitter is None:
                self.pointEmitter = qgis.gui.QgsMapToolEmitPoint(self.canvas)
                self.pointEmitter.canvasClicked .connect(self.selectPickedFeature)
            if self.canvas.mapTool() != self.pointEmitter:
                try:
                    self.canvas.mapToolSet.disconnect(self.toolsetChanged)
                except TypeError:
                    pass
                self.canvas.setMapTool(self.pointEmitter)
                self.canvas.mapToolSet.connect(self.toolsetChanged)
        if False:
            self.pointEmitter.canvasClicked .connect(self.selectPickedFeature)
            self.canvas.setMapTool( self.pointEmitter )

        if False:
            print(self.canvas.mapTool())
            if self.canvas.mapTool() != self.pointEmitter:
                self.pointEmitter.canvasClicked.connect(self.selectPickedFeature)
                self.canvas.mapToolSet.connect(self.toolsetChanged)
                self.canvas.setMapTool(self.pointEmitter)
                print('action')

        if True:
            try:
                self.pointEmitter.canvasClicked.disconnect(self.selectPickedFeature)
            except TypeError:
                pass
            try:
                self.canvas.mapToolSet.disconnect(self.toolsetChanged)
            except TypeError:
                pass
            self.pointEmitter.canvasClicked.connect(self.selectPickedFeature)
            self.canvas.mapToolSet.connect(self.toolsetChanged)
            self.canvas.setMapTool(self.pointEmitter)

    def editFeature(self):
        if self.editfeatureworking == True :
            return


        self.editfeatureworking = False

        """
        if True:
            if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                qgis.core.QgsMapLayerRegistry.instance().addMapLayer(self.dbase.dbasetables[tablename]['layerqgis'],
                                                                     False)
            else:
                qgis.core.QgsProject.instance().addMapLayer(self.dbase.dbasetables[tablename]['layerqgis'],
                                                            False)
        lamialegendgroup.addLayer(self.dbase.dbasetables[tablename]['layerqgis'])
        """


        if self.stackedWidget_main.currentIndex() == 0:
            wdg = self.MaintabWidget.widget(0).layout().itemAt(0).widget()

            self.editfeaturelayer = qgis.core.QgsVectorLayer(wdg.dbasetable['layer'].source(),
                                                             wdg.dbasetable['layer'].name() + '_edit',
                                                             wdg.dbasetable['layer'].providerType())

            if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                qgis.core.QgsMapLayerRegistry.instance().addMapLayer(self.editfeaturelayer,False)
                self.editfeaturetreelayer = self.qgislegendnode.insertLayer(0,self.editfeaturelayer)
                if self.dbase.qgsiface is not None :
                    self.dbase.qgsiface.setActiveLayer(self.editfeaturelayer)
                    self.editfeaturelayer.startEditing()
                    self.dbase.qgsiface.actionNodeTool().trigger()
            else:
                qgis.core.QgsProject.instance().addMapLayer(self.editfeaturelayer, False)
                self.editfeaturetreelayer = self.qgislegendnode.insertLayer(0,self.editfeaturelayer)
                if self.dbase.qgsiface is not None :
                    self.dbase.qgsiface.setActiveLayer(self.editfeaturelayer)
                    self.editfeaturelayer.startEditing()
                    self.dbase.qgsiface.actionVertexTool().trigger()

            self.editfeatureworking = True


    def closeEditFeature(self, maintreewdgindex=None, savechanges=False):

        if self.editfeatureworking:
            self.editfeatureworking = False
            if isinstance(savechanges,bool) and savechanges:
                self.editfeaturelayer.commitChanges()
            else:
                self.editfeaturelayer.rollBack()
            self.qgislegendnode.removeLayer(self.editfeaturelayer)


    def selectPickedFeature(self, point):
        # print('select',point.x(), point.y())
        debug = False
        if debug: logging.getLogger("Lamia").debug('Start %s', str(point))

        addselection = False
        modifiers = QApplication.keyboardModifiers()
        #print('modif')
        #if modifiers == QtCore.Qt.ShiftModifier:
        if modifiers == QtCore.Qt.ControlModifier:
            # print('Ctrl+Click')
            addselection = True



        if False:
            self.canvas.unsetMapTool(self.pointEmitter)
            try:
                self.pointEmitter.canvasClicked.disconnect(self.selectPickedFeature)
            except:
                pass
        # print('windowd selectPickedFeature',self.stackedWidget_main.currentIndex() )
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




        if False:
            self.canvas.unsetMapTool( self.pointEmitter )
            if self.canvas.mapTool() != self.pointEmitter:
                pass
            try:
                self.pointEmitter.canvasClicked .disconnect(self.selectPickedFeature)
            except:
                pass




    def toolsetChanged(self, newtool, oldtool=None):
        # print('toolsetchanged', newtool,oldtool )
        self.closeEditFeature()

        if newtool != self.pointEmitter :
            if False:
                try:
                    self.pointEmitter.canvasClicked .disconnect()
                except TypeError:
                    pass
                # self.pointEmitter = None
                self.canvas.mapToolSet.disconnect(self.toolsetChanged)
            if True:
                self.pointEmitter.canvasClicked.disconnect()
                self.canvas.mapToolSet.disconnect(self.toolsetChanged)

    def setImageDir(self):
        file = self.qfiledlg.getExistingDirectory(self, "Select Directory",self.dbase.imagedirectory, QFileDialog.ShowDirsOnly)
        if file:
            self.dbase.imagedirectory = file
            QtCore.QSettings().setValue("InspectionDigue/picturepath", file)


    def showNumPad(self, finalwdg):
        # print('ok', finalwdg)

        self.numpaddialog.exec_()
        number = self.numpaddialog.dialogIsFinished()
        # print(number)
        if number:
            finalwdg.setValue(number)



    def exportBase(self):

        #exportfile, extension = self.qfiledlg.getOpenFileNameAndFilter(None, 'Export vers', '','Spatialite (*.sqlite)', '')
        if sys.version_info.major == 2:
            exportfile = self.qfiledlg.getSaveFileName(self, 'Lamia exporter vers', '', '*.sqlite')
        elif sys.version_info.major == 3:
            exportfile, fileext = self.qfiledlg.getSaveFileName(self, 'Lamia exporter vers', '', '*.sqlite')

        if exportfile:
            self.exportdbase = DBaseParser()
            self.exportdbase.loadQgisVectorLayers(exportfile)

            # backup destination exportfile
            name = os.path.basename(exportfile)
            date = datetime.datetime.now().strftime("%y_%m_%d_%H_%M")
            finalname = os.path.join(os.path.dirname(exportfile), name.split('.')[0] + '_' + date + '.sqlite')
            shutil.copyfile(exportfile, finalname)

            # run export
            self.dbase.exportBase(self.exportdbase)

            if self.dbase.qgsiface is not None:
                # if not self.dbase.standalone:
                self.dbase.qgsiface.messageBar().pushMessage("Lamia ", 'Export fini', level=qgis.gui.QgsMessageBar.SUCCESS, duration=3)
            else:
                print('export fini')

    def openHelp(self):
        path = os.path.join(os.path.dirname(__file__),'..','doc_html','index.html')
        if platform.system() == 'Linux':
            r = subprocess.call(('xdg-open', path))
        elif platform.system() == 'Windows':
            os.startfile(path)


    def errorMessage(self, text):
        # print('eror', self.sender(),self.sender().name())
        if self.dbase.qgsiface is not None:
            #if not self.dbase.standalone:
            if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                self.dbase.qgsiface.messageBar().pushMessage("Lamia ", text,
                                                          level=qgis.gui.QgsMessageBar.CRITICAL, duration=3)
            else:
                self.dbase.qgsiface.messageBar().pushMessage("Lamia ", text,
                                                          level=qgis.core.Qgis.Critical , duration=3)
        else:
            print('ErrorMessage', text)

        QApplication.processEvents()

    def warningMessage(self, text):
        if self.dbase.qgsiface is not None:
            # if not self.dbase.standalone:
            if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                self.dbase.qgsiface.messageBar().pushMessage("Lamia ", text,
                                                          level=qgis.gui.QgsMessageBar.WARNING, duration=3)
            else:
                self.dbase.qgsiface.messageBar().pushMessage("Lamia ", text,
                                                          level= qgis.core.Qgis.Warning , duration=3)
        else:
            print('ErrorMessage', text)

    def normalMessage(self, text):
        if self.dbase.qgsiface is not None:
            #if not self.dbase.standalone:
            # self.dbase.qgsiface.messageBar().pushMessage("InspectionDigue", text, level=qgis.gui.QgsMessageBar.INFO, duration=3)
            if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                self.dbase.qgsiface.messageBar().pushMessage("Lamia ", text, self.dbase.qgsiface.messageBar().INFO)
            else:
                self.dbase.qgsiface.messageBar().pushMessage("Lamia " ,text, qgis.core.Qgis.Info)

        else:
            print('normalMessage', text)

        QApplication.processEvents()



    def cleanLayerTree(self):
        if self.qgislegendnode is not None:
            self.qgislegendnode.removeAllChildren()
            root = qgis.core.QgsProject.instance().layerTreeRoot()
            root.removeChildNode(self.qgislegendnode)





    def exportPDFFinished(self):
        self.normalMessage('Export termine')


    def printError(self,errorstr):
        print('error', errorstr)

    def printMessage(self,message):
        print('message', message)

    """
    def importObjet(self):

        items = ("Points topo", "Infralineaire")
        item, ok = QInputDialog.getItem(self, "select input dialog",
                                        "list of languages", items, 0, False)
        if ok and item:
            if self.dbase.qgsiface is not None:
                #if not self.dbase.standalone:
                currentlayer = self.dbase.qgsiface.activeLayer()
                currentlayerfields = currentlayer.fields()
                currentlayerfieldsname = [''] + [field.name() for field in currentlayerfields]
                # combofield = QComboBox([''] + currentlayerfieldsname)
            else:       #debug outside qgis
                currentlayerfieldsname = ['','ALTINGF','typ']



            if item == "Points topo":
                print('ok')
                templinkuserwgd = self.dbase.dbasetables['Topographie']['widget'].propertieswdgPOINTTOPO.linkuserwdg
            if item == "Infralineaire":
                templinkuserwgd = self.dbase.dbasetables['Infralineaire']['widget'].linkuserwdg
            if item == "Desordre":
                templinkuserwgd = self.dbase.dbasetables['Desordre']['widget'].linkuserwdg
            if item == "Observation":
                templinkuserwgd = self.dbase.dbasetables['Observation']['widget'].linkuserwdg
            if item == "Noeud":
                templinkuserwgd = self.dbase.dbasetables['Noeud']['widget'].linkuserwdg
            if item == "Equipement":
                templinkuserwgd = self.dbase.dbasetables['Equipement']['widget'].linkuserwdg
            if item == "Travaux":
                templinkuserwgd = self.dbase.dbasetables['Travaux']['widget'].linkuserwdg
            if item == "Environnement":
                templinkuserwgd = self.dbase.dbasetables['Environnement']['widget'].linkuserwdg


            self.importobjetdialog.tableWidget.setRowCount(0)
            self.importobjetdialog.tableWidget.setColumnCount(2)
            for tablename in templinkuserwgd:
                if tablename in self.dbase.dbasetables.keys():
                    dbasetable = self.dbase.dbasetables[tablename]
                    for field in dbasetable['fields'].keys():
                        #print(field)
                        rowPosition = self.importobjetdialog.tableWidget.rowCount()
                        self.importobjetdialog.tableWidget.insertRow(rowPosition)
                        itemfield = QTableWidgetItem(tablename + '.' + field)
                        itemfield.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                        self.importobjetdialog.tableWidget.setItem(rowPosition, 0, itemfield)
                        # item.setFlags()
                        if field[0:2] != 'id':
                            combofield = QComboBox()
                            combofield.addItems(currentlayerfieldsname)
                            self.importobjetdialog.tableWidget.setCellWidget(rowPosition, 1, combofield)
                        else:
                            itemfield = QTableWidgetItem('')
                            self.importobjetdialog.tableWidget.setItem(rowPosition, 1, itemfield)


            self.importobjetdialog.exec_()
            tableview = self.importobjetdialog.dialogIsFinished()
            if tableview is not None:
                result = []
                for row in range(self.importobjetdialog.tableWidget.rowCount()):
                    if self.importobjetdialog.tableWidget.cellWidget(row, 1) is not None:
                        result.append([self.importobjetdialog.tableWidget.item(row,0).text(),
                                       self.importobjetdialog.tableWidget.cellWidget(row, 1).currentText()])
                    else:
                        result.append([self.importobjetdialog.tableWidget.item(row,0).text(),self.importobjetdialog.tableWidget.item(row,1).text()])
                print(result)

                if True:
                    self.worker = ImportObjectWorker(self.dbase, item, result)
                    self.worker.finished.connect(self.exportPDFFinished)
                    self.worker.error.connect(self.printError)
                    self.worker.message.connect(self.printMessage)
                    self.worker.run()
    """

    def modeHorsLigne(self):



        #First we have to disconnect : create a local db and transfer the data .............................................................
        if not self.dbase.horsligne:


            #1)Create a spatialite db ..................................................
            # create database
            try :
                os.remove('../local/DB_local.sqlite')
            except:
                pass

            #Create the folder to stock the new pictures
            local_folder='../local/local_data'
            if not os.path.exists(local_folder):
                os.makedirs(local_folder)

            #Deal with the connections : keep in memory the former connection
            if self.dbase.dbasetype=='spatialite':
                self.dbase.offLineConn = self.dbase.connSLITE
                self.dbase.offLineCursor = self.dbase.SLITEcursor
                self.dbase.offLineType = 'spatialite'
            else:
                self.dbase.offLineConn = self.dbase.connPGis
                self.dbase.offLineCursor = self.dbase.PGiscursor
                self.dbase.offLineType = 'postgis'


            local_db='../local/DB_local.sqlite'

            originalfile = os.path.join(os.path.dirname(__file__), '..', 'DBASE', 'DBase_ind0.sqlite')
            shutil.copyfile(originalfile, local_db)


            self.dbase.createDbase(file=local_db, crs=self.dbase.crsnumber, type='digue', dbasetype='spatialite',
                                       dbaseressourcesdirectory=local_folder)
            self.dbaseressourcesdirectory=local_folder
            self.dbase.dbasetype = 'spatialite'
            self.dbase.date_deconnexion=datetime.datetime.now()



            #2)Add items from the file to the spatialite database .................................................................
            for order in range(10):
                for dbname in self.dbase.dbasetables:
                    if self.dbase.dbasetables[dbname]['order'] == order and not dbname=='Basedonnees':

                        print("Import de la table : "+dbname)
                        fields_table = self.dbase.dbasetables[dbname]['fields'].keys()


                        fields_to_import=fields_table
                        if 'geom' in self.dbase.dbasetables[dbname]:
                            fields_to_import+=['ST_AsText(geom)']
                        sql = 'SELECT '+  ','.join(fields_to_import) + ' FROM '+ str(dbname)

                        if self.dbase.offLineType == 'spatialite' :
                            try:
                                print(sql)
                                query = self.dbase.offLineCursor.execute(sql)
                                returnquery = list(query)
                                self.dbase.commit()
                            except OperationalError as e:
                                print('error query', e)
                                continue
                        else :
                            print(sql)
                            self.PGiscursor.execute(sql)
                            if sql.strip()[0:6] == 'SELECT':
                                try:
                                    rows = self.dbase.offLineCursor.fetchall()
                                    returnquery = list(rows)
                                    self.dbase.commit()
                                except psycopg2.ProgrammingError as e:
                                    print('error query', e)
                                    continue

                        if 'geom' in self.dbase.dbasetables[dbname]:
                            fields_to_import[-1]='geom'

                        #Deal with all the encoding problems
                        for result in returnquery:
                            str_test="'"
                            compteur=-1
                            if 'geom' in fields_to_import:
                                geometry = result[-1]
                                result = result[:-1]
                            for toto in result:
                                null=False
                                try:
                                    toto2=toto.decode('utf-8')
                                except AttributeError:
                                    toto2=str(toto)
                                except:
                                    toto2=normalize('NFKD', toto).encode('ASCII', 'ignore')

                                if toto2=='':
                                    toto2=""
                                elif toto2=='None' or toto2=='NULL':
                                    toto2='NULL'
                                    null=True
                                    str_test=str_test[:-1]
                                if null:
                                    str_test+=toto2+", '"
                                else:
                                    str_test+=toto2+"', '"
                            str_test=str_test[:-3]

                            if 'geom' in fields_to_import:
                                str_test+=", "
                                try :
                                    str_test+='ST_GeomFromText(\''+geometry+'\', '+str(self.dbase.crsnumber)+')'
                                except:
                                    str_test+="NULL"


                            #Insert
                            sql = 'INSERT INTO ' +  str(dbname) +' ('+  ','.join(fields_to_import) + ') VALUES ('+ str(str_test)+')'
                            print(sql)
                            self.dbase.query(sql)

            self.dbase.horsligne = not self.dbase.horsligne
            self.date_deconnexion = datetime.datetime.now()
            print("Mode hors ligne active : ", self.dbase.horsligne)
            return


        #Second part : reconcilliating the two databases ...............................................................................
        if self.dbase.horsligne:
            #1) Reonnect to database
            if self.dbase.offLineType=='spatialite':
                self.dbase.offLineConn, self.dbase.connSLITE = self.dbase.connSLITE , self.dbase.offLineConn
                self.dbase.offLineCursor, self.dbase.SLITEcursor = self.dbase.SLITEcursor, self.dbase.offLineCursor
            else:
                self.dbase.offLineConn, self.dbase.connPGis =self.dbase.connPGis, self.dbase.offLineConn
                self.dbase.offLineCursor, self.dbase.PGiscursor = self.dbase.PGiscursor, self.dbase.offLineCursor
                self.dbase.offLineType = 'spatialite'
                self.dbase.dbasetype='postgis'




            #2)Confront the two databases
            #Table to get the correspondances between local ids and ids in the original database
            switch_id={}

            #Table to store the date of the creation and the last modification of each object on the server where id_objet is the key
            list_dates_reperes = {}

            for order in range(10):
                for dbname in self.dbase.dbasetables:

                    switch_id[dbname]=[]
                    #First we work on the tables connected to an object : the one with an id_objet ..............................................................................
                    if self.dbase.dbasetables[dbname]['order'] == order and 'id_objet' in self.dbase.dbasetables[dbname]['fields'].keys():


                        #Gather the data on the local and online database
                        print("Export de la table : "+dbname)
                        fields_to_import=self.dbase.dbasetables[dbname]['fields'].keys()
                        if 'geom' in self.dbase.dbasetables[dbname]:
                            fields_to_import+=['ST_AsText(geom)']


                        #Get the data of the table in both database
                        sql = 'SELECT '+  ','.join(fields_to_import) + ' FROM '+ str(dbname) + ' WHERE datecreation > \'' + str(self.dbase.date_deconnexion.strftime("%Y-%m-%d %H:%M:%S")) + '\' OR datemodification > \'' + str(self.dbase.date_deconnexion.strftime("%Y-%m-%d %H:%M:%S"))+'\''


                        print(fields_to_import)
                        print(sql)

                        #Run query
                        try:
                            query = self.dbase.offLineCursor.execute(sql)
                            local_data = list(query)
                            self.dbase.offLineConn.commit()
                        except OperationalError as e:
                            print('error query', e)
                            return None

                        #We run the same query on the orginial database
                        original_data = self.dbase.query(sql)


                        if 'geom' in self.dbase.dbasetables[dbname]:
                            #Rename the last field from 'ST_AsText(geom) to geom
                            fields_to_import[-1]='geom'



                        #Store the list of the dates of creation on the local db and date of modification on the server.
                        #We compare date createion on the local databse (when the base was created or after) with date modification on the central database (last update of the true db)
                        if dbname == 'Objet':

                            for item in local_data:
                                id_local=item[list(self.dbase.dbasetables[dbname]['fields'].keys()).index('id_objet')]
                                if item[list(self.dbase.dbasetables[dbname]['fields'].keys()).index('datecreation')] == None or item[list(self.dbase.dbasetables[dbname]['fields'].keys()).index('datecreation')] == 'NULL':
                                    list_dates_reperes[id_local]=[None]
                                else:
                                    try:
                                        list_dates_reperes[id_local]=[datetime.datetime.strptime(item[list(self.dbase.dbasetables[dbname]['fields'].keys()).index('datecreation')], '%Y-%m-%dT%H:%M:%S')]
                                    except:
                                        list_dates_reperes[id_local]=[datetime.datetime.strptime(item[list(self.dbase.dbasetables[dbname]['fields'].keys()).index('datecreation')], '%Y-%m-%d')]

                            for original in original_data:
                                id_original=original[list(self.dbase.dbasetables[dbname]['fields'].keys()).index('id_objet')]
                                try :
                                    if original[list(self.dbase.dbasetables[dbname]['fields'].keys()).index('datemodification')]==None or original[list(self.dbase.dbasetables[dbname]['fields'].keys()).index('datemodification')]=='NULL':
                                        list_dates_reperes[id_original]+=[None]
                                    else:
                                        try :
                                            list_dates_reperes[id_original]+=[datetime.datetime.strptime(original[list(self.dbase.dbasetables[dbname]['fields'].keys()).index('datemodification')], '%Y-%m-%dT%H:%M:%S')]
                                        except:
                                            list_dates_reperes[id_original]+=[datetime.datetime.strptime(original[list(self.dbase.dbasetables[dbname]['fields'].keys()).index('datemodification')], '%Y-%m-%d')]
                                except : #The item doesn't exist in the local version
                                    list_dates_reperes[id_original]=[None]
                                    if original[list(self.dbase.dbasetables[dbname]['fields'].keys()).index('datemodification')]==None or original[list(self.dbase.dbasetables[dbname]['fields'].keys()).index('datemodification')]=='NULL':
                                        list_dates_reperes[id_original]+=[None]
                                    else:
                                        try :
                                            list_dates_reperes[id_original]+=[datetime.datetime.strptime(original[list(self.dbase.dbasetables[dbname]['fields'].keys()).index('datemodification')], '%Y-%m-%dT%H:%M:%S')]
                                        except:
                                            list_dates_reperes[id_original]+=[datetime.datetime.strptime(original[list(self.dbase.dbasetables[dbname]['fields'].keys()).index('datemodification')], '%Y-%m-%d')]





                        #Make sure we update the foreign key used by using the switch table
                        for item in local_data :
                            print('item : '+str(item))
                            pos=0
                            #Get the proper id to use when updating the database
                            for field in self.dbase.dbasetables[dbname]['fields'].keys() :
                                pos+=1

                                if 'lk_' in field or 'id_' in field:
                                    field = field[3:].lower()

                                if field in switch_id :
                                    for tuple_coresp in switch_id[field] :
                                        if not item[pos]=='NULL' and not item[pos]==None:
                                            try:
                                                if tuple_coresp[0]==int(item[pos]):
                                                    item[pos]=tuple_coresp[1]
                                                    break
                                            except:
                                                pass
                                        else:
                                            item[pos]='NULL'



                        #Get the output to send back to the database by recreating the request
                            str_test="'"
                            if 'geom' in fields_to_import:
                                geometry = item[-1]
                                item = item[:-1]

                            for toto in item :
                                null=False
                                try:
                                    toto2=toto.decode('utf-8')
                                except AttributeError:
                                    toto2=str(toto)
                                except:
                                    toto2=normalize('NFKD', toto).encode('ASCII', 'ignore')
                                if toto2=='' or toto2=="'''" or toto2=="'":
                                    toto2=""
                                elif toto2=='None' or toto2=='NULL':
                                    toto2='NULL'
                                    null=True
                                    str_test=str_test[:-1]
                                if null:
                                    str_test+=toto2+", '"
                                else:
                                    str_test+=toto2+"', '"
                            output=str(str_test[:-3])

                            if 'geom' in fields_to_import:
                                output+=", "
                                try :
                                    output+='ST_GeomFromText(\''+geometry+'\', '+str(self.dbase.crsnumber)+')'
                                except:
                                    output+="NULL"

                            print('output : '+ output)





                            id_local = item[self.dbase.dbasetables[dbname]['fields'].keys().index('id_objet')]



                            #Is it a new item ? test : date de creation > date de début offline
                            nouveau=False
                            no_id=False
                            try :


                                #We deal with the exceptions
                                if id_local=='NULL' or id_local == None:
                                    nouveau=False
                                    no_id = True
                                    print('id_local null')
                                elif list_dates_reperes[id_local][0]==None or list_dates_reperes[id_local][0]=='NULL':
                                    nouveau=True
                                else:


                                    #The true test
                                    nouveau = list_dates_reperes[id_local][0]>self.dbase.date_deconnexion


                            #Other exceptions
                            except KeyError as e:
                                print(e, list_dates_reperes)
                                return
                                nouveau = False
                                no_id=True


                            #If it is a new item, we add it to the database online
                            if nouveau:

                                sql = 'INSERT INTO ' +  str(dbname) +' ('+  ','.join(fields_to_import) + ') VALUES ('+ str(output) + ') RETURNING id_'+str(dbname)
                                id_res= self.dbase.query(sql)
                                print('nouveau, sql : '+sql)




                                #Add the new id fit in a tuple : We make sure we get the id online of the newly created item
                                switch_id[dbname]+=[(item[list(self.dbase.dbasetables[dbname]['fields'].keys()).index('id_'+str(dbname).lower())],id_res)]




                            #Else : the data has been modified on the local version of the database
                            else :
                                #More exceptions ...
                                if not original_data==[]:
                                    if no_id :
                                        print('pad d\'id local')
                                        pass
                                    else:


                                        if list_dates_reperes[id_local][1]==None or list_dates_reperes[id_local][1]=='NULL':
                                            non_modifie = True
                                        else:


                                            #Was the item modified while offline ? The test is here
                                            non_modifie = list_dates_reperes[id_local][1]<self.dbase.date_deconnexion



                                        #If last modification on the server is before the deconnection -> inject
                                        if non_modifie:

                                            #Construct the UPDATE request
                                            sql = 'UPDATE '+ str(dbname)+ ' SET '
                                            output=output[output.index(','):]
                                            for field in fields_to_import:
                                                if field==('id_'+dbname.lower()):
                                                    output=output[output.index(',')+1:]
                                                    pass
                                                elif field=='geom':
                                                    sql+="geom ="+output
                                                else:
                                                    output=str(output)
                                                    try :
                                                        sql += str(field)+' ='+ output[:output.index(',')]+', '
                                                        output=output[output.index(',')+1:]
                                                    except:
                                                        sql += str(field)+' ='+ output

                                            sql += ' WHERE id_'+str(dbname)+' = ' + str(id_local)
                                            print('update car non modifié, output et sql :'+output, sql)
                                            self.dbase.query(sql)



                                        #If last modification on the server is after the deconnection -> give the choice to the user
                                        else :
                                            #User has to choose the data to keep
                                            #Get the item version from the server to compare. Id should be the same as it was created before the deconection
                                            original = None
                                            for item_online in original_data:
                                                if item_online[list(self.dbase.dbasetables[dbname]['fields'].keys()).index('id_objet')] == id_local:
                                                    original=item_online
                                                    print(original, item)
                                                    break



                                            #3)Correct the conflict
                                            #Ask the user what to do
                                            print('conflit')
                                            ecrase = ConflitHorsLigne(item, original)




                                            #If the user wants to erase the data online
                                            if ecrase :
                                                #Construct the UPDATE request
                                                sql = 'UPDATE '+ str(dbname)+ ' SET '
                                                output=output[output.index(','):]
                                                for field in fields_to_import:
                                                    if field==('id_'+dbname.lower()):
                                                        output=output[output.index(',')+1:]
                                                        pass
                                                    elif field=='geom':
                                                        sql+="geom ="+output
                                                    else:
                                                        output=str(output)
                                                        print('output, sql :'+ output, sql)
                                                        try :
                                                            sql += str(field)+' ='+ output[:output.index(',')]+', '
                                                            output=output[output.index(',')+1:]
                                                        except:
                                                            sql += str(field)+' ='+ output

                                                sql += ' WHERE id_'+str(dbname)+' = ' + str(id_local)
                                                print('conflit, final :'+output, sql)
                                                self.dbase.query(sql)





                    #Deal with the tc tables
                    elif self.dbase.dbasetables[dbname]['order'] == order and 'id_tcobjet' in self.dbase.dbasetables[dbname]['fields'].keys():
                        print("Export de la table : "+dbname)
                        fields_to_import=self.dbase.dbasetables[dbname]['fields'].keys()

                        #Une tc ne sera pas modifiee, au mieux on ajoute des choses dedans
                        #We select the data
                        sql = 'SELECT '+  ','.join(fields_to_import) + ' FROM '+ str(dbname)
                        print(sql)

                        try:
                            query = self.dbase.offLineCursor.execute(sql)
                            local_data = list(query)
                            self.dbase.offLineConn.commit()
                        except OperationalError as e:
                            print('error query', e)
                            return None

                        original_data = self.dbase.query(sql)




                        #compare the datasets
                        for item in local_data :
                            id_item=item[list(self.dbase.dbasetables[dbname]['fields'].keys()).index('id_'+dbname.lower())]
                            print('item : '+str(item))


                            #Get the proper id to use when updating the database
                            pos=0
                            for field in self.dbase.dbasetables[dbname]['fields'].keys() :
                                pos+=1

                                if 'id_tc' in field:
                                    field = field[5:].lower()

                                if field in switch_id :
                                    for tuple_coresp in switch_id[field] :
                                        if not item[pos]=='NULL' and not item[pos]==None:
                                            try:
                                                if tuple_coresp[0]==int(item[pos]):
                                                    item[pos]=tuple_coresp[1]
                                                    break
                                            except:
                                                pass



                            new=True
                            for local in original_data:
                                id_local=local[list(self.dbase.dbasetables[dbname]['fields'].keys()).index('id_'+dbname.lower())]
                                if id_local==id_item:
                                    new = False
                                    break
                            if new :
                                output="'"
                                for value in item :
                                    output += str(value)
                                    str_test+=toto2+"', '"

                                output=str(str_test[:-3])
                                print('output : '+ output)

                                sql = 'INSERT INTO ' +  str(dbname) +' ('+  ','.join(fields_to_import) + ') VALUES ('+ str(output) + ') RETURNING id_'+str(dbname).lower()
                                id_res= self.dbase.query(sql)
                                print('tc_new, sql : '+sql)

                                switch_id[dbname]+=[(item[list(self.dbase.dbasetables[dbname]['fields'].keys()).index('id_'+str(dbname).lower())],id_res)]



            #4) Copy the static files ....................................................................
            local_folder='../local/local_data'
            try :
                for file in os.listdir(local_folder):
                    shutil.copyfile(file,self.dbase.imagedirectory)
            except:
                print('no folder to export the ressources, check imagedirectory')

            self.dbase.horsligne = not self.dbase.horsligne
            self.dbase.offLineConn = None
            self.dbase.offLineCursor = None
            self.dbase.offLineType = None

            return

    def importDBase(self, slfile=None, crs=None, typemetier=None, dbasetype='spatialite',
                    dbname=None, schema=None, user=None, host='localhost', port=None, password=None,    # postgis
                    dbaseressourcesdirectory=None, typeimport='nouvelle'):

        if self.sender() is not None:
            actionname = self.sender().objectName()
            #print(actionname,slfile )

            if actionname == 'actionImporter_et_ajouter_la_base':
                typeimport = "nouvelle"
            elif actionname == 'actionImporter_et_mettre_jour_la_base':
                typeimport = "import_terrain"

        if (slfile is not None and not isinstance(slfile, bool)) or dbname is not None:
            pass
        else:

            self.newDBDialog.comboBox_type.setEnabled(False)
            self.newDBDialog.exec_()
            dbasetype, type, variante = self.newDBDialog.dialogIsFinished()
            self.newDBDialog.comboBox_type.setEnabled(True)
            if dbasetype is None and type is None:
                return

            if dbasetype == 'postgis':
                resdir = self.qfiledlg.getExistingDirectory(self, "Selectionner le reperoire des ressources")
                if resdir:
                    dbaseressourcesdirectory = str(resdir)
                else:
                    return
            else:
                resdir = None

            # create database
            if dbasetype == 'spatialite':
                if sys.version_info.major == 2:
                    spatialitefile, extension = self.qfiledlg.getOpenFileNameAndFilter(None, 'Export vers', '',
                                                                                   'Spatialite (*.sqlite)', '')
                elif sys.version_info.major == 3:
                    spatialitefile, extension = self.qfiledlg.getOpenFileName(None, 'Export vers', '',
                                                                                   'Spatialite (*.sqlite)', '')
                if spatialitefile:
                    slfile = spatialitefile


            elif dbasetype == 'postgis':
                self.connDialog.exec_()
                adresse, port, nom, schema, user, password = self.connDialog.dialogIsFinished()
                if adresse is not None and port is not None and nom is not None and user is not None and password is not None:
                    databaseexists, schemaexists = self.dbase.checkIfPGShcemaExists(host=adresse, dbname=nom, schema=schema,
                                                                                    user=user, password=password)
                    if False:
                        if  schemaexists :
                            print('schema existe deja - choisir un autre schema')
                        else:
                            self.normalMessage('Creation de la base de donnees...')
                            QApplication.processEvents()

                            self.dbase.createDbase(crs=crsnumber, type=type, dbasetype='postgis', dbname=nom, schema=schema,
                                                   user=user, host=adresse, password=password, dbaseressourcesdirectory=resdir,
                                                   port=port)

        self.importexportdbase = DBaseParser(self.canvas)
        self.importexportdbase.loadQgisVectorLayers(file=slfile, dbasetype=dbasetype, host=host, port=None, dbname=None, schema=None, user=None, password=None)

        self.dbase.importDbase(self.importexportdbase,typeimport )




    def exportDBase(self):
        if self.sender() is not None:
            actionname = self.sender().objectName()
            # print(actionname )
        if sys.version_info.major == 2:
            spatialitefile = self.qfiledlg.getSaveFileName(self, 'Lamia nouveau', '', '*.sqlite')
        elif sys.version_info.major == 3:
            spatialitefile, fileext = self.qfiledlg.getSaveFileName(self, 'Lamia nouveau', '', '*.sqlite')

        if spatialitefile:
            slfile = spatialitefile

            self.dbase.exportDbase(slfile)





    def setLoadingProgressBar(self, progressbar, val):
        if progressbar is not None:
            progressbar.setValue(val)
        else:
            logger.info('Chargement %d', val )
        QApplication.processEvents()



    def reinitDBase(self):
        #clean eventualy previous dbase
        self.MaintreeWidget.clear()
        self.ElemtreeWidget.clear()
        self.menuOutils.clear()

        if self.dbase.dbasetype is not None:
            if False:
                root = qgis.core.QgsProject.instance().layerTreeRoot()
                #root.addGroup('Lamia')
                if self.dbasetype == "spatialite":
                    groupname = 'Lamia_' + os.path.basename(self.spatialitefile)
                elif self.dbasetype == "postgis":
                    groupname = 'Lamia_' + self.pgschema

                lamialegendgroup =  root.findGroup(groupname)

                if lamialegendgroup is not None:
                    lamialegendgroup.removeAllChildren()

            if self.qgislegendnode is not None:
                self.qgislegendnode.removeAllChildren()
                root = qgis.core.QgsProject.instance().layerTreeRoot()
                root.removeChildNode(self.qgislegendnode)

        self.dbase.reInitDBase()

        self.setVisualMode(reset=True)
        self.desktopuiloaded = False

        if True:
            self.uifields = []
            self.uidesktop = []
            self.uipostpro = []
            self.menuclasses = []

            self.tools = []
            self.menutools = []



        if False:
            if self.dbase is not None:
                self.dbase.reInitDBase()
            self.MaintreeWidget.clear()
            self.ElemtreeWidget.clear()
            # self.dbase = DBaseParser(self.canvas)
            self.__init__(self.canvas)


    def openTableFieldDialog(self):
        self.tablefielddialog.dbase = self.dbase
        self.tablefielddialog.update()
        if self.dbase.qgsiface is not None:
            self.tablefielddialog.setWindowModality(QtCore.Qt.NonModal)
            self.tablefielddialog.show()
        else:
            self.tablefielddialog.exec_()








    def tr(self, message):
        return QCoreApplication.translate('InspectiondigueWindowWidget', message)


class LoadUiField(QtCore.QObject):

    finished = QtCore.pyqtSignal()

    def __init__(self,dialog ):
        QtCore.QObject.__init__(self)
        self.dialog = dialog
        self.dbase = dialog.dbase
        self.uifields = dialog.uifields
        self.ElemtreeWidget = dialog.ElemtreeWidget
        self.gpsutil =dialog.gpsutil

    def loadUiField(self):
        timestart = self.dbase.getTimeNow()

        if debugtime: logger.debug(' start %.3f', self.dbase.getTimeNow()  - timestart)

        if self.dbase.qgsiface is not None:
            # if not self.dbase.standalone:
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

        i = 0
        for uifield in self.uifields:
            if debugtime: logger.debug(' start %s %.3f', uifield.dbasetablename, self.dbase.getTimeNow()  - timestart)
            # try:
            dbasename = uifield.dbasetablename
            # print(dbasename)
            self.dbase.dbasetables[dbasename]['widget'] = uifield(dbase=self.dbase,
                                                                  dialog=self,
                                                                  linkedtreewidget=self.ElemtreeWidget,
                                                                  gpsutil=self.gpsutil)
            if debugtime: logger.debug(' end %s %.3f', uifield.dbasetablename, self.dbase.getTimeNow()  - timestart)
            i += 1
            self.setLoadingProgressBar(progress, i)
            # except Exception as e:
            #     print('error load', e)

        if progress is not None: self.dbase.qgsiface.messageBar().clearWidgets()
        self.finished.emit()



