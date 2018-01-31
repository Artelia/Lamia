# -*- coding: utf-8 -*-
import qgis
from qgis.PyQt import uic, QtGui, QtCore
try:
    from qgis.PyQt.QtGui import (QWidget, QLabel, QFrame, QTreeWidgetItem, QHeaderView)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget, QLabel, QFrame, QTreeWidgetItem, QHeaderView)

from ..toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
import os
from ..toolprepro.InspectionDigue_photos_tool import PhotosTool
from ..toolprepro.InspectionDigue_observation_tool import ObservationTool
from ..toolabstract.inspectiondigue_abstractworker import AbstractWorker
import io
from ..libs import pyqtgraph as pg
from ..libs.pyqtgraph import exporters

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import networkx
import numpy as np


# ********************************************************************************************************************
# ********************************* Main Widget                *******************************************************
# ********************************************************************************************************************

class PathTool(AbstractInspectionDigueTool):

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(PathTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil,parentwidget, parent=parent)
        
    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Synthese'
        self.NAME = 'Chemins'
        self.visualmode = [1]
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

        self.nxgraph = None
        self.indexnoeuds = None
        # self.rubberbandpath
        self.rubberBand = qgis.gui.QgsRubberBand(self.canvas,self.dbase.dbasetables['Infralineaire']['layer'].geometryType())
        self.rubberBand.setWidth(5)
        self.rubberBand.setColor(QtGui.QColor("magenta"))

        self.rubberbandtrack = qgis.gui.QgsVertexMarker(self.canvas)
        self.rubberbandtrack.setColor(QtGui.QColor(QtCore.Qt.red))
        self.rubberbandtrack.setIconSize(5)
        self.rubberbandtrack.setIconType(qgis.gui.QgsVertexMarker.ICON_BOX) # or ICON_CROSS, ICON_X
        self.rubberbandtrack.setPenWidth(3)


        self.postOnActivation()

        # ****************************************************************************************
        # properties ui
        self.groupBox_geom.setParent(None)
        # self.groupBox_elements.setParent(None)

        # ****************************************************************************************
        # userui

        self.userwdg = UserUI()
        self.linkuserwdg = [self.userwdg.lineEdit_nom,
                            self.userwdg.lineEdit_start,
                            self.userwdg.lineEdit_end]

        self.linkuserwdg = {self.dbasetablename: [self.userwdg.lineEdit_nom,
                                                    self.userwdg.lineEdit_start,
                                                    self.userwdg.lineEdit_end]}

        self.userwdg.pushButton_pickstart.clicked.connect(self.getPickResult)
        self.userwdg.pushButton_pickend.clicked.connect(self.getPickResult)

        # plot
        self.plotWdg = pg.PlotWidget()
        datavline = pg.InfiniteLine(0, angle=90, pen=pg.mkPen('r', width=1), name='cross_vertical')
        datahline = pg.InfiniteLine(0, angle=0, pen=pg.mkPen('r', width=1), name='cross_horizontal')
        self.plotWdg.addItem(datavline)
        self.plotWdg.addItem(datahline)
        self.userwdg.frame_chart.layout().addWidget(self.plotWdg)
        self.userwdg.checkBox_track.stateChanged.connect(self.activateMouseTracking)
        self.doTracking = True
        self.showcursor = True

        self.userwdg.comboBox_chart_theme.addItems(['Profil'])
        self.userwdg.comboBox_chart_theme.currentIndexChanged.connect(self.computeGraph)



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


    def computeGraph(self):

        # self.plotwdg = self.plotWdg
        pitems = self.plotWdg.getPlotItem().listDataItems()
        for item in pitems:
            self.plotWdg.removeItem(item)
        try:
            self.plotWdg.scene().sigMouseMoved.disconnect(self.mouseMoved)
        except:
            pass


        datas = self.getGraphData()
        #x=[0, self.geomfinal.length()]
        #y = [0,0]
        # self.plotWdg.plot(x, y, pen=pg.mkPen(model1.item(i, 1).data(Qt.BackgroundRole), width=2), name=tmp_name)
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

        #self.plotWdg.addLegend()




    def getGraphData(self):
        graphtype = self.userwdg.comboBox_chart_theme.currentText()
        datas={}    #data[i] = ['graph type', x, y]
        if graphtype == 'Profil':
            # datas['test'] = {'x' : [0, self.geomfinal.length()], 'y' : [0,0]}
            # datas['crete'] = {'x':[], 'y':[] }
            # datas['tnarriere'] = {'x':[], 'y':[] }
            # datas['niveauprotection'] = {'x':[], 'y':[] }

            #process topographie

            geomfinalbuffer = self.geomfinal.buffer(200,12).exportToWkt()

            sql = "SELECT typepointtopo, zmngf,id_topographie, ST_AsText(geom)  FROM Pointtopo "
            sql += "WHERE ST_WITHIN(geom, ST_GeomFromText('" + geomfinalbuffer + "',"+str(self.dbase.crsnumber) + "));"
            query = self.dbase.query(sql)
            result = [row[0:4] for row in query]
            #print(result)

            for pointtopo in result:
                geompointtopo = qgis.core.QgsGeometry.fromWkt(pointtopo[3])
                geompointtopopoint = geompointtopo.asPoint()
                nearestinfralinid, dist = self.dbase.dbasetables['Infralineaire']['widget'].getNearestId(geompointtopopoint,
                                                                                                   comefromcanvas=False)
                # print(geompointtopo, nearestinfralinid, dist)
                if nearestinfralinid in self.geomfinalids:
                    # print('in nearest')
                    # print('pointtopo',pointtopo)
                    graphname = str(pointtopo[2]) + '-' + str(pointtopo[0])
                    if not graphname in datas.keys():
                        # datas[graphname]={'x':[], 'y':[] }
                        datas[graphname] ={'x':[], 'y':[], 'xy':[] }

                    distline = self.geomfinal.lineLocatePoint(geompointtopo)

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
                totallengeom = self.geomfinal.length()
                # print(totallengeom, datas[dataname]['x'],datas[dataname]['y'])
                if 0 not in datas[dataname]['x']:
                    datas[dataname]['x'] = np.insert(datas[dataname]['x'], 0, 0)
                    datas[dataname]['y'] = np.insert(datas[dataname]['y'], 0, datas[dataname]['y'][0])
                if totallengeom not in datas[dataname]['x']:
                    datas[dataname]['x'] = np.append(datas[dataname]['x'], totallengeom)
                    datas[dataname]['y'] = np.append(datas[dataname]['y'],  datas[dataname]['y'][-1])
                #print(totallengeom, datas[dataname]['x'], datas[dataname]['y'])





        # print('datas', datas)
        return datas





    def getPickResult(self):
        # print('cliekd')
        if self.sender() == self.userwdg.pushButton_pickstart:
            self.tempbutton = 'start'
        elif self.sender() == self.userwdg.pushButton_pickend:
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
            self.userwdg.lineEdit_start.setText(str(point2.x()) + ',' + str(point2.y()))
        elif self.tempbutton == 'end':
            self.userwdg.lineEdit_end.setText(str(point2.x()) + ',' + str(point2.y()))

        try:
            point1 = np.array([float(elem1) for elem1 in self.userwdg.lineEdit_start.text().split(',')])
            point2 = np.array([float(elem1) for elem1 in self.userwdg.lineEdit_end.text().split(',')])
        except ValueError:
            print('ValueError')
            return

        self.computePath(point1, point2)

    def computePath(self,  point1, point2):

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
                self.userwdg.label_pathids.setText('Pas de chemin')
                return

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

            geomfinalnodes = []
            for id, reverse in shortestids:
                # print(id, reverse)
                feat = self.getLayerFeatureById('Infralineaire', id)
                geom = feat.geometry()
                nodes = geom.asPolyline()
                if reverse:
                    nodes.reverse()
                    #geom = qgis.core.QgsGeometry.fromPolyline(nodes)
                geomfinalnodes += nodes

            geom = qgis.core.QgsGeometry.fromPolyline(geomfinalnodes)
            xform = qgis.core.QgsCoordinateTransform(self.dbase.qgiscrs ,self.canvas.mapSettings().destinationCrs())
            #success = qgis.core.QgsGeometry.fromPoint(pointfromcanvas).transform(xform)
            geomforrubberband = qgis.core.QgsGeometry(geom)
            geomforrubberband.transform(xform)
            # print(geomforrubberband.asPolyline())
            self.rubberBand.addGeometry(geomforrubberband, None)

            self.geomfinalnodes = geomfinalnodes
            self.geomfinal = qgis.core.QgsGeometry.fromPolyline(geomfinalnodes)
            self.geomfinalids = shortestids[:,0]

            # print('self.geomfinalnodes',self.geomfinalnodes)
            # print('self.geomfinal', self.geomfinal)
            # print('self.geomfinalids', self.geomfinalids)
            self.userwdg.label_pathids.setText(str(list(self.geomfinalids)))

            self.rubberBand.show()

            self.computeGraph()


    def postOnActivation(self):
        # print('post path activ')
        self.computeNXGraph()


    def computeNXGraph(self):
        self.nxgraph = networkx.Graph()

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

        query = self.dbase.query(sql)
        if len(query)>0:
            rawpoints = np.array([[[float(elem1) for elem1 in row[1].split('(')[1][:-1].split(' ')],
                                [float(elem2) for elem2 in row[2].split('(')[1][:-1].split(' ')]] for row in query])
            self.ids = np.array([row[0] for row in query])

            pointstemp = np.append(rawpoints[:,0], rawpoints[:,1] ,axis = 0)

            pointstemp1 = np.array([str(row) for row in pointstemp])

            points, index1, index2 = np.unique(pointstemp1, return_index=True,  return_inverse=True)

            pointsarr = pointstemp[index1]

            index2bis = np.transpose(np.reshape(index2, (2,-1)))

            self.nxgraph.add_edges_from([(edge[0], edge[1]) for edge in index2bis])

            self.indexnoeuds = pointsarr
            self.infralinfaces = index2bis
            self.reverseinfralinfaces = np.flip(self.infralinfaces,1)



    def postInitFeatureProperties(self, feat):
        # print('post path')
        if self.rubberBand is not None:
            self.rubberBand.reset(self.dbase.dbasetables['Infralineaire']['layer'].geometryType())
        self.userwdg.label_pathids.setText('')

        try:
            point1 = np.array([float(elem1) for elem1 in self.userwdg.lineEdit_start.text().split(',')])
            point2 = np.array([float(elem1) for elem1 in self.userwdg.lineEdit_end.text().split(',')])
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

    def exportCurrentGraph(self,w,h,exportfile):
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
                    print(pitems)
                    pitems = self.plotWdg.getPlotItem().listDataItems()
                    print(pitems)
                    for item in pitems:
                        exportplotWdg.addItem(item)
                exportplotWdg.addItem(self.plotWdg.getPlotItem())

            except:
                pass
            exporter = exporters.ImageExporter(exportplotWdg.scene())
            exporter.export(exportfile)


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
        uipath = os.path.join(os.path.dirname(__file__), 'pathTool.ui')
        uic.loadUi(uipath, self)

