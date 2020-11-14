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

    SLFILE = r"C:\01_WORKINGDIR\OO\VTA_L93_Lamia_SIRS_BDY_06-11-20.sqlite"

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
        # deficiency_lastobservation_point  deficiency_lastobservation_line
        exportconffilepath="deficiency_lastobservation_line",  # lamia_edge_z_sketch  lamia_node_observation_fr
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

