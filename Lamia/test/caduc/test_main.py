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
import shutil
#import time
from pyspatialite import dbapi2 as db
from qgis.PyQt import QtGui

from InspectionDigueV2.src.dialog.InspectionDigue_dockwidget import InspectiondigueDockWidget
from InspectionDigueV2.src.dialog.InspectionDigue_windowwidget import InspectiondigueWindowWidget


def testCoreParserValue(canvas,loadfile=True,typedb="spatialite" ):

    print('begin')
    wind = InspectiondigueWindowWidget(canvas)
    wind.setParent(None)


    if loadfile:
        if typedb == "spatialite":
            # path = os.path.normpath('C://Users//patrice.verchere//Documents//GitHub//InspectionDigue//DBASE//test1.sqlite')
            # path = os.path.normpath('c://000_testdigue//testdbase.sqlite')
            # path = os.path.normpath('C://000_testimportBM//BD_BM_ind1.sqlite')
            # path = os.path.normpath('C://000_testimportBM//BD_BM_ind3.sqlite')
            #path = os.path.normpath('C://001_travail_BM//BD_SIJALAG_ind0_travail2.sqlite')
            #path = os.path.normpath('I://FLUVIAL//4352024_33_Conformite_digues_BM//6_Reglementaire//61_Calculs//Basedonnees//201710_Begles//BD_Begles_ind0.sqlite')
            path = os.path.normpath('C://000_testdigue//testBM//BD_Begles_ind0.sqlite')
            wind.dbase.loadQgisVectorLayers(path)

        elif typedb == "postgis":
            wind.dbase.loadQgisVectorLayers(dbasetype='postgis', dbname='PVR_test', schema='exportbm', user='postgres',
                                            host='localhost',
                                            password='PVR', port=5432)



    # canvas.setDestinationCrs(wind.dbase.dbasetables['Infralineaire']['layer'].crs())
    canvas.setDestinationCrs(qgis.core.QgsCoordinateReferenceSystem(2154))

    layerstoadd = []
    for tablename in wind.dbase.dbasetables.keys():
        layerstoadd.append(qgis.gui.QgsMapCanvasLayer(wind.dbase.dbasetables[tablename]['layerqgis']))

    canvas.setLayerSet(layerstoadd)
    # canvas.show()
    # canvas.setExtent(qgis.core.QgsRectangle(0, 0, 1, 1))
    canvas.setExtent(wind.dbase.dbasetables['Infralineaire']['layer'].extent())
    canvas.refresh()

    canvas.show()
    canvas.refresh()
    wind.show()


def testSpatialiteDbaseCreation(canvas):
    print('begin')
    wind = InspectiondigueWindowWidget(canvas)
    file = 'c://000_testdigue//testdbase.sqlite'
    file = 'C:\\000_testimportBM\\BD_BM_ind4.sqlite'

    crs = 3945

    #shutil.rmtree('c://000_testdigue//BDspatialite')


    originalfile = os.path.join(os.path.dirname(__file__), '..', 'DBASE', 'DBase_ind0.sqlite')
    shutil.copyfile(originalfile, file)

    # wind.dbase.createDbase(file = file,crs = crs,type = 'Digue',dbaseressourcesdirectory='c://000_testdigue//BDspatialite')
    wind.dbase.createDbase(file=file, crs=crs, type='Digue', dbaseressourcesdirectory='c://000_testimportBM//BDspatialite')

    if False:    #try to add features
        conn = db.connect(file)
        cur = conn.cursor()
        sql = "INSERT INTO OBJET (Commentaire) VALUES('test1');"
        print(sql)
        cur.execute(sql)
        conn.commit()
        sql = "INSERT INTO DESCRIPTIONSYSTEME (IdObjet) VALUES (1);"
        print(sql)
        cur.execute(sql)
        conn.commit()

        sql = "INSERT INTO TRONCON (Nom, geom) VALUES ('popo', GeomFromText('LINESTRING(0 0, 1 1)',2154 ));"
        print(sql)
        cur.execute(sql)
        conn.commit()

        sql = "INSERT INTO OBJET (Commentaire) VALUES('test1');"
        print(sql)
        cur.execute(sql)
        conn.commit()

        sql = "INSERT INTO RESSOURCESDOC (IdObjet) VALUES (2 );"
        print(sql)
        cur.execute(sql)
        conn.commit()

        sql = "INSERT INTO PHOTO (file, IdObjet,IdRes,LkObjet,geom) VALUES ('c://popo',2,1, 1, GeomFromText('POINT(0 0)',2154 ));"
        print(sql)
        cur.execute(sql)
        conn.commit()







        try:
            rs.close()
        except:
            print('no rs')
        conn.close()
    if False:
        window = QtGui.QMainWindow()
        layout = QtGui.QHBoxLayout()
        layout.addWidget(canvas)
        layout.addWidget(wind)

        #canvas.show()
        #canvas.refresh()
        window.show()

    print('fin')



