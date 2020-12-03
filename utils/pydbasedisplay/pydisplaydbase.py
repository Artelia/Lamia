import os, sys
import cProfile, logging

lamiapath = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
print(lamiapath)
sys.path.append(lamiapath)
from Lamia.test.test_utils import *
import Lamia.api

from Lamia.api.dbasemanager.dbaseparserfactory import DBaseParserFactory
from Lamia.qgisiface.iface.ifaceabstractconnector import LamiaIFaceAbstractConnectors
import warnings
import colorama
from colorama import Fore, Back, Style

colorama.init()

# warnings.filterwarnings("ignore")
# os.environ["PYTHONWARNINGS"] = "ignore"

# with warnings.catch_warnings(record=True) as w:
# Cause all warnings to always be triggered.
# warnings.simplefilter("always")
# Trigger a warning.
# fxn()
# print(w)
# Verify some things
# assert len(w) == 1
# assert issubclass(w[-1].category, DeprecationWarning)
# assert "deprecated" in str(w[-1].message)


# default ignore
import networkx

warnings.filterwarnings("ignore", category=DeprecationWarning, module="networkx")

import Lamia.api.libs.pyqtgraph

warnings.filterwarnings(
    "ignore", category=DeprecationWarning, module="Lamia.api.libs.pyqtgraph"
)

import numpy

warnings.filterwarnings("ignore", message="numpy.ufunc size changed")

# warnings.filterwarnings("ignore", category=RuntimeWarning, module="numpy")
# warnings.filterwarnings("ignore")

# with warnings.catch_warnings():
#     warnings.filterwarnings("ignore")
# warnings.filterwarnings("default", category=DeprecationWarning, module="numpy")
# warnings.filterwarnings("default", category=RuntimeWarning, module="numpy")

numpy.seterr(all="ignore")

from Lamia.qgisiface.iface.qgsconnector.ifaceloggingconnector import LoggingConnector

INTERFACEINDEX = 4
PROFILING = False


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def launchIface():
    if PROFILING:
        pr = cProfile.Profile()

    translator = loadLocale()
    mainwin, canvas, lamiawidget = getDisplayWidget()

    lamiawidget.connector = LoggingConnector()
    # lamiawidget.dbase.messageinstance = lamiawidget.connector

    #  sl_base3_urbandrainage_Lamia   sl_base3_waterdistribution_Lamia
    # sl_base3_constructionsite_Lamia   sl_base3_constructionsite_Orange
    # sl_base3_levee_Lamia   sl_base3_levee_SIRS   sl_base3_faunaflora_Lamia
    worktype = "sl_base3_waterdistribution_Lamia"
    # SLFILE = os.path.join(TESTDIR, "c_creation", worktype, "test01.sqlite")
    # SLFILE = r"C:\01_WORKINGDIR\bm\BD_totale_ind15.sqlite"
    SLFILE = r"C:\01_WORKINGDIR\reims\testast\BDD_REIMS_J1_AST.sqlite"
    SLFILE = r"C:\01_WORKINGDIR\reims\testast\mergeddbase.sqlite"
    # SLFILE = r"C:\01_WORKINGDIR\alban\lamia\test_alban.sqlite"
    # SLFILE = r"C:\01_WORKINGDIR\sebastien\VTA_2020_Noailles.sqlite"
    SLFILE = r"C:\01_WORKINGDIR\bm\BD_totale_ind15.sqlite"
    # SLFILE = r"C:\Users\Public\Documents\lamia\BD_totale_ind15\BD_totale_ind15.sqlite"
    # SLFILE = r"C:\01_WORKINGDIR\sebastien\VTA_2020_Noailles.sqlite"
    # SLFILE = r"C:\01_WORKINGDIR\herve\fusion\mergeddbase.sqlite"
    # SLFILE = r"C:\01_WORKINGDIR\aaa\testconstruction.sqlite"
    # SLFILE = r"C:\01_WORKINGDIR\BACALAN\GPMB Bacalan.sqlite"
    # SLFILE = r"C:\Users\Public\Documents\lamia\GPMB Bacalan\GPMB Bacalan.sqlite"

    # SLFILE = r"C:\111_GitProjects\Lamia\testfiles\offlinemodedbase\parentdb\parenttestoffline.sqlite"
    # SLFILE = r"C:\111_GitProjects\Lamia\testfiles\offlinemodedbase\childdb\childtestoffline.sqlite"
    # SLFILE = r"C:\111_GitProjects\Lamia\testfiles\offlinemodedbase\parentdb\parenttestoffline_initialbackup.sqlite"
    # SLFILE = r"C:\111_GitProjects\Lamia\testfiles\offlinemodedbase\parentdb\parenttestoffline_backup.sqlite"

    SLFILE = r"C:\01_WORKINGDIR\aaaa\test.sqlite"

    SLFILE = r"C:\01_WORKINGDIR\aaa\VTA_2020_Baie-Aiguillon.sqlite"

    print(f"{bcolors.OKGREEN}Opening: {os.path.abspath(SLFILE)} {bcolors.ENDC}")

    lamiawidget.loadDBase(dbtype="Spatialite", slfile=SLFILE)
    # lamiawidget.loadDBase(
    #     dbtype="Postgis",
    #     host="localhost",
    #     # host="localhost",
    #     port=5432,
    #     dbname="lamiaunittest",
    #     # schema="base3_urbandrainage_lamia",
    #     schema="importgpmb",
    #     user="pvr",
    #     password="pvr",
    # )
    # binval = b"\x89PNG\r\n\x1a\n\x00\x00"
    # binval2 = str(binval)
    # sql = f"INSERT INTO resource(thumbnail) VALUES({binval})"
    # print(sql)
    # lamiawidget.dbase.query(sql)

    lamiawidget.setVisualMode(visualmode=INTERFACEINDEX)
    lamiawidget.dbase.raiseexceptions = False  # False True
    lamiawidget.dbase.printsql = False  # False True
    lamiawidget.dbase.printorm = True  # False True

    if PROFILING:
        pr.enable()
    #   toolpostpro     toolprepro
    # wdg = lamiawidget.toolwidgets["lamiamca"]
    # wdg.tooltreewidget.currentItemChanged.emit(wdg.qtreewidgetitem, None)
    # wdg.editAMC()
    # wdg.analyseSubdomains()
    # wdg.mcacore.mcavirtualayerFactory.setConfName("_test")
    # wdg.mcacore.createMcaDB("_test")
    # res = wdg.mcacore.computeNodeScore("_test", nodeid="1")
    # print("*", res)
    # lay = wdg.mcacore.joinResultToQgslayer("_test", res)
    # data, lay = wdg.mcacore.createMcaDB("_test")
    # print(data)

    # lamiawidget.pullDBase()
    # lamiawidget.pushDBase()

    # wdg = lamiawidget.toolwidgets["lamiaITVimport"]
    # wdg.tooltreewidget.currentItemChanged.emit(wdg.qtreewidgetitem, None)
    # wdg.computeRereau()
    # # wdg.viewAsLayer()
    # itvfiles = [
    #     lamiawidget.dbase.completePathOfFile(fl.strip())
    #     for fl in wdg.toolwidgetmain.file.text().split(";")
    # ]
    # wdg.itvcore.getUniquesValuesbyEdge(itvfiles)

    mainwin.exec_()

    if PROFILING:
        pr.disable()
        cprofilepath = os.path.join(os.path.dirname(__file__), "pydisplay.cprof")
        pr.dump_stats(cprofilepath)
        # REm : run     python -m snakeviz pydisplay.cprof       for viz


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
