# -*- coding: utf-8 -*-

# qgis pyqt import
from qgis.PyQt import QtGui, uic, QtCore
from unicodedata import normalize
from qgis.PyQt.QtCore import pyqtSignal
try:
    from qgis.PyQt.QtGui import (QDockWidget, QMainWindow, QFileDialog, QLabel, QInputDialog,
                                 QComboBox,QTableWidgetItem,QProgressBar,QApplication,QToolBar,
                                 QPushButton,QToolButton,QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QDockWidget, QMainWindow, QFileDialog, QLabel, QInputDialog,
                                     QComboBox,QTableWidgetItem, QProgressBar,QApplication,QToolBar,
                                     QPushButton,QToolButton,QWidget)

# other libs import
import os
import qgis
import shutil
import datetime
import sys
import logging
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
from .InspectionDigue_impression_rapport import ImpressionRapportDialog
from .InspectionDigue_exportShapefile import ExportShapefileDialog
from .InspectionDigue_Import import ImportObjetDialog
from .Lamia_numpad import NumPadDialog
from .Lamia_iconsize import IconSizeDialog

from .InspectionDigue_newDB import newDBDialog
from .InspectionDigue_getDate import getDateDialog


from ..toolgeneral.InspectionDigue_rapport import printPDFWorker
from ..toolgeneral.InspectionDigue_exportshp import exportShapefileWorker
from ..toolgeneral.InspectionDigue_import import ImportObjectWorker

import time

