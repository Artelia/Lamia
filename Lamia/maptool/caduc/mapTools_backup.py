# -*- coding: utf-8 -*-
# -----------------------------------------------------------
#
# Qgep
# Copyright (C) 2014  Matthias Kuhn
# -----------------------------------------------------------
#
# licensed under the terms of GNU GPL 2
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, print to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# ---------------------------------------------------------------------

"""
Some map tools for digitizing features
"""

from qgis.PyQt import uic, QtCore, QtGui

from qgis.gui import (
    QgsMapToolAdvancedDigitizing,
    QgsMapTool,
    QgsRubberBand,
    QgsMessageBar,
    QgsMapToolCapture,
    QgsMapMouseEvent
)
from qgis.core import (
    QgsFeature,
    QgsPoint,
    QgsSnapper,
    QgsTolerance,
    QgsFeatureRequest,
    QGis,
    QgsGeometry
)
from PyQt4.QtGui import (
    QCursor,
    QColor,
    QApplication,
    QDialog,
    QGridLayout,
    QLabel,
    QLineEdit,
    QDialogButtonBox
)
from PyQt4.QtCore import (
    Qt,
    pyqtSignal
)
#from qgepplugin.utils.qgeplayermanager import QgepLayerManager
import math
import qgis
import qgis.utils
#import qgis.utils.iface
#class QgepMapToolAddFeature(QgsMapToolAdvancedDigitizing):




class mapToolCapture(QgsMapToolCapture):

    stopCapture = QtCore.pyqtSignal(list)

    def __init__(self, canvas, dockwdget, mode,layer):
        QgsMapToolCapture.__init__(self, canvas, dockwdget, mode)
        self.canvas          = canvas
        self.layer           = layer
        self.mappoints = []
        
    
    def canvasReleaseEvent(self, event):
        #print('canvasReleaseEvent')
        if event.button() == Qt.LeftButton:
            #print('capt',self.isCapturing(),self.capturing)
            #if not self.capturing:
            if not self.isCapturing():
                self.startCapturing()
            #self.addVertex(event.pos())
            
            mapPt,layerPt = self.transformCoordinates(event.pos())
            mapPt = event.snapPoint(QgsMapMouseEvent.SnapProjectConfig )
            self.addVertex(mapPt)
            self.mappoints.append(mapPt)
            
            if self.mode() ==  qgis.gui.QgsMapToolAdvancedDigitizing.CapturePoint :
                #points = self.getCapturedGeometry()
                self.stopCapturing()
                #if points != None:
                if len(self.mappoints)>0:
                    
                    #self.stopCapture.emit(points)
                    self.stopCapture.emit(self.mappoints)
                    self.mappoints = []
            
        elif event.button() == Qt.RightButton:
            #points = self.getCapturedGeometry()
            self.stopCapturing()
            #self.stopCapture.emit(points)
            self.stopCapture.emit(self.mappoints)
            """
            if points != None:
                pass
                #self.geometryCaptured(points)
            """
                

    def transformCoordinates(self, canvasPt):
        return (self.toMapCoordinates(canvasPt),
                self.toLayerCoordinates(self.layer, canvasPt))
                
    """
    def getCapturedGeometry(self):
        points = self.points()
        return points
    """

    """
    def geometryCaptured(self, layerCoords):

        if self.captureMode == mapToolCapture.CAPTURE_LINE:
            geometry = QgsGeometry.fromPolyline(layerCoords)
        elif self.captureMode == mapToolCapture.CAPTURE_POLYGON:
            geometry = QgsGeometry.fromPolygon([layerCoords])
        feature = QgsFeature()
        feature.setGeometry(geometry)
        self.layer.addFeature(feature)
        self.layer.updateExtents()
        self.onGeometryAdded()
        
        
    def geometryCaptured2(self, layerCoords):

        if self.captureMode == mapToolCapture.CAPTURE_LINE:
            geometry = QgsGeometry.fromPolyline(layerCoords)
        elif self.captureMode == mapToolCapture.CAPTURE_POLYGON:
            geometry = QgsGeometry.fromPolygon([layerCoords])
        feature = QgsFeature()
        feature.setGeometry(geometry)
        self.layer.addFeature(feature)
        self.layer.updateExtents()
        self.onGeometryAdded()
    """


