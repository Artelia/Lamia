# -*- coding: utf-8 -*-

"""
/***************************************************************************
 PostTelemac
                                 A QGIS plugin
 Post Traitment or Telemac
                              -------------------
        begin                : 2015-07-07
        git sha              : $Format:%H$
        copyright            : (C) 2015 by Artelia
        email                : patrice.Verchere@arteliagroup.com
 ***************************************************************************/

 ***************************************************************************/
 get Image class
 Generate a Qimage from selafin file to be displayed in map canvas 
 with tht draw method of posttelemacpluginlayer

Versions :
0.0 : debut

 ***************************************************************************/
"""
import os
import qgis
import qgis.gui
# import time

from pyspatialite import dbapi2 as db
import shutil
import os

print('debut')

path='c://test_db.sqlite'

#shutil.rmtree(path)
if False:
    try:
        os.remove(path)
    except WindowsError:
        print('no file')

conn = db.connect(path)

cur = conn.cursor()

# testing library versions
rs = cur.execute('SELECT sqlite_version(), spatialite_version()')
for row in rs:
    msg = "> SQLite v%s Spatialite v%s" % (row[0], row[1])
    print msg

if True:

    try:
        sql="SELECT DiscardGeometryColumn('test_pt', 'geom')"
        print(sql)
        cur.execute(sql)
    except Exception as e:
        print('err',e)


    try:
        sql="SELECT DiscardGeometryColumn('test_point2', 'geom')"
        print(sql)
        cur.execute(sql)
    except Exception as e:
        print('err',e)

    try:
        sql = 'DROP TABLE test_pt'
        print(sql)
        cur.execute(sql)
    except Exception as e:
        print('err',e)


    try:
        sql = 'DROP TABLE test_point2'
        print(sql)
        cur.execute(sql)
    except Exception as e:
        print('err',e)

if False:
    sql = " SELECT DiscardSpatialIndex('test_pt', 'geom') "
    cur.execute(sql)


if True:
    sql = 'SELECT InitSpatialMetadata()'
    print(sql)
    cur.execute(sql)

# creating a POINT table
sql = 'CREATE TABLE test_pt ('
sql += 'id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT ,'
sql += 'name TEXT NOT NULL)'
print(sql)
cur.execute(sql)
# creating a POINT Geometry column
sql = "SELECT AddGeometryColumn('test_pt',"
sql += "'geom', 3945, 'POINT', 'XY')"
print(sql)
cur.execute(sql)

if False:
    sql = "SELECT CreateSpatialIndex('test_pt', 'geom')"
    cur.execute(sql)


sql = "PRAGMA table_info(test_pt)"
print(sql)
rs = cur.execute(sql)
for row in rs:
    print(row)



# inserting some POINTs
# please note well: SQLite is ACID and Transactional
# so (to get best performance) the whole insert cycle
# will be handled as a single TRANSACTION
for i in range(10):
    name = "test POINT #%d" % (i+1)
    geom = "GeomFromText('POINT("
    geom += "%f " % (i / 1000.0)
    geom += "%f" % (i / 1000.0)
    geom += ")', 3945)"
    #sql = "INSERT INTO test_pt (id, name, geom) "
    sql = "INSERT INTO test_pt ( name, geom) "
    #sql += "VALUES (%d, '%s', %s)" % (i+1, name, geom)
    sql += "VALUES ( '%s', %s)" % ( name, geom)
    #print(sql)
    cur.execute(sql)
conn.commit()

if False:
    sql = "SELECT * FROM  test_pt"
    rs = cur.execute(sql)
    for row in rs:
        print(row)

sql = "PRAGMA foreign_keys"
print(sql)
rs = cur.execute(sql)
for row in rs:
    print(row)

sql = "PRAGMA foreign_keys = ON"
cur.execute(sql)

sql = "PRAGMA foreign_keys"
print(sql)
rs = cur.execute(sql)
for row in rs:
    print(row)



sql = 'CREATE TABLE test_point2('
sql += '  id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT  , '
sql += '    name2   TEXT, '
sql += '    pointID   INTEGER NOT NULL, '
sql += '    FOREIGN KEY(pointID) REFERENCES test_pt(id) )'
print(sql)
cur.execute(sql)
# creating a POINT Geometry column
sql = "SELECT AddGeometryColumn('test_point2',"
sql += "'geom', 3945, 'POINT', 'XY')"
print(sql)
cur.execute(sql)

sql = "PRAGMA table_info(test_point2)"
print(sql)
rs = cur.execute(sql)
for row in rs:
    print(row)

if True:
    uri = QgsDataSourceURI()

    uri.setDatabase(path)
    uri.setDataSource('','test_point2','geom')
    
    vlayer = QgsVectorLayer(uri.uri(), 'test1', 'spatialite')
    
    QgsMapLayerRegistry.instance().addMapLayer(vlayer)
    print('****************')
    
    uri = QgsDataSourceURI()

    uri.setDatabase(path)
    uri.setDataSource('','test_pt','geom')
    
    vlayer = QgsVectorLayer(uri.uri(), 'test0', 'spatialite')
    
    QgsMapLayerRegistry.instance().addMapLayer(vlayer)
    print('****************')
    
    
    
    
    for fet in vlayer.getFeatures():
        print(fet.id())


try:
    sql = "INSERT INTO test_point2 (  name2, pointID, geom) VALUES (  'test POINT #20', 20, GeomFromText('POINT(0.008000 0.008000)', 3945))"
    print(sql)
    cur.execute(sql)
except db.IntegrityError as e:
    print('err',e)



try:
    sql = "INSERT INTO test_point2 (  name2, pointID, geom) VALUES ( 'test POINT #9', 9, GeomFromText('POINT(0.008000 0.008000)', 3945))"
    print(sql)
    cur.execute(sql)
    conn.commit()
except db.IntegrityError as e:
    print('err',e)



conn.commit()

if True:
    sql = "SELECT * FROM  test_point2"
    rs = cur.execute(sql)
    for row in rs:
        print(row)
        
        
        
if True:
    vlayer.reload()
    qgis.utils.iface.mapCanvas().refresh()
    print('*************')
    for fet in vlayer.getFeatures():
        print(fet.id())
        
        
try:
    rs.close()
except:
    print('no rs')
conn.close()

print('fin')
