import unittest, os, logging, sys, platform

lamiapath = os.path.join(os.path.join(os.path.dirname(__file__)), "..", "..")
sys.path.append(lamiapath)
from test.test_utils import *
import Lamia
from Lamia.secrets import postgis_aws

import qgis, qgis.core, qgis.gui


from Lamia.api.dbasemanager.dbaseparserfactory import DBaseParserFactory
from Lamia.qgisiface.iface.qgscanvas.ifaceqgiscanvas import QgisCanvas


def importInPostGis():
    # * conf
    pgdbase = DBaseParserFactory("postgis").getDbaseParser()
    sldbase = DBaseParserFactory("spatialite").getDbaseParser()
    # destdb
    # host = "localhost"
    # port = 5432
    # dbname = "lamiaunittest"
    # schema = "importgpmbb"
    # user = "pvr"
    # pwd = "pvr"
    # postgisresourcedir = os.path.join(os.path.dirname(__file__), dbname + "_" + schema)

    host = postgis_aws.host
    port = postgis_aws.port
    dbname = postgis_aws.dbname
    schema = "importgpmb"
    user = postgis_aws.user
    pwd = postgis_aws.password
    postgisresourcedir = os.path.join(os.path.dirname(__file__), dbname + "_" + schema)

    # sqlite from db
    slfile = r"C:\01_WORKINGDIR\GPMB\final_ass\mergeddbase.sqlite"

    # * script

    # load sldbase
    sldbase.loadDBase(slfile=slfile)
    crs = sldbase.crsnumber
    worktype = sldbase.worktype
    variante = sldbase.variante
    # create pgdbase
    dbaseressourcesdirectory = os.path.join(os.path.dirname(__file__), "importBM_pg")
    pgdbase.createDBase(
        crs=str(crs),
        worktype=worktype,
        dbaseressourcesdirectory=postgisresourcedir,
        variante=variante,
        host=host,
        port=str(port),
        dbname=dbname,
        schema=schema,
        user=user,
        password=pwd,
    )
    pgdbase.loadDBase(
        host=host,
        port=str(port),
        dbname=dbname,
        schema=schema,
        user=user,
        password=pwd,
    )

    pgdbase.dbaseofflinemanager.addDBase(**{"slfile": slfile})


def createProject():
    pgdbase = DBaseParserFactory("postgis").getDbaseParser()
    pgdbase.loadDBase(
        host="localhost",
        port="5432",
        dbname="lamiaunittest",
        schema="importgpmb",
        user="pvr",
        password="pvr",
    )
    canvas = qgis.gui.QgsMapCanvas()
    canvas.enableAntiAliasing(True)
    canvascrs = qgis.core.QgsCoordinateReferenceSystem()
    canvascrs.createFromString("EPSG:3945")
    canvas.setDestinationCrs(canvascrs)
    qgscanvas = QgisCanvas(canvas)
    qgscanvas.createLayersForQgisServer(pgdbase)


def main():
    app = initQGis()
    logging.basicConfig(
        format="%(asctime)s :: %(levelname)s :: %(module)s :: %(funcName)s :: %(message)s",
        datefmt="%H:%M:%S",
    )
    logging.getLogger("Lamia_unittest").setLevel(logging.DEBUG)

    # import in postgis
    importInPostGis()

    # create project for qgisserver
    # createProject()

    exitQGis()


if __name__ == "__main__":
    main()

