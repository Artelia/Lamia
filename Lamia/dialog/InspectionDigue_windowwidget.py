# -*- coding: utf-8 -*-

# qgis pyqt import
from qgis.PyQt import QtGui, uic, QtCore
from qgis.PyQt.QtCore import pyqtSignal
try:
    from qgis.PyQt.QtGui import (QDockWidget, QMainWindow, QFileDialog, QLabel, QInputDialog,
                                 QComboBox,QTableWidgetItem,QProgressBar,QApplication)
except ImportError:
    from qgis.PyQt.QtWidgets import (QDockWidget, QMainWindow, QFileDialog, QLabel, QInputDialog,
                                     QComboBox,QTableWidgetItem, QProgressBar,QApplication)

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

# plugin import
from ..main.DBaseParser import DBaseParser
from .InspectionDigue_Connexion_PG import ConnexionPGDialog
from .InspectionDigue_impression_rapport import ImpressionRapportDialog
from .InspectionDigue_exportShapefile import ExportShapefileDialog
from .InspectionDigue_Import import ImportObjetDialog

from .InspectionDigue_newDB import newDBDialog
from .InspectionDigue_getDate import getDateDialog
from ..maptool.mapTools import mapToolCapture

from ..toolgeneral.InspectionDigue_rapport import printPDFWorker
from ..toolgeneral.InspectionDigue_exportshp import exportShapefileWorker
from ..toolgeneral.InspectionDigue_import import ImportObjectWorker
from ..gps.GPSutil import GpsUtil
import time


