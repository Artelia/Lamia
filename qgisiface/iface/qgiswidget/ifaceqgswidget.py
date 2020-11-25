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
from qgis.PyQt.QtWidgets import (
    QDockWidget,
    QMainWindow,
    QFileDialog,
    QLabel,
    QInputDialog,
    QComboBox,
    QTableWidgetItem,
    QProgressBar,
    QApplication,
    QToolBar,
    QPushButton,
    QToolButton,
    QWidget,
    QMessageBox,
    QAction,
    QFrame,
)


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
import webbrowser


import glob, importlib, inspect
from pprint import pprint

import Lamia, Lamia.qgisiface, Lamia.config, time
from Lamia.api.libslamia.gps.GPSutil import GpsUtil
from Lamia.api.dbasemanager.dbaseparserfactory import DBaseParserFactory

from ..ifaceabstractwidget import LamiaIFaceAbstractWidget
from ..qgsconnector.ifaceqgisconnector import QgisConnector
from ..qgscanvas.ifaceqgiscanvas import QgisCanvas

from .subdialogs.lamia_Connexion_PG import ConnexionPGDialog
from .subdialogs.lamia_ConflitHorsLigne import ConflitHorsLigne
from .subdialogs.lamia_iconsize import IconSizeDialog
from .subdialogs.lamia_newDB import newDBDialog
from .subdialogs.lamia_getDate import getDateDialog
from .subdialogs.lamia_tablefield_dialog import LamiaTableFieldDialog


# version 01


debugtime = False