def testPostGisDbaseCreation(canvas):
    print('begin')
    wind = InspectiondigueWindowWidget(canvas)
    #file = 'c://testdbase.sqlite'
    crs = 3945

    shutil.rmtree('c://000_testdigue//BDpostgis')

    #originalfile = os.path.join(os.path.dirname(__file__), '..', 'DBASE', 'DBase_ind0.sqlite')
    #shutil.copyfile(originalfile, file)

    #wind.dbase.createDbase(file = file,crs = crs,type = 'Digue')

    wind.dbase.createDbase(crs = crs,type = 'Digue', dbasetype='postgis', dbname='PVR_test', schema = 'diguebebe', user='postgres', host='localhost',
                password='PVR',dbaseressourcesdirectory='c://000_testdigue//BDpostgis')

    if False:    #try to add features
        conn = db.connect(file)
        cur = conn.cursor()
        sql = "INSERT INTO OBJET (Commentaire) VALUES('test1');"
        print(sql)
        cur.execute(sql)
        conn.commit()
        sql = "INSERT INTO DESCRIPTIONSYSTEME (IdObjet) VALUES (1);"
        print(sql)
        cur.execute(sql)
        conn.commit()

        sql = "INSERT INTO TRONCON (Nom, geom) VALUES ('popo', GeomFromText('LINESTRING(0 0, 1 1)',2154 ));"
        print(sql)
        cur.execute(sql)
        conn.commit()

        sql = "INSERT INTO OBJET (Commentaire) VALUES('test1');"
        print(sql)
        cur.execute(sql)
        conn.commit()

        sql = "INSERT INTO RESSOURCESDOC (IdObjet) VALUES (2 );"
        print(sql)
        cur.execute(sql)
        conn.commit()

        sql = "INSERT INTO PHOTO (file, IdObjet,IdRes,LkObjet,geom) VALUES ('c://popo',2,1, 1, GeomFromText('POINT(0 0)',2154 ));"
        print(sql)
        cur.execute(sql)
        conn.commit()







        try:
            rs.close()
        except:
            print('no rs')
        conn.close()
    if False:
        window = QtGui.QMainWindow()
        layout = QtGui.QHBoxLayout()
        layout.addWidget(canvas)
        layout.addWidget(wind)

        #canvas.show()
        #canvas.refresh()
        window.show()

    print('fin')

if True:
    qgis_path = "C://OSGeo4W64//apps//qgis"
else:
    qgis_path = "C://OSGeo4W64//apps//qgis-dev"

app = qgis.core.QgsApplication([], True)
qgis.core.QgsApplication.setPrefixPath(qgis_path, True)
qgis.core.QgsApplication.initQgis()
canvas = qgis.gui.QgsMapCanvas()
canvas.enableAntiAliasing(True)

##test1 : DBase creation
# testSpatialiteDbaseCreation(canvas)
# testPostGisDbaseCreation(canvas)

##test2 : plugin

testCoreParserValue(canvas,True)

# testCoreParserValuePG(canvas,True)


app.exec_()
qgis.core.QgsApplication.exitQgis()
print('ok')