class InspectiondigueWindowWidget(QMainWindow):
    """
    the main window widget
    """
    closingPlugin = pyqtSignal()
    # debug
    #logger = logging.getLogger(__name__)
    #logger.setLevel(logging.DEBUG)  # DEBUG INFO WARNING ERROR CRITICAL
    # logging.basicConfig( level=logging.DEBUG)


    def __init__(self, canvas, dockwgt=None, parent=None):
        """
        Constructor
        :param canvas : current qgsmapcanvas
        :param parent : pyqt widget parent
        """
        super(InspectiondigueWindowWidget, self).__init__(parent)
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
        self.dateDialog = getDateDialog()
        # the new db dialog
        self.newDBDialog = newDBDialog()
        # the postgis connection dialog
        self.connDialog = ConnexionPGDialog()
        # for printing reports
        self.printrapportdialog = ImpressionRapportDialog()
        self.exportshapefiledialog = ExportShapefileDialog()
        self.importobjetdialog =ImportObjetDialog()



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

        if self.dbase.dbasetype == 'postgis':
            self.actionMode_hors_ligne_Reconnexion.setDisabled(False)
        else:
            self.actionMode_hors_ligne_Reconnexion.setDisabled(True)
        self.actionMode_hors_ligne_Reconnexion.triggered.connect(self.modeHorsLigne)


        self.pushButton_zoomFeature.clicked.connect(self.zoomToFeature)
        self.pushButton_selectfeat.clicked.connect(self.selectFeature)
        self.action_Repertoire_photo.triggered.connect(self.setImageDir)
        self.actionDate_de_travail.triggered.connect(self.setWorkingDate)
        self.actionModeExpert.triggered.connect(self.setVisualMode)
        self.actionTTC.triggered.connect(self.setVisualMode)
        self.actionModeTerrain.triggered.connect(self.setVisualMode)
        self.actionPosttraitement.triggered.connect(self.setVisualMode)
        self.actionReinitialier_prestation_courante.triggered.connect(self.reinitCurrentPrestation)
        self.actionHauteur_de_perche_GPS.triggered.connect(self.setHauteurPerche)
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


    def setWorkingDate(self):
        """
        pass
        """
        if self.dbase.workingdate is None:
            self.dateDialog.setDate()
        else:
            self.dateDialog.setDate(self.dbase.workingdate)
        self.dateDialog.exec_()
        date = self.dateDialog.dialogIsFinished()
        if date is not None:
            self.dbase.workingdate = date
            self.dbase.updateWorkingDate()

    def closeEvent(self, event):
        """
        PyQt closeEvent - called when the windowdialog is closed
        Unloads the tools widgets
        """
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
                                self.tools.append(obj(self.dbase, self, qgis.utils.iface.mapCanvas() ))


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
        file, extension = self.qfiledlg.getOpenFileNameAndFilter(None, 'Choose the file', '',
                                                                 'Spatialite (*.sqlite)', '')
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
        # logger.info('InspectiondigueWindowWidget - Dbase loaded')
        self.gpsutil.setCRS(self.dbase.qgiscrs)
        self.dbase.updateWorkingDate()
        printtime = False
        timestart = time.clock()

        if qgis.utils.iface is not None:
            progressMessageBar = qgis.utils.iface.messageBar().createMessage("Loading widget...")
            progress = QProgressBar()
            progress.setMaximum(20)
            progress.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
            progressMessageBar.layout().addWidget(progress)
            qgis.utils.iface.messageBar().pushWidget(progressMessageBar, qgis.utils.iface.messageBar().INFO)
        else:
            progress = None

        if debugtime: logger.debug(' progress bar done %s', str(round(time.clock() - timestart, 3)))


        if self.dbase.type.lower() == 'digue':
            # *************************************************************************************************
            # Description sys  ***************************
            i = 0
            if True:
                from ..toolprepro.InspectionDigue_infralineaire_tool import InfraLineaireTool
                self.dbase.dbasetables['Infralineaire']['widget'] = InfraLineaireTool(dbase = self.dbase,
                                                                             dialog = self,
                                                                             linkedtreewidget = self.ElemtreeWidget,
                                                                             gpsutil = self.gpsutil)

                if debugtime: logger.debug('InfraLineaireTool %s', str(round(time.clock() - timestart, 3)))
                #if printtime : print('InfraLineaireTool',round(time.clock() - timestart, 3))
                i += 1
                self.setLoadingProgressBar(progress, i)

            if True:
                from ..toolprepro.InspectionDigue_tronconemprise_tool import TronconEmpriseTool
                self.dbase.dbasetables['Infralinemprise']['widget'] = TronconEmpriseTool(dbase=self.dbase,
                                                                                  dialog=self,
                                                                                  linkedtreewidget=self.ElemtreeWidget,
                                                                                    gpsutil = self.gpsutil)
                if debugtime: logger.debug('TronconEmpriseTool %s', str(round(time.clock() - timestart, 3)))
                i += 1
                self.setLoadingProgressBar(progress, i)

            if True:
                from ..toolprepro.InspectionDigue_equipement_tool import EquipementTool
                self.dbase.dbasetables['Equipement']['widget'] = EquipementTool(dbase=self.dbase,
                                                                                dialog=self,
                                                                                linkedtreewidget=self.ElemtreeWidget,
                                                                                gpsutil=self.gpsutil)
                parentwdg = self.dbase.dbasetables['Equipement']['widget']
                parentwdg.propertieswdgEQUIPEMENT = EquipementTool(dbase=self.dbase, parentwidget=parentwdg)
                parentwdg.dbasechildwdg.append(self.dbase.dbasetables['Equipement']['widget'].propertieswdgEQUIPEMENT)
                try:
                    parentwdg.currentFeatureChanged.disconnect()
                except:
                    pass
                for childwdg in parentwdg.dbasechildwdg:
                    parentwdg.currentFeatureChanged.connect(childwdg.loadChildFeatureinWidget)
                if debugtime: logger.debug('EquipementTool %s', str(round(time.clock() - timestart, 3)))
                i += 1
                self.setLoadingProgressBar(progress, i)

            if True:
                from ..toolprepro.InspectionDigue_profil_tool import ProfilTool
                self.dbase.dbasetables['Profil']['widget'] = ProfilTool(dbase=self.dbase,
                                                                        dialog=self,
                                                                        linkedtreewidget=self.ElemtreeWidget,
                                                                        gpsutil=self.gpsutil)
                if debugtime: logger.debug(' ProfilTool %s', str(round(time.clock() - timestart, 3)))
                i += 1
                self.setLoadingProgressBar(progress, i)

            if True:
                from ..toolprepro.InspectionDigue_noeud_tool import NoeudTool
                self.dbase.dbasetables['Noeud']['widget'] = NoeudTool(dbase=self.dbase,
                                                                        dialog=self,
                                                                        linkedtreewidget=self.ElemtreeWidget,
                                                                        gpsutil=self.gpsutil)
                if debugtime: logger.debug('NoeudTool %s', str(round(time.clock() - timestart, 3)))
                i += 1
                self.setLoadingProgressBar(progress, i)

            # *************************************************************************************************
            # Ressource ***************************
            if True:
                from ..toolprepro.InspectionDigue_photos_tool import PhotosTool
                self.dbase.dbasetables['Photo']['widget'] = [PhotosTool(dbase=self.dbase,
                                                                        dialog=self,
                                                                        linkedtreewidget= self.ElemtreeWidget,
                                                                        gpsutil=self.gpsutil)]
                if debugtime: logger.debug('PhotosTool %s', str(round(time.clock() - timestart, 3)))
                i += 1
                self.setLoadingProgressBar(progress, i)
            if True:
                from ..toolprepro.InspectionDigue_croquis_tool import CroquisTool
                self.dbase.dbasetables['Photo']['widget'].append( CroquisTool(dbase=self.dbase,
                                                                              dialog=self,
                                                                              linkedtreewidget=self.ElemtreeWidget,
                                                                              gpsutil=self.gpsutil) )
                if debugtime: logger.debug('CroquisTool %s', str(round(time.clock() - timestart, 3)))
                i += 1
                self.setLoadingProgressBar(progress, i)
            if True:
                from ..toolprepro.InspectionDigue_rapport_tool import RapportTool
                self.dbase.dbasetables['Rapport']['widget'] = RapportTool(dbase=self.dbase,
                                                                          dialog=self,
                                                                          linkedtreewidget=self.ElemtreeWidget,
                                                                          gpsutil=self.gpsutil)
                if debugtime: logger.debug('RapportTool %s',  str(round(time.clock() - timestart, 3)))
                i += 1
                self.setLoadingProgressBar(progress, i)
            if True:
                from ..toolprepro.InspectionDigue_raster_tool import RasterTool
                self.dbase.dbasetables['Rasters']['widget'] = RasterTool(dbase=self.dbase,
                                                                         dialog=self,
                                                                         linkedtreewidget=self.ElemtreeWidget,
                                                                         gpsutil=self.gpsutil)
                if debugtime: logger.debug('RasterTool %s', str(round(time.clock() - timestart, 3)))
                i += 1
                self.setLoadingProgressBar(progress, i)
            if True:
                from ..toolprepro.InspectionDigue_topographie_tool import TopographieTool
                self.dbase.dbasetables['Topographie']['widget'] = TopographieTool(dbase=self.dbase,
                                                                                  dialog=self,
                                                                                  linkedtreewidget=self.ElemtreeWidget,
                                                                                  gpsutil=self.gpsutil)
                if debugtime: logger.debug('TopographieTool %s',  str(round(time.clock() - timestart, 3)))
                i += 1
                self.setLoadingProgressBar(progress, i)
            if True:
                from ..toolprepro.InspectionDigue_graphique_tool import GraphiqueTool
                self.dbase.dbasetables['Graphique']['widget'] = GraphiqueTool(dbase=self.dbase,
                                                                              dialog=self,
                                                                              linkedtreewidget=self.ElemtreeWidget,
                                                                              gpsutil=self.gpsutil)
                if debugtime: logger.debug('GraphiqueTool %s',  str(round(time.clock() - timestart, 3)))
                i += 1
                self.setLoadingProgressBar(progress, i)
            if True:
                from ..toolprepro.InspectionDigue_pointtopo_tool import PointtopoTool
                self.dbase.dbasetables['Pointtopo']['widget'] = PointtopoTool(dbase=self.dbase,
                                                                              dialog=self,
                                                                              linkedtreewidget=self.ElemtreeWidget,
                                                                              gpsutil=self.gpsutil)
                if debugtime: logger.debug('PointtopoTool %s', str(round(time.clock() - timestart, 3)))
                i += 1
                self.setLoadingProgressBar(progress, i)

            # *************************************************************************************************
            # Desordre  ***************************
            if True:
                from ..toolprepro.InspectionDigue_desordre_tool import DesordreTool
                self.dbase.dbasetables['Desordre']['widget'] = DesordreTool(dbase=self.dbase,
                                                                            dialog=self,
                                                                            linkedtreewidget=self.ElemtreeWidget,
                                                                            gpsutil=self.gpsutil)
                if debugtime: logger.debug('DesordreTool %s',  str(round(time.clock() - timestart, 3)))
                i += 1
                self.setLoadingProgressBar(progress, i)

            if True:
                from ..toolprepro.InspectionDigue_observation_tool import ObservationTool
                self.dbase.dbasetables['Observation']['widget'] = ObservationTool(dbase=self.dbase,
                                                                                  dialog=self,
                                                                                  linkedtreewidget=self.ElemtreeWidget,
                                                                                  gpsutil=self.gpsutil)
                if debugtime: logger.debug('ObservationTool %s',  str(round(time.clock() - timestart, 3)))
                i += 1
                self.setLoadingProgressBar(progress, i)

            # *************************************************************************************************
            # Autre ***************************
            if True:
                from ..toolprepro.InspectionDigue_zonegeo_tool import ZonegeoTool
                self.dbase.dbasetables['Zonegeo']['widget'] = ZonegeoTool(dbase=self.dbase,
                                                                          dialog=self,
                                                                          linkedtreewidget=self.ElemtreeWidget,
                                                                          gpsutil=self.gpsutil)
                if debugtime: logger.debug('ZonegeoTool %s',str(round(time.clock() - timestart, 3)))
                i += 1
                self.setLoadingProgressBar(progress, i)
            if True:
                from ..toolprepro.InspectionDigue_marche_tool import MarcheTool
                self.dbase.dbasetables['Marche']['widget'] = MarcheTool(dbase=self.dbase,
                                                                        dialog=self,
                                                                        linkedtreewidget=self.ElemtreeWidget,
                                                                        gpsutil=self.gpsutil)
                if debugtime: logger.debug('MarcheTool %s', str(round(time.clock() - timestart, 3)))
                i += 1
                self.setLoadingProgressBar(progress, i)
            if True:
                from ..toolprepro.InspectionDigue_intervenant_tool import IntervenantTool
                self.dbase.dbasetables['Intervenant']['widget'] = IntervenantTool(dbase=self.dbase,
                                                                                  dialog=self,
                                                                                  linkedtreewidget=self.ElemtreeWidget,
                                                                                  gpsutil=self.gpsutil)
                if debugtime: logger.debug('IntervenantTool %s',  str(round(time.clock() - timestart, 3)))
                i += 1
                self.setLoadingProgressBar(progress, i)

            # *************************************************************************************************
            # Base  ***************************
            if False:
                from ..toolprepro.InspectionDigue_objet_tool import objetTool
                self.dbase.dbasetables['OBJET']['widget'] = objetTool(dbase=self.dbase,
                                                                      dialog=self,
                                                                      linkedtreewidget=self.ElemtreeWidget,
                                                                      gpsutil=self.gpsutil)

            if False:
                from ..toolprepro.InspectionDigue_descriptionsysteme_tool import DescriptionsystemeTool
                self.dbase.dbasetables['DESCRIPTIONSYSTEME']['widget'] = DescriptionsystemeTool(dbase=self.dbase,
                                                                                                dialog=self,
                                                                                                linkedtreewidget=self.ElemtreeWidget,
                                                                                                gpsutil=self.gpsutil)

            # *************************************************************************************************
            # PostPro  ***************************

            if True:
                from ..toolpostpro.InspectionDigue_synth_zonegeo_tool import SyntheseZonegeoTool
                self.synthesezonegeotool = SyntheseZonegeoTool(dbase=self.dbase,
                                                               dialog=self,
                                                               linkedtreewidget=self.ElemtreeWidget)
                self.tools.append(self.synthesezonegeotool)
                if debugtime: logger.debug('SyntheseZonegeoTool %s',   str(round(time.clock() - timestart, 3)))
                i += 1
                self.setLoadingProgressBar(progress, i)

            if True:
                try:
                    from ..toolpostpro.InspectionDigue_path_tool import PathTool
                    self.pathtool = PathTool(dbase=self.dbase,
                                                                   dialog=self,
                                                                   linkedtreewidget=self.ElemtreeWidget)
                    self.tools.append(self.pathtool)
                    if debugtime: logger.debug('PathTool %s',  str(round(time.clock() - timestart, 3)))

                    if not os.path.isfile(self.pathtool.dbasetablename):
                        filepath = open(self.pathtool.dbasetablename,'w')
                        filepath.close()
                    i += 1
                    self.setLoadingProgressBar(progress, i)
                except:
                    pass

            if progress is not None: qgis.utils.iface.messageBar().clearWidgets()

        self.applyVisualMode()

        if debugtime: logger.debug('applyVisualMode %s',str(round(time.clock() - timestart, 3)))

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
            nearestid, dist = wdg.getNearestId(point)
            itemindex = wdg.comboBox_featurelist.findText(str(nearestid))
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

            if qgis.utils.iface is not None:
                qgis.utils.iface.messageBar().pushMessage("InspectionDigue", 'Export fini', level=qgis.gui.QgsMessageBar.SUCCESS, duration=3)
            else:
                print('export fini')

    def openHelp(self):
        path = os.path.join(os.path.dirname(__file__),'..','html','index.html')
        os.startfile(path)


    def errorMessage(self, text):
        if qgis.utils.iface is not None:
            qgis.utils.iface.messageBar().pushMessage("InspectionDigue", text,
                                                      level=qgis.gui.QgsMessageBar.CRITICAL, duration=3)
        else:
            print('ErrorMessage', text)

    def warningMessage(self, text):
        if qgis.utils.iface is not None:
            qgis.utils.iface.messageBar().pushMessage("InspectionDigue", text,
                                                      level=qgis.gui.QgsMessageBar.WARNING, duration=3)
        else:
            print('ErrorMessage', text)

    def normalMessage(self, text):
        if qgis.utils.iface is not None:
            qgis.utils.iface.messageBar().pushMessage("InspectionDigue", text,
                                                      level=qgis.gui.QgsMessageBar.INFO, duration=3)
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
            if True:
                self.worker = printPDFWorker(self.dbase, qgis.core.QgsProject.instance(), self.canvas, reporttype, pdffile,self)
                self.worker.finished.connect(self.exportPDFFinished)
                self.worker.error.connect(self.printError)
                self.worker.message.connect(self.printMessage)
                self.worker.run()

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
            if True:
                self.worker = exportShapefileWorker(self.dbase, self, tabletype, pdffile)
                self.worker.finished.connect(self.exportPDFFinished)
                self.worker.error.connect(self.printError)
                self.worker.message.connect(self.printMessage)
                self.worker.run()


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
            if qgis.utils.iface is not None:
                currentlayer = qgis.utils.iface.activeLayer()
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
        self.horsligne = not self.horsligne

    def setLoadingProgressBar(self, progressbar, val):
        if progressbar is not None:
            progressbar.setValue(val)
        else:
            logger.info('Chargement %s', str(val))
        QApplication.processEvents()


