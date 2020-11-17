import unittest, os, logging, sys, platform
import shutil

lamiapath = os.path.join(os.path.join(os.path.dirname(__file__)), "..", "..")
sys.path.append(lamiapath)
from test.test_utils import *
import Lamia
from Lamia.secrets import postgis_aws

import qgis, qgis.core, qgis.gui


from Lamia.api.dbasemanager.dbaseparserfactory import DBaseParserFactory


SLFILEFROM = r"C:\01_WORKINGDIR\reims\BER\BDD LAMIA BER\BDD_REIMS_BER_20200915.sqlite"
SLFILETO = r"C:\01_WORKINGDIR\reims\testast\BDD_REIMS_J1_AST.sqlite"


def addDbase():
    newname = os.path.join(
        os.path.dirname(SLFILETO),
        os.path.basename(SLFILETO).split(".")[0] + "_copy.sqlite",
    )
    shutil.copy(SLFILETO, newname)

    # sldbasefrom = DBaseParserFactory("spatialite").getDbaseParser()
    sldbaseto = DBaseParserFactory("spatialite").getDbaseParser()

    sldbaseto.loadDBase(slfile=newname)

    sldbaseto.dbaseofflinemanager.addDBase(**{"slfile": SLFILEFROM})


def main():
    app = initQGis()
    # logging.basicConfig(
    #     format="%(asctime)s :: %(levelname)s :: %(module)s :: %(funcName)s :: %(message)s",
    #     datefmt="%H:%M:%S",
    # )
    # logging.getLogger("Lamia_unittest").setLevel(logging.DEBUG)

    # import in postgis
    addDbase()

    # create project for qgisserver
    # createProject()

    exitQGis()


if __name__ == "__main__":
    main()

