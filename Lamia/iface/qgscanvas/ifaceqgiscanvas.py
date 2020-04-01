# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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
import os, sys, io
import qgis, qgis.core, qgis.utils, qgis.gui

import Lamia
from ..ifaceabstractcanvas import LamiaAbstractIFaceCanvas
from .maptool.mapTools import mapToolCapture, mapToolEdit

class QgisCanvas(LamiaAbstractIFaceCanvas):

    def __init__(self, canvas=None):
        LamiaAbstractIFaceCanvas.__init__(self)
        self.canvas = canvas
        if canvas is None and qgis.utils.iface is not None:
            self.setCanvas(qgis.utils.iface.mapCanvas())
        
        self.dbaseqgiscrs = None
        self.layers = {}
        self.mtoolpoint = None
        self.mtoolline = None
        self.mtoolpolygon = None

    def setCanvas(self,qgscanvas):
        self.canvas = qgscanvas

        #init maptools
        self.cadwdg = qgis.gui.QgsAdvancedDigitizingDockWidget(self.canvas)
        self.mtoolpoint = mapToolCapture(self.canvas, self.cadwdg,
                                qgis.gui.QgsMapToolCapture.CapturePoint)
        self.mtoolline = mapToolCapture(self.canvas, self.cadwdg,
                                        qgis.gui.QgsMapToolCapture.CaptureLine)
        self.mtoolpolygon = mapToolCapture(self.canvas, self.cadwdg,
                                        qgis.gui.QgsMapToolCapture.CapturePolygon)


    def createLayers(self, dbaseparser):

        if dbaseparser.__class__.__name__ == 'SpatialiteDBaseParser':
            dbtype = 'spatialite'
        elif dbaseparser.__class__.__name__ == 'PostGisDBaseParser':
            dbtype = 'postgres'
        
        for rawtablename in dbaseparser.dbasetables:
            tablenames = [rawtablename, rawtablename + '_qgis', rawtablename + '_django']
            tabletypes = ['layer', 'layerqgis', 'layerdjango']
            for i, tablename in enumerate(tablenames):
                tablenamelower = tablename.lower()
                tabletype = tabletypes[i]
                self.layers[tablename] = {}
                #rawlayers
                uri = qgis.core.QgsDataSourceUri()
                if dbtype == 'spatialite':
                    uri.setDatabase(dbaseparser.spatialitefile)
                    if dbaseparser.isTableSpatial(tablename):
                        uri.setDataSource('', str(tablename), 'geom')
                    else:
                        uri.setDataSource('', str(tablename), '')
                elif dbtype == 'postgres':
                    uri.setConnection(dbaseparser.pghost, str(dbaseparser.pgport), 
                                        dbaseparser.pgdb, dbaseparser.pguser, dbaseparser.pgpassword)
                    if dbaseparser.isTableSpatial(tablenamelower):
                        uri.setDataSource(dbaseparser.pgschema, str(tablenamelower), 'geom', '', "pk_" + str(tablenamelower))
                    else:
                        uri.setDataSource(dbaseparser.pgschema, str(tablenamelower), None, '', "'pk_" + str(tablenamelower))
                self.layers[tablename][tabletype] = qgis.core.QgsVectorLayer(uri.uri(), tablename, dbtype)

        self.dbaseqgiscrs = qgis.core.QgsCoordinateReferenceSystem()
        self.dbaseqgiscrs.createFromString('EPSG:' + str(dbaseparser.crsnumber))
        self.updateQgsCoordinateTransform()

    def loadLayersInCanvas(self, dbaseparser):
        if qgis.utils.iface is not None:
            #create node in legend
            root = qgis.core.QgsProject.instance().layerTreeRoot()
            groupname = 'Lamia_' + dbaseparser.getDBName().lower()
            lamialegendgroup = root.findGroup(groupname)
            if lamialegendgroup is None:
                lamialegendgroup = root.insertGroup(0, groupname)
            self.qgislegendnode = lamialegendgroup


            for tablename in self.dbase.dbasetables:
                qgis.core.QgsProject.instance().addMapLayer(self.dbase.dbasetables[tablename]['layerqgis'], False)
                lamialegendgroup.addLayer(self.dbase.dbasetables[tablename]['layerqgis'])

        else:
            layerstoadd = []
            dbasetables = self.layers
            goodtablekey = [val for val in dbasetables.keys() if 'layerqgis' in dbasetables[val].keys()  ]
            for tablename in goodtablekey:
                layerstoadd.append(dbasetables[tablename]['layerqgis'])
            self.canvas.setLayers(layerstoadd)
            self.canvas.setExtent(dbasetables['Infralineaire']['layer'].extent())
            self.canvas.refresh()


    def applyStyle(self, worktype, styledir):
        styledirectory = os.path.join(os.path.dirname(Lamia.__file__), 'DBASE', 'style', worktype, styledir )
        allfiles = [x[2] for x in os.walk(styledirectory)][0]
        qmlfiles = [uknfile.split('.')[0] for uknfile in allfiles if uknfile.split('.')[1] == 'qml']
        for tablename in self.layers.keys():
            if 'layerqgis' in self.layers[tablename].keys() :
                #apply style
                stylepath = os.path.join(styledirectory, tablename + '.qml')
                self.layers[tablename]['layerqgis'].loadNamedStyle(stylepath)
                #setvisibility
                ltl = qgis.core.QgsProject.instance().layerTreeRoot().findLayer(self.layers[tablename]['layerqgis'].id())
                if tablename in qmlfiles:
                    if ltl:
                        ltl.setItemVisibilityChecked(True)
                else:
                    if ltl:
                        ltl.setItemVisibilityChecked(False)

        self.canvas.refreshAllLayers()
        self.canvas.refresh()

    def updateQgsCoordinateTransform(self):
        """
        Methode appellée lorsque le crs du canvas qgis change
        met à jour self.xform et self.xformreverse pour effectuer les transformations crs canvas <-> crs lamia
        """

        if self.dbaseqgiscrs is not None and self.canvas is not None:
            self.xform = qgis.core.QgsCoordinateTransform(self.dbaseqgiscrs,
                                                            self.canvas.mapSettings().destinationCrs(),
                                                            qgis.core.QgsProject.instance() )
            self.xformreverse = qgis.core.QgsCoordinateTransform(self.canvas.mapSettings().destinationCrs(),
                                                                    self.dbaseqgiscrs,
                                                                qgis.core.QgsProject.instance() )
