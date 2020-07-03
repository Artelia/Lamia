import os, sys

import qgis, qgis.core

lamiapath = os.path.join(os.path.join(os.path.dirname(__file__)), "..", "..")
sys.path.append(lamiapath)

from test.test_utils import *
import Lamia

from Lamia.dbasemanager.dbaseparserfactory import DBaseParserFactory

from Lamia.libslamia.lamiadxfexport.lamiadxfexport import ExporDxfCore

import cProfile

PROFILING = True


def main(argv):
    if PROFILING:
        pr = cProfile.Profile()

    # SLFILE = r"C:\111_GitProjects\Lamia\test\datas\lamia_digue\test01.sqlite"
    SLFILE = r"C:\111_GitProjects\Lamia\test\testtempfiles\c_creation\sl_base3_constructionsite_Lamia\test01.sqlite"

    tempparser = DBaseParserFactory("spatialite").getDbaseParser()
    tempparser.loadDBase(dbtype="Spatialite", slfile=SLFILE)

    app = initQGis()

    print("start dxfCore")

    lamiadxfexport = ExporDxfCore(tempparser)

    if PROFILING:
        pr.enable()

    lamiadxfexport.exportTopography(pktopotoexport=1, filename="toto.dxf")

    if PROFILING:
        pr.disable()
        cprofilepath = os.path.join(os.path.dirname(__file__), "pydxfexport.cprof")
        pr.dump_stats(cprofilepath)

    # REm : run     python -m snakeviz pydxfexport.cprof       for viz

    exitQGis()


if __name__ == "__main__":
    main(sys.argv[1:])

