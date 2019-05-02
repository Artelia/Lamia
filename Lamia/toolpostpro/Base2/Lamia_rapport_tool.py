# -*- coding: utf-8 -*-

import qgis
import qgis.core
import os
import re
import logging
# from ..toolabstract.inspectiondigue_abstractworker import AbstractWorker
from qgis.PyQt import QtGui, uic, QtCore, QtXml
try:
    from qgis.PyQt.QtGui import QPrinter
    from qgis.PyQt.QtGui import (QProgressBar, QApplication,QAction, QWidget, QAbstractItemView)
    #except ImportError:
except ImportError as e:
    from qgis.PyQt.QtPrintSupport import QPrinter
    from qgis.PyQt.QtWidgets import  (QProgressBar, QApplication,QAction, QWidget, QAbstractItemView)
# from ...libs import pyqtgraph as pg
import networkx
import numpy as np
from collections import OrderedDict
import glob, sys, logging, inspect

from ...toolabstract.Lamia_abstract_tool import AbstractLamiaTool




class RapportTool(AbstractLamiaTool):
    DBASES = ['digue', 'base_digue', 'base2_digue', 'base2_parking']
    TOOLNAME = 'rapporttools'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None, parentwidget=None, parent=None):
        super(RapportTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil, parentwidget, parent=parent)
        # self.postInit()

    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Import/export'
        self.NAME = 'Impression rapport'
        self.dbasetablename = 'Zonegeo'
        self.visualmode = [4]
        # self.PointENABLED = True
        # self.LineENABLED = True
        # self.PolygonEnabled = True
        # self.magicfunctionENABLED = True
        # self.linkagespec = None
        # self.pickTable = None
        # print(self.dbase.recentsdbase)
        self.multipleselection = True

        self.iconpath = os.path.join(os.path.dirname(__file__), 'Lamia_rapport_tool_icon.png')
        self.qtreewidgetfields = ['libelle']

        # ****************************************************************************************
        # properties ui
        self.groupBox_geom.setParent(None)
        self.groupBox_elements.setParent(None)

        self.qfiledlg = self.windowdialog.qfiledlg
        self.confData = None

        self.confdatamain = os.path.join(os.path.dirname(inspect.getsourcefile(self.__class__)), self.TOOLNAME)
        self.confdataproject = os.path.join(self.dbase.dbaseressourcesdirectory, 'config',self.TOOLNAME)

        if False:
            print(inspect.getmodule(self))
            #self.impressionpdfworker = inspect.getmodule(self).printPDFBaseWorker(dbase=self.dbase)
            self.impressionpdfworker = printPDFBaseWorker(dbase=self.dbase)
            print(self.impressionpdfworker.NAME )

    def initFieldUI(self):
        if self.userwdgfield is None:

            # ****************************************************************************************
            # userui

            self.userwdgfield = UserUI()
            self.userwdgfield.toolButton_filechooser.clicked.connect(self.chooseFile)

            self.userwdgfield.pushButton_export.clicked.connect(self.launchRapport)

            if self.dbase.qgsiface is None:
                self.userwdgfield.lineEdit_nom.setText('c://test_rapport.pdf')


    def chooseFile(self):
        reportfile = self.qfiledlg.getSaveFileName(self,
                                                   'Lamia - impression rapport',
                                                   '',
                                                   'PDF (*.pdf)')
        if reportfile:
            if isinstance(reportfile, tuple):    # qt5
                reportfile = reportfile[0]
            self.userwdgfield.lineEdit_nom.setText(reportfile)



    def postOnActivation(self):

        self.createconfData()

        #self.linkedtreewidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.linkedtreewidget.itemSelectionChanged.connect(self.itemChanged)

    def postInitFeatureProperties(self, feat):
        pass





    def itemChanged(self, itemplus=None, itemmoins=None):
        pass
        #print(itemplus,itemmoins )

        #print('treewdg', self.linkedtreewidget.selectedItems())
        #print([it.text(0) for it in self.linkedtreewidget.selectedItems()])



    def createconfData(self):
        """
        Lit le fichier de conf situé dans self.createfilesdir, soit dans ./rapporttools
        :return: un dictionnaire confData :
                {'atalslayersql' : la requete qui selectionne les éléments à énumérer dans l'atlas,
                 'atlaslayerid' : l'id à considérer par rapport aux colonnes de la requete,
                 'atlaslayerstyle' : le style du qgsvectorlyaer utilisé pour l'atlas
                 atlasdrivemap : {...,
                                  le nom du mapitem qui se déplace avec l'atlas : {'minscale' : l'echelle minimum ,
                                                                                typescale : le type d'echelle,
                                                                                layers: list des maplayers à mettre dans le  mapitem},
                                 ...},
                 generalmap : {...,
                                  le nom du mapitem de la carte générale :     {'minscale' : l'echelle minimum ,
                                                                                typescale : le type d'echelle,
                                                                                layers: list des maplayers à mettre dans le  mapitem},
                                 ...},
                 childprint :  {confname : le nom du fichier txt dans rapporttools à utiliser
                                linkcolumn: le colonne de liaison avec l'id du coverage layer,
                                optionsql: requete sql à rajouter à la fin de la requete de selection des enfants}
                 }
        """

        debug = False

        if debug: logging.getLogger("Lamia").debug('started')

        self.confData = {}
        self.userwdgfield.comboBox_type.clear()

        for workdir in [self.confdatamain, self.confdataproject ]:
            for filename in glob.glob(os.path.join(workdir, '*.txt')):
                basename = os.path.basename(filename).split('.')[0]
                if debug: logging.getLogger("Lamia").debug('basename %s',basename )
                self.confData[basename] = {}
                if sys.version_info.major == 2:
                    filetoread = open(filename, 'r')
                elif sys.version_info.major == 3:
                    filetoread = open(filename, 'r',encoding="utf-8")
                compt = 0
                for line in filetoread:
                    if line[0:3] == '###':  # new field
                        actualdictkey = line[3:].strip()
                        if actualdictkey in ['atlaslayersql','atlaslayerid' ,'atlaslayerstyle','ordering']:
                            self.confData[basename][actualdictkey] = ''
                        else:
                            self.confData[basename][actualdictkey] = {}
                    elif line[0:1] == '#':
                        continue
                    elif line.strip() == '' :
                        continue
                    else:
                        if actualdictkey == 'atlaslayersql':
                            self.confData[basename][actualdictkey] += line.strip() + ' '
                        elif actualdictkey in ['atlaslayerid','atlaslayerstyle','ordering'] :
                            self.confData[basename][actualdictkey] = line.strip()
                        elif actualdictkey in ['atlasdrivemap','generalmap']:
                            speclist = line.split(';')
                            self.confData[basename][actualdictkey][speclist[0].strip()] = {}
                            if speclist[1].strip() != '':
                                minscale = int(speclist[1].strip())
                            else:
                                minscale = None

                            typescale = speclist[2].strip()
                            if typescale != '':
                                if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                                    toexec = "typescale = qgis.core.QgsComposerMap." + typescale
                                    exec(toexec)
                                else:
                                    typescale = eval("qgis.core.QgsLayoutItemMap." + typescale)

                            self.confData[basename][actualdictkey][speclist[0].strip()]['minscale'] = minscale
                            self.confData[basename][actualdictkey][speclist[0].strip()]['typescale'] = typescale
                            self.confData[basename][actualdictkey][speclist[0].strip()]['layers'] = eval(speclist[3].strip())
                        elif actualdictkey in ['spatial']:
                            self.confData[basename][actualdictkey] = eval(line.strip())
                        elif actualdictkey in ['childprint']:
                            speclist = line.split(';')
                            self.confData[basename][actualdictkey]['confname'] = speclist[0].strip()
                            self.confData[basename][actualdictkey]['linkcolumn'] = speclist[1].strip()
                            self.confData[basename][actualdictkey]['optionsql'] = speclist[2].strip()
                        elif actualdictkey in ['images']:
                            speclist = line.split(';')
                            self.confData[basename][actualdictkey][speclist[0].strip()] = speclist[1].strip()

                filetoread.close()

                if self.userwdgfield is not None:
                    if len(basename.split('_')) == 1:
                        if workdir == self.confdataproject:
                            basename = '*' + basename
                        self.userwdgfield.comboBox_type.addItems([basename])

        if False:
            # Update dialog
            if self.userwdgfield is not None:
                self.userwdgfield.comboBox_type.clear()
                for typerapport in self.confData.keys():
                    if len(typerapport.split('_')) == 1:
                        self.userwdgfield.comboBox_type.addItems([typerapport])

        if debug: logging.getLogger("Lamia").debug('confData : %s',self.confData )




    def launchRapport(self):
        pdffile = self.userwdgfield.lineEdit_nom.text()
        reporttype = self.userwdgfield.comboBox_type.currentText()

        if reporttype[0] == '*':
            createfilesdir = self.confdataproject
            reporttype = reporttype[1:]
        else:
            createfilesdir = self.confdatamain

        self.impressionpdfworker = inspect.getmodule(self).printPDFBaseWorker(dbase=self.dbase,
                                                                             windowdialog=self.windowdialog,
                                                                             parentprintPDFworker=None,
                                                                             confData=self.confData,
                                                                             pdffile=pdffile,
                                                                             reporttype=reporttype,
                                                                              templatedir=createfilesdir )

        self.impressionpdfworker.work()





class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        # self.setupUi(self)
        uipath = os.path.join(os.path.dirname(__file__), 'Lamia_rapport_tool.ui')
        uic.loadUi(uipath, self)






