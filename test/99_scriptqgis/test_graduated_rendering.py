from qgis.PyQt import uic, QtCore, QtGui

lay1 = iface.activeLayer()

if False:
    target_field  ='result_amc_val'
    myRangeList = []

    symbol = qgis.core.QgsSymbol.defaultSymbol(lay1.geometryType())
    symbol.setColor(QtGui.QColor("#f5c9c9"))
    myRange = qgis.core.QgsRendererRange(0, 5, symbol, 'Group 1')
    myRangeList.append(myRange)

    myRenderer = qgis.core.QgsGraduatedSymbolRenderer(target_field, myRangeList)

    myRenderer.setMode(qgis.core.QgsGraduatedSymbolRenderer.Custom)
    # myRenderer.setClassificationMethod(qgis.core.QgsClassificationMethod.Custom)
    myRenderer.updateClasses(lay1,5)
    
if True:
    myRenderer = QgsGraduatedSymbolRenderer()
    # symbol = createMarkerSymbol()
    if lay1.geometryType() == QgsWkbTypes.LineGeometry :
        symbol = qgis.core.QgsSymbol.defaultSymbol(lay1.geometryType())
        symbol = QgsLineSymbol()
        symbol.setWidth(2)
    
    myRenderer.setSourceSymbol(symbol.clone())
    
    myStyle = QgsStyle().defaultStyle()
    defaultColorRampNames = myStyle.colorRampNames()
    print(defaultColorRampNames)
    
    ramp = myStyle.colorRamp('Spectral')
    ramp.invert()
    
    print(ramp)
    
    myRenderer.updateColorRamp(ramp)
    
    
    myRenderer.setClassAttribute("result_amc_val")
    # myRenderer.setMode(qgis.core.QgsGraduatedSymbolRenderer.Custom)
    
    myRenderer.updateClasses(lay1, myRenderer.EqualInterval, 3)
    
    print(myRenderer.ranges())
    
    

lay1.setRenderer(myRenderer)
lay1.repaintRequested.emit()


