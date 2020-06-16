import os, sys
import cProfile, logging

lamiapath = os.path.join(os.path.join(os.path.dirname(__file__)), "..", "..")
sys.path.append(lamiapath)
from test.test_utils import *
import Lamia

from Lamia.dbasemanager.dbaseparserfactory import DBaseParserFactory
import networkx
import warnings

warnings.filterwarnings("default", category=DeprecationWarning, module="networkx")
INTERFACEINDEX = 0


def launchIface():
    translator = loadLocale()
    mainwin, canvas, lamiawidget = getDisplayWidget()

    testdir = os.path.join(
        os.path.dirname(Lamia.__file__), "../test/testtempfiles/c_creation"
    )
    #  sl_base3_urbandrainage_Lamia   sl_base3_waterdistribution_Lamia
    # sl_base3_constructionsite_Lamia   sl_base3_constructionsite_Orange
    # sl_base3_levee_Lamia      sl_base3_faunaflora_Lamia
    worktype = "sl_base3_faunaflora_Lamia"

    SLFILE = os.path.join(testdir, worktype, "test01.sqlite")

    # SLFILE = r"C:\111_GitProjects\Lamia\test\datas\lamia_digue\test01.sqlite"
    # SLFILE = r"C:\111_GitProjects\Lamia\test\datas\lamia_digue_base3\test01.sqlite"
    # SLFILE = r"C:\01_WORKINGDIR\GPMB\c_merge_ass\mergeddbase.sqlite"

    lamiawidget.loadDBase(dbtype="Spatialite", slfile=SLFILE)

    lamiawidget.setVisualMode(visualmode=INTERFACEINDEX)
    lamiawidget.dbase.raiseexceptions = True  # False True
    lamiawidget.dbase.printsql = False  # False True

    #   toolpostpro     toolprepro
    # wdg = self.wind.toolwidgets["toolpostpro"]["reporttools"]
    # wdg.tooltreewidget.currentItemChanged.emit(wdg.qtreewidgetitem, None)

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
