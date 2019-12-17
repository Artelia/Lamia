lay1 = iface.activeLayer()

templayer = QgsVectorLayer("U://FR//BOR//VT//PVR//20_LAMIA//0_Github//Lamia//test//testliaison//lien2.dbf", 'temp1', "ogr")
# QgsMapLayerRegistry.instance().addMapLayer(templayer)

for fet in templayer.getFeatures():
    print(fet.attributes())

joinObject = qgis.core.QgsVectorLayerJoinInfo()
joinObject.setJoinFieldName('field_1')
joinObject.setTargetFieldName('liaison')
joinObject.setJoinLayerId(templayer.id())
joinObject.setUsingMemoryCache(True)
joinObject.setJoinLayer(templayer)

lay1.addJoin(joinObject)





