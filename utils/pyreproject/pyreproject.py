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
    SLFILE = r"M:\FR\BOR\VT\FLUVIAL\4352789_33_BM_surveillance_digues_PI_Ambes\05_ETUDES\052_Calculs\Basedonnees\VTA_Ambes_ind2_PVR.sqlite"

    ReprojectCRS = "2154"

    tempparser = DBaseParserFactory("spatialite").getDbaseParser()
    tempparser.loadDBase(dbtype="Spatialite", slfile=SLFILE)

    app = initQGis()
    # canvas = qgis.gui.QgsMapCanvas()

    # qgiscanvas = QgisCanvas(canvas)

    print("start Reprojecting")

    for tablename in tempparser.dbasetables.keys():

        if not "geom" in tempparser.dbasetables[tablename].keys():
            continue

        print(f'Reprojecting {tablename} ...)

        sql = f"UPDATE geometry_columns SET srid={ReprojectCRS} WHERE f_table_name='{tablename.lower()}'"
        tempparser.query(sql)

        sql = f"UPDATE {tablename} SET geom = ST_Transform(geom, {ReprojectCRS})"
        tempparser.query(sql)

    sql = f"UPDATE Basedonnees SET crs = {ReprojectCRS}"
    tempparser.query(sql)

    print("Reprojecting done")

    if PROFILING:
        pr.disable()
        cprofilepath = os.path.join(os.path.dirname(__file__), "pyreport.cprof")
        pr.dump_stats(cprofilepath)

    # REm : run     python -m snakeviz pyreport.cprof       for viz

    exitQGis()


if __name__ == "__main__":
    main(sys.argv[1:])

