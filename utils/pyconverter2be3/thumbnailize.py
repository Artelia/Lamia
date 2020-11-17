import os, sys, shutil

lamiapath = os.path.join(os.path.join(os.path.dirname(__file__)), "..", "..", "..")
sys.path.append(lamiapath)

import Lamia
from Lamia.api.libs.odsreader.ODSReader import ODSReader
from Lamia.api.dbasemanager.dbaseparserfactory import DBaseParserFactory

if True:
    sourcefile = r"C:\01_WORKINGDIR\GPMB\final_ass\mergeddbase.sqlite"
    sourcefile = r"U:\FR\BOR\VT\PVR\sncf2\LANDY-09-2020.sqlite"
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
sqlitedbasesource.beginTransaction()
for pk_res, filename in res:
    if filename:
        completefilepath = sqlitedbasesource.completePathOfFile(filename)
        if os.path.isfile(completefilepath):
            sqlitedbasesource.createBlobThumbnail(pk_res, completefilepath)
sqlitedbasesource.commitTransaction()
