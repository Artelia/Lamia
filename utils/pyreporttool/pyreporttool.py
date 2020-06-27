import os, sys

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

    tempparser = DBaseParserFactory("spatialite").getDbaseParser()
    tempparser.loadDBase(dbtype="Spatialite", slfile=SLFILE)

    app = initQGis()
    # canvas = qgis.gui.QgsMapCanvas()

    # qgiscanvas = QgisCanvas(canvas)

    print("start ReportCore")

    reportcore = ReportCore(tempparser, messageinstance=tempparser.messageinstance)
    if PROFILING:
        pr.enable()
    try:
        reportcore.runReport(
            r"C:\000_testdigue\test_rapport.pdf",
            "Desordres",
            pkzonegeos=[2],
            pklist=None,
        )
    except:
        pass

    if PROFILING:
        pr.disable()
        cprofilepath = os.path.join(os.path.dirname(__file__), "pyreport.cprof")
        print(cprofilepath)
        pr.dump_stats(cprofilepath)

    # REm : run
    # python -m snakeviz pyreport.cprof
    # for viz

    exitQGis()


if __name__ == "__main__":
    main(sys.argv[1:])

