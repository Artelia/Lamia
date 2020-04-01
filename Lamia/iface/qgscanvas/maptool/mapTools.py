"""
This file is part of LAMIA.

    LAMIA is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    LAMIA is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Foobar.  If not, see <https://www.gnu.org/licenses/>.

"""
"""
  * Copyright (c) 2017-2020 ARTELIA Commit <lamia@arteliagroup.com>
  * 
  * SPDX-License-Identifier: GPL-3.0-or-later
  * License-Filename: LICENSING.md
 """


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
import qgis
import qgis.utils
qgis.utils.uninstallErrorHook()     #for standart output

"""
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

import math
import qgis
import qgis.utils
"""


class mapToolEdit(qgis.gui.QgsMapToolEdit):

    def __init__(self, canvas=None, layer=None, onTrackEdited=None):
        qgis.gui.QgsMapToolEdit.__init__(self, canvas)
        self.onTrackEdited = onTrackEdited
        self.dragging      = False
        self.feature       = None
        self.vertex        = None
        #self.setLayer(layer)
        self.setCursor(QtCore.Qt.CrossCursor)






class mapToolCapture(qgis.gui.QgsMapToolCapture):
    stopCapture = QtCore.pyqtSignal(list)

    # def __init__(self, canvas, dockwdget, mode,layer):
    def __init__(self, canvas, dockwdget, mode):
        qgis.gui.QgsMapToolCapture.__init__(self, canvas, dockwdget, mode)
        self.canvas = canvas
        # self.layer = layer
        # self.mappoints = []
        self.mappoints = []

        try:
            self.qgisversion_int = qgis.utils.QGis.QGIS_VERSION_INT
        except AttributeError:  #qgis 3
            self.qgisversion_int = qgis.utils.Qgis.QGIS_VERSION_INT


    def canvasReleaseEvent(self, event):
        # print(self.mappoints)
        if event.button() == QtCore.Qt.LeftButton:
            """
            if not self.isCapturing():
                self.startCapturing()
            """

            # mapPt,layerPt = self.transformCoordinates(event.pos())

            if int(str(self.qgisversion_int)[0:3]) < 220:
                mapPt = event.snapPoint(qgis.gui.QgsMapMouseEvent.SnapProjectConfig)
            else:
                mapPt = event.snapPoint()

            self.addVertex(mapPt)
            self.mappoints.append(mapPt)
            # print(self.points(), mapPt)

            if int(str(self.qgisversion_int)[0:3]) < 220:
                capturemodepoint = qgis.gui.QgsMapToolAdvancedDigitizing.CapturePoint
            else:
                capturemodepoint = qgis.gui.QgsMapToolCapture.CapturePoint

            if self.mode() == capturemodepoint:
                # if len(self.points()) > 0:
                if len(self.mappoints) > 0:
                    if qgis.utils.iface is not None:  #run from within qgis
                        self.stopCapture.emit(self.mappoints)
                        # self.stopCapture.emit(self.points())
                    else:       # run from pycharm
                        self.stopCapture.emit(self.mappoints)
                    self.stopCapturing()
                    self.mappoints = []

        elif event.button() == QtCore.Qt.RightButton:
            if qgis.utils.iface is not None:  # run from within qgis
                self.stopCapture.emit(self.mappoints)
                #self.stopCapture.emit(self.points())
            else:  # run from pycharm
                self.stopCapture.emit(self.mappoints)
            self.stopCapturing()
            self.mappoints = []

    if False:
        def transformCoordinates(self, canvasPt):
            return (self.toMapCoordinates(canvasPt),
                    self.toLayerCoordinates(self.layer, canvasPt))


class mapToolCapture2(qgis.gui.QgsMapToolCapture):

    stopCapture = QtCore.pyqtSignal(list)

    def __init__(self, canvas, dockwdget, mode,layer):
        qgis.gui.QgsMapToolCapture.__init__(self, canvas, dockwdget, mode)
        self.canvas = canvas
        self.layer = layer
        self.mappoints = []
        
    
    def canvasReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            if not self.isCapturing():
                self.startCapturing()
            
            mapPt,layerPt = self.transformCoordinates(event.pos())
            mapPt = event.snapPoint(qgis.gui.QgsMapMouseEvent.SnapProjectConfig )
            self.addVertex(mapPt)
            self.mappoints.append(mapPt)
            
            if self.mode() ==  qgis.gui.QgsMapToolAdvancedDigitizing.CapturePoint:
                self.stopCapturing()
                if len(self.mappoints)>0:
                    self.stopCapture.emit(self.mappoints)
                    self.mappoints = []
            
        elif event.button() == QtCore.Qt.RightButton:
            self.stopCapturing()
            self.stopCapture.emit(self.mappoints)
                

    def transformCoordinates(self, canvasPt):
        return (self.toMapCoordinates(canvasPt),
                self.toLayerCoordinates(self.layer, canvasPt))
                

