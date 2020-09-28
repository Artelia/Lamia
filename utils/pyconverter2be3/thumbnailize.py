import os, sys, shutil

lamiapath = os.path.join(os.path.join(os.path.dirname(__file__)), "..", "..")
sys.path.append(lamiapath)

import Lamia
from Lamia.libs.odsreader.ODSReader import ODSReader
from Lamia.dbasemanager.dbaseparserfactory import DBaseParserFactory

if True:
    sourcefile = r"C:\01_WORKINGDIR\GPMB\final_ass\mergeddbase.sqlite"
    sourcefile = r"M:\FR\BOR\VT\FLUVIAL\4352024_33_Conformite_digues_BM\6_Reglementaire\61_Calculs\Basedonnees\BD_totale_ind13_tempPVR.sqlite"
    sqlitedbasesource = DBaseParserFactory("spatialite").getDbaseParser()
    sqlitedbasesource.loadDBase(dbtype="Spatialite", slfile=sourcefile)

if False:
    sqlitedbasesource = DBaseParserFactory("postgis").getDbaseParser()
    sqlitedbasesource.loadDBase(
        dbtype="Postgis",
        host="localhost",
        # host="localhost",
        port=5432,
        dbname="lamiaunittest",
        schema="importgpmb",
        user="pvr",
        password="pvr",
    )

sql = "SELECT pk_resource, file FROM resource"
res = sqlitedbasesource.query(sql)
for pk_res, filename in res:
    if filename:
        completefilepath = sqlitedbasesource.completePathOfFile(file)
        sqlitedbasesource.createBlobThumbnail(pk_res, completefilepath)
