import qgis
import qgis.core

uri = qgis.core.QgsDataSourceURI()
# uri.setDatabase(file)
#
uri.setConnection("localhost", "5432", 'digue', "postgres", "PVR", qgis.core.QgsDataSourceURI.SSLdisable)
#uri.setConnection("127.0.0.1", "5432", "digue", "postgres", "PVR", qgis.core.QgsDataSourceURI.SSLdisable)
#uri.setConnection("127.0.0.1", "5432", "digue", "postgres", "PVR")


print('info', uri.connectionInfo())

# table="public"."desordre"

#uri.setDataSource("",  "troncon" , "geom","","ID")
uri.setDataSource("public",  'troncon' , "geom")
#uri.setDataSource("'public'", "'desordre'", "geom","","ID")
uri.setSrid('2154')
uri.setWkbType(1)

print('info', uri.connectionInfo())
print('key',uri.keyColumn())
print('key',uri.srid())
print('key',uri.table())
print('key',uri.service ())
print('key',uri.driver () )
print('key',uri.driver () )
print('key',uri.database () )

#\"public\".\"test\"


layer = qgis.core.QgsVectorLayer(uri.uri(False),"troncon", "postgres" )

print(layer.source())


print(layer.name(), [field.name() for field in layer.fields()] )

#qgis.core.QgsDataSourceUri.SSLDisable