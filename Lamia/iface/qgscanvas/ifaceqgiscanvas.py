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
import os, sys, io, logging, datetime
import qgis, qgis.core, qgis.utils, qgis.gui
from qgis.PyQt import QtGui
import Lamia
from ..ifaceabstractcanvas import LamiaAbstractIFaceCanvas
from .maptool.mapTools import mapToolCapture, mapToolEdit

class QgisCanvas(LamiaAbstractIFaceCanvas):

    def __init__(self, canvas=None):
        LamiaAbstractIFaceCanvas.__init__(self)
        self.canvas = canvas
        self.mtoolpoint = None
        self.mtoolline = None
        self.mtoolpolygon = None
        self.rubberBand = None
        if canvas is None and qgis.utils.iface is not None:
            self.setCanvas(qgis.utils.iface.mapCanvas())
        
        self.dbaseqgiscrs = None
        self.layers = {}



        #behaviour
        self.editingrawlayer = False
        self.currentmaptool = None  #the maptool in use

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

        self.pointEmitter = qgis.gui.QgsMapToolEmitPoint(self.canvas)

    def _____________________________layersManagement(self):
        pass

    def createLayers(self, dbaseparser):

        if dbaseparser.__class__.__name__ == 'SpatialiteDBaseParser':
            dbtype = 'spatialite'
        elif dbaseparser.__class__.__name__ == 'PostGisDBaseParser':
            dbtype = 'postgres'
        
        for rawtablename in dbaseparser.dbasetables:
            tablenames = [rawtablename, rawtablename + '_qgis', rawtablename + '_django']
            tabletypes = ['layer', 'layerqgis', 'layerdjango']
            self.layers[rawtablename] = {}
            for i, tablename in enumerate(tablenames):
                tablenamelower = tablename.lower()
                tabletype = tabletypes[i]
                
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
                self.layers[rawtablename][tabletype] = qgis.core.QgsVectorLayer(uri.uri(), tablename, dbtype)

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

            dbasetables = self.layers
            for tablename in dbasetables:
                qgis.core.QgsProject.instance().addMapLayer(dbasetables[tablename]['layerqgis'], False)
                lamialegendgroup.addLayer(dbasetables[tablename]['layerqgis'])

        else:
            layerstoadd = []
            dbasetables = self.layers
            goodtablekey = [val for val in dbasetables.keys() if 'layerqgis' in dbasetables[val].keys()  ]
            for tablename in goodtablekey:
                layerstoadd.append(dbasetables[tablename]['layerqgis'])
            self.canvas.setLayers(layerstoadd)
            self.canvas.setExtent(dbasetables['Infralineaire']['layer'].extent())
            self.canvas.refresh()


    def unloadLayersInCanvas(self):
        if self.qgislegendnode is not None:
            self.qgislegendnode.removeAllChildren()
            root = qgis.core.QgsProject.instance().layerTreeRoot()
            root.removeChildNode(self.qgislegendnode)


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

    def addRawLayerInCanvasForEditing(self, layername):

        if self.editingrawlayer == True :
                return


        self.editingrawlayer = False

        """
        if True:
            if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                qgis.core.QgsMapLayerRegistry.instance().addMapLayer(self.dbase.dbasetables[tablename]['layerqgis'],
                                                                    False)
            else:
                qgis.core.QgsProject.instance().addMapLayer(self.dbase.dbasetables[tablename]['layerqgis'],
                                                            False)
        lamialegendgroup.addLayer(self.dbase.dbasetables[tablename]['layerqgis'])
        """
        self.editlayer = qgis.core.QgsVectorLayer(self.layers[layername]['layer'].source(),
                                                self.layers[layername]['layer'].name() + '_edit',
                                                self.layers[layername]['layer'].providerType())
        qgis.core.QgsProject.instance().addMapLayer(self.editlayer, False)
        self.editfeaturetreelayer = self.qgislegendnode.insertLayer(0,self.editlayer)
        if qgis.utils.iface is not None :
            self.dbase.qgsiface.setActiveLayer(self.editlayer)
            self.editlayer.startEditing()
            self.dbase.qgsiface.actionVertexTool().trigger()

        self.editingrawlayer = True
        
        
        """
        if self.stackedWidget_main.currentIndex() == 0:
            wdg = self.MaintabWidget.widget(0).layout().itemAt(0).widget()

            self.editfeaturelayer = qgis.core.QgsVectorLayer(wdg.dbasetable['layer'].source(),
                                                            wdg.dbasetable['layer'].name() + '_edit',
                                                            wdg.dbasetable['layer'].providerType())

            if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                qgis.core.QgsMapLayerRegistry.instance().addMapLayer(self.editfeaturelayer,False)
                self.editfeaturetreelayer = self.qgislegendnode.insertLayer(0,self.editfeaturelayer)
                if self.dbase.qgsiface is not None :
                    self.dbase.qgsiface.setActiveLayer(self.editfeaturelayer)
                    self.editfeaturelayer.startEditing()
                    self.dbase.qgsiface.actionNodeTool().trigger()
            else:
                qgis.core.QgsProject.instance().addMapLayer(self.editfeaturelayer, False)
                self.editfeaturetreelayer = self.qgislegendnode.insertLayer(0,self.editfeaturelayer)
                if self.dbase.qgsiface is not None :
                    self.dbase.qgsiface.setActiveLayer(self.editfeaturelayer)
                    self.editfeaturelayer.startEditing()
                    self.dbase.qgsiface.actionVertexTool().trigger()

            self.editingrawlayer = True
        """

    def closeRawLayerEditing(self, maintreewdgindex=None, savechanges=False):

        if self.editingrawlayer:
            self.editingrawlayer = False
            if isinstance(savechanges,bool) and savechanges:
                self.editlayer.commitChanges()
            else:
                self.editlayer.rollBack()
            self.qgislegendnode.removeLayer(self.editlayer)

    def updateWorkingDate(self, dbaseparser, datetimearg=None, revision=None):
        """
        Methode appelée lorsque la date de travail (self.workingdate) ou la version de travail (self.currentrevision)
        est modifiée
        Change les filtres de toutes les tables qgis en fonction
        """

        #workingdatemodif = QtCore.QDate.fromString(self.workingdate, 'yyyy-MM-dd').addDays(1).toString('yyyy-MM-dd')
        if datetimearg:
            workingdatemodif = datetimearg
        else:
            workingdatemodif = dbaseparser.workingdate
        if revision:
            revision = revision
        else:
            revision = dbaseparser.currentrevision
        if dbaseparser.__class__.__name__ == 'SpatialiteDBaseParser':
            parsertruevalue = '1'
        elif dbaseparser.__class__.__name__ == 'PostGisDBaseParser':
            parsertruevalue = 'TRUE'

        subsetstringtemp = """  "datetimecreation" <= '{workingdate}' """\
                           """ AND CASE WHEN "datetimedestruction" IS NOT NULL  THEN "datetimedestruction" > '{workingdate}' ELSE {truevalue} END """\
                           """ AND "lpk_revision_begin" <= '{currentrevision}' """\
                           """ AND CASE WHEN "lpk_revision_end" IS NOT NULL  THEN "lpk_revision_end" > '{currentrevision}' ELSE {truevalue} END """
        #print(subsetstringtemp)
        #print(workingdatemodif, parsertruevalue, revision)
        subsetstring = subsetstringtemp.format(workingdate=workingdatemodif,
                                               truevalue=parsertruevalue,
                                                currentrevision=str(revision))

        #
        #if self.dbasetype == 'spatialite':
        #    subsetstring = '"datetimecreation" <= ' + "'" + workingdatemodif + "'"
        #    subsetstring += ' AND CASE WHEN "datetimedestruction" IS NOT NULL  THEN "datetimedestruction" > ' + "'" + workingdatemodif + "'" + ' ELSE 1 END'
        #    if self.revisionwork:
        #        subsetstring += ' AND "lpk_revision_begin" <= ' + str(self.currentrevision)
        #        subsetstring += ' AND CASE WHEN "lpk_revision_end" IS NOT NULL  THEN "lpk_revision_end" > ' + str(
        #            self.currentrevision) + ' ELSE 1 END'
        #
        #elif self.dbasetype == 'postgis':
        #    subsetstring = '"datetimecreation" <= ' + "'" + workingdatemodif + "'"
        #    subsetstring += ' AND CASE WHEN "datetimedestruction" IS NOT NULL  THEN "datetimedestruction" > ' + "'" + workingdatemodif + "'" + ' ELSE TRUE END'
        #    if self.revisionwork:
        #        subsetstring += ' AND "lpk_revision_begin" <= ' + str(self.currentrevision)
        #        subsetstring += ' AND CASE WHEN "lpk_revision_end" IS NOT NULL  THEN "lpk_revision_end" > ' + str(
        #            self.currentrevision) + ' ELSE TRUE END'


        #for tablename in self.dbasetables:
        for tablename, tabledict in self.layers.items():
            fieldnames = [field.name().lower() for field in tabledict['layerqgis'].fields()]
            if 'datecreation' in fieldnames or 'datetimecreation' in fieldnames :
                tabledict['layerqgis'].setSubsetString(subsetstring)
                tabledict['layerqgis'].triggerRepaint()


    def _____________________________maptoolsManagement(self):
        pass

    def toolsetChanged(self, newtool, oldtool=None):
        # print('toolsetchanged', newtool,oldtool )
        # self.closeEditFeature()
        if newtool != self.pointEmitter :
            self.pointEmitter.canvasClicked.disconnect()
            self.canvas.mapToolSet.disconnect(self.toolsetChanged)


    def captureGeometry(self, 
                        capturetype=0,
                        fctonstopcapture=None,
                        listpointinitialgeometry=[]):
        """
        Method called when capturing geometry is needed (add/extent point, line, polygon...)
        Launch the capture tool

        :param connectint: Catching widget signal
        :param listpointinitialgeometry: list of geometry to be extended, if new empty list
        :param type: geom type (point, line, polygone)
        """
        """
        source = self.sender()

        if source is not None and source.objectName() != 'pushButton_rajoutPoint':
            listpointinitialgeometry = []
        

        if type is None:
            if 'Point' in source.objectName():
                type = 0
            elif 'Line' in source.objectName():
                type = 1
            elif 'Polygon' in source.objectName():
                type = 2
        """
        debug = False
        if debug: 
            logging.getLogger("Lamia_unittest").debug('\n  %s \n  %s \n  %s',
                                                        str(listpointinitialgeometry), 
                                                        # type=None,
                                                        str(capturetype),
                                                        str(fctonstopcapture))      
        self.createorresetRubberband(capturetype)
        if capturetype == qgis.core.QgsWkbTypes.PointGeometry:
            self.currentmaptool = self.mtoolpoint
        elif capturetype == qgis.core.QgsWkbTypes.LineGeometry:
            self.currentmaptool = self.mtoolline
        elif capturetype == qgis.core.QgsWkbTypes.PolygonGeometry:
            self.currentmaptool = self.mtoolpolygon
        else:
            return

        if self.canvas.mapTool() != self.currentmaptool:
            self.canvas.setMapTool(self.currentmaptool)
        #self.currentmaptool.stopCapture.connect(self.setTempGeometry)
        self.currentmaptool.stopCapture.connect(fctonstopcapture)
        self.currentmaptool.setMapPoints(listpointinitialgeometry)
        #self.currentmaptool.mappoints = listpointinitialgeometry
        self.currentmaptool.startCapturing()

    def ______________________________RubberbandManagement(self):
        pass

    def createorresetRubberband(self,type=0):
        """
        Reset the rubberband

        :param type: geom type
        """
        if self.rubberBand is not None:
            self.rubberBand.reset(type)
        else:
            self.rubberBand = qgis.gui.QgsRubberBand(self.canvas,type)
            self.rubberBand.setWidth(5)
            self.rubberBand.setColor(QtGui.QColor("magenta"))

    def createRubberBandForSelection(self, qgsgeom):
        # geomtype = qgsgeom.type()
        self.createorresetRubberband(qgis.core.QgsWkbTypes.LineGeometry)
        canvasscale = self.canvas.scale() 
        distpixel = 4.0
        dist = distpixel * canvasscale / 1000.0

        bufferedgeom = qgsgeom.buffer(dist, 12).convertToType(qgis.core.QgsWkbTypes.LineGeometry)
        self.rubberBand.setToGeometry(bufferedgeom, self.dbaseqgiscrs)

    def _____________________________Functions(self):
        pass
    
    # def getNearestPk(self, dbasetable, dbasetablename, point, comefromcanvas=True):
    def getNearestPk(self, tablename, point, comefromcanvas=True): 
        """
        Permet d'avoir le pk du feature le plus proche du qgsvectorlayer correspondant à dbasetablename
        pas besoin de filtre sur les dates et versions on travaille avec le qgsectorlyaer de la table
        qui dispose déjà d'un filtre en fonction de la date et de la version
        :param dbasetable: la dbasetable considérée
        :param dbasetablename:  le nom de la dbasetable
        :param point: le point dont on veut connaitre le plus proche élément
        :param comefromcanvas: spécifie sir le point provient du canvas qgis (nécessité de trasformation) ou non
        :return: le pk de la table dbasetablenamele plus proche du point
        """
        debug = False
        layertoprocess = self.layers[tablename]['layer']
        # checking if layer is spatial one
        # isspatial = dbasetable['layerqgis'].isSpatial()
        isspatial = layertoprocess.isSpatial()
        if not isspatial:
            return None, None

        # crs transform if needed
        if debug: logging.getLogger("Lamia").debug('pointbefore %s', str(point))
        if comefromcanvas:
            if qgis.utils.iface is not None:
                point2 = self.xformreverse.transform(point)
            else:   #debug purpose
                point2 = point
        else:
            point2 = point
        if debug: logging.getLogger("Lamia").debug('pointafter %s', str(point2))

        # spatialindex creation
        # spindex = qgis.core.QgsSpatialIndex(dbasetable['layerqgis'].getFeatures())
        spindex = qgis.core.QgsSpatialIndex(layertoprocess.getFeatures())
        layernearestid = spindex.nearestNeighbor(point2, 1)

        point2geom = qgis.core.QgsGeometry.fromPointXY(point2)
        
        """
        if not self.revisionwork:
            nearestfet = self.getLayerFeatureById(dbasetablename, layernearestid[0])
        else:
            nearestfet = self.getLayerFeatureByPk(dbasetablename, layernearestid[0])
        """
        nearestfet = layertoprocess.getFeature(layernearestid[0])
        nearestfetgeom = nearestfet.geometry()

        # if point layer : nearestNeighbor gives the right value
        #if dbasetable['layerqgis'].geometryType() == 0:
        if layertoprocess.geometryType() == 0:
            disfrompoint = nearestfetgeom.distance(point2geom)
            return layernearestid[0], disfrompoint

        # if line or polygon layer : as the nearestNeighbor is with a bounding box, we need to filter
        # the elements in this boundingbox
        else:
            # clean nearestfet geometry if not valid
            if not nearestfetgeom.isGeosValid() and nearestfetgeom.type() == 1:
                nearestfetgeom = qgis.core.QgsGeometry.fromPointXY(qgis.core.QgsPointXY(nearestfetgeom.asPolyline()[0]))

            disfrompoint = nearestfetgeom.distance(point2geom)

            if debug: logging.getLogger("Lamia").debug('nearestfetgeom - dist %s %s', str(nearestfetgeom.exportToWkt()), str(disfrompoint))
            if disfrompoint < 0.1:
                disfrompoint = 0.1

            bboxtofilter = point2geom.buffer(disfrompoint * 1.2, 12).boundingBox()
            idsintersectingbbox = spindex.intersects(bboxtofilter)

            if debug: logging.getLogger("Lamia").debug('idsintersectingbbox %s', str(idsintersectingbbox))

            # search nearest geom in bbox
            distance = None
            nearestindex = None
            finalgeomispoint = False
            distanceratio = 1.2

            for intersectingid in idsintersectingbbox:
                ispoint = False
                #feat = self.getLayerFeatureByPk(dbasetablename, intersectingid)
                feat = layertoprocess.getFeature(intersectingid)
                featgeom = feat.geometry()

                if debug: logging.getLogger("Lamia").debug('intersectingid %s  - is valid : %s - type : %s - multi : %s',
                                                           str(intersectingid), str(featgeom.isGeosValid()),
                                                           str(featgeom.type()), str(featgeom.isMultipart()))

                if featgeom.isGeosValid():  # if not valid, return dist = -1...
                    dist = featgeom.distance(point2geom)
                else:  # point
                    if featgeom.type() == 1 and not featgeom.isMultipart():

                        ispoint = True
                        if len(featgeom.asPolyline()) == 1:  # polyline of 1 point
                            dist = qgis.core.QgsGeometry.fromPointXY(qgis.core.QgsPointXY(featgeom.asPolyline()[0])).distance(point2geom)
                        elif len(featgeom.asPolyline()) == 2 and featgeom.asPolyline()[0] == featgeom.asPolyline()[1]:
                            dist = qgis.core.QgsGeometry.fromPointXY(qgis.core.QgsPointXY(featgeom.asPolyline()[0])).distance(point2geom)
                    else:
                        continue
                if debug: logging.getLogger("Lamia").debug('distance : %s - ispoint : %s', str(dist), str(ispoint))
                # algo for keeping point in linestring layer as nearest
                # if point is nearest than 1.2 x dist from nearest line
                if debug: logging.getLogger("Lamia").debug('distance : %s - ispoint : %s - geomfinalispoint : %s - finaldist : %s' ,
                                                           str(dist), str(ispoint), str(finalgeomispoint), str(distance))
                if distance is None:
                    distance = dist
                    nearestindex = intersectingid
                    finalgeomispoint = ispoint
                elif not finalgeomispoint and ispoint and dist < distance*distanceratio:
                    distance = dist
                    nearestindex = intersectingid
                    finalgeomispoint = True
                elif finalgeomispoint and not ispoint and dist < distance/distanceratio:
                    distance = dist
                    nearestindex = intersectingid
                    finalgeomispoint = False
                elif finalgeomispoint == ispoint and dist < distance:
                    distance = dist
                    nearestindex = intersectingid
                    finalgeomispoint = ispoint


        if debug: logging.getLogger("Lamia").debug('nearestpk, dist %s %s', str(nearestindex), str(distance))
        return nearestindex, distance