class LamiaWindowWidget(QMainWindow, LamiaIFaceAbstractWidget):
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
        # super(LamiaWindowWidget, self).__init__(parent)
        # super(LamiaWindowWidget, self).__init__(parent)
        LamiaIFaceAbstractWidget.__init__(self)
        QMainWindow.__init__(self, parent)
        debug = False

        if debug:
            logging.getLogger("Lamia").debug("start")

        path = os.path.join(os.path.dirname(__file__), "ifaceqgswidget.ui")
        uic.loadUi(path, self)

        # connector and canvas
        self.connector = QgisConnector()
        self.connector.widget = self
        self.qgiscanvas = QgisCanvas()
        self.gpsutil = GpsUtil()
        self.gpsutil.hauteurperche = 2.0

        # statusbar
        self.GPSlabel = QLabel(self.tr("GPS not connected"))
        self.statusBar().addWidget(self.GPSlabel)
        self.GPSlabelperchheigh = QLabel(self.tr("GPS rod height : /"))
        self.statusBar().addWidget(self.GPSlabelperchheigh)
        self.GPSlabelprecision = QLabel(self.tr("Accuracy"))
        self.statusBar().addWidget(self.GPSlabelprecision)

        # interfacemode
        # old :self.dbase.visualmode
        self.interfacemode = None
        self.wdgclasses = {}  # dict containing all tools classes (prepro / postpro)
        self.toolwidgets = {}  # dict containing all tools widgets (prepro / postpro)
        self.toolwidgets[
            "desktop_loaded"
        ] = False  # used to store desktoptools are arlready loaded

        # behaviour var
        self.currenttoolwidget = None
        self.imagedirectory = None
        self.currentchoosertreewidget = None
        # store qgis tool bar visibility when entering/exiting field mode
        self.toolbarsvisibility = {}

        # subdialogs
        self.newDBDialog = newDBDialog()
        self.crsselector = qgis.gui.QgsProjectionSelectionDialog()
        self.qfiledlg = QFileDialog()
        self.connPGDialog = ConnexionPGDialog()
        self.tablefielddialog = LamiaTableFieldDialog()

        # camera path
        if QtCore.QSettings().value("Lamia/picturepath") is not None:
            self.imagedirectory = os.path.normpath(
                QtCore.QSettings().value("Lamia/picturepath")
            )
        else:
            self.imagedirectory = None

        # ************** Init actions ******************
        self._manageQgisDockWidgetOnStart()
        self._connectMenuAndOthers()
        self._connectToolBar()
        self._readRecentDBase()
        self._updateRecentDBaseMenu()

        self.splitter_2.setSizes([80, 200])
        if debug:
            logging.getLogger("Lamia").debug("end")

        # ******* dev actions
        self.hideDevQWidgets()

    # ***********************************************************
    # **************** File menu actions ***********************
    # ***********************************************************

    def ____________FileMenuActions(self):
        pass

    def _dialogForDbaseConf(self, dbtype="spatialite"):
        if dbtype == "spatialite":
            # spatialitefile, fileext = self.qfiledlg.getSaveFileName(
            #     self, self.tr("Lamia new"), "", "*.sqlite"
            # )

            spatialitefile, fileext = self.qfiledlg.getOpenFileName(
                None, self.tr("Lamia new"), "", "Spatialite (*.sqlite)", "",
            )

            return {"slfile": spatialitefile}
        elif dbtype == "postgis":
            self.connDialog.exec_()
            (
                adresse,
                port,
                nom,
                schema,
                user,
                password,
            ) = self.connDialog.dialogIsFinished()
            return {
                "host": adresse,
                "port": port,
                "dbname": nom,
                "schema": schema,
                "user": user,
                "password": password,
            }

    def newDBase(self):
        """
        pass
        """
        # dialog with dbtype, worktype, vartype  chooser
        # self.newDBDialog.comboBox_type.currentIndexChanged.emit(0)
        self.newDBDialog.exec_()
        dbtype, worktype, vartype = self.newDBDialog.dialogIsFinished()
        if dbtype is None:
            return

        # dialog for crs selector
        self.crsselector.exec_()
        crs = self.crsselector.crs().authid()
        crsnumber = int(crs.split(":")[1])

        # dialog for ressources directory
        if dbtype == "postgis":
            resdir = self.qfiledlg.getExistingDirectory(
                self, self.tr("Select resources directory")
            )
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
        if dbtype == "spatialite":
            spatialitefile, fileext = self.qfiledlg.getSaveFileName(
                self, self.tr("Lamia new"), "", "*.sqlite"
            )
            # self.createDBase() TODO
            if spatialitefile:
                if self.connector:
                    self.connector.showNormalMessage(self.tr(" Database creation..."))

                self.dbase = DBaseParserFactory(
                    "spatialite", self.connector
                ).getDbaseParser()
                self.dbase.createDBase(
                    crs=crsnumber,
                    worktype=worktype,
                    dbaseressourcesdirectory=resdir,
                    variante=vartype,
                    slfile=spatialitefile,
                )
                self.loadDBase(dbtype="Spatialite", slfile=spatialitefile)

        elif dbtype == "postgis":
            self.connPGDialog.exec_()
            (
                adresse,
                port,
                nom,
                schema,
                user,
                password,
            ) = self.connPGDialog.dialogIsFinished()
            if (
                adresse is not None
                and port is not None
                and nom is not None
                and user is not None
                and password is not None
            ):
                # self.createDBase()
                databaseexists, schemaexists = self.dbase.checkIfPGShcemaExists(
                    host=adresse,
                    dbname=nom,
                    schema=schema,
                    user=user,
                    password=password,
                )
                if schemaexists:
                    print("schema existe deja - choisir un autre schema")
                else:
                    if self.connector:
                        self.connector.showNormalMessage(
                            self.tr(" Database creation...")
                        )
                    # reset dbase
                    # self.createDBase()
                    # QApplication.processEvents()

                    # resdir = self.createRessourcesDir(dbtype, resdir,vardir=vardir)

                    # self.dbase.createDbase(crs=crsnumber, worktype=worktype, dbasetype='postgis', dbname=nom, schema=schema,
                    #                       user=user, host=adresse, password=password, dbaseressourcesdirectory=resdir,
                    #                       port=port,variante=vartype)
                    self.dbase = DBaseParserFactory(
                        "postgis", self.connector
                    ).getDbaseParser()
                    self.dbase.createDBase(
                        crs=crsnumber,
                        worktype=worktype,
                        dbaseressourcesdirectory=resdir,
                        variante=vartype,
                        host=adresse,
                        port=port,
                        dbname=nom,
                        schema=schema,
                        user=user,
                        password=password,
                    )
                    self.loadDBase(
                        dbtype="Postgis",
                        host=adresse,
                        port=port,
                        dbname=nom,
                        schema=schema,
                        user=user,
                        password=password,
                    )

    def loadDBase(self, **kwargs):
        """[summary]
        kwargs contains either var:
        - dbtype : 'Postgis' or 'Spatialite'
        - slfile (optionnal)
        - host port dbname schema userpassword (optionnal)
        """
        self.reinitWidgetbeforeloading()

        if "dbtype" not in kwargs.keys():  # case come from qt event
            kwargs["dbtype"] = self.sender().objectName()[6:]
        success = self._loadDBaseParser(**kwargs)
        if not success:
            return
        # self.connector.showNormalMessage(self.tr('Loading Layers ...'))
        self.connector.createProgressBar(self.tr("Loading Layers ..."), 0)
        self._loadVectorLayers()
        self._loadStyles()
        QApplication.processEvents()
        self.connector.closeProgressBar()
        self._AddDbaseInRecentsDBase(self.dbase)

        self.loadToolsClasses()
        self.loadToolsWidgets()

        # self.connector.createProgressBar(self.tr('Loading Layers ...'), 0 )
        self.setVisualMode(visualmode=0)
        self.qgiscanvas.updateWorkingDate(dbaseparser=self.dbase)
        # self.connector.closeProgressBar()

        self.connector.showNormalMessage("Lamia loaded")

    def reinitWidgetbeforeloading(self):
        # old :self.dbase.visualmode

        self.interfacemode = None

        self.wdgclasses = {}  # dict containing all tools classes (prepro / postpro)
        self.toolwidgets = {}  # dict containing all tools widgets (prepro / postpro)
        self.toolwidgets[
            "desktop_loaded"
        ] = False  # used to store desktoptools are arlready loaded

        self.MaintreeWidget.setStyleSheet("")
        try:
            self.MaintreeWidget.disconnect()
        except:
            pass
        self.MaintreeWidget.clear()
        self.ElemtreeWidget.clear()
        # behaviour var
        if self.currenttoolwidget:
            self.currenttoolwidget.setParent(None)
        self.currenttoolwidget = None
        # self.imagedirectory = None
        self.currentchoosertreewidget = None

        # if self.qgiscanvas.rubberBand is not None:
        #     self.qgiscanvas.rubberBand.reset(0)
        self.qgiscanvas.createorresetRubberband(rubtype="all")

        self.qgiscanvas.unloadLayersInCanvas()
        self.gpsutil.closeConnection()
        try:
            self.dbase.disconnect()
        except:
            pass
        # QApplication.processEvents()

    def pullDBase(self, exportfilepath=None):  # for offline mode

        exportfilepath = self.dbase.dbaseofflinemanager.pullDBase(exportfilepath)
        self.loadDBase(dbtype="Spatialite", slfile=exportfilepath)

    def pushDBase(self):  # for offline mode
        self.dbase.dbaseofflinemanager.pushDBase()

    def addDBase(self):
        dbconf = self._dialogForDbaseConf()
        self.dbase.dbaseofflinemanager.addDBase(**dbconf)

    def _loadDBaseParser(self, **kwargs):
        success = False
        if "dbtype" in kwargs.keys():
            dbtype = kwargs.get("dbtype")
            if dbtype == "Postgis":
                neededkwargs = set(
                    ["host", "port", "dbname", "schema", "user", "password"]
                )
                if not neededkwargs.issubset(set(list(kwargs.keys()))):
                    self.connDialog = ConnexionPGDialog()
                    self.connDialog.exec_()
                    (
                        host,
                        port,
                        dbname,
                        schema,
                        user,
                        password,
                    ) = self.connDialog.dialogIsFinished()
                else:
                    host, port, dbname, schema, user, password = (
                        kwargs.get("host"),
                        kwargs.get("port"),
                        kwargs.get("dbname"),
                        kwargs.get("schema"),
                        kwargs.get("user"),
                        kwargs.get("password"),
                    )

                if (
                    host is not None
                    and port is not None
                    and dbname is not None
                    and user is not None
                    and password is not None
                ):
                    # reset dbase
                    # self.createDBase()
                    self.dbase = DBaseParserFactory(
                        "postgis", self.connector
                    ).getDbaseParser()
                    self.dbase.loadDBase(
                        host=host,
                        port=port,
                        dbname=dbname,
                        schema=schema,
                        user=user,
                        password=password,
                    )

                    # self.dbase.loadQgisVectorLayers(file=None, dbasetype='postgis', host=adresse, port=port, dbname=nom,
                    #                                schema=schema, user=user, password=password)
                    success = True
            elif dbtype == "Spatialite":
                if not "slfile" in kwargs.keys():
                    slfile, extension = self.qfiledlg.getOpenFileName(
                        None,
                        self.tr("Choose the file"),
                        "",
                        "Spatialite (*.sqlite)",
                        "",
                    )
                else:
                    slfile = kwargs.get("slfile")

                if slfile:
                    # reset dbase
                    # self.reinitDBase()
                    # reset dbase
                    # self.createDBase()
                    self.dbase = DBaseParserFactory(
                        "spatialite", self.connector
                    ).getDbaseParser()
                    self.dbase.loadDBase(slfile=slfile)
                    # self.dbase.loadQgisVectorLayers(file)
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
        pathrecentproject = os.path.join(
            os.path.dirname(Lamia.qgisiface.__file__), "config", "recentprojects.txt"
        )
        try:
            file = open(pathrecentproject, "r")
            lines = file.readlines()
            file.close()
            self.recentsdbase = []
            for line in lines:
                if os.path.isfile(line.strip()):
                    self.recentsdbase.append(line.strip())
                elif len(line.split(";")) == 3:
                    self.recentsdbase.append(line.strip())
        except:
            pass
        # self.recentDBaseChanged.emit()
        self._updateRecentDBaseMenu()

    def _AddDbaseInRecentsDBase(self, dbaseparser):
        """
        Methode appelée lors du chargement d'une BD lamia
        Ajoute le chemin dans le fichier chargé dans Menu//Fichier//base de données recentes
        """
        # if self.dbase.dbasetype == 'spatialite':
        if dbaseparser.__class__.__name__ == "SpatialiteDBaseParser":
            spatialitefile = dbaseparser.spatialitefile
            if spatialitefile in self.recentsdbase:
                index = self.recentsdbase.index(spatialitefile)
                del self.recentsdbase[index]
            self.recentsdbase.insert(0, spatialitefile)
            self._saveRecentDBase()
            # self.recentDBaseChanged.emit()
            self._updateRecentDBaseMenu()
        # elif self.dbase.dbasetype == 'postgis':
        elif dbaseparser.__class__.__name__ == "PostGisDBaseParser":
            # name = dbname + '.' +schema  + '@' + host + ':' + str(port) + ';' + user + ';' + password
            name = dbaseparser.pgdb + "." + dbaseparser.pgschema
            name += "@" + str(dbaseparser.pghost) + ":" + str(dbaseparser.pgport) + ";"
            name += dbaseparser.pguser + ";" + dbaseparser.pgpassword
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
        pathrecentproject = os.path.join(
            os.path.dirname(Lamia.qgisiface.__file__), "config", "recentprojects.txt"
        )
        file = open(pathrecentproject, "w")
        for i, path in enumerate(self.recentsdbase):
            if i > 10:
                break
            if not path == "":
                file.write(path + "\n")
        file.close()
        self._updateRecentDBaseMenu()

    def _openFileFromMenu(self, action):
        """
        pass
        """
        filetoopen = action.text()
        if len(filetoopen.split(";")) == 1:
            # self.createDBase()
            # self.dbase.loadQgisVectorLayers(filetoopen)
            self.loadDBase(dbtype="Spatialite", slfile=filetoopen)
        else:
            # self.createDBase()
            db, user, password = filetoopen.split(";")
            nom, schema = db.split("@")[0].split(".")
            adresse, port = db.split("@")[1].split(":")
            # self.dbase.loadQgisVectorLayers(dbasetype='postgis', host=adresse, port=int(port), dbname=nom,
            #                                schema=schema, user=user, password=password)
            self.loadDBase(
                dbtype="Postgis",
                host=adresse,
                port=int(port),
                dbname=nom,
                schema=schema,
                user=user,
                password=password,
            )

    def _loadStyles(self):
        try:
            self.comboBox_style.currentIndexChanged.disconnect(self.comboStyleChanged)
        except:
            pass
        self.comboBox_style.clear()

        stylepath = self.qgiscanvas._getStyleDirectory(self.dbase.worktype)

        styledirs = [x[1] for x in os.walk(stylepath) if len(x[1]) > 0]
        if len(styledirs) > 0:
            styledirs = styledirs[0]
            self.comboBox_style.addItems(styledirs)
            self.comboBox_style.currentIndexChanged.connect(self.comboStyleChanged)
            self.comboBox_style.currentIndexChanged.emit(0)

    def comboStyleChanged(self, comboindex):
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
    def ____________InterfacemodeActions(self):
        pass

    # def setVisualMode(self, tempres=None, reset=False):
    def setVisualMode(self, **kwargs):
        """
        pass
        """
        visualmodedict = {
            0: "actionModeTerrain",
            1: "actionTTC",
            2: "actionModeExpert",
            4: "actionPosttraitement",
        }

        reset = kwargs.get("reset", None)
        visualmode = kwargs.get("visualmode", None)

        if visualmode is not None:
            actionname = visualmodedict[visualmode]
        elif isinstance(self.sender(), QAction):
            actionname = self.sender().objectName()
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
            if not self.toolwidgets["desktop_loaded"]:
                # self.loadUiDesktop()
                self.loadToolsWidgets(fullloading=True)
        elif actionname == visualmodedict[2]:
            self.interfacemode = 2
        elif actionname == visualmodedict[4]:
            self.interfacemode = 4
            if not self.toolwidgets["desktop_loaded"]:
                # self.loadUiDesktop()
                self.loadToolsWidgets(fullloading=True)

        self._applyVisualMode()

    def _applyVisualMode(self, actiontext=None):

        if self.dbase.base3version:
            for toolname in self.toolwidgets.keys():
                if toolname == "desktop_loaded":
                    continue
                toolwdg = self.toolwidgets[toolname]
                toolwdg.changeInterfaceMode()

        else:
            for tooltype in self.toolwidgets.keys():
                if tooltype == "desktop_loaded":
                    continue

                for toolname in self.toolwidgets[tooltype].keys():
                    toolwdg = self.toolwidgets[tooltype][toolname]
                    if isinstance(toolwdg, list):
                        for wdg in toolwdg:
                            # tool dep
                            if hasattr(wdg, "changeInterfaceMode"):
                                wdg.changeInterfaceMode()
                            else:
                                wdg.changePropertiesWidget()
                    else:
                        # tool dep
                        if hasattr(toolwdg, "changeInterfaceMode"):
                            toolwdg.changeInterfaceMode()
                        else:
                            toolwdg.changePropertiesWidget()

    def loadToolsClasses(self):
        if self.dbase.base3version:
            self.loadToolsClassesBase3()
        else:
            self.loadToolsClassesBase2()

    def loadToolsClassesBase2(self):
        """
        Load layers and put them in a legend group in qgis
        Load all modules (prepro, postpro and menu)
        Show field ui

        :return:
        """

        debug = False
        if debug:
            logging.getLogger("Lamia").debug("start")

        tooltypestoload = ["toolprepro", "toolpostpro"]
        for tooltypetoload in tooltypestoload:
            self.wdgclasses[tooltypetoload] = {}

            path = os.path.join(
                os.path.dirname(__file__),
                "tools",
                tooltypetoload,
                self.dbase.worktype.lower(),
            )
            modules = glob.glob(path + "/*.py")
            __all__ = [os.path.basename(f)[:-3] for f in modules if os.path.isfile(f)]
            interfacefielduisup = []
            for x in __all__:
                if debug:
                    logging.getLogger("Lamia_unittest").debug("x %s", x)
                parentmodulename = ".".join(__name__.split(".")[:-1])
                modulename = (
                    parentmodulename
                    + ".tools."
                    + tooltypetoload
                    + "."
                    + self.dbase.worktype.lower()
                )
                exec("import " + modulename)
                moduletemp = importlib.import_module("." + str(x), modulename)

                for name, obj in inspect.getmembers(moduletemp, inspect.isclass):
                    if moduletemp.__name__ == obj.__module__:
                        if tooltypetoload == "toolpostpro" and hasattr(obj, "TOOLNAME"):
                            self.wdgclasses[tooltypetoload][obj.TOOLNAME] = obj
                        elif (
                            tooltypetoload == "toolpostpro"
                            and hasattr(obj, "POSTPROTOOLNAME")  # dbase3
                            and hasattr(obj, "POSTPROTOOLNAME")
                            and obj.POSTPROTOOLNAME is not None
                        ):
                            self.wdgclasses[tooltypetoload][obj.POSTPROTOOLNAME] = obj

                        if tooltypetoload == "toolprepro" and hasattr(
                            obj, "dbasetablename"
                        ):  # tool dep
                            self.wdgclasses[tooltypetoload][obj.dbasetablename] = obj
                        elif (
                            tooltypetoload == "toolprepro"
                            and hasattr(obj, "DBASETABLENAME")  # dbase3
                            and hasattr(obj, "PREPROTOOLNAME")
                            and obj.PREPROTOOLNAME is not None
                        ):
                            self.wdgclasses[tooltypetoload][obj.PREPROTOOLNAME] = obj
                        elif (
                            tooltypetoload == "toolprepro"
                            and hasattr(obj, "DBASETABLENAME")
                            and hasattr(obj, "tooltreewidgetSUBCAT")
                            and obj.tooltreewidgetSUBCAT is not None
                        ):
                            self.wdgclasses[tooltypetoload][
                                obj.tooltreewidgetSUBCAT
                            ] = obj

        if debug:
            logging.getLogger("Lamia_unittest").debug("x %s", str(self.wdgclasses))

    def loadToolsClassesBase3(self):
        """
        Load layers and put them in a legend group in qgis
        Load all modules (prepro, postpro and menu)
        Show field ui

        :return:
        """

        debug = False
        if debug:
            logging.getLogger("Lamia").debug("start")

        # tooltypestoload = ["toolprepro", "toolpostpro"]

        modulelistpath = [
            # "Lamia",
            # "worktypeconf",
            self.dbase.worktype.lower(),
            "qgswidgets",
        ]

        path = os.path.join(
            os.path.dirname(Lamia.config.__file__), "//".join(modulelistpath)
        )

        pyfilespath = glob.glob(path + "/*.py")
        pyfiles = [os.path.basename(f)[:-3] for f in pyfilespath if os.path.isfile(f)]
        for x in pyfiles:
            if debug:
                logging.getLogger("Lamia_unittest").debug("x %s", x)
            classlistpath = ["Lamia.config"] + modulelistpath + [x]
            modulename = ".".join(classlistpath)
            moduletemp = importlib.import_module(modulename)

            for name, obj in inspect.getmembers(moduletemp, inspect.isclass):
                if moduletemp.__name__ == obj.__module__:
                    if (
                        hasattr(obj, "POSTPROTOOLNAME")
                        and obj.POSTPROTOOLNAME is not None
                    ):
                        self.wdgclasses[obj.POSTPROTOOLNAME] = {
                            "class": obj,
                            "type": "postpro",
                            "loaded": False,
                            "loadfirst": True
                            if hasattr(obj, "LOADFIRST") and obj.LOADFIRST
                            else False,
                        }
                    elif (
                        hasattr(obj, "PREPROTOOLNAME")
                        and obj.PREPROTOOLNAME is not None
                    ):
                        self.wdgclasses[obj.PREPROTOOLNAME] = {
                            "class": obj,
                            "type": "prepro",
                            "loaded": False,
                            "loadfirst": True
                            if hasattr(obj, "LOADFIRST") and obj.LOADFIRST
                            else False,
                        }

    def loadToolsWidgets(self, fullloading=False):
        if self.dbase.base3version:
            self.loadToolsWidgetsBase3(fullloading)
        else:
            self.loadToolsWidgetsBase2(fullloading)

    def loadToolsWidgetsBase2(self, fullloading=False):

        debug = False
        typeswdg = ["toolprepro", "toolpostpro"]

        toopreprodict = self.wdgclasses["toolprepro"]
        lenprogresspartialloading = len(
            [
                name
                for name in toopreprodict.keys()
                if hasattr(toopreprodict[name], "LOADFIRST")
                and toopreprodict[name].LOADFIRST
            ]
        )
        lenprogressfullloading = len(self.wdgclasses["toolprepro"]) + len(
            self.wdgclasses["toolpostpro"]
        )

        creationstring = self.tr("Loading widgets...")
        if fullloading:
            self.connector.createProgressBar(
                creationstring, lenprogressfullloading - lenprogresspartialloading
            )
        else:
            self.connector.createProgressBar(creationstring, lenprogresspartialloading)

        i = 0
        for typewdg in typeswdg:
            if not fullloading and typewdg == "toolpostpro":
                continue
            if not typewdg in self.toolwidgets.keys():
                self.toolwidgets[typewdg] = {}
            for toolname in self.wdgclasses[typewdg].keys():
                if toolname in self.toolwidgets[typewdg].keys():
                    continue
                if debug:
                    logging.getLogger("Lamia_unittest").debug("loading %s", toolname)
                self.toolwidgets[typewdg][toolname] = []
                toolwdglist = self.toolwidgets[typewdg][toolname]
                toolwdgcls = self.wdgclasses[typewdg][toolname]
                try:
                    if (
                        hasattr(self.wdgclasses[typewdg][toolname], "PREPROTOOLNAME")
                        and not fullloading
                    ):
                        self.toolwidgets[typewdg][toolname] = toolwdgcls(
                            dbaseparser=self.dbase,
                            mainifacewidget=self,
                            choosertreewidget=self.ElemtreeWidget,
                            parentwidget=None,
                        )

                    elif (
                        hasattr(self.wdgclasses[typewdg][toolname], "POSTPROTOOLNAME")
                        and fullloading
                    ):
                        self.toolwidgets[typewdg][toolname] = toolwdgcls(
                            dbaseparser=self.dbase,
                            mainifacewidget=self,
                            choosertreewidget=self.ElemtreeWidget,
                            parentwidget=None,
                        )

                    elif (
                        hasattr(self.wdgclasses[typewdg][toolname], "LOADFIRST")
                        and not fullloading
                    ):
                        toolwdglist.append(
                            toolwdgcls(
                                dbase=self.dbase,
                                dialog=self,
                                linkedtreewidget=self.ElemtreeWidget,
                                gpsutil=self.gpsutil,
                            )
                        )

                    else:  # tool dep
                        toolwdglist.append(
                            toolwdgcls(
                                dbase=self.dbase,
                                dialog=self,
                                linkedtreewidget=self.ElemtreeWidget,
                                gpsutil=self.gpsutil,
                            )
                        )

                except TypeError as e:
                    print(toolname, e)
                    # raise TypeError
                i += 1
                self.connector.updateProgressBar(i)

        if not self.toolwidgets["desktop_loaded"] and fullloading:
            self.toolwidgets["desktop_loaded"] = True
        self.connector.closeProgressBar()

    def loadToolsWidgetsBase3(self, fullloading=False):

        debug = False

        lenprogresspartialloading = len(
            list(
                [
                    elem["loadfirst"]
                    for elem in self.wdgclasses.values()
                    if elem["loadfirst"]
                ]
            )
        )
        lenprogressfullloading = len(self.wdgclasses)
        """
        toopreprodict = self.wdgclasses["toolprepro"]
        lenprogresspartialloading = len(
            [
                name
                for name in toopreprodict.keys()
                if hasattr(toopreprodict[name], "LOADFIRST")
                and toopreprodict[name].LOADFIRST
            ]
        )
        lenprogressfullloading = len(self.wdgclasses["toolprepro"]) + len(
            self.wdgclasses["toolpostpro"]
        )
        """
        # print(lenprogresspartialloading)

        creationstring = self.tr("Loading widgets...")
        if fullloading:
            self.connector.createProgressBar(
                creationstring, lenprogressfullloading - lenprogresspartialloading
            )
        else:
            self.connector.createProgressBar(creationstring, lenprogresspartialloading)

        i = 0

        for wdgname, wdgvalues in self.wdgclasses.items():
            if not fullloading and wdgvalues["type"] == "postpro":
                continue
            if wdgname in self.toolwidgets.keys():
                continue

            if debug:
                logging.getLogger("Lamia_unittest").debug("loading %s", wdgname)

            if (
                wdgvalues["type"] == "prepro"
                and wdgvalues["loadfirst"]
                and not fullloading
            ):
                self.toolwidgets[wdgname] = wdgvalues["class"](
                    dbaseparser=self.dbase,
                    mainifacewidget=self,
                    choosertreewidget=self.ElemtreeWidget,
                    parentwidget=None,
                )
            else:
                self.toolwidgets[wdgname] = wdgvalues["class"](
                    dbaseparser=self.dbase,
                    mainifacewidget=self,
                    choosertreewidget=self.ElemtreeWidget,
                    parentwidget=None,
                )
            i += 1
            self.connector.updateProgressBar(i)

        """
        for typewdg in typeswdg:
            if not fullloading and typewdg == "toolpostpro":
                continue
            if not typewdg in self.toolwidgets.keys():
                self.toolwidgets[typewdg] = {}
            for toolname in self.wdgclasses[typewdg].keys():
                if toolname in self.toolwidgets[typewdg].keys():
                    continue
                if debug:
                    logging.getLogger("Lamia_unittest").debug("loading %s", toolname)
                self.toolwidgets[typewdg][toolname] = []
                toolwdglist = self.toolwidgets[typewdg][toolname]
                toolwdgcls = self.wdgclasses[typewdg][toolname]
                try:
                    if (
                        hasattr(self.wdgclasses[typewdg][toolname], "PREPROTOOLNAME")
                        and not fullloading
                    ):
                        self.toolwidgets[typewdg][toolname] = toolwdgcls(
                            dbaseparser=self.dbase,
                            mainifacewidget=self,
                            choosertreewidget=self.ElemtreeWidget,
                            parentwidget=None,
                        )

                    elif (
                        hasattr(self.wdgclasses[typewdg][toolname], "POSTPROTOOLNAME")
                        and fullloading
                    ):
                        self.toolwidgets[typewdg][toolname] = toolwdgcls(
                            dbaseparser=self.dbase,
                            mainifacewidget=self,
                            choosertreewidget=self.ElemtreeWidget,
                            parentwidget=None,
                        )

                    elif (
                        hasattr(self.wdgclasses[typewdg][toolname], "LOADFIRST")
                        and not fullloading
                    ):
                        toolwdglist.append(
                            toolwdgcls(
                                dbase=self.dbase,
                                dialog=self,
                                linkedtreewidget=self.ElemtreeWidget,
                                gpsutil=self.gpsutil,
                            )
                        )

                    else:  # tool dep
                        toolwdglist.append(
                            toolwdgcls(
                                dbase=self.dbase,
                                dialog=self,
                                linkedtreewidget=self.ElemtreeWidget,
                                gpsutil=self.gpsutil,
                            )
                        )

                except TypeError as e:
                    print(toolname, e)
                    # raise TypeError
                i += 1
                self.connector.updateProgressBar(i)
        """

        if not self.toolwidgets["desktop_loaded"] and fullloading:
            self.toolwidgets["desktop_loaded"] = True
        self.connector.closeProgressBar()

    def loadUiDesktop(self, fullloading=False):

        debug = False

        # init progress bar
        lenuifields = len(self.uidesktop)
        lenuipostpro = len(self.uipostpro)
        lenmenutool = len(self.menuclasses)
        self.connector.createProgressBar(
            self.tr("Loading widgets..."), lenuifields + lenuipostpro + lenmenutool
        )
        if self.dbase.qgsiface is not None:
            progressMessageBar = self.dbase.qgsiface.messageBar().createMessage(
                self.tr("Loading widgets...")
            )
            progress = QProgressBar()
            progress.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
            progressMessageBar.layout().addWidget(progress)
            if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                self.dbase.qgsiface.messageBar().pushWidget(
                    progressMessageBar, self.dbase.qgsiface.messageBar().INFO
                )
            else:
                self.dbase.qgsiface.messageBar().pushWidget(
                    progressMessageBar, qgis.core.Qgis.Info
                )

        else:
            progress = None

        # load menu ui
        i = 0
        for menuclasse in self.menuclasses:
            self.menutools.append(menuclasse(dbase=self.dbase, windowdialog=self))
            i += 1
            self.setLoadingProgressBar(progress, i)
            if debug:
                logger.debug(" loading %s", str(menuclasse))

        # load postpro ui
        for uidpostpr in self.uipostpro:
            # print('uidpostpr', uidpostpr)
            strtoexec = (
                "self."
                + uidpostpr.__name__.lower()
                + " = uidpostpr(dbase = self.dbase, dialog = self,linkedtreewidget = self.ElemtreeWidget, gpsutil = self.gpsutil)"
            )
            # print(strtoexec)
            exec(strtoexec)
            # print('test', eval('self.' + uidpostpr.__name__.lower()))
            strtoexec = (
                "self.tools.append(" + "self." + uidpostpr.__name__.lower() + ")"
            )
            # print(strtoexec)
            exec(strtoexec)

            if debug:
                logger.debug(" loading %s", str(uidpostpr.__name__))
            # print('ok')

            if False:
                self.tools.append(
                    uidpostpr(
                        dbase=self.dbase,
                        dialog=self,
                        linkedtreewidget=self.ElemtreeWidget,
                        gpsutil=self.gpsutil,
                    )
                )
            i += 1
            self.setLoadingProgressBar(progress, i)

        # load uidesktop ui
        for uidesktop in self.uidesktop:
            try:
                dbasename = uidesktop.dbasetablename
                self.dbase.dbasetables[dbasename]["widget"].append(
                    uidesktop(
                        dbase=self.dbase,
                        dialog=self,
                        linkedtreewidget=self.ElemtreeWidget,
                        gpsutil=self.gpsutil,
                    )
                )
                i += 1
                self.setLoadingProgressBar(progress, i)

            except AttributeError:
                pass

        if progress is not None:
            self.dbase.qgsiface.messageBar().clearWidgets()
        self.desktopuiloaded = True

    # *************************************************************
    # Settings menu
    # *************************************************************

    def ____________SettingsMenuActions(self):
        pass

    def connectToGPS(self):
        # self.actionHauteur_de_perche_GPS
        # ports = self.gpsutil.getAvailablePorts()
        # for portname, portid in ports:
        #     self.actionHauteur_de_perche_GPS.addAction(portname)
        if True:
            self.gpsutil.setCRS(self.qgiscanvas.dbaseqgiscrs)
            success = self.gpsutil.connectToGPS()

    def connectToPort(self):
        self.menuConnect_to_port.clear()
        ports = self.gpsutil.getAvailablePorts()
        for portname, portid in ports:
            newAct = QAction(portname, self)
            self.menuConnect_to_port.addAction(newAct)
            newAct.triggered.connect(self.portClicked)

    def portClicked(self):
        self.gpsutil.setCRS(self.qgiscanvas.dbaseqgiscrs)
        self.gpsutil.connectToPort(self.sender().text())

    def GPSconnected(self, success):
        if success:
            self.GPSlabel.setStyleSheet(
                "QLabel { background-color : rgb(85, 255, 0);  }"
            )  # vert
            self.GPSlabel.setText(self.tr("GPS connected"))
            self.GPSlabelperchheigh.setText(
                self.tr("Rod height : {}").format(self.gpsutil.hauteurperche)
            )
            self.GPSlabelperchheigh.setStyleSheet(
                "QLabel { background-color : rgb(85, 255, 0);  }"
            )
            self.GPSlabelprecision.setStyleSheet("QLabel { background-color : red;  }")
            self.GPSlabelprecision.setText(self.tr("Accuracy : error"))
            self.gpsutil.gstsentence.connect(self.displayGPSPrecision)
            self.actiontoobargeomaddGPSpoint.setEnabled(True)
        else:
            self.GPSlabel.setStyleSheet(
                "QLabel { background-color : rgba(0, 0, 0, 0);  }"
            )
            self.GPSlabel.setText(self.tr("GPS not connected"))
            self.GPSlabelperchheigh.setText(self.tr("Rod height : {}").format("/"))
            self.GPSlabelperchheigh.setStyleSheet(
                "QLabel { background-color : rgba(0, 0, 0, 0);  }"
            )
            self.GPSlabelprecision.setStyleSheet(
                "QLabel { background-color : rgba(0, 0, 0, 0);  }"
            )
            self.GPSlabelprecision.setText(self.tr("Accuracy : off"))
            self.actiontoobargeomaddGPSpoint.setEnabled(False)
            try:
                self.gpsutil.gstsentence.disconnect(self.displayGPSPrecision)
            except:
                pass

    def displayGPSPrecision(self, gpsdict):
        xprecision = gpsdict["xprecision"]
        yprecision = gpsdict["yprecision"]
        zprecision = gpsdict["zprecision"]

        try:
            totalprecision = round(
                math.sqrt(xprecision ** 2 + yprecision ** 2 + zprecision ** 2), 2
            )
            if totalprecision < 0.1:
                self.GPSlabelprecision.setStyleSheet(
                    "QLabel { background-color : rgb(85, 255, 0);  }"
                )  # vert
            elif totalprecision < 0.4:
                self.GPSlabelprecision.setStyleSheet(
                    "QLabel { background-color : yellow;  }"
                )
            elif totalprecision < 1.5:
                self.GPSlabelprecision.setStyleSheet(
                    "QLabel { background-color : rgb(255, 170, 0);  }"
                )
            else:
                self.GPSlabelprecision.setStyleSheet(
                    "QLabel { background-color : red;  }"
                )
            self.GPSlabelprecision.setText("Précision : " + str(totalprecision) + " m")

        except:
            self.GPSlabelprecision.setStyleSheet("QLabel { background-color : red;  }")
            self.GPSlabelprecision.setText("Précision : erreur")

    def setHauteurPerche(self):
        num, ok = QInputDialog.getDouble(
            self,
            self.tr("Rod height"),
            self.tr("Enter GPS rod height"),
            self.gpsutil.hauteurperche,
            decimals=2,
        )
        if ok:
            # self.dbase.hauteurperche = num
            self.gpsutil.hauteurperche = num

    def setImageDir(self):
        file = self.qfiledlg.getExistingDirectory(
            self,
            self.tr("Select Directory"),
            self.dbase.imagedirectory,
            QFileDialog.ShowDirsOnly,
        )
        if file:
            self.imagedirectory = file
            QtCore.QSettings().setValue("Lamia/picturepath", file)

    def openProjectDir(self):
        if not self.dbase.dbaseressourcesdirectory:
            return

        if platform.system() == "Linux":
            pass
        elif platform.system() == "Windows":
            subprocess.Popen(
                f'explorer "{os.path.realpath(os.path.abspath(self.dbase.dbaseressourcesdirectory))}"'
            )

    def openLamiaDir(self):
        if platform.system() == "Linux":
            pass
        elif platform.system() == "Windows":
            subprocess.Popen(
                f'explorer "{os.path.realpath(os.path.dirname(Lamia.qgisiface.__file__))}"'
            )

    def showHideQgisToolbars(self):
        if not len(self.toolbarsvisibility):
            self._unloadQgisToolbar()
        else:
            self._reloadQgisToolbar()

    def _unloadQgisToolbar(self):
        if not qgis.utils.iface:
            return

        for x in qgis.utils.iface.mainWindow().findChildren(QToolBar):
            self.toolbarsvisibility[x.objectName()] = x.isVisible()
            if x.objectName() not in [
                "Lamia",
                "mFileToolBar",
                "mSnappingToolBar",
                "lamiatoolBarFormCreation",
                "lamiatoolBarFormGeom",
                "lamiatoolbareditlayer",
                "lamiatoolBartools",
                "lamiatoolBarglobaltools",
            ]:
                x.setVisible(False)

    def _reloadQgisToolbar(self):
        if not qgis.utils.iface:
            return
        if not len(self.toolbarsvisibility):
            return
        for x in qgis.utils.iface.mainWindow().findChildren(QToolBar):
            if x.objectName() in self.toolbarsvisibility.keys():
                x.setVisible(self.toolbarsvisibility[x.objectName()])
        self.toolbarsvisibility = {}

    def _manageQgisDockWidgetOnStart(self):
        if not qgis.utils.iface:
            return
        for x in qgis.utils.iface.mainWindow().findChildren(QDockWidget):
            if x.objectName() == "GPSInformation":
                x.setVisible(True)
            elif x.objectName() == "LayerStyling":
                x.setVisible(False)

    # *************************************************************
    # About menu
    # *************************************************************

    def ____________AboutMenuActions(self):
        pass

    def openHelp(self):
        if platform.system() == "Linux":
            pass
        elif platform.system() == "Windows":
            httphelp = "https://artelia.github.io/Lamia/index.html"
            os.startfile(httphelp)

    def openSchema(self):
        if platform.system() == "Linux":
            pass
        elif platform.system() == "Windows":
            sender = f"{self.sender().objectName()}"
            if sender == "actionConceptual_model":
                filepath = os.path.join(
                    os.path.dirname(Lamia.__file__),
                    "doc",
                    "schemas",
                    "DBstructure-Relations.png",
                )
                os.startfile(filepath)
            elif sender == "actionViews":
                filepath = os.path.join(
                    os.path.dirname(Lamia.__file__),
                    "doc",
                    "schemas",
                    "DBstructure-Views.png",
                )
                os.startfile(filepath)

    def openTablesAndFields(self):
        # self.tablefielddialog.run()
        # self.tablefielddialog.exec_()
        # self.tablefielddialog.setWindowModality(QtCore.Qt.Modal)  # NonModal
        self.tablefielddialog.dbase = self.dbase
        self.tablefielddialog.update()
        self.tablefielddialog.setModal(False)
        self.tablefielddialog.show()

    def reportBug(self):
        webbrowser.open("mailto:lamia@arteliagroup.com&subject=Lamia bug report", new=1)

    # *************************************************************
    # toolbar
    # *************************************************************

    def ____________ToolBarActions(self):
        pass

    def _connectToolBar(self):
        self.actiontoolbarnew.triggered.connect(self.toolbarNew)
        self.actiontoolbarmagic.triggered.connect(self.toolbarMagic)
        self.actiontoolbarundo.triggered.connect(self.toolbarUndo)
        self.actiontoolbardelete.triggered.connect(self.toolbarDelete)
        self.actiontoolbarzoomto.triggered.connect(self.toolbarZoomTo)
        self.actiontoolbarzoomto.triggered.connect(self.toolbarZoomTo)
        self.actiontoolbarlinkeditor.triggered.connect(self.toolbarEditLink)
        self.actiontoolbarsave.triggered.connect(self.toolbarSave)

        self.actiontoobargeomnewpoint.triggered.connect(self.toolbarGeom)
        self.actiontoobargeomnewline.triggered.connect(self.toolbarGeom)
        self.actiontoobargeomnewpolygon.triggered.connect(self.toolbarGeom)
        self.actiontoobargeomaddpoint.triggered.connect(self.toolbarGeom)
        self.actiontoobargeomaddGPSpoint.triggered.connect(self.toolbarGeomAddGPS)

        self.actiontoobargeomeditlayer.triggered.connect(
            self.addRawLayerInCanvasForEditing
        )
        self.actiontoolbarlayersave.triggered.connect(
            lambda: self.saveRawLayerInCanvasForEditing()
        )
        self.actiontoolbarlayerundo.triggered.connect(
            lambda: self.saveRawLayerInCanvasForEditing(savechanges=False)
        )

        self.actiontoolbartoolsprint.triggered.connect(self.printCurrentFormWidget)
        self.actiontoolbartoolsprint.setEnabled(False)
        self.actiontoolbartoolscamera.triggered.connect(self.openCamera)

    def toolbarNew(self):
        logging.getLogger("Lamia_unittest").info("called")
        if self.currenttoolwidget and hasattr(self.currenttoolwidget, "toolbarNew"):
            self.currenttoolwidget.toolbarNew()
        if self.currentchoosertreewidget:
            self.currentchoosertreewidget.toolbarNew()

    def toolbarMagic(self):
        if self.currenttoolwidget and hasattr(self.currenttoolwidget, "toolbarMagic"):
            self.currenttoolwidget.toolbarMagic()

    def toolbarUndo(self):
        logging.getLogger("Lamia_unittest").info("called")
        if self.currenttoolwidget and hasattr(self.currenttoolwidget, "toolbarUndo"):
            self.currenttoolwidget.toolbarUndo()
        if self.currentchoosertreewidget:
            self.currentchoosertreewidget.toolbarUndo()

    def toolbarDelete(self):
        logging.getLogger("Lamia_unittest").info("called")
        if self.currenttoolwidget and hasattr(self.currenttoolwidget, "toolbarDelete"):
            self.currenttoolwidget.toolbarDelete()
        if self.currentchoosertreewidget:
            self.currentchoosertreewidget.toolbarDelete()

    def toolbarZoomTo(self):
        if self.currenttoolwidget and hasattr(self.currenttoolwidget, "toolbarZoomTo"):
            self.currenttoolwidget.toolbarZoomTo()

    def toolbarEditLink(self):
        if self.currenttoolwidget and hasattr(self.currenttoolwidget, "toolbarZoomTo"):
            self.currenttoolwidget.toolbarEditLink()

    def toolbarSave(self):
        logging.getLogger("Lamia_unittest").info("called")
        if self.currenttoolwidget and hasattr(self.currenttoolwidget, "toolbarSave"):
            self.currenttoolwidget.toolbarSave()
        if self.currentchoosertreewidget:
            self.currentchoosertreewidget.toolbarSave()

    def toolbarGeom(self):
        logging.getLogger("Lamia_unittest").info("called")
        if self.currenttoolwidget and hasattr(self.currenttoolwidget, "toolbarGeom"):
            self.currenttoolwidget.toolbarGeom()

    def toolbarGeomAddGPS(self):
        logging.getLogger("Lamia_unittest").info("called")
        if self.currenttoolwidget and hasattr(
            self.currenttoolwidget, "toolbarGeomAddGPS"
        ):
            self.currenttoolwidget.toolbarGeomAddGPS()

    def addRawLayerInCanvasForEditing(self):
        currentdbasetablename = self.currenttoolwidget.DBASETABLENAME
        self.qgiscanvas.addRawLayerInCanvasForEditing(self.dbase, currentdbasetablename)
        for child in self.findChildren((QFrame, QToolBar)):
            child.setEnabled(False)
        self.lamiatoolbareditlayer.setEnabled(True)

    def saveRawLayerInCanvasForEditing(self, savechanges=True):
        self.qgiscanvas.saveRawLayerInCanvasForEditing(self.dbase, savechanges)
        for child in self.findChildren((QFrame, QToolBar)):
            child.setEnabled(True)

    def printCurrentFormWidget(self):
        self.currenttoolwidget.printWidget()

    def openCamera(self):

        if platform.system() == "Linux":
            pass
        elif platform.system() == "Windows":
            subprocess.run("start microsoft.windows.camera:", shell=True)

    # *************************************************************
    # menu
    # *************************************************************

    def ____________MenuActions(self):
        pass

    def _connectMenuAndOthers(self):
        # file menu
        self.actionNouvelle_base.triggered.connect(self.newDBase)
        self.actionSpatialite.triggered.connect(self.loadDBase)
        self.actionPostgis.triggered.connect(self.loadDBase)
        self.actionImporter_et_ajouter_la_base.triggered.connect(self.addDBase)
        self.action_pushdb.triggered.connect(self.pushDBase)
        self.action_pulldb.triggered.connect(lambda: self.pullDBase())

        # visual mode menu
        self.actionModeExpert.triggered.connect(self.setVisualMode)
        self.actionTTC.triggered.connect(self.setVisualMode)
        self.actionModeTerrain.triggered.connect(self.setVisualMode)
        self.actionPosttraitement.triggered.connect(self.setVisualMode)
        # settings menu
        self.actionHauteur_de_perche_GPS.triggered.connect(self.setHauteurPerche)
        self.menuConnect_to_port.aboutToShow.connect(self.connectToPort)
        self.action_GPSConnection.triggered.connect(self.connectToGPS)
        self.gpsutil.GPSConnected.connect(self.GPSconnected)
        self.action_Repertoire_photo.triggered.connect(self.setImageDir)
        self.actionOpen_project_directory.triggered.connect(self.openProjectDir)
        self.actionOpen_Lamia_directory.triggered.connect(self.openLamiaDir)
        self.actionShow_Hide_QGis_toolbars.triggered.connect(self.showHideQgisToolbars)

        # about menu
        self.actionAide.triggered.connect(self.openHelp)
        self.actionConceptual_model.triggered.connect(self.openSchema)
        self.actionViews.triggered.connect(self.openSchema)
        self.actionTables_and_fields.triggered.connect(self.openTablesAndFields)
        self.actionReport_bug.triggered.connect(self.reportBug)

        # others
        self.pushButton_selectfeat.clicked.connect(self.selectFeature)
        self.pushButton_qgspan.clicked.connect(self.panCanvas)

        # on exit qgis : restore toolbars
        if qgis.utils.iface is not None:
            qgis.core.QgsProject.instance().cleared.connect(self._reloadQgisToolbar)

    def panCanvas(self):
        self.qgiscanvas.panCanvas()

    def selectFeature(self):

        pointemitter = self.qgiscanvas.pointEmitter
        try:
            pointemitter.canvasClicked.disconnect(self.selectPickedFeature)
        except TypeError:
            pass
        # try:
        #     self.qgiscanvas.canvas.mapToolSet.disconnect(self.qgiscanvas.toolsetChanged)
        # except TypeError:
        #     pass
        pointemitter.canvasClicked.connect(self.selectPickedFeature)
        # self.qgiscanvas.canvas.mapToolSet.connect(self.qgiscanvas.toolsetChanged)
        self.qgiscanvas.canvas.setMapTool(pointemitter)

    def selectPickedFeature(self, point, tablename=None):
        debug = False
        if debug:
            logging.getLogger("Lamia_unittest").debug("Start %s", str(point))

        if self.currenttoolwidget is None:
            return

        addselection = False
        modifiers = QApplication.keyboardModifiers()
        # print('modif')
        # if modifiers == QtCore.Qt.ShiftModifier:
        if modifiers == QtCore.Qt.ControlModifier:
            # print('Ctrl+Click')
            addselection = True

        # get parent
        parentwdg = self.currenttoolwidget
        while parentwdg.parentWidget is not None:
            parentwdg = parentwdg.parentWidget

        if hasattr(parentwdg, "selectPickedFeature"):
            parentwdg.selectPickedFeature(point)
            return

        if not (
            hasattr(parentwdg, "DBASETABLENAME")
            and parentwdg.DBASETABLENAME is not None
        ):
            return
        # getCurrentLayer
        tablename = parentwdg.DBASETABLENAME
        fieldconstraint = parentwdg.TABLEFILTERFIELD
        # qgslayer = self.qgiscanvas.layers[tablename]['layerqgis']
        # point2 = self.qgiscanvas.pointEmitter.toLayerCoordinates(qgslayer, point)
        nearestpk, dist = self.qgiscanvas.getNearestPk(
            tablename,
            point,  # former point2
            comefromcanvas=True,
            fieldconstraint=fieldconstraint,
        )
        if debug:
            logging.getLogger("Lamia_unittest").debug("nearestpk %s", str(nearestpk))

        if nearestpk is None:  # no element in table
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

    def ____________devFeature(self):
        pass

    def hideDevQWidgets(self):
        if qgis.utils.iface is None:
            return

        self.menuConnect_to_port.setEnabled(False)
