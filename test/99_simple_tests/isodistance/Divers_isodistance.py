# -*- coding: utf-8 -*-

##[00_divers]=group

##Table_point=vector point
##Table_ligne=vector Line
##id_point=field Table_point

##maxcost=number 200.0
##nbre_max_resultat_par_ligne=number 2

##output_layer_cost=output vector
##output_layer_point=output vector


import qgis
import qgis.utils
import qgis.core
import qgis.networkanalysis
# import qgis.PyQt.QtCore
from qgis.PyQt import QtCore, QtGui
import os
#from qgis.PyQt.QtGui import QApplication

if False:
    from qgis.core import *
    from qgis.gui import *
    from qgis.networkanalysis import *
    from qgis.PyQt.QtCore import *
    from qgis.PyQt.QtGui import *




debug = False

if debug: print('start - qgis.utils.iface : ',qgis.utils.iface)

# ********************************************************************************
# Load vector layers  ********************************************************************
# ********************************************************************************

if qgis.utils.iface is not None:
    from processing.tools.vector import VectorWriter
    layerline=processing.getObjectFromUri(Table_ligne)
    layerpoint = processing.getObjectFromUri(Table_point)
else:
    if True:
        app = QtGui.QApplication([])
        qgis.core.QgsApplication.setPrefixPath("C://OSGeo4W64//apps//qgis-ltr", True)
        qgis.core.QgsApplication.initQgis()

    pathpoint = os.path.join(os.path.dirname(__file__), 'test_PI_ind0.shp')
    layerpoint = qgis.core.QgsVectorLayer(pathpoint, 'test1', 'ogr')
    pathline = os.path.join(os.path.dirname(__file__), 'voiries_traitees_cc44_ind0.shp')
    layerline =  qgis.core.QgsVectorLayer(pathline, "test2", "ogr")
    maxcost = 200
    nbre_max_resultat_par_ligne = 2
    id_point=0


# ********************************************************************************
# Build output layers   and other*******************************************************************


if True:
    #layerlinepoint = qgis.core.QgsVectorLayer("Point?crs=epsg:2154", "result", "memory")
    layerlinepoint = qgis.core.QgsVectorLayer("Point?crs=" + layerline.crs().authid(), "result", "memory")
    layerlinepoint.startEditing()
    for feat in layerline.getFeatures():
        fetgeompoly = feat.geometry().asPolyline()
        for point in fetgeompoly:
            featto = qgis.core.QgsFeature()
            featto.setGeometry(qgis.core.QgsGeometry().fromPoint(point))
            layerlinepoint.addFeatures([featto])
    layerlinepoint.commitChanges()
    spindex = qgis.core.QgsSpatialIndex(layerlinepoint.getFeatures())


if True:
    #templayer = qgis.core.QgsVectorLayer("LineString?crs=epsg:2154", "result", "memory")
    templayer = qgis.core.QgsVectorLayer("LineString?crs=" + layerline.crs().authid(), "result", "memory")
    templayer.startEditing()
    templayer.dataProvider().addAttributes([qgis.core.QgsField('idfrom',QtCore.QVariant.Int),qgis.core.QgsField('cost',QtCore.QVariant.Double)])
    templayer.updateFields()
    templayer.startEditing()
    if debug: print('temp layer built')

if True and qgis.utils.iface is not None :
    outlayerline = VectorWriter(output_layer_cost,
                                         None,
                                          [qgis.core.QgsField('idfrom',QtCore.QVariant.Int),qgis.core.QgsField('cost',QtCore.QVariant.Double)],
                                         qgis.core.QGis.WKBMultiLineString,
                                         layerline.crs())

    outlayerpoint = VectorWriter(output_layer_point,
                                         None,
                                          [qgis.core.QgsField('idfrom',QtCore.QVariant.Int)],
                                         qgis.core.QGis.WKBMultiLineString,
                                         layerline.crs())


    if debug: print('out layer built')







# ********************************************************************************
# Build progressbar  ********************************************************************
# ********************************************************************************

