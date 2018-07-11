# -*- coding: utf-8 -*-

import qgis
import os
import re
import logging
# from ..toolabstract.inspectiondigue_abstractworker import AbstractWorker
from qgis.PyQt import QtGui, uic, QtCore, QtXml
try:
    from qgis.PyQt.QtGui import QPrinter
    from qgis.PyQt.QtGui import QProgressBar, QApplication
    #except ImportError:
except ImportError as e:
    from qgis.PyQt.QtPrintSupport import QPrinter
    from qgis.PyQt.QtWidgets import  QProgressBar, QApplication
from ...libs import pyqtgraph as pg
import networkx
import numpy as np
from collections import OrderedDict

from .rapporttools.InspectionDigue_impression_rapport import ImpressionRapportDialog


# class printPDFWorker(AbstractWorker):
class printPDFBaseWorker(object):

    def __init__(self,
                 dbase,
                 windowdialog,
                 # project = None,
                 # canvas = None,
                 reporttype = None,
                 pdffile = None,
                 printer=None,
                 painter=None,
                 idparent=None,
                 parentheightpx=None):
        #AbstractWorker.__init__(self)

        self.dbase = dbase
        self.windowdialog = windowdialog
        self.project = qgis.core.QgsProject.instance()
        self.canvas = self.dbase.canvas
        self.reporttype = reporttype
        self.pdffile = pdffile
        
        self.printrapportdialog = ImpressionRapportDialog()

        lauchaction = QtGui.QAction(QtGui.QIcon(), 'Impression rapport',self.windowdialog.menuPreferences)
        lauchaction.triggered.connect(self.launchDialog)
        self.windowdialog.menuOutils.addAction(lauchaction)
        
        
        
        self.logger = logging.getLogger("Lamia")




        if printer is None:
            self.printer = QPrinter()

            self.painter = QtGui.QPainter()
            self.idparent = None
            self.parentheightpx = None
        else:
            self.printer = printer
            self.painter = painter
            self.idparent = idparent
            self.parentheightpx = parentheightpx



        self.reportdict={}

        self.postInit()


        
    def launchDialog(self,reporttype=None, pdffile=None):
        # def printRapport(self, reporttype=None, pdffile=None):
        if reporttype is None or pdffile is None:
            self.printrapportdialog.exec_()
            reporttype, pdffile = self.printrapportdialog.dialogIsFinished()
            # print(reporttype, pdffile)

        if reporttype is not None and pdffile is not None and pdffile != '':
            if False:
                self.worker = printPDFWorker(self.dbase, qgis.core.QgsProject.instance(), self.canvas, reporttype,
                                             pdffile, self)
                self.thread = QtCore.QThread()
                self.worker.moveToThread(self.thread)
                self.worker.finished.connect(self.exportPDFFinished)
                self.worker.error.connect(self.printError)
                self.worker.message.connect(self.printMessage)
                self.worker.finished.connect(self.exportPDFFinished)
                self.worker.finished.connect(self.worker.deleteLater)
                self.thread.finished.connect(self.thread.deleteLater)
                self.worker.finished.connect(self.thread.quit)

                self.thread.started.connect(self.worker.run)

                self.thread.start()
            if False:
                self.worker = printPDFWorker(self.dbase, qgis.core.QgsProject.instance(), self.canvas, reporttype,
                                             pdffile, self)
                self.worker.finished.connect(self.exportPDFFinished)
                self.worker.error.connect(self.printError)
                self.worker.message.connect(self.printMessage)
                self.worker.run()
            if True:
                # self.worker = printPDFWorker(self.dbase, qgis.core.QgsProject.instance(), self.canvas, reporttype, pdffile, self)

                self.pdffile = pdffile
                self.reporttype = reporttype

                self.work()


        


    def postInit(self):

        # ****************************  Infralineaire *****************************************************

        sql = "SELECT Infralineaire.*,"
        sql += " Objet.datecreation, Objet.datedestruction, Objet.commentaire, Objet.libelle, "
        sql += "Descriptionsystem.importancestrat, Descriptionsystem.etatfonct, Descriptionsystem.datederniereobs, Descriptionsystem.qualitegeoloc, Descriptionsystem.parametres, Descriptionsystem.listeparametres"
        sql += " FROM Infralineaire INNER JOIN Descriptionsystem ON Infralineaire.id_descriptionsystem = Descriptionsystem.id_descriptionsystem "
        sql += "INNER JOIN Objet ON Objet.id_objet = Infralineaire.id_objet"

        sql += '  WHERE Objet.Datecreation <= ' + "'" + self.dbase.workingdate + "'"
        if self.dbase.dbasetype == 'postgis':
            sql += ' AND CASE WHEN Objet.Datedestruction IS NOT NULL  '
            sql += 'THEN Objet.DateDestruction > ' + "'" + self.dbase.workingdate + "'" + ' ELSE TRUE END'
        elif self.dbase.dbasetype == 'spatialite':
            sql += ' AND CASE WHEN Objet.datedestruction IS NOT NULL  '
            sql += 'THEN Objet.dateDestruction > ' + "'" + self.dbase.workingdate + "'" + ' ELSE 1 END'
        sql += "&uid=id_infralineaire"
        #print(sql)

        atlaslayer = qgis.core.QgsVectorLayer("?query=" + sql, "myvlayer", "virtual")

        self.reportdict['Infrastructure lineaire'] = {'qptfile': 'Infralineaire',
                                                      'dbasename':'Infralineaire',
                                                      'atlaslayer': atlaslayer,
                                                      #'specialstyledlayer' : self.dbase.dbasetables['Infralineaire']['layerqgis'],
                                                      'atlaslayerstyle': 'Infralineaire_atlas.qml',
                                                      'atlasdriven': ['map1'],
                                                      'atlasdrivenminscale' : 2500,
                                                      #'atlastypescale' : qgis.core.QgsComposerMap.Auto,
                                                      'atlastypescale': 'Auto',
                                                      'generalmap': ['map0'],
                                                      'layers': {'map0': [self.dbase.dbasetables['Infralineaire']['layerqgis'],
                                                                          'scan25'],
                                                                 #'map1': [self.dbase.dbasetables['Infralineaire']['layerqgis'],
                                                                 'map1': ['atlaslayer',
                                                                         self.dbase.dbasetables['Equipement']['layerqgis'],
                                                                         'ortho']},
                                                      'images':{'graph' : 'profile',
                                                                'profiltravers' : 'profiltravers',
                                                                'photo' : 'photo',
                                                                'logo':'logo'}
                                                      }

        # ****************************  Equipements hydrauliques *****************************************************

        sql = "SELECT Equipement.*,"
        sql += " Objet.datecreation, Objet.datedestruction, Objet.commentaire, Objet.libelle, "
        sql += "Descriptionsystem.importancestrat, Descriptionsystem.etatfonct, Descriptionsystem.datederniereobs, Descriptionsystem.qualitegeoloc, Descriptionsystem.parametres, Descriptionsystem.listeparametres"
        sql += " FROM Equipement INNER JOIN Descriptionsystem ON Equipement.id_descriptionsystem = Descriptionsystem.id_descriptionsystem "
        sql += "INNER JOIN Objet ON Objet.id_objet = Equipement.id_objet"
        sql += " WHERE ( Equipement.categorie = 'RHF' or Equipement.categorie = 'RHO' or Equipement.categorie = 'OUH')"
        # sql += " AND Equipement.lk_equipement IS NULL"

        sql += ' AND  Objet.Datecreation <= ' + "'" + self.dbase.workingdate + "'"
        if self.dbase.dbasetype == 'postgis':
            sql += ' AND CASE WHEN Objet.Datedestruction IS NOT NULL  '
            sql += 'THEN Objet.DateDestruction > ' + "'" + self.dbase.workingdate + "'" + ' ELSE TRUE END'
        elif self.dbase.dbasetype == 'spatialite':
            sql += ' AND CASE WHEN Objet.datedestruction IS NOT NULL  '
            sql += 'THEN Objet.dateDestruction > ' + "'" + self.dbase.workingdate + "'" + ' ELSE 1 END'
        sql += "&uid=id_equipement"
        # print(sql)

        atlaslayer = qgis.core.QgsVectorLayer("?query=" + sql, "myvlayer", "virtual")


        if False:

            for fet in atlaslayer.getFeatures():
                print(fet.attributes())
                print(fet.id())
            print([fiel.name() for fiel in atlaslayer.fields()])


        self.reportdict['Equipements hydrauliques'] = {'qptfile': 'Equipement_hydraulique',
                                                       'dbasename': 'Equipement',
                                                       'atlaslayer': atlaslayer,
                                                       #'expression':'lk_equipement = NULL and (categorie=RHO or categorie=RHF or categorie=RHF or categorie = OUH)',
                                                       'atlaslayerstyle': 'Equipement_atlas.qml',
                                                       'atlasdriven': ['map1'],
                                                       'atlasdrivenminscale': 2000,
                                                       # 'atlastypescale': qgis.core.QgsComposerMap.Auto,
                                                       'atlastypescale': 'Auto',
                                                       'generalmap': ['map0'],
                                                       'layers':{'map0': [self.dbase.dbasetables['Infralineaire']['layerqgis'],
                                                                          'scan25'],
                                                                'map1': ['atlaslayer',
                                                                         self.dbase.dbasetables['Infralineaire']['layerqgis'],
                                                                         'ortho']},
                                                       'images':{'photo1': 'photo'},
                                                       'childprint':  "Equipements hydrauliques annexes"
                                                       }


        # ****************************  Equipements hydrauliques annexes *****************************************************

        sql = "SELECT Equipement.*,"
        sql += " Objet.datecreation, Objet.datedestruction, Objet.commentaire, Objet.libelle, "
        sql += "Descriptionsystem.importancestrat, Descriptionsystem.etatfonct, Descriptionsystem.datederniereobs, Descriptionsystem.qualitegeoloc, Descriptionsystem.parametres, Descriptionsystem.listeparametres"
        sql += " FROM Equipement INNER JOIN Descriptionsystem ON Equipement.id_descriptionsystem = Descriptionsystem.id_descriptionsystem "
        sql += "INNER JOIN Objet ON Objet.id_objet = Equipement.id_objet"
        sql += " WHERE ( Equipement.categorie = 'RHF' or Equipement.categorie = 'RHO' or Equipement.categorie = 'OUH')"
        if self.idparent is not None:
            sql += " AND Equipement.lk_equipement = " + str(self.idparent)

        sql += '  AND  Objet.Datecreation <= ' + "'" + self.dbase.workingdate + "'"
        if self.dbase.dbasetype == 'postgis':
            sql += ' AND CASE WHEN Objet.Datedestruction IS NOT NULL  '
            sql += 'THEN Objet.DateDestruction > ' + "'" + self.dbase.workingdate + "'" + ' ELSE TRUE END'
        elif self.dbase.dbasetype == 'spatialite':
            sql += ' AND CASE WHEN Objet.datedestruction IS NOT NULL  '
            sql += 'THEN Objet.dateDestruction > ' + "'" + self.dbase.workingdate + "'" + ' ELSE 1 END'
        sql += "&uid=id_equipement"
        # print(sql)

        atlaslayer = qgis.core.QgsVectorLayer("?query=" + sql, "myvlayer", "virtual")


        if False:

            for fet in atlaslayer.getFeatures():
                print(fet.attributes())
                print(fet.id())
            print([fiel.name() for fiel in atlaslayer.fields()])


        self.reportdict['Equipements hydrauliques annexes'] = {'qptfile': 'Equipement_hydraulique_annexe',
                                                       'dbasename': 'Equipement',
                                                       'atlaslayer': atlaslayer,
                                                       #'expression':'lk_equipement = NULL and (categorie=RHO or categorie=RHF or categorie=RHF or categorie = OUH)',
                                                       'atlaslayerstyle': 'Equipement.qml',
                                                       'atlasdriven': [],
                                                       'atlasdrivenminscale': 2000,
                                                       # 'atlastypescale': qgis.core.QgsComposerMap.Auto,
                                                       'atlastypescale': 'Auto',
                                                       'generalmap': [],
                                                       'layers':{},
                                                       'images':{'photo1': 'photo'},
                                                       }



        # ****************************  Desordres *****************************************************

        """
        if self.dbase.dbasetype == 'spatialite':
            sql = "SELECT Observation.*, Desordre.*, Objet.*,  MAX(Observation.dateobservation)  FROM Observation "
            sql += "INNER JOIN Desordre ON Desordre.id_desordre = Observation.lk_desordre "
            #sql += "INNER JOIN Observation ON Desordre.id_desordre = Observation.lk_desordre "
            sql += "INNER JOIN Objet ON Objet.id_objet = Observation.id_objet "
            sql += "GROUP BY Observation.lk_desordre"
        elif self.dbase.dbasetype == 'postgis':
            pass
        """
        sql = " SELECT Desordre.*, Objet.* FROM Desordre INNER JOIN Objet ON Objet.id_objet = Desordre.id_objet"

        sql += '  WHERE  Objet.Datecreation <= ' + "'" + self.dbase.workingdate + "'"
        if self.dbase.dbasetype == 'postgis':
            sql += ' AND CASE WHEN Objet.Datedestruction IS NOT NULL  '
            sql += 'THEN Objet.DateDestruction > ' + "'" + self.dbase.workingdate + "'" + ' ELSE TRUE END'
        elif self.dbase.dbasetype == 'spatialite':
            sql += '  AND CASE WHEN Objet.datedestruction IS NOT NULL  '
            sql += 'THEN Objet.dateDestruction > ' + "'" + self.dbase.workingdate + "'" + ' ELSE 1 END'
        sql += "&uid=id_desordre"
        # print(sql)

        atlaslayer = qgis.core.QgsVectorLayer("?query=" + sql, "myvlayer", "virtual")

        if False:

            for fet in atlaslayer.getFeatures():
                print(fet.attributes())
                print(fet.id())
            print([fiel.name() for fiel in atlaslayer.fields()])

        self.reportdict['Desordre'] = {'qptfile': 'Desordres',
                                                      'dbasename':'Desordre',
                                                      'atlaslayer': atlaslayer,
                                                      #'specialstyledlayer' : self.dbase.dbasetables['Infralineaire']['layerqgis'],
                                                      'atlaslayerstyle': 'Desordre_atlas.qml',
                                                      'atlasdriven': ['map1'],
                                                      'atlasdrivenminscale' : 2500,
                                                      # 'atlastypescale': qgis.core.QgsComposerMap.Predefined,
                                                         'atlastypescale': 'Predefined',
                                                       #'atlastypescale': qgis.core.QgsComposerMap.Fixed,
                                                      'generalmap': ['map0'],
                                                      'layers': {'map0': [self.dbase.dbasetables['Infralineaire']['layerqgis'],
                                                                          'scan25'],
                                                                 'map1': ['atlaslayer',
                                                                          self.dbase.dbasetables['Infralineaire']['layerqgis'],
                                                                          self.dbase.dbasetables['Equipement']['layerqgis'],
                                                                          'ortho']},
                                                      'images':{
                                                                #'photo1' : 'photo1',
                                                                #'photo2': 'photo2',
                                                                'logo':'logo'},
                                                     'childprint': "Observation"
                                                      }


        # ****************************  Observations *****************************************************

        if self.dbase.dbasetype == 'spatialite':
            sql = "SELECT Observation.*, Desordre.*, Objet.*  FROM Observation "
            sql += "INNER JOIN Desordre ON Desordre.id_desordre = Observation.lk_desordre "
            # sql += "INNER JOIN Observation ON Desordre.id_desordre = Observation.lk_desordre "
            sql += "INNER JOIN Objet ON Objet.id_objet = Observation.id_objet "
            # sql += "GROUP BY Observation.lk_desordre"
        elif self.dbase.dbasetype == 'postgis':
            pass

        sql += '  WHERE  Objet.Datecreation <= ' + "'" + self.dbase.workingdate + "'"
        if self.dbase.dbasetype == 'postgis':
            sql += ' AND CASE WHEN Objet.Datedestruction IS NOT NULL  '
            sql += 'THEN Objet.DateDestruction > ' + "'" + self.dbase.workingdate + "'" + ' ELSE TRUE END'
        elif self.dbase.dbasetype == 'spatialite':
            sql += '  AND CASE WHEN Objet.datedestruction IS NOT NULL  '
            sql += 'THEN Objet.dateDestruction > ' + "'" + self.dbase.workingdate + "'" + ' ELSE 1 END'
        if self.idparent is not None:
            sql += " AND Observation.lk_desordre = " + str(self.idparent)
            sql += " ORDER BY Observation.dateobservation DESC"

        sql += "&uid=id_observation"
        # print(sql)

        atlaslayer = qgis.core.QgsVectorLayer("?query=" + sql, "myvlayer", "virtual")

        if False:

            for fet in atlaslayer.getFeatures():
                print(fet.attributes())
                print(fet.id())
            print([fiel.name() for fiel in atlaslayer.fields()])

        self.reportdict['Observation'] = {'qptfile': 'Observation',
                                       'dbasename': 'Observation',
                                       'atlaslayer': atlaslayer,
                                       # 'specialstyledlayer' : self.dbase.dbasetables['Infralineaire']['layerqgis'],
                                       'atlaslayerstyle': 'Desordre_atlas.qml',
                                       'atlasdriven': [],
                                       'atlasdrivenminscale': 2500,
                                       # 'atlastypescale': qgis.core.QgsComposerMap.Predefined,
                                       'atlastypescale': 'Predefined',
                                       # 'atlastypescale': qgis.core.QgsComposerMap.Fixed,
                                       'generalmap': [],
                                       'layers': {},
                                       'images': {'photo1': 'photo1',
                                                  'photo2': 'photo2',
                                                  'photo3': 'photo3',
                                                  #'logo': 'logo'
                                                  }
                                       }

    def work(self):
        # self.message.emit('newComposition creation')
        if self.dbase.qgsiface is not None:
            debug = False
            stop10 = False
        else:
            debug = True  # True False
            stop10 = True



        if debug : self.logger.debug('started')
        mapsettings = self.canvas.mapSettings()
        layertoremove = []

        # ********************* create composition *****************************
        if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
            newComposition = qgis.core.QgsComposition(mapsettings)
        else:
            newComposition = qgis.core.QgsPrintLayout(self.project)

        if self.reporttype == "Infrastructure lineaire":
            reportdic = self.reportdict['Infrastructure lineaire']
        elif self.reporttype == "Equipements hydrauliques":
            reportdic = self.reportdict['Equipements hydrauliques']
        elif self.reporttype == "Equipements hydrauliques annexes":
            reportdic = self.reportdict['Equipements hydrauliques annexes']
        elif self.reporttype == "Desordres":
            reportdic = self.reportdict['Desordre']
        elif self.reporttype == "Observation":
            reportdic = self.reportdict['Observation']

        if debug : self.logger.debug('type %s %s', str(self.reporttype),str(self.idparent))

        # ********************* Load template *****************************
        if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
            templatepath = os.path.abspath(os.path.join(os.path.dirname(__file__),'..','DBASE','rapport',self.dbase.type, reportdic['qptfile'] + '.qpt'))
        else:
            templatepath = os.path.abspath(
                os.path.join(os.path.dirname(__file__), '..', 'DBASE', 'rapport', self.dbase.type,reportdic['qptfile'] + '3.qpt'))
        template_file = QtCore.QFile(templatepath)
        template_file.open(QtCore.QIODevice.ReadOnly | QtCore.QIODevice.Text)
        template_content = template_file.readAll()
        template_file.close()
        if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
            document = QtXml.QDomDocument()
            document.setContent(template_content)
            # You can use this to replace any string like this [key]
            # in the template with a new value. e.g. to replace
            # [date] pass a map like this {'date': '1 Jan 2012'}
            # substitution_map = {'DATE_TIME_START': 'foo','DATE_TIME_END': 'bar'}
            substitution_map = {}
            newComposition.loadFromTemplate(document,substitution_map)
        else:
            document = QtXml.QDomDocument()
            document.setContent(template_content)
            substitution_map = {}
            newComposition.loadFromTemplate(document,qgis.core.QgsReadWriteContext())


        if debug: self.logger.debug('template loaded')

        if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
            if debug: self.logger.debug('paperHeight %s', str(newComposition.paperHeight() 		))
        else:
            if debug: self.logger.debug('paperHeight %s', str(newComposition.pageCollection().page(0).pageSize().height() 	))

        # ********************* set atlas and linked composeritem *****************************
        if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
            atlas = newComposition.atlasComposition()
        else:
            atlas = newComposition.atlas()
        #coveragelayer = qgis.core.QgsVectorLayer(reportdic['atlaslayer'])
        if True:
            coveragelayer = reportdic['atlaslayer']
            stylepath = os.path.join(os.path.dirname(__file__), '..','DBASE', 'style', self.dbase.type, reportdic['atlaslayerstyle'])
            coveragelayer.loadNamedStyle(stylepath)
            # print(stylepath)

            if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                qgis.core.QgsMapLayerRegistry.instance().addMapLayer(coveragelayer, False)
            else:
                qgis.core.QgsProject.instance().addMapLayer(coveragelayer, False)
            layertoremove.append(coveragelayer)
            atlas.setCoverageLayer(coveragelayer)

        if False:
            atlas.setCoverageLayer(reportdic['atlaslayer'])

        if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
            toexec = "reportdic['atlastypescale'] = qgis.core.QgsComposerMap." + reportdic['atlastypescale']
            # print(toexec)
            exec(toexec)
        else:
            toexec = "reportdic['atlastypescale'] = qgis.core.QgsLayoutItemMap." + reportdic['atlastypescale']
            # print(toexec)
            exec(toexec)

        atlas.setEnabled(True)

        if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
            atlas.setSingleFile(True)
            ret = newComposition.setAtlasMode(qgis.core.QgsComposition.ExportAtlas)

        if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
            #atlas.setComposerMap(newComposition.composerMapItems()[0])
            for mapname in reportdic['atlasdriven']:
                # print('mapname', mapname)
                atlas.setComposerMap(newComposition.getComposerItemById(mapname))
                newComposition.getComposerItemById(mapname).setAtlasDriven(True)
                #newComposition.getComposerItemById(mapname).setNewScale(reportdic['atlasdrivenscale'])
                #newComposition.getComposerItemById(mapname).setAtlasScalingMode(qgis.core.QgsComposerMap.Auto)
                newComposition.getComposerItemById(mapname).setAtlasScalingMode(reportdic['atlastypescale'])

        else:
            for mapname in reportdic['atlasdriven']:
                # atlas.setComposerMap(newComposition.getComposerItemById(mapname))
                temp1 = newComposition.itemById(mapname)
                # print(mapname, type(temp1))
                temp1.__class__ = qgis.core.QgsLayoutItemMap
                # print(mapname, type(temp1))
                newComposition.itemById(mapname).setAtlasDriven(True)
                #newComposition.getComposerItemById(mapname).setNewScale(reportdic['atlasdrivenscale'])
                #newComposition.getComposerItemById(mapname).setAtlasScalingMode(qgis.core.QgsComposerMap.Auto)
                newComposition.itemById(mapname).setAtlasScalingMode(reportdic['atlastypescale'])


        if debug: self.logger.debug('atlas driven loaded')

        # ********************* fill composer map with layers *****************************

        for mapname in reportdic['layers'].keys():
            layersformapcomposer = []
            for layer in reportdic['layers'][mapname]:
                if isinstance(layer, str):
                    if True and layer == 'atlaslayer':
                        layersformapcomposer.append(coveragelayer)
                        if False:
                            stylepath = os.path.join(os.path.dirname(__file__), '..', 'DBASE', 'style', self.dbase.type, reportdic['specialstyledlayerstyle'])
                            reportdic['specialstyledlayer'].loadNamedStyle(stylepath)
                            layersformapcomposer.append(reportdic['specialstyledlayer'])
                            if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                                qgis.core.QgsMapLayerRegistry.instance().addMapLayer(reportdic['specialstyledlayer'], False)
                            else:
                                qgis.core.QgsProject.instance().addMapLayer(reportdic['specialstyledlayer'], False)
                            layertoremove.append(reportdic['specialstyledlayer'])

                    elif layer == 'scan25':
                        sql = "SELECT Ressource.file from Rasters"
                        sql += " INNER JOIN Ressource ON Rasters.id_ressource = Ressource.id_ressource"
                        sql += " WHERE Rasters.typeraster = 'IRF'"
                        query = self.dbase.query(sql)
                        result = [row[0] for row in query]
                        if len(result) > 0:
                            #fileraster = self.dbase.dbasetables['Infralineaire']['widget'].completePathOfFile(result[0])
                            fileraster = self.dbase.completePathOfFile(result[0])
                            rlayer = qgis.core.QgsRasterLayer(fileraster, os.path.basename(fileraster).split('.')[0])
                            try:
                                rlayer.renderer().setOpacity(0.5)
                            except:
                                pass
                            if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                                qgis.core.QgsMapLayerRegistry.instance().addMapLayer(rlayer,False)
                            else:
                                qgis.core.QgsProject.instance().addMapLayer(rlayer,False)
                            layersformapcomposer.append(rlayer)
                            layertoremove.append(rlayer)

                    elif layer == 'ortho':
                        sql = "SELECT Ressource.file from Rasters"
                        sql += " INNER JOIN Ressource ON Rasters.id_ressource = Ressource.id_ressource"
                        sql += " WHERE Rasters.typeraster = 'ORF'"
                        query = self.dbase.query(sql)
                        result = [row[0] for row in query]
                        if len(result) > 0:
                            #fileraster = self.dbase.dbasetables['Infralineaire']['widget'].completePathOfFile(result[0])
                            fileraster = self.dbase.completePathOfFile(result[0])
                            rlayer = qgis.core.QgsRasterLayer(fileraster, os.path.basename(fileraster).split('.')[0])
                            rlayer.renderer().setOpacity(0.5)
                            if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                                qgis.core.QgsMapLayerRegistry.instance().addMapLayer(rlayer,False)
                            else:
                                qgis.core.QgsProject.instance().addMapLayer(rlayer,False)
                            layersformapcomposer.append(rlayer)
                            layertoremove.append(rlayer)

                else:
                    layersformapcomposer.append(layer)

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

            # newComposition.getComposerItemById('map0').setAtlasScalingMode(qgis.core.QgsComposerMap.Auto)

        if False:
            for mapname in reportdic['generalmap']:
                layerext = reportdic['atlaslayer'].extent()
                layerextgeom = qgis.core.QgsGeometry.fromRect(layerext)
                # xform = qgis.core.QgsCoordinateTransform(self.dbase.qgiscrs, self.canvas.mapSettings().destinationCrs())
                layerextgeomcanvas = layerextgeom.transform(self.dbase.xform)
                layerextgeomcanvasfinal = layerextgeom.boundingBox()
                if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                    newComposition.getComposerItemById(mapname).zoomToExtent(layerextgeomcanvasfinal)
                    #overview
                    overvw = newComposition.getComposerItemById(mapname).overview()
                else:
                    temp1 = newComposition.itemById(mapname)
                    temp1.__class__ = qgis.core.QgsLayoutItemMap
                    temp1.zoomToExtent(layerextgeomcanvasfinal)
                    overvw = temp1.overview()

            if debug: self.logger.debug('map configured')

        if False:
            sql = "SELECT Ressource.file from Rasters"
            sql += " INNER JOIN Ressource ON Rasters.id_ressource = Ressource.id_ressource"
            sql += " WHERE Rasters.typeraster = 'IRF'"
            query = self.dbase.query(sql)
            result = [row[0] for row in query]
            # print(result)
            if len(result)>0:
                fileraster = self.dbase.dbasetables['Infralineaire']['widget'].completePathOfFile(result[0])
                # print(fileraster)
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

            # print('layerextgeom', layerextgeom.asPolygon())
            newComposition.getComposerItemById('map0').setNewExtent(layerextgeomcanvasfinal)

            # self.message.emit('Printing')

        # ********************* %lamia var in composer *****************************

        dictfields={}
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

        # ********************* ordering ids for pdf *****************************
        orderedids = OrderedDict()
        if self.idparent is None:
            orderedids = self.orderIdsAlongPath()
        #if orderedids is None:
        if len(orderedids) == 0:
            orderedids[0] = [feat.id() for feat in reportdic['atlaslayer'].getFeatures()]



        if debug: self.logger.debug('orderedids %s', str(orderedids))


        if orderedids is None or len(orderedids) == 0:
            return

        # ********************* if zonegeo selected *****************************
        idsforreportdict = OrderedDict()
        #print(self.dbase.dbasetables['Zonegeo']['layerqgis'].selectedFeatures())
        #print([fet for fet in self.dbase.dbasetables['Zonegeo']['layerqgis'].selectedFeatures()])
        # print([fet.attributes() for fet in self.dbase.dbasetables['Zonegeo']['layerqgis'].selectedFeatures()])
        #print([fet.id() for fet in self.dbase.dbasetables['Zonegeo']['layerqgis'].selectedFeatures()])
        #print(self.dbase.dbasetables['Zonegeo']['layerqgis'].selectedFeaturesIds())
        #print([fet.id() for fet in self.dbase.dbasetables['Zonegeo']['layerqgis'].getFeatures()])

        #print(set(self.dbase.dbasetables['Zonegeo']['layerqgis'].selectedFeaturesIds()).issubset([fet.id() for fet in self.dbase.dbasetables['Zonegeo']['layerqgis'].getFeatures()]))

        setselected = set(self.dbase.dbasetables['Zonegeo']['layerqgis'].selectedFeaturesIds())
        setids = set([fet.id() for fet in self.dbase.dbasetables['Zonegeo']['layerqgis'].getFeatures()])
        isresultvalid = setselected.issubset(setids)

        if (self.idparent is None
                and len(self.dbase.dbasetables['Zonegeo']['layerqgis'].selectedFeatures()) > 0
                and isresultvalid):

            # print([fld.name() for fld in self.dbase.dbasetables['Zonegeo']['layerqgis'].fields()])
            idszonegeoselected = [int(feat['id_zonegeo']) for feat in self.dbase.dbasetables['Zonegeo']['layerqgis'].selectedFeatures()]
            # print(idszonegeoselected)
            if False:
                sql = "SELECT * FROM  " + reportdic['dbasename'] + ",Zonegeo "
                sql += " WHERE ST_WITHIN(ST_MakeValid(" +reportdic['dbasename']  +".geom),ST_MakeValid(Zonegeo.geom))"
                if len(idszonegeoselected)==1:
                    sql += " AND Zonegeo.id_zonegeo = " + str(idszonegeoselected[0])
                else:
                    sql += " AND Zonegeo.id_zonegeo IN " + str(tuple(idszonegeoselected))
                # print(sql)
                query = self.dbase.query(sql)
                idsinzonegeo = [row[0] for row in query]
                # print(idsinzonegeo)
            if True:
                for zonegeoid in orderedids.keys():
                    # print(zonegeoid,idszonegeoselected )
                    if zonegeoid in idszonegeoselected:
                        idsforreportdict[zonegeoid] = orderedids[zonegeoid]
        else:
            #idsinzonegeo = orderedids
            idsforreportdict = orderedids

        #idsforreport = OrderedDict()

        #idsforreport = [id for id in orderedids if id in idsinzonegeo]
        if debug: self.logger.debug('idsforreport %s', str(idsforreportdict))


        # ********************* progress bar *****************************
        if self.dbase.qgsiface is not None and self.idparent is None:
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

        # *********************************************************************
        # ********************* begin printing  *****************************
        # *********************************************************************
        # try:

        if True:
            if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                newComposition.setUseAdvancedEffects(False)
                atlas.beginRender()
                exporter = None
                if self.idparent is None:
                    newComposition.beginPrintAsPDF(self.printer, self.pdffile)
                    printReady = self.painter.begin(self.printer)
                    if debug: self.logger.debug('print ready %s', printReady)
            else:
                atlas.beginRender()
                exporter = qgis.core.QgsLayoutExporter(newComposition)
                settings = qgis.core.QgsLayoutExporter.PdfExportSettings()
                printsettings = qgis.core.QgsLayoutExporter.PrintExportSettings()
                if self.idparent is None:
                    #newComposition.beginPrintAsPDF(self.printer, self.pdffile)

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
                    self.printer.setPaperSize(QtCore.QSizeF(paperWidth, paperHeight), QPrinter.Millimeter)
                    self.printer.setFullPage(True)

                    printReady = self.painter.begin(self.printer)
                    if debug: self.logger.debug('print ready %s', printReady)

            #print('paint', self.painter.device().width(),self.painter.device().widthMM() , self.painter.device().logicalDpiX())
            idecalage = 0
            compt = 0
            for zonegeoid in idsforreportdict.keys():

                #set generalmap extent to zonegeo
                if zonegeoid > 0:
                    for mapname in reportdic['generalmap']:
                        zonegeofet = self.dbase.dbasetables['Zonegeo']['layerqgis'].getFeatures(qgis.core.QgsFeatureRequest(zonegeoid)).next()
                        layerext = zonegeofet.geometry().boundingBox()
                        layerext = layerext.buffer(layerext.height() / 10.0)
                        #layerext = reportdic['atlaslayer'].extent()
                        layerextgeom = qgis.core.QgsGeometry.fromRect(layerext)
                        # xform = qgis.core.QgsCoordinateTransform(self.dbase.qgiscrs, self.canvas.mapSettings().destinationCrs())
                        layerextgeomcanvas = layerextgeom.transform(self.dbase.xform)
                        layerextgeomcanvasfinal = layerextgeom.boundingBox()
                        if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                            newComposition.getComposerItemById(mapname).zoomToExtent(layerextgeomcanvasfinal)
                            # overview
                            #overvw = newComposition.getComposerItemById(mapname).overview()
                        else:
                            temp1 = newComposition.itemById(mapname)
                            temp1.__class__ = qgis.core.QgsLayoutItemMap
                            temp1.zoomToExtent(layerextgeomcanvasfinal)
                            # overvw = temp1.overview()
                        if newComposition.getComposerItemById(mapname).scale() < reportdic['atlasdrivenminscale']*5.0:
                            #print('scale', newComposition.getComposerItemById(mapname).scale())
                            newComposition.getComposerItemById(mapname).setNewScale(reportdic['atlasdrivenminscale']*5.0)



                # for i, featid in enumerate(idsforreport):
                # for i, featid in enumerate([6]):
                for i, featid in enumerate(idsforreportdict[zonegeoid]):
                    # print('featid', featid)
                    compt += 1
                    self.setLoadingProgressBar(progress, compt)
                    #parentfeat = self.dbase.dbasetables[tablename]['layer'].getFeatures(qgis.core.QgsFeatureRequest(parendid)).next()
                    if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                        atlasfeat = reportdic['atlaslayer'].getFeatures(qgis.core.QgsFeatureRequest(featid)).next()
                    else:
                        atlasfeat = next(reportdic['atlaslayer'].getFeatures(qgis.core.QgsFeatureRequest(featid)))

                    if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                        if atlasfeat.geometry().boundingBox().toString() == 'Empty':        #point in linelayer
                            for mapname in reportdic['atlasdriven']:
                                newComposition.getComposerItemById(mapname).setAtlasScalingMode(qgis.core.QgsComposerMap.Fixed)
                                newComposition.getComposerItemById(mapname).setNewScale(reportdic['atlasdrivenminscale'])
                        else:
                            for mapname in reportdic['atlasdriven']:
                                newComposition.getComposerItemById(mapname).setAtlasScalingMode(reportdic['atlastypescale'])

                    if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                        atlas.prepareForFeature(atlasfeat)
                        currentfeature = atlas.feature()
                    else:
                        atlas.seekTo(atlasfeat)
                        currentfeature = atlasfeat

                    if debug: self.logger.debug('feat attr : %s', str([field.name() for field in currentfeature.fields()]))
                    if debug: self.logger.debug('feat attr : %s',str(currentfeature.attributes()))

                    #check atlasdriven map scale
                    if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                        for mapname in reportdic['atlasdriven']:
                            if newComposition.getComposerItemById(mapname).scale() < reportdic['atlasdrivenminscale']:
                                newComposition.getComposerItemById(mapname).setNewScale(reportdic['atlasdrivenminscale'])
                                # print('ok')
                            elif newComposition.getComposerItemById(mapname).scale() > 100000.0:
                                newComposition.getComposerItemById(mapname).setNewScale(reportdic['atlasdrivenminscale'])
                                #print('ok')

                    # photo and graph inclusion
                    if debug: self.logger.debug('image')
                    if True:
                        for imageitemname in reportdic['images'].keys():
                            if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                                imageitem = newComposition.getComposerItemById(imageitemname)
                            else:
                                imageitem = newComposition.itemById(imageitemname)
                                #composeritem = newComposition.itemByUuid(compitemuuid)
                                imageitem.__class__ = qgis.core.QgsLayoutItemPicture

                            #print(imageitem, reportdic['images'][imageitemname])
                            imagefile = None
                            if os.path.isfile(reportdic['images'][imageitemname]):
                                imagefile = reportdic['images'][imageitemname]
                            elif True and reportdic['images'][imageitemname] == 'profile':
                                try:
                                    imagefile = self.getImageFileOfProfile(atlas.currentGeometry(self.dbase.qgiscrs),imageitem)
                                except Exception as e:
                                    print(e)
                            elif True and reportdic['images'][imageitemname] ==   'profiltravers':
                                imagefile = self.getImageFileOfProfileTravers(reportdic, currentfeature,imageitem)
                            elif reportdic['images'][imageitemname] == 'photo':
                                imagefile = self.getPhoto(reportdic, currentfeature)
                            elif 'photo' in reportdic['images'][imageitemname]:
                                photoid = int(reportdic['images'][imageitemname][5:])
                                imagefile = self.getNumberedPhoto(reportdic, currentfeature, photoid)
                            elif reportdic['images'][imageitemname] == 'logo':
                                imagefile = os.path.join(os.path.dirname(__file__), '..', 'DBASE', 'rapport','utils', 'logo.jpg')

                            if imageitem is not None:
                                # print('ok',imagefile )
                                imageitem.setPicturePath(imagefile)
                                if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                                    imageitem.updateItem()
                                else:
                                    imageitem.refreshPicture()


                    if debug: self.logger.debug('var')


                    # var inclusion

                    if True:
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
                                    field = temptxt.split('.')[2]
                                    #sql = "SELECT " + field + " FROM " + table + " WHERE id_" + table + " = " + str(currentfeature.id())

                                    sql = "SELECT " + field + " FROM " + table
                                    #print('id_' + table.lower(), self.dbase.dbasetables[reportdic['dbasename']]['fields'].keys())
                                    if 'id_' + table.lower() in self.dbase.dbasetables[reportdic['dbasename']]['fields'].keys():
                                        sql += " WHERE " + table + ".id_" + table + " = " + str(currentfeature['id_' + table.lower()])
                                    elif 'lk_' + table.lower() in self.dbase.dbasetables[reportdic['dbasename']]['fields'].keys():
                                        sql += " WHERE " + table + ".id_" + table + " = " + str(currentfeature['lk_' + table.lower()])

                                    # print('lamia', sql)
                                    query = self.dbase.query(sql)
                                    valtemp = [row[0] for row in query][0]
                                    #print(valtemp)

                                    #val = self.dbase.getConstraintTextFromRawValue(table, field, currentfeature[field])
                                    val = self.dbase.getConstraintTextFromRawValue(table, field,valtemp)
                                    if unicode(val).lstrip("-").isdigit() and float(val) == -1.:
                                        finaltxt.append('/')
                                    elif val == '':
                                        finaltxt.append(' / ')
                                    elif field[0:4] == 'date':
                                        #print(val)
                                        #print(val.split('-'))
                                        #print(val.split('-')[::-1])
                                        #print('-'.join(val.split('-')[::-1]))
                                        dateinverted = '-'.join(val.split('-')[::-1])
                                        finaltxt.append(dateinverted)
                                    else:
                                        finaltxt.append(unicode(val))
                                elif 'lamiasql.' in temptxt:
                                    """
                                    "SELECT Tcobjetintervenant.fonction, Intervenant.nom,Intervenant.societe  FROM Tcobjetintervenant 
                                    INNER JOIN Intervenant ON Tcobjetintervenant.id_tcintervenant = Intervenant.id_intervenant 
                                    WHERE id_tcobjet = " + str(currentfeature['id_objet'])
                                    """
                                    # print(str(eval(temptxt[9:])))
                                    try:
                                        query = self.dbase.query(str(eval(temptxt[9:])))
                                        result = [row for row in query]
                                        if len(result)>0:
                                            finaltxt.append(' - '.join(list(result[0])))
                                        else:
                                            finaltxt.append('NR')
                                    except Exception as e:
                                        finaltxt.append(str(eval(temptxt[9:])))
                                else:
                                    finaltxt.append(temptxt)
                            txt = ''.join(finaltxt)
                            composeritem.setText(txt)

                    if debug: self.logger.debug('childprint')



                    if self.idparent is  None:
                        if i > 0 :
                            self.printer.newPage()

                        if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                            newComposition.doPrint(self.printer, self.painter)
                        else:
                            #newComposition.doPrint(self.printer, self.painter)
                            exporter.renderPage(self.painter,0)
                            eval('exporter.print(self.printer, printsettings )')
                    else:
                        # print('height', self.parentheightpx,selfheightpx , self.painter.device().height())
                        #selfheightpx = newComposition.compositionBounds().height()/ 25.4 * 96 * 1.08
                        pageheightmm = self.printer.paperRect(QPrinter.Millimeter).height()
                        selfheightpx = newComposition.compositionBounds().height() /pageheightmm * self.painter.device().height()
                        verticalpositionpx = self.parentheightpx + (i - idecalage + 1) * selfheightpx
                        # print('temp', self.idparent,verticalpositionpx, self.painter.device().height() )
                        if verticalpositionpx > self.painter.device().height():
                            # print('***************************************************** attention *****************************')
                            self.printer.newPage()
                            self.parentheightpx = 0
                            idecalage = i


                        self.painter.translate(0,self.parentheightpx + (i - idecalage) *selfheightpx)
                        newComposition.doPrint(self.printer, self.painter)
                        self.painter.translate(0, -self.parentheightpx - (i - idecalage) * selfheightpx)

                    # childprint
                    if True:
                        if 'childprint' in reportdic.keys():
                            #parentheight = newComposition.getComposerItemById('parentheight').rectWithFrame().height()
                            #pour A4
                            #print('paperSize()' , self.printer.paperRect(QPrinter.Millimeter).height())
                            parentheightmm = newComposition.getComposerItemById('parentheight').rectWithFrame().height()
                            pageheightmm = self.printer.paperRect(QPrinter.Millimeter).height()
                            parentheightpx = int(parentheightmm / pageheightmm * self.painter.device().height())
                            # height = height(mm)/(inchtomm) * resolution *1.08
                            #parentheightpx = parentheight / 25.4 * 96 * 1.08
                            childrapport = printPDFWorker(self.dbase,
                                                self.project,
                                                self.canvas,
                                                reportdic['childprint'],
                                                self.pdffile,
                                                self.windowdialog,
                                                self.printer,
                                                self.painter,
                                                idparent=currentfeature.id(),
                                                 parentheightpx=parentheightpx)
                            childrapport.work()

                    if stop10 and i == 5 :
                        break

            # ********************* close printing  *****************************
            atlas.endRender()
            if self.idparent is None:
                self.painter.end()
            if debug: self.logger.debug('end')
            if progress is not None: self.dbase.qgsiface.messageBar().clearWidgets()
            return


        for rastlayer in layertoremove:
            if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                qgis.core.QgsMapLayerRegistry.instance().removeMapLayer(rastlayer)
            else:
                qgis.core.QgsProject.instance().removeMapLayer(rastlayer)


        if debug: self.logger.debug('end')


    def orderIdsAlongPath(self):
        if self.dbase.qgsiface is not None:
            debug = False
        else:
            debug = True  #True false
        orderedids=OrderedDict()

        if debug : self.logger.debug('start')

        # **********************   ordering view ****************************
        # ************ by zonegeo and infralineaire ************************

        sql = "SELECT id_zonegeo FROM Zonegeo"
        query = self.dbase.query(sql)
        zonegeoids = [row[0] for row in query]
        dictedgesordered = {}
        if len(zonegeoids) > 0:
            for zonegeoid in zonegeoids:
                dictedgesordered[zonegeoid] = []
                sql = "SELECT ST_AsText(geom) FROM Zonegeo WHERE id_zonegeo = " + str(zonegeoid)
                query = self.dbase.query(sql)
                zonegeogeom = [row[0] for row in query][0]
                sql = "SELECT Infralineaire.id_infralineaire FROM Infralineaire"
                sql += " WHERE ST_WITHIN(ST_MakeValid(Infralineaire.geom),ST_GeomFromText('" + str(zonegeogeom) + "'," + str(
                    self.dbase.crsnumber) + "))"
                query = self.dbase.query(sql)
                result = [row[0] for row in query]
                dictedgesordered[zonegeoid] = result



        if debug: self.logger.debug('dictedgesordered %s', str(dictedgesordered))


        self.windowdialog.pathtool.computeNXGraphForAll()

        if len(dictedgesordered) > 0:
            for zonegeoid in dictedgesordered.keys():
                orderedids[zonegeoid] = []
                nxgraph, ids, indexnoeuds, infralinfaces, reverseinfralinfaces = self.windowdialog.pathtool.computeNXGraph(dictedgesordered[zonegeoid])
                subgraphs = networkx.connected_component_subgraphs(nxgraph)
                for subgraph in subgraphs:
                    #count elem
                    npedges = np.ravel(list(subgraph.edges()))
                    unique, counts = np.unique(npedges, return_counts=True)
                    edgeextremite = unique[np.where(counts==1)]
                    edgenoeud = unique[np.where(counts>2)]

                    if len(edgenoeud)>0:
                        print('attention presence d un noeud - non traite')
                    else:
                        paths=[list(edgeextremite)]

                    # if len(paths)==0 and len(edgenoeud)==0: #cas d'un circuit fermé

                    if debug: self.logger.debug('subgraph %s %s %s', str(subgraph), str(edgeextremite), str(edgenoeud))

                    for path in paths:
                        shortestpathedges = networkx.shortest_path(nxgraph, path[0], path[1])
                        id = self.windowdialog.pathtool.getIdsFromPath(shortestpathedges, ids, infralinfaces,reverseinfralinfaces)
                        #reverse list of not from amaont to aval
                        if not shortestpathedges[0:2] in infralinfaces.tolist():
                            shortestpathedgesreversed = shortestpathedges[::-1]
                            id = self.windowdialog.pathtool.getIdsFromPath(shortestpathedgesreversed, ids, infralinfaces,
                                                                           reverseinfralinfaces)


                        if self.reporttype == 'Infrastructure lineaire':
                            #orderedids += list(id[:,0])
                            orderedids[zonegeoid] += list(id[:, 0])

                        elif self.reporttype == 'Desordres':
                            geom = self.windowdialog.pathtool.getGeomFromIds(id)

                            datas = self.windowdialog.pathtool.getGraphData(geom,list(id[:,0]),'desordre', 'Profil')
                            res = [int(id) for id in datas['desordre']['id']]
                            #orderedids += res
                            orderedids[zonegeoid] += res

                        elif self.reporttype == 'Equipements hydrauliques':
                            geom = self.windowdialog.pathtool.getGeomFromIds(id)
                            datas = self.windowdialog.pathtool.getGraphData(geom,list(id[:,0]),'equipement_hydraulique', 'Profil')

                            res = [int(id) for id in datas['equipement']['id']]
                            # orderedids += res
                            orderedids[zonegeoid] += res

        return orderedids


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

    def getNumberedPhoto(self,reportdic, feat, photoid):
        #print('getNumberedPhoto', photoid)
        resfile = None

        sql = "SELECT Ressource.file FROM " + reportdic['dbasename']
        sql += " INNER JOIN Objet ON Objet.id_objet = " + reportdic['dbasename'] + ".id_objet"
        sql += " INNER JOIN Tcobjetressource ON Tcobjetressource.id_tcobjet = Objet.id_objet"
        sql += " INNER JOIN Ressource ON Tcobjetressource.id_tcressource = Ressource.id_ressource"
        sql += " INNER JOIN Photo ON Photo.id_ressource = Ressource.id_ressource"
        sql += " WHERE " + reportdic['dbasename'] + ".id_objet = " + str(feat['id_objet'])
        # print(sql)
        query = self.dbase.query(sql)
        result = [row for row in query]
        #print(result)
        # resfile = result[0][0]
        if len(result) > (photoid -1):
            resfile = self.dbase.completePathOfFile(result[photoid -1][0])
            # print(resfile)
        return resfile


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

        #self.windowdialog.pathtool.computePath(point1, point2)
        #print('path',self.windowdialog.pathtool.geomfinalids)

        # print(imageitem.rect().width(), imageitem.rect().height())

        exportfile = os.path.join(os.path.dirname(__file__), '..', 'config', 'tempgraph.png')
        self.windowdialog.pathtool.exportCurrentGraph(point1, point2,
                                                      imageitem.rect().width(),
                                                      imageitem.rect().height(),
                                                      exportfile)

        return os.path.abspath(exportfile)


    def getImageFileOfProfileTravers(self,reportdic, feat,imageitem):
        resfile = None
        #print([field.name() for field in reportdic['atlaslayer'].fields()])
        currentfeatureid = feat.id()
        if 'lk_profil' in self.dbase.dbasetables[reportdic['dbasename']]['fields'].keys():
            # if 'lk_profil' in [field.name() for field in reportdic['atlaslayer'].fields()]:
            sql = "SELECT lk_profil FROM Infralineaire WHERE id_infralineaire = " + str(currentfeatureid)
            query = self.dbase.query(sql)
            result = [row for row in query]
            lkressourceprofile = result[0][0]
            # print('getPhoto',lkphoto )

            if not self.dbase.isAttributeNull(lkressourceprofile):
                sql = "SELECT Ressource.file FROM Photo INNER JOIN Ressource ON Photo.id_ressource = Ressource.id_ressource WHERE Photo.id_ressource = "
                sql += str(lkressourceprofile)
                query = self.dbase.query(sql)
                result = [row for row in query]
                if len(result) > 0:
                    filephoto = result[0][0]
                    resfile = self.dbase.completePathOfFile(filephoto)

                sql = "SELECT typegraphique, id_graphique FROM Graphique  WHERE id_ressource = " + str(lkressourceprofile)
                query = self.dbase.query(sql)
                result = [row for row in query]
                if len(result) > 0:
                    #self.userwdgdesktop.stackedWidget_profiltravers.setCurrentIndex(1)
                    # print('ok')
                    typegraphique = result[0][0]
                    idgraphique = result[0][1]
                    # print(idgraphique)

                    #self.graphprofil.featureSelected(idgraphique, True)

                    datas = self.dbase.dbasetables['Graphique']['widget'].getGraphData(idgraphique)
                    exportfile = os.path.join(os.path.dirname(__file__), '..', 'config', 'tempgraph.png')
                    self.dbase.dbasetables['Graphique']['widget'].exportgraph(typegraphique,
                                                                                        datas,
                                                                                        exportfile,
                                                                                        imageitem.rect().width(),
                                                                                        imageitem.rect().height())
                    resfile = exportfile


        # print('resfile', resfile)
        if resfile is None:
            pass

        """
        # print(imageitem.rect().width(), imageitem.rect().height())

        exportfile = os.path.join(os.path.dirname(__file__), '..', 'config', 'tempgraph.png')
        self.windowdialog.pathtool.exportCurrentGraph(point1, point2,
                                                      imageitem.rect().width(),
                                                      imageitem.rect().height(),
                                                      exportfile)

        return os.path.abspath(exportfile)
        """

        return resfile

    def setLoadingProgressBar(self, progressbar, val):
        if progressbar is not None:
            progressbar.setValue(val)
        else:
            if self.dbase.qgsiface is None:
                logging.getLogger('Lamia').info('Generation du pdf %d', val )
        QApplication.processEvents()