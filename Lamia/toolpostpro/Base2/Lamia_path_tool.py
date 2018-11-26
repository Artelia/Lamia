# -*- coding: utf-8 -*-
import qgis
from qgis.PyQt import uic, QtGui, QtCore
try:
    from qgis.PyQt.QtGui import (QWidget, QLabel, QFrame, QTreeWidgetItem, QHeaderView)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget, QLabel, QFrame, QTreeWidgetItem, QHeaderView)

#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
#from ...toolabstract.Lamia_abstract_tool import AbstractLamiaTool
import os
import io
import sys
if False:
    if sys.version_info.major == 2:
        from ...libs import pyqtgraph as pg
        from ...libs.pyqtgraph import exporters
    elif sys.version_info.major == 3:
        from ...libs import pyqtgraph as pg
        pg.setConfigOption('background', 'w')

if sys.version_info.major == 2:
    from matplotlib.backends.backend_qt4agg import (FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
elif sys.version_info.major == 3:
    from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import networkx
import numpy as np
import shutil
import logging


# ********************************************************************************************************************
# ********************************* Main Widget                *******************************************************
# ********************************************************************************************************************

class PathTool(AbstractInspectionDigueTool):

    DBASES = ['digue','base_digue']

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(PathTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil,parentwidget, parent=parent)

        
    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Synthese'
        self.NAME = 'Chemins'
        self.visualmode = [4]
        # self.PointENABLED = True
        # self.LineENABLED = True
        # self.PolygonEnabled = True
        # self.magicfunctionENABLED = True
        # self.linkagespec = None
        # self.pickTable = None
        # print(self.dbase.recentsdbase)

        if self.dbase.dbasetype == 'spatialite':
            fielpathname = 'path_' + os.path.basename(self.dbase.spatialitefile).split('.')[0]
        elif self.dbase.dbasetype == 'postgis':
            fielpathname = 'path_' + str(self.dbase.pghost)+ '_' + str(self.dbase.pgdb) + '_' + str(self.dbase.pgschema)
        self.dbasetablename = os.path.join(os.path.dirname(__file__), '..', 'config', fielpathname + '.txt')
        #networkx var
        self.nxgraph = None
        self.ids = None
        self.indexnoeuds = None
        self.infralinfaces = None
        self.reverseinfralinfaces = None
        self.indexnoeuds = None
        # rubberband var
        self.rubberBand = qgis.gui.QgsRubberBand(self.canvas,self.dbase.dbasetables['Infralineaire']['layer'].geometryType())
        self.rubberBand.setWidth(5)
        self.rubberBand.setColor(QtGui.QColor("magenta"))

        self.rubberbandtrack = qgis.gui.QgsVertexMarker(self.canvas)
        self.rubberbandtrack.setColor(QtGui.QColor(QtCore.Qt.red))
        self.rubberbandtrack.setIconSize(5)
        self.rubberbandtrack.setIconType(qgis.gui.QgsVertexMarker.ICON_BOX) # or ICON_CROSS, ICON_X
        self.rubberbandtrack.setPenWidth(3)
        # matplotlib var
        self.figuretype = plt.figure()
        self.axtype = self.figuretype.add_subplot(111)

        self.postOnActivation()
        
        self.iconpath = os.path.join(os.path.dirname(__file__), 'lamiabase_croquis_tool_icon.png')

        # ****************************************************************************************
        # properties ui
        self.groupBox_geom.setParent(None)
        # self.groupBox_elements.setParent(None)

    def initFieldUI(self):

        # ****************************************************************************************
        # userui Desktop
        if self.userwdgfield is None:

            # ****************************************************************************************
            # userui

            self.userwdgfield = UserUI()
            self.linkuserwdgfield = [self.userwdgfield.lineEdit_nom,
                                self.userwdgfield.lineEdit_start,
                                self.userwdgfield.lineEdit_end]

            self.linkuserwdgfield = {self.dbasetablename: [self.userwdgfield.lineEdit_nom,
                                                        self.userwdgfield.lineEdit_start,
                                                        self.userwdgfield.lineEdit_end]}

            self.userwdgfield.pushButton_pickstart.clicked.connect(self.getPickResult)
            self.userwdgfield.pushButton_pickend.clicked.connect(self.getPickResult)

            # plot
            if False:
                self.plotWdg = pg.PlotWidget()
                datavline = pg.InfiniteLine(0, angle=90, pen=pg.mkPen('r', width=1), name='cross_vertical')
                datahline = pg.InfiniteLine(0, angle=0, pen=pg.mkPen('r', width=1), name='cross_horizontal')
                self.plotWdg.addItem(datavline)
                self.plotWdg.addItem(datahline)
                self.userwdgfield.frame_chart.layout().addWidget(self.plotWdg)
                self.userwdgfield.checkBox_track.stateChanged.connect(self.activateMouseTracking)
                self.doTracking = True
                self.showcursor = True

                self.userwdgfield.comboBox_chart_theme.addItems(['Profil'])
                self.userwdgfield.comboBox_chart_theme.currentIndexChanged.connect(self.computeGraph)
            if True:
                self.figuretype = plt.figure()
                self.axtype = self.figuretype.add_subplot(111)
                self.mplfigure = FigureCanvas(self.figuretype)
                self.userwdgfield.frame_chart.layout().addWidget(self.mplfigure)
                self.toolbar = NavigationToolbar(self.mplfigure, self.userwdgfield.frame_chart)
                self.userwdgfield.frame_chart.layout().addWidget(self.toolbar)

                self.userwdgfield.comboBox_chart_theme.currentIndexChanged.connect(self.computeGraph)

    """
    def activateMouseTracking(self, state):
            try:
                self.plotWdg.scene().sigMouseMoved.disconnect(self.mouseMovedPyQtGraph)
            except Exception as e :
                #print(e)
                pass

            if state == 2:
                self.doTracking = True
                self.plotWdg.scene().sigMouseMoved.connect(self.mouseMovedPyQtGraph)
                self.rubberbandtrack.show()
            elif state == 0:
                self.doTracking = False
                self.rubberbandtrack.hide()

    def mouseMovedPyQtGraph(self, pos): # si connexion directe du signal "mouseMoved" : la fonction reçoit le point courant
            roundvalue = 3
            if self.plotWdg.sceneBoundingRect().contains(pos): # si le point est dans la zone courante
                range = self.plotWdg.getViewBox().viewRange()
                mousePoint = self.plotWdg.getViewBox().mapSceneToView(pos)  # récupère le point souris à partir ViewBox

                pitems = self.plotWdg.getPlotItem()
                ytoplot = None
                xtoplot = None

                if len(pitems.listDataItems()) > 0:
                    # get data and nearest xy from cursor
                    compt = 0
                    for item in pitems.listDataItems():
                        if item.isVisible() :
                            x,y = item.getData()
                            nearestindex = np.argmin( abs(np.array(x)-mousePoint.x()) )
                            if compt == 0:
                                xtoplot = np.array(x)[nearestindex]
                                ytoplot = np.array(y)[nearestindex]
                            else:
                                if abs( np.array(y)[nearestindex] - mousePoint.y() ) < abs( ytoplot -  mousePoint.y() ):
                                    ytoplot = np.array(y)[nearestindex]
                                    xtoplot = np.array(x)[nearestindex]
                            compt += 1
                    #plot xy label and cursor
                if not xtoplot is None and not ytoplot is None:
                    # print(mousePoint)
                    #xtoplot = mousePoint.x()
                    #ytoplot =  mousePoint.y()
                    # print(self.plotWdg.allChildItems())
                    for item in self.plotWdg.allChildItems():
                        if isinstance(item, pg.graphicsItems.InfiniteLine.InfiniteLine):
                            if item.name() == 'cross_vertical':
                                item.show()
                                item.setPos(xtoplot)
                            elif item.name() == 'cross_horizontal':
                                item.show()
                                item.setPos(ytoplot)

                    if self.doTracking and not xtoplot is None and not ytoplot is None:
                        pointprojected = self.geomfinal.interpolate(xtoplot)
                        self.rubberbandtrack.show()
                        xform = qgis.core.QgsCoordinateTransform(self.dbase.qgiscrs,self.canvas.mapSettings().destinationCrs())
                        geomforrubberband = qgis.core.QgsGeometry(pointprojected)
                        geomforrubberband.transform(xform)
                        self.rubberbandtrack.setCenter(geomforrubberband.asPoint())

    """

    def computeGraph(self):
        # print('computeGraph')
        # self.plotwdg = self.plotWdg

        self.axtype.clear()

        if False:
            pitems = self.plotWdg.getPlotItem().listDataItems()
            for item in pitems:
                self.plotWdg.removeItem(item)
            try:
                self.plotWdg.scene().sigMouseMoved.disconnect(self.mouseMoved)
            except:
                pass



        datas = self.getGraphData()
        # print('datas', datas)
        #x=[0, self.geomfinal.length()]
        #y = [0,0]
        # self.plotWdg.plot(x, y, pen=pg.mkPen(model1.item(i, 1).data(Qt.BackgroundRole), width=2), name=tmp_name)
        if False:
            self.plotWdg.addLegend()
            for dataname in datas.keys():
                # print(dataname.split('-')[1])
                if dataname.split('-')[1] == 'CRE':
                    penforgraph = pg.mkPen(color='k', width=3, style=QtCore.Qt.SolidLine)
                elif dataname.split('-')[1] == 'TNT':
                    penforgraph = pg.mkPen(color='g',width=3, style=QtCore.Qt.SolidLine)
                else:
                    penforgraph = pg.mkPen(color='b', width=3,style=QtCore.Qt.DashLine)
                datavalues = datas[dataname]
                self.plotWdg.plot(datavalues['x'], datavalues['y'], name=dataname, pen= penforgraph)

            self.plotWdg.getViewBox().autoRange(items=self.plotWdg.getPlotItem().listDataItems())
            self.plotWdg.getViewBox().disableAutoRange()

        if True:
            for dataname in datas.keys():
                # print(dataname.split('-')[1])
                if False:
                    if dataname.split('-')[1] == 'CRE':
                        penforgraph = pg.mkPen(color='k', width=3, style=QtCore.Qt.SolidLine)
                    elif dataname.split('-')[1] == 'TNT':
                        penforgraph = pg.mkPen(color='g',width=3, style=QtCore.Qt.SolidLine)
                    else:
                        penforgraph = pg.mkPen(color='b', width=3,style=QtCore.Qt.DashLine)
                datavalues = datas[dataname]

                self.axtype.plot(datavalues['x'], datavalues['y'])
                #self.axtype.grid()
            self.figuretype.canvas.draw()




        #self.plotWdg.addLegend()

    def getOrderedProjectedIds(self, geomprojection=None, geomprojectionids= None, layertoproject=None,constraint=''):
        """
        Projette sur la ligne geomprojection constituée des infralineaire d'id geomprojectionids
        les éléments du qgsvectorlayer layertoproject les plus proches de geomprojection
        :param geomprojection: la geometrie sur laquelle on se projette
        :param geomprojectionids: les id dont est constituée la geometrie sur laquelle on se projette
        :return: datas : dict : 'x' : lenght along the geomprojection
                                     'y' : pk de la couche layertoproject (choisi pour être id_..)
                                     'xy' : list with [x,y]
        """
        datas = {}
        if geomprojection is not None:
            # init la valeur retournée
            datas = {'x': [], 'id': [], 'xy': []}
            # iteration sur layertoproject pour retenir seulement les éléments les plus près de la geomprojection
            layertoproject.setSubsetString(constraint)
            for fet in layertoproject.getFeatures():
                # met en forme la geoemtrie
                layergeomtype = layertoproject.geometryType()
                if fet.geometry() is None:
                    continue
                if layergeomtype == 0:
                    geom = [fet.geometry().asPoint()]
                elif layergeomtype == 1:
                    geom = fet.geometry().asPolyline()

                # iteration sur le premier et dernier point de la geometrie pour voir si l'infralineaire la plus
                # proche est dans la list  geomprojectionids
                for point in [geom[0], geom[-1]]:
                    geompointequipement1 = qgis.core.QgsGeometry.fromPoint(point)
                    nearestinfralinpk, dist = self.dbase.getNearestPk(self.dbase.dbasetables['Infralineaire'],
                                                                      'Infralineaire',
                                                                       point,
                                                                       comefromcanvas=False)
                    nearestinfralinid = self.dbase.getLayerFeatureByPk('Infralineaire', nearestinfralinpk)['id_infralineaire']
                    if nearestinfralinid in geomprojectionids:
                        distline = geomprojection.lineLocatePoint(geompointequipement1)
                        datas['xy'].append([distline, int(fet.id())])
                        break
            # met en forme le resultat notamment en le classant par abscisse sur la geomprojection
            if len(datas['xy']) > 0:
                xy = np.array(datas['xy'])
                xysorted = xy[xy[:, 0].argsort()]
                datas['x'] = xysorted[:, 0]
                datas['id'] = xysorted[:, 1]
            layertoproject.setSubsetString('')

        return datas






    def getGraphData(self, geomprojection=None, geomprojectionids= None, datatype=None,graphtype='Profillong' ):
        """

        :param geomprojection: la geometrie sur laquelle on se projette
        :param datatype: le type d'ojet à projeter
        :return: datas : dict with name as key : for topo its the leve topo name
                                                 for desordre its 'desordres'
                                    and value dict : 'x' : lenght along the geomprojection
                                                     'y' : value to store (z mngf for topo, desordre id for desordre)
                                                     'xy' : list with [x,y]

        """
        debug = False
        if debug: logging.getLogger('Lamia').info('start')


        # print('getGraphData')
        if graphtype is None:
            graphtype = self.userwdg.comboBox_chart_theme.currentText()


        if geomprojection is None:
            geomprojection = self.geomfinal
        if geomprojectionids is None:
            geomprojectionids = self.geomfinalids

        #temp
        if datatype is None:
            datatype = 'topographie'

        if debug: logging.getLogger('Lamia').info('init geomprojectionids : %s - datatype : %s - graphtype : %s',
                                                  str(geomprojectionids),        str(datatype),  str(graphtype))

        datas={}    #data[i] = ['graph type', x, y]

        if graphtype == 'Profillong':
            # datas['test'] = {'x' : [0, self.geomfinal.length()], 'y' : [0,0]}
            # datas['crete'] = {'x':[], 'y':[] }
            # datas['tnarriere'] = {'x':[], 'y':[] }
            # datas['niveauprotection'] = {'x':[], 'y':[] }

            #process topographie
            if geomprojection is not None:
                if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                    geomfinalbuffer = geomprojection.buffer(200,12).exportToWkt()
                else:
                    geomfinalbuffer = geomprojection.buffer(200, 12).asWkt()



                if datatype == 'equipement_hydraulique':
                    sql = "SELECT id_equipement, ST_AsText(geom)  FROM Equipement "
                    sql += " INNER JOIN Objet ON Objet.id_objet = Equipement.id_objet "
                    sql += "WHERE ST_WITHIN(ST_MakeValid(geom), ST_GeomFromText('" + geomfinalbuffer + "'," + str(
                        self.dbase.crsnumber) + "))"
                    sql += " AND ( Equipement.categorie = 'RHF' or Equipement.categorie = 'RHO' or Equipement.categorie = 'OUH') "
                    sql += " AND lk_equipement IS NULL"
                    sql += ' AND  Objet.Datecreation <= ' + "'" + self.dbase.workingdate + "'"
                    if self.dbase.dbasetype == 'postgis':
                        sql += ' AND CASE WHEN Objet.Datedestruction IS NOT NULL  '
                        sql += 'THEN Objet.DateDestruction > ' + "'" + self.dbase.workingdate + "'" + ' ELSE TRUE END'
                    elif self.dbase.dbasetype == 'spatialite':
                        sql += ' AND CASE WHEN Objet.datedestruction IS NOT NULL  '
                        sql += 'THEN Objet.dateDestruction > ' + "'" + self.dbase.workingdate + "'" + ' ELSE 1 END'

                    # print(sql)
                    query = self.dbase.query(sql)
                    result = [row for row in query]

                    datas['equipement'] = {'x': [], 'id': [], 'xy': []}

                    for iterequipement in result:

                        geomequipement = qgis.core.QgsGeometry.fromWkt(iterequipement[1])

                        # startpoint
                        geompointequipementpoint1 = geomequipement.asPolyline()[0]
                        geompointequipement1 = qgis.core.QgsGeometry.fromPoint(geompointequipementpoint1)
                        nearestinfralinid1, dist = self.dbase.getNearestId(self.dbase.dbasetables['Infralineaire'],
                                                                           'Infralineaire',
                                                                           geompointequipementpoint1,
                                                                           comefromcanvas=False)
                        # endpoint
                        geompointequipementpoint2 = geomequipement.asPolyline()[-1]
                        geompointequipement2 = qgis.core.QgsGeometry.fromPoint(geompointequipementpoint1)
                        nearestinfralinid2, dist = self.dbase.getNearestId(self.dbase.dbasetables['Infralineaire'],
                                                                           'Infralineaire',
                                                                           geompointequipementpoint2,
                                                                           comefromcanvas=False)

                        if nearestinfralinid1 in geomprojectionids:
                            # print('ok')
                            distline = geomprojection.lineLocatePoint(geompointequipement1)
                            datas['equipement']['xy'].append([distline, int(iterequipement[0])])
                        elif nearestinfralinid2 in geomprojectionids:
                            distline = geomprojection.lineLocatePoint(geompointequipement2)
                            datas['equipement']['xy'].append([distline, int(iterequipement[0])])

                    if len(datas['equipement']['xy']) > 0:
                        xy = np.array(datas['equipement']['xy'])
                        # print(xy)
                        xysorted = xy[xy[:, 0].argsort()]
                        # print(xysorted)
                        # xysorted = xy[xy[:, 0].argsort()]
                        datas['equipement']['x'] = xysorted[:, 0]
                        datas['equipement']['id'] = xysorted[:, 1]



                if datatype == 'desordre':
                    sql = "SELECT id_desordre, ST_AsText(geom)  FROM Desordre "
                    sql += " INNER JOIN Objet ON Objet.id_objet = Desordre.id_objet "
                    sql += "WHERE ST_WITHIN(ST_MakeValid(geom), ST_GeomFromText('" + geomfinalbuffer + "'," + str(
                        self.dbase.crsnumber) + "))"
                    sql += ' AND  Objet.Datecreation <= ' + "'" + self.dbase.workingdate + "'"
                    if self.dbase.dbasetype == 'postgis':
                        sql += ' AND CASE WHEN Objet.Datedestruction IS NOT NULL  '
                        sql += 'THEN Objet.DateDestruction > ' + "'" + self.dbase.workingdate + "'" + ' ELSE TRUE END'
                    elif self.dbase.dbasetype == 'spatialite':
                        sql += ' AND CASE WHEN Objet.datedestruction IS NOT NULL  '
                        sql += 'THEN Objet.dateDestruction > ' + "'" + self.dbase.workingdate + "'" + ' ELSE 1 END'

                    # print(sql)
                    query = self.dbase.query(sql)
                    result = [row for row in query]
                    # print('result',result)

                    datas['desordre'] = {'x': [], 'id': [], 'xy': []}
                    for iterdesordre in result:
                        print(iterdesordre[1])
                        if iterdesordre[1] is not None:
                            geomdesordre = qgis.core.QgsGeometry.fromWkt(iterdesordre[1])

                            #startpoint
                            geompointdesordrepoint1 = geomdesordre.asPolyline()[0]
                            geompointdesordre1 = qgis.core.QgsGeometry.fromPoint(geompointdesordrepoint1)
                            nearestinfralinid1, dist = self.dbase.getNearestId(self.dbase.dbasetables['Infralineaire'],
                                                                              'Infralineaire',
                                                                               geompointdesordrepoint1,
                                                                              comefromcanvas=False)
                            # endpoint
                            geompointdesordrepoint2 = geomdesordre.asPolyline()[-1]
                            geompointdesordre2 = qgis.core.QgsGeometry.fromPoint(geompointdesordrepoint1)
                            nearestinfralinid2, dist = self.dbase.getNearestId(self.dbase.dbasetables['Infralineaire'],
                                                                              'Infralineaire',
                                                                               geompointdesordrepoint2,
                                                                              comefromcanvas=False)

                            if nearestinfralinid1 in geomprojectionids :
                                #print('ok')
                                distline = geomprojection.lineLocatePoint(geompointdesordre1)
                                datas['desordre']['xy'].append([distline,int(iterdesordre[0])])
                            elif nearestinfralinid2 in geomprojectionids:
                                distline = geomprojection.lineLocatePoint(geompointdesordre2)
                                datas['desordre']['xy'].append([distline,int(iterdesordre[0])])

                    if len(datas['desordre']['xy'])>0:
                        xy = np.array(datas['desordre']['xy'])
                        #print(xy)
                        xysorted = xy[xy[:, 0].argsort()]
                        #print(xysorted)
                        #xysorted = xy[xy[:, 0].argsort()]
                        datas['desordre']['x'] = xysorted[:,0]
                        datas['desordre']['id'] = xysorted[:, 1]




                elif datatype == 'topographie':

                    sql = "SELECT typepointtopo, zmngf,id_topographie, ST_AsText(geom)  FROM Pointtopo_qgis "
                    sql += "WHERE ST_WITHIN(geom, ST_GeomFromText('" + geomfinalbuffer + "',"+str(self.dbase.crsnumber) + "));"
                    query = self.dbase.query(sql)
                    result = [row[0:4] for row in query]
                    #print(result)

                    for pointtopo in result:
                        geompointtopo = qgis.core.QgsGeometry.fromWkt(pointtopo[3])
                        geompointtopopoint = geompointtopo.asPoint()

                        nearestinfralinpk, dist = self.dbase.getNearestPk(self.dbase.dbasetables['Infralineaire'],
                                                                          'Infralineaire',
                                                                          geompointtopopoint,
                                                                          comefromcanvas=False)
                        nearestinfralinid = self.dbase.getLayerFeatureByPk('Infralineaire', nearestinfralinpk)['id_infralineaire']

                        if False:
                            nearestinfralinid, dist = self.dbase.getNearestId(self.dbase.dbasetables['Infralineaire'],
                                                                              'Infralineaire',
                                                                              geompointtopopoint,
                                                                              comefromcanvas=False)

                        # print(geompointtopo, nearestinfralinid, dist)
                        if nearestinfralinid in geomprojectionids:
                            # print('in nearest')
                            # print('pointtopo',pointtopo)
                            graphname = str(pointtopo[2]) + '-' + str(pointtopo[0])
                            if not graphname in datas.keys():
                                # datas[graphname]={'x':[], 'y':[] }
                                datas[graphname] ={'x':[], 'y':[], 'xy':[] }

                            distline = geomprojection.lineLocatePoint(geompointtopo)

                            datas[graphname]['xy'].append([distline,pointtopo[1]])
                            #datas[graphname]['y'].append(pointtopo[1])

                    for dataname in datas.keys():
                        # print('***********')
                        xy = np.array(datas[dataname]['xy'])
                        #print(xy)
                        xyforunique = np.array([str(datas[dataname]['xy'][i]) for i in range(len(datas[dataname]['xy'])) ] )
                        #print(xyforunique)
                        xyuniquetemp, index1, index2 = np.unique(xyforunique, return_index=True, return_inverse=True)
                        #print(xyuniquetemp)
                        xyunique = xy[index1]
                        #print(xyunique)
                        #pointstemp1 = np.array([str(row) for row in pointstemp])

                        #points, index1, index2 = np.unique(pointstemp1, return_index=True, return_inverse=True)


                        xysorted = xyunique[xyunique[:, 0].argsort()]
                        #print(xysorted)
                        #xysorted = xy[xy[:, 0].argsort()]
                        datas[dataname]['x'] = xysorted[:,0]
                        datas[dataname]['y'] = xysorted[:, 1]

                        #adapt to geomfinal
                        totallengeom = geomprojection.length()
                        # print(totallengeom, datas[dataname]['x'],datas[dataname]['y'])
                        if 0 not in datas[dataname]['x']:
                            datas[dataname]['x'] = np.insert(datas[dataname]['x'], 0, 0)
                            datas[dataname]['y'] = np.insert(datas[dataname]['y'], 0, datas[dataname]['y'][0])
                        if totallengeom not in datas[dataname]['x']:
                            datas[dataname]['x'] = np.append(datas[dataname]['x'], totallengeom)
                            datas[dataname]['y'] = np.append(datas[dataname]['y'],  datas[dataname]['y'][-1])
                        #print(totallengeom, datas[dataname]['x'], datas[dataname]['y'])





        #print('datas', datas)
        return datas





    def getPickResult(self):
        # print('cliekd')
        if self.sender() == self.userwdgfield.pushButton_pickstart:
            self.tempbutton = 'start'
        elif self.sender() == self.userwdgfield.pushButton_pickend:
            self.tempbutton = 'end'
        self.pointEmitter.canvasClicked.connect(self.selectPickedFeature)
        self.canvas.setMapTool(self.pointEmitter)



    def selectPickedFeature(self, point):
        pointfromcanvas = point
        # print(pointfromcanvas)

        self.rubberBand.reset(self.dbase.dbasetables['Infralineaire']['layer'].geometryType())
        try:
            self.pointEmitter.canvasClicked.disconnect(self.selectPickedFeature)
        except:
            pass
        if False:
            # print(self.canvas.mapSettings().destinationCrs().authid(), self.dbase.qgiscrs.authid())
            xform = qgis.core.QgsCoordinateTransform( self.canvas.mapSettings().destinationCrs(),self.dbase.qgiscrs)
            success = qgis.core.QgsGeometry.fromPoint(pointfromcanvas).transform(xform)
            # print(pointfromcanvas)
        point2 = self.pointEmitter.toLayerCoordinates(self.dbase.dbasetables['Infralineaire']['layerqgis'], point)
        # print(point2)

        if self.tempbutton == 'start':
            self.userwdgfield.lineEdit_start.setText(str(point2.x()) + ',' + str(point2.y()))
        elif self.tempbutton == 'end':
            self.userwdgfield.lineEdit_end.setText(str(point2.x()) + ',' + str(point2.y()))

        try:
            point1 = np.array([float(elem1) for elem1 in self.userwdgfield.lineEdit_start.text().split(',')])
            point2 = np.array([float(elem1) for elem1 in self.userwdgfield.lineEdit_end.text().split(',')])
        except ValueError:
            print('ValueError')
            return

        self.computePath(point1, point2)

    def computePath(self,  point1, point2, alsocomputegraph=True):
        """
        Calcul le plus court chemin entre point1 et point2
        Dessine le chemin sur le rubberband
        Défini self.geomfinal : le qgsgeomtry entre le point1 et 2
                self.geomfinalids : les ids entre le point1 1 et 2

        :param point1:
        :param point2:
        :param alsocomputegraph:
        :return:
        """

        if self.nxgraph is None:
            self.computeNXGraphForAll()

        point1 = np.array(point1)
        point2 = np.array(point2)
        if self.indexnoeuds is not None:
            dist1 = np.linalg.norm(self.indexnoeuds - point1,axis = 1)
            index = np.where(dist1 == np.amin(dist1))
            networkpoint1 = index[0][0]
            dist2 = np.linalg.norm(self.indexnoeuds - point2,axis = 1)
            index = np.where(dist2  == np.amin(dist2))
            networkpoint2 = index[0][0]

            try:
                shortestpathedges = networkx.shortest_path(self.nxgraph, networkpoint1, networkpoint2)
                # print('shortestpathedges', shortestpathedges)
            except networkx.exception.NetworkXNoPath:
                #print('no path')
                self.userwdgfield.label_pathids.setText('Pas de chemin')
                return

            if False:
                shortestids=[]
                for i in range(len(shortestpathedges)-1):
                    singlepath = [shortestpathedges[i], shortestpathedges[i + 1]]
                    reverse = 0 #not reverse
                    index = np.where(np.all(self.infralinfaces == singlepath, axis=1))[0]
                    if len(index) == 0:
                        index = np.where(np.all(self.reverseinfralinfaces == singlepath, axis=1))[0]
                        reverse = 1
                    shortestids.append([self.ids[index[0]],reverse])
                shortestids = np.array(shortestids)
            if True:
                shortestids = self.getIdsFromPath(shortestpathedges)


            # print(shortestids)

            if False:
                geomfinalnodes = []
                for id, reverse in shortestids:
                    # print(id, reverse)
                    feat = self.dbase.getLayerFeatureById('Infralineaire', id)
                    geom = feat.geometry()
                    nodes = geom.asPolyline()
                    if reverse:
                        nodes.reverse()
                        #geom = qgis.core.QgsGeometry.fromPolyline(nodes)
                    geomfinalnodes += nodes
                geom = qgis.core.QgsGeometry.fromPolyline(geomfinalnodes)

            if True:
                self.geomfinal = self.getGeomFromIds(shortestids)

            # print(self.geomfinal.asPolyline())
            # xform = qgis.core.QgsCoordinateTransform(self.dbase.qgiscrs ,self.canvas.mapSettings().destinationCrs())
            #success = qgis.core.QgsGeometry.fromPoint(pointfromcanvas).transform(xform)
            geomforrubberband = qgis.core.QgsGeometry(self.geomfinal)
            #geomforrubberband.transform(xform)
            geomforrubberband.transform(self.dbase.xform)
            # print(geomforrubberband.asPolyline())
            self.rubberBand.addGeometry(geomforrubberband, None)

            if len(shortestids)>0:
                #self.geomfinalnodes = geomfinalnodes
                #self.geomfinal = qgis.core.QgsGeometry.fromPolyline(geomfinalnodes)
                self.geomfinalids = shortestids[:,0]

                # print('self.geomfinalnodes',self.geomfinalnodes)
                # print('self.geomfinal', self.geomfinal)
                # print('self.geomfinalids', self.geomfinalids)
                self.userwdgfield.label_pathids.setText(str(list(self.geomfinalids)))

                self.rubberBand.show()
            else:
                self.geomfinalnodes = None
                self.geomfinal = None
                self.geomfinalids = []

            if alsocomputegraph:
                self.computeGraph()

    def getIdsFromPath(self,pathedges, ids=None, infralinfaces=None, reverseinfralinfaces=None):
        """
        :param pathedges: the edges of the path
        :return: np.array [..[id, reverse = True/False : if the geom is in the same direction of path edge]...]
        """
        # print('getIdsFromPath',pathedges)
        if ids is None and infralinfaces is None and reverseinfralinfaces is None  :
            if self.nxgraph is None:
                self.computeNXGraphForAll()
            ids = self.ids
            infralinfaces = self.infralinfaces
            reverseinfralinfaces = self.reverseinfralinfaces
        shortestids = []

        # print('***********************getIdsFromPath***')
        # print(pathedges)
        # print(ids)

        for i in range(len(pathedges) - 1):
            singlepath = [pathedges[i], pathedges[i + 1]]

            # print(singlepath)
            # print('infra', infralinfaces)
            # print()
            reverse = 0  # not reverse
            index = np.where(np.all(infralinfaces == singlepath, axis=1))[0]
            # print('index1', index)
            if len(index) == 0:
                index = np.where(np.all(reverseinfralinfaces == singlepath, axis=1))[0]
                reverse = 1
            # print(ids)
            # print('index2', index)
            shortestids.append([ids[index[0]], reverse])
        shortestids = np.array(shortestids)
        return shortestids


    def getGeomFromIds(self,ids):
        """
        convertie une serie d'ids qui forment un path en polyligne
        :param ids: les ids dont on veut assembler la geometrie
        :return: la geometrie
        """
        geomfinalnodes = []
        for id, reverse in ids:
            # print('id, reverse', id, reverse)
            feat = self.dbase.getLayerFeatureById('Infralineaire', id)
            geom = feat.geometry()
            nodes = geom.asPolyline()
            if reverse:
                nodes.reverse()
                # geom = qgis.core.QgsGeometry.fromPolyline(nodes)
            geomfinalnodes += nodes
        if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
            geom = qgis.core.QgsGeometry.fromPolyline(geomfinalnodes)
        else:
            geom = qgis.core.QgsGeometry.fromPolylineXY(geomfinalnodes)
        return geom



    def postOnActivation(self):
        # print('post path activ')
        self.computeNXGraphForAll()
        #self.nxgraph, self.indexnoeuds, self.infralinfaces, self.reverseinfralinfaces= self.computeNXGraph()

    def computeNXGraphForAll(self):
        self.nxgraph, self.ids, self.indexnoeuds, self.infralinfaces, self.reverseinfralinfaces = self.computeNXGraph()

    def computeNXGraph(self, listids=None):
        """
        compute networkx graph for all infralineaire or for listids if specified
        Calcul le networkx graph pour toutes les infralineaires ou seulement pour les infralineaires dont
        l'id est fournie
        :param listids: optionnel - les id d'infralineaire sur lequels on veut faire le graph
        :return: nxgraph : le graph netxworkx
                 ids : list des id
                  indexnoeuds : list où l'ordre est l'index du noeud selon le graph , et la valeur le xy du noeud
                   infralinfaces : les index des extremites correspondant aux id dans le sens de la geometrie
                    reverseinfralinfaces : les index des extremites correspondant aux id dans le sens inverse de la geometrie
        """
        nxgraph = networkx.Graph()
        if False:
            #get noeuds
            sql = "SELECT Infralineaire.id_infralineaire, ST_AsText(ST_StartPoint(Infralineaire.geom)), ST_AsText(ST_EndPoint(Infralineaire.geom)) "
            sql += "FROM Infralineaire "
            sql += "INNER JOIN Descriptionsystem ON Infralineaire.id_descriptionsystem = Descriptionsystem.id_descriptionsystem "
            sql += "INNER JOIN Objet ON Objet.id_objet = Infralineaire.id_objet "
            sql += ' WHERE  Objet.Datecreation <= ' + "'" + self.dbase.workingdate + "'"
            if self.dbase.dbasetype == 'postgis':
                sql += ' AND CASE WHEN Objet.Datedestruction IS NOT NULL  '
                sql += 'THEN Objet.DateDestruction > ' + "'" + self.dbase.workingdate + "'" + ' ELSE TRUE END'
            elif self.dbase.dbasetype == 'spatialite':
                sql += ' AND CASE WHEN Objet.datedestruction IS NOT NULL  '
                sql += 'THEN Objet.dateDestruction > ' + "'" + self.dbase.workingdate + "'" + ' ELSE 1 END'
            if listids is not None:
                sql += " AND Infralineaire.id_infralineaire IN " + str(tuple(listids))
        else:
            sql = "SELECT Infralineaire_qgis.id_infralineaire,"
            sql += " ST_AsText(ST_StartPoint(Infralineaire_qgis.geom)), ST_AsText(ST_EndPoint(Infralineaire_qgis.geom))"
            sql += " FROM Infralineaire_qgis "
            sql += ' WHERE '
            sql += self.dbase.dateVersionConstraintSQL()
            if listids is not None:
                sql += " AND Infralineaire_qgis.id_infralineaire IN " + str(tuple(listids))

        query = self.dbase.query(sql)
        if len(query)>0:
            rawpoints = np.array([[[float(elem1) for elem1 in row[1].split('(')[1][:-1].split(' ')],
                                [float(elem2) for elem2 in row[2].split('(')[1][:-1].split(' ')]] for row in query])
            ids = np.array([row[0] for row in query])
            # create 1d array with startxy1, startxy2, ..., startxyn, endxy1, endxyy2, ...,endxyn
            pointstemp = np.append(rawpoints[:,0], rawpoints[:,1] ,axis = 0)
            # convert to string to manage np.unique with couple of xy
            pointstemp1 = np.array([str(row) for row in pointstemp])
            # get unique point with index compared to pointstemp1
            points, index1, index2 = np.unique(pointstemp1, return_index=True,  return_inverse=True)
            # list of unique points
            pointsarr = pointstemp[index1]      # the uniques points
            # list of unique point index compared to pointstemp1
            index2bis = np.transpose(np.reshape(index2, (2,-1)))
            #
            nxgraph.add_edges_from([(edge[0], edge[1]) for edge in index2bis])
            indexnoeuds = pointsarr
            infralinfaces = index2bis
            reverseinfralinfaces = np.flip(infralinfaces,1)

            return nxgraph, ids, indexnoeuds, infralinfaces, reverseinfralinfaces
        else:
            return None, None, None, None, None




    def postInitFeatureProperties(self, feat):
        # print('post path')
        if self.rubberBand is not None:
            self.rubberBand.reset(self.dbase.dbasetables['Infralineaire']['layer'].geometryType())
        self.userwdgfield.label_pathids.setText('')

        try:
            point1 = np.array([float(elem1) for elem1 in self.userwdgfield.lineEdit_start.text().split(',')])
            point2 = np.array([float(elem1) for elem1 in self.userwdgfield.lineEdit_end.text().split(',')])
        except ValueError:
            print('ValueError')
            return

        self.computePath(point1, point2)



    def postOnDesactivation(self):
        if self.rubberBand is not None:
            self.rubberBand.reset(self.dbase.dbasetables['Infralineaire']['layer'].geometryType())

        try:
            self.plotWdg.scene().sigMouseMoved.disconnect(self.mouseMovedPyQtGraph)
        except Exception as e:
            print(e)
        try:
            self.pointEmitter.canvasClicked.disconnect(self.selectPickedFeature)
        except Exception as e:
            print(e)

    def exportCurrentGraph(self,point1,point2, w,h,exportfile):

        debug = False

        logging.getLogger('Lamia').info('start')

        self.computePath(point1, point2, alsocomputegraph=False)
        logging.getLogger('Lamia').info('path %s %s', str(self.geomfinal),str( self.geomfinalids))

        datas = self.getGraphData()
        logging.getLogger('Lamia').info('datas %s', str(datas))

        self.axtype.cla()
        self.figuretype.set_size_inches(w / 25.4, h / 25.4)

        if len(datas) == 0:
            src_file = os.path.join(os.path.dirname(__file__), '..','..', 'DBASE', 'rapport', 'utils', 'blank.png')
            shutil.copyfile(src_file, exportfile)
            return

        for dataname in datas.keys():
            # print('*****')
            datavalues = datas[dataname]
            label = []
            topoid = int(dataname.split('-')[0].strip())
            # print(topoid)
            topofet = self.dbase.getLayerFeatureById('Topographie',int(topoid))
            idressource = self.dbase.getValuesFromPk('Topographie_qgis', 'id_ressource',topofet.id() )
            # idressource = self.dbase.getLayerFeatureById('Topographie',int(topoid))['id_ressource']
            # print(idressource)
            nom = self.dbase.getLayerFeatureById('Ressource',idressource)['Description']
            # print(nom)
            label.append(nom)
            label.append(self.dbase.getConstraintTextFromRawValue('Pointtopo','typepointtopo',dataname.split('-')[1].strip()))
            labelname = '-'.join(label)


            self.axtype.plot(datavalues['x'], datavalues['y'], label = labelname)
        #legend = self.axtype.legend(loc='upper center', prop={'size': 6}, shadow=False)
        #legend = self.axtype.legend(bbox_to_anchor=(1.04,0), loc="lower left", borderaxespad=0, prop={'size': 8}, shadow=False)
        legend = self.axtype.legend(bbox_to_anchor=(0., 1.), loc="lower left", bbox_transform=self.figuretype.transFigure, prop={'size': 8})
        # print('size',w,h)
            #self.plotWdg.plot(, name=dataname, pen= penforgraph)
        # plt.ylabel('Altitude m NGF', fontsize=8)
        self.axtype.set_ylabel('Altitude m NGF', fontsize=8)
        #self.figuretype.set_size_inches(w/25.4,h/25.4)
        #self.figuretype.savefig(exportfile, bbox_inches='tight')
        # plt.draw()
        # self.axtype.apply_aspec()
        self.figuretype.savefig(exportfile, bbox_inches='tight', dpi = 150)
        # self.figuretype.savefig(exportfile, dpi=150)

        if False:
            exportplotWdg = pg.PlotWidget()
            exportplotWdg.resize(w, h)
            exportplotWdg.setVisible(True)
            QtGui.QApplication.processEvents()
            exportplotWdg.setVisible(False)
            try:
                # exporter = exporters.ImageExporter(self.plotWdg.plotItem)
                if False:
                    pitems = self.plotWdg.getPlotItem()
                    # print(pitems)
                    pitems = self.plotWdg.getPlotItem().listDataItems()
                    # print(pitems)
                    for item in pitems:
                        exportplotWdg.addItem(item)
                exportplotWdg.addItem(self.plotWdg.getPlotItem())

            except:
                pass
            exporter = exporters.ImageExporter(exportplotWdg.scene())
            exporter.export(exportfile)

        if False:
            self.plotWdg.resize(w, h)

            self.plotWdg.setVisible(True)
            QtGui.QApplication.processEvents()
            self.plotWdg.setVisible(False)
            exporter = exporters.ImageExporter(self.plotWdg.scene())
            exporter.export(exportfile)

    def resizewidget(self,w,h):

        if True:
            self.plotWdg.resize(w, h)
        if True:
            win = pg.GraphicsWindow()
            win.resize(w,h)
        if True:
            export_area = pg.GraphicsLayoutWidget(border=(50, 50, 50))
            export_area.setBackground('w')
            export_area.resize(w, h)
            export_area.setVisible(True)
            export_area.setVisible(False)



class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        # self.setupUi(self)
        uipath = os.path.join(os.path.dirname(__file__), 'Lamia_path_tool.ui')
        uic.loadUi(uipath, self)

