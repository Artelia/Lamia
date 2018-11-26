# -*- coding: utf-8 -*-

import qgis
import os
# from ..toolabstract.inspectiondigue_abstractworker import AbstractWorker
from qgis.PyQt import QtGui, uic, QtCore, QtXml
from collections import OrderedDict
import datetime
import decimal
import numpy as np
import glob

#from .tools.Lamia_exportshpdialog import ExportShapefileDialog
from ..base2.Lamiabase_rapport import printPDFBaseWorker

#class exportShapefileWorker(AbstractWorker):


class printPDFDigueWorker(printPDFBaseWorker):


    def __init__(self,
                 dbase=None,
                 windowdialog=None,
                 parentprintPDFworker=None):
        super(printPDFDigueWorker, self).__init__(dbase, windowdialog,parentprintPDFworker)

    def postInit(self):
        """
        Appelé à la fin de l'init
        permet pour les classes filles de préciser le self.createfilesdir
        """
        self.createfilesdir = os.path.join(os.path.dirname(__file__), 'rapporttools')
        """
        for filename in glob.glob(os.path.join(self.createfilesdir, '*.txt')):
            basename = os.path.basename(filename).split('.')[0]
            #self.exportshapefiledialog.comboBox_type.addItems([basename])
            self.printrapportdialog.comboBox_type.addItems([basename])
        """



    def processImages(self,newComposition,atlas,atlasfeat):
        if True:
            #for imageitemname in reportdic['images'].keys():
            for imageitemname in self.atlasconfData['images'].keys():
                # get imageitem
                if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                    imageitem = newComposition.getComposerItemById(imageitemname)
                else:
                    imageitem = newComposition.itemById(imageitemname)
                    # composeritem = newComposition.itemByUuid(compitemuuid)
                    imageitem.__class__ = qgis.core.QgsLayoutItemPicture

                # print(imageitem, reportdic['images'][imageitemname])
                imagefile = None

                if os.path.isfile(self.atlasconfData['images'][imageitemname]):
                    imagefile = self.atlasconfData['images'][imageitemname]

                elif True and self.atlasconfData['images'][imageitemname] == 'profile':
                    #try:
                    imagefile = self.getImageFileOfProfile(atlas.currentGeometry(self.dbase.qgiscrs), imageitem)
                    #except Exception as e:
                    #    print(e)

                elif True and self.atlasconfData['images'][imageitemname] == 'profiltravers':
                    # imagefile = self.getImageFileOfProfileTravers(reportdic, currentfeature, imageitem)
                    imagefile = self.getImageFileOfProfileTravers(atlasfeat, imageitem)


                elif 'photo' in self.atlasconfData['images'][imageitemname]:
                    photoid = int(self.atlasconfData['images'][imageitemname][5:])
                    imagefile = self.getNumberedPhoto(atlasfeat, photoid)

                elif 'ressource' in self.atlasconfData['images'][imageitemname]:
                    ressourcenum = int(self.atlasconfData['images'][imageitemname][9:])
                    #imagefile = self.getPhoto(reportdic, currentfeature)
                    imagefile = self.getNumberedRessource(atlasfeat, ressourcenum)

                elif self.atlasconfData['images'][imageitemname] == 'logo':
                    imagefile = os.path.join(os.path.dirname(__file__), '..','..', 'DBASE', 'rapport', 'utils', 'logo.jpg')

                if imageitem is not None:
                    # print('ok',imagefile )
                    imageitem.setPicturePath(imagefile)
                    if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                        imageitem.updateItem()
                    else:
                        imageitem.refreshPicture()



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

        exportfile = os.path.join(os.path.dirname(__file__), '..','..', 'config', 'tempgraph.png')

        # get pathtool and init it
        pathtool = None
        for i, tool in enumerate(self.windowdialog.tools):
            if 'PathTool' in tool.__class__.__name__ :
                pathtool = self.windowdialog.tools[i]

        pathtool.exportCurrentGraph(point1, point2,
                                              imageitem.rect().width(),
                                              imageitem.rect().height(),
                                              exportfile)

        return os.path.abspath(exportfile)


    # def getImageFileOfProfileTravers(self,reportdic, feat,imageitem):
    def getImageFileOfProfileTravers(self, atlasfeat, imageitem):
        resfile = None
        #print([field.name() for field in reportdic['atlaslayer'].fields()])
        currentfeatureid = atlasfeat.id()
        #if 'lk_profil' in self.dbase.dbasetables[reportdic['dbasename']]['fields'].keys():
        if True:

            # if 'lk_profil' in [field.name() for field in reportdic['atlaslayer'].fields()]:
            # sql = "SELECT lk_ressource4 FROM Infralineaire WHERE id_infralineaire = " + str(currentfeatureid)
            sql = "SELECT lid_ressource_4 FROM Infralineaire WHERE id_infralineaire = " + str(currentfeatureid)
            query = self.dbase.query(sql)
            result = [row for row in query]
            lkressourceprofile = result[0][0]
            # print('getPhoto',lkphoto )

            if not self.dbase.isAttributeNull(lkressourceprofile):
                # sql = "SELECT Ressource.file FROM Photo INNER JOIN Ressource ON Photo.id_ressource = Ressource.id_ressource WHERE Photo.id_ressource = "
                sql = "SELECT file FROM Photo_qgis  WHERE id_ressource = "
                sql += str(lkressourceprofile)
                query = self.dbase.query(sql)
                result = [row for row in query]
                if len(result) > 0:
                    filephoto = result[0][0]
                    resfile = self.dbase.completePathOfFile(filephoto)

                # sql = "SELECT typegraphique, id_graphique FROM Graphique  WHERE id_ressource = " + str(lkressourceprofile)
                sql = "SELECT typegraphique, id_graphique FROM Graphique_qgis  WHERE id_ressource = " + str(lkressourceprofile)
                query = self.dbase.query(sql)
                result = [row for row in query]
                if len(result) > 0:
                    #self.userwdgdesktop.stackedWidget_profiltravers.setCurrentIndex(1)
                    # print('ok')
                    typegraphique = result[0][0]
                    idgraphique = result[0][1]
                    # print(idgraphique)

                    #self.graphprofil.featureSelected(idgraphique, True)

                    datas = self.dbase.dbasetables['Graphique']['widget'][0].getGraphData(idgraphique)
                    exportfile = os.path.join(os.path.dirname(__file__), '..','..', 'config', 'tempgraph.png')
                    self.dbase.dbasetables['Graphique']['widget'][0].exportgraph(typegraphique,
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