import os, sys, logging

import qgis, qgis.core

lamiapath = os.path.join(os.path.join(os.path.dirname(__file__)), "..", "..")
sys.path.append(lamiapath)

from test.test_utils import *
import Lamia

from Lamia.api.dbasemanager.dbaseparserfactory import DBaseParserFactory

from Lamia.api.libslamia.lamiaexportshp.lamiaexportshp import ExportShapefileCore


import cProfile

PROFILING = True


def main(argv):
    if PROFILING:
        pr = cProfile.Profile()

    # SLFILE = r"C:\111_GitProjects\Lamia\test\datas\lamia_digue\test01.sqlite"
    SLFILE = r"C:\111_GitProjects\Lamia\test\testtempfiles\c_creation\sl_base3_constructionsite_Lamia\test01.sqlite"
    SLFILE = r"C:\01_WORKINGDIR\cier\AEP Cieux.sqlite"
    SLFILE = (
        r"C:\111_GitProjects\Lamia\test\datas\lamia_assainissement_base3\test01.sqlite"
    )
    SLFILE = r"C:\01_WORKINGDIR\perigord\CC_Bastides_Dordogne_Perigord_finale.sqlite"
    SLFILE = r"C:\01_WORKINGDIR\canejean2\Canejan.sqlite"

    tempparser = DBaseParserFactory("spatialite").getDbaseParser()
    tempparser.loadDBase(dbtype="Spatialite", slfile=SLFILE)

    app = initQGis()

    print("start ExportShapefileCore")

    from Lamia.qgisiface.iface.qgsconnector.ifaceloggingconnector import (
        LoggingConnector,
    )

    connector = LoggingConnector()
    lamiashpexport = ExportShapefileCore(tempparser, messageinstance=connector)
    lamiashpexport.SHOWSQL = False
    logging.getLogger("Lamia_unittest").setLevel(logging.DEBUG)
    logging.getLogger("Lamia").setLevel(logging.DEBUG)

    if PROFILING:
        pr.enable()

    lamiashpexport.runExport(
        destinationshapefile=r"C:\01_WORKINGDIR\toto\infraline.shp",
        exportconffilepath="lamia_edge_z_sketch_photo",  # lamia_edge_z_sketch  lamia_node_observation_fr
        pkzonegeos=[],
    )

    if PROFILING:
        pr.disable()
        cprofilepath = os.path.join(os.path.dirname(__file__), "pydxfexport.cprof")
        pr.dump_stats(cprofilepath)

    # REm : run     python -m snakeviz pydxfexport.cprof       for viz

    exitQGis()


if __name__ == "__main__":
    main(sys.argv[1:])

