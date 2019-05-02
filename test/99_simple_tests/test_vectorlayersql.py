import qgis
import qgis.utils

try:
    qgisversion_int = qgis.utils.QGis.QGIS_VERSION_INT
except AttributeError:  # qgis 3
    qgisversion_int = qgis.utils.Qgis.QGIS_VERSION_INT



if int(str(qgisversion_int)[0:3]) < 220:
    uri = qgis.core.QgsDataSourceURI()
else:
    uri = qgis.core.QgsDataSourceUri()

uri = qgis.core.QgsDataSourceUri()

spatialitefile = "C://000_testdigue//temp_base2_assainissement//test01.sqlite"
sql = "(SELECT * FROM Noeud)"

uri.setDatabase(spatialitefile)
#uri.setDataSource('', sql , 'geom' ,'','pk_noeud')
uri.setDataSource('', sql , 'geom' ,'','pk_noeud' )

print(uri.uri())

layer = qgis.core.QgsVectorLayer(uri.uri(), 'test', 'spatialite')

print([fet.id() for fet in layer.getFeatures() ])

print('finished')