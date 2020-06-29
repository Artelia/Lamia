import os, sys
import cProfile

lamiapath = os.path.join(os.path.join(os.path.dirname(__file__)), "..", "..")
sys.path.append(lamiapath)
from test.test_utils import *
import Lamia
from Lamia.dbasemanager.dbaseparserfactory import DBaseParserFactory


def main():
    app = initQGis()

    mainwin, canvas, lamiawidget = getDisplayWidget()
    translator = loadLocale()

    testdir = os.path.join(
        os.path.dirname(Lamia.__file__), "../test/testtempfiles/c_creation"
    )
    #  sl_base3_urbandrainage_Lamia   sl_base3_waterdistribution_Lamia
    # sl_base3_constructionsite_Lamia   sl_base3_constructionsite_Orange
    # sl_base3_levee_Lamia      sl_base3_faunaflora_Lamia
    worktype = "sl_base3_levee_Lamia"

    SLFILE = os.path.join(testdir, worktype, "test01.sqlite")
    print(os.path.abspath(SLFILE))

    lamiawidget.loadDBase(dbtype="Spatialite", slfile=SLFILE)

    exitQGis()


if __name__ == "__main__":
    main()
