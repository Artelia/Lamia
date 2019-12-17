import qgis, os
import qgis.core
from qgis.PyQt import QtGui, uic, QtCore, QtXml
from pprint import pprint as pprint
from Lamia.Lamia.main.DBaseParser import DBaseParser
import sqlite3
from pprint import pprint



if False:
    qgis_path = "C://Program Files//OSGeo4W64-310//apps//qgis"
    app = qgis.core.QgsApplication([], True)
    qgis.core.QgsApplication.setPrefixPath(qgis_path, True)
    qgis.core.QgsApplication.initQgis()

slfile = os.path.join(os.path.dirname(__file__), 'autocommit', 'test01.sqlite')

connSLITE = sqlite3.dbapi2.connect(slfile)
connSLITE.enable_load_extension(True)
connSLITE.execute("SELECT load_extension('mod_spatialite')")
SLITEcursor = connSLITE.cursor()

sql = "BEGIN"
query = list(SLITEcursor.execute(sql))

sql = "INSERT INTO Objet (libelle) VALUES('test')"
query = list(SLITEcursor.execute(sql))

if False:
    sql = "COMMIT"
    query = list(SLITEcursor.execute(sql))

sql = "INSERT INTO Objet (libelle) VALUES('test')"
query = list(SLITEcursor.execute(sql))


sql = "SELECT * FROM Objet"
query = list(SLITEcursor.execute(sql))
print('*****')
pprint(query)

sql = 'SELECT last_insert_rowid()'
query = list(SLITEcursor.execute(sql))
print('*****')
pprint(query)

connSLITE.close()

print('step1')




