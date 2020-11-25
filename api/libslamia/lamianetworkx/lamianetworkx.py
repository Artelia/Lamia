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

        # the global graph computed
        self.nxgraph = None
        # list of edge pks
        # old : use networkx.get_edge_attributes(self.nxgraph, "pk").values()
        self.edgespks = None
        # list of node geom in same order as self.nxgraph.nodes()
        # old : use list(networkx.get_node_attributes(self.nxgraph, "xy").values())
        self.nodegeom = None
        # old - same as self.nxgraph.edges()
        self.edgesnodeindex = None
        # old - same as np.flip(np.array(self.nxgraph.edges()), 1)
        self.edgesreversenodeindex = None

        #: list of pk of nodes linked by tolerance
        self.tolerancenodepk = None

    def __________________GraphCreation():
        pass

    def computeNXGraph(self, listpks=[], graphtype="geographic", tolerance=0.0):
        if graphtype == "geographic":
            self.computeNXGraphGeographic(listpks=listpks, tolerance=tolerance)
        elif graphtype == "topologic":
            self.computeNXGraphTopologic(listpks=listpks)

    def computeNXGraphTopologic(self, listpks=[]):
        debug = False
        nxgraph = pks = indexnoeuds = infralinfaces = reverseinfralinfaces = None
        nxgraph = networkx.Graph()

        # get nodes
        if self.dbase.base3version:
            sql = "SELECT pk_node, X(geom), Y(geom) FROM node_now"
        else:
            sql = "SELECT pk_noeud, X(geom), Y(geom) FROM Noeud_now"
        sql = self.dbase.sqlNow(sql)
        query = self.dbase.query(sql)

        if len(query) == 0:
            return

        nodepkxy = np.array(query, dtype=np.float64)
        nodepkxy[:, 0] = nodepkxy[:, 0].astype(int)
        # remove none
        nodepkxy = nodepkxy[np.all(nodepkxy != None, axis=1)]
        # remove np.nan
        nodepkxy = nodepkxy[~np.isnan(nodepkxy).any(axis=1)]

        for pk_node, x, y in nodepkxy:
            nxgraph.add_node(pk_node, xy=[x, y])
        if self.dbase.base3version:
            sql = " SELECT edge_now.pk_edge, startnode.pk_node, endnode.pk_node FROM edge_now \
                    INNER JOIN node_now as startnode ON edge_now.lid_descriptionsystem_1 = startnode.id_descriptionsystem \
                    INNER JOIN node_now as endnode ON edge_now.lid_descriptionsystem_2 = endnode.id_descriptionsystem     "
        else:
            sql = " SELECT Infralineaire_now.pk_infralineaire, startnode.pk_noeud, endnode.pk_noeud FROM Infralineaire_now \
                    INNER JOIN Noeud_now as startnode ON Infralineaire_now.lid_descriptionsystem_1 = startnode.id_descriptionsystem \
                    INNER JOIN Noeud_now as endnode ON Infralineaire_now.lid_descriptionsystem_2 = endnode.id_descriptionsystem     "
        sql = self.dbase.sqlNow(sql)
        query = self.dbase.query(sql)
        for pk_edge, pk_startnode, pk_endnode in query:
            nxgraph.add_edge(pk_startnode, pk_endnode, pk=pk_edge)

        self.nxgraph = nxgraph

        nodes = np.asarray(
            list(networkx.get_node_attributes(self.nxgraph, "xy").values())
        )

    def computeNXGraphGeographic(self, listpks=[], tolerance=0.0):
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
        # print("computeNXGraphGeographic", listpks)
        debug = False
        nxgraph = pks = indexnoeuds = infralinfaces = reverseinfralinfaces = None
        nxgraph = networkx.Graph()

        if self.dbase.base3version:
            sql = "SELECT edge_now.pk_edge, \
                 X(ST_StartPoint(edge_now.geom)), Y(ST_StartPoint(edge_now.geom)), \
                 X(ST_EndPoint(edge_now.geom)), Y(ST_EndPoint(edge_now.geom))\
                FROM edge_now "

            if listpks:
                if len(listpks) == 1:
                    sql += " WHERE edge_now.pk_edge = " + str(listpks[0])
                else:
                    sql += " WHERE edge_now.pk_edge IN " + str(tuple(listpks))
        else:
            sql = "SELECT Infralineaire_now.pk_infralineaire, \
                 X(ST_StartPoint(Infralineaire_now.geom)), Y(ST_StartPoint(Infralineaire_now.geom)), \
                 X(ST_EndPoint(Infralineaire_now.geom)), Y(ST_EndPoint(Infralineaire_now.geom))\
                 FROM Infralineaire_now "
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

        if len(query) > 0:
            rawpoints = []
            pks = []

            nodepkxy = np.array(query, dtype=np.float64)
            nodepkxy[:, 0] = nodepkxy[:, 0].astype(int)
            # remove None value
            nodepkxy = nodepkxy[np.all(nodepkxy != None, axis=1)]
            # remove np.nan
            nodepkxy = nodepkxy[~np.isnan(nodepkxy).any(axis=1)]

            self.tolerancenodepk = []

            for i, row in enumerate(nodepkxy):
                npstartnode = row[1:3]
                npendnode = row[3:5]
                npstartnodes = nodepkxy[:, 1:3]
                npendnodes = nodepkxy[:, 3:5]

                for npnode in [npstartnode, npendnode]:
                    for npnodes in [npstartnodes, npendnodes]:
                        # find index in npnodes where npnode equal npnodes
                        npindexrealequal = np.where(np.all(npnodes == npnode, axis=1))[
                            0
                        ]
                        # find index in npnodes where npnode within tolerance from npnodes
                        dist1 = np.linalg.norm(npnodes - npnode, axis=1)
                        npindextolerance = np.where(dist1 < tolerance)[0]
                        # remove  from npindextolerance index that are equal
                        npindextolerance = np.delete(
                            npindextolerance,
                            np.where(npindextolerance == npindexrealequal),
                        )
                        # if npindextolerance is not null, change point value in origin array (nodepkxy)
                        # and add edge pk values in tolerancenodepk
                        if npindextolerance.size == 0:
                            continue
                        npnodes[npindextolerance] = npnode
                        self.tolerancenodepk.append(
                            [row[0], nodepkxy[npindextolerance, 0].tolist()]
                        )

            edgepks = nodepkxy[:, 0].astype(int)

            # compute unique points for graph
            flattenxystartend = np.concatenate((nodepkxy[:, 1:3], nodepkxy[:, 3:5]))

            uniquepoints, uniqueindexfromoriginal, uniqueindextooriginal = np.unique(
                flattenxystartend, return_index=True, return_inverse=True, axis=0
            )

            nodegeombyindex = flattenxystartend[uniqueindexfromoriginal]

            listedgenodedefined = np.transpose(
                np.reshape(uniqueindextooriginal, (2, -1))
            )

            lstedgepk = np.insert(listedgenodedefined, 2, edgepks, axis=1)
            for edge1, edge2, edgepk in lstedgepk:
                nxgraph.add_edge(edge1, edge2, pk=edgepk)

            for nodeindex in nxgraph.nodes():
                nxgraph.node[nodeindex]["xy"] = nodegeombyindex[nodeindex].tolist()

            npedges = listedgenodedefined
            npreverseedges = np.flip(listedgenodedefined, 1)

            self.nxgraph = nxgraph
            self.edgespks = edgepks
            self.nodegeom = nodegeombyindex
            self.edgesnodeindex = npedges
            self.edgesreversenodeindex = npreverseedges

    def getSubGraphs(self):
        # return networkx.connected_component_subgraphs(self.nxgraph)
        return [
            self.nxgraph.subgraph(c).copy()
            for c in networkx.connected_components(self.nxgraph)
        ]

    def getSubGraphsEdgePks(self):
        edgenodepks = []
        for nxsubdomain in self.getSubGraphs():
            edgesdata = nxsubdomain.edges.data("pk")
            edgespk = [elem[2] for elem in edgesdata]
            edgenodepks.append(edgespk)

        return edgenodepks

    def __________________GraphFunctions():
        pass

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

    def __________________ShortestPathFunctions():
        pass

    def getShortestPath(self, indexstart, indexstop):
        return networkx.shortest_path(self.nxgraph, indexstart, indexstop)

    def __________________GraphToGisLayerfunctions():
        pass

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
            return

        node1index, node1geom = self.nearestNode(point1)
        node2index, node2geom = self.nearestNode(point2)

        try:
            shortestpathedges = networkx.shortest_path(
                self.nxgraph, node1index, node2index
            )
        except networkx.exception.NetworkXNoPath:
            return None, None

        shortestpks = self.getInfralineairePkFromNxEdges(shortestpathedges)
        geomfinal = self.getQgsGeomFromPks(shortestpks)

        return geomfinal, shortestpks

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
            print("nograph")
            return
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

            edgesnodeindex = np.array([e for e in self.nxgraph.edges()])
            edgesreversenodeindex = np.flip(edgesnodeindex, 1)
            edgespks = np.array(
                list(networkx.get_edge_attributes(self.nxgraph, "pk").values())
            )
            reverse = 0  # not reverse
            index = np.where(np.all(edgesnodeindex == singlepath, axis=1))[0]
            # print('index1', index)
            if len(index) == 0:
                index = np.where(np.all(edgesreversenodeindex == singlepath, axis=1))[0]
                reverse = 1
            # print(ids)
            # print('index2', index)
            shortestids.append([edgespks[index[0]], reverse])
        shortestids = np.array(shortestids)
        return shortestids

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

    def __________________VizFunctions():
        pass

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

    def nearestNode(self, pointaslist):
        # closest point
        # def closest_node(node, nodes):
        # nodes = np.asarray(self.nodegeom)
        nxindexvalues = networkx.get_node_attributes(self.nxgraph, "xy")
        nxindexes = np.array(list(nxindexvalues.keys()))
        nodesgeom = np.array(list(nxindexvalues.values()))

        # nodes = np.asarray(
        #     list(networkx.get_node_attributes(self.nxgraph, "xy").values())
        # )

        nodegeom = np.array(pointaslist)
        dist_2 = np.sum((nodesgeom - nodegeom) ** 2, axis=1)
        npindex = np.argmin(dist_2)
        indexnode = nxindexes[npindex]
        geomnode = nodesgeom[npindex]
        return indexnode, geomnode