from ..gps.GPSutil import GpsUtil
from ..maptool.mapTools import mapToolCapture


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
        # the pick maptool
        # self.pointEmitter = None
        self.pointEmitter = qgis.gui.QgsMapToolEmitPoint(self.canvas)
        # The DBase parser
        self.dbase = DBaseParser(self.canvas)
        # The GPS util
        self.gpsutil = GpsUtil()
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
        #iconsize
        self.iconsizedialog = IconSizeDialog(self)
        # for printing reports
        self.printrapportdialog = ImpressionRapportDialog()
        self.exportshapefiledialog = ExportShapefileDialog()
        self.importobjetdialog =ImportObjetDialog()
        #ui classes
        self.uifields = []
        self.uidesktop = []
        self.uipostpro = []
        self.desktopuiloaded = False

        # icon size changed
        if False and self.dbase.qgsiface is not None:
            mainwindow = self.dbase.qgsiface.mainWindow()
            toolbars = mainwindow.findChildren(QToolBar)
            toolbars[0].iconSizeChanged.connect(self.themechanged)
            #self.dbase.qgsiface.currentThemeChanged.connect(self.themechanged)


        if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
            self.crsselector = qgis.gui.QgsGenericProjectionSelector()
        else:
            self.crsselector = qgis.gui.QgsProjectionSelectionDialog()
        self.dockwgt = dockwgt

        # the qgis editing maptool
        self.cadwdg = qgis.gui.QgsAdvancedDigitizingDockWidget(self.canvas)
        if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
            self.mtoolpoint = mapToolCapture(self.canvas, self.cadwdg,
                                             qgis.gui.QgsMapToolAdvancedDigitizing.CapturePoint)
            self.mtoolline = mapToolCapture(self.canvas, self.cadwdg,
                                            qgis.gui.QgsMapToolAdvancedDigitizing.CaptureLine)
            self.mtoolpolygon = mapToolCapture(self.canvas, self.cadwdg,
                                               qgis.gui.QgsMapToolAdvancedDigitizing.CapturePolygon)
        else:
            self.mtoolpoint = mapToolCapture(self.canvas, self.cadwdg,
                                             qgis.gui.QgsMapToolCapture.CapturePoint)
            self.mtoolline = mapToolCapture(self.canvas, self.cadwdg,
                                            qgis.gui.QgsMapToolCapture.CaptureLine)
            self.mtoolpolygon = mapToolCapture(self.canvas, self.cadwdg,
                                               qgis.gui.QgsMapToolCapture.CapturePolygon)

        self.currentprestationlabel = QLabel('Prestation inactif')
        self.statusBar().addWidget(self.currentprestationlabel, 1)

        self.GPSlabel = QLabel('GPS non connecte')
        self.statusBar().addWidget(self.GPSlabel)

        if debug: logging.getLogger('Lamia').debug('step1')

        # ***************************************************************
        # ******************   Actions  ****************************
        # ***************************************************************
        self.MaintreeWidget.expandAll()
        self.actionModeTerrain.setChecked(True)

        # ***************************************************************
        # ******************   Signals ****************************
        # ***************************************************************
        #qgis signals
        if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
            self.canvas.destinationCrsChanged.connect(self.dbase.updateQgsCoordinateTransformFromLayerToCanvas)
        else:
            qgis.core.QgsProject.instance().crsChanged.connect(self.dbase.updateQgsCoordinateTransformFromLayerToCanvas)
        # DBase signals
        self.dbase.recentDBaseChanged.connect(self.updateRecentDBaseMenu)
        self.dbase.dBaseLoaded.connect(self.DBaseLoaded)
        self.dbase.errorMessage.connect(self.errorMessage)
        # QT signals
        self.actionNouvelle_base.triggered.connect(self.newDbase)
        self.actionSpatialite.triggered.connect(self.loadSLDbase)
        self.actionPostgis.triggered.connect(self.loadPGDbase)
        self.actionAide.triggered.connect(self.openHelp)
        self.menuBases_recentes.triggered.connect(self.openFileFromMenu)
        self.actionExporter_base.triggered.connect(self.exportBase)
        self.actionImprimer_rapport.triggered.connect(self.printRapport)
        self.actionExport_shapefile.triggered.connect(self.exportShapefile)
        self.actionImport.triggered.connect(self.importObjet)
        self.actionVersion.triggered.connect(self.setVersion)

        if self.dbase.dbasetype == 'postgis':
            self.actionMode_hors_ligne_Reconnexion.setEnabled(True)
        else:
            #self.actionMode_hors_ligne_Reconnexion.setEnabled(True)
            self.actionMode_hors_ligne_Reconnexion.setEnabled(True)
        self.actionMode_hors_ligne_Reconnexion.triggered.connect(self.modeHorsLigne)


        #self.pushButton_zoomFeature.clicked.connect(self.zoomToFeature)
        self.pushButton_selectfeat.clicked.connect(self.selectFeature)
        self.action_Repertoire_photo.triggered.connect(self.setImageDir)
        #self.actionDate_de_travail.triggered.connect(self.setWorkingDate)
        self.toolButton_date.clicked.connect(self.setWorkingDate)
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
        self.updateRecentDBaseMenu()
        self.splitter_2.setSizes([80, 200])
        # camera path
        if QtCore.QSettings().value("InspectionDigue/picturepath") is not None:
            self.dbase.imagedirectory = os.path.normpath(QtCore.QSettings().value("InspectionDigue/picturepath"))
        else:
            self.dbase.imagedirectory = None

        if debug: logging.getLogger('Lamia').debug('end')


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
            self.GPSlabel.setText('GPS connecte')
        else:
            self.GPSlabel.setText('GPS non connecte')


    """
    def loadTools(self, filetype=None):


        import glob, inspect, importlib

        self.unloadTools()
        if False :
            #self.normalMessage('Loading tools')
            path = os.path.join(os.path.dirname(__file__), '..', 'tools')
            modules = glob.glob(path+"/*.py")
            __all__ = [os.path.basename(f)[:-3] for f in modules if os.path.isfile(f)]
            for x in __all__:
                #print('file',x)
                moduletemp = importlib.import_module('.' + str(x), 'InspectionDigue.tools')
                for name, obj in inspect.getmembers(moduletemp, inspect.isclass):
                    if moduletemp.__name__ == obj.__module__:
                        try:
                            #print('obj',self.tools,obj, self.dbase,self )
                            tempobjt = obj(self.dbase, self)
                            if tempobjt.CAT is not None:
                                self.tools.append(tempobjt)

                        except Exception as e:
                            #self.errorMessage('Error importing tool - ' + str(x) + ' : ' + str(e))
                            print('moduletemp',e)



                if False:
                    try:
                        moduletemp = importlib.import_module('.' + str(x), 'InspectionDigue.tools')
                        for name, obj in inspect.getmembers(moduletemp, inspect.isclass):
                            if moduletemp.__name__ == obj.__module__:

                                print('obj',self.tools,obj, self.dbase,self )
                                self.tools.append(obj(self.dbase, self, self.dbase.qgsiface.mapCanvas() ))


                                if False:

                                    try:  # case obj has NAME
                                        istool = obj.NAME
                                        #print(obj, istool)
                                        if filetype is None and istool is not None:

                                            print('obj',self.tools,obj, self.dbase,self )
                                            self.tools.append(obj(self.dbase, self))

                                        else:   # specific software tool
                                            try:    # case obj has SOFTWARE
                                                print('obj',x,obj.CAT,obj.NAME)
                                                if len(obj.SOFTWARE) > 0 and filetype in obj.SOFTWARE:
                                                    try:
                                                        #self.tools.append(obj(self.meshlayer, self))
                                                        self.tools.append(obj(self.dbase, self))
                                                    except Exception as e:
                                                        #self.errorMessage(istool + ' : ' + str(e))
                                                        print('soft',e)
                                                elif len(obj.SOFTWARE) == 0:
                                                    try:
                                                        #self.tools.append(obj(self.meshlayer, self))
                                                        self.tools.append(obj(self.dbase, self))
                                                    except Exception as e:
                                                        #self.errorMessage(istool + ' : ' + str(e))
                                                        print('nosoft',e)
                                            except:
                                                pass
                                    except Exception as e:
                                        pass
                    except Exception as e:
                        #self.errorMessage('Error importing tool - ' + str(x) + ' : ' + str(e))
                        print('moduletemp',e)
            #self.normalMessage('Tools loaded')

        if False:
            if  False:
                from ..tools.InspectionDigue_troncons_tool import tronconsTool
                self.tools.append(tronconsTool(self.dbase, self, self.ElemtreeWidget,  parent=self))
            if False:
                from ..tools.InspectionDigue_desordres_tool import desordresTool
                self.tools.append(desordresTool(self.dbase, self, self.ElemtreeWidget,parent = self) )
            if False:
                from ..tools.InspectionDigue_desordres_obs_tool import desordresobsTool
                self.tools.append(desordresobsTool(self.dbase, self, self.ElemtreeWidget,parent=self))
            if False:
                from ..tools.InspectionDigue_photographies_tool import photographiesTool
                self.tools.append(photographiesTool(self.dbase, self, self.ElemtreeWidget,parent=self))
            if False:
                from ..tools.InspectionDigue_reseaux_spe_tool import reseauxspeTool
                self.tools.append(reseauxspeTool(self.dbase, self, self.ElemtreeWidget,parent=self))
            if False:
                from ..tools.InspectionDigue_reseaux_tool import reseauxTool
                self.tools.append(reseauxTool(self.dbase, self, self.ElemtreeWidget,parent=self))
            if True:
                from ..tools.InspectionDigue_structures_tool import structuresTool
                #self.tools.append(structuresTool(self.dbase, self, self.ElemtreeWidget,parent=self))
                self.tools.append(structuresTool(self.dbase, self, self.ElemtreeWidget))

            if True:
                from ..tools.InspectionDigue_photos_tool import PhotosTool
                #self.tools.append(structuresTool(self.dbase, self, self.ElemtreeWidget,parent=self))
                self.tools.append(PhotosTool(self.dbase, self, self.ElemtreeWidget))

            if False:
                try:
                    from ..tools.InspectionDigue_analyse import AnalyseDesordresTool
                    self.tools.append(AnalyseDesordresTool(self.dbase, self, self.ElemtreeWidget,parent=self))
                except:
                    print("analyse non charge")

            for tool in self.tools:
                #pass
                tool.loadWidgetinMainTree()

    """

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

    def setVisualMode(self):
        """
        pass
        """
        # print(self.sender.objectName())
        actionname = self.sender().objectName()
        if actionname == 'actionModeTerrain':
            self.dbase.visualmode = 0
            self.actionModeTerrain.setChecked(True)
            self.actionTTC.setChecked(False)
            self.actionModeExpert.setChecked(False)
            self.actionPosttraitement.setChecked(False)

        elif actionname == 'actionTTC':
            self.dbase.visualmode = 1
            self.actionModeTerrain.setChecked(False)
            self.actionTTC.setChecked(True)
            self.actionModeExpert.setChecked(False)
            self.actionPosttraitement.setChecked(False)
            if not self.desktopuiloaded:
                self.loadUiDesktop()

        elif actionname == 'actionModeExpert':
            self.dbase.visualmode = 2
            self.actionModeTerrain.setChecked(False)
            self.actionTTC.setChecked(False)
            self.actionModeExpert.setChecked(True)
            self.actionPosttraitement.setChecked(False)

        elif actionname == 'actionPosttraitement':
            self.dbase.visualmode = 4
            self.actionPosttraitement.setChecked(True)
            self.actionModeTerrain.setChecked(False)
            self.actionTTC.setChecked(False)
            self.actionModeExpert.setChecked(False)

        self.applyVisualMode()

    def applyVisualMode(self):
        if self.dbase.dbasetables is not None:
            for tablename in self.dbase.dbasetables.keys():
                if 'widget' in self.dbase.dbasetables[tablename].keys():
                    if isinstance(self.dbase.dbasetables[tablename]['widget'], list):
                        for wdg in self.dbase.dbasetables[tablename]['widget']:
                            wdg.changePropertiesWidget()
                    else:
                        self.dbase.dbasetables[tablename]['widget'].changePropertiesWidget()
            for tool in self.tools:
                tool.changePropertiesWidget()

    def reinitCurrentPrestation(self):
        if self.dbase is not None:
            self.dbase.currentprestationid = None
            self.currentprestationlabel.setText('Prestation inactif')

    def setHauteurPerche(self):
        num, ok = QInputDialog.getDouble(self,
                                         "Hauteur de perche",
                                         "Rentrer la hauteur de perche GPS",
                                         self.dbase.hauteurperche)
        if ok:
            self.dbase.hauteurperche = num

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
        self.newDBDialog.exec_()
        dbtype, type = self.newDBDialog.dialogIsFinished()
        if dbtype is None and type is None:
            return
        # crs selector
        self.crsselector.exec_()
        if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
            crs = self.crsselector.selectedAuthId()
            crsnumber = int(crs.split(':')[1])
        else:
            crs = self.crsselector.crs().authid()
            crsnumber = int(crs.split(':')[1])
        # ressources directory
        if dbtype == 'postgis':
            resdir = self.qfiledlg.getExistingDirectory(self, "Selectionner le reperoire des ressources")
            if resdir:
                resdir = str(resdir)
            else:
                return
        else:
            resdir = None

        # dialogs finished - reinit base
        self.dbase.reInitDBase()
        # create database
        if dbtype == 'spatialite':
            spatialitefile = self.qfiledlg.getSaveFileName(self, 'InspectionDigue nouveau', '', '*.sqlite')
            if spatialitefile:
                originalfile = os.path.join(os.path.dirname(__file__), '..', 'DBASE', 'DBase_ind0.sqlite')
                shutil.copyfile(originalfile, spatialitefile)
                self.dbase.createDbase(file=spatialitefile, crs=crsnumber, type=type, dbasetype='spatialite',
                                       dbaseressourcesdirectory = resdir)
        elif dbtype == 'postgis':
            self.connDialog.exec_()
            adresse, port, nom, schema, user, password = self.connDialog.dialogIsFinished()
            if adresse is not None and port is not None and nom is not None and user is not None and password is not None:
                databaseexists, schemaexists = self.dbase.checkIfPGShcemaExists(host=adresse, dbname=nom, schema=schema,
                                                                                user=user, password=password)
                if  schemaexists :
                    print('schema existe deja - choisir un autre schema')
                else:
                    self.dbase.createDbase(crs=crsnumber, type=type, dbasetype='postgis', dbname=nom, schema=schema,
                                           user=user, host=adresse, password=password, dbaseressourcesdirectory=resdir,
                                           port=port)

    def openFileFromMenu(self, action):
        """
        pass
        """
        filetoopen = action.text()
        if len(filetoopen.split(';')) == 1:
            self.dbase.loadQgisVectorLayers(filetoopen)
        else:
            db, user, password = filetoopen.split(';')
            nom, schema = db.split('@')[0].split('.')
            adresse, port = db.split('@')[1].split(':')
            self.dbase.loadQgisVectorLayers(dbasetype='postgis', host=adresse, port=int(port), dbname=nom,
                                            schema=schema, user=user, password=password)

    #
    def loadSLDbase(self):
        if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
            file, extension = self.qfiledlg.getOpenFileNameAndFilter(None, 'Choose the file', '',
                                                                     'Spatialite (*.sqlite)', '')
        else:
            file , extension= self.qfiledlg.getOpenFileName(None, 'Choose the file', '',
                                                                     'Spatialite (*.sqlite)', '')
            print(file)
        if file:
            self.dbase.loadQgisVectorLayers(file)

    def loadPGDbase(self):
        self.connDialog = ConnexionPGDialog()
        self.connDialog.exec_()
        adresse, port, nom, schema, user, password = self.connDialog.dialogIsFinished()
        if adresse is not None and port is not None and nom is not None and user is not None and password is not None:
            self.dbase.loadQgisVectorLayers(file=None, dbasetype='postgis', host=adresse, port=port, dbname=nom,
                                            schema=schema, user=user, password=password)

    def updateRecentDBaseMenu(self):
        self.menuBases_recentes.triggered.disconnect(self.openFileFromMenu)
        self.menuBases_recentes.clear()
        for telem in self.dbase.recentsdbase:
            self.menuBases_recentes.addAction(telem)
        self.menuBases_recentes.triggered.connect(self.openFileFromMenu)

    def DBaseLoaded(self):

        debug = False
        if debug: logging.getLogger('Lamia').debug('start')


        if False:
            qgis.utils.uninstallErrorHook()  # for standart output
            qgis.utils.uninstallErrorHook()  # for standart output
            sys.excepthook = sys.__excepthook__
            print(sys.excepthook)
            print(sys.stderr)
            'okok'.decode('utf-8')
        self.gpsutil.setCRS(self.dbase.qgiscrs)
        self.dbase.updateWorkingDate()
        timestart = time.clock()


        if debugtime: logger.debug(' progress bar done %.3f', time.clock() - timestart)


        # ************************** LOAD LAYERS AND STYLES ***********************************

        root = qgis.core.QgsProject.instance().layerTreeRoot()
        #root.addGroup('Lamia')
        lamialegendgroup =  root.findGroup('Lamia')
        if lamialegendgroup is None:
            lamialegendgroup = root.insertGroup(0, 'Lamia')


        for tablename in self.dbase.dbasetables:
            if self.dbase.dbasetables[tablename]['showinqgis']:

                if True:
                    if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                        qgis.core.QgsMapLayerRegistry.instance().addMapLayer(self.dbase.dbasetables[tablename]['layerqgis'],
                                                                             False)
                    else:
                        qgis.core.QgsProject.instance().addMapLayer(self.dbase.dbasetables[tablename]['layerqgis'],
                                                                    False)

                lamialegendgroup.addLayer(self.dbase.dbasetables[tablename]['layerqgis'])


            else:
                if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                    qgis.core.QgsMapLayerRegistry.instance().addMapLayer(self.dbase.dbasetables[tablename]['layer'],
                                                                         False)
                else:
                    qgis.core.QgsProject.instance().addMapLayer(self.dbase.dbasetables[tablename]['layer'],
                                                                False)

            if False and 'scale' in self.dbase.dbasetables[tablename].keys():
                self.dbase.dbasetables[tablename]['layerqgis'].setScaleBasedVisibility(True)
                if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                    self.dbase.dbasetables[tablename]['layerqgis'].setMaximumScale(self.dbase.dbasetables[tablename]['scale'])
                else:
                    self.dbase.dbasetables[tablename]['layerqgis'].setMinimumScale(self.dbase.dbasetables[tablename]['scale'])


        self.loadStyle()

        # ************************** LOAD MODULES ********************************************
        if True:


            path = os.path.join(os.path.dirname(__file__), '..', 'toolprepro', self.dbase.type.lower())
            modules = glob.glob(path + "/*.py")
            __all__ = [os.path.basename(f)[:-3] for f in modules if os.path.isfile(f)]

            for x in __all__:
                if debug: logging.getLogger('Lamia').debug('x %s', x)
                if self.dbase.qgsiface is not None:
                    #   if not self.dbase.standalone:
                    exec('import Lamia.toolprepro.' + self.dbase.type.lower())
                    moduletemp = importlib.import_module('.' + str(x), 'Lamia.toolprepro.' + self.dbase.type.lower() )
                    # moduletemp = importlib.import_module('.' + str(x), 'Lamia.toolprepro.' + self.dbase.type.lower())
                    # moduletemp = importlib.import_module('.' + str(x), '..toolprepro.' + self.dbase.type.lower())
                else:
                    exec('import Lamia.Lamia.toolprepro.' + self.dbase.type.lower())
                    moduletemp = importlib.import_module('.' + str(x), 'Lamia.Lamia.toolprepro.' + self.dbase.type.lower())

                for name, obj in inspect.getmembers(moduletemp, inspect.isclass):
                    if moduletemp.__name__ == obj.__module__:
                        try:
                            if obj.LOADFIRST:
                                self.uifields.append(obj)
                            else:
                                self.uidesktop.append(obj)
                        except AttributeError:
                            pass

            if debug: logging.getLogger('Lamia').debug('step1')

            path = os.path.join(os.path.dirname(__file__), '..', 'toolpostpro')
            modules = glob.glob(path + "/*.py")
            __all__ = [os.path.basename(f)[:-3] for f in modules if os.path.isfile(f)]
            for x in __all__:
                if self.dbase.qgsiface is not None:
                    #if not self.dbase.standalone:
                    exec('import Lamia.toolpostpro')
                    moduletemp = importlib.import_module('.' + str(x), 'Lamia.toolpostpro' )
                else:
                    exec('import Lamia.Lamia.toolpostpro' )
                    moduletemp = importlib.import_module('.' + str(x), 'Lamia.Lamia.toolpostpro')
                for name, obj in inspect.getmembers(moduletemp, inspect.isclass):
                    if moduletemp.__name__ == obj.__module__:
                        try:
                            if self.dbase.type.lower() in obj.DBASES:
                                self.uipostpro.append(obj)
                        except AttributeError:
                            pass

            if False:
                print('*********** ui lodaded *************** ')
                print(self.uifields)
                print(self.uidesktop)
                print(self.uipostpro)

            self.loadUiField()



        if debugtime: logger.debug('applyVisualMode %.3f', time.clock() - timestart)


    def loadStyle(self):
        try:
            self.comboBox_style.currentIndexChanged.disconnect(self.comboStyleChanged)
        except:
            pass
        self.comboBox_style.clear()
        stylepath = os.path.join(os.path.dirname(__file__), '..','DBASE', 'style', self.dbase.type)
        # print([x[0] for x in os.walk(stylepath)])
        #print([x[1] for x in os.walk(stylepath) if len(x[1])>0])

        styledirs = [x[1] for x in os.walk(stylepath) if len(x[1])>0][0]

        self.comboBox_style.addItems(styledirs)
        self.comboBox_style.currentIndexChanged.connect(self.comboStyleChanged)
        self.comboBox_style.currentIndexChanged.emit(0)


    def comboStyleChanged(self,comboindex):
        #print('comboStyleChanged')
        #print(comboindex)

        styledir = self.comboBox_style.currentText()

        stylerep = os.path.join(os.path.dirname(__file__), '..', 'DBASE', 'style', self.dbase.type,styledir )

        #print(stylerep)

        allfiles = [x[2] for x in os.walk(stylerep)][0]
        qmlfiles = [uknfile.split('.')[0] for uknfile in allfiles if uknfile.split('.')[1] == 'qml']

        #print([x[2] for x in os.walk(stylerep)])

        #print('qml',qmlfiles)
        #print('inst', qgis.core.QgsProject.instance())

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
                        # pass
                        # qgis.utils.iface.layerTreeView().currentNode().setItemVisibilityChecked(False)
                        #qgis.utils.iface.layerTreeView().layerTreeModel().layerTreeModel().findLegendNode(self.dbase.dbasetables[dbasetablename]['layerqgis'].id()).layerNode ()
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


        # print('comboStyleChanged finished')



    def loadUiField2(self):
        self.thread = QtCore.QThread()
        self.worker = LoadUiField(self)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.loadUiField)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.finished.connect(self.thread.quit)
        self.thread.start()



    def loadUiField(self):
        timestart = time.clock()


        if debugtime: logger.debug(' start %.3f', time.clock() - timestart)

        if self.dbase.qgsiface is not None:
            #if not self.dbase.standalone:
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
            if debugtime: logger.debug(' start %s %.3f', uifield.dbasetablename, time.clock() - timestart)
            #try:
            dbasename = uifield.dbasetablename
            # print(dbasename)
            if False:
                self.dbase.dbasetables[dbasename]['widget'] = uifield(dbase = self.dbase,
                                                                         dialog = self,
                                                                         linkedtreewidget = self.ElemtreeWidget,
                                                                         gpsutil = self.gpsutil)
            else:
                self.dbase.dbasetables[dbasename]['widget'].append( uifield(dbase = self.dbase,
                                                                         dialog = self,
                                                                         linkedtreewidget = self.ElemtreeWidget,
                                                                         gpsutil = self.gpsutil) )

            if debugtime: logger.debug(' end %s %.3f', uifield.dbasetablename, time.clock() - timestart)
            i += 1
            self.setLoadingProgressBar(progress, i)
            #except Exception as e:
            #     print('error load', e)

        if progress is not None: self.dbase.qgsiface.messageBar().clearWidgets()



    """
    def loadUiDesktop(self):
        self.thread = QtCore.QThread()
        self.worker = LoadUiDesktop(self.dbase, self.uidesktop, self.uipostpro)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.loadUiDesktop)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.finished.connect(self.thread.quit)
        self.thread.start()
    """


    def loadUiDesktop(self):

        if self.dbase.qgsiface is not None:
            #if not self.dbase.standalone:
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
            progress.setMaximum(lenuifields + lenuipostpro)
        else:
            progress = None


        i = 0
        for uidesktop in self.uidesktop:
            try:
                dbasename = uidesktop.dbasetablename
                if False:
                    self.dbase.dbasetables[dbasename]['widget'] = uidesktop(dbase = self.dbase,
                                                                             dialog = self,
                                                                             linkedtreewidget = self.ElemtreeWidget,
                                                                             gpsutil = self.gpsutil)
                else:
                    self.dbase.dbasetables[dbasename]['widget'].append(uidesktop(dbase = self.dbase,
                                                                             dialog = self,
                                                                             linkedtreewidget = self.ElemtreeWidget,
                                                                             gpsutil = self.gpsutil))
                # self.dbase.dbasetables[dbasename]['widget'].initWidgets()
                i += 1
                self.setLoadingProgressBar(progress, i)

            except AttributeError:
                pass




        if False:
            for dbasename in self.dbase.dbasetables.keys():
                if 'widget' in self.dbase.dbasetables[dbasename].keys():
                    print('iniwdg', dbasename)
                    if isinstance(self.dbase.dbasetables[dbasename]['widget'], list):
                        for wdg in self.dbase.dbasetables[dbasename]['widget']:
                            wdg.initWidgets()
                    else:
                        self.dbase.dbasetables[dbasename]['widget'].initWidgets()


        for uidpostpr in self.uipostpro:

            strtoexec = ('self.' + uidpostpr.__name__.lower() + " = uidpostpr(dbase = self.dbase, dialog = self,linkedtreewidget = self.ElemtreeWidget, gpsutil = self.gpsutil)")
            # print(strtoexec)
            exec(strtoexec)
            # print('test', eval('self.' + uidpostpr.__name__.lower()))
            strtoexec = 'self.tools.append(' + 'self.' + uidpostpr.__name__.lower() + ')'
            # print(strtoexec)
            exec(strtoexec)
            # print('ok')


            if False:
                self.tools.append( uidpostpr(dbase = self.dbase,
                                             dialog = self,
                                             linkedtreewidget = self.ElemtreeWidget,
                                             gpsutil = self.gpsutil)
                               )
            i += 1
            self.setLoadingProgressBar(progress, i)


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


    def selectPickedFeature(self, point):
        # print('select',point.x(), point.y())

        if False:
            self.canvas.unsetMapTool(self.pointEmitter)
            try:
                self.pointEmitter.canvasClicked.disconnect(self.selectPickedFeature)
            except:
                pass
        # print('windowd selectPickedFeature',self.stackedWidget_main.currentIndex() )
        if self.stackedWidget_main.currentIndex() == 0:
            wdg = self.MaintabWidget.widget(0).layout().itemAt(0).widget()
            layer = wdg.dbasetable['layerqgis']
            #nearestid, dist = wdg.getNearestId(point)
            point2 = self.pointEmitter.toLayerCoordinates(wdg.dbasetable['layerqgis'], point)
            nearestpk, dist = self.dbase.getNearestId(wdg.dbasetable,
                                                      wdg.dbasetablename,
                                                      point2,
                                                      False)
            if self.dbase.revisionwork:
                feat = self.dbase.getLayerFeatureByPk(wdg.dbasetablename, nearestpk)
                featid = feat['id_' + wdg.dbasetablename]
                # print('sel',featid)
            else:
                featid = nearestpk

            itemindex = wdg.comboBox_featurelist.findText(str(featid))
            wdg.comboBox_featurelist.setCurrentIndex(itemindex)

        elif self.stackedWidget_main.currentIndex() == 1:
            wdg = self.stackedWidget_main.widget(1).layout().itemAt(0).widget()
            wdg.selectPickedFeature(point)

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
        exportfile, extension = self.qfiledlg.getOpenFileNameAndFilter(None, 'Export vers', '',
                                                                       'Spatialite (*.sqlite)', '')
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
                self.dbase.qgsiface.messageBar().pushMessage("InspectionDigue", 'Export fini', level=qgis.gui.QgsMessageBar.SUCCESS, duration=3)
            else:
                print('export fini')

    def openHelp(self):
        path = os.path.join(os.path.dirname(__file__),'..','html','index.html')
        os.startfile(path)


    def errorMessage(self, text):
        # print('eror', self.sender(),self.sender().name())
        if self.dbase.qgsiface is not None:
            #if not self.dbase.standalone:
            if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                self.dbase.qgsiface.messageBar().pushMessage("InspectionDigue", text,
                                                          level=qgis.gui.QgsMessageBar.CRITICAL, duration=3)
            else:
                self.dbase.qgsiface.messageBar().pushMessage("InspectionDigue", text,
                                                          level=qgis.core.Qgis.Critical , duration=3)
        else:
            print('ErrorMessage', text)

    def warningMessage(self, text):
        if self.dbase.qgsiface is not None:
            # if not self.dbase.standalone:
            if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                self.dbase.qgsiface.messageBar().pushMessage("InspectionDigue", text,
                                                          level=qgis.gui.QgsMessageBar.WARNING, duration=3)
            else:
                self.dbase.qgsiface.messageBar().pushMessage("InspectionDigue", text,
                                                          level= qgis.core.Qgis.Warning , duration=3)
        else:
            print('ErrorMessage', text)

    def normalMessage(self, text):
        if self.dbase.qgsiface is not None:
            #if not self.dbase.standalone:
            # self.dbase.qgsiface.messageBar().pushMessage("InspectionDigue", text, level=qgis.gui.QgsMessageBar.INFO, duration=3)
            if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                self.dbase.qgsiface.messageBar().pushMessage("InspectionDigue", text, self.dbase.qgsiface.messageBar().INFO)
            else:
                self.dbase.qgsiface.messageBar().pushMessage("InspectionDigue" ,text, qgis.core.Qgis.Info)

        else:
            print('normalMessage', text)


    def printRapport(self, reporttype=None, pdffile=None):
        if reporttype is None or pdffile is None:
            self.printrapportdialog.exec_()
            reporttype, pdffile = self.printrapportdialog.dialogIsFinished()
            # print(reporttype, pdffile)

        if reporttype is not None and pdffile is not None and pdffile != '':
            if False:
                self.worker = printPDFWorker(self.dbase, qgis.core.QgsProject.instance(), self.canvas, reporttype, pdffile,self)
                self.thread = QtCore.QThread()
                self.worker.moveToThread(self.thread)
                self.worker.finished.connect(self.exportPDFFinished)
                self.worker.error.connect(self.printError)
                self.worker.message.connect(self.printMessage)
                self.worker.finished.connect(self.exportPDFFinished)
                self.worker.finished.connect(self.worker.deleteLater)
                self.thread.finished.connect(self.thread.deleteLater)
                self.worker.finished.connect(self.thread.quit)

                self.thread.started.connect(self.worker.run)

                self.thread.start()
            if False:
                self.worker = printPDFWorker(self.dbase, qgis.core.QgsProject.instance(), self.canvas, reporttype, pdffile,self)
                self.worker.finished.connect(self.exportPDFFinished)
                self.worker.error.connect(self.printError)
                self.worker.message.connect(self.printMessage)
                self.worker.run()
            if True:
                self.worker = printPDFWorker(self.dbase, qgis.core.QgsProject.instance(), self.canvas, reporttype,
                                             pdffile, self)
                self.worker.work()




    def exportShapefile(self,tabletype=None, pdffile=None):
        if tabletype is None or pdffile is None:
            self.exportshapefiledialog.exec_()
            tabletype, pdffile = self.exportshapefiledialog.dialogIsFinished()
            # print(reporttype, pdffile)

        if tabletype is not None and pdffile is not None and pdffile != '':
            if False:
                self.worker = exportShapefileWorker(self.dbase, tabletype, pdffile)
                self.thread = QtCore.QThread()
                self.worker.moveToThread(self.thread)
                self.worker.finished.connect(self.exportPDFFinished)
                self.worker.error.connect(self.printError)
                self.worker.message.connect(self.printMessage)
                self.worker.finished.connect(self.exportPDFFinished)
                self.worker.finished.connect(self.worker.deleteLater)
                self.thread.finished.connect(self.thread.deleteLater)
                self.worker.finished.connect(self.thread.quit)
                self.thread.started.connect(self.worker.run)
                self.thread.start()
            if False:
                self.worker = exportShapefileWorker(self.dbase, self, tabletype, pdffile)
                self.worker.finished.connect(self.exportPDFFinished)
                self.worker.error.connect(self.printError)
                self.worker.message.connect(self.printMessage)
                self.worker.run()
            if True:
                self.worker = exportShapefileWorker(self.dbase, self, tabletype, pdffile)
                self.worker.work()


    def reInitWindows(self):
        root = qgis.core.QgsProject.instance().layerTreeRoot()
        grp = root.findGroup('Lamia')
        qgis.core.QgsProject.instance().layerTreeRoot().removeChildNode(grp)



    def exportPDFFinished(self):
        self.normalMessage('Export termine')


    def printError(self,errorstr):
        print('error', errorstr)

    def printMessage(self,message):
        print('message', message)


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


    def modeHorsLigne(self):
        if not self.dbase.horsligne:


            #1)Create a spatialite db
            # create database
            try :
                os.remove('../local/DB_local.sqlite')
            except:
                pass

            #Create the folder to stock the new pictures
            local_folder='../local/local_data'
            if not os.path.exists(local_folder):
                os.makedirs(local_folder)

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



            #2)Add items from the file to the spatialite database
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



                            sql = 'INSERT INTO ' +  str(dbname) +' ('+  ','.join(fields_to_import) + ') VALUES ('+ str(str_test)+')'
                            print(sql)
                            self.dbase.query(sql)

            self.dbase.horsligne = not self.dbase.horsligne
            self.date_deconnexion = datetime.datetime.now()
            print("Mode hors ligne active : ", self.dbase.horsligne)
            return



        if self.dbase.horsligne:
            #1) Connect to database
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
                    #First we work on the tables connected to an object
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

                        try:
                            query = self.dbase.offLineCursor.execute(sql)
                            local_data = list(query)
                            self.dbase.offLineConn.commit()
                        except OperationalError as e:
                            print('error query', e)
                            return None

                        original_data = self.dbase.query(sql)


                        if 'geom' in self.dbase.dbasetables[dbname]:
                            fields_to_import[-1]='geom'




                        #Store the list of the dates of creation on the local db and date of modification on the server
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





                        #Make sure we update the foreign key used
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




                        #Get the output to send back to the database
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

                        #Une tc ne sera pas modifiée, au mieux on ajoute des choses dedans
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



            #4) Copy the static files
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



    def setLoadingProgressBar(self, progressbar, val):
        if progressbar is not None:
            progressbar.setValue(val)
        else:
            logger.info('Chargement %d', val )
        QApplication.processEvents()



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
        timestart = time.clock()

        if debugtime: logger.debug(' start %.3f', time.clock() - timestart)

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
            if debugtime: logger.debug(' start %s %.3f', uifield.dbasetablename, time.clock() - timestart)
            # try:
            dbasename = uifield.dbasetablename
            # print(dbasename)
            self.dbase.dbasetables[dbasename]['widget'] = uifield(dbase=self.dbase,
                                                                  dialog=self,
                                                                  linkedtreewidget=self.ElemtreeWidget,
                                                                  gpsutil=self.gpsutil)
            if debugtime: logger.debug(' end %s %.3f', uifield.dbasetablename, time.clock() - timestart)
            i += 1
            self.setLoadingProgressBar(progress, i)
            # except Exception as e:
            #     print('error load', e)

        if progress is not None: self.dbase.qgsiface.messageBar().clearWidgets()
        self.finished.emit()
