vl = iface.activeLayer()

if False:
    spindex = qgis.core.QgsSpatialIndex(vl.getFeatures())


    layernearestid = spindex.nearestNeighbor(QgsPoint(0,0), 1)

fetsel = vl.selectedFeatures()
print(fetsel)

print('ok')