class mapToolCapture2(QgsMapToolCapture):

    CAPTURE_LINE    = 1
    CAPTURE_POLYGON = 2

    def __init__(self, canvas, dockwdget, mode,layer):
        QgsMapToolCapture.__init__(self, canvas, dockwdget, mode)
        self.canvas          = canvas
        self.layer           = layer
        self.mappoints = []
        
        #self.onGeometryAdded = onGeometryAdded
        #self.captureMode     = captureMode
        #self.rubberBand      = None
        #self.tempRubberBand  = None
        #self.capturedPoints  = []
        #self.capturing       = False
        
        #self.setCursor(Qt.CrossCursor)
        
    """
    def cadCanvasMoveEvent (self, event):
    
        if self.tempRubberBand != None and self.capturing:
            mapPt,layerPt = self.transformCoordinates(event.pos())
            self.tempRubberBand.movePoint(mapPt)
    """
            
        
    
    def canvasReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            #print('capt',self.isCapturing(),self.capturing)
            #if not self.capturing:
            if not self.isCapturing():
                self.startCapturing()
            #self.addVertex(event.pos())
            
            mapPt,layerPt = self.transformCoordinates(event.pos())
            print(mapPt,layerPt)
            layerPt = event.snapPoint(QgsMapMouseEvent.SnapProjectConfig )
            self.addVertex(layerPt)
            #self.mappoints.append(
            
        elif event.button() == Qt.RightButton:
            points = self.getCapturedGeometry()
            print('test',points)
            self.stopCapturing()
            if points != None:
                pass
                #self.geometryCaptured(points)
                

    def transformCoordinates(self, canvasPt):

        return (self.toMapCoordinates(canvasPt),
                self.toLayerCoordinates(self.layer, canvasPt))
                
                
    def getCapturedGeometry(self):
        #points = self.capturedPoints
        points = self.points ()
        #print(points)
        return points
        """
        if self.captureMode == mapToolCapture.CAPTURE_LINE:
            if len(points) < 2:
                return None
        if self.captureMode == mapToolCapture.CAPTURE_POLYGON:
            if len(points) < 3:
                return None
        if self.captureMode == mapToolCapture.CAPTURE_POLYGON:
            points.append(points[0]) # Close polygon.
        return points
        """
    
    
    
    
    """
    def startCapturing(self):

        color = QColor("red")
        color.setAlphaF(0.78)
        self.rubberBand = QgsRubberBand(self.canvas,
                                        self.bandType())
        self.rubberBand.setWidth(2)
        self.rubberBand.setColor(color)
        self.rubberBand.show()

        self.tempRubberBand = QgsRubberBand(self.canvas,
                                            self.bandType())
        self.tempRubberBand.setWidth(2)
        self.tempRubberBand.setColor(color)
        self.tempRubberBand.setLineStyle(Qt.DotLine)
        self.tempRubberBand.show()
        self.capturing = True
    """
        
    """

    def bandType(self):
        if self.captureMode == CaptureTool.CAPTURE_POLYGON:
            return QGis.Polygon
        else:
            return QGis.Line
            
    def stopCapturing(self):
        if self.rubberBand:
            self.canvas.scene().removeItem(self.rubberBand)
            self.rubberBand = None
        if self.tempRubberBand:
            self.canvas.scene().removeItem(self.tempRubberBand)
            self.tempRubberBand = None
        self.capturing = False
        self.capturedPoints = []
        self.canvas.refresh()
        
    def addVertex(self, canvasPoint):

        mapPt,layerPt = self.transformCoordinates(canvasPoint)
        self.rubberBand.addPoint(mapPt)
        self.capturedPoints.append(layerPt)
        self.tempRubberBand.reset(self.bandType())
        if self.captureMode == mapToolCapture.CAPTURE_LINE:
            self.tempRubberBand.addPoint(mapPt)

        elif self.captureMode == mapToolCapture.CAPTURE_POLYGON:
            firstPoint = self.rubberBand.getPoint(0, 0)
            self.tempRubberBand.addPoint(firstPoint)
            self.tempRubberBand.movePoint(mapPt)
            self.tempRubberBand.addPoint(mapPt)

            
    def getCapturedGeometry(self):
        points = self.capturedPoints
        if self.captureMode == mapToolCapture.CAPTURE_LINE:
            if len(points) < 2:
                return None
        if self.captureMode == mapToolCapture.CAPTURE_POLYGON:
            if len(points) < 3:
                return None
        if self.captureMode == mapToolCapture.CAPTURE_POLYGON:
            points.append(points[0]) # Close polygon.
        return points
            
    
    def geometryCaptured(self, layerCoords):

        if self.captureMode == mapToolCapture.CAPTURE_LINE:
            geometry = QgsGeometry.fromPolyline(layerCoords)
        elif self.captureMode == mapToolCapture.CAPTURE_POLYGON:
            geometry = QgsGeometry.fromPolygon([layerCoords])
        feature = QgsFeature()
        feature.setGeometry(geometry)
        self.layer.addFeature(feature)
        self.layer.updateExtents()
        self.onGeometryAdded()
            
    """


