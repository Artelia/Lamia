import os, sys
import cProfile, logging

lamiapath = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.append(lamiapath)
from Lamia.test.test_utils import *
import Lamia.api
from Lamia.api.dbasemanager.dbaseparserfactory import DBaseParserFactory
from Lamia.qgisiface.iface.qgsconnector.ifaceloggingconnector import LoggingConnector


def launchIface():

    translator = loadLocale()
    mainwin, canvas, lamiawidget = getDisplayWidget()

    lamiawidget.connector = LoggingConnector()

    SLFILE = r"C:\01_WORKINGDIR\aaaa\variante_lamia.sqlite"
    # SHPFILE = r"C:\01_WORKINGDIR\alban\data\ART_RegardsEU.shp"
    SHPFILE = r"C:\01_WORKINGDIR\aaaa\Troncons_SBY_L93_3.shp"
    IMPORTTYPE = "edge"

    lamiawidget.loadDBase(dbtype="Spatialite", slfile=SLFILE)

    lamiawidget.setVisualMode(visualmode=4)
    lamiawidget.dbase.raiseexceptions = False  # False True
    lamiawidget.dbase.printsql = False  # False True
    lamiawidget.dbase.printorm = True  # False True

    wdg = lamiawidget.toolwidgets["lamiaimport"]
    wdg.tooltreewidget.currentItemChanged.emit(wdg.qtreewidgetitem, None)

    qgslayer = qgis.core.QgsVectorLayer(SHPFILE, "result", "ogr")

    wdg.showFlowChart(qgslayer, IMPORTTYPE)


def main():

    logging.basicConfig(
        format="%(asctime)s :: %(levelname)s :: %(module)s :: %(funcName)s :: %(message)s",
        datefmt="%H:%M:%S",
    )
    logging.getLogger("Lamia").setLevel(logging.DEBUG)
    logging.getLogger("Lamia.iface.qgscanvas.ifaceqgiscanvas").setLevel(logging.DEBUG)
    # logging.getLogger("Lamia").setLevel(logging.DEBUG)

    app = initQGis()

    launchIface()

    exitQGis()


if __name__ == "__main__":
    main()
