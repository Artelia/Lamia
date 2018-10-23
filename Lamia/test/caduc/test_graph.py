import qgis
from qgis.networkanalysis import *
from qgis.PyQt import QtGui, uic, QtCore, QtXml

# https://docs.qgis.org/2.18/en/docs/pyqgis_developer_cookbook/network_analysis.html


print('begin')

uri = qgis.core.QgsDataSourceURI()
uri.setDatabase('C://000_testimportBM//BD_BM_ind3.sqlite')
uri.setDataSource('', 'Infralineaire', 'geom')
vlayer = qgis.core.QgsVectorLayer(uri.uri(), 'Infralineaire', 'spatialite')

#qgis.core.QgsMapLayerRegistry.instance().addMapLayer(vlayer)

print(vlayer.isValid())

print('director')

director = QgsLineVectorLayerDirector(vlayer, -1, '', '', '', 3)
properter = QgsDistanceArcProperter()
director.addProperter(properter)

print('crs')
crs = vlayer.crs()
builder = QgsGraphBuilder(crs)

print('QgsGraphBuilder')

#pStart = qgis.core.QgsPoint(1.41944e+06,4.19085e+06)
pStart = qgis.core.QgsPoint(1419444.7139,4190845.018347)
pStop = qgis.core.QgsPoint(1419652.749903,4196561.779806)
pStop = qgis.core.QgsPoint(1417370.095717,4196164.153156)
print('pStart')
tiedPoints = director.makeGraph(builder, [pStart,pStop])
print('tiedPoints',tiedPoints)

graph = builder.graph()

tStart = tiedPoints[0]
tStop = tiedPoints[1]

idStart = graph.findVertex(pStart)
print('idStart',idStart)

tree = QgsGraphAnalyzer.shortestTree(graph, idStart, 0)
print('tree',tree, tree.vertexCount(), tree.arcCount())

# print('tree',tree.findVertex(tStart), tree.findVertex(tStop))
idStart = tree.findVertex(tStart)
idStop = tree.findVertex(tStop)




if False:
    if idStop == -1:
      print "Path not found"
    else:
      p = []
      while (idStart != idStop):
        l = tree.vertex(idStop).inArc()
        if len(l) == 0:
          break
        e = tree.arc(l[0])
        p.insert(0, tree.vertex(e.inVertex()).point())
        idStop = e.outVertex()

      p.insert(0, tStart)
      rb = qgis.gui.QgsRubberBand(qgis.utils.iface.mapCanvas())
      rb.setColor(QtCore.Qt.red)
      rb.setWidth(5)

      for pnt in p:
        rb.addPoint(pnt)


print('end')