class mapToolAddFeature(QgsMapToolAdvancedDigitizing):
    """
    Base class for adding features
    """
    def __init__(self, iface, layer):
        QgsMapToolAdvancedDigitizing.__init__(self, iface.mapCanvas(), iface.cadDockWidget())
        self.iface = iface
        self.canvas = iface.mapCanvas()
        self.layer = layer
        self.rubberband = QgsRubberBand(iface.mapCanvas(), layer.geometryType())
        self.rubberband.setColor(QColor("#ee5555"))
        self.rubberband.setWidth(1)
        self.tempRubberband = QgsRubberBand(iface.mapCanvas(), layer.geometryType())
        self.tempRubberband.setColor(QColor("#ee5555"))
        self.tempRubberband.setWidth(1)
        self.tempRubberband.setLineStyle(Qt.DotLine)

    def activate(self):
        """
        When activating the map tool
        """
        QgsMapToolAdvancedDigitizing.activate(self)
        self.canvas.setCursor(QCursor(Qt.CrossCursor))

    def deactivate(self):
        """
        On deactivating the map tool
        """
        QgsMapToolAdvancedDigitizing.deactivate(self)
        self.canvas.unsetCursor()

    # pylint: disable=no-self-use
    def isZoomTool(self):
        """
        This is no zoom tool
        """
        return False

    # ===========================================================================
    # Events
    # ===========================================================================

    def cadCanvasReleaseEvent(self, event):
        """
        Called when a mouse button is
        :param event:
        :return:
        """
        print('release')
        if event.button() == Qt.RightButton:
            self.rightClicked(event)
        else:
            self.leftClicked(event)

    def leftClicked(self, event):
        """
        When the canvas is left clicked we add a new point to the rubberband.
        :type event: QMouseEvent
        """
        mousepos = self.canvas.getCoordinateTransform()\
            .toMapCoordinates(event.pos().x(), event.pos().y())
        print('mousepos',mousepos)
        self.rubberband.addPoint(mousepos)
        self.tempRubberband.reset()

    def rightClicked(self, _):
        """
        On a right click we create a new feature from the existing rubberband and show the add
        dialog
        """
        print('geom',self.rubberband.asGeometry())
        if False:
            f = QgsFeature(self.layer.pendingFields())
            f.setGeometry(self.rubberband.asGeometry())
            dlg = self.iface.getFeatureForm(self.layer, f)
            dlg.setIsAddDialog(True)
            dlg.exec_()
        self.rubberband.reset()
        self.tempRubberband.reset()

    def cadCanvasMoveEvent(self, event):
        """
        When the mouse is moved the rubberband needs to be updated
        :param event: The coordinates etc.
        """

        # When a generated event arrives it's a QMoveEvent... No idea why, but this prevents from an exception
        try:
            QgsMapToolAdvancedDigitizing.cadCanvasMoveEvent(self, event)
            mousepos = event.mapPoint()
            self.tempRubberband.movePoint(mousepos)
        except TypeError:
            pass



