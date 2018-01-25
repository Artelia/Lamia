import os


path = os.path.normpath('//Svpborfs01//data//FLUVIAL//4352024_33_Conformite_digues_BM//5_Conception//51_Calculs//travail_fiches//test//test2.sqlite')

uri = QgsDataSourceURI()

uri.setDatabase(path)
uri.setDataSource('','desordres_obs','')

vlayer = QgsVectorLayer(uri.uri(), 'test', 'spatialite')
"""
print(uri.uri())
print(vlayer.geometryType())
print(vlayer.featureCount())
"""
QgsMapLayerRegistry.instance().addMapLayer(vlayer)

print( vlayer.isValid() )
