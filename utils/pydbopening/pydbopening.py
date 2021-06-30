import os, sys, logging

import qgis, qgis.core

lamiapath = os.path.join(os.path.join(os.path.dirname(__file__)), "..", "..")
sys.path.append(lamiapath)

from test.test_utils import *
import Lamia

from Lamia.api.dbasemanager.dbaseparserfactory import DBaseParserFactory



SLFILE = r"C:\01_WORKINGDIR\ambes\VTA_Ambes_ind2_PVR_FJE.sqlite"
SLFILE = r"C:\01_WORKINGDIR\00_test\tetete.sqlite"

tempparser = DBaseParserFactory("spatialite").getDbaseParser()
tempparser.loadDBase(dbtype="Spatialite", slfile=SLFILE)

print("loaded")

sql = "INSERT INTO node (geom) VALUES (ST_GeomFromText('Point (446914.22767816123086959 6491802.08524716459214687)',2154))"
# sql = "UPDATE node SET geom = ST_GeomFromText('Point (446914.22767816123086959 6491802.08524716459214687)',2154) WHERE pk_node = 118"
tempparser.query(sql)

sql = "SELECT ST_astext(geom) from node"
res = tempparser.query(sql)
print(res[-1])