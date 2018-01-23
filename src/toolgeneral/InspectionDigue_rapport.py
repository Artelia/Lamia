# -*- coding: utf-8 -*-

import qgis
import os
import re
import logging
from ..toolabstract.inspectiondigue_abstractworker import AbstractWorker
from qgis.PyQt import QtGui, uic, QtCore, QtXml
try:
    from qgis.PyQt.QtGui import  QPrinter
except ImportError:
    from qgis.PyQt.QtPrintSupport import QPrinter
from ..libs import pyqtgraph as pg

class printPDFWorker(AbstractWorker):

    def __init__(self, dbase, project, canvas, reporttype, pdffile,windowdialog):
        AbstractWorker.__init__(self)
        self.dbase = dbase
        self.project =project
        self.canvas =canvas
        self.reporttype = reporttype
        self.pdffile = pdffile
        self.windowdialog = windowdialog

        #debug
        formatter = logging.Formatter("%(asctime)s -- %(name)s -- %(funcName)s -- %(levelname)s -- %(message)s")
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)             # DEBUG INFO WARNING
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        stream_handler.setLevel(logging.DEBUG)
        self.logger.addHandler(stream_handler)

        self.reportdict={}
        self.reportdict['Infrastructure lineaire'] = {'qptfile': 'Infralineaire',
                                                      'atlaslayer': self.dbase.dbasetables['Infralineaire']['layerqgis'],
                                                      'atlasdriven': ['map1'],
                                                      'generalmap': ['map0'],
                                                      'layers': {'map0': [self.dbase.dbasetables['Infralineaire']['layerqgis'],
                                                                          'scan25'],
                                                                'map1': [self.dbase.dbasetables['Infralineaire']['layerqgis'],
                                                                         self.dbase.dbasetables['Equipement']['layerqgis'],
                                                                         'scan25']},
                                                      'images':{'graph' : 'profile'}}

        self.reportdict['Equipements hydrauliques'] = {'qptfile': 'Equipement_hydraulique',
                                                       'atlaslayer': self.dbase.dbasetables['Equipement']['layerqgis'],
                                                       'expression':'lk_equipement = NULL and (categorie=RHO or categorie=RHF or categorie=RHF or categorie = OUH)',
                                                       'atlasdriven': ['map1'],
                                                       'atlasdrivenscale': 2000,
                                                       'generalmap': ['map0'],
                                                       'layers':{'map0': [self.dbase.dbasetables['Equipement']['layerqgis'],
                                                                          'scan25'],
                                                                'map1': [self.dbase.dbasetables['Infralineaire']['layerqgis'],
                                                                         self.dbase.dbasetables['Equipement']['layerqgis'],
                                                                         'scan25']},
                                                       'images':{'photo': 'lastphoto'},
                                                       'childlayer': {'name': 'Equipement',
                                                                      'lkfieldparentlayer': 'lk_equimement',
                                                                      'lkfieldchildlayer': 'id_equipement',
                                                                      'images': {}}}


    def work(self):
        # self.message.emit('newComposition creation')
        self.logger.debug('started')
        mapsettings = self.canvas.mapSettings()

        if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
            newComposition = qgis.core.QgsComposition(mapsettings)
        else:
            newComposition = qgis.core.QgsComposition(self.project)

        if self.reporttype == "Infrastructure lineaire":
            reportdic = self.reportdict['Infrastructure lineaire']
        elif self.reporttype == "Equipements hydrauliques":
            reportdic = self.reportdict['Equipements hydrauliques']

            # templatepath = "C://00_Base.qpt"


        # Load template
        templatepath = os.path.abspath(os.path.join(os.path.dirname(__file__),'..','DBASE','rapport',self.dbase.type, reportdic['qptfile'] + '.qpt'))
        template_file = QtCore.QFile(templatepath)
        template_file.open(QtCore.QIODevice.ReadOnly | QtCore.QIODevice.Text)
        template_content = template_file.readAll()
        template_file.close()
        document = QtXml.QDomDocument()
        document.setContent(template_content)
        # You can use this to replace any string like this [key]
        # in the template with a new value. e.g. to replace
        # [date] pass a map like this {'date': '1 Jan 2012'}
        # substitution_map = {'DATE_TIME_START': 'foo','DATE_TIME_END': 'bar'}
        substitution_map = {}
        newComposition.loadFromTemplate(document,substitution_map)
        self.logger.debug('template loaded')

        #atlas

        atlas = newComposition.atlasComposition()
        #atlas.setCoverageLayer(self.dbase.dbasetables['Infralineaire']['layerqgis'])
        atlas.setCoverageLayer(reportdic['atlaslayer'])
        atlas.setEnabled(True)
        atlas.setSingleFile(True)
        ret = newComposition.setAtlasMode(qgis.core.QgsComposition.ExportAtlas)
        if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
            #atlas.setComposerMap(newComposition.composerMapItems()[0])
            for mapname in reportdic['atlasdriven']:
                atlas.setComposerMap(newComposition.getComposerItemById(mapname))
                newComposition.getComposerItemById(mapname).setAtlasDriven(True)
                #newComposition.getComposerItemById(mapname).setNewScale(reportdic['atlasdrivenscale'])
                newComposition.getComposerItemById(mapname).setAtlasScalingMode(qgis.core.QgsComposerMap.Fixed)
        else:
            pass
        self.logger.debug('atlas driven loaded')

        num = atlas.numFeatures()

        # fill composer map with layers
        rastertoremove = []
        for mapname in reportdic['layers'].keys():
            layersformapcomposer = []
            for layer in reportdic['layers'][mapname]:
                if isinstance(layer, str):
                    if layer == 'scan25':
                        sql = "SELECT Ressource.file from Rasters"
                        sql += " INNER JOIN Ressource ON Rasters.id_ressource = Ressource.id_ressource"
                        sql += " WHERE Rasters.typeraster = 'IRF'"
                        query = self.dbase.query(sql)
                        result = [row[0] for row in query]
                        if len(result) > 0:
                            fileraster = self.dbase.dbasetables['Infralineaire']['widget'].completePathOfFile(result[0])
                            rlayer = qgis.core.QgsRasterLayer(fileraster, os.path.basename(fileraster).split('.')[0])
                            if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                                qgis.core.QgsMapLayerRegistry.instance().addMapLayer(rlayer,False)
                            else:
                                qgis.core.QgsProject.instance().addMapLayer(rlayer,False)
                            layersformapcomposer.append(rlayer)
                            rastertoremove.append(rlayer)

                else:
                    layersformapcomposer.append(layer)

            if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                layersformapcomposer = [layer.id() for layer in layersformapcomposer]

            newComposition.getComposerItemById(mapname).setLayerSet(layersformapcomposer)
            newComposition.getComposerItemById(mapname).setKeepLayerSet(True)

            # newComposition.getComposerItemById('map0').setAtlasScalingMode(qgis.core.QgsComposerMap.Auto)

        for mapname in reportdic['generalmap']:
            layerext = reportdic['atlaslayer'].extent()
            layerextgeom = qgis.core.QgsGeometry.fromRect(layerext)
            # xform = qgis.core.QgsCoordinateTransform(self.dbase.qgiscrs, self.canvas.mapSettings().destinationCrs())
            layerextgeomcanvas = layerextgeom.transform(self.dbase.xform)
            layerextgeomcanvasfinal = layerextgeom.boundingBox()
            #newComposition.getComposerItemById(mapname).setNewExtent(layerextgeomcanvasfinal)
            newComposition.getComposerItemById(mapname).zoomToExtent(layerextgeomcanvasfinal)

            #overview
            overvw = newComposition.getComposerItemById(mapname).overview()

            # print(overvw.frameSymbol(), overvw.frameMapId(), overvw.inverted() )

        self.logger.debug('map configured')

        if False:
            layersformapcomposer = [self.dbase.dbasetables['Infralineaire']['layerqgis'],
                                    self.dbase.dbasetables['Equipement']['layerqgis']]

        if False:
            sql = "SELECT Ressource.file from Rasters"
            sql += " INNER JOIN Ressource ON Rasters.id_ressource = Ressource.id_ressource"
            sql += " WHERE Rasters.typeraster = 'IRF'"
            query = self.dbase.query(sql)
            result = [row[0] for row in query]
            print(result)
            if len(result)>0:
                fileraster = self.dbase.dbasetables['Infralineaire']['widget'].completePathOfFile(result[0])
                print(fileraster)
                rlayer = qgis.core.QgsRasterLayer(fileraster, os.path.basename(fileraster).split('.')[0])
                if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                    qgis.core.QgsMapLayerRegistry.instance().addMapLayer(rlayer,
                                                                         False)
                else:
                    qgis.core.QgsProject.instance().addMapLayer(rlayer,
                                                                False)


                layersformapcomposer.append(rlayer)
            else:
                rlayer = None
            if False:
                if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                    layersformapcomposer = [layer.id() for layer in layersformapcomposer]
                    newComposition.composerMapItems()[0].setLayerSet(layersformapcomposer)
                    newComposition.composerMapItems()[0].setKeepLayerSet(True)
                else:
                    newComposition.composerMapItems()[0].setLayers(layersformapcomposer)
                    newComposition.composerMapItems()[0].setKeepLayerSet(True)

            if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                layersformapcomposer = [layer.id() for layer in layersformapcomposer]
            newComposition.getComposerItemById('map1').setLayerSet(layersformapcomposer)
            newComposition.getComposerItemById('map1').setKeepLayerSet(True)
            #newComposition.getComposerItemById('map1').setCrs(self.dbase.qgiscrs)

            newComposition.getComposerItemById('map0').setLayerSet(layersformapcomposer)
            newComposition.getComposerItemById('map0').setKeepLayerSet(True)
            #newComposition.getComposerItemById('map0').setCrs(self.dbase.qgiscrs)
            # print(self.dbase.dbasetables['Infralineaire']['layer'].extent().asPolygon() )

            #extent
            layerext = self.dbase.dbasetables['Infralineaire']['layer'].extent()
            layerextgeom = qgis.core.QgsGeometry.fromRect(layerext)
            # xform = qgis.core.QgsCoordinateTransform(self.dbase.qgiscrs, self.canvas.mapSettings().destinationCrs())
            layerextgeomcanvas = layerextgeom.transform(self.dbase.xform)
            layerextgeomcanvasfinal = layerextgeom.boundingBox()

            print('layerextgeom', layerextgeom.asPolygon())
            newComposition.getComposerItemById('map0').setNewExtent(layerextgeomcanvasfinal)

            # self.message.emit('Printing')


        #create dict for values
        #for composeritem in newComposition.composerItems(qgis.core.QgsComposerLabel):
        for composeritem in newComposition.items():
            if isinstance(composeritem, qgis.core.QgsComposerLabel):
                #print(composeritem.displayText())
                print(composeritem.text())
                print re.findall(r'\[([^]]*)\]', composeritem.text())





        return

        try:
            printer = QPrinter()
            # newComposition.beginPrintAsPDF(printer, "C:\\test.pdf")
            # painter = QtGui.QPainter(printer)
            painter = QtGui.QPainter()
            # atlas.beginRender()

            if True:
                newComposition.setUseAdvancedEffects(False)
                atlas.beginRender()
                newComposition.beginPrintAsPDF(printer, self.pdffile)
                printReady = painter.begin(printer)
                # newComposition.beginPrint(printer)
                for i in range(0, num):

                    # self.message.emit('num' + str(i) + str(painter.isActive()))
                    # painter = QtGui.QPainter()
                    atlas.prepareForFeature(i)
                    currentfeature = atlas.feature()
                    print(currentfeature.attributes())
                    # print('*********')
                    # print(newComposition.getComposerItemById('map1').currentMapExtent().asPolygon())
                    # print(newComposition.getComposerItemById('map1').extent().asPolygon())
                    # print(newComposition.getComposerItemById('map0').extent().asPolygon())

                    # *************************************************************
                    # Values






                    try:
                        for imageitemname in reportdic['images'].keys():
                            imageitem = newComposition.getComposerItemById(imageitemname)
                            if os.path.isfile(reportdic['images'][imageitemname]):
                                imagefile = reportdic['images'][imageitemname]
                            elif reportdic['images'][imageitemname] == 'profile':
                                imagefile = self.getImageFileOfProfile(atlas.currentGeometry(self.dbase.qgiscrs),imageitem)
                            imageitem.setPicturePath(imagefile)
                            imageitem.updateItem()
                    except Exception as e:
                        print('image error', e)
                    # newComposition.beginPrintAsPDF(printer, "C:\\test.pdf")
                    # newComposition.beginPrint(printer)
                    # printReady = painter.begin(printer)
                    if i > 0:
                        printer.newPage()
                    newComposition.doPrint(printer, painter)
                    # painter.end()
                # self.message.emit('end print')
                atlas.endRender()
                painter.end()

        except Exception as e:
            self.error.emit(e)

        for rastlayer in rastertoremove:
            if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                qgis.core.QgsMapLayerRegistry.instance().removeMapLayer(rastlayer)
            else:
                qgis.core.QgsProject.instance().removeMapLayer(rastlayer)

        if False:
            if self.reporttype == "Infrastructure lineaire":
                if rlayer is not None:
                    if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                        qgis.core.QgsMapLayerRegistry.instance().removeMapLayer(rlayer)
                    else:
                        qgis.core.QgsProject.instance().removeMapLayer(rlayer)

    def getImageFileOfProfile(self,featgeom,imageitem):
        point1 = [featgeom.asPolyline()[0].x(), featgeom.asPolyline()[0].y()]
        point2 = [featgeom.asPolyline()[-1].x(), featgeom.asPolyline()[-1].y()]
        #self.windowdialog.pathtool.plotWdg.setParent(None)

        #self.windowdialog.pathtool.resizewidget(imageitem.rect().width(), imageitem.rect().height())

        # self.windowdialog.pathtool.plotWdg.resize(imageitem.rect().width(), imageitem.rect().height())
        #self.windowdialog.pathtool.plotWdg.setVisible(True)
        #self.windowdialog.pathtool.plotWdg.setVisible(False)
        # QtGui.QApplication.processEvents()

        # win = pg.GraphicsWindow(title="Basic plotting examples")
        # win.resize(imageitem.rect().width(), imageitem.rect().height())

        self.windowdialog.pathtool.computePath(point1, point2)
        print('path',self.windowdialog.pathtool.geomfinalids)

        print(imageitem.rect().width(), imageitem.rect().height())

        exportfile = os.path.join(os.path.dirname(__file__), '..', 'config', 'tempgraph.png')
        self.windowdialog.pathtool.exportCurrentGraph(imageitem.rect().width()*96,
                                                      imageitem.rect().height()*96,
                                                      exportfile)

        return os.path.abspath(exportfile)