#class QgepMapToolAddReach(mapToolAddFeature):
class mapToolAddLine(mapToolAddFeature):
    """
    Create a new reach with the mouse.
    Will snap to wastewater nodes for the first and last point and auto-connect
    these.
    """
    currentSnappingResult = None
    firstSnappingResult = None
    lastSnappingResult = None

    def __init__(self, iface, layer):
        mapToolAddFeature.__init__(self, iface, layer)
        #self.nodeLayer = QgepLayerManager.layer('vw_wastewater_node')
        self.nodeLayer = layer
        assert self.nodeLayer
        #self.reachLayer = QgepLayerManager.layer('vw_qgep_reach')
        self.reachLayer = layer
        assert self.reachLayer
        self.setMode(QgsMapToolAdvancedDigitizing.CaptureLine)

    def leftClicked(self, event):
        """
        The mouse is clicked: snap to neary points which are on the wastewater node layer
        and update the rubberband
        :param event: The coordinates etc.
        """
        self.snap(event.pos())
        if self.rubberband.numberOfVertices() == 0:
            self.firstSnappingResult = self.currentSnappingResult
        self.lastSnappingResult = self.currentSnappingResult
        if self.currentSnappingResult:
            pt = self.currentSnappingResult.snappedVertex
        else:
            pt = event.mapPoint()
        self.rubberband.addPoint(pt)
        self.tempRubberband.reset()
        self.tempRubberband.addPoint(pt)

    def snap(self, pos):
        """
        Snap to nearby points on the wastewater node layer which may be used as connection
        points for this reach.
        :param pos: The position to snap
        :return: The snapped position
        """
        snapper = QgsSnapper(self.iface.mapCanvas().mapSettings())
        snap_nodelayer = QgsSnapper.SnapLayer()
        snap_nodelayer.mLayer = self.nodeLayer
        snap_nodelayer.mTolerance = 20
        snap_nodelayer.mUnitType = QgsTolerance.Pixels
        snap_nodelayer.mSnapTo = QgsSnapper.SnapToVertex
        snapper.setSnapLayers([snap_nodelayer])
        (_, snappedPoints) = snapper.snapPoint(pos)
        if snappedPoints:
            self.currentSnappingResult = snappedPoints[0]
            return self.currentSnappingResult.snappedVertex
        else:
            snapper = QgsSnapper(self.iface.mapCanvas().mapSettings())
            snap_reachlayer = QgsSnapper.SnapLayer()
            snap_reachlayer.mLayer = self.reachLayer
            snap_reachlayer.mTolerance = 10
            snap_reachlayer.mUnitType = QgsTolerance.Pixels
            snap_reachlayer.mSnapTo = QgsSnapper.SnapToVertexAndSegment
            snapper.setSnapLayers([snap_reachlayer])
            (_, snappedPoints) = snapper.snapPoint(pos)
            if snappedPoints:
                self.currentSnappingResult = snappedPoints[0]
                return self.currentSnappingResult.snappedVertex
            else:
                self.currentSnappingResult = None
                return pos

    def rightClicked(self, _):
        """
        The party is over, the reach digitized. Create a feature from the rubberband and
        show the feature form.
        """
        self.tempRubberband.reset()

        f = QgsFeature(self.layer.pendingFields())
        f.setGeometry(self.rubberband.asGeometry())

        if self.firstSnappingResult is not None:
            req = QgsFeatureRequest(self.firstSnappingResult.snappedAtGeometry)
            from_networkelement = self.firstSnappingResult.layer.getFeatures(req).next()
            from_field = self.layer.pendingFields()\
                .indexFromName('rp_from_fk_wastewater_networkelement')
            f.setAttribute(from_field, from_networkelement.attribute('obj_id'))
            from_level_field = self.layer.pendingFields()\
                .indexFromName('rp_from_level')
            try:
                # bottom_level is only available for a node (and not for a
                # reach)
                from_level = from_networkelement['bottom_level']
                f.setAttribute(from_level_field, from_level)
            except:
                pass
        
        if self.lastSnappingResult is not None:
            req = QgsFeatureRequest(self.lastSnappingResult.snappedAtGeometry)
            to_networkelement = self.lastSnappingResult.layer.getFeatures(req).next()
            to_field = self.layer.pendingFields().indexFromName('rp_to_fk_wastewater_networkelement')
            f.setAttribute(to_field, to_networkelement.attribute('obj_id'))
            to_level_field = self.layer.pendingFields()\
                .indexFromName('rp_to_level')
            try:
                # bottom_level is only available for a node (and not for a
                # reach)
                to_level = to_networkelement['bottom_level']
                f.setAttribute(to_level_field, to_level)
            except:
                pass
        if False:
            dlg = self.iface.getFeatureForm(self.layer, f)
            dlg.setIsAddDialog(True)
            dlg.exec_()
        self.rubberband.reset()


