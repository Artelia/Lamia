# -*- coding: utf-8 -*-

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


import os
import io
import sys

from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar,
)

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import networkx
import numpy as np
import shutil
import logging
from pprint import pprint

import qgis
from qgis.PyQt import uic, QtGui, QtCore
from qgis.PyQt.QtWidgets import QWidget, QLabel, QFrame, QTreeWidgetItem, QHeaderView


class NetWorkCore:

    POSTPROTOOLNAME = "Networktool"

    def __init__(self, dbaseparser, messageinstance=None, qgiscanvas=None):
        # super(ExportShapefileTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil, parentwidget, parent=parent)
        self.dbase = dbaseparser
        self.messageinstance = messageinstance
        self.qgiscanvas = qgiscanvas

        # matplotlib vars
        self.figuretype = plt.figure()
        self.axtype = self.figuretype.add_subplot(111)

    """
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
        
        self.iconpath = os.path.join(os.path.dirname(__file__), 'Lamia_path_tool_icon.png')

        # ****************************************************************************************
        # properties ui
        self.groupBox_elements.setParent(None)
        self.frame_editing.setParent(None)

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
        # x=[0, self.geomfinal.length()]
        # y = [0,0]
        # self.plotWdg.plot(x, y, pen=pg.mkPen(model1.item(i, 1).data(Qt.BackgroundRole), width=2), name=tmp_name)
        if False:
            self.plotWdg.addLegend()
            for dataname in datas.keys():
                # print(dataname.split('-')[1])
                if dataname.split("-")[1] == "CRE":
                    penforgraph = pg.mkPen(
                        color="k", width=3, style=QtCore.Qt.SolidLine
                    )
                elif dataname.split("-")[1] == "TNT":
                    penforgraph = pg.mkPen(
                        color="g", width=3, style=QtCore.Qt.SolidLine
                    )
                else:
                    penforgraph = pg.mkPen(color="b", width=3, style=QtCore.Qt.DashLine)
                datavalues = datas[dataname]
                self.plotWdg.plot(
                    datavalues["x"], datavalues["y"], name=dataname, pen=penforgraph
                )

            self.plotWdg.getViewBox().autoRange(
                items=self.plotWdg.getPlotItem().listDataItems()
            )
            self.plotWdg.getViewBox().disableAutoRange()

        if True:
            for dataname in datas.keys():
                # print(dataname.split('-')[1])
                if False:
                    if dataname.split("-")[1] == "CRE":
                        penforgraph = pg.mkPen(
                            color="k", width=3, style=QtCore.Qt.SolidLine
                        )
                    elif dataname.split("-")[1] == "TNT":
                        penforgraph = pg.mkPen(
                            color="g", width=3, style=QtCore.Qt.SolidLine
                        )
                    else:
                        penforgraph = pg.mkPen(
                            color="b", width=3, style=QtCore.Qt.DashLine
                        )
                datavalues = datas[dataname]

                self.axtype.plot(datavalues["x"], datavalues["y"])
                # self.axtype.grid()
            self.figuretype.canvas.draw()
        # self.plotWdg.addLegend()

    # def getOrderedProjectedIds(self, geomprojection=None, geomprojectionids= None, layertoproject=None,constraint=''):
    def getOrderedProjectedPks(
        self, pathpksreverse=None, layertoproject=None, constraint=""
    ):
        """
        Projette sur la ligne geomprojection constituée des infralineaire d'id geomprojectionids
        les éléments du qgsvectorlayer layertoproject les plus proches de geomprojection
        :param geomprojection: la geometrie sur laquelle on se projette
        :param geomprojectionids: les id dont est constituée la geometrie sur laquelle on se projette
        :return: datas : dict : 'x' : lenght along the geomprojection
                                     'y' : pk de la couche layertoproject (choisi pour être id_..)
                                     'xy' : list with [x,y]
        """
        debug = False
        if debug:
            logging.getLogger("Lamia").debug("start")

        datas = {}
        geomprojection = self.getQgsGeomFromPks(pathpksreverse)
        geomprojectionpks = list(pathpksreverse[:, 0])

        if geomprojection is not None:
            # init la valeur retournée
            datas = {"x": [], "pk": [], "xy": []}
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

                    geompointequipement1 = qgis.core.QgsGeometry.fromPointXY(point)
                    if self.dbase.base3version:
                        nearestinfralinpk, dist = self.qgiscanvas.getNearestPk(
                            "edge", point, comefromcanvas=False
                        )
                    else:
                        nearestinfralinpk, dist = self.qgiscanvas.getNearestPk(
                            "Infralineaire", point, comefromcanvas=False
                        )

                    # nearestinfralinid = self.dbase.getLayerFeatureByPk('Infralineaire', nearestinfralinpk)['id_infralineaire']
                    if nearestinfralinpk in geomprojectionpks:
                        distline = geomprojection.lineLocatePoint(geompointequipement1)
                        datas["xy"].append([distline, int(fet.id())])
                        break
            # met en forme le resultat notamment en le classant par abscisse sur la geomprojection
            if len(datas["xy"]) > 0:
                xy = np.array(datas["xy"])
                xysorted = xy[xy[:, 0].argsort()]
                datas["x"] = xysorted[:, 0]
                datas["pk"] = xysorted[:, 1]
            layertoproject.setSubsetString("")

        return datas

    def getLongitudinalProfile(
        self,
        geomprojectionpks=None,
        datatype=None,
        graphtype="Profillong",
        tablesql=None,
    ):
        """Ask pk on first sql select and ST_AsText(geom)  on second !!!

        :param geomprojectionpks: [description], defaults to None
        :type geomprojectionpks: [type], optional
        :param datatype: [description], defaults to None
        :type datatype: [type], optional
        :param graphtype: [description], defaults to "Profillong"
        :type graphtype: str, optional
        :param tablesql: [description], defaults to None
        :type tablesql: [type], optional
        """

        geomprojection = self.getQgsGeomFromPks(geomprojectionpks)

        if geomprojection is not None:
            geomfinalbuffer = geomprojection.buffer(200, 12).asWkt()

            # request table sq in buffer
            sqlsplitted = self.dbase.utils.splitSQLSelectFromWhereOrderby(tablesql)
            if "WHERE" in sqlsplitted.keys():
                sqlsplitted["WHERE"] += " AND "
            else:
                sqlsplitted["WHERE"] = ""
            sqlsplitted[
                "WHERE"
            ] += f"WHERE ST_WITHIN(ST_MakeValid(geom), \
                                        ST_GeomFromText('{geomfinalbuffer}', {self.dbase.crsnumber}))"
            sql = self.dbase.utils.rebuildSplittedQuery(sqlsplitted)
            sql = self.dbase.sqlNow(sql)
            results = self.dbase.query(sql)

            datas = {"x": [], "id": [], "xy": []}
            for iterelem in result:
                pkelem = result[0]
                geomelem = result[1]

                qgsgeomelem = qgis.core.QgsGeometry.fromWkt(geomelem)

                geomtype = qgsgeomelem.type()
                if geomtype == 0:
                    pass

                elif geomtype == 1:
                    pass

                # startpoint
                geompointequipementpoint1 = geomequipement.asPolyline()[0]
                geompointequipement1 = qgis.core.QgsGeometry.fromPoint(
                    geompointequipementpoint1
                )
                # getNearestPk
                # def getNearestPk(self, tablename, point, comefromcanvas=True, fieldconstraint=None):
                nearestinfralinid1, dist = self.dbase.getNearestId(
                    self.dbase.dbasetables["Infralineaire"],
                    "Infralineaire",
                    geompointequipementpoint1,
                    comefromcanvas=False,
                )
                # endpoint
                geompointequipementpoint2 = geomequipement.asPolyline()[-1]
                geompointequipement2 = qgis.core.QgsGeometry.fromPoint(
                    geompointequipementpoint1
                )
                nearestinfralinid2, dist = self.dbase.getNearestId(
                    self.dbase.dbasetables["Infralineaire"],
                    "Infralineaire",
                    geompointequipementpoint2,
                    comefromcanvas=False,
                )

                if nearestinfralinid1 in geomprojectionpks:
                    # print('ok')
                    distline = geomprojection.lineLocatePoint(geompointequipement1)
                    datas["equipement"]["xy"].append([distline, int(iterequipement[0])])
                elif nearestinfralinid2 in geomprojectionpks:
                    distline = geomprojection.lineLocatePoint(geompointequipement2)
                    datas["equipement"]["xy"].append([distline, int(iterequipement[0])])

    # def getGraphData(self, geomprojection=None, geomprojectionids= None, datatype=None,graphtype='Profillong' ):
    def getGraphData(
        self, geomprojectionpks=None, datatype=None, graphtype="Profillong"
    ):
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
        if debug:
            logging.getLogger("Lamia").info("start")

        # print('getGraphData')
        # if graphtype is None:
        #    graphtype = self.userwdg.comboBox_chart_theme.currentText()

        geomprojection = self.getQgsGeomFromPks(geomprojectionpks)

        # if geomprojection is None:
        #    geomprojection = self.geomfinal
        # if geomprojectionids is None:
        #    geomprojectionids = self.geomfinalids

        # temp
        if datatype is None:
            datatype = "topographie"

        if debug:
            logging.getLogger("Lamia").info(
                "init geomprojectionpks : %s - datatype : %s - graphtype : %s",
                str(geomprojectionpks),
                str(datatype),
                str(graphtype),
            )

        datas = {}  # data[i] = ['graph type', x, y]

        if graphtype == "Profillong":
            # datas['test'] = {'x' : [0, self.geomfinal.length()], 'y' : [0,0]}
            # datas['crete'] = {'x':[], 'y':[] }
            # datas['tnarriere'] = {'x':[], 'y':[] }
            # datas['niveauprotection'] = {'x':[], 'y':[] }

            # process topographie
            if geomprojection is not None:
                geomfinalbuffer = geomprojection.buffer(200, 12).asWkt()
                if datatype == "equipement_hydraulique":
                    sql = "SELECT id_equipement, ST_AsText(geom)  FROM Equipement "
                    sql += " INNER JOIN Objet ON Objet.id_objet = Equipement.id_objet "
                    sql += (
                        "WHERE ST_WITHIN(ST_MakeValid(geom), ST_GeomFromText('"
                        + geomfinalbuffer
                        + "',"
                        + str(self.dbase.crsnumber)
                        + "))"
                    )
                    sql += " AND ( Equipement.categorie = 'RHF' or Equipement.categorie = 'RHO' or Equipement.categorie = 'OUH') "
                    sql += " AND lk_equipement IS NULL"
                    sql += (
                        " AND  Objet.Datecreation <= "
                        + "'"
                        + self.dbase.workingdate
                        + "'"
                    )
                    if self.dbase.dbasetype == "postgis":
                        sql += " AND CASE WHEN Objet.Datedestruction IS NOT NULL  "
                        sql += (
                            "THEN Objet.DateDestruction > "
                            + "'"
                            + self.dbase.workingdate
                            + "'"
                            + " ELSE TRUE END"
                        )
                    elif self.dbase.dbasetype == "spatialite":
                        sql += " AND CASE WHEN Objet.datedestruction IS NOT NULL  "
                        sql += (
                            "THEN Objet.dateDestruction > "
                            + "'"
                            + self.dbase.workingdate
                            + "'"
                            + " ELSE 1 END"
                        )

                    # print(sql)
                    query = self.dbase.query(sql)
                    result = [row for row in query]

                    datas["equipement"] = {"x": [], "id": [], "xy": []}

                    for iterequipement in result:

                        geomequipement = qgis.core.QgsGeometry.fromWkt(
                            iterequipement[1]
                        )

                        # startpoint
                        geompointequipementpoint1 = geomequipement.asPolyline()[0]
                        geompointequipement1 = qgis.core.QgsGeometry.fromPoint(
                            geompointequipementpoint1
                        )
                        nearestinfralinid1, dist = self.dbase.getNearestId(
                            self.dbase.dbasetables["Infralineaire"],
                            "Infralineaire",
                            geompointequipementpoint1,
                            comefromcanvas=False,
                        )
                        # endpoint
                        geompointequipementpoint2 = geomequipement.asPolyline()[-1]
                        geompointequipement2 = qgis.core.QgsGeometry.fromPoint(
                            geompointequipementpoint1
                        )
                        nearestinfralinid2, dist = self.dbase.getNearestId(
                            self.dbase.dbasetables["Infralineaire"],
                            "Infralineaire",
                            geompointequipementpoint2,
                            comefromcanvas=False,
                        )

                        if nearestinfralinid1 in geomprojectionpks:
                            # print('ok')
                            distline = geomprojection.lineLocatePoint(
                                geompointequipement1
                            )
                            datas["equipement"]["xy"].append(
                                [distline, int(iterequipement[0])]
                            )
                        elif nearestinfralinid2 in geomprojectionpks:
                            distline = geomprojection.lineLocatePoint(
                                geompointequipement2
                            )
                            datas["equipement"]["xy"].append(
                                [distline, int(iterequipement[0])]
                            )

                    if len(datas["equipement"]["xy"]) > 0:
                        xy = np.array(datas["equipement"]["xy"])
                        # print(xy)
                        xysorted = xy[xy[:, 0].argsort()]
                        # print(xysorted)
                        # xysorted = xy[xy[:, 0].argsort()]
                        datas["equipement"]["x"] = xysorted[:, 0]
                        datas["equipement"]["id"] = xysorted[:, 1]

                if datatype == "desordre":
                    sql = "SELECT id_desordre, ST_AsText(geom)  FROM Desordre "
                    sql += " INNER JOIN Objet ON Objet.id_objet = Desordre.id_objet "
                    sql += (
                        "WHERE ST_WITHIN(ST_MakeValid(geom), ST_GeomFromText('"
                        + geomfinalbuffer
                        + "',"
                        + str(self.dbase.crsnumber)
                        + "))"
                    )
                    sql += (
                        " AND  Objet.Datecreation <= "
                        + "'"
                        + self.dbase.workingdate
                        + "'"
                    )
                    if self.dbase.dbasetype == "postgis":
                        sql += " AND CASE WHEN Objet.Datedestruction IS NOT NULL  "
                        sql += (
                            "THEN Objet.DateDestruction > "
                            + "'"
                            + self.dbase.workingdate
                            + "'"
                            + " ELSE TRUE END"
                        )
                    elif self.dbase.dbasetype == "spatialite":
                        sql += " AND CASE WHEN Objet.datedestruction IS NOT NULL  "
                        sql += (
                            "THEN Objet.dateDestruction > "
                            + "'"
                            + self.dbase.workingdate
                            + "'"
                            + " ELSE 1 END"
                        )

                    # print(sql)
                    query = self.dbase.query(sql)
                    result = [row for row in query]
                    # print('result',result)

                    datas["desordre"] = {"x": [], "id": [], "xy": []}
                    for iterdesordre in result:
                        print(iterdesordre[1])
                        if iterdesordre[1] is not None:
                            geomdesordre = qgis.core.QgsGeometry.fromWkt(
                                iterdesordre[1]
                            )

                            # startpoint
                            geompointdesordrepoint1 = geomdesordre.asPolyline()[0]
                            geompointdesordre1 = qgis.core.QgsGeometry.fromPoint(
                                geompointdesordrepoint1
                            )
                            nearestinfralinid1, dist = self.dbase.getNearestId(
                                self.dbase.dbasetables["Infralineaire"],
                                "Infralineaire",
                                geompointdesordrepoint1,
                                comefromcanvas=False,
                            )
                            # endpoint
                            geompointdesordrepoint2 = geomdesordre.asPolyline()[-1]
                            geompointdesordre2 = qgis.core.QgsGeometry.fromPoint(
                                geompointdesordrepoint1
                            )
                            nearestinfralinid2, dist = self.dbase.getNearestId(
                                self.dbase.dbasetables["Infralineaire"],
                                "Infralineaire",
                                geompointdesordrepoint2,
                                comefromcanvas=False,
                            )

                            if nearestinfralinid1 in geomprojectionpks:
                                # print('ok')
                                distline = geomprojection.lineLocatePoint(
                                    geompointdesordre1
                                )
                                datas["desordre"]["xy"].append(
                                    [distline, int(iterdesordre[0])]
                                )
                            elif nearestinfralinid2 in geomprojectionpks:
                                distline = geomprojection.lineLocatePoint(
                                    geompointdesordre2
                                )
                                datas["desordre"]["xy"].append(
                                    [distline, int(iterdesordre[0])]
                                )

                    if len(datas["desordre"]["xy"]) > 0:
                        xy = np.array(datas["desordre"]["xy"])
                        # print(xy)
                        xysorted = xy[xy[:, 0].argsort()]
                        # print(xysorted)
                        # xysorted = xy[xy[:, 0].argsort()]
                        datas["desordre"]["x"] = xysorted[:, 0]
                        datas["desordre"]["id"] = xysorted[:, 1]

                elif datatype == "topographie":

                    sql = "SELECT typepointtopo, zmngf,topographie_qgis.pk_topographie, ST_AsText(geom)  FROM Topographiedata "
                    sql += " INNER JOIN topographie_qgis ON topographie_qgis.pk_topographie = Topographiedata.lpk_topographie "
                    sql += (
                        "WHERE ST_WITHIN(geom, ST_GeomFromText('"
                        + geomfinalbuffer
                        + "',"
                        + str(self.dbase.crsnumber)
                        + "));"
                    )
                    query = self.dbase.query(sql)
                    result = [row[0:4] for row in query]
                    # print(result)

                    for pointtopo in result:
                        geompointtopo = qgis.core.QgsGeometry.fromWkt(pointtopo[3])
                        geompointtopopoint = geompointtopo.asPoint()

                        nearestinfralinpk, dist = self.qgiscanvas.getNearestPk(
                            "Infralineaire", geompointtopopoint, comefromcanvas=False
                        )
                        # nearestinfralinid = self.dbase.getLayerFeatureByPk('Infralineaire', nearestinfralinpk)['id_infralineaire']

                        # print(geompointtopo, nearestinfralinid, dist)
                        if nearestinfralinpk in geomprojectionpks:
                            # print('in nearest')
                            # print('pointtopo',pointtopo)
                            graphname = str(pointtopo[2]) + "-" + str(pointtopo[0])
                            if not graphname in datas.keys():
                                # datas[graphname]={'x':[], 'y':[] }
                                datas[graphname] = {"x": [], "y": [], "xy": []}

                            distline = geomprojection.lineLocatePoint(geompointtopo)

                            datas[graphname]["xy"].append([distline, pointtopo[1]])
                            # datas[graphname]['y'].append(pointtopo[1])

                    for dataname in datas.keys():
                        # print('***********')
                        xy = np.array(datas[dataname]["xy"])
                        # print(xy)
                        xyforunique = np.array(
                            [
                                str(datas[dataname]["xy"][i])
                                for i in range(len(datas[dataname]["xy"]))
                            ]
                        )
                        # print(xyforunique)
                        xyuniquetemp, index1, index2 = np.unique(
                            xyforunique, return_index=True, return_inverse=True
                        )
                        # print(xyuniquetemp)
                        xyunique = xy[index1]
                        # print(xyunique)
                        # pointstemp1 = np.array([str(row) for row in pointstemp])

                        # points, index1, index2 = np.unique(pointstemp1, return_index=True, return_inverse=True)

                        xysorted = xyunique[xyunique[:, 0].argsort()]
                        # print(xysorted)
                        # xysorted = xy[xy[:, 0].argsort()]
                        datas[dataname]["x"] = xysorted[:, 0]
                        datas[dataname]["y"] = xysorted[:, 1]

                        # adapt to geomfinal
                        totallengeom = geomprojection.length()
                        # print(totallengeom, datas[dataname]['x'],datas[dataname]['y'])
                        if 0 not in datas[dataname]["x"]:
                            datas[dataname]["x"] = np.insert(datas[dataname]["x"], 0, 0)
                            datas[dataname]["y"] = np.insert(
                                datas[dataname]["y"], 0, datas[dataname]["y"][0]
                            )
                        if totallengeom not in datas[dataname]["x"]:
                            datas[dataname]["x"] = np.append(
                                datas[dataname]["x"], totallengeom
                            )
                            datas[dataname]["y"] = np.append(
                                datas[dataname]["y"], datas[dataname]["y"][-1]
                            )
                        # print(totallengeom, datas[dataname]['x'], datas[dataname]['y'])

        # print('datas', datas)
        return datas

    def getPickResult(self):
        # print('cliekd')
        if self.sender() == self.userwdgfield.pushButton_pickstart:
            self.tempbutton = "start"
        elif self.sender() == self.userwdgfield.pushButton_pickend:
            self.tempbutton = "end"
        self.pointEmitter.canvasClicked.connect(self.selectPickedFeature)
        self.canvas.setMapTool(self.pointEmitter)

    """
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
    """

    # def computePath(self,  point1, point2, alsocomputegraph=True):
    def getQgisgeomBetweenPoints(self, point1, point2):
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
            self.computeNXGraph()

        point1 = np.array(point1)
        point2 = np.array(point2)
        if self.nodegeom is not None:
            dist1 = np.linalg.norm(self.nodegeom - point1, axis=1)
            index = np.where(dist1 == np.amin(dist1))
            networkpoint1 = index[0][0]
            dist2 = np.linalg.norm(self.nodegeom - point2, axis=1)
            index = np.where(dist2 == np.amin(dist2))
            networkpoint2 = index[0][0]

            try:
                shortestpathedges = networkx.shortest_path(
                    self.nxgraph, networkpoint1, networkpoint2
                )
                # print('shortestpathedges', shortestpathedges)
            except networkx.exception.NetworkXNoPath:
                print("no path")
                # self.userwdgfield.label_pathids.setText('Pas de chemin')
                return

            # shortestids = self.getIdsFromPath(shortestpathedges)
            shortestpks = self.getInfralineairePkFromNxEdges(shortestpathedges)
            # self.geomfinal = self.getQgsGeomFromPks(shortestpks)
            geomfinal = self.getQgsGeomFromPks(shortestpks)

            return geomfinal, shortestpks
            """
            # print(self.geomfinal.asPolyline())
            # xform = qgis.core.QgsCoordinateTransform(self.dbase.qgiscrs ,self.canvas.mapSettings().destinationCrs())
            #success = qgis.core.QgsGeometry.fromPoint(pointfromcanvas).transform(xform)
            geomforrubberband = qgis.core.QgsGeometry(self.geomfinal)
            #geomforrubberband.transform(xform)
            geomforrubberband.transform(self.dbase.xform)
            # print(geomforrubberband.asPolyline())
            self.rubberBand.addGeometry(geomforrubberband, None)

            if len(shortestpks)>0:
                #self.geomfinalnodes = geomfinalnodes
                #self.geomfinal = qgis.core.QgsGeometry.fromPolyline(geomfinalnodes)
                self.geomfinalids = shortestpks[:,0]

                # print('self.geomfinalnodes',self.geomfinalnodes)
                # print('self.geomfinal', self.geomfinal)
                # print('self.geomfinalids', self.geomfinalids)
                self.userwdgfield.label_pathids.setText(str(list(self.geomfinalids)))

                self.rubberBand.show()
            else:
                self.geomfinalnodes = None
                self.geomfinal = None
                self.geomfinalids = []
            """
            if alsocomputegraph:
                self.computeGraph()

    # def getIdsFromPath(self,pathedges, ids=None, infralinfaces=None, reverseinfralinfaces=None):
    def getInfralineairePkFromNxEdges(self, nxpathedges):
        """
        :param pathedges: the edges of the path
        :return: np.array [..[id, reverse = True/False : if the geom is in the same direction of path edge]...]
        """
        # print('getIdsFromPath',pathedges)
        if self.nxgraph is None:
            self.computeNXGraph()
        # if ids is None and infralinfaces is None and reverseinfralinfaces is None  :
        #    if self.nxgraph is None:
        #        self.computeNXGraphForAll()
        #    ids = self.ids
        #    infralinfaces = self.infralinfaces
        #    reverseinfralinfaces = self.reverseinfralinfaces
        shortestids = []

        # print('***********************getIdsFromPath***')
        # print(pathedges)
        # print(ids)

        for i in range(len(nxpathedges) - 1):
            singlepath = [nxpathedges[i], nxpathedges[i + 1]]

            # print(singlepath)
            # print('infra', infralinfaces)
            # print()
            reverse = 0  # not reverse
            index = np.where(np.all(self.edgesnodeindex == singlepath, axis=1))[0]
            # print('index1', index)
            if len(index) == 0:
                index = np.where(
                    np.all(self.edgesreversenodeindex == singlepath, axis=1)
                )[0]
                reverse = 1
            # print(ids)
            # print('index2', index)
            shortestids.append([self.edgespks[index[0]], reverse])
        shortestids = np.array(shortestids)
        return shortestids

    # def getGeomFromIds(self,ids):
    def getQgsGeomFromPks(self, pksreverse):
        """
        convertie une serie d'ids qui forment un path en polyligne
        :param ids: les ids dont on veut assembler la geometrie
        :return: la geometrie
        """
        geomfinalnodes = []
        # for id, reverse in ids:
        for pk, reversebool in pksreverse:
            # print('id, reverse', id, reverse)
            # feat = self.dbase.getLayerFeatureById('Infralineaire', id)
            # geom = feat.geometry()
            if self.dbase.base3version:
                geomtxt = self.dbase.getValuesFromPk("edge", "ST_AsText(geom)", pk)
            else:
                geomtxt = self.dbase.getValuesFromPk(
                    "Infralineaire", "ST_AsText(geom)", pk
                )
            geom = qgis.core.QgsGeometry.fromWkt(geomtxt).asPolyline()
            # nodes = geom.asPolyline()
            if reversebool:
                geom.reverse()
                # geom = qgis.core.QgsGeometry.fromPolyline(nodes)
            geomfinalnodes += geom

        geom = qgis.core.QgsGeometry.fromPolylineXY(geomfinalnodes)
        return geom

    """
    def postOnActivation(self):
        # print('post path activ')
        self.computeNXGraphForAll()
        #self.nxgraph, self.indexnoeuds, self.infralinfaces, self.reverseinfralinfaces= self.computeNXGraph()


    def computeNXGraphForAll(self):
        debug = False
        #self.nxgraph, self.nodepks, self.nodeindex, self.infralinfaces, self.reverseinfralinfaces = self.computeNXGraph()
        self.nxgraph, self.edgespks, self.nodegeom, self.edgesnodeindex, self.edgesreversenodeindex = self.computeNXGraph()
        if debug:
            pprint('self.nxgraph :')
            pprint(self.nxgraph)
            print('self.edgespks : ')
            pprint(self.edgespks)
            print('self.nodegeom : ')
            pprint(self.nodegeom)
            print('self.edgesnodeindex : ')
            pprint(self.edgesnodeindex)
            print('self.edgesreversenodeindex : ')
            pprint(self.edgesreversenodeindex)
    """

    # def computeNXGraph(self, listids=None):
    def computeNXGraph(self, listpks=[]):
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
        debug = False
        nxgraph = pks = indexnoeuds = infralinfaces = reverseinfralinfaces = None
        nxgraph = networkx.Graph()

        # sql = "SELECT Infralineaire_qgis.id_infralineaire,"
        # sql += " ST_AsText(ST_StartPoint(Infralineaire_qgis.geom)), ST_AsText(ST_EndPoint(Infralineaire_qgis.geom))"
        # sql += " FROM Infralineaire_qgis "
        # sql += ' WHERE '
        # sql += self.dbase.dateVersionConstraintSQL()
        if self.dbase.base3version:
            sql = (
                "SELECT edge_now.pk_edge, "
                "ST_AsText(ST_StartPoint(edge_now.geom)), ST_AsText(ST_EndPoint(edge_now.geom)) "
                "FROM edge_now "
            )
            if listpks:
                if len(listpks) == 1:
                    sql += " WHERE edge_now.pk_edge = " + str(listpks[0])
                else:
                    sql += " WHERE edge_now.pk_edge IN " + str(tuple(listpks))
        else:
            sql = (
                "SELECT Infralineaire_now.pk_infralineaire, "
                "ST_AsText(ST_StartPoint(Infralineaire_now.geom)), ST_AsText(ST_EndPoint(Infralineaire_now.geom)) "
                "FROM Infralineaire_now "
            )
            if listpks:
                if len(listpks) == 1:
                    sql += " WHERE Infralineaire_now.pk_infralineaire = " + str(
                        listpks[0]
                    )
                else:
                    sql += " WHERE Infralineaire_now.pk_infralineaire IN " + str(
                        tuple(listpks)
                    )
        sql = self.dbase.sqlNow(sql)
        query = self.dbase.query(sql)
        # print('sql', sql, query)
        if len(query) > 0:
            rawpoints = []
            # ids=[]
            pks = []
            for row in query:
                # print(row[1], row[2])
                # print([float(elem1) for elem1 in row[1].split('(')[1][:-1].split(' ')])
                if row[1] is not None and row[2] is not None:
                    x = [float(elem1) for elem1 in row[1].split("(")[1][:-1].split(" ")]
                    y = [float(elem2) for elem2 in row[2].split("(")[1][:-1].split(" ")]
                    rawpoints.append([x, y])
                    # startpoints.append([float(elem1) for elem1 in row[1].split('(')[1][:-1].split(' ')])
                    # endpoints.append([float(elem2) for elem2 in row[2].split('(')[1][:-1].split(' ')])
                    pks.append(row[0])
                # print([float(elem1) for elem1 in row[1].split('(')[1][:-1].split(' ')])
                # print([float(elem2) for elem2 in row[2].split('(')[1][:-1].split(' ')])

            pks = np.array(pks)
            rawpoints = np.array(rawpoints)

            # create 1d array with startxy1, startxy2, ..., startxyn, endxy1, endxyy2, ...,endxyn
            pointstemp = np.append(rawpoints[:, 0], rawpoints[:, 1], axis=0)
            # convert to string to manage np.unique with couple of xy
            pointstemp1 = np.array([str(row) for row in pointstemp])
            # get unique point with index compared to pointstemp1
            points, index1, index2 = np.unique(
                pointstemp1, return_index=True, return_inverse=True
            )
            # list of unique points
            pointsarr = pointstemp[index1]  # the uniques points
            # list of unique point index compared to pointstemp1
            index2bis = np.transpose(np.reshape(index2, (2, -1)))
            #
            nxgraph.add_edges_from([(edge[0], edge[1]) for edge in index2bis])
            indexnoeuds = pointsarr
            infralinfaces = index2bis
            reverseinfralinfaces = np.flip(infralinfaces, 1)

        (
            self.nxgraph,
            self.edgespks,
            self.nodegeom,
            self.edgesnodeindex,
            self.edgesreversenodeindex,
        ) = (nxgraph, pks, indexnoeuds, infralinfaces, reverseinfralinfaces)

        if debug:
            pprint("self.nxgraph :")
            pprint(self.nxgraph)
            print("self.edgespks : ")
            pprint(self.edgespks)
            print("self.nodegeom : ")
            pprint(self.nodegeom)
            print("self.edgesnodeindex : ")
            pprint(self.edgesnodeindex)
            print("self.edgesreversenodeindex : ")
            pprint(self.edgesreversenodeindex)

    def getSubGraphs(self):
        # return networkx.connected_component_subgraphs(self.nxgraph)
        return [
            self.nxgraph.subgraph(c).copy()
            for c in networkx.connected_components(self.nxgraph)
        ]

    def getShortestPath(self, indexstart, indexstop):
        return networkx.shortest_path(self.nxgraph, indexstart, indexstop)

    def getExtremityNodeIndexFromLinearGraph(self, nxgraph):
        npedges = np.ravel(list(nxgraph.edges()))
        unique, counts = np.unique(npedges, return_counts=True)
        edgeextremite = unique[np.where(counts == 1)]
        edgenoeud = unique[np.where(counts > 2)]

        if len(edgenoeud) > 0:  # graph is not a line
            return None
        else:
            return list(
                edgeextremite
            )  # logiquement cette list comporte deux elements : le noeud de depart et d 'arrivee

    """
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
        if False:
            try:
                self.plotWdg.scene().sigMouseMoved.disconnect(self.mouseMovedPyQtGraph)
            except Exception as e:
                print(e)
        try:
            self.pointEmitter.canvasClicked.disconnect(self.selectPickedFeature)
        except Exception as e:
            print(e)
    """

    def exportCurrentGraph(self, point1, point2, datatype, graphtype, w, h, exportfile):

        debug = False

        if debug:
            logging.getLogger("Lamia").info("start")

        # geomfinal, shortestpks = self.computePath(point1, point2, alsocomputegraph=False)
        geomfinal, shortestpks = self.getQgisgeomBetweenPoints(point1, point2)
        if debug:
            logging.getLogger("Lamia").info(
                "path %s %s", str(self.geomfinal), str(self.geomfinalids)
            )

        datas = self.getGraphData(
            geomprojectionpks=shortestpks, datatype=datatype, graphtype=graphtype
        )
        # geomprojectionpks= None, datatype=None,graphtype='Profillong' )
        if debug:
            logging.getLogger("Lamia").info("datas %s", str(datas))

        self.axtype.cla()
        self.figuretype.set_size_inches(w / 25.4, h / 25.4)

        if len(datas) == 0:
            src_file = os.path.join(
                os.path.dirname(__file__), "..", "..", "DBASE", "utils", "blank.png"
            )
            shutil.copyfile(src_file, exportfile)
            return

        if datatype == "topographie":
            for dataname in datas.keys():
                # print('*****')
                datavalues = datas[dataname]
                label = []
                topopk = int(dataname.split("-")[0].strip())
                # print(topoid)
                # topofet = self.dbase.getLayerFeatureById('Topographie',int(topopk))
                # idressource = self.dbase.getValuesFromPk('Topographie_qgis', 'id_ressource',topofet.id() )
                ## idressource = self.dbase.getLayerFeatureById('Topographie',int(topoid))['id_ressource']
                ## print(idressource)
                # nom = self.dbase.getLayerFeatureById('Ressource',idressource)['Description']

                nom = self.dbase.getValuesFromPk(
                    "Topographie_qgis", "Description", topopk
                )

                # print(nom)
                if nom is None:
                    nom = "test"
                label.append(nom)
                label.append(
                    self.dbase.getConstraintTextFromRawValue(
                        "Pointtopo", "typepointtopo", dataname.split("-")[1].strip()
                    )
                )
                labelname = "-".join(label)
                self.axtype.plot(datavalues["x"], datavalues["y"], label=labelname)

        legend = self.axtype.legend(
            bbox_to_anchor=(0.0, 1.0),
            loc="lower left",
            bbox_transform=self.figuretype.transFigure,
            prop={"size": 8},
        )
        self.axtype.set_ylabel("Altitude m NGF", fontsize=8)
        self.figuretype.savefig(exportfile, bbox_inches="tight", dpi=150)

    def resizewidget(self, w, h):

        if False:
            self.plotWdg.resize(w, h)
        if True:
            win = pg.GraphicsWindow()
            win.resize(w, h)
        if True:
            export_area = pg.GraphicsLayoutWidget(border=(50, 50, 50))
            export_area.setBackground("w")
            export_area.resize(w, h)
            export_area.setVisible(True)
            export_area.setVisible(False)
