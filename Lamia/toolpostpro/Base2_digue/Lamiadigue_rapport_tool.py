# -*- coding: utf-8 -*-
import qgis
from qgis.PyQt import uic, QtGui, QtCore
try:
    from qgis.PyQt.QtGui import (QWidget, QLabel, QFrame, QTreeWidgetItem, QHeaderView)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget, QLabel, QFrame, QTreeWidgetItem, QHeaderView)

# from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
import os
import io
import glob

from ..Base2.Lamia_rapport_tool import RapportTool
from ..Base2.Lamia_rapport_tool import printPDFBaseWorker

# ********************************************************************************************************************
# ********************************* Main Widget                *******************************************************
# ********************************************************************************************************************

class DigueRapportTool(RapportTool):

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(DigueRapportTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil,parentwidget, parent=parent)




class printPDFBaseWorker(printPDFBaseWorker):


    def __init__(self, dbase, windowdialog=None, parentprintPDFworker=None, confData=None, pdffile=None, reporttype=None,templatedir=None):
        super(printPDFBaseWorker, self).__init__(dbase=dbase,
                                                 windowdialog=windowdialog,
                                                 parentprintPDFworker=parentprintPDFworker,
                                                 confData=confData,
                                                 pdffile=pdffile,
                                                 reporttype=reporttype,
                                                 templatedir=templatedir)

    #def profile(self,featgeom,imageitem):
    def profile(self):
        featgeom = self.currentatlasfeat.geometry()
        imageitem = self.currentimageItem

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


    #def profiltravers(self, atlasfeat, qrect):
    def profiltravers(self):
        atlasfeat = self.currentatlasfeat
        qrect = self.currentimageItem.rect()

        resfile = None
        #print([field.name() for field in reportdic['atlaslayer'].fields()])
        if isinstance(atlasfeat, qgis.core.QgsFeature):
            currentfeatureid = atlasfeat.id()
        elif isinstance(atlasfeat, int):
            currentfeatureid = atlasfeat
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
                                                                                         qrect.width(),
                                                                                         qrect.height())
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