class printPDFBaseWorker(object):

    NAME = 'pdf1'

    def __init__(self,
                 dbase=None,
                 windowdialog=None,
                 parentprintPDFworker=None,
                 confData=None,
                 pdffile=None,
                 reporttype=None,
                 templatedir=None):

        self.dbase = dbase
        self.windowdialog = windowdialog
        self.parentprintPDFworker = parentprintPDFworker

        self.project = qgis.core.QgsProject.instance()
        self.canvas = self.dbase.canvas
        self.reporttype = reporttype
        self.pdffile = pdffile
        self.currentid = None
        self.currentimageItem = None

        self.presetscales = [50,500, 1000, 2500, 5000, 10000, 25000, 50000]
        
        self.logger = logging.getLogger("Lamia")

        self.confData = None
        self.createfilesdir = None
        self.idecalage = 0
        if self.parentprintPDFworker is None:
            self.printer = QPrinter()
            self.painter = QtGui.QPainter()
            self.confData = confData
            self.createfilesdir = templatedir
            # self.parentheightpx = None
        else:
            self.printer = parentprintPDFworker.printer
            self.painter = parentprintPDFworker.painter
            self.confData = parentprintPDFworker.confData
            self.createfilesdir = parentprintPDFworker.createfilesdir
            # self.parentheightpx = parentprintPDFworker.parentheightpx


        #self.postInit()
        #self.createconfData()







    def setCoverageLayer(self):
        """
        créé le qgsvectorlayer utilisé pour l'atlas
        attention ce fichier doit avoir pour clé primaire l'id de la couche lamia et non le pk...
        :return: qgsvectorlayer qui servira à l'atlas
        """
        debug = False

        sql = self.atlasconfData['atlaslayersql']


        #sql += ' AND '
        #sql += self.dbase.dateVersionConstraintSQL()

        sql = self.dbase.updateQueryTableNow(sql)

        if self.parentprintPDFworker is not None:
            sql += ' AND ' + self.parentprintPDFworker.atlasconfData['childprint']['linkcolumn']
            #sql += ' = ' + str(self.parentprintPDFworker.currentid)
            if False:
                linktablename = self.parentprintPDFworker.atlasconfData['childprint']['linkcolumn'].split('_')[-1]
                sql += ' = ' + str(self.parentprintPDFworker.currentatlasfeat['id_' + linktablename])
                sql += ' ' + self.parentprintPDFworker.atlasconfData['childprint']['optionsql']
            if True:
                linkcolumnname = self.parentprintPDFworker.atlasconfData['childprint']['linkcolumn'].split('.')[-1]
                if linkcolumnname.split('_')[0] in ['lpk', 'lid']:
                    linkcolumnname = linkcolumnname[1:]
                else:
                    self.windowdialog.errorMessage('Erreur sur la champs de liaison childprint')
                    return False
                sql += ' = ' + str(self.parentprintPDFworker.currentatlasfeat[linkcolumnname])
                sql += ' ' + self.parentprintPDFworker.atlasconfData['childprint']['optionsql']

        if debug: logging.getLogger("Lamia").debug('atlaslayer sql : %s', sql)

        if sys.version_info.major == 2:
            atlaslayer = self.dbase.createQgsVectorLayer(tablename='atlaslayer',
                                                        isspatial=self.atlasconfData['spatial'],
                                                        sql=sql,
                                                        tableid=self.atlasconfData['atlaslayerid'])
        elif sys.version_info.major == 3:
            atlaslayer = self.dbase.createQgsVectorLayer(tablename='atlaslayer',
                                                        isspatial=self.atlasconfData['spatial'],
                                                        sql=sql,
                                                        tableid=self.atlasconfData['atlaslayerid'])

        if debug: logging.getLogger("Lamia").debug('atlaslayer pk index : %s', str(atlaslayer.dataProvider().pkAttributeIndexes()))
        if debug: logging.getLogger("Lamia").debug('atlaslayer ids : %s', str([fet.id() for fet in atlaslayer.getFeatures() ]))

        return atlaslayer


    def work(self):
        """
        Méthode principale - génère le pdf
        :return:
        """
        if self.dbase.qgsiface is not None:
            debug = False
            stop10 = False
        else:
            debug = True  # True False
            stop10 = True


        if debug: logging.getLogger("Lamia").debug('started')
        mapsettings = self.canvas.mapSettings()
        layertoremove = []
        if self.parentprintPDFworker is not None:
            self.reporttype = self.parentprintPDFworker.atlasconfData['childprint']['confname']

        self.atlasconfData = self.confData[self.reporttype]

        if debug: logging.getLogger("Lamia").debug('self.atlasconfData %s', str(self.atlasconfData))

        # ********************* create composition *****************************
        newComposition = self.createComposition(mapsettings )
        if debug: logging.getLogger("Lamia").debug('template loaded')

        # ********************* set atlas and linked composeritem *****************************
        coveragelayer = self.setCoverageLayer()
        layertoremove.append(coveragelayer)
        atlas = self.setAtlasLayer(newComposition,coveragelayer )
        if debug: logging.getLogger("Lamia").debug('atlas driven loaded')

        # ********************* fill composer map with layers *****************************
        layers = self.fillComposerMapsWihLayers(newComposition, coveragelayer)
        for layer in layers:
            layertoremove.append(layer)
        if debug: logging.getLogger("Lamia").debug('composer map fill')

        # ********************* %lamia var in composer *****************************
        dictfields = self.getLamiaVarInComposition(newComposition)
        if debug: logging.getLogger("Lamia").debug('lamia var read')


        # ********************* ordering ids for pdf *****************************

        idsforreportdict = self.getOrderedIdsForAtlas(coveragelayer)


        if False:
            orderedids = OrderedDict()
            if self.idparent is None:
                orderedids = self.orderIdsAlongPath(coveragelayer)
            #if orderedids is None:
            if len(orderedids) == 0:
                #orderedids[0] = [feat.id() for feat in reportdic['atlaslayer'].getFeatures()]
                orderedids[0] = [feat.id() for feat in coveragelayer.getFeatures()]




            if debug: self.logger.debug('orderedids %s', str(orderedids))


            if orderedids is None or len(orderedids) == 0:
                return

            # ********************* if zonegeo selected *****************************
            idsforreportdict = OrderedDict()
            setselected = set(self.dbase.dbasetables['Zonegeo']['layerqgis'].selectedFeaturesIds())
            setids = set([fet.id() for fet in self.dbase.dbasetables['Zonegeo']['layerqgis'].getFeatures()])
            isresultvalid = setselected.issubset(setids)

            if (self.idparent is None
                    and len(self.dbase.dbasetables['Zonegeo']['layerqgis'].selectedFeatures()) > 0
                    and isresultvalid):

                idszonegeoselected = [int(feat['id_zonegeo']) for feat in self.dbase.dbasetables['Zonegeo']['layerqgis'].selectedFeatures()]
                for zonegeoid in orderedids.keys():
                    # print(zonegeoid,idszonegeoselected )
                    if zonegeoid in idszonegeoselected:
                        idsforreportdict[zonegeoid] = orderedids[zonegeoid]
            else:
                idsforreportdict = orderedids

        if debug: self.logger.debug('idsforreport %s', str(idsforreportdict))



        # ********************* progress bar *****************************
        progress = self.initProgressBar(idsforreportdict)


       # *********************************************************************
        # ********************* begin printing  *****************************
        # *********************************************************************
        # try:
        atlas.beginRender()
        exporter = self.initPrinterAndPainter(newComposition,atlas)

        idecalage = 0
        compt = 0


        #initialize var for page dimension in case of child print
        if self.parentprintPDFworker is not None:
            self.heightpx = 0
            self.currentpageheightpx  = self.parentprintPDFworker.heightpx
        elif 'childprint' in self.atlasconfData.keys() and len(self.atlasconfData['childprint'].keys()) > 0:
            if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                parentheightmm = newComposition.getComposerItemById('parentheight').rectWithFrame().height()
            else:
                parentheightmm = newComposition.itemById('parentheight').rectWithFrame().height()

            pageheightmm = self.printer.paperRect(QPrinter.Millimeter).height()
            self.heightpx = int(parentheightmm / pageheightmm * self.painter.device().height())
            self.currentpageheightpx = 0
        else:
            self.heightpx = 0
            self.currentpageheightpx = 0

        indexpagetotal = -1

        for zonegeoid in idsforreportdict.keys():
            #set generalmap extent to zonegeo

            if zonegeoid > 0:
                self.setGeneralMapExtentByZonegeo(newComposition,zonegeoid)
                if debug: self.logger.debug('setGeneralMapExtentByZonegeo done')


            for indexpage, featid in enumerate(idsforreportdict[zonegeoid]):
                indexpagetotal += 1
                if debug: self.logger.debug('featid %s , indexpage %s', str(featid), str(indexpage))
                if False and stop10 and indexpage == 20: break

                self.currentid = featid
                compt += 1
                if self.parentprintPDFworker is None:
                    self.setLoadingProgressBar(progress, compt)

                if False:
                    request = qgis.core.QgsFeatureRequest().setFilterExpression('"' + self.atlasconfData['atlaslayerid'] + '" = ' + str(featid))
                if True:
                    request = qgis.core.QgsFeatureRequest(featid)

                # if debug: logging.getLogger("Lamia").debug('request %s', self.atlasconfData['atlaslayerid'] + '" = ' + str(featid))

                if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                    #atlasfeat = reportdic['atlaslayer'].getFeatures(qgis.core.QgsFeatureRequest(featid)).next()
                    self.currentatlasfeat = coveragelayer.getFeatures(qgis.core.QgsFeatureRequest(request)).next()
                else:
                    #atlasfeat = next(reportdic['atlaslayer'].getFeatures(qgis.core.QgsFeatureRequest(featid)))
                    requ = coveragelayer.getFeatures(qgis.core.QgsFeatureRequest(request))
                    #print('res',[fet.id() for fet in requ])
                    #print('res',[fet['id_desordre'] for fet in coveragelayer.getFeatures()])
                    self.currentatlasfeat = coveragelayer.getFeatures(qgis.core.QgsFeatureRequest(request)).__next__()

                # print('fetaatr', atlasfeat.attributes())


                if self.atlasconfData['spatial']:
                    if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                        if self.currentatlasfeat.geometry().boundingBox().toString() == 'Empty':        #point in linelayer
                            #for mapname in reportdic['atlasdriven']:
                            for mapname in self.atlasconfData['atlasdrivemap']:
                                newComposition.getComposerItemById(mapname).setAtlasScalingMode(qgis.core.QgsComposerMap.Fixed)
                                # newComposition.getComposerItemById(mapname).setNewScale(reportdic['atlasdrivenminscale'])
                                newComposition.getComposerItemById(mapname).setNewScale(self.atlasconfData['atlasdrivemap'][mapname]['minscale'])
                                #print('***', mapname, self.atlasconfData['atlasdrivemap'][mapname]['minscale'])

                        else:
                            #for mapname in reportdic['atlasdriven']:
                            for mapname in self.atlasconfData['atlasdrivemap']:
                                # newComposition.getComposerItemById(mapname).setAtlasScalingMode(reportdic['atlastypescale'])
                                newComposition.getComposerItemById(mapname).setAtlasScalingMode(self.atlasconfData['atlasdrivemap'][mapname]['typescale'])
                    else:
                        pass





                if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                    atlas.prepareForFeature(self.currentatlasfeat)
                    #currentfeature = atlas.feature()
                else:
                    atlas.seekTo(self.currentatlasfeat)
                    #currentfeature = atlasfeat

                if  debug: self.logger.debug('feat attr : %s', str([field.name() for field in self.currentatlasfeat.fields()]))
                if debug: self.logger.debug('feat attr : %s',str(self.currentatlasfeat.attributes()))

                #check atlasdriven map scale

                if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                    #for mapname in reportdic['atlasdriven']:
                    for mapname in self.atlasconfData['atlasdrivemap']:
                        # if newComposition.getComposerItemById(mapname).scale() < reportdic['atlasdrivenminscale']:
                        if newComposition.getComposerItemById(mapname).scale() < self.atlasconfData['atlasdrivemap'][mapname]['minscale']:
                            # newComposition.getComposerItemById(mapname).setNewScale(reportdic['atlasdrivenminscale'])
                            newComposition.getComposerItemById(mapname).setNewScale(self.atlasconfData['atlasdrivemap'][mapname]['minscale'])
                            # print('ok')
                        elif newComposition.getComposerItemById(mapname).scale() > 100000.0:
                            #newComposition.getComposerItemById(mapname).setNewScale(reportdic['atlasdrivenminscale'])
                            newComposition.getComposerItemById(mapname).setNewScale(self.atlasconfData['atlasdrivemap'][mapname]['minscale'])
                            #print('ok')
                else:
                    for mapname in self.atlasconfData['atlasdrivemap']:
                        currentmapscale = newComposition.itemById(mapname).scale()
                        if currentmapscale < self.atlasconfData['atlasdrivemap'][mapname]['minscale']:
                            newComposition.itemById(mapname).setScale(self.atlasconfData['atlasdrivemap'][mapname]['minscale'])
                        elif currentmapscale > 100000.0:
                            newComposition.itemById(mapname).setScale(self.atlasconfData['atlasdrivemap'][mapname]['minscale'])
                        else:   # because bad predef scale in qgis 3
                            if int(currentmapscale) not in self.presetscales:
                                for scale in self.presetscales:
                                    if currentmapscale >= scale:
                                        continue
                                    else:
                                        newComposition.itemById(mapname).setScale(scale)
                                        break

                self.processImages(newComposition, atlas, self.currentatlasfeat)

                self.processLamiaVars(newComposition, dictfields, self.currentatlasfeat)

                self.printAtlasPage(newComposition,exporter, indexpagetotal, indexpage, idecalage)


        # ********************* close printing  *****************************
        atlas.endRender()
        if self.parentprintPDFworker is None:
            self.painter.end()
        if debug: self.logger.debug('end')
        if progress is not None: self.dbase.qgsiface.messageBar().clearWidgets()
        # return

        for rastlayer in layertoremove:
            if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                qgis.core.QgsMapLayerRegistry.instance().removeMapLayer(rastlayer)
            else:
                qgis.core.QgsProject.instance().removeMapLayer(rastlayer)


        if debug: self.logger.debug('end')


    def processImages(self,newComposition,atlas,atlasfeat):
        if True:

            #for imageitemname in reportdic['images'].keys():
            for imageitemname in self.atlasconfData['images'].keys():
                # get imageitem
                if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                    imageitem = newComposition.getComposerItemById(imageitemname)
                else:
                    imageitem = newComposition.itemById(imageitemname)
                    # print('****', imageitem.__class__)
                    # composeritem = newComposition.itemByUuid(compitemuuid)
                    #imageitem.__class__ = qgis.core.QgsLayoutItemPicture

                # print(imageitem, reportdic['images'][imageitemname])
                imageresult = None
                self.currentimageItem = imageitem
                # *******************************************************

                if os.path.isfile(self.atlasconfData['images'][imageitemname]):
                    imageresult = self.atlasconfData['images'][imageitemname]

                elif 'photo' in self.atlasconfData['images'][imageitemname]:
                    table = self.atlasconfData['images'][imageitemname].split('.')[0]
                    photoid = int(self.atlasconfData['images'][imageitemname].split('.')[-1][5:])
                    imageresult = self.getNumberedPhoto(atlasfeat, table, photoid)

                elif 'ressource' in self.atlasconfData['images'][imageitemname]:
                    table = self.atlasconfData['images'][imageitemname].split('.')[0]
                    ressourcenum = int(self.atlasconfData['images'][imageitemname].split('.')[-1][9:])
                    #imageresult = self.getPhoto(reportdic, currentfeature)
                    imageresult = self.getNumberedRessource(atlasfeat, table, ressourcenum)

                elif self.atlasconfData['images'][imageitemname] == 'logo':
                    imageresult = os.path.join(os.path.dirname(__file__), '..','..', 'DBASE', 'utils', 'logo.jpg')

                else:
                    typeprocess = self.atlasconfData['images'][imageitemname]
                    exec('imageresult = self.' + typeprocess + '()')




                if False:
                    if imageitem is not None:
                        # print('ok',imagefile )
                        imageitem.setPicturePath(imagefile)
                        if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                            imageitem.updateItem()
                        else:
                            imageitem.refreshPicture()

                if True:
                    if imageitem is not None:
                        # print('ok',imagefile )
                        if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                            if isinstance(imageitem, qgis.core.QgsComposerPicture):
                                imageitem.setPicturePath(imageresult)
                                imageitem.updateItem()
                            elif isinstance(imageitem, qgis.core.QgsComposerFrame):
                                # print(htmltotal)
                                imageitem.multiFrame().setContentMode(1)
                                imageitem.multiFrame().setHtml(imageresult)
                                imageitem.multiFrame().loadHtml()
                        else:
                            if isinstance(imageitem, qgis.core.QgsLayoutItemPicture):
                                imageitem.setPicturePath(imageresult)
                                imageitem.refreshPicture()
                            if isinstance(imageitem, qgis.core.QgsLayoutFrame):
                                imageitem.multiFrame().setContentMode(1)
                                imageitem.multiFrame().setHtml(imageresult)
                                imageitem.multiFrame().loadHtml()



    def processLamiaVars(self,newComposition, dictfields, atlasfeat):
        """
        Remplace les champs %lamia et %lamiasql definis dans le composeur par leur valeur dépendante du qgsfeature en
        cours de l'atlas

        ex : %lamia.lamiatable.lamiacolonne  fait une requete de type :
        WITH tempquery AS (sql cript for coveragelayer creation) SELECT lamiacolonne FROM lamiatable
        WHERE atlaslayerid (défini dans conf) = (l'id en cours de l'atlas)

        ex : %lamiasql.lamiascriptsql :
        WITH tempquery AS (sql cript for coveragelayer creation) + lamiascriptsql
        AND atlaslayerid (défini dans conf) = (l'id en cours de l'atlas)


        :param newComposition:
        :param dictfields:
        :return:
        """

        debug = False
        atlasfeatid = atlasfeat.id()
        atlasfeatpk = atlasfeat[self.atlasconfData['atlaslayerid']]

        for compitemuuid in dictfields.keys():
            if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                composeritem = newComposition.getComposerItemByUuid(compitemuuid)
            else:
                composeritem = newComposition.itemByUuid(compitemuuid)
                composeritem.__class__ = qgis.core.QgsLayoutItemLabel
            finaltxt = []
            for temptxt in dictfields[compitemuuid]:
                if 'lamia.' in temptxt:
                    table = temptxt.split('.')[1]
                    field = '.'.join(temptxt.split('.')[2:])
                    #creating sql request

                    if False:
                        sql = ' WITH tempquery AS ('
                        if False:
                            sql += self.atlasconfData['atlaslayersql']
                            sql += ' AND '
                            sql += self.dbase.dateVersionConstraintSQL()
                        sql += self.dbase.updateQueryTableNow(self.atlasconfData['atlaslayersql'])
                        if self.parentprintPDFworker is not None:
                            sql += ' AND ' + self.parentprintPDFworker.atlasconfData['childprint']['linkcolumn']
                            # sql += ' = ' + str(self.parentprintPDFworker.currentid)
                            # sql += ' = ' + str(self.parentprintPDFworker.currentid)
                            linktablename = self.parentprintPDFworker.atlasconfData['childprint']['linkcolumn'].split('_')[-1]
                            sql += ' = ' + str(self.parentprintPDFworker.currentatlasfeat['id_' + linktablename])
                            sql += ' ' + self.parentprintPDFworker.atlasconfData['childprint']['optionsql']
                        sql += ') '
                        # sql += "SELECT " + field + " FROM " + table
                        sql += "SELECT " + field + " FROM tempquery "
                        sql += ' WHERE ' + self.atlasconfData['atlaslayerid'] + ' = ' + str(atlasfeat.id())

                    if True:
                        tempsplittedquery = self.dbase.splitSQLSelectFromWhereOrderby(self.atlasconfData['atlaslayersql'])
                        tempsplittedquery['SELECT'] = table + '.' + field
                        if 'WHERE' in tempsplittedquery.keys():
                            tempsplittedquery['WHERE'] += ' AND ' + self.atlasconfData['atlaslayerid'] + ' = ' + str(atlasfeatpk)
                        else:
                            tempsplittedquery['WHERE'] =  self.atlasconfData['atlaslayerid'] + ' = ' + str( atlasfeatpk)
                        #tempsplittedquery['FROM'] = table
                        sql = self.dbase.rebuildSplittedQuery(tempsplittedquery)
                        sql = self.dbase.updateQueryTableNow(sql)


                    if debug: self.logger.debug('sql %s', str(sql))

                    query = self.dbase.query(sql)
                    valtemp = [row[0] for row in query][0]
                    rawtable = table.split('_')[0]  #split in cas _qgis table
                    val = self.dbase.getConstraintTextFromRawValue(rawtable, field, valtemp)

                    if unicode(val).lstrip("-").isdigit() and float(val) == -1.:
                        finaltxt.append('/')
                    elif val == '':
                        finaltxt.append(' / ')
                        """
                        elif field[0:8] == 'datetime':
                            tempdate = '-'.join(val.split(' ')[0].split('-')[::-1])
                            finaltxt.append(tempdate + ' ' + str(val.split(' ')[1]))
    
                        elif field[0:4] == 'date':
                            dateinverted = '-'.join(val.split('-')[::-1])
                            finaltxt.append(dateinverted)
                        """
                    else:
                        finaltxt.append(unicode(val))

                elif 'lamiasql.' in temptxt:
                    if False:
                        sql = ' WITH tempquery AS ('
                        sql += self.atlasconfData['atlaslayersql']

                        sql += ' AND '
                        sql += self.dbase.dateVersionConstraintSQL()
                        if self.parentprintPDFworker is not None:
                            sql += ' AND ' + self.parentprintPDFworker.atlasconfData['childprint']['linkcolumn']
                            # sql += ' = ' + str(self.parentprintPDFworker.currentid)
                            # sql += ' = ' + str(self.parentprintPDFworker.currentid)
                            linktablename = self.parentprintPDFworker.atlasconfData['childprint']['linkcolumn'].split('_')[-1]
                            sql += ' = ' + str(self.parentprintPDFworker.currentatlasfeat['id_' + linktablename])
                            sql += ' ' + self.parentprintPDFworker.atlasconfData['childprint']['optionsql']
                        sql += ') '
                        sql += temptxt[9:]
                        sql += ' AND ' + self.atlasconfData['atlaslayerid'] + ' = ' + str(atlasfeatpk)


                    if True:
                        tempsplittedquery = self.dbase.splitSQLSelectFromWhereOrderby(self.atlasconfData['atlaslayersql'])
                        #tempsplittedquery['SELECT'] = table + '.' + field
                        tempsplittedquery['SELECT'] = '(' + temptxt[9:] + ')'


                        if 'WHERE' in tempsplittedquery.keys():
                            tempsplittedquery['WHERE'] += ' AND ' + self.atlasconfData['atlaslayerid'] + ' = ' + str(atlasfeatpk)
                        else:
                            tempsplittedquery['WHERE'] =  self.atlasconfData['atlaslayerid'] + ' = ' + str( atlasfeatpk)
                        #tempsplittedquery['FROM'] = table
                        sql = self.dbase.rebuildSplittedQuery(tempsplittedquery)
                        sql = self.dbase.updateQueryTableNow(sql)

                    if debug: self.logger.debug('lamiasql %s', str(sql))

                    query = self.dbase.query(sql)
                    result = [row for row in query]
                    if len(result) > 0:
                        txtresult = [res  if res is not None else '/' for res in result[0] ]
                        finaltxt.append(' - '.join(txtresult))
                    else:
                        finaltxt.append('NR')

                else:
                    finaltxt.append(temptxt)
            if debug: self.logger.debug('result %s', str(finaltxt))
            txt = ''.join(finaltxt)
            composeritem.setText(txt)





    def createComposition(self, mapsettings):
        """
        Create a composition with template found in \rapporttools\self.reporttype + '.qpt'
        :param mapsettings: qgis mapsettings
        :return: the composition created
        """

        debug = False
        if debug: self.logger.debug('started')

        if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
            newComposition = qgis.core.QgsComposition(mapsettings)
        else:
            newComposition = qgis.core.QgsPrintLayout(self.project)

        if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
            templatefile = self.reporttype + '.qpt'
        else:
            templatefile = self.reporttype + '3.qpt'

        #templatepath = os.path.abspath(os.path.join(os.path.dirname(__file__), 'rapporttools', templatefile))
        templatepath = os.path.abspath(os.path.join(self.createfilesdir, templatefile))
        template_file = QtCore.QFile(templatepath)
        template_file.open(QtCore.QIODevice.ReadOnly | QtCore.QIODevice.Text)
        template_content = template_file.readAll()
        template_file.close()

        if debug: self.logger.debug('template read')

        if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
            document = QtXml.QDomDocument()
            document.setContent(template_content)
            # You can use this to replace any string like this [key]
            # in the template with a new value. e.g. to replace
            # [date] pass a map like this {'date': '1 Jan 2012'}
            # substitution_map = {'DATE_TIME_START': 'foo','DATE_TIME_END': 'bar'}
            substitution_map = {}
            newComposition.loadFromTemplate(document, substitution_map)
        else:
            document = QtXml.QDomDocument()
            document.setContent(template_content)
            substitution_map = {}
            newComposition.loadFromTemplate(document, qgis.core.QgsReadWriteContext())

        return newComposition

    def setAtlasLayer(self, newComposition, coveragelayer):
        """
        Parametre l'atlas de la newComposition
        :param newComposition: la composition en cours
        :param coveragelayer: le layer utilisé pour l'atals
        :return: l'atlasComposition de la newComposition
        """
        if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
            atlas = newComposition.atlasComposition()
        else:
            atlas = newComposition.atlas()
        # apply style
        # stylepath = os.path.join(os.path.dirname(__file__), 'rapporttools', self.atlasconfData['atlaslayerstyle'])
        stylepath = os.path.join(self.createfilesdir, self.atlasconfData['atlaslayerstyle'])
        coveragelayer.loadNamedStyle(stylepath)
        # add coveragelayer to QgsProject
        if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
            qgis.core.QgsMapLayerRegistry.instance().addMapLayer(coveragelayer, False)
        else:
            qgis.core.QgsProject.instance().addMapLayer(coveragelayer, False)
        # set coveragelayer to atlas
        atlas.setCoverageLayer(coveragelayer)
        # set scale mode

        # enable atlas
        atlas.setEnabled(True)

        # set atlas spec
        if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
            atlas.setSingleFile(True)
            ret = newComposition.setAtlasMode(qgis.core.QgsComposition.ExportAtlas)

        if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
            for mapname in self.atlasconfData['atlasdrivemap'].keys():
                # atlas.setComposerMap(newComposition.getComposerItemById(mapname))
                newComposition.getComposerItemById(mapname).setAtlasDriven(True)
                newComposition.getComposerItemById(mapname).setAtlasScalingMode(self.atlasconfData['atlasdrivemap'][mapname]['typescale'])
        else:
            for mapname in self.atlasconfData['atlasdrivemap'].keys():
                # print('mapname', mapname)
                temp1 = newComposition.itemById(mapname)
                # print(type(temp1))
                # temp1.__class__ = qgis.core.QgsLayoutItemMap
                newComposition.itemById(mapname).setAtlasDriven(True)
                # print(self.atlasconfData['atlasdrivemap'][mapname]['typescale'])
                newComposition.itemById(mapname).setAtlasScalingMode(self.atlasconfData['atlasdrivemap'][mapname]['typescale'])
                newComposition.itemById(mapname).setFixedSize(newComposition.itemById(mapname).sizeWithUnits()) # nedd in qgis3
                newComposition.itemById(mapname).setCrs(self.dbase.qgiscrs)     # for scale analysys in qgis3


        return atlas

    def fillComposerMapsWihLayers(self, newComposition, coveragelayer):
        """
        Charge les tables spécifiée dans le fichier txt de conf dans les mapitems
        :param newComposition: la composition en cours d'utilisation
        :param confData: le ficier de conf
        :return: les qgsmaplayers qu'il faudra décahrger ensuite
        """
        debug = False
        layertoremove = []
        for typemap in ['atlasdrivemap', 'generalmap']:
            # for mapname in reportdic['layers'].keys():
            for mapname in self.atlasconfData[typemap].keys():
                layersformapcomposer = []
                # print('mapname',mapname)
                for layername in self.atlasconfData[typemap][mapname]['layers']:
                    if layername == 'atlaslayer':
                        layersformapcomposer.append(coveragelayer)

                    elif layername == 'scan25':
                        sql = "SELECT file from Rasters_qgis"
                        # sql += " INNER JOIN Ressource ON Rasters.id_ressource = Ressource.id_ressource"
                        sql += " WHERE typeraster = 'IRF'"
                        query = self.dbase.query(sql)
                        result = [row[0] for row in query]
                        if len(result) > 0:
                            # fileraster = self.dbase.dbasetables['Infralineaire']['widget'].completePathOfFile(result[0])
                            fileraster = self.dbase.completePathOfFile(result[0])
                            if os.path.isfile(fileraster):
                                rlayer = qgis.core.QgsRasterLayer(fileraster,
                                                                  os.path.basename(fileraster).split('.')[0])
                                try:
                                    rlayer.renderer().setOpacity(0.5)
                                except:
                                    pass
                                if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                                    qgis.core.QgsMapLayerRegistry.instance().addMapLayer(rlayer, False)
                                else:
                                    qgis.core.QgsProject.instance().addMapLayer(rlayer, False)
                                layersformapcomposer.append(rlayer)
                                layertoremove.append(rlayer)
                            else:
                                if debug: logging.getLogger("Lamia").debug('no scan25 file')

                    elif layername == 'ortho':
                        sql = "SELECT file from Rasters_qgis"
                        # sql += " INNER JOIN Ressource ON Rasters.id_ressource = Ressource.id_ressource"
                        sql += " WHERE typeraster = 'ORF'"
                        query = self.dbase.query(sql)
                        result = [row[0] for row in query]
                        if len(result) > 0:
                            # fileraster = self.dbase.dbasetables['Infralineaire']['widget'].completePathOfFile(result[0])
                            fileraster = self.dbase.completePathOfFile(result[0])
                            if os.path.isfile(fileraster):
                                rlayer = qgis.core.QgsRasterLayer(fileraster,
                                                                  os.path.basename(fileraster).split('.')[0])
                                if self.dbase.qgsiface is not None:
                                    rlayer.renderer().setOpacity(0.5)
                                if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                                    qgis.core.QgsMapLayerRegistry.instance().addMapLayer(rlayer, False)
                                else:
                                    qgis.core.QgsProject.instance().addMapLayer(rlayer, False)
                                layersformapcomposer.append(rlayer)
                                layertoremove.append(rlayer)
                            else:
                                if debug: logging.getLogger("Lamia").debug('no ortho file')

                    elif layername in self.dbase.dbasetables.keys():
                        strtoeval = "self.dbase.dbasetables['" + layername + "']['layerqgis']"
                        layer = eval(strtoeval)
                        layersformapcomposer.append(layer)
                    else:
                        layer = self.dbase.dbasetables['Rasters']['widget'][0].createMapLayer(libelle=layername)
                        if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                            qgis.core.QgsMapLayerRegistry.instance().addMapLayer(layer, False)
                        else:
                            qgis.core.QgsProject.instance().addMapLayer(layer, False)
                        layersformapcomposer.append(layer)
                        layertoremove.append(layer)


                if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                    layersformapcomposer = [layer.id() for layer in layersformapcomposer]

                if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                    newComposition.getComposerItemById(mapname).setLayerSet(layersformapcomposer)
                    newComposition.getComposerItemById(mapname).setKeepLayerSet(True)
                else:
                    temp1 = newComposition.itemById(mapname)
                    temp1.__class__ = qgis.core.QgsLayoutItemMap
                    temp1.setLayers(layersformapcomposer)
                    temp1.setKeepLayerSet(True)


        return layertoremove


    def getLamiaVarInComposition(self, newComposition):
        """
        Crée un dictionnaire des requetes sql présentes dans la composition
        qui sont sous la forme .. #lamia {requete sql} #lamia ..
        :param newComposition: la composition en cours d'utilisation
        :return: un dicionnaire : {...composeritem.uuid(): le texte du composerlabel splité avec #
        """

        dictfields = {}
        if True:
            for composeritem in newComposition.items():
                if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                    labelclass = qgis.core.QgsComposerLabel
                else:
                    labelclass = qgis.core.QgsLayoutItemLabel
                if isinstance(composeritem, labelclass):
                    # print(composeritem.text())
                    if "#lamia" in composeritem.text():
                        txtsplit = composeritem.text().split('#')
                        dictfields[composeritem.uuid()] = txtsplit
        return dictfields




    def getOrderedIdsForAtlas(self,coveragelayer):
        """
        Renvoi un dictionnaire avec zoneeo_id camme clé et la list des ids du coveragelayer ordonnée comme valeur
        est ensuite lu et itéré lors de la generation de l'atlas
        :param coveragelayer:
        :return:idsforreportdict : OrderedDict with {... zongeo_id:[list of ids of coverage layer],...}
        """
        debug = False

        orderedids = OrderedDict()
        if self.parentprintPDFworker is None and self.atlasconfData['spatial'] and 'ordering' in self.atlasconfData.keys():
            idszonegeoselected=[]
            if len(self.dbase.dbasetables['Zonegeo']['layerqgis'].selectedFeatures()) > 0:
                idszonegeoselected = [int(feat['id_zonegeo']) for feat in self.dbase.dbasetables['Zonegeo']['layerqgis'].selectedFeatures()]

            orderedids = self.orderIdsAlongPath(coveragelayer,idszonegeoselected)
        else:
            orderedids[0] = [feat.id() for feat in coveragelayer.getFeatures()]



        # if orderedids is None:
        if len(orderedids) == 0:
            # orderedids[0] = [feat.id() for feat in reportdic['atlaslayer'].getFeatures()]
            orderedids[0] = [feat.id() for feat in coveragelayer.getFeatures()]

        if debug: self.logger.debug('orderedids %s', str(orderedids))

        if orderedids is None or len(orderedids) == 0:
            return

        if False:
            # ********************* if zonegeo selected *****************************
            idsforreportdict = OrderedDict()
            setselected = set(self.dbase.dbasetables['Zonegeo']['layerqgis'].selectedFeaturesIds())
            setids = set([fet.id() for fet in self.dbase.dbasetables['Zonegeo']['layerqgis'].getFeatures()])
            isresultvalid = setselected.issubset(setids)

            idsforreportdict = orderedids


            if (self.parentprintPDFworker is None
                    and len(self.dbase.dbasetables['Zonegeo']['layerqgis'].selectedFeatures()) > 0
                    and isresultvalid):

                idszonegeoselected = [int(feat['id_zonegeo']) for feat in
                                      self.dbase.dbasetables['Zonegeo']['layerqgis'].selectedFeatures()]
                for zonegeoid in orderedids.keys():
                    # print(zonegeoid,idszonegeoselected )
                    if zonegeoid in idszonegeoselected:
                        idsforreportdict[zonegeoid] = orderedids[zonegeoid]
            else:
                idsforreportdict = orderedids

        return orderedids




    def initProgressBar(self, idsforreportdict):
        """
        Initialise la progress bar d'avancement de la generation du rapport
        :param idsforreportdict:
        :return:
        """
        if self.dbase.qgsiface is not None and self.parentprintPDFworker is None:
            progressMessageBar = self.dbase.qgsiface.messageBar().createMessage("Generation du pdf...")
            progress = QProgressBar()
            lenidsforreportdict = 0
            for reportkey in idsforreportdict.keys():
                lenidsforreportdict += len(idsforreportdict[reportkey])
            progress.setMaximum(lenidsforreportdict)
            progress.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
            progressMessageBar.layout().addWidget(progress)
            if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                self.dbase.qgsiface.messageBar().pushWidget(progressMessageBar, self.dbase.qgsiface.messageBar().INFO)
            else:
                self.dbase.qgsiface.messageBar().pushWidget(progressMessageBar, qgis.core.Qgis.Info)
        else:
            progress = None

        return progress



    def orderIdsAlongPath(self, coveragelayer,zonegeoids=[]):
        if self.dbase.qgsiface is not None:
            debug = False
        else:
            debug = True  #True false
        orderedids=OrderedDict()

        if debug : self.logger.debug('start')

        # **********************   ordering view ****************************
        # ************ by zonegeo and infralineaire ************************

        #get simple list of infralin id within zonegeo
        if len(zonegeoids) == 0:
            sql = "SELECT id_zonegeo FROM Zonegeo "
            query = self.dbase.query(sql)
            zonegeoids = [row[0] for row in query]

        dictedgesordered = {}
        if len(zonegeoids) > 0:
            for zonegeoid in zonegeoids:
                dictedgesordered[zonegeoid] = []
                sql = "SELECT ST_AsText(geom) FROM Zonegeo WHERE id_zonegeo = " + str(zonegeoid)
                query = self.dbase.query(sql)
                zonegeogeom = [row[0] for row in query][0]
                if False:
                    sql = "SELECT Infralineaire.id_infralineaire FROM Infralineaire"
                    sql += " INNER JOIN Objet ON Objet.id_objet = Infralineaire.id_objet "
                    sql += " WHERE ST_WITHIN(ST_MakeValid(Infralineaire.geom),ST_GeomFromText('" + str(zonegeogeom) + "'," + str(
                        self.dbase.crsnumber) + "))"
                    sql += '  AND Objet.Datecreation <= ' + "'" + self.dbase.workingdate + "'"
                    if self.dbase.dbasetype == 'postgis':
                        sql += ' AND CASE WHEN Objet.Datedestruction IS NOT NULL  '
                        sql += 'THEN Objet.DateDestruction > ' + "'" + self.dbase.workingdate + "'" + ' ELSE TRUE END'
                    elif self.dbase.dbasetype == 'spatialite':
                        sql += ' AND CASE WHEN Objet.datedestruction IS NOT NULL  '
                        sql += 'THEN Objet.dateDestruction > ' + "'" + self.dbase.workingdate + "'" + ' ELSE 1 END'
                if True:
                    sql = "SELECT Infralineaire_qgis.id_infralineaire FROM Infralineaire_qgis"
                    sql += " WHERE ST_WITHIN(ST_MakeValid(Infralineaire_qgis.geom),ST_GeomFromText('" + str(zonegeogeom) + "'," + str(self.dbase.crsnumber) + "))"
                    sql += ' AND '
                    # sql = self.dbase.appendDateVersionConstraintToSQL(sql)
                    sql += self.dbase.dateVersionConstraintSQL()
                    # print('sql',sql)



                query = self.dbase.query(sql)
                result = [row[0] for row in query]
                dictedgesordered[zonegeoid] = result



        if debug: self.logger.debug('dictedgesordered %s', str(dictedgesordered))

        # get pathtool and init it
        pathtool = None
        for i, tool in enumerate(self.windowdialog.tools):
            if 'PathTool' in tool.__class__.__name__ :
                pathtool = self.windowdialog.tools[i]
        #self.windowdialog.pathtool.computeNXGraphForAll()
        pathtool.computeNXGraphForAll()


        #begin ordering process
        if len(dictedgesordered) > 0:
            for zonegeoid in dictedgesordered.keys():
                orderedids[zonegeoid] = []
                # define networkx graph for specified ids
                nxgraph, ids, indexnoeuds, infralinfaces, reverseinfralinfaces = pathtool.computeNXGraph(dictedgesordered[zonegeoid])
                # get subgraphs within nxgraph
                subgraphs = networkx.connected_component_subgraphs(nxgraph)
                #for all subgrahs, order ids
                for subgraph in subgraphs:
                    #recherche des extremites presentes qu une fois - ce sont les limites d'un path
                    npedges = np.ravel(list(subgraph.edges()))
                    unique, counts = np.unique(npedges, return_counts=True)
                    edgeextremite = unique[np.where(counts==1)]
                    edgenoeud = unique[np.where(counts>2)]

                    if len(edgenoeud)>0:
                        print('attention presence d un noeud - non traite')
                    else:
                        paths=[list(edgeextremite)]     #logiquement cette list comporte deux elements : le noeud de depart et d 'arrivee

                    # if len(paths)==0 and len(edgenoeud)==0: #cas d'un circuit fermé

                    if debug: self.logger.debug('subgraph %s edgeextremite : %s edgenoeud : %s', str(subgraph), str(edgeextremite), str(edgenoeud))

                    for path in paths:
                        shortestpathedges = networkx.shortest_path(nxgraph, path[0], path[1])
                        #id = self.windowdialog.pathtool.getIdsFromPath(shortestpathedges, ids, infralinfaces,reverseinfralinfaces)
                        pathids = pathtool.getIdsFromPath(shortestpathedges, ids, infralinfaces, reverseinfralinfaces)
                        if  debug: self.logger.debug('subgraph path ids : %s', str(pathids))
                        #reverse list of not from amaont to aval
                        if not shortestpathedges[0:2] in infralinfaces.tolist():
                            shortestpathedgesreversed = shortestpathedges[::-1]
                            #id = self.windowdialog.pathtool.getIdsFromPath(shortestpathedgesreversed, ids, infralinfaces,reverseinfralinfaces)

                            pathids = pathtool.getIdsFromPath(shortestpathedgesreversed, ids, infralinfaces,reverseinfralinfaces)



                        #if self.reporttype == 'Infrastructure lineaire':
                        if self.atlasconfData['ordering'].split(';')[0] == 'autopath' :
                            orderedids[zonegeoid] += list(pathids[:, 0])

                        # else:
                        elif self.atlasconfData['ordering'].split(';')[0] == 'autoalongpath' :
                            geom = pathtool.getGeomFromIds(pathids)

                            datas = pathtool.getOrderedProjectedIds(geomprojection=geom,
                                                                    geomprojectionids=list(pathids[:, 0]),
                                                                    layertoproject=coveragelayer,
                                                                    constraint=self.atlasconfData['ordering'].split(';')[1])

                            # print('ids infralin',list(pathids[:, 0]) )
                            # print('datas', datas)
                            res = [int(id) for id in datas['id']]
                            # print('res',zonegeoid, res)
                            # orderedids += res
                            orderedids[zonegeoid] += res


                        if False:
                            if self.reporttype == 'Desordres':
                                #geom = self.windowdialog.pathtool.getGeomFromIds(id)
                                geom = pathtool.getGeomFromIds(id)



                                #datas = self.windowdialog.pathtool.getGraphData(geom,list(id[:,0]),'desordre', 'Profil')
                                datas = pathtool.getGraphData(geomprojection=geom,
                                                              geomprojectionids=list(id[:, 0]),
                                                              datatype='desordre',
                                                              datasql='',
                                                              graphtype='Profillong')

                                res = [int(id) for id in datas['desordre']['id']]
                                #orderedids += res
                                orderedids[zonegeoid] += res

                            elif self.reporttype == 'Equipements hydrauliques':
                                # geom = self.windowdialog.pathtool.getGeomFromIds(id)
                                # datas = self.windowdialog.pathtool.getGraphData(geom,list(id[:,0]),'equipement_hydraulique', 'Profil')

                                geom = pathtool.getGeomFromIds(id)
                                datas = pathtool.getGraphData(geom,list(id[:,0]),'equipement_hydraulique', 'Profillong')

                                res = [int(id) for id in datas['equipement']['id']]
                                # orderedids += res
                                orderedids[zonegeoid] += res

        return orderedids



    def initPrinterAndPainter(self,newComposition,atlas):
        """
        initialise le self.priner et le self.painter pour accuilir l'impression
        retourne un QgsLayoutExporter pour qgis3 sinon None
        :param newComposition: la composition de travail
        :param atlas: l'alas de la composition de travail
        :return: QgsLayoutExporter pour qgis3 sinon None
        """
        debug = False
        exporter = None
        if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
            newComposition.setUseAdvancedEffects(False)
            atlas.beginRender()
            if self.parentprintPDFworker is None:
                newComposition.beginPrintAsPDF(self.printer, self.pdffile)
                printReady = self.painter.begin(self.printer)
                if debug: self.logger.debug('print ready %s', printReady)
        else:
            atlas.beginRender()
            exporter = qgis.core.QgsLayoutExporter(newComposition)
            settings = qgis.core.QgsLayoutExporter.PdfExportSettings()
            printsettings = qgis.core.QgsLayoutExporter.PrintExportSettings()



            if self.parentprintPDFworker is None:
                # newComposition.beginPrintAsPDF(self.printer, self.pdffile)

                # equivalent for beginPrintAsPDF
                """
                printer.setOutputFormat(QPrinter::PdfFormat );
                printer.setOutputFileName(file);
                printer.setPaperSize(QSizeF(paperWidth(), paperHeight()), QPrinter::Millimeter );
                """
                self.printer.setOutputFormat(QPrinter.PdfFormat)
                self.printer.setOutputFileName(self.pdffile)
                paperWidth = newComposition.pageCollection().page(0).pageSize().width()
                paperHeight = newComposition.pageCollection().page(0).pageSize().height()
                if debug: self.logger.debug('print size %s %s', str(paperWidth), str(paperHeight))
                self.printer.setPaperSize(QtCore.QSizeF(paperWidth, paperHeight), QPrinter.Millimeter)
                self.printer.setFullPage(True)

                printReady = self.painter.begin(self.printer)
                if debug: self.logger.debug('print ready %s', printReady)


        return exporter

    def setGeneralMapExtentByZonegeo(self, newComposition, zonegeoid):
        """
        Adapte le zoom de la carte générale en fonction de la zonegeo en cours
        :param newComposition: la composition en cours d'utilisation
        :param zonegeoid: l'id de la zone geo en cours de traitement
        """
        for mapname in self.atlasconfData['generalmap'].keys():
            pkzonegeofet = self.dbase.getLayerFeatureById('Zonegeo', zonegeoid).id()
            if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                zonegeofet = self.dbase.dbasetables['Zonegeo']['layerqgis'].getFeatures(qgis.core.QgsFeatureRequest(pkzonegeofet)).next()
                layerext = zonegeofet.geometry().boundingBox()
                layerext = layerext.buffer(layerext.height() / 10.0)
            else:
                zonegeofet = self.dbase.dbasetables['Zonegeo']['layerqgis'].getFeatures(qgis.core.QgsFeatureRequest(pkzonegeofet)).__next__()
                layerext = zonegeofet.geometry().boundingBox()
                layerext = layerext.buffered(layerext.height() / 10.0)
            layerextgeom = qgis.core.QgsGeometry.fromRect(layerext)
            layerextgeomcanvas = layerextgeom.transform(self.dbase.xform)
            layerextgeomcanvasfinal = layerextgeom.boundingBox()
            if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                newComposition.getComposerItemById(mapname).zoomToExtent(layerextgeomcanvasfinal)
            else:
                temp1 = newComposition.itemById(mapname)
                #temp1.__class__ = qgis.core.QgsLayoutItemMap
                temp1.zoomToExtent(layerextgeomcanvasfinal)

            # set min scale
            minscale = 0
            for atlasmapitem in self.atlasconfData['atlasdrivemap'].keys():
                if self.atlasconfData['atlasdrivemap'][atlasmapitem]['minscale'] > minscale:
                    minscale = self.atlasconfData['atlasdrivemap'][atlasmapitem]['minscale']
            if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                if newComposition.getComposerItemById(mapname).scale() < minscale * 5.0:
                    newComposition.getComposerItemById(mapname).setNewScale(minscale * 5.0)
            else:
                if newComposition.itemById(mapname).scale() < minscale * 5.0:
                    newComposition.itemById(mapname).setNewScale(minscale * 5.0)








    def printAtlasPage(self,newComposition,exporter, indexpagetotal, indexpage, idecalage):
        """
        Realise l'impression de la composition sur pdf
        Dans le cas de childprint, appele le printPDFBaseWorker chargé de faire l'impression des childs
        :param newComposition: la compostion en cours
        :param exporter: utile pour qgis3
        :param indexpage: index de la page en cours d'edition
        :param idecalage: iterateur utilisé dans le childprint pour décaler l'impression
        :return:
        """
        if int(str(self.dbase.qgisversion_int)[0:3]) > 220:
            printsettings = qgis.core.QgsLayoutExporter.PrintExportSettings()

        if self.parentprintPDFworker is None:
            if indexpagetotal > 0:
                self.printer.newPage()
            if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                newComposition.doPrint(self.printer, self.painter)
            else:
                # newComposition.doPrint(self.printer, self.painter)
                exporter.renderPage(self.painter, 0)
                eval('exporter.print(self.printer, printsettings )')
        else:
            # print('height', self.parentheightpx,selfheightpx , self.painter.device().height())
            # selfheightpx = newComposition.compositionBounds().height()/ 25.4 * 96 * 1.08
            pageheightmm = self.printer.paperRect(QPrinter.Millimeter).height()

            if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                selfheightpx = newComposition.compositionBounds().height() / pageheightmm * self.painter.device().height()
            else:
                selfheightpx = newComposition.layoutBounds().height() / pageheightmm * self.painter.device().height()

            verticalpositionpx = self.currentpageheightpx + (indexpage - self.idecalage + 1) * selfheightpx
            #verticalpositionpx = self.parentprintPDFworker.heightpx + (indexpage - idecalage + 1) * selfheightpx
            # print('temp', self.idparent,verticalpositionpx, self.painter.device().height() )
            # print(self.currentpageheightpx, indexpage, self.idecalage)
            # print(selfheightpx, verticalpositionpx, self.painter.device().height())

            if verticalpositionpx > self.painter.device().height():
                # print('***************************************************** attention *****************************')
                self.printer.newPage()
                self.currentpageheightpx = 0
                self.idecalage = indexpage


            self.painter.translate(0, self.currentpageheightpx + (indexpage - self.idecalage) * selfheightpx)
            if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                newComposition.doPrint(self.printer, self.painter)
            else:
                exporter.renderPage(self.painter, 0)

                beforeheight, beforewidth = self.printer.paperRect(QPrinter.Millimeter).height(),self.printer.paperRect(QPrinter.Millimeter).width()
                eval('exporter.print(self.printer, printsettings )')
                self.printer.setPaperSize(QtCore.QSizeF(beforewidth, beforeheight), QPrinter.Millimeter)
                self.printer.setFullPage(True)

            self.painter.translate(0, -self.currentpageheightpx - (indexpage - self.idecalage) * selfheightpx)

        # childprint
        if True:
            #if 'childprint' in reportdic.keys():
            # print('self.atlasconfData[childprin].keys()',self.atlasconfData['childprint'].keys())
            if len(self.atlasconfData['childprint'].keys()) > 0:
                """
                # parentheight = newComposition.getComposerItemById('parentheight').rectWithFrame().height()
                # pour A4
                # print('paperSize()' , self.printer.paperRect(QPrinter.Millimeter).height())
                parentheightmm = newComposition.getComposerItemById('parentheight').rectWithFrame().height()
                pageheightmm = self.printer.paperRect(QPrinter.Millimeter).height()
                parentheightpx = int(parentheightmm / pageheightmm * self.painter.device().height())
                # height = height(mm)/(inchtomm) * resolution *1.08
                # parentheightpx = parentheight / 25.4 * 96 * 1.08
                """

                childrapport = self.__class__(dbase=self.dbase,
                                                  windowdialog=self.windowdialog,
                                                  parentprintPDFworker=self)


                childrapport.work()




    def getPhoto(self,reportdic, feat):
        # print('getPhoto')
        resfile = None
        #print([field.name() for field in reportdic['atlaslayer'].fields()])
        #if 'lk_photo' in [field.name() for field in reportdic['atlaslayer'].fields()]:
        if 'lk_photo' in self.dbase.dbasetables[reportdic['dbasename']]['fields'].keys():
            sql = "SELECT lk_photo FROM " + reportdic['dbasename']
            sql += " WHERE id_" + reportdic['dbasename']  + " = " + str(feat.id())
            # print(sql)
            query = self.dbase.query(sql)
            result = [row for row in query]
            # print('reslkphoto', result)
            #lkphoto = feat['lk_photo']
            # print('getPhoto',lkphoto )
            #if not self.dbase.isAttributeNull(lkphoto):
            if len(result) > 0 and not self.dbase.isAttributeNull(result[0][0]):
                sql = "SELECT Ressource.file FROM Photo INNER JOIN Ressource ON Photo.id_ressource = Ressource.id_ressource WHERE Photo.id_objet = "
                #sql += str(feat['lk_photo'])
                sql += str(result[0][0])
                query = self.dbase.query(sql)
                result = [row for row in query]
                filephoto = result[0][0]
                # print(filephoto)
                resfile = self.dbase.completePathOfFile(filephoto)
        if resfile is None:
            """
            sql = "SELECT Ressource.file FROM " + reportdic['dbasename']
            sql += " INNER JOIN Objet ON Objet.id_objet = " + reportdic['dbasename'] + ".id_objet"
            sql += " INNER JOIN Tcobjetressource ON Tcobjetressource.id_tcobjet = Objet.id_objet"
            sql += " INNER JOIN Ressource ON Tcobjetressource.id_tcressource = Ressource.id_ressource"
            sql += " INNER JOIN Photo ON Photo.id_ressource = Ressource.id_ressource"
            sql += " WHERE "+ reportdic['dbasename'] + ".id_objet = " + str(feat['id_objet'])
            #print(sql)
            query = self.dbase.query(sql)
            result = [row for row in query]
            # print(result)
            #resfile = result[0][0]
            if len(result)>0:
                resfile = self.dbase.completePathOfFile(result[0][0])
            """
            resfile = self.getNumberedPhoto(reportdic, feat, 1)

        return resfile



    def getNumberedPhoto(self, atlasfeat, table, photoid):
        # print('getNumberedPhoto', photoid)
        debug = False

        resfile = None

        if False:
            reportdic={}
            feat = None
            sql = "SELECT Ressource.file FROM " + reportdic['dbasename']
            sql += " INNER JOIN Objet ON Objet.id_objet = " + reportdic['dbasename'] + ".id_objet"
            sql += " INNER JOIN Tcobjetressource ON Tcobjetressource.id_tcobjet = Objet.id_objet"
            sql += " INNER JOIN Ressource ON Tcobjetressource.id_tcressource = Ressource.id_ressource"
            sql += " INNER JOIN Photo ON Photo.id_ressource = Ressource.id_ressource"
            sql += " WHERE " + reportdic['dbasename'] + ".id_objet = " + str(feat['id_objet'])

        if False:
            sql = ' WITH tempquery AS ('
            sql += self.atlasconfData['atlaslayersql']
            sql += ' AND '
            sql += self.dbase.dateVersionConstraintSQL()
            if False and self.parentprintPDFworker is not None:
                sql += ' AND ' + self.parentprintPDFworker.atlasconfData['childprint']['linkcolumn']
                sql += ' = ' + str(self.parentprintPDFworker.currentid)
                sql += ' ' + self.parentprintPDFworker.atlasconfData['childprint']['optionsql']
            sql += '), Ressourcetemp AS( '
            sql += " SELECT Ressource.id_ressource, file FROM Ressource "
            sql += " INNER JOIN Photo ON Photo.lpk_ressource = Ressource.pk_ressource "
            sql+=  "WHERE Photo.typephoto = 'PHO') "
            sql += " SELECT file  FROM Ressourcetemp, tempquery "
            sql += " INNER JOIN Tcobjetressource ON lid_ressource = id_ressource "
            sql += " WHERE id_objet = lid_objet "
            #sql += ' AND ' + self.atlasconfData['atlaslayerid'] + ' = ' + str(atlasfeat.id())
            sql += ' AND ' + self.atlasconfData['atlaslayerid'] + ' = ' + str(atlasfeat[self.atlasconfData['atlaslayerid']])
            if debug: self.logger.debug('sql  %s', str(sql))
            query = self.dbase.query(sql)
            result = [row for row in query]

        if True:
            #get id_objet
            tempsplittedquery = self.dbase.splitSQLSelectFromWhereOrderby(self.atlasconfData['atlaslayersql'])
            tempsplittedquery['SELECT'] = table + '.id_objet '
            if 'WHERE' in tempsplittedquery.keys():
                tempsplittedquery['WHERE'] += ' AND ' + self.atlasconfData['atlaslayerid'] + ' = ' + str(atlasfeat.id())
            else:
                tempsplittedquery['WHERE'] = self.atlasconfData['atlaslayerid'] + ' = ' + str(atlasfeat.id())
            # tempsplittedquery['FROM'] = table
            sql = self.dbase.rebuildSplittedQuery(tempsplittedquery)
            sql = self.dbase.updateQueryTableNow(sql)
            query = self.dbase.query(sql)
            idobjet = [row[0] for row in query][0]

            sql = "SELECT file FROM Ressource_now INNER JOIN Tcobjetressource ON lid_ressource = id_ressource"
            sql += " WHERE Tcobjetressource.lid_objet = " + str(idobjet)
            sql = self.dbase.updateQueryTableNow(sql)
            query = self.dbase.query(sql)
            result = [row for row in query]





        #print(result)
        # resfile = result[0][0]
        if len(result) > (photoid -1):
            resfile = self.dbase.completePathOfFile(result[photoid -1][0])
            #print('photo', sql)
            # print(resfile)
        if debug: self.logger.debug('resfile  %s', str(resfile))
        return resfile




    def getNumberedPhoto2(self, atlasfeat, photoid):
        # print('getNumberedPhoto', photoid)
        debug = False

        resfile = None

        if False:
            reportdic={}
            feat = None
            sql = "SELECT Ressource.file FROM " + reportdic['dbasename']
            sql += " INNER JOIN Objet ON Objet.id_objet = " + reportdic['dbasename'] + ".id_objet"
            sql += " INNER JOIN Tcobjetressource ON Tcobjetressource.id_tcobjet = Objet.id_objet"
            sql += " INNER JOIN Ressource ON Tcobjetressource.id_tcressource = Ressource.id_ressource"
            sql += " INNER JOIN Photo ON Photo.id_ressource = Ressource.id_ressource"
            sql += " WHERE " + reportdic['dbasename'] + ".id_objet = " + str(feat['id_objet'])

        if False:
            sql = ' WITH tempquery AS ('
            sql += self.atlasconfData['atlaslayersql']
            sql += ' AND '
            sql += self.dbase.dateVersionConstraintSQL()
            if False and self.parentprintPDFworker is not None:
                sql += ' AND ' + self.parentprintPDFworker.atlasconfData['childprint']['linkcolumn']
                sql += ' = ' + str(self.parentprintPDFworker.currentid)
                sql += ' ' + self.parentprintPDFworker.atlasconfData['childprint']['optionsql']
            sql += '), Ressourcetemp AS( '
            sql += " SELECT Ressource.id_ressource, file FROM Ressource "
            sql += " INNER JOIN Photo ON Photo.lpk_ressource = Ressource.pk_ressource "
            sql+=  "WHERE Photo.typephoto = 'PHO') "
            sql += " SELECT file  FROM Ressourcetemp, tempquery "
            sql += " INNER JOIN Tcobjetressource ON lid_ressource = id_ressource "
            sql += " WHERE id_objet = lid_objet "
            #sql += ' AND ' + self.atlasconfData['atlaslayerid'] + ' = ' + str(atlasfeat.id())
            sql += ' AND ' + self.atlasconfData['atlaslayerid'] + ' = ' + str(atlasfeat[self.atlasconfData['atlaslayerid']])

        if True:
            pass


        if debug: self.logger.debug('sql  %s', str(sql))
        query = self.dbase.query(sql)
        result = [row for row in query]
        #print(result)
        # resfile = result[0][0]
        if len(result) > (photoid -1):
            resfile = self.dbase.completePathOfFile(result[photoid -1][0])
            #print('photo', sql)
            # print(resfile)
        if debug: self.logger.debug('resfile  %s', str(resfile))
        return resfile





    def getNumberedRessource(self, atlasfeat, table,  photoid):

        debug = False

        resfile = None

        if False:
            sql = ' WITH tempquery AS ('
            sql += self.atlasconfData['atlaslayersql']
            sql += ' AND '
            sql += self.dbase.dateVersionConstraintSQL()
            if self.parentprintPDFworker is not None:
                sql += ' AND ' + self.parentprintPDFworker.atlasconfData['childprint']['linkcolumn']
                sql += ' = ' + str(self.parentprintPDFworker.currentid)
                sql += ' ' + self.parentprintPDFworker.atlasconfData['childprint']['optionsql']
            sql += '), Ressourcetemp AS( '
            sql += " SELECT Ressource.id_ressource, file FROM Ressource "
            sql+=  ") "
            sql += " SELECT file  FROM Ressourcetemp, tempquery "
            #sql += " INNER JOIN Tcobjetressource ON id_tcressource = id_ressource "
            sql += " INNER JOIN Tcobjetressource ON lid_ressource = id_ressource "
            # sql += " WHERE id_objet = id_tcobjet "
            sql += " WHERE id_objet = lid_objet "
            sql += ' AND '
            # sql += 'id_ressource = ' + str(str(atlasfeat['lk_ressource' + str(photoid)]))
            sql += 'id_ressource = ' + str(str(atlasfeat['lid_ressource_' + str(photoid)]))
            if debug: self.logger.debug('sql  %s %s', str(photoid), str(sql))
            query = self.dbase.query(sql)
            result = [row for row in query]
        if True:

            tempsplittedquery = self.dbase.splitSQLSelectFromWhereOrderby(self.atlasconfData['atlaslayersql'])
            tempsplittedquery['SELECT'] = table + '.lid_ressource_' + str(photoid)
            if 'WHERE' in tempsplittedquery.keys():
                tempsplittedquery['WHERE'] += ' AND ' + self.atlasconfData['atlaslayerid'] + ' = ' + str(atlasfeat.id())
            else:
                tempsplittedquery['WHERE'] = self.atlasconfData['atlaslayerid'] + ' = ' + str(atlasfeat.id())
            # tempsplittedquery['FROM'] = table
            sql = self.dbase.rebuildSplittedQuery(tempsplittedquery)
            sql = self.dbase.updateQueryTableNow(sql)

            query = self.dbase.query(sql)
            idressource = [row[0] for row in query][0]

            if not self.dbase.isAttributeNull(idressource):
                sql = "SELECT file FROM Ressource_now WHERE id_ressource = " + str(idressource)
                sql = self.dbase.updateQueryTableNow(sql)
                query = self.dbase.query(sql)
                result = [row for row in query]

                # print(result)
                if len(result)>0:
                    resfile = self.dbase.completePathOfFile( result[0][0] )


                if False and len(result) > (photoid -1):
                    resfile = self.dbase.completePathOfFile(result[photoid -1][0])
                    # print(resfile)
                if debug: self.logger.debug('resfile  %s', str(resfile))
        return resfile


    def getNumberedRessource2(self, atlasfeat, photoid):

        debug = False

        resfile = None

        if False:
            sql = ' WITH tempquery AS ('
            sql += self.atlasconfData['atlaslayersql']
            sql += ' AND '
            sql += self.dbase.dateVersionConstraintSQL()
            if self.parentprintPDFworker is not None:
                sql += ' AND ' + self.parentprintPDFworker.atlasconfData['childprint']['linkcolumn']
                sql += ' = ' + str(self.parentprintPDFworker.currentid)
                sql += ' ' + self.parentprintPDFworker.atlasconfData['childprint']['optionsql']
            sql += '), Ressourcetemp AS( '
            sql += " SELECT Ressource.id_ressource, file FROM Ressource "
            sql+=  ") "
            sql += " SELECT file  FROM Ressourcetemp, tempquery "
            #sql += " INNER JOIN Tcobjetressource ON id_tcressource = id_ressource "
            sql += " INNER JOIN Tcobjetressource ON lid_ressource = id_ressource "
            # sql += " WHERE id_objet = id_tcobjet "
            sql += " WHERE id_objet = lid_objet "
            sql += ' AND '
            # sql += 'id_ressource = ' + str(str(atlasfeat['lk_ressource' + str(photoid)]))
            sql += 'id_ressource = ' + str(str(atlasfeat['lid_ressource_' + str(photoid)]))
            if debug: self.logger.debug('sql  %s %s', str(photoid), str(sql))
            query = self.dbase.query(sql)
            result = [row for row in query]
        if True:
            idressource = atlasfeat['lid_ressource_' + str(photoid)]
            sql = "SELECT file FROM Ressource_now WHERE id_ressource = " + str(idressource)
            sql = self.dbase.updateQueryTableNow(sql)
            query = self.dbase.query(sql)
            result = [row for row in query]


        # print(result)
        if len(result)>0:
            resfile = self.dbase.completePathOfFile( result[0][0] )


        if False and len(result) > (photoid -1):
            resfile = self.dbase.completePathOfFile(result[photoid -1][0])
            # print(resfile)
        if debug: self.logger.debug('resfile  %s', str(resfile))
        return resfile



    def setLoadingProgressBar(self, progressbar, val):
        if progressbar is not None:
            progressbar.setValue(val)
        else:
            if self.dbase.qgsiface is None:
                logging.getLogger('Lamia').info('Generation du pdf %d', val )
        QApplication.processEvents()