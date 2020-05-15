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
import os, sys, io, logging, datetime, re, json
import qgis, qgis.core, qgis.utils, qgis.gui
from qgis.PyQt import QtGui, QtCore
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
        self.dbaseqgiscrs = None
        if canvas is None and qgis.utils.iface is not None:
            self.setCanvas(qgis.utils.iface.mapCanvas())
        
        self.layers = {}
        self.qgislegendnode = None

        self.xform = None
        self.xformreverse = None

        #behaviour
        self.editingrawlayer = False
        self.currentmaptool = None  #the maptool in use

    def setCanvas(self,qgscanvas):
        if self.canvas:
            try:
                self.canvas.destinationCrsChanged.disconnect(self.updateQgsCoordinateTransform)
            except TypeError:
                pass
        
        self.canvas = qgscanvas

        """

        cadwdg = qgis.gui.QgsAdvancedDigitizingDockWidget(iface.mapCanvas())
        print(cadwdg.cadEnabled () )
        cadwdg.enable()
        """

        #init maptools
        self.cadwdg = qgis.gui.QgsAdvancedDigitizingDockWidget(self.canvas)
        self.cadwdg.enable()
        self.mtoolpoint = mapToolCapture(self.canvas, self.cadwdg,
                                qgis.gui.QgsMapToolCapture.CapturePoint)
        self.mtoolline = mapToolCapture(self.canvas, self.cadwdg,
                                        qgis.gui.QgsMapToolCapture.CaptureLine)
        self.mtoolpolygon = mapToolCapture(self.canvas, self.cadwdg,
                                        qgis.gui.QgsMapToolCapture.CapturePolygon)
        self.pointEmitter = qgis.gui.QgsMapToolEmitPoint(self.canvas)


        self.updateQgsCoordinateTransform()

        self.canvas.destinationCrsChanged.connect(self.updateQgsCoordinateTransform)

    def _____________________________layersManagement(self):
        pass


    def createLayersForQgisServer(self,dbaseparser,specifichost=None):
        """
        used for creating a qgis project configured for using in postgis server
        """
        if dbaseparser.TYPE == 'spatialite':
            return
        #* create pg_config.conf
        """
        [qgisservertest]
        host=docker.for.win.localhost
        port=5432
        user=pvr
        password=pvr
        dbname=lamiaunittest
        """
        dbqgisserverdirectory = os.path.join(dbaseparser.dbaseressourcesdirectory,'qgisserver')
        if not os.path.isdir(dbqgisserverdirectory):
            os.mkdir(dbqgisserverdirectory)
        
        pg_configfile = os.path.join(dbqgisserverdirectory,'pg_service.conf')
        
        filewriter = open(pg_configfile, 'w', newline='\n')
        dbaseconf = dbaseparser.connectconf
        filewriter.write('[qgisserver]\n')
        if specifichost:
            filewriter.write('host=' + specifichost + '\n')
        else:
            filewriter.write('host=' + dbaseconf['host'] + '\n')
        filewriter.write('port=' + dbaseconf['port'] + '\n')
        filewriter.write('user=' + dbaseconf['user'] + '\n')
        filewriter.write('password=' + dbaseconf['password'] + '\n')
        filewriter.write('dbname=' + dbaseconf['dbname'] + '\n')
        filewriter.close()

        #create project with layers inside
        layers={}
        project = qgis.core.QgsProject.instance()
        projectcrs = qgis.core.QgsCoordinateReferenceSystem()
        projectcrs.createFromString('EPSG:' + str(dbaseparser.crsnumber))
        project.setCrs(projectcrs)

        for rawtablename, rawdict in dbaseparser.dbasetables.items():
            # if 'geom' not in rawdict:
            #     continue
            tablenames = [rawtablename]
            tabletypes = ['layer']
            if 'djangoviewsql' in rawdict.keys():
                tabletypes += ['layerdjango']
                tablenames += [rawtablename + '_django']
            if 'qgisPGviewsql' in rawdict.keys() or 'qgisviewsql' in rawdict.keys() :
                tabletypes += ['layerqgis']
                tablenames += [rawtablename + '_qgis']
            
            layers[rawtablename] = {}
            for i, tablename in enumerate(tablenames):
                tablenamelower = tablename.lower()
                tabletype = tabletypes[i]
                #rawlayers
                uri = qgis.core.QgsDataSourceUri()
                uri.setConnection('qgisserver',             # the service name
                                  dbaseparser.pgdb.lower(),
                                  dbaseparser.pguser,
                                  dbaseparser.pgpassword,
                                  qgis.core.QgsDataSourceUri.SslDisable )

                if dbaseparser.isTableSpatial(tablenamelower):
                    uri.setDataSource(dbaseparser.pgschema.lower(), str(tablenamelower), 'geom', '', "pk_" + rawtablename.lower())
                    geomtype = dbaseparser.dbasetables[rawtablename]['geom']
                    if geomtype == 'POINT':
                        qgsgeomtype = qgis.core.QgsWkbTypes.Point
                    elif geomtype == 'LINESTRING':
                        qgsgeomtype = qgis.core.QgsWkbTypes.LineString
                    elif geomtype == 'MULTIPOLYGON':
                        qgsgeomtype = qgis.core.QgsWkbTypes.MultiPolygon 
                    # print(geomtype)
                    uri.setWkbType(qgsgeomtype)
                    uri.setSrid(str(dbaseparser.crsnumber))
                else:
                    uri.setDataSource(dbaseparser.pgschema.lower(), str(tablenamelower), None, '', "pk_" + rawtablename.lower())
                layers[rawtablename][tabletype] = qgis.core.QgsVectorLayer(uri.uri(), tablename, 'postgres')
                layers[rawtablename][tabletype].dataProvider().setEncoding('UTF-8')
                layers[rawtablename][tabletype].setCrs(projectcrs)

        #load layers and set style
        root = project.layerTreeRoot()
        styledirectory = os.path.join(os.path.dirname(Lamia.__file__), 'DBASE', 'style', dbaseparser.worktype, '0_Defaut' )
        for tablename in layers:
            if ('layerqgis' in layers[tablename].keys() 
                    and layers[tablename]['layerqgis'].geometryType() != qgis.core.QgsWkbTypes.NullGeometry ):
                project.addMapLayer(layers[tablename]['layerqgis'], True)
                # root.addLayer(layers[tablename]['layerqgis'])
                # stylepath = os.path.join(styledirectory, tablename + '.qml')
                # stylepath = os.path.realpath(stylepath)
                layers[tablename]['layerqgis'].triggerRepaint()
                layers[tablename]['layerqgis'].dataProvider().reloadData()


        if self.canvas:
            self.canvas.refreshAllLayers()
            self.canvas.refresh()

        for tablename in layers:
            if ('layerqgis' in layers[tablename].keys() 
                    and layers[tablename]['layerqgis'].geometryType() != qgis.core.QgsWkbTypes.NullGeometry ):
                stylepath = os.path.join(styledirectory, tablename + '.qml')
                if os.path.isfile(stylepath):
                    txt, res = layers[tablename]['layerqgis'].loadNamedStyle(stylepath, loadFromLocalDb=False)
                    if False and not res:   #TODO style do not apply arg !!!!! geometryType() not recognized
                        print(stylepath, os.path.isfile(stylepath))
                        print(layers[tablename]['layerqgis'].geometryType() )
                        print(layers[tablename]['layerqgis'].dataProvider().wkbType () )
                        print(txt, res)
                


        projectfile = os.path.join(dbqgisserverdirectory,'project.qgs')
        project.write(projectfile)
        project.clear()

        #finaly write dbasedbasetables
        jsonfile = os.path.join(dbqgisserverdirectory,'dbasetables.json')
        with open(jsonfile, 'w') as outfile:
            json.dump(dbaseparser.dbasetables, outfile, indent=2)




    def createLayers(self, dbaseparser):

        if dbaseparser.__class__.__name__ == 'SpatialiteDBaseParser':
            dbtype = 'spatialite'
        elif dbaseparser.__class__.__name__ == 'PostGisDBaseParser':
            dbtype = 'postgres'
        
        for rawtablename, rawdict in dbaseparser.dbasetables.items():
            #old way for qgislayer
            # if 'geom' not in rawdict:
            #     continue
            tablenames = [rawtablename]
            tabletypes = ['layer']
            if 'djangoviewsql' in rawdict.keys():
                tabletypes += ['layerdjango']
                tablenames += [rawtablename + '_django']
            if 'qgisPGviewsql' in rawdict.keys() or 'qgisviewsql' in rawdict.keys() :
                tabletypes += ['layerqgis']
                tablenames += [rawtablename + '_qgis']

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
                                        dbaseparser.pgdb.lower(), dbaseparser.pguser, dbaseparser.pgpassword)
                    if dbaseparser.isTableSpatial(tablenamelower):
                        uri.setDataSource(dbaseparser.pgschema.lower(), str(tablenamelower), 'geom', '', "pk_" + rawtablename.lower())
                    else:
                        uri.setDataSource(dbaseparser.pgschema.lower(), str(tablenamelower), None, '', "pk_" + rawtablename.lower())
                self.layers[rawtablename][tabletype] = qgis.core.QgsVectorLayer(uri.uri(), tablename, dbtype)

            #ValueMap for qgislayer
            if 'layerqgis' in self.layers[rawtablename].keys():
                workingvl = self.layers[rawtablename]['layerqgis']
                cstdict = self._getConstraintFromDBaseTables(dbaseparser, rawtablename)
                for i, field in enumerate(workingvl.fields()):
                    if field.name() in cstdict.keys():
                        config = {'map' : cstdict[field.name()]}
                        widget_setup = qgis.core.QgsEditorWidgetSetup('ValueMap',config)
                        workingvl.setEditorWidgetSetup(i, widget_setup)


            #new way for qgislayer
            tabletype = 'layerqgisjoined'
            # self.layers[rawtablename][tabletype] = qgis.core.QgsVectorLayer(self.layers[rawtablename]['layer'] )
            self.layers[rawtablename][tabletype] = self.layers[rawtablename]['layer'].clone()
            currentlayername = rawtablename

            for parentable in dbaseparser.getParentTable(rawtablename):
                currentField = 'lpk_' + parentable.lower()
                joinedField = 'pk_' + parentable.lower()
                joinObject = qgis.core.QgsVectorLayerJoinInfo()
                joinObject.setJoinFieldName(joinedField)
                joinObject.setTargetFieldName(currentField)
                joinObject.setJoinLayerId(self.layers[parentable]['layer'].id())
                joinObject.setUsingMemoryCache(True)
                joinObject.setJoinLayer(self.layers[parentable]['layer'])
                joinObject.setEditable(True)
                joinObject.setPrefix ('')
                joinObject.setDynamicFormEnabled(True)
                self.layers[rawtablename][tabletype].addJoin(joinObject)
                currentlayername = parentable

            #ValueMap for qgislayerjoined
            workingvl = self.layers[rawtablename]['layerqgisjoined']
            cstdict = self._getConstraintFromDBaseTables(dbaseparser, rawtablename)
            for i, field in enumerate(workingvl.fields()):
                if field.name() in cstdict.keys():
                    config = {'map' : cstdict[field.name()]}
                    widget_setup = qgis.core.QgsEditorWidgetSetup('ValueMap',config)
                    workingvl.setEditorWidgetSetup(i, widget_setup)


        self.dbaseqgiscrs = qgis.core.QgsCoordinateReferenceSystem()
        self.dbaseqgiscrs.createFromString('EPSG:' + str(dbaseparser.crsnumber))
        self.updateQgsCoordinateTransform()


    def _getConstraintFromDBaseTables(self, dbaseparser, tablename):
        dictcst = {}
        parenttables = dbaseparser.getParentTable(tablename) + [tablename]
        parenttables = parenttables[::-1]
        for tablename in parenttables:
            for fieldname, fielddict in dbaseparser.dbasetables[tablename]['fields'].items():
                if 'Cst' in fielddict:
                    valuesformap = [[lst[0], lst[1]] for lst in fielddict['Cst']]
                    qgisvaluesformat = [{var[0]: var[1]} for var in valuesformap]
                    dictcst[fieldname] =  qgisvaluesformat
        return dictcst


    def createSingleQgsVectorLayer(self,dbaseparser,tablename='tempvectorlayer',isspatial = True,  sql='', tableid=None):
        layer = None

        if tableid is not None:
            finaltableid = tableid
        else:
            finaltableid = "id_" + str(tablename.lower())
        if dbaseparser.__class__.__name__ == 'SpatialiteDBaseParser':
            dbtype = 'spatialite'
        elif dbaseparser.__class__.__name__ == 'PostGisDBaseParser':
            dbtype = 'postgres'

        uri = qgis.core.QgsDataSourceUri()

        if dbtype == 'spatialite':
            # uri.setDataSource("public","japan_ver52","the_geom","","gid")
            # uri.setDataSource("",sql,"the_geom","","gid")
            uri.setDatabase(dbaseparser.spatialitefile)
            if isspatial:
                uri.setDataSource('', f'({sql})' , 'geom' ,'',finaltableid)
            else:
                uri.setDataSource('', f'({sql})', '', '', finaltableid)

            layer = qgis.core.QgsVectorLayer(uri.uri(), tablename, 'spatialite')


        elif dbtype == 'postgres':
            uri.setConnection(dbaseparser.pghost, 
                              str(dbaseparser.pgport), 
                              dbaseparser.pgdb.lower(), 
                              dbaseparser.pguser, 
                              dbaseparser.pgpassword)

            # qgis bug _ need to add schema name 
            sqlsplitted = re.split('[ \n]',sql)
            finalsql = []
            for word in sqlsplitted:
                if word.split('.')[0].split('_qgis')[0] in dbaseparser.dbasetables.keys():
                    word = dbaseparser.pgschema.lower() + '.' + word
                finalsql.append(word)
            finalsql = ' '.join(finalsql)



            if isspatial:
                #uri.setDataSource(dbaseparser.pgschema.lower(), str(tablenamelower), 'geom', '', "pk_" + rawtablename.lower())
                #uri.setDataSource(dbaseparser.pgschema.lower(), f'({sql})', 'geom','' , finaltableid)
                uri.setDataSource('', f'({finalsql})', 'geom','' , finaltableid)
            else:
                #uri.setDataSource(dbaseparser.pgschema.lower(), f'({sql})', None, '' , finaltableid )
                uri.setDataSource('', f'({finalsql})', None, '' , finaltableid )

            layer = qgis.core.QgsVectorLayer(uri.uri(), tablename, 'postgres')
        """
        uri = qgis.core.QgsDataSourceUri()
        uri.setConnection('localhost', 
                        '5432', 
                        'lamiaunittest', 
                        'pvr', 
                        'pvr')
        sql = "SELECT * FROM Infralineaire"
        print(f'({sql})')
        uri.setDataSource('', f'({sql})' , 'geom' ,'','pk_infralineaire')
        uri.setSchema('base2_digue_lamia')
        #base2_digue_lamia
        layer = qgis.core.QgsVectorLayer(uri.uri(), 'tt', 'postgres')
        print(uri.uri())
        QgsProject.instance().addMapLayer(layer)
        print([fet.id() for fet in layer.getFeatures()])
        """


        return layer


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
            # #old way
            # for tablename in dbasetables:
            #     if ('layerqgis' in dbasetables[tablename].keys() 
            #             and dbasetables[tablename]['layerqgis'].geometryType() != qgis.core.QgsWkbTypes.NullGeometry ):
            #         qgis.core.QgsProject.instance().addMapLayer(dbasetables[tablename]['layerqgis'], False)
            #         lamialegendgroup.addLayer(dbasetables[tablename]['layerqgis'])
            #new way
            for tablename in self.layers:
                if ('layerqgis' in self.layers[tablename].keys() 
                        and self.layers[tablename]['layerqgisjoined'].geometryType() != qgis.core.QgsWkbTypes.NullGeometry 
                        ):
                    qgis.core.QgsProject.instance().addMapLayer(self.layers[tablename]['layerqgis'], False)
                    lamialegendgroup.addLayer(self.layers[tablename]['layerqgis'])

        else:
            layerstoadd = []
            # dbasetables = self.layers
            goodtablekey = [val for val in self.layers.keys() if 'layerqgis' in self.layers[val].keys()  ]
            for tablename in goodtablekey:
                layerstoadd.append(self.layers[tablename]['layerqgis'])
            self.canvas.setLayers(layerstoadd)
            if 'edge' in self.layers.keys():
                self.canvas.setExtent(self.layers['edge']['layer'].extent())
            else:
                self.canvas.setExtent(self.layers['Infralineaire']['layer'].extent())
            self.canvas.refresh()


    def unloadLayersInCanvas(self):
        if self.qgislegendnode is not None:
            self.qgislegendnode.removeAllChildren()
            root = qgis.core.QgsProject.instance().layerTreeRoot()
            root.removeChildNode(self.qgislegendnode)
        elif qgis.utils.iface is None:
            self.canvas.setLayers([])
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
        
        if self.canvas:
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


        self.editlayer = self.layers[layername]['layerqgisjoined'].clone()

        qgis.core.QgsProject.instance().addMapLayer(self.editlayer, False)
        if self.qgislegendnode is None: #outsideqgis case
            return
        self.editfeaturetreelayer = self.qgislegendnode.insertLayer(0,self.editlayer)
        if qgis.utils.iface is not None :
            qgis.utils.iface.setActiveLayer(self.editlayer)
            self.editlayer.startEditing()
            qgis.utils.iface.actionVertexTool().trigger()

        self.editingrawlayer = True
        

    def saveRawLayerInCanvasForEditing(self, savechanges=False):

        if self.editingrawlayer:
            self.editingrawlayer = False
            if isinstance(savechanges,bool) and savechanges:
                self.editlayer.commitChanges()
            else:
                self.editlayer.rollBack()

            #self.qgislegendnode.removeLayer(self.editlayer)
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
            if 'layerqgis' in tabledict.keys():
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
            self.currentmaptool.activate()
            print(self.currentmaptool.cadDockWidget().cadEnabled () )
            self.currentmaptool.cadDockWidget().enable()
            print(self.currentmaptool.cadDockWidget().cadEnabled () )
            self.currentmaptool.activate()

        #self.currentmaptool.stopCapture.connect(self.setTempGeometry)
        self.currentmaptool.stopCapture.connect(fctonstopcapture)
        self.currentmaptool.setMapPoints(listpointinitialgeometry)
        #self.currentmaptool.mappoints = listpointinitialgeometry
        self.currentmaptool.startCapturing()


    def stopCapture(self):
        if self.currentmaptool is not None:
            try:
                self.currentmaptool.stopCapture.disconnect()
            except TypeError:
                pass


    def ______________________________RubberbandManagement(self):
        pass


    def createorresetRubberband(self,type=0, instance=None):
        """
        Reset the rubberband

        :param type: geom type
        """
        if instance is None:
            instance = self
            rbcolor = 'red'
        else:
            rbcolor = 'blue'
        if not hasattr(instance, 'rubberBand'):
            instance.rubberBand = None
        
        if instance.rubberBand is not None:
            instance.rubberBand.reset(type)
        else:
            instance.rubberBand = qgis.gui.QgsRubberBand(self.canvas,type)
            instance.rubberBand.setWidth(5)
            instance.rubberBand.setColor(QtGui.QColor(rbcolor))

    def createorresetRubberband_Old(self,type=0):
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

    def createRubberBandForSelection(self, qgsgeom, instance=None):
        # geomtype = qgsgeom.type()
        if not instance:
            instance = self
        self.createorresetRubberband(qgis.core.QgsWkbTypes.LineGeometry, instance=instance)
        canvasscale = self.canvas.scale() 
        distpixel = 4.0
        dist = distpixel * canvasscale / 1000.0

        if not isinstance(qgsgeom,list):
            qgsgeom = [qgsgeom]

        for geom in qgsgeom:
            bufferedgeom = geom.buffer(dist, 12).convertToType(qgis.core.QgsWkbTypes.LineGeometry)
            instance.rubberBand.addGeometry(bufferedgeom, self.dbaseqgiscrs)


    def getQgsGeomFromPk(self,dbaseparser, tablename, pk):
        wkt = dbaseparser.getWktGeomFromPk(tablename, pk)
        geom = qgis.core.QgsGeometry.fromWkt(wkt)
        return geom

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
        layertoprocess = self.layers[tablename]['layerqgis']        #layer qgis has conf with only good versions
        # checking if layer is spatial one
        # isspatial = dbasetable['layerqgis'].isSpatial()
        isspatial = layertoprocess.isSpatial()
        if not isspatial:
            return None, None

        # crs transform if needed
        if debug: logging.getLogger("Lamia").debug('pointbefore %s', str(point))
        if comefromcanvas:
            point2 = self.xformreverse.transform(point)
        else:
            point2 = point
        if debug: logging.getLogger("Lamia").debug('pointafter %s', str(point2))

        # spatialindex creation
        # spindex = qgis.core.QgsSpatialIndex(dbasetable['layerqgis'].getFeatures())
        spindex = qgis.core.QgsSpatialIndex(layertoprocess.getFeatures())
        layernearestid = spindex.nearestNeighbor(point2, 1)
        if not layernearestid:
            return

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

            if debug: logging.getLogger("Lamia").debug('nearestfetgeom - dist %s %s', str(nearestfetgeom.asWkt()), str(disfrompoint))
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

