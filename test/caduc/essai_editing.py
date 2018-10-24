vl = iface.activeLayer()

cvs = qgis.utils.iface.mapCanvas()

mtool = qgis.gui.QgsMapToolEdit(cvs)

vl.startEditing()

if True:
    cvs.setMapTool(mtool)
    
#iface.actionToggleEditing()



#mtool.activate()

