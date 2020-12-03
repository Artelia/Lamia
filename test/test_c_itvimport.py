import unittest, os, logging, sys, shutil, logging, time, glob

sys.path.append(os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..")))
import warnings

with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=DeprecationWarning)


import qgis, qgis.core
from qgis.PyQt.QtWidgets import QApplication

from Lamia.api.dbasemanager.dbaseparserfactory import DBaseParserFactory
from Lamia.api.libslamia.lamiaITVimport.lamiaITVimport import ITVImportCore
from Lamia.qgisiface.iface.qgsconnector.ifaceqgisconnector import QgisConnector
from test_utils import *
from settings import *


class DBaseTest(unittest.TestCase):

    """Test case utilisé pour tester les fonctions du module 'random'."""

    def setUp(self):
        """Initialisation des tests."""
        # TESTDIR = os.path.join(os.path.join(os.path.dirname(__file__)), 'temp')
        self.connector = QgisConnector()
        self.testcdir = os.path.join(TESTDIR, "c_creation")
        # self.itvtdir = os.path.join(TESTDIR, "itvimport")
        # if not os.path.isdir(self.itvtdir):
        #     os.mkdir(self.itvtdir)

    def test_a_generateITV(self):
        sqlitedbase = DBaseParserFactory("spatialite").getDbaseParser()
        # slfile = os.path.join(
        #     self.testcdir, "sl_base3_urbandrainage_Lamia", "test01.sqlite"
        # )
        slfile = r"C:\01_WORKINGDIR\aaaa\test.sqlite"
        sqlitedbase.loadDBase(slfile=slfile)

        itvcore = ITVImportCore(sqlitedbase, messageinstance=self.connector)

        datafiles = os.path.join(
            os.path.dirname(__file__), "datas", "itvimport", "VU-5024-0418.txt"
        )

        logging.getLogger("Lamia_itvcore").debug("STARTING")

        # resdataframe = itvcore.readITVs(datafiles)

        # logging.getLogger("Lamia_itvcore").debug(
        #     "res %s", str(resdataframe.values.tolist())
        # )

        # noidinlamia = itvcore.checkNodesExistInLamia(datafiles)
        # logging.getLogger("Lamia_itvcore").debug(
        #     "res %s", str(noidinlamia)
        # )

        # itvcore.getUniquesValuesbyEdge(datafiles)

        itvcore.computeNotation("rereau_base", [1])


def main():
    app = initQGis()
    logging.basicConfig(
        format="%(asctime)s :: %(levelname)s :: %(module)s :: %(funcName)s :: %(message)s",
        datefmt="%H:%M:%S",
    )
    logging.getLogger("Lamia_itvcore").setLevel(logging.DEBUG)
    unittest.main()
    exitQGis()


if __name__ == "__main__":
    main()

