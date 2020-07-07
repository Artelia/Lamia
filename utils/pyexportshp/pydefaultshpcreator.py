import os, sys

import qgis, qgis.core

lamiapath = os.path.join(os.path.join(os.path.dirname(__file__)), "..", "..")
sys.path.append(lamiapath)

from test.test_utils import *
import Lamia
from Lamia.dbasemanager.dbaseparserfactory import DBaseParserFactory


def createDefaultTxtExport(dbaseparser, tablename):

    dbaseparser.dbasetables = dbaseparser.dbconfigreader.dbasetables
    tablestoiterate = [tablename] + dbaseparser.getParentTable(tablename)
    pathfiletowrite = os.path.join(os.path.dirname(__file__), tablename + ".txt")

    filetowrite = open(pathfiletowrite, "w")

    for table in tablestoiterate:
        filetowrite.write("\n")
        filetowrite.write(f"###{table}\n")
        filetowrite.write(
            "#name".ljust(20)
            + "type".ljust(21)
            + "cst".ljust(21)
            + "value".ljust(21)
            + "\n"
        )
        for fieldname, fieldconf in dbaseparser.dbasetables[table]["fields"].items():
            # define export type
            shptype = ""
            if fieldconf["PGtype"] in ["INT"]:
                shptype = "Int"
            elif fieldconf["PGtype"] in ["Real"]:
                shptype = "Double"
            else:
                shptype = "String"

            # define cst txt
            csttxt = ""
            if "Cst" in fieldconf.keys():
                csttxt = fieldname

            # write line
            filetowrite.write(
                f"{fieldname.ljust(20)};{shptype.ljust(20)};{csttxt.ljust(20)};{tablename}_now.{fieldname}\n"
            )

    # geom part
    if "geom" in dbaseparser.dbasetables[tablename].keys():
        filetowrite.write("\n")
        filetowrite.write("###geom\n")
        filetowrite.write(
            f"{'geom'.ljust(20)};{'String'.ljust(20)};{''.ljust(20)};ST_AsText({tablename}_now.geom)\n"
        )

    # main part
    filetowrite.write("\n")
    filetowrite.write("###main\n")
    filetowrite.write(f"FROM {tablename}_now\n")

    filetowrite.close()


def main(argv):

    dbaseparser = DBaseParserFactory("spatialite").getDbaseParser()
    """
        "base3_urbandrainage",
        "base3_waterdistribution",
        "base3_constructionsite",
        "base3_faunaflora",
        "base3_levee",
    """
    dbaseparser.dbconfigreader.createDBDictionary("base3_faunaflora")
    createDefaultTxtExport(dbaseparser, "node")
    createDefaultTxtExport(dbaseparser, "edge")
    createDefaultTxtExport(dbaseparser, "surface")


if __name__ == "__main__":
    main(sys.argv[1:])
