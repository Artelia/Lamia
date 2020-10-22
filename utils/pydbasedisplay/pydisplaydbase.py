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

INTERFACEINDEX = 0
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

    testdir = os.path.join(
        os.path.dirname(Lamia.utils.__file__), "../test/testtempfiles/c_creation"
    )
    #  sl_base3_urbandrainage_Lamia   sl_base3_waterdistribution_Lamia
    # sl_base3_constructionsite_Lamia   sl_base3_constructionsite_Orange
    # sl_base3_levee_Lamia   sl_base3_levee_SIRS   sl_base3_faunaflora_Lamia
    worktype = "sl_base3_urbandrainage_Lamia"

    SLFILE = os.path.join(testdir, worktype, "test01.sqlite")

    # SLFILE = r"C:\111_GitProjects\Lamia\test\datas\lamia_digue\test01.sqlite"
    # SLFILE = r"C:\111_GitProjects\Lamia\test\datas\lamia_digue_base3\test01.sqlite"
    # SLFILE = r"C:\01_WORKINGDIR\GPMB\c_merge_ass\mergeddbase.sqlite"
    # SLFILE = r"C:\111_GitProjects\Lamia\utils\pynetworktool\networktest_geographic\test01.sqlite"
    # SLFILE = (
    #     r"C:\111_GitProjects\Lamia\test\datas\lamia_assainissement_base3\test01.sqlite"
    # )
    # SLFILE = r"M:\FR\BOR\VT\FLUVIAL\4352024_33_Conformite_digues_BM\6_Reglementaire\61_Calculs\Basedonnees\BD_totale_ind12_tempPVR.sqlite"
    # SLFILE = r"C:\111_GitProjects\Lamia\test\datas\lamia_digue_base3\test01.sqlite"
    SLFILE = r"C:\01_WORKINGDIR\cier\AEP Cieux.sqlite"
    # SLFILE = r"M:\FR\BOR\VT\FLUVIAL\4352789_33_BM_surveillance_digues_PI_Ambes\05_ETUDES\052_Calculs\Basedonnees\VTA_Ambes_ind2_PVR.sqlite"
    # SLFILE = r"C:\111_GitProjects\Lamia\test\testtempfiles\c_creation\sl_base3_constructionsite_Orange\test01.sqlite"
    # SLFILE = r"C:\01_WORKINGDIR\GPMB\c_merge_ass\mergeddbase.sqlite"
    # SLFILE = r"C:\01_WORKINGDIR\cons\cons.sqlite"
    # SLFILE = r"C:\01_WORKINGDIR\orange\toto.sqlite"
    # SLFILE = r"C:\111_GitProjects\Lamia\testtempfiles\c_creation\sl_base3_urbandrainage_Lamia\test01.sqlite"
    # SLFILE = r"C:\111_GitProjects\Lamia\testtempfiles\digue\VTA_Ambes_ind2.sqlite"
    # SLFILE = r"C:\111_GitProjects\Lamia\testtempfiles\c_creation\sl_base3_levee_Lamia\test01.sqlite"
    # SLFILE = r"M:\FR\BOR\VT\FLUVIAL\4352789_33_BM_surveillance_digues_PI_Ambes\05_ETUDES\052_Calculs\temps2\VTA_Ambes_ind2.sqlite"
    # SLFILE = r"C:\01_WORKINGDIR\cons\SPATIALITE_2747.sqlite"
    # SLFILE = r"C:\01_WORKINGDIR\sncf\new\LANDY-09-2020.sqlite"
    # SLFILE = r"U:\FR\BOR\VT\PVR\sncf\LANDY-09-2020.sqlite"
    # SLFILE = r"M:\FR\BOR\VT\FLUVIAL\4352907_33_CDC_SaintLoubes_VTA\05_ETUDES\05_1_TERRAIN\BD_PVR\dor\VTA_StLoubes_ind1_FJE_Dordogne.sqlite"
    SLFILE = r"C:\01_WORKINGDIR\VTA_2020_Noailles.sqlite"
    SLFILE = (
        r"U:\FR\BOR\VT\PVR\sebastien\Noailles\20200917_sbn\VTA_2020_Noailles.sqlite"
    )

    # print(TGREEN, f"Opening {os.path.abspath(SLFILE)}", ENDC)

    print(f"{bcolors.OKGREEN}Opening: {os.path.abspath(SLFILE)} {bcolors.ENDC}")

    return

    lamiawidget.loadDBase(dbtype="Spatialite", slfile=SLFILE)
    # lamiawidget.loadDBase(
    #     dbtype="Postgis",
    #     host="localhost",
    #     # host="localhost",
    #     port=5432,
    #     dbname="lamiaunittest",
    #     schema="base3_urbandrainage_lamia",
    #     user="pvr",
    #     password="pvr",
    # )

    lamiawidget.setVisualMode(visualmode=INTERFACEINDEX)
    lamiawidget.dbase.raiseexceptions = True  # False True
    lamiawidget.dbase.printsql = False  # False True

    if PROFILING:
        pr.enable()
    #   toolpostpro     toolprepro
    # wdg = lamiawidget.toolwidgets["networktool"]
    # wdg.tooltreewidget.currentItemChanged.emit(wdg.qtreewidgetitem, None)
    # wdg.analyseSubdomains()

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
    logging.getLogger("Lamia_unittest").setLevel(logging.DEBUG)
    logging.getLogger("Lamia.iface.qgscanvas.ifaceqgiscanvas").setLevel(logging.DEBUG)
    # logging.getLogger("Lamia").setLevel(logging.DEBUG)

    app = initQGis()

    launchIface()

    exitQGis()


if __name__ == "__main__":
    main()
