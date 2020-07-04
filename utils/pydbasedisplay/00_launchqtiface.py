from qgis.PyQt.QtWidgets import QDialog, QMainWindow, QWidget
from qgis.PyQt.QtCore import QCoreApplication, QSettings, Qt, QTranslator, qVersion
from qgis.PyQt import QtCore, uic
from Lamia.iface.qgiswidget.ifaceqgswidget import LamiaWindowWidget
from Lamia.dbasemanager.dbaseparserfactory import DBaseParserFactory
import qgis.gui
import qgis.core
import qgis
import Lamia.libs.pyqtgraph
import networkx
from pprint import pprint
import warnings
import unittest
import platform
import logging
import os
import sys

lamiapath = os.path.join(os.path.join(os.path.dirname(__file__)), "..", "..")
# print(os.path.abspath(lamiapath))
sys.path.append(lamiapath)


# warnings.simplefilter("ignore")
# os.environ["PYTHONWARNINGS"] = "ignore" # Also affect subprocesses
warnings.filterwarnings(
    "default", category=DeprecationWarning, module="networkx")


# from settings import *

X_BEGIN = 400000.0
Y_BEGIN = 6000000.0
LOCALE = "fr"  # fr en
INTERFACEINDEX = 0
# p


class DBaseViewer:
    def __init__(self):
        self.testdir = os.path.join(
            os.path.dirname(
                __file__), "..", "..", "test", "testtempfiles", "c_creation"
        )

    def run(self):

        if True:

            #  sl_base3_urbandrainage_Lamia   sl_base3_waterdistribution_Lamia
            # sl_base3_constructionsite_Lamia   sl_base3_constructionsite_Orange
            # sl_base3_levee_Lamia      sl_base3_faunaflora_Lamia
            worktype = "sl_base3_constructionsite_Lamia"
            SLFILE = os.path.join(self.testdir, worktype, "test01.sqlite")

            # SLFILE = r"C:\01_WORKINGDIR\GPMB\c_merge_ass\mergeddbase.sqlite"

            self._loadLocale()
            self._createWin()
            self._createMainWin()
            self.wind.loadDBase(dbtype="Spatialite", slfile=SLFILE)

        if False:
            self._createWin()
            self._createMainWin()
            PGhost = "localhost"
            PGport = 5432
            PGbase = "lamiaunittest"
            PGschema = "base3_urbandrainage_lamia"
            PGuser = "pvr"
            PGpassword = "pvr"
            self.wind.loadDBase(
                dbtype="Postgis",
                host=PGhost,
                port=PGport,
                dbname=PGbase,
                schema=PGschema,
                user=PGuser,
                password=PGpassword,
            )

        self.showIFace()
        # self.testReport()

    def showIFace(self):
        if ("edge" in self.wind.qgiscanvas.layers.keys()
                and self.wind.qgiscanvas.layers["edge"]["layer"].featureCount() > 0):
            extent = (self.wind.qgiscanvas.layers["edge"]["layer"].extent().buffered(
                10.0))
        else:
            extent = qgis.core.QgsRectangle(
                X_BEGIN, Y_BEGIN, X_BEGIN + 10, Y_BEGIN + 10)
        # logging.getLogger("Lamia_unittest").debug('Extent : %s', extent)
        self.wind.qgiscanvas.canvas.setExtent(extent)

        self.wind.setVisualMode(visualmode=INTERFACEINDEX)
        # self.wind.dbase.printsql = True

        # display good widget
        if False:
            if False:
                self.wind.setVisualMode(visualmode=4)
                # print(self.wind.toolwidgets['toolpostpro'].keys())
                wdg = self.wind.toolwidgets["toolpostpro"]["reporttools"]
            if True:
                # deficiency
                wdg = self.wind.toolwidgets["toolprepro"]["graphdb"]
            wdg.tooltreewidget.currentItemChanged.emit(
                wdg.qtreewidgetitem, None)

        self.mainwin.exec_()

    def testReport(self):
        from Lamia.libslamia.lamiareport.lamiareport import ReportCore

        exporterreport = ReportCore(
            self.wind.dbase, messageinstance=self.wind.connector
        )

        destfile = os.path.join(os.path.dirname(
            __file__), "testoutput", "testreport.pdf")
        confname = "testreport"
        exporterreport.runReport(
            destinationfile=destfile, reportconffilename=confname, pkzonegeos=[])

    def _createMainWin(self):

        self.mainwin = UserUI()
        self.mainwin.frame.layout().addWidget(self.canvas)
        self.mainwin.frame_2.layout().addWidget(self.wind)
        self.mainwin.setParent(None)
        self.mainwin.resize(QtCore.QSize(1600, 800))

    def _createWin(self):
        self.canvas = qgis.gui.QgsMapCanvas()
        self.canvas.enableAntiAliasing(True)
        canvascrs = qgis.core.QgsCoordinateReferenceSystem()
        canvascrs.createFromString("EPSG:2154")
        self.canvas.setDestinationCrs(canvascrs)

        self.wind = LamiaWindowWidget()
        self.wind.qgiscanvas.setCanvas(self.canvas)

        stylesheet = """
                    QMainWindow{
                                background-color: rgba(0, 55, 90,80);
                                }
                    """
        stylesheet = ""
        self.wind.setStyleSheet(stylesheet)
        self.wind.setParent(None)
        self.dbase = self.wind.dbase
        self.mainwin = None

    def _loadLocale(self):
        # initialize locale
        # locale = QSettings().value('locale/userLocale')[0:2]
        locale = LOCALE
        QtCore.QSettings().setValue("locale/userLocale", LOCALE)

        plugin_dir = os.path.join(
            os.path.dirname(__file__), "..", "..", "Lamia")
        locale_path = os.path.join(
            plugin_dir, "i18n", "Lamia_{}.qm".format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > "4.3.3":
                QCoreApplication.installTranslator(self.translator)
                # self.app.installTranslator(self.translator)


class UserUI(QDialog):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), "mainwindows.ui")
        uic.loadUi(uipath, self)


def initQGis():
    if platform.system() == "Windows":
        qgis_path = "C://OSGeo4W64//apps//qgis-ltr"
    elif platform.system() == "Linux":
        qgis_path = "/usr"

    app = qgis.core.QgsApplication([], True)
    qgis.core.QgsApplication.setPrefixPath(qgis_path, True)
    qgis.core.QgsApplication.initQgis()
    return app


def exitQGis():
    qgis.core.QgsApplication.exitQgis()


def main():
    # os.environ["QT_LOGGING_RULES"] = 'qt.svg.debug=false;qt.svg.warning=false'
    app = initQGis()
    logging.basicConfig(
        format="%(asctime)s :: %(levelname)s :: %(module)s :: %(funcName)s :: %(message)s",
        datefmt="%H:%M:%S",
    )
    logging.getLogger("Lamia_unittest").setLevel(logging.DEBUG)

    # os.environ["QT_LOGGING_RULES"] = 'qt.svg.debug=false;qt.svg.warning=false'
    # print(type(os.environ["QT_LOGGING_RULES"]))
    # sys.exit()

    # unittest.main()
    dbaseviewer = DBaseViewer()
    dbaseviewer.run()

    exitQGis()


if __name__ == "__main__":
    main()
