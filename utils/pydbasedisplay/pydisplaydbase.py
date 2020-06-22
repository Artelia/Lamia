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

INTERFACEINDEX = 4


def launchIface():
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
    worktype = "sl_base3_faunaflora_Lamia"

    SLFILE = os.path.join(testdir, worktype, "test01.sqlite")

    # SLFILE = r"C:\111_GitProjects\Lamia\test\datas\lamia_digue\test01.sqlite"
    SLFILE = r"C:\111_GitProjects\Lamia\test\datas\lamia_digue_base3\test01.sqlite"
    # SLFILE = r"C:\01_WORKINGDIR\GPMB\c_merge_ass\mergeddbase.sqlite"
    # SLFILE = r"C:\111_GitProjects\Lamia\utils\pynetworktool\networktest_geographic\test01.sqlite"

    lamiawidget.loadDBase(dbtype="Spatialite", slfile=SLFILE)

    lamiawidget.setVisualMode(visualmode=INTERFACEINDEX)
    lamiawidget.dbase.raiseexceptions = True  # False True
    lamiawidget.dbase.printsql = False  # False True

    #   toolpostpro     toolprepro
    # wdg = lamiawidget.toolwidgets["networktool"]
    # wdg.tooltreewidget.currentItemChanged.emit(wdg.qtreewidgetitem, None)
    # wdg.analyseSubdomains()

    mainwin.exec_()


def main():

    logging.basicConfig(
        format="%(asctime)s :: %(levelname)s :: %(module)s :: %(funcName)s :: %(message)s",
        datefmt="%H:%M:%S",
    )
    logging.getLogger("Lamia_unittest").setLevel(logging.DEBUG)

    app = initQGis()

    launchIface()

    exitQGis()


if __name__ == "__main__":
    main()