class QgepMapToolDigitizeDrainageChannel(QgsMapTool):
    '''
    This is used to digitize a drainage channel.

    It lets you digitize two points and then creates a polygon based on these two points
    by adding an orthogonal offset at each side.

    Input:

       x==============x

    Output:

       ----------------
       |              |
       ----------------

    Usage:
      Connect to the signals deactivated() and geometryDigitized()
      If geometryDigitized() is called you can use the member variable geometry
      which will contain a rectangle polygon
      deactivated() will be emited after a right click
    '''

    geometryDigitized = pyqtSignal()

    def __init__(self, iface, layer):
        QgsMapTool.__init__(self, iface.mapCanvas())
        self.iface = iface
        self.canvas = iface.mapCanvas()
        self.layer = layer
        self.rubberband = QgsRubberBand(iface.mapCanvas(), QGis.Line)
        self.rubberband.setColor(QColor("#ee5555"))
        self.rubberband.setWidth(2)
        self.firstPoint = None
        self.messageBarItem = None
        self.geometry = None

    def activate(self):
        """
        Map tool is activated
        """
        QgsMapTool.activate(self)
        self.canvas.setCursor(QCursor(Qt.CrossCursor))
        msgtitle = self.tr('Digitizing Drainage Channel')
        msg = self.tr('Digitize start and end point. Rightclick to abort.')
        self.messageBarItem = QgsMessageBar.createMessage(msgtitle,
                                                          msg)
        self.iface.messageBar().pushItem(self.messageBarItem)

    def deactivate(self):
        """
        Map tool is deactivated
        """
        QgsMapTool.deactivate(self)
        self.iface.messageBar().popWidget(self.messageBarItem)
        try:
            self.iface.mapCanvas().scene().removeItem(self.rubberband)
            del self.rubberband
        except AttributeError:
            # Called repeatedly... bail out
            pass
        self.canvas.unsetCursor()

    def canvasMoveEvent(self, event):
        """
        Mouse is moved: Update rubberband
        :param event: coordinates etc.
        """
        mousepos = event.mapPoint()
        self.rubberband.movePoint(mousepos)

    def canvasReleaseEvent(self, event):
        """
        Canvas is released. This means:
          * start digitizing
          * stop digitizing (create a rectangle
            * if the Ctrl-modifier is pressed, ask for the rectangle width
        :param event: coordinates etc.
        """
        if event.button() == Qt.RightButton:
            self.deactivate()
        else:
            mousepos = self.canvas.getCoordinateTransform()\
                .toMapCoordinates(event.pos().x(), event.pos().y())
            self.rubberband.addPoint(mousepos)
            if self.firstPoint:  # If the first point was set before, we are doing the second one
                lp1 = self.rubberband.asGeometry().asPolyline()[0]
                lp2 = self.rubberband.asGeometry().asPolyline()[1]
                width = 0.2
                if QApplication.keyboardModifiers() & Qt.ControlModifier:
                    dlg = QDialog()
                    dlg.setLayout(QGridLayout())
                    dlg.layout().addWidget(QLabel(self.tr('Enter width')))
                    txt = QLineEdit('0.2')
                    dlg.layout().addWidget(txt)
                    bb = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
                    dlg.layout().addWidget(bb)
                    bb.accepted.connect(dlg.accept)
                    bb.rejected.connect(dlg.reject)
                    if dlg.exec_():
                        try:
                            width = float(txt.text())
                        except ValueError:
                            width = 0.2

                length = math.sqrt(math.pow(lp1.x() - lp2.x(), 2) + math.pow(lp1.y() - lp2.y(), 2))
                xd = lp2.x() - lp1.x()
                yd = lp2.y() - lp1.y()

                pt1 = QgsPoint(lp1.x() + width * (yd / length), lp1.y() - width * (xd / length))
                pt2 = QgsPoint(lp1.x() - width * (yd / length), lp1.y() + width * (xd / length))
                pt3 = QgsPoint(lp2.x() - width * (yd / length), lp2.y() + width * (xd / length))
                pt4 = QgsPoint(lp2.x() + width * (yd / length), lp2.y() - width * (xd / length))

                self.geometry = QgsGeometry.fromPolygon([[pt1, pt2, pt3, pt4, pt1]])

                self.geometryDigitized.emit()

            self.firstPoint = mousepos
            
            
            
