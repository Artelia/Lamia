import os
import sys
if sys.version_info.major == 2:
    uri = qgis.core.QgsDataSourceURI()
else:
    uri = qgis.core.QgsDataSourceUri()

if True:
    #path = os.path.join(os.path.dirname(__file__), baurech.sqlite)
    path = "U://FR//BOR//VT//PVR//20_LAMIA//0_Github//Lamia//test//99_scriptqgis//baurech.sqlite"
    print('path',path)
    uri.setDatabase(path)
    uri.setDataSource('', '(SELECT * FROM Desordre)', 'geom','','id_desordre')
    #uri.setDataSource('', 'Infralineaire_qgis', 'geom','','id_desordre')

    print(uri.uri())

    vl = qgis.core.QgsVectorLayer(uri.uri(), 'Desordre', 'spatialite')

    pr = vl.dataProvider()
    print('pr',pr)
    if sys.version_info.major == 3:
        print(pr.dataSourceUri())
        print('key col',pr.uri().keyColumn () )
        print(pr.pkAttributeIndexes () )
        print(pr.allFeatureIds () )
        
        
        print(pr.ProviderOptions )
         
        pr.reloadData ()

if False:
    vl = qgis.core.QgsVectorLayer("dbname='U://FR//BOR//VT//PVR//20_LAMIA//0_Github//Lamia//test//99_scriptqgis//baurech.sqlite' table = '(SELECT * FROM Desordre)' (geom) key='lid_objet'", "lolo", "spatialite")
        



print([fet.id() for fet in vl.getFeatures()])
print(vl.featureCount() )
try:
    if sys.version_info.major == 2:
        print(vl.getFeatures(qgis.core.QgsFeatureRequest(4)).next() )
        
    else:
        print(vl.getFeatures(qgis.core.QgsFeatureRequest(4)).__next__() )
        
    print(list(vl.getFeatures(qgis.core.QgsFeatureRequest(4)) ))
    
except Exception as e:
    print('no id 4')
    
if sys.version_info.major == 2:
    qgis.core.QgsMapLayerRegistry.instance().addMapLayer(vl)
else:
    qgis.core.QgsProject.instance().addMapLayer(vl)

print('ok')