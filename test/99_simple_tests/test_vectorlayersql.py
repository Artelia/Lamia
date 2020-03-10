import qgis
import qgis.utils
import os

qgis_path = '/usr/bin/qgis'
qgis_path = '/usr'

app = qgis.core.QgsApplication([], True)
qgis.core.QgsApplication.setPrefixPath(qgis_path, True)
qgis.core.QgsApplication.initQgis()

try:
    qgisversion_int = qgis.utils.QGis.QGIS_VERSION_INT
except AttributeError:  # qgis 3
    qgisversion_int = qgis.utils.Qgis.QGIS_VERSION_INT



if int(str(qgisversion_int)[0:3]) < 220:
    uri = qgis.core.QgsDataSourceURI()
else:
    uri = qgis.core.QgsDataSourceUri()

uri = qgis.core.QgsDataSourceUri()

spatialitefile = "/home/docker/temp_base2_ass2/test01.sqlite"
print(os.path.isfile(spatialitefile))

sql = "(SELECT * FROM Noeud)"

uri.setDatabase(spatialitefile)
#uri.setDataSource('', sql , 'geom' ,'','pk_noeud')
uri.setDataSource('', sql , 'geom' ,'','pk_noeud' )

print(uri.uri())

layer = qgis.core.QgsVectorLayer(uri.uri(), 'test', 'spatialite')

print([fet.id() for fet in layer.getFeatures() ])

print('finished')