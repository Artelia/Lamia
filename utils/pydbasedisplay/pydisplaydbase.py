import os, sys
import cProfile, logging

lamiapath = os.path.join(os.path.join(os.path.dirname(__file__)), "..", "..")
sys.path.append(lamiapath)
from test.test_utils import *
import Lamia

from Lamia.dbasemanager.dbaseparserfactory import DBaseParserFactory
from Lamia.iface.ifaceabstractconnector import LamiaIFaceAbstractConnectors
import warnings

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

import Lamia.libs.pyqtgraph

warnings.filterwarnings(
    "ignore", category=DeprecationWarning, module="Lamia.libs.pyqtgraph"
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

from Lamia.iface.qgsconnector.ifaceloggingconnector import LoggingConnector

INTERFACEINDEX = 0
PROFILING = False


TGREEN = "\033[32m"
TRED = "\033[31m"
ENDC = "\033[m"


def launchIface():
    if PROFILING:
        pr = cProfile.Profile()

    translator = loadLocale()
    mainwin, canvas, lamiawidget = getDisplayWidget()

    lamiawidget.connector = LoggingConnector()
    # lamiawidget.dbase.messageinstance = lamiawidget.connector

    testdir = os.path.join(
        os.path.dirname(Lamia.__file__), "../test/testtempfiles/c_creation"
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
    # SLFILE = r"C:\01_WORKINGDIR\cier\AEP Cieux.sqlite"
    # SLFILE = r"M:\FR\BOR\VT\FLUVIAL\4352789_33_BM_surveillance_digues_PI_Ambes\05_ETUDES\052_Calculs\Basedonnees\VTA_Ambes_ind2_PVR.sqlite"
    # SLFILE = r"C:\111_GitProjects\Lamia\test\testtempfiles\c_creation\sl_base3_constructionsite_Orange\test01.sqlite"
    SLFILE = r"C:\01_WORKINGDIR\GPMB\c_merge_ass\mergeddbase.sqlite"
    # SLFILE = r"C:\01_WORKINGDIR\cons\cons.sqlite"
    # SLFILE = r"C:\01_WORKINGDIR\orange\toto.sqlite"
    SLFILE = r"C:\111_GitProjects\Lamia\testtempfiles\c_creation\sl_base3_urbandrainage_Lamia\test01.sqlite"

    print(TGREEN, f"Opening {os.path.abspath(SLFILE)}", ENDC)

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
