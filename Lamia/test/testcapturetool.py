from qgis.PyQt import uic, QtCore, QtGui
import qgis
import qgis.gui
import qgis.utils

class mapToolCapture(qgis.gui.QgsMapToolCapture):

    stopCapture = QtCore.pyqtSignal(list)

    # def __init__(self, canvas, dockwdget, mode,layer):
    def __init__(self, canvas, dockwdget, mode):
        qgis.gui.QgsMapToolCapture.__init__(self, canvas, dockwdget, mode)
        self.canvas = canvas
        # self.layer = layer
        #self.mappoints = []
        
        
    
    def canvasReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            """
            if not self.isCapturing():
                self.startCapturing()
            """
            
            # mapPt,layerPt = self.transformCoordinates(event.pos())
            mapPt = event.snapPoint(qgis.gui.QgsMapMouseEvent.SnapProjectConfig )
            
            self.addVertex(mapPt)
            #self.mappoints.append(mapPt)
            #print(self.points(), mapPt)
            
            if self.mode() ==  qgis.gui.QgsMapToolAdvancedDigitizing.CapturePoint:
                if len(self.mappoints)>0:
                    #self.stopCapture.emit(self.mappoints)
                    self.stopCapture.emit(self.points())
                    self.stopCapturing()
                    # self.mappoints = []
            
        elif event.button() == QtCore.Qt.RightButton:
            # self.stopCapture.emit(self.mappoints)
            self.stopCapture.emit(self.points())
            self.stopCapturing()
            # self.mappoints = []
                
    if False:
        def transformCoordinates(self, canvasPt):
            return (self.toMapCoordinates(canvasPt),
                    self.toLayerCoordinates(self.layer, canvasPt))
                
                

    



class Test():
    def __init__(self, canvas,showcanvas=True):
        self.canvas = canvas
        self.widget = QtGui.QWidget()
        self.layout = QtGui.QVBoxLayout()
        if showcanvas:
            self.layout.addWidget(canvas)
        self.widget.setLayout(self.layout)
        self.button = QtGui.QPushButton("Do test")
        self.layout.addWidget(self.button)
        self.cadwdg = qgis.gui.QgsAdvancedDigitizingDockWidget(self.canvas)
        mode = qgis.gui.QgsMapToolAdvancedDigitizing.CaptureLine
        self.mtool = mapToolCapture(self.canvas, self.cadwdg, mode)
        self.button.clicked.connect(self.testMaptool)
        # self.widget.show()

    def testMaptool(self):
        if self.canvas.mapTool() != self.mtool:
            self.canvas.setMapTool(self.mtool)
        self.mtool.stopCapture.connect(self.setTempGeometry)
        # self.mtool.activate()
        self.mtool.startCapturing()

    def setTempGeometry(self, points=None):
        print('setTempGeometry',points)
        self.mtool.stopCapture.disconnect(self.setTempGeometry)
        qgis.utils.iface.actionPan().trigger()
        # iface.mapCanvas().setMapTool(mtool)
        # self.canvas.unsetMapTool(self.mtool)



if False:
    if True:
        qgis_path = "C://OSGeo4W64//apps//qgis"
    else:
        qgis_path = "C://OSGeo4W64//apps//qgis-dev"

    app = qgis.core.QgsApplication([], True)
    qgis.core.QgsApplication.setPrefixPath(qgis_path, True)
    qgis.core.QgsApplication.initQgis()

    print(qgis.utils.iface)

    if qgis.utils.iface is None:
        canvas = qgis.gui.QgsMapCanvas()
        canvas.enableAntiAliasing(True)
    else:
        canvas = qgis.utils.iface.mapCanvas()
    tempclass = Test(canvas)
    tempclass.widget.show()


    #widget.show()
    #testMaptool(canvas)
    #testCoreParserValuePG(canvas,True)


    app.exec_()
    qgis.core.QgsApplication.exitQgis()
    print('ok')

if True:
    canvas = qgis.utils.iface.mapCanvas()
    tempclass = Test(canvas,False)
    tempclass.widget.show()