progress = None
if True and qgis.utils.iface is not None :
    progress = QtGui.QProgressBar()
    maxfeat = len([feat.id() for feat in layerpoint.getFeatures()])
    progress.setMaximum(maxfeat) 
    progressMessageBar = qgis.utils.iface.messageBar()
    progressMessageBar.pushWidget(progress)
    if debug: print('progress bar built')
        
if False:
    rt = QgsRubberBand(qgis.utils.iface.mapCanvas(), True)
    rt.setColor(Qt.red)
    rt.setWidth (3)


# ********************************************************************************
# network analysys  ********************************************************************
# ********************************************************************************


director = qgis.networkanalysis.QgsLineVectorLayerDirector(layerline, -1, '', '', '', 3)
properter = qgis.networkanalysis.QgsDistanceArcProperter()
director.addProperter(properter)





for j, featpoint in enumerate(layerpoint.getFeatures()):
    # print(featpoint.id())
    if progress: progress.setValue(j)
    if debug: print('point : ',featpoint.id() )

    pointid = featpoint[id_point]
    pStart = featpoint.geometry().asPoint()

    layernearestid = spindex.nearestNeighbor(pStart, 1)[0]
    featgeom = layerlinepoint.getFeatures(qgis.core.QgsFeatureRequest(layernearestid)).next()
    featgeompoint = featgeom.geometry().asPoint()

    if qgis.utils.iface is not None:
        featoutpoint = qgis.core.QgsFeature()
        featoutpoint.setGeometry(qgis.core.QgsGeometry().fromPolyline([featgeompoint,featgeompoint]))
        featoutpoint.setAttributes([pointid])
        outlayerpoint.addFeature(featoutpoint)


    if debug: print('geom ',pStart,  featgeompoint)
    #recontrct builder every time
    builder = qgis.networkanalysis.QgsGraphBuilder(layerline.crs())
    tiedPoints = director.makeGraph(builder, [featgeompoint])
    graph = builder.graph()
    tStart = tiedPoints[0]
    idStart = graph.findVertex(tStart)

    (tree, cost) = qgis.networkanalysis.QgsGraphAnalyzer.dijkstra(graph, idStart, 0)

    if debug: print('tree done ')

    i = 0
    while i < len(cost):
        try:
            if tree[i] != -1 and cost[i] <= maxcost:
                inVertexId = graph.arc(tree [i]).inVertex()
                point1 = graph.vertex(inVertexId).point()
                outVertexId = graph.arc(tree [i]).outVertex()
                if True and outVertexId != -1 :

                    point2 = graph.vertex(outVertexId).point()

                    featout = qgis.core.QgsFeature()
                    qgspoint1 = qgis.core.QgsPoint(point1.x(), point1.y())
                    qgspoint2 = qgis.core.QgsPoint(point2.x(), point2.y())

                    if debug: print('add path ',qgspoint1, qgspoint2 )

                    featout.setGeometry(qgis.core.QgsGeometry.fromPolyline([qgspoint1, qgspoint2]))
                    featout.setAttributes([pointid,cost[i]])
                    templayer.addFeatures([featout])
        except Exception as e:
            print('error, e')

        i += 1

templayer.commitChanges()
if debug: print('temp layer done ')
# ********************************************************************************
# build output layer  ********************************************************************
# ********************************************************************************

if qgis.utils.iface is not None:
    idsdone=[]
    for feat in templayer.getFeatures():
        featid = feat.id()
        if featid in idsdone:
            continue
        featgeom = feat.geometry()
        otherfeatures = templayer.getFeatures(qgis.core.QgsFeatureRequest().setFilterRect(featgeom.boundingBox()))
        tempresult=[]
        for otherfeat in otherfeatures:
            if otherfeat.id() not in idsdone and otherfeat.geometry().within(featgeom.buffer(0.01,12)):
                idsdone.append(otherfeat.id() )
                tempresult.append([otherfeat['cost'], otherfeat])
        tempresultsorted = sorted(tempresult)


        for temp in tempresultsorted[:nbre_max_resultat_par_ligne]:
            outlayerline.addFeature(temp[1])

    qgis.utils.iface.messageBar().clearWidgets()

if debug: print('finished ')