import os, sys, logging

import qgis, qgis.core

lamiapath = os.path.join(os.path.join(os.path.dirname(__file__)), "..", "..")
sys.path.append(lamiapath)

from test.test_utils import *
import Lamia

from Lamia.dbasemanager.dbaseparserfactory import DBaseParserFactory

# from Lamia.iface.qgsconnector.ifaceqgisconnector import QgisConnector
from Lamia.libslamia.lamianetworkx.lamianetworkx import NetWorkCore
from Lamia.libslamia.lamiareport.lamiareport import ReportCore
from Lamia.iface.qgscanvas.ifaceqgiscanvas import QgisCanvas
import numpy as np
import cProfile

PROFILING = False


def main(argv):
    if PROFILING:
        pr = cProfile.Profile()

    SLFILE = r"C:\111_GitProjects\Lamia\test\datas\lamia_digue\test01.sqlite"
    SLFILE = r"M:\FR\BOR\VT\FLUVIAL\4352789_33_BM_surveillance_digues_PI_Ambes\05_ETUDES\052_Calculs\Basedonnees\VTA_Ambes_ind2_PVR.sqlite"
    SLFILE = r"C:\01_WORKINGDIR\orange\toto.sqlite"
    SLFILE = r"C:\01_WORKINGDIR\GPMB\c_merge_ass\mergeddbase.sqlite"
    SLFILE = r"C:\Users\patrice.verchere\OneDrive - ARTELIA\Documents\lamia\tpo\test01.sqlite"

    tempparser = DBaseParserFactory("spatialite").getDbaseParser()
    tempparser.loadDBase(dbtype="Spatialite", slfile=SLFILE)

    app = initQGis()
    # canvas = qgis.gui.QgsMapCanvas()

    # qgiscanvas = QgisCanvas(canvas)

    print("start ReportCore")

    reportcore = ReportCore(tempparser, messageinstance=tempparser.messageinstance)
    if PROFILING:
        pr.enable()

    # try:

    # Infralineaire Equipementhydraulique Desordres
    reportcore.runReport(
        r"C:\000_testdigue\des.pdf",
        "TRAMprocesverbalmiseadisposition",
        pkzonegeos=[],
        pklist=None,
    )
    # except Exception as e:
    #     print(e)

    if PROFILING:
        pr.disable()
        cprofilepath = os.path.join(os.path.dirname(__file__), "pyreport.cprof")
        pr.dump_stats(cprofilepath)

    # REm : run     python -m snakeviz pyreport.cprof       for viz

    exitQGis()


if __name__ == "__main__":
    logging.basicConfig(stream=sys.stderr)
    logging.getLogger("Lamia_unittest").setLevel(logging.DEBUG)
    main(sys.argv[1:])

