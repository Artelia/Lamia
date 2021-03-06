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

import os, sys, logging, glob, inspect, importlib

import qgis, qgis.core
from qgis.PyQt import QtGui, QtCore, QtXml
from qgis.PyQt.QtPrintSupport import QPrinter

from ..lamianetworkx.lamianetworkx import NetWorkCore
from Lamia.qgisiface.iface.qgscanvas.ifaceqgiscanvas import QgisCanvas
from Lamia.api.dbasemanager.dbaseparserfactory import DBaseParserFactory
from Lamia.qgisiface.iface.qgsconnector.ifaceqgisconnector import QgisConnector


class ReportCore:

    POSTPROTOOLNAME = "reporttools"
    LAUNCHINQTHREAD = True

    def __init__(self, dbaseparser, messageinstance=None):
        # super(ExportShapefileTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil, parentwidget, parent=parent)
        self.dbase = dbaseparser
        self.messageinstance = messageinstance
        self.tooldir = os.path.join(
            os.path.dirname(__file__), self.dbase.worktype.lower()
        )

        self.tasks = []

        self.confdataplugin = os.path.join(
            os.path.dirname(__file__), self.dbase.worktype.lower()
        )
        self.confdataproject = os.path.join(
            self.dbase.dbaseressourcesdirectory, "config", self.POSTPROTOOLNAME
        )

        self.printingthread = printingThread(self)

    def runReport(
        self, destinationfile, reportconffilename, pkzonegeos=[], pklist=None
    ):
        if os.path.isfile(
            reportconffilename
        ):  # complete path is given in exportconffilepath
            tabletypepath = reportconffilename
        else:  # just filename is given in exportconffilepath
            tabletypepath = os.path.join(self.tooldir, reportconffilename + ".txt")

        self.printingthread.launchThread(
            reportcore=self,
            # windowdialog=self.windowdialog,
            parentprintPDFworker=None,
            reportconffilename=reportconffilename,
            # confData=self.confData,
            pdffile=destinationfile,
            # reporttype=reporttype,
            # templatedir=createfilesdir ,
            pklist=pklist,
            pkzonegeolist=pkzonegeos,
        )
        """
        if self.LAUNCHINQTHREAD:
            self.printingthread.launchThread(reportcore=self,
                                                            #windowdialog=self.windowdialog,
                                                            parentprintPDFworker=None,
                                                            reportconffilename=reportconffilename,
                                                            #confData=self.confData,
                                                            pdffile=destinationfile,
                                                            #reporttype=reporttype,
                                                            #templatedir=createfilesdir ,
                                                            pklist=pklist,
                                                            pkzonegeolist=pkzonegeos)


            # self.tasks.append( printingThread(reportcore=self,
            #                                     #windowdialog=self.windowdialog,
            #                                     parentprintPDFworker=None,
            #                                     reportconffilename=reportconffilename,
            #                                     #confData=self.confData,
            #                                     pdffile=destinationfile,
            #                                     #reporttype=reporttype,
            #                                     #templatedir=createfilesdir ,
            #                                     pklist=pklist,
            #                                     pkzonegeolist=pkzonegeos)
            # )

        else:
            self.impressionpdfworker = printPDFBaseWorker(reportcore=self,
                                                            #windowdialog=self.windowdialog,
                                                            parentprintPDFworker=None,
                                                            reportconffilename=reportconffilename,
                                                            #confData=self.confData,
                                                            pdffile=destinationfile,
                                                            #reporttype=reporttype,
                                                            #templatedir=createfilesdir ,
                                                            pklist=pklist,
                                                            pkzonegeolist=pkzonegeos)

            self.impressionpdfworker.work()
        """

    def getcompletePath(self, reportconffilename):
        currentfilepath = None
        if reportconffilename is not None and len(reportconffilename) > 0:
            if reportconffilename[0] == self.projectcharacter:
                currentfilepath = os.path.join(
                    self.confdataproject, reportconffilename[1:] + self.fileext
                )
            else:
                currentfilepath = os.path.join(
                    self.confdataplugin, reportconffilename + self.fileext
                )

        return currentfilepath

    def new(self, confpath):
        if not os.path.exists(self.confdataproject):
            os.mkdir(self.confdataproject)

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

    """
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

        self.impressionpdfworker = printPDFBaseWorker(dbase=self.dbase,
                                                    windowdialog=self.windowdialog,
                                                    parentprintPDFworker=None,
                                                    confData=self.confData,
                                                    pdffile=pdffile,
                                                    reporttype=reporttype,
                                                    templatedir=createfilesdir ,
                                                    idlist=None)

        self.impressionpdfworker.work()
    """


class printingThread(QtCore.QObject):

    finished = QtCore.pyqtSignal()

    def __init__(self, reportcore):
        QtCore.QObject.__init__(self)
        self.reportcore = reportcore
        self.printthread = QtCore.QThread()
        self.reportthreaded = self.reportcore.LAUNCHINQTHREAD

    def launchThread(self, **kwargs):

        if self.reportthreaded and not self.printthread.isRunning():

            self.impressionpdfworker = printPDFBaseWorker(**kwargs)
            # self.printthread = QtCore.QThread()
            self.impressionpdfworker.moveToThread(self.printthread)
            self.printthread.started.connect(self.impressionpdfworker.work)

            self.impressionpdfworker.initprogressbar.connect(
                self.reportcore.messageinstance.createProgressBar
            )
            self.impressionpdfworker.updateprogressbar.connect(
                self.reportcore.messageinstance.updateProgressBar
            )
            self.impressionpdfworker.closeprogressbar.connect(
                self.reportcore.messageinstance.closeProgressBar
            )
            self.impressionpdfworker.errormessage.connect(
                self.reportcore.messageinstance.showErrorMessage
            )
            self.impressionpdfworker.finished.connect(self.finished)

            self.printthread.start()

        elif not self.reportthreaded:
            self.impressionpdfworker = printPDFBaseWorker(**kwargs)
            self.impressionpdfworker.initprogressbar.connect(
                self.reportcore.messageinstance.createProgressBar
            )
            self.impressionpdfworker.updateprogressbar.connect(
                self.reportcore.messageinstance.updateProgressBar
            )
            self.impressionpdfworker.closeprogressbar.connect(
                self.reportcore.messageinstance.closeProgressBar
            )
            self.impressionpdfworker.errormessage.connect(
                self.reportcore.messageinstance.showErrorMessage
            )

            self.impressionpdfworker.work()

            self.reportcore.messageinstance.showNormalMessage("Report ready !")

    def finished(self):
        self.impressionpdfworker.deleteLater()
        self.printthread.quit()
        self.printthread.wait()
        self.printthread.deleteLater()

        self.printthread = QtCore.QThread()  # prepare new thread for next print

        self.reportcore.messageinstance.showNormalMessage("Report ready !")


class printingTask(qgis.core.QgsTask):

    emittxt = QtCore.pyqtSignal(str)

    def __init__(self, description, **kwargs):
        qgis.core.QgsTask.__init__(self, description)
        # self.time= time
        # self.kwargs = kwargs
        print(kwargs)
        self.impressionpdfworker = printPDFBaseWorker(**kwargs)
        self.emittxt.connect(self.show)

    def run(self):
        # logging.getLogger("Lamia_unittest").debug('run')
        # self.emittxt.emit('run')
        self.impressionpdfworker.work()
        # self.completed()
        return True

    def show(self, txt):
        logging.getLogger("Lamia_unittest").debug(txt)


