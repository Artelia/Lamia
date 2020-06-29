import unittest, os, logging, sys, platform

sys.path.append(os.path.join(os.path.join(os.path.dirname(__file__)), ".."))
"""
import warnings
with warnings.catch_warnings():
    warnings.filterwarnings("ignore",category=DeprecationWarning)

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")
"""
import networkx
import Lamia.libs.pyqtgraph


from pprint import pprint
import qgis, qgis.core, qgis.gui
from qgis.PyQt import uic, QtCore
from qgis.PyQt.QtCore import QSettings, QTranslator, qVersion, QCoreApplication, Qt
from qgis.PyQt.QtWidgets import QWidget, QDialog, QMainWindow

import warnings, os

# warnings.simplefilter("ignore")
# os.environ["PYTHONWARNINGS"] = "ignore" # Also affect subprocesses
warnings.filterwarnings("default", category=DeprecationWarning, module="networkx")

from Lamia.iface.qgiswidget.ifaceqgswidget import LamiaWindowWidget
from Lamia.dbasemanager.dbaseparserfactory import DBaseParserFactory
from Lamia.iface.qgscanvas.ifaceqgiscanvas import QgisCanvas
from settings import *


class DBaseTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_a_generateqgisserverconf(self):
        pgdbase = DBaseParserFactory("postgis").getDbaseParser()
        if False:
            dbaseressourcesdirectory = os.path.join(
                os.path.dirname(__file__), "testtempfiles", "importBM_pg"
            )
            if not os.path.isdir(dbaseressourcesdirectory):
                os.mkdir(dbaseressourcesdirectory)
            pgdbase.createDBase(
                crs="2154",
                worktype="Base2_digue",
                dbaseressourcesdirectory=dbaseressourcesdirectory,
                variante="Lamia",
                host="localhost",
                port="5432",
                dbname="lamiaunittest",
                schema="importBM",
                user="pvr",
                password="pvr",
            )
            pgdbase.loadDBase(
                host="localhost",
                port="5432",
                dbname="lamiaunittest",
                schema="importBM",
                user="pvr",
                password="pvr",
            )

            bmtoimport = os.path.join(
                os.path.dirname(__file__),
                "..",
                "test",
                "datas",
                "lamia_digue",
                "test01.sqlite",
            )

            pgdbase.dbaseofflinemanager.addDBase(**{"slfile": bmtoimport})
        else:
            pgdbase.loadDBase(
                host="localhost",
                port="5432",
                dbname="lamiaunittest",
                schema="importBM",
                user="pvr",
                password="pvr",
            )

        canvas = qgis.gui.QgsMapCanvas()
        canvas.enableAntiAliasing(True)
        canvascrs = qgis.core.QgsCoordinateReferenceSystem()
        canvascrs.createFromString("EPSG:2154")
        canvas.setDestinationCrs(canvascrs)

        qgscanvas = QgisCanvas(canvas)

        qgscanvas.createLayersForQgisServer(
            pgdbase, specifichost="docker.for.win.localhost"
        )

    def _createMainWin(self):
        self.mainwin = UserUI()
        self.mainwin.frame.layout().addWidget(self.canvas)
        self.mainwin.frame_2.layout().addWidget(self.wind)
        self.mainwin.setParent(None)
        self.mainwin.resize(QtCore.QSize(1000, 800))

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


class UserUI(QDialog):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), "qtdialog", "mainwindows.ui")
        uic.loadUi(uipath, self)


def main():
    app = initQGis()
    logging.basicConfig(
        format="%(asctime)s :: %(levelname)s :: %(module)s :: %(funcName)s :: %(message)s",
        datefmt="%H:%M:%S",
    )
    logging.getLogger("Lamia_unittest").setLevel(logging.DEBUG)

    unittest.main()
    exitQGis()


if __name__ == "__main__":
    main()