# class printPDFBaseWorker(object):
class printPDFBaseWorker(QtCore.QObject):

    finished = QtCore.pyqtSignal()
    initprogressbar = QtCore.pyqtSignal(str, int)
    updateprogressbar = QtCore.pyqtSignal(int)
    closeprogressbar = QtCore.pyqtSignal()
    errormessage = QtCore.pyqtSignal(str)

    """
    def __init__(self,
                 dbase=None,
                 windowdialog=None,
                 parentprintPDFworker=None,
                 confData=None,
                 pdffile=None,
                 reporttype=None,
                 templatedir=None,
                 idlist=None):
    """

    def __init__(
        self,
        reportcore=None,
        # windowdialog=self.windowdialog,
        parentprintPDFworker=None,
        reportconffilename=None,
        # confData=self.confData,
        pdffile=None,
        # reporttype=reporttype,
        # templatedir=createfilesdir ,
        # idlist=None,
        pklist=None,
        pkzonegeolist=[],
    ):

        # if parentprintPDFworker:
        #     QtCore.QObject.__init__(self, parent=parentprintPDFworker)
        # else:
        QtCore.QObject.__init__(self)

        self.enablemessages = False
        self.reportcore = reportcore
        self.parentprintPDFworker = parentprintPDFworker

        # self.heightpx = 0               #the height to communicate to childprint for starting
        # self.childstartheightpx = None               #the height to communicate to childprint for starting
        # self.currentpageheightpx = 0    #the height for starting print for this print
        self.currentstartheightpx = None  # the height for starting print for this print
        self.pageheightpx = None  # this print page height (without parent print)

        if self.parentprintPDFworker is None:
            self.dbase = self.reportcore.dbase
            # self.dbase = DBaseParserFactory(self.reportcore.dbase.TYPE,self.reportcore.messageinstance).getDbaseParser()
            # self.dbase.loadDBase(**self.reportcore.dbase.connectconf)
            # self.dbase.createDBase(crs=crsnumber,
            #                         worktype=worktype,
            #                         dbaseressourcesdirectory=resdir,
            #                         variante=vartype,
            #                         slfile=spatialitefile)
            # self.loadDBase(dbtype='Spatialite',
            #                 slfile=spatialitefile)

            # self.messageinstance = self.reportcore.messageinstance

            self.pklist = pklist
            self.reportconffilename = reportconffilename
            self.pdffile = pdffile
            self.pkzonegeolist = pkzonegeolist
            # self.qgiscanvas = QgisCanvas()
            # self.qgiscanvas.createLayers(self.dbase)
            # if self.dbase.base3version :
            #     self.qgiscanvas.applyStyle(self.dbase.worktype, '0_default')
            # else:
            #     self.qgiscanvas.applyStyle(self.dbase.worktype, '0_Defaut')
            # self.networkcore = NetWorkCore(self.dbase, self.messageinstance, self.qgiscanvas)
            # self.project = qgis.core.QgsProject.instance()

            # self.printer = QPrinter()
            # self.painter = QtGui.QPainter()
            # #self.confData = confData
            # self.confData, self.templatedir = self.createconfData(self.reportconffilename)

            # strtoexec = '..{}.lamiareportworktypefunc'.format(self.dbase.worktype.lower())
            # self.addonimagesmodule = importlib.import_module(strtoexec, package=self.__module__)

        else:
            self.dbase = parentprintPDFworker.dbase
            self.messageinstance = parentprintPDFworker.messageinstance
            self.pklist = None
            self.pdffile = parentprintPDFworker.pdffile
            self.qgiscanvas = parentprintPDFworker.qgiscanvas
            self.networkcore = parentprintPDFworker.networkcore
            self.project = parentprintPDFworker.project

            self.printer = parentprintPDFworker.printer
            self.painter = parentprintPDFworker.painter
            # self.confData = parentprintPDFworker.confData
            self.reportconffilename = self.parentprintPDFworker.atlasconfData[
                "childprint"
            ]["confname"]
            self.confData, self.templatedir = self.createconfData(
                self.reportconffilename
            )
            # self.parentheightpx = parentprintPDFworker.parentheightpx

        """
        self.canvas = self.dbase.canvas
        self.reporttype = reporttype
        self.pdffile = pdffile
        """
        self.currentid = None
        self.currentimageItem = None

        self.presetscales = [100, 500, 1000, 2500, 5000, 10000, 25000, 50000]

        self.logger = logging.getLogger("Lamia_unittest")

        # self.confData = None
        # self.createfilesdir = None
        self.idecalage = 0
        """
        if self.parentprintPDFworker is None:
            self.printer = QPrinter()
            self.painter = QtGui.QPainter()
            #self.confData = confData
            self.confData, self.templatedir = self.createconfData(self.reportconffilename)
            #self.createfilesdir = templatedir
            # self.parentheightpx = None
        else:
            self.printer = parentprintPDFworker.printer
            self.painter = parentprintPDFworker.painter
            #self.confData = parentprintPDFworker.confData
            self.confData, self.templatedir = self.createconfData(self.reportconffilename)
            #self.createfilesdir = parentprintPDFworker.createfilesdir
            # self.parentheightpx = parentprintPDFworker.parentheightpx
        """

        # self.postInit()
        # self.createconfData()

    def work(self):
        """
        Méthode principale - génère le pdf
        :return:
        """
        if qgis.utils.iface is not None:
            debug = False
        else:
            debug = False  # True False

        self.initprogressbar.emit("Report preparation ...", 0)

        if (
            self.parentprintPDFworker is None
        ):  # create specific dbase for specific printing thread
            self.project = qgis.core.QgsProject.instance()
            # self.messageinstance = QgisConnector()
            self.messageinstance = self.reportcore.messageinstance
            self.dbase = DBaseParserFactory(self.reportcore.dbase.TYPE).getDbaseParser()
            self.dbase.loadDBase(**self.reportcore.dbase.connectconf)

            self.canvas = qgis.gui.QgsMapCanvas()
            self.canvas.enableAntiAliasing(True)
            dbaseqgiscrs = qgis.core.QgsCoordinateReferenceSystem()
            dbaseqgiscrs.createFromString("EPSG:" + str(self.dbase.crsnumber))
            # canvascrs = qgis.core.QgsCoordinateReferenceSystem()
            # canvascrs.createFromString('EPSG:2154')
            self.canvas.setDestinationCrs(dbaseqgiscrs)

            self.qgiscanvas = QgisCanvas(canvas=self.canvas)
            self.qgiscanvas.createLayers(self.dbase)
            if self.dbase.base3version:
                # self.qgiscanvas.applyStyle(self.dbase.worktype, "0_default")
                self.qgiscanvas.applyStyle(self.dbase, "0_default")
            else:
                # self.qgiscanvas.applyStyle(self.dbase.worktype, "0_Defaut")
                self.qgiscanvas.applyStyle(self.dbase, "0_Defaut")
            self.networkcore = NetWorkCore(
                self.dbase, self.messageinstance, self.qgiscanvas
            )

            self.networkcore = NetWorkCore(
                self.dbase, self.messageinstance, self.qgiscanvas
            )

            self.printer = QPrinter()
            self.painter = QtGui.QPainter()
            # self.confData = confData
            self.confData, self.templatedir = self.createconfData(
                self.reportconffilename
            )

            strtoexec = "..{}.lamiareportworktypefunc".format(
                self.dbase.worktype.lower()
            )
            self.addonimagesmodule = importlib.import_module(
                strtoexec, package=self.__module__
            )

        else:
            self.messageinstance = self.parentprintPDFworker.messageinstance
            self.dbase = self.parentprintPDFworker.dbase
            self.qgiscanvas = self.parentprintPDFworker.qgiscanvas
            self.networkcore = self.parentprintPDFworker.networkcore

        self.printtype = "atlas"  # report atlas
        if debug:
            logging.getLogger("Lamia_unittest").debug("started")
        mapsettings = qgis.core.QgsMapSettings()
        mapsettings.setDestinationCrs(self.qgiscanvas.dbaseqgiscrs)
        layertoremove = []
        self.atlasconfData = self.confData

        if debug:
            logging.getLogger("Lamia_unittest").debug(
                "self.atlasconfData %s", str(self.atlasconfData)
            )

        # ********************* create composition *****************************
        if self.printtype == "atlas":
            newComposition = self.createComposition(mapsettings)
        elif self.printtype == "report":
            newComposition = self.createReport()
        if debug:
            logging.getLogger("Lamia_unittest").debug("template loaded")

        # ********************* set atlas and linked composeritem *****************************
        coveragelayer = self.setCoverageLayer()
        layertoremove.append(coveragelayer)
        mainprinter = None
        if self.printtype == "atlas":
            # atlas = self.setAtlasLayer(newComposition,coveragelayer )
            mainprinter = self.setAtlasLayer(newComposition, coveragelayer)
        elif self.printtype == "report":
            mainprinter = newComposition
            reportmapsection = self.setSectionLayer(newComposition, coveragelayer)
        if debug:
            logging.getLogger("Lamia_unittest").debug("atlas driven loaded")

        # ********************* fill composer map with layers *****************************
        if self.printtype == "atlas":
            layers = self.fillComposerMapsWihLayers(newComposition, coveragelayer)
        elif self.printtype == "report":
            layers = self.fillComposerMapsWihLayers(
                reportmapsection.body(), coveragelayer
            )

        for layer in layers:
            layertoremove.append(layer)
        if debug:
            logging.getLogger("Lamia_unittest").debug("composer map fill")

        # ********************* %lamia var in composer *****************************
        if self.printtype == "atlas":
            dictfields = self.getLamiaVarInComposition(newComposition)
        elif self.printtype == "report":
            dictfields = self.getLamiaVarInComposition(reportmapsection.body())
        if debug:
            logging.getLogger("Lamia_unittest").debug("lamia var read")

        # ********************* ordering pks for pdf *****************************
        if self.pklist is None:
            pksforreportdict = self.getOrderedPksForAtlas(coveragelayer)
        else:
            # idsforreportdict = self.idlist
            pksforreportdict = self.pklist

        if debug:
            logging.getLogger("Lamia_unittest").debug(
                "pksforreportdict %s", str(pksforreportdict)
            )

        # ********************* progress bar *****************************
        self.closeprogressbar.emit()
        lenpks = 0
        for zonegeopk, pks in pksforreportdict.items():
            lenpks += len(pks)
        # progress = self.messageinstance.initProgressBar(pksforreportdict)
        # if self.enablemessages: self.messageinstance.createProgressBar(inittext="Generation du pdf...", maxvalue=lenpks)
        self.initprogressbar.emit("Report printing...", lenpks)
        # print('Generation du pdf')

        if self.printtype == "atlas":
            self.atlasPrinting(
                mainprinter, newComposition, coveragelayer, pksforreportdict, dictfields
            )
        elif self.printtype == "report":
            self.reportPrinting(mainprinter)

        for rastlayer in layertoremove:
            self.project.removeMapLayer(rastlayer)

        if self.parentprintPDFworker is None:
            self.closeprogressbar.emit()
            self.finished.emit()

    def reportPrinting(self, mainprinter):
        mainprinter.beginRender()
        settings = qgis.core.QgsLayoutExporter.PdfExportSettings()
        printsettings = qgis.core.QgsLayoutExporter.PrintExportSettings()

        self.printer.setOutputFormat(QPrinter.PdfFormat)
        self.printer.setOutputFileName(self.pdffile)
        # paperWidth = newComposition.pageCollection().page(0).pageSize().width()
        # paperHeight = newComposition.pageCollection().page(0).pageSize().height()
        # if debug: self.logger.debug('print size %s %s', str(paperWidth), str(paperHeight))
        # self.printer.setPaperSize(QtCore.QSizeF(paperWidth, paperHeight), QPrinter.Millimeter)
        self.printer.setFullPage(True)
        printReady = self.painter.begin(self.printer)
        # if debug: self.logger.debug('print ready %s', printReady)

        indexpagetotal = -1

        for zonegeopk in pksforreportdict.keys():
            for indexpage, featpk in enumerate(pksforreportdict[zonegeopk]):
                indexpagetotal += 1
                self.currentatlasfeat = coveragelayer.getFeature(featpk)
                # atlas.seekTo(self.currentatlasfeat)

                while mainprinter.next():
                    # print(mainprinter.layout())
                    exporter = qgis.core.QgsLayoutExporter(mainprinter.layout())
                    exporter.renderPage(self.painter, numpage)
                    exporter.print(self.printer, printsettings)
                    # print(mainprinter.layout().reportContext().feature().attributes())

                    numpage += 1

        mainprinter.endRender()

    def atlasPrinting(
        self, atlas, newComposition, coveragelayer, pksforreportdict, dictfields
    ):

        if qgis.utils.iface is not None:
            debug = False
            debugscale = False
            stop10 = None
        else:
            debug = False  # True False
            debugscale = False
            stop10 = None

        # *********************************************************************
        # ********************* begin printing  *****************************
        # *********************************************************************
        # try:
        atlas.beginRender()
        # mainprinter.beginRender()
        exporter = self.initPrinterAndPainter(newComposition)
        # exporter = self.initPrinterAndPainter(mainprinter)

        idecalage = 0
        compt = 0

        # * initialize var for page dimension in case of child print
        self.initHeightpx(newComposition)

        indexpagetotal = -1

        # for zonegeoid in idsforreportdict.keys():
        for zonegeopk in pksforreportdict.keys():

            # set generalmap extent to zonegeo
            if stop10 is not None and indexpagetotal >= stop10:
                break

            if zonegeopk > 0:
                self.setGeneralMapExtentByZonegeo(newComposition, zonegeopk)
                if debug:
                    logging.getLogger("Lamia_unittest").debug(
                        "setGeneralMapExtentByZonegeo done"
                    )

            # for indexpage, featid in enumerate(pksforreportdict[zonegeopk]):
            for indexpage, featpk in enumerate(pksforreportdict[zonegeopk]):
                indexpagetotal += 1
                if debug:
                    logging.getLogger("Lamia_unittest").debug(
                        "featpk %s , indexpage %s", str(featpk), str(indexpagetotal)
                    )
                # print('indexpagetotal == stop10',indexpagetotal >= stop10)

                if stop10 is not None and indexpagetotal >= stop10:
                    break

                self.currentid = featpk
                compt += 1
                if self.parentprintPDFworker is None:
                    # self.setLoadingProgressBar(progress, compt)
                    # if self.enablemessages: self.messageinstance.updateProgressBar(compt)
                    self.updateprogressbar.emit(compt)
                    # print('Generation du pdf', compt)

                self.currentatlasfeat = coveragelayer.getFeature(featpk)

                if self.atlasconfData["spatial"]:

                    if debugscale:
                        logging.getLogger("Lamia_unittest").debug(
                            "Boundingbox %s",
                            str(
                                self.currentatlasfeat.geometry()
                                .boundingBox()
                                .toString()
                            ),
                        )
                    geombb = self.currentatlasfeat.geometry().boundingBox()
                    if (
                        self.currentatlasfeat.geometry().boundingBox().toString()
                        == "Empty"
                    ):  # point in linelayer

                        # for mapname in reportdic['atlasdriven']:
                        for mapname in self.atlasconfData["atlasdrivemap"]:
                            # newComposition.getComposerItemById(mapname).setAtlasScalingMode(qgis.core.QgsComposerMap.Fixed)
                            newComposition.itemById(mapname).setAtlasScalingMode(
                                qgis.core.QgsLayoutItemMap.Fixed
                            )
                            # newComposition.getComposerItemById(mapname).setNewScale(reportdic['atlasdrivenminscale'])
                            # newComposition.getComposerItemById(mapname).setNewScale(self.atlasconfData['atlasdrivemap'][mapname]['minscale'])
                            newComposition.itemById(mapname).setScale(
                                self.atlasconfData["atlasdrivemap"][mapname]["minscale"]
                            )
                            # print('***', mapname, self.atlasconfData['atlasdrivemap'][mapname]['minscale'])

                    # else:
                    #    #for mapname in reportdic['atlasdriven']:
                    #    for mapname in self.atlasconfData['atlasdrivemap']:
                    #        #newComposition.itemById(mapname).setExtent(geombb)
                    #        # newComposition.getComposerItemById(mapname).setAtlasScalingMode(reportdic['atlastypescale'])
                    #        #newComposition.getComposerItemById(mapname).setAtlasScalingMode(self.atlasconfData['atlasdrivemap'][mapname]['typescale'])
                    #        newComposition.itemById(mapname).setAtlasScalingMode(self.atlasconfData['atlasdrivemap'][mapname]['typescale'])
                    #        newComposition.itemById(mapname).refresh()
                    #
                    #        if debugscale: logging.getLogger("Lamia_unittest").debug('scale %s', str(newComposition.itemById(mapname).scale()))

                atlas.seekTo(self.currentatlasfeat)
                atlas.refreshCurrentFeature()

                # currentfeature = atlasfeat
                if debug:
                    logging.getLogger("Lamia_unittest").debug(
                        "feat attr : %s",
                        str([field.name() for field in self.currentatlasfeat.fields()]),
                    )
                if debug:
                    logging.getLogger("Lamia_unittest").debug(
                        "feat attr : %s", str(self.currentatlasfeat.attributes())
                    )

                # check atlasdriven map scale

                for mapname in self.atlasconfData["atlasdrivemap"]:
                    currentmapscale = newComposition.itemById(mapname).scale()

                    if debugscale:
                        logging.getLogger("Lamia_unittest").debug(
                            "currentscale %s", str(currentmapscale)
                        )
                    if debugscale:
                        logging.getLogger("Lamia_unittest").debug(
                            "minscale %s",
                            str(
                                self.atlasconfData["atlasdrivemap"][mapname]["minscale"]
                            ),
                        )

                    if (
                        currentmapscale
                        < self.atlasconfData["atlasdrivemap"][mapname]["minscale"]
                    ):
                        newComposition.itemById(mapname).setScale(
                            self.atlasconfData["atlasdrivemap"][mapname]["minscale"]
                        )
                        newComposition.itemById(mapname).refresh()
                    elif currentmapscale > 100000.0:
                        newComposition.itemById(mapname).setScale(
                            self.atlasconfData["atlasdrivemap"][mapname]["minscale"]
                        )
                        newComposition.itemById(mapname).refresh()

                    # do lamia auto scale ... don't understand qgis way
                    if True:
                        # geombb = self.currentatlasfeat.geometry().boundingBox()
                        # newComposition.itemById(mapname).setExtent(geombb)
                        # currentmapscale = newComposition.itemById(mapname).scale()
                        if int(currentmapscale) not in self.presetscales:
                            for scale in self.presetscales:
                                if currentmapscale >= scale:
                                    continue
                                else:
                                    if debugscale:
                                        logging.getLogger("Lamia_unittest").debug(
                                            "adjust scale %s", str(scale)
                                        )
                                    newComposition.itemById(mapname).setScale(
                                        scale, True
                                    )
                                    # newComposition.itemById(mapname).setAtlasMargin(5.)
                                    newComposition.itemById(mapname).refresh()
                                    break

                self.processImages(newComposition, atlas, self.currentatlasfeat)

                self.processLamiaVars(newComposition, dictfields, self.currentatlasfeat)

                self.printAtlasPage(
                    newComposition, exporter, indexpagetotal, indexpage, idecalage
                )

                if False and sys.version_info.major == 3:
                    for mapname in self.atlasconfData["atlasdrivemap"]:
                        # currentmapscale = newComposition.itemById(mapname).scale()
                        newComposition.itemById(mapname).setAtlasScalingMode(
                            self.atlasconfData["atlasdrivemap"][mapname]["typescale"]
                        )

        # ********************* close printing  *****************************
        atlas.endRender()
        if self.parentprintPDFworker is None:
            self.painter.end()

        # if self.enablemessages: self.messageinstance.closeProgressBar()
        # return

        # for rastlayer in layertoremove:
        #     qgis.core.QgsProject.instance().removeMapLayer(rastlayer)

        if debug:
            logging.getLogger("Lamia_unittest").debug("end")

    def setCoverageLayer(self):
        """
        créé le qgsvectorlayer utilisé pour l'atlas
        attention ce fichier doit avoir pour clé primaire l'id de la couche lamia et non le pk...
        :return: qgsvectorlayer qui servira à l'atlas
        """
        debug = False

        sql = self.atlasconfData["atlaslayersql"]
        # sql = self.dbase.updateQueryTableNow(sql)

        if self.parentprintPDFworker is not None:
            sqlsplitted = self.dbase.utils.splitSQLSelectFromWhereOrderby(sql)
            sqlwhere = ""
            if "WHERE" in sqlsplitted.keys():
                sqlwhere += sqlsplitted["WHERE"] + " AND "
            sqlwhere += self.parentprintPDFworker.atlasconfData["childprint"][
                "linkcolumn"
            ]

            linkcolumnname = self.parentprintPDFworker.atlasconfData["childprint"][
                "linkcolumn"
            ].split(".")[-1]
            if linkcolumnname.split("_")[0] in ["lpk", "lid"]:
                linkcolumnname = "_".join(linkcolumnname[1:].split("_")[0:2])
            else:
                # if self.enablemessages: self.messageinstance.showErrorMessage('Erreur sur la champs de liaison childprint')
                self.errormessage.emit("Erreur sur la champs de liaison childprint")
                return False

            sqlwhere += " = " + str(
                self.parentprintPDFworker.currentatlasfeat[linkcolumnname]
            )
            sqlsplitted["WHERE"] = sqlwhere
            sql = self.dbase.utils.rebuildSplittedQuery(sqlsplitted)

            sql += (
                " " + self.parentprintPDFworker.atlasconfData["childprint"]["optionsql"]
            )

        sql = self.dbase.updateQueryTableNow(sql)

        if debug:
            logging.getLogger("Lamia_unittest").debug("atlaslayer sql : %s", sql)

        atlaslayer = self.qgiscanvas.createSingleQgsVectorLayer(
            dbaseparser=self.dbase,
            tablename="atlaslayer",
            isspatial=self.atlasconfData["spatial"],
            sql=sql,
            tableid=self.atlasconfData["atlaslayerid"],
        )

        # if debug: logging.getLogger("Lamia_unittest").debug('atlaslayer pk index : %s', str(atlaslayer.dataProvider().pkAttributeIndexes()))
        if debug:
            logging.getLogger("Lamia_unittest").debug(
                "atlaslayer ids : %s",
                str([fet.id() for fet in atlaslayer.getFeatures()]),
            )

        return atlaslayer

    def processImages(self, newComposition, atlas, atlasfeat):

        for imageitemname in self.atlasconfData["images"].keys():
            # get imageitem
            imageitem = newComposition.itemById(imageitemname)

            imageresult = None
            self.currentimageItem = imageitem
            # *******************************************************

            if os.path.isfile(self.atlasconfData["images"][imageitemname]):
                imageresult = self.atlasconfData["images"][imageitemname]

            elif "photo" in self.atlasconfData["images"][imageitemname]:
                table = self.atlasconfData["images"][imageitemname].split(".")[0]
                photoid = int(
                    self.atlasconfData["images"][imageitemname].split(".")[-1][5:]
                )
                imageresult = self.getNumberedPhoto(atlasfeat, table, photoid)
            elif (
                "croquis" in self.atlasconfData["images"][imageitemname]
                or "sketch" in self.atlasconfData["images"][imageitemname]
            ):
                table = self.atlasconfData["images"][imageitemname].split(".")[0]
                photoid = int(
                    self.atlasconfData["images"][imageitemname].split(".")[-1][7:]
                )
                imageresult = self.getNumberedCroquis(atlasfeat, table, photoid)

            elif (
                "ressource" in self.atlasconfData["images"][imageitemname]
                or "resource" in self.atlasconfData["images"][imageitemname]
            ):
                table = self.atlasconfData["images"][imageitemname].split(".")[0]
                ressourcenum = self.atlasconfData["images"][imageitemname].split(".")[
                    -1
                ][9:]
                imageresult = self.getNumberedResource(atlasfeat, table, ressourcenum)

            elif self.atlasconfData["images"][imageitemname][0:4] == "logo":
                imagepath = os.path.join(
                    os.path.dirname(__file__),
                    "..",
                    "..",
                    "DBASE",
                    "utils",
                    self.atlasconfData["images"][imageitemname] + ".png",
                )
                imageresult = os.path.join(imagepath)

            else:
                typeprocess = self.atlasconfData["images"][imageitemname]
                if hasattr(self.addonimagesmodule, typeprocess):
                    func = getattr(self.addonimagesmodule, typeprocess)
                    imageresult = func(self)

                # exec('imageresult = self.addonimagesmodule.' +typeprocess + '(self)', locals(), globals() )
                # imageresult = globals()['imageresult']

            if imageitem is not None:
                if isinstance(imageitem, qgis.core.QgsLayoutItemPicture):
                    imageitem.setPicturePath(imageresult)
                    imageitem.refreshPicture()
                if isinstance(imageitem, qgis.core.QgsLayoutFrame):
                    imageitem.multiFrame().setContentMode(1)
                    imageitem.multiFrame().setHtml(imageresult)
                    imageitem.multiFrame().loadHtml()

    def processLamiaVars(self, newComposition, dictfields, atlasfeat):
        """
        Remplace les champs %lamia et %lamiasql definis dans le composeur par leur valeur dépendante du qgsfeature en
        cours de l'atlas

        ex : %lamia.lamiatable.lamiacolonne  fait une requete de type :
        WITH tempquery AS (sql cript for coveragelayer creation) SELECT lamiacolonne FROM lamiatable
        WHERE atlaslayerid (défini dans conf) = (l'id en cours de l'atlas)

        ex : %lamiasql.lamiascriptsql :
        WITH tempquery AS (sql cript for coveragelayer creation) + lamiascriptsql
        AND atlaslayerid (défini dans conf) = (l'id en cours de l'atlas)


        :param newComposition:
        :param dictfields:
        :return:
        """

        debug = False
        atlasfeatid = atlasfeat.id()
        atlasfeatpk = atlasfeat[self.atlasconfData["atlaslayerid"]]

        for compitemuuid in dictfields.keys():
            if False:  # qgis 2 version
                composeritem = newComposition.getComposerItemByUuid(compitemuuid)
            else:
                composeritem = newComposition.itemByUuid(compitemuuid)
                # composeritem.__class__ = qgis.core.QgsLayoutItemLabel

            finaltxt = []
            for temptxt in dictfields[compitemuuid]:
                if "lamia." in temptxt:
                    table = temptxt.split(".")[1]
                    field = ".".join(temptxt.split(".")[2:])
                    # creating sql request

                    if False:
                        sql = " WITH tempquery AS ("
                        if False:
                            sql += self.atlasconfData["atlaslayersql"]
                            sql += " AND "
                            sql += self.dbase.dateVersionConstraintSQL()
                        sql += self.dbase.updateQueryTableNow(
                            self.atlasconfData["atlaslayersql"]
                        )
                        if self.parentprintPDFworker is not None:
                            sql += (
                                " AND "
                                + self.parentprintPDFworker.atlasconfData["childprint"][
                                    "linkcolumn"
                                ]
                            )
                            # sql += ' = ' + str(self.parentprintPDFworker.currentid)
                            # sql += ' = ' + str(self.parentprintPDFworker.currentid)
                            linktablename = self.parentprintPDFworker.atlasconfData[
                                "childprint"
                            ]["linkcolumn"].split("_")[-1]
                            sql += " = " + str(
                                self.parentprintPDFworker.currentatlasfeat[
                                    "id_" + linktablename
                                ]
                            )
                            sql += (
                                " "
                                + self.parentprintPDFworker.atlasconfData["childprint"][
                                    "optionsql"
                                ]
                            )
                        sql += ") "
                        # sql += "SELECT " + field + " FROM " + table
                        sql += "SELECT " + field + " FROM tempquery "
                        sql += (
                            " WHERE "
                            + self.atlasconfData["atlaslayerid"]
                            + " = "
                            + str(atlasfeat.id())
                        )

                    if True:
                        tempsplittedquery = self.dbase.utils.splitSQLSelectFromWhereOrderby(
                            self.atlasconfData["atlaslayersql"]
                        )
                        tempsplittedquery["SELECT"] = table + "." + field
                        if "WHERE" in tempsplittedquery.keys():
                            tempsplittedquery["WHERE"] += (
                                " AND "
                                + self.atlasconfData["atlaslayerid"]
                                + " = "
                                + str(atlasfeatpk)
                            )
                        else:
                            tempsplittedquery["WHERE"] = (
                                self.atlasconfData["atlaslayerid"]
                                + " = "
                                + str(atlasfeatpk)
                            )
                        # tempsplittedquery['FROM'] = table
                        sql = self.dbase.utils.rebuildSplittedQuery(tempsplittedquery)
                        sql = self.dbase.updateQueryTableNow(sql)

                    if debug:
                        self.logger.debug("sql %s", str(sql))

                    query = self.dbase.query(sql)
                    valtemp = [row[0] for row in query][0]
                    rawtable = table.split("_")[0]  # split in cas _qgis table

                    if (
                        not rawtable in self.dbase.dbasetables.keys()
                    ):  # case as in sql query
                        atlassql = self.atlasconfData["atlaslayersql"]
                        atlassqlsplitted = atlassql.split("as")
                        for i, elem in enumerate(atlassqlsplitted):
                            if i == 0:
                                continue
                            if elem.strip().split(" ")[0] == rawtable:
                                possibletable = (
                                    atlassqlsplitted[i - 1]
                                    .strip()
                                    .split(" ")[-1]
                                    .split("_")[0]
                                )
                                if possibletable in self.dbase.dbasetables.keys():
                                    rawtable = possibletable
                                    break

                    val = self.dbase.getConstraintTextFromRawValue(
                        rawtable, field, valtemp
                    )

                    if unicode(val).lstrip("-").isdigit() and float(val) == -1.0:
                        finaltxt.append("/")
                    elif val == "":
                        finaltxt.append(" / ")
                    else:
                        finaltxt.append(unicode(val))

                elif "lamiasql." in temptxt:
                    tempsplittedquery = self.dbase.utils.splitSQLSelectFromWhereOrderby(
                        self.atlasconfData["atlaslayersql"]
                    )
                    # tempsplittedquery['SELECT'] = table + '.' + field
                    tempsplittedquery["SELECT"] = "(" + temptxt[9:] + ")"

                    if "WHERE" in tempsplittedquery.keys():
                        tempsplittedquery["WHERE"] += (
                            " AND "
                            + self.atlasconfData["atlaslayerid"]
                            + " = "
                            + str(atlasfeatpk)
                        )
                    else:
                        tempsplittedquery["WHERE"] = (
                            self.atlasconfData["atlaslayerid"]
                            + " = "
                            + str(atlasfeatpk)
                        )
                    # tempsplittedquery['FROM'] = table
                    sql = self.dbase.utils.rebuildSplittedQuery(tempsplittedquery)
                    sql = self.dbase.updateQueryTableNow(sql)

                    if debug:
                        self.logger.debug("lamiasql %s", str(sql))

                    query = self.dbase.query(sql)
                    result = [row for row in query]
                    if len(result) > 0:
                        txtresult = [
                            res if res is not None else "/" for res in result[0]
                        ]
                        finaltxt.append(" - ".join(txtresult))
                    else:
                        finaltxt.append("NR")

                else:
                    finaltxt.append(temptxt)
            if debug:
                self.logger.debug("result %s", str(finaltxt))
            txt = "".join(finaltxt)

            labelclasstxt = qgis.core.QgsLayoutItemLabel
            labelclasshtml = qgis.core.QgsLayoutFrame

            if isinstance(composeritem, labelclasstxt):
                composeritem.setText(txt)
            elif isinstance(composeritem, labelclasshtml) or isinstance(
                composeritem, qgis._core.QgsLayoutFrame
            ):
                composeritem.multiFrame().setHtml(txt)
                composeritem.multiFrame().loadHtml()

    def createComposition(self, mapsettings):
        """
        Create a composition with template found in \rapporttools\self.reporttype + '.qpt'
        :param mapsettings: qgis mapsettings
        :return: the composition created
        """

        debug = False
        if debug:
            self.logger.debug("started")

        newComposition = qgis.core.QgsPrintLayout(self.project)

        # newComposition = qgis.core.QgsMasterLayoutInterface(self.project)

        templatefile = self.reportconffilename + ".qpt"
        # templatepath = os.path.abspath(os.path.join(self.createfilesdir, templatefile))
        templatepath = os.path.abspath(os.path.join(self.templatedir, templatefile))

        template_file = QtCore.QFile(templatepath)
        template_file.open(QtCore.QIODevice.ReadOnly | QtCore.QIODevice.Text)
        template_content = template_file.readAll()
        template_file.close()

        if debug:
            self.logger.debug("template read")

        document = QtXml.QDomDocument()
        document.setContent(template_content)
        substitution_map = {}
        newComposition.loadFromTemplate(document, qgis.core.QgsReadWriteContext())

        return newComposition

    def createReport(self):
        """
        newComposition = qgis.core.QgsReport(self.project)


        # newComposition = qgis.core.QgsMasterLayoutInterface(self.project)

        templatefile = self.reportconffilename + '.qpt'
        #templatepath = os.path.abspath(os.path.join(self.createfilesdir, templatefile))
        templatepath = os.path.abspath(os.path.join(self.templatedir, templatefile))
        
        template_file = QtCore.QFile(templatepath)
        template_file.open(QtCore.QIODevice.ReadOnly | QtCore.QIODevice.Text)
        template_content = template_file.readAll()
        template_file.close()

        document = QtXml.QDomDocument()
        document.setContent(template_content)
        # substitution_map = {}
        # newComposition.loadFromTemplate(document, qgis.core.QgsReadWriteContext())
        newComposition.readLayoutXml(document.documentElement(), document, qgis.core.QgsReadWriteContext())
        """
        projectforreading = qgis.core.QgsProject.instance()
        projectforreading.read(
            os.path.join(self.templatedir, "test_report_project.qgz")
        )
        layoutmanager = projectforreading.layoutManager()
        newComposition = layoutmanager.layoutByName(self.reportconffilename)

        return newComposition

    def setAtlasLayer(self, newComposition, coveragelayer):
        """
        Parametre l'atlas de la newComposition
        :param newComposition: la composition en cours
        :param coveragelayer: le layer utilisé pour l'atals
        :return: l'atlasComposition de la newComposition
        """

        atlas = newComposition.atlas()
        # apply style
        # stylepath = os.path.join(os.path.dirname(__file__), 'rapporttools', self.atlasconfData['atlaslayerstyle'])
        stylepath = os.path.join(
            self.templatedir, self.atlasconfData["atlaslayerstyle"]
        )
        coveragelayer.loadNamedStyle(stylepath)
        # add coveragelayer to QgsProject
        qgis.core.QgsProject.instance().addMapLayer(coveragelayer, False)
        # set coveragelayer to atlas
        atlas.setCoverageLayer(coveragelayer)
        # set scale mode

        # enable atlas
        atlas.setEnabled(True)

        # set atlas spec
        for mapname in self.atlasconfData["atlasdrivemap"].keys():
            # print('mapname', mapname)
            temp1 = newComposition.itemById(mapname)
            # print(type(temp1))
            # temp1.__class__ = qgis.core.QgsLayoutItemMap
            newComposition.itemById(mapname).setAtlasDriven(True)
            # print(self.atlasconfData['atlasdrivemap'][mapname]['typescale'])
            # TODO
            newComposition.itemById(mapname).setAtlasScalingMode(
                self.atlasconfData["atlasdrivemap"][mapname]["typescale"]
            )
            newComposition.itemById(mapname).setFixedSize(
                newComposition.itemById(mapname).sizeWithUnits()
            )  # nedd in qgis3
            newComposition.itemById(mapname).setCrs(
                self.qgiscanvas.dbaseqgiscrs
            )  # for scale analysys in qgis3

        return atlas

    def setSectionLayer(self, newComposition, coveragelayer):

        self.project.addMapLayer(coveragelayer, False)
        stylepath = os.path.join(
            self.templatedir, self.atlasconfData["atlaslayerstyle"]
        )
        coveragelayer.loadNamedStyle(stylepath)

        # print(newComposition.childSections())
        for section in newComposition.childSections():
            # print(section.type())
            if section.type() == "SectionFieldGroup":
                section.setLayer(coveragelayer)
                section.setField(self.atlasconfData["atlaslayerid"])
                return section

    def fillComposerMapsWihLayers(self, newComposition, coveragelayer):
        """
        Charge les tables spécifiée dans le fichier txt de conf dans les mapitems
        :param newComposition: la composition en cours d'utilisation
        :param confData: le ficier de conf
        :return: les qgsmaplayers qu'il faudra décahrger ensuite
        """
        debug = False
        layertoremove = []
        for typemap in ["atlasdrivemap", "generalmap"]:
            # for mapname in reportdic['layers'].keys():
            for mapname in self.atlasconfData[typemap].keys():
                layersformapcomposer = []
                # print('mapname',mapname)
                for layername in self.atlasconfData[typemap][mapname]["layers"]:
                    if layername == "atlaslayer":
                        layersformapcomposer.append(coveragelayer)

                    elif layername == "scan25":

                        if self.dbase.base3version:
                            sql = "SELECT file from rasters_qgis"
                            sql += " WHERE rastertype = 'IRF'"
                        else:
                            sql = "SELECT file from Rasters_qgis"
                            sql += " WHERE typeraster = 'IRF'"
                        query = self.dbase.query(sql)
                        results = [row[0] for row in query]
                        if len(results) > 0:
                            for result in results:
                                # fileraster = self.dbase.dbasetables['Infralineaire']['widget'].completePathOfFile(result[0])
                                fileraster = self.dbase.completePathOfFile(result)
                                if os.path.isfile(fileraster):
                                    rlayer = qgis.core.QgsRasterLayer(
                                        fileraster,
                                        os.path.basename(fileraster).split(".")[0],
                                    )
                                    try:
                                        rlayer.renderer().setOpacity(0.5)
                                    except:
                                        pass
                                    qgis.core.QgsProject.instance().addMapLayer(
                                        rlayer, False
                                    )
                                    layersformapcomposer.append(rlayer)
                                    layertoremove.append(rlayer)
                                else:
                                    if debug:
                                        logging.getLogger("Lamia_unittest").debug(
                                            "no scan25 file"
                                        )

                    elif layername == "ortho":
                        if self.dbase.base3version:
                            sql = "SELECT file from rasters_qgis"
                            sql += " WHERE rastertype = 'ORF'"
                        else:
                            sql = "SELECT file from Rasters_qgis"
                            sql += " WHERE typeraster = 'ORF'"
                        query = self.dbase.query(sql)
                        results = [row[0] for row in query]
                        if len(results) > 0:
                            for result in results:
                                # fileraster = self.dbase.dbasetables['Infralineaire']['widget'].completePathOfFile(result[0])
                                fileraster = self.dbase.completePathOfFile(result)
                                if os.path.isfile(fileraster):
                                    rlayer = qgis.core.QgsRasterLayer(
                                        fileraster,
                                        os.path.basename(fileraster).split(".")[0],
                                    )
                                    if qgis.utils.iface is not None:
                                        rlayer.renderer().setOpacity(0.5)
                                    qgis.core.QgsProject.instance().addMapLayer(
                                        rlayer, False
                                    )
                                    layersformapcomposer.append(rlayer)
                                    layertoremove.append(rlayer)
                                else:
                                    if debug:
                                        logging.getLogger("Lamia_unittest").debug(
                                            "no ortho file"
                                        )

                    elif layername in self.dbase.dbasetables.keys():
                        # strtoeval = "self.dbase.dbasetables['" + layername + "']['layerqgis']"
                        strtoeval = (
                            "self.qgiscanvas.layers['" + layername + "']['layerqgis']"
                        )
                        layer = eval(strtoeval)
                        layersformapcomposer.append(layer)
                    else:

                        if self.dbase.base3version:
                            sql = "SELECT file from rasters_qgis"
                            sql += f" WHERE name = '{layername}'"
                        else:
                            sql = "SELECT file from Rasters_qgis"
                            sql += f" WHERE libelle = '{layername}'"
                        query = self.dbase.query(sql)
                        results = [row[0] for row in query]
                        filelayer = None
                        if len(results) > 0:
                            filelayer = self.dbase.completePathOfFile(result)
                            if os.path.isfile(filelayer):
                                rlayer = qgis.core.QgsVectorLayer(
                                    filelayer,
                                    os.path.basename(filelayer).split(".")[0],
                                    "ogr",
                                )
                                if qgis.utils.iface is not None:
                                    rlayer.renderer().setOpacity(0.5)
                                qgis.core.QgsProject.instance().addMapLayer(
                                    rlayer, False
                                )
                                layersformapcomposer.append(rlayer)
                                layertoremove.append(rlayer)

                        if not filelayer:
                            if debug:
                                logging.getLogger("Lamia_unittest").debug(
                                    "layer file %s not found", layername
                                )

                temp1 = newComposition.itemById(mapname)
                temp1.__class__ = qgis.core.QgsLayoutItemMap
                temp1.setLayers(layersformapcomposer)
                temp1.setKeepLayerSet(True)

        return layertoremove

    def getLamiaVarInComposition(self, newComposition):
        """
        Crée un dictionnaire des requetes sql présentes dans la composition
        qui sont sous la forme .. #lamia {requete sql} #lamia ..
        :param newComposition: la composition en cours d'utilisation
        :return: un dicionnaire : {...composeritem.uuid(): le texte du composerlabel splité avec #
        """

        dictfields = {}
        for composeritem in newComposition.items():
            if sys.version_info.major == 2:
                labelclasstxt = qgis.core.QgsComposerLabel
                labelclasshtml = qgis.core.QgsComposerFrame
            elif sys.version_info.major == 3:
                labelclasstxt = qgis.core.QgsLayoutItemLabel
                labelclasshtml = qgis.core.QgsLayoutFrame

            if isinstance(composeritem, labelclasstxt):
                # print(composeritem.text())
                if "#lamia" in composeritem.text():
                    txtsplit = composeritem.text().split("#")
                    dictfields[composeritem.uuid()] = txtsplit
            elif isinstance(composeritem, labelclasshtml):
                if (
                    composeritem.multiFrame() is not None
                    and "#lamia" in composeritem.multiFrame().html()
                ):
                    txtsplit = composeritem.multiFrame().html().split("#")
                    dictfields[composeritem.uuid()] = txtsplit

        return dictfields

    def getOrderedPksForAtlas(self, coveragelayer):
        """
        Renvoi un dictionnaire avec zoneeo_id camme clé et la list des ids du coveragelayer ordonnée comme valeur
        est ensuite lu et itéré lors de la generation de l'atlas
        :param coveragelayer:
        :return:idsforreportdict : OrderedDict with {... zongeo_id:[list of ids of coverage layer],...}
        """
        debug = False

        # orderedids = OrderedDict()
        orderedpks = {}
        if (
            self.parentprintPDFworker is None
            and self.atlasconfData["spatial"]
            and "ordering" in self.atlasconfData.keys()
            and self.atlasconfData["ordering"] != ""
        ):
            orderedpks = self.orderPksAlongPath(coveragelayer, self.pkzonegeolist)
        else:
            # orderedpks[0] = [feat[self.atlasconfData['atlaslayerid']] for feat in coveragelayer.getFeatures()]
            orderedpks[0] = [feat.id() for feat in coveragelayer.getFeatures()]

        if len(orderedpks) == 0:
            orderedpks[0] = [feat.id() for feat in coveragelayer.getFeatures()]

        if debug:
            self.logger.debug("orderedpks %s", str(orderedpks))

        if orderedpks is None or len(orderedpks) == 0:
            return

        return orderedpks

    def orderPksAlongPath(self, coveragelayer, zonegeopks=[]):

        debug = False

        orderedpks = {}

        # **********************   ordering view ****************************
        # ************ by zonegeo and infralineaire ************************

        # get simple list of infralin id within zonegeo
        if len(zonegeopks) == 0:
            sql = "SELECT pk_zonegeo FROM Zonegeo "
            query = self.dbase.query(sql)
            zonegeopks = [row[0] for row in query]

        dictedgesordered = {}
        for zonegeopk in zonegeopks:
            dictedgesordered[zonegeopk] = []
            sql = "SELECT ST_AsText(geom) FROM Zonegeo WHERE pk_zonegeo = " + str(
                zonegeopk
            )
            query = self.dbase.query(sql)
            zonegeogeom = [row[0] for row in query][0]
            sql = (
                "SELECT Infralineaire_now.pk_infralineaire FROM Infralineaire_now"
                " WHERE ST_WITHIN(ST_MakeValid(Infralineaire_now.geom),ST_GeomFromText('{}',{}))".format(
                    zonegeogeom, self.dbase.crsnumber
                )
            )
            sql = self.dbase.sqlNow(sql)
            query = self.dbase.query(sql)
            result = [row[0] for row in query]
            dictedgesordered[zonegeopk] = result

        if debug:
            self.logger.debug("dictedgesordered %s", str(dictedgesordered))

        # get pathtool and init it
        self.networkcore.computeNXGraph()

        # begin ordering process
        if len(dictedgesordered) > 0:
            for zonegeopk in dictedgesordered.keys():
                orderedpks[zonegeopk] = []
                self.networkcore.computeNXGraph(dictedgesordered[zonegeopk])
                # get subgraphs within nxgraph
                subgraphs = self.networkcore.getSubGraphs()
                for subgraph in subgraphs:
                    extremities = self.networkcore.getExtremityNodeIndexFromLinearGraph(
                        subgraph
                    )
                    if extremities is None:
                        # if self.enablemessages: self.messageinstance.showErrorMessage('attention presence d un noeud - non traite')
                        self.errormessage.emit(
                            "attention presence d un noeud - non traite"
                        )

                    if debug:
                        self.logger.debug(
                            "zonegeo %s extremities  %s ", zonegeopk, str(extremities)
                        )

                    shortestpathedges = self.networkcore.getShortestPath(
                        extremities[0], extremities[1]
                    )
                    pathpksreverse = self.networkcore.getInfralineairePkFromNxEdges(
                        shortestpathedges
                    )
                    if debug:
                        self.logger.debug(
                            "zonegeo %s subgraph path pks : %s",
                            zonegeopk,
                            str(pathpksreverse),
                        )
                    # reverse list of not from amaont to aval
                    if (
                        not shortestpathedges[0:2]
                        in self.networkcore.edgesnodeindex.tolist()
                    ):
                        shortestpathedgesreversed = shortestpathedges[::-1]
                        pathpksreverse = self.networkcore.getInfralineairePkFromNxEdges(
                            shortestpathedges
                        )

                    if self.atlasconfData["ordering"].split(";")[0] == "autopath":
                        orderedpks[zonegeopk] += list(pathpksreverse[:, 0])

                    elif (
                        self.atlasconfData["ordering"].split(";")[0] == "autoalongpath"
                    ):
                        datas = self.networkcore.getOrderedProjectedPks(
                            pathpksreverse=pathpksreverse,
                            layertoproject=coveragelayer,
                            constraint=self.atlasconfData["ordering"].split(";")[1],
                        )

                        # print('datas', datas)
                        res = [int(pk) for pk in datas["pk"]]
                        orderedpks[zonegeopk] += res

        return orderedpks

    def initPrinterAndPainter(self, newComposition):
        """
        initialise le self.priner et le self.painter pour accuilir l'impression
        retourne un QgsLayoutExporter pour qgis3 sinon None
        :param newComposition: la composition de travail
        :param atlas: l'alas de la composition de travail
        :return: QgsLayoutExporter pour qgis3 sinon None
        """
        debug = False
        exporter = None
        if self.printtype == "atlas":
            exporter = qgis.core.QgsLayoutExporter(newComposition)
        settings = qgis.core.QgsLayoutExporter.PdfExportSettings()
        printsettings = qgis.core.QgsLayoutExporter.PrintExportSettings()

        if self.parentprintPDFworker is None:

            self.printer.setOutputFormat(QPrinter.PdfFormat)
            self.printer.setOutputFileName(self.pdffile)
            paperWidth = newComposition.pageCollection().page(0).pageSize().width()
            paperHeight = newComposition.pageCollection().page(0).pageSize().height()
            if debug:
                self.logger.debug("print size %s %s", str(paperWidth), str(paperHeight))
            self.printer.setPaperSize(
                QtCore.QSizeF(paperWidth, paperHeight), QPrinter.Millimeter
            )
            self.printer.setFullPage(True)

            printReady = self.painter.begin(self.printer)
            if debug:
                self.logger.debug("print ready %s", printReady)

        return exporter

    def setGeneralMapExtentByZonegeo(self, newComposition, zonegeopk):
        """
        Adapte le zoom de la carte générale en fonction de la zonegeo en cours
        :param newComposition: la composition en cours d'utilisation
        :param zonegeoid: l'id de la zone geo en cours de traitement
        """
        for mapname in self.atlasconfData["generalmap"].keys():
            zonegeofet = self.qgiscanvas.layers["Zonegeo"]["layer"].getFeature(
                zonegeopk
            )

            layerext = zonegeofet.geometry().boundingBox()
            layerext = layerext.buffered(layerext.height() / 10.0)
            layerextgeom = qgis.core.QgsGeometry.fromRect(layerext)
            if self.qgiscanvas.xform is not None:
                layerextgeomcanvas = layerextgeom.transform(self.qgiscanvas.xform)
            else:
                layerextgeomcanvas = layerextgeom
            layerextgeomcanvasfinal = layerextgeom.boundingBox()
            temp1 = newComposition.itemById(mapname)
            # temp1.__class__ = qgis.core.QgsLayoutItemMap
            temp1.zoomToExtent(layerextgeomcanvasfinal)

            # set min scale
            minscale = 0
            for atlasmapitem in self.atlasconfData["atlasdrivemap"].keys():
                if (
                    self.atlasconfData["atlasdrivemap"][atlasmapitem]["minscale"]
                    > minscale
                ):
                    minscale = self.atlasconfData["atlasdrivemap"][atlasmapitem][
                        "minscale"
                    ]

            if newComposition.itemById(mapname).scale() < minscale * 5.0:
                newComposition.itemById(mapname).setScale(minscale * 5.0)

    def printAtlasPage(
        self, newComposition, exporter, indexpagetotal, indexpage, idecalage
    ):
        """
        Realise l'impression de la composition sur pdf
        Dans le cas de childprint, appele le printPDFBaseWorker chargé de faire l'impression des childs
        :param newComposition: la compostion en cours
        :param exporter: utile pour qgis3
        :param indexpage: index de la page en cours d'edition
        :param idecalage: iterateur utilisé dans le childprint pour décaler l'impression
        :return:
        """

        printsettings = qgis.core.QgsLayoutExporter.PrintExportSettings()

        if self.parentprintPDFworker is None:
            if indexpagetotal > 0:
                self.printer.newPage()

            for numpage in range(newComposition.pageCollection().pageCount()):
                if numpage > 0:
                    self.printer.newPage()
                exporter.renderPage(self.painter, numpage)
                exporter.print(self.printer, printsettings)
            self.updateStartHeight(self.pageheightpx)

        else:
            # evaluate new page
            futureverticalpositionpx = self.currentstartheightpx + self.pageheightpx
            if futureverticalpositionpx > self.painter.device().height():
                self.printer.newPage()
                futureverticalpositionpx = 10 + self.pageheightpx
                self.currentstartheightpx = 10

            self.painter.translate(0, self.currentstartheightpx)
            exporter.renderPage(self.painter, 0)
            beforeheight, beforewidth = (
                self.printer.paperRect(QPrinter.Millimeter).height(),
                self.printer.paperRect(QPrinter.Millimeter).width(),
            )
            exporter.print(self.printer, printsettings)
            self.printer.setPaperSize(
                QtCore.QSizeF(beforewidth, beforeheight), QPrinter.Millimeter
            )
            self.printer.setFullPage(True)
            self.painter.translate(0, -self.currentstartheightpx)

            self.updateStartHeight(futureverticalpositionpx)

        self.childPrint()

    def childPrint(self):
        # childprint
        if len(self.atlasconfData["childprint"].keys()) > 0:
            childrapport = self.__class__(
                reportcore=self.reportcore,
                # windowdialog=self.windowdialog,
                parentprintPDFworker=self,
                reportconffilename=None,
                # confData=self.confData,
                pdffile=None,
                # reporttype=reporttype,
                # templatedir=createfilesdir ,
                # idlist=None,
                pklist=None,
                pkzonegeolist=[],
            )
            childrapport.work()

    def getPhoto(self, reportdic, feat):
        # print('getPhoto')
        resfile = None
        if (
            "lk_photo"
            in self.dbase.dbasetables[reportdic["dbasename"]]["fields"].keys()
        ):
            sql = "SELECT lk_photo FROM " + reportdic["dbasename"]
            sql += " WHERE id_" + reportdic["dbasename"] + " = " + str(feat.id())
            query = self.dbase.query(sql)
            result = [row for row in query]
            if len(result) > 0 and not self.dbase.isAttributeNull(result[0][0]):
                sql = "SELECT Ressource.file FROM Photo INNER JOIN Ressource ON Photo.id_ressource = Ressource.id_ressource WHERE Photo.id_objet = "
                sql += str(result[0][0])
                query = self.dbase.query(sql)
                result = [row for row in query]
                filephoto = result[0][0]
                # print(filephoto)
                resfile = self.dbase.completePathOfFile(filephoto)
        if resfile is None:
            resfile = self.getNumberedPhoto(reportdic, feat, 1)

        return resfile

    def getNumberedPhoto(self, atlasfeat, table, photoid, typeressource="PHO"):

        debug = False

        resfile = None
        # get id_objet
        tempsplittedquery = self.dbase.utils.splitSQLSelectFromWhereOrderby(
            self.atlasconfData["atlaslayersql"]
        )

        if self.dbase.base3version:
            tempsplittedquery["SELECT"] = table + ".id_object "
        else:
            tempsplittedquery["SELECT"] = table + ".id_objet "

        if "WHERE" in tempsplittedquery.keys():
            tempsplittedquery["WHERE"] += (
                " AND "
                + self.atlasconfData["atlaslayerid"]
                + " = "
                + str(atlasfeat[self.atlasconfData["atlaslayerid"]])
            )
        else:
            tempsplittedquery["WHERE"] = (
                self.atlasconfData["atlaslayerid"]
                + " = "
                + str(atlasfeat[self.atlasconfData["atlaslayerid"]])
            )

        sql = self.dbase.utils.rebuildSplittedQuery(tempsplittedquery)
        sql = self.dbase.updateQueryTableNow(sql)
        query = self.dbase.query(sql)
        if len(query) == 0:
            return None
        idobjet = [row[0] for row in query][0]

        if self.dbase.base3version:
            sql = f"SELECT file FROM media_now INNER JOIN tcobjectresource ON lid_resource = id_resource \
                     WHERE tcobjectresource.lid_object = {idobjet}  AND typemedia = '{typeressource}' "
        else:
            sql = "SELECT file FROM Photo_now INNER JOIN Tcobjetressource ON lid_ressource = id_ressource"
            sql += (
                " WHERE Tcobjetressource.lid_objet = "
                + str(idobjet)
                + " AND typephoto = '"
                + typeressource
                + "'"
            )
        sql = self.dbase.updateQueryTableNow(sql)
        query = self.dbase.query(sql)
        if query is None:
            return None
        result = [row for row in query]

        if len(result) > (photoid - 1):
            resfile = self.dbase.completePathOfFile(result[photoid - 1][0])
        if debug:
            self.logger.debug("resfile  %s", str(resfile))
        return resfile

    def getNumberedCroquis(self, atlasfeat, table, photoid):
        return self.getNumberedPhoto(atlasfeat, table, photoid, typeressource="CRO")

    def getNumberedResource(self, atlasfeat, table, photoid):

        debug = False

        resfile = None

        tempsplittedquery = self.dbase.utils.splitSQLSelectFromWhereOrderby(
            self.atlasconfData["atlaslayersql"]
        )

        if self.dbase.base3version:
            tempsplittedquery["SELECT"] = table + ".lid_resource_" + str(photoid)
        else:
            tempsplittedquery["SELECT"] = table + ".lid_ressource_" + str(photoid)

        if "WHERE" in tempsplittedquery.keys():
            tempsplittedquery["WHERE"] += (
                " AND "
                + self.atlasconfData["atlaslayerid"]
                + " = "
                + str(atlasfeat[self.atlasconfData["atlaslayerid"]])
            )
        else:
            tempsplittedquery["WHERE"] = (
                self.atlasconfData["atlaslayerid"]
                + " = "
                + str(atlasfeat[self.atlasconfData["atlaslayerid"]])
            )

        sql = self.dbase.utils.rebuildSplittedQuery(tempsplittedquery)
        sql = self.dbase.updateQueryTableNow(sql)

        query = self.dbase.query(sql)
        if len(query) == 0:
            return None
        idressource = [row[0] for row in query][0]

        if not self.dbase.utils.isAttributeNull(idressource):
            if self.dbase.base3version:
                sql = "SELECT file FROM resource_now WHERE id_resource = " + str(
                    idressource
                )
            else:
                sql = "SELECT file FROM Ressource_now WHERE id_ressource = " + str(
                    idressource
                )
            sql = self.dbase.updateQueryTableNow(sql)
            query = self.dbase.query(sql)
            result = [row for row in query]

            # print(result)
            if len(result) > 0:
                resfile = self.dbase.completePathOfFile(result[0][0])

            if debug:
                self.logger.debug("resfile  %s", str(resfile))
        return resfile

    def createconfData(self, tabletypename):
        """
        Lit le fichier de conf situé dans self.createfilesdir, soit dans ./rapporttools
        :return: un dictionnaire confData :
                {'atalslayersql' : la requete qui selectionne les éléments à énumérer dans l'atlas,
                 'atlaslayerid' : l'id à considérer par rapport aux colonnes de la requete,
                 'atlaslayerstyle' : le style du qgsvectorlyaer utilisé pour l'atlas
                 atlasdrivemap : {...,
                                  le nom du mapitem qui se déplace avec l'atlas : {'minscale' : l'echelle minimum ,
                                                                                typescale : le type d'echelle,
                                                                                layers: list des maplayers à mettre dans le  mapitem},
                                 ...},
                 generalmap : {...,
                                  le nom du mapitem de la carte générale :     {'minscale' : l'echelle minimum ,
                                                                                typescale : le type d'echelle,
                                                                                layers: list des maplayers à mettre dans le  mapitem},
                                 ...},
                 childprint :  {confname : le nom du fichier txt dans rapporttools à utiliser
                                linkcolumn: le colonne de liaison avec l'id du coverage layer,
                                optionsql: requete sql à rajouter à la fin de la requete de selection des enfants}
                 }
        """

        debug = False

        if debug:
            logging.getLogger("Lamia_unittest").debug(
                "tabletypename : %s", tabletypename
            )

        # self.confData = {}
        # self.toolwidgetmain .comboBox_type.clear()
        confData = {}

        # * search good file
        # reportcore
        tabletypepath = None
        for workdir in [
            self.reportcore.confdataplugin,
            self.reportcore.confdataproject,
        ]:
            for filename in glob.glob(os.path.join(workdir, "*.txt")):
                basename = os.path.basename(filename).split(".")[0]
                if basename == tabletypename:
                    goodworkdir = workdir
                    tabletypepath = filename
                    break
        if tabletypepath is None:
            return None, None

        basename = os.path.basename(tabletypepath).split(".")[0]
        if debug:
            logging.getLogger("Lamia_unittest").debug("basename %s", basename)

        filetoread = open(tabletypepath, "r", encoding="utf-8")
        compt = 0
        for line in filetoread:
            if line[0:3] == "###":  # new field
                actualdictkey = line[3:].strip()
                if actualdictkey in [
                    "atlaslayersql",
                    "atlaslayerid",
                    "atlaslayerstyle",
                    "ordering",
                ]:
                    confData[actualdictkey] = ""
                else:
                    confData[actualdictkey] = {}
            elif line[0:1] == "#":
                continue
            elif line.strip() == "":
                continue
            else:
                if actualdictkey == "atlaslayersql":
                    confData[actualdictkey] += line.strip() + " "
                elif actualdictkey in ["atlaslayerid", "atlaslayerstyle", "ordering"]:
                    confData[actualdictkey] = line.strip()
                elif actualdictkey in ["atlasdrivemap", "generalmap"]:
                    speclist = line.split(";")
                    confData[actualdictkey][speclist[0].strip()] = {}
                    if speclist[1].strip() != "":
                        minscale = int(speclist[1].strip())
                    else:
                        minscale = None

                    typescale = speclist[2].strip()
                    if typescale != "":
                        typescale = eval("qgis.core.QgsLayoutItemMap." + typescale)

                    confData[actualdictkey][speclist[0].strip()]["minscale"] = minscale
                    confData[actualdictkey][speclist[0].strip()][
                        "typescale"
                    ] = typescale
                    confData[actualdictkey][speclist[0].strip()]["layers"] = eval(
                        speclist[3].strip()
                    )
                elif actualdictkey in ["spatial"]:
                    confData[actualdictkey] = eval(line.strip())
                elif actualdictkey in ["childprint"]:
                    speclist = line.split(";")
                    confData[actualdictkey]["confname"] = speclist[0].strip()
                    confData[actualdictkey]["linkcolumn"] = speclist[1].strip()
                    confData[actualdictkey]["optionsql"] = speclist[2].strip()
                elif actualdictkey in ["images"]:
                    speclist = line.split(";")
                    confData[actualdictkey][speclist[0].strip()] = speclist[1].strip()

        filetoread.close()

        if debug:
            logging.getLogger("Lamia_unittest").debug("confData : %s", confData)
        return confData, goodworkdir

    def initHeightpx(self, newComposition):

        # * initialize var for page dimension in case of child print
        self.pageheightpx = self.getCompositionHeightpx(newComposition)

        if self.parentprintPDFworker is not None:
            self.currentstartheightpx = self.parentprintPDFworker.currentstartheightpx
        else:
            self.currentstartheightpx = 0

    def updateStartHeight(self, heightvaluepx):
        self.currentstartheightpx = heightvaluepx  # margin
        if self.parentprintPDFworker:
            self.parentprintPDFworker.updateStartHeight(heightvaluepx)

    def getCompositionHeightpx(self, newComposition):
        if newComposition.itemById("parentheight"):
            itemheightmm = (
                newComposition.itemById("parentheight").rectWithFrame().height()
            )
        else:
            itemheightmm = newComposition.pageItemBounds(
                newComposition.pageCollection().pageCount() - 1
            ).height()

        compositionheightmm = (
            newComposition.pageCollection()
            .page(newComposition.pageCollection().pageCount() - 1)
            .pageSize()
            .height()
        )
        pageheightmm = self.printer.paperRect(QPrinter.Millimeter).height()

        if itemheightmm > 0.9 * compositionheightmm:
            pageheightpx = int(
                compositionheightmm / pageheightmm * self.painter.device().height()
            )
        else:
            pageheightpx = int(
                itemheightmm / pageheightmm * self.painter.device().height()
            )

        return pageheightpx
