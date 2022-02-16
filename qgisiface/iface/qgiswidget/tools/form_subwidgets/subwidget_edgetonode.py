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
import os, logging

import qgis
from qgis.PyQt import uic, QtCore
from qgis.PyQt.QtWidgets import QWidget, QVBoxLayout, QComboBox

from .subwidget_abstract import AbstractSubWidget


class EdgeToNodeWidget(AbstractSubWidget):

    UIPATH = os.path.join(os.path.dirname(__file__), "subwidget_edgetonode_ui.ui")

    def __init__(
        self,
        parentwdg,
        lateralfield,
        upstreamnodeidfield,
        downstreamnodeidfield,
        parentframe,
    ):
        super(EdgeToNodeWidget, self).__init__(
            parentwdg=parentwdg, parentframe=parentframe
        )
        # uipath = os.path.join(os.path.dirname(__file__), 'subwidget_edgetonode_ui.ui')
        # uic.loadUi(uipath, self)

        self.parentwdg = parentwdg
        self.lateralfield = lateralfield
        self.upstreamnodeidfield = upstreamnodeidfield
        self.downstreamnodeidfield = downstreamnodeidfield

        # self.parentframe = parentframe
        # if self.parentframe.layout() is not None:
        #     self.parentframe.layout().addWidget(self)
        # else:
        #     vlayout = QVBoxLayout()
        #     vlayout.addWidget(self)
        #     self.parentframe.setLayout(vlayout)

        self.toolButton_pickam.clicked.connect(self._pickToNode)
        self.toolButton_pickav.clicked.connect(self._pickToNode)

        self.picksender = None

    def postSelectFeature(self):
        idup = iddown = None
        if self.parentwdg.currentFeaturePK is not None:
            sql = f"SELECT {self.upstreamnodeidfield} ,  {self.downstreamnodeidfield} \
                    FROM edge WHERE  pk_edge = {self.parentwdg.currentFeaturePK} "
            res = self.parentwdg.dbase.query(sql)
            idup, iddown = res[0]

        if idup:
            self.spinBox_lk_noeud1.setValue(idup)
        else:
            self.spinBox_lk_noeud1.setValue(-1)
        if iddown:
            self.spinBox_lk_noeud2.setValue(iddown)
        else:
            self.spinBox_lk_noeud2.setValue(-1)

    def postSaveFeature(self, parentfeaturepk=None):

        # self.currentFeature = self.dbase.getLayerFeatureByPk(self.dbasetablename, self.currentFeaturePK)
        # fetgeom = self.currentFeature.geometry().asPolyline()
        dbase = self.parentwdg.dbase
        qgiscanvas = self.parentwdg.mainifacewidget.qgiscanvas
        geomtext = dbase.getValuesFromPk(
            self.parentwdg.DBASETABLENAME, "ST_AsText(geom)", parentfeaturepk
        )
        if not qgis.core.QgsGeometry.fromWkt(geomtext):
            return
        fetgeom = qgis.core.QgsGeometry.fromWkt(geomtext).asPolyline()


        indexnodes = [1, 2]
        for indexnode in indexnodes:
            idnode = eval("self.spinBox_lk_noeud{}.value()".format(indexnode))
            if idnode > -1:
                sql = "SELECT pk_node FROM node_qgis WHERE id_descriptionsystem = {}".format(
                    idnode
                )
                query = dbase.query(sql)
                pks = [row for row in query]
                if len(pks) == 1:
                    pknoeud = pks[0][0]
                    layer = qgiscanvas.layers["node"]["layer"]
                    nearestnodepoint1 = layer.getFeature(pknoeud).geometry().asPoint()
                    if indexnode == 1:
                        order = [0, -1]
                    else:
                        order = [-1, 0]
                    if not dbase.utils.areNodesEquals(
                        fetgeom[order[0]], nearestnodepoint1
                    ):
                        if dbase.utils.areNodesEquals(
                            fetgeom[order[1]], nearestnodepoint1
                        ):
                            fetgeom = fetgeom[::-1]
                            newgeom = qgis.core.QgsGeometry.fromPolylineXY(fetgeom)
                            layer = qgiscanvas.layers["edge"]["layer"]
                            layer.startEditing()
                            success = layer.changeGeometry(parentfeaturepk, newgeom)
                            layer.commitChanges()
                        else:
                            self.spinBox_lk_noeud1.setValue(-1)
                            exec(
                                "self.spinBox_lk_noeud{}.setValue(-1)".format(indexnode)
                            )
                            self.parentwdg.formutils.saveFeatureProperties(
                                parentfeaturepk
                            )

        # self.upstreamnodeidfield = upstreamnodeidfield
        # self.downstreamnodeidfield = downstreamnodeidfield

        if self.spinBox_lk_noeud1.value() == -1:
            node1value = "NULL"
        else:
            node1value = self.spinBox_lk_noeud1.value()
        if self.spinBox_lk_noeud2.value() == -1:
            node2value = "NULL"
        else:
            node2value = self.spinBox_lk_noeud2.value()

        sql = f"UPDATE edge SET {self.upstreamnodeidfield} = {node1value}, \
                                {self.downstreamnodeidfield} = {node2value}  \
                WHERE pk_edge = {parentfeaturepk}"
        dbase.query(sql)

    def _isLateral(self):
        # searchwidget
        if isinstance(self.lateralfield, bool):
            return self.lateralfield

        wdg = self.parentwdg.formtoolwidgetconfdict[self.parentwdg.DBASETABLENAME][
            "widgets"
        ][self.lateralfield]
        if isinstance(wdg, QComboBox):
            wdgvalue = wdg.currentText()
            wdgrawvalue = int(
                self.parentwdg.dbase.getConstraintRawValueFromText(
                    "edge", self.lateralfield, wdgvalue
                )
            )
            if wdgrawvalue:
                return True
            else:
                return False

    def _pickToNode(self):
        # print('pick',self.sender())
        self.picksender = str(self.sender().objectName())
        try:
            self.parentwdg.mainifacewidget.qgiscanvas.pointEmitter.canvasClicked.disconnect()
        except Exception as e:
            print("**", e)

        self.parentwdg.mainifacewidget.qgiscanvas.pointEmitter.canvasClicked.connect(
            self._picknearestnode
        )
        self.parentwdg.mainifacewidget.qgiscanvas.canvas.setMapTool(
            self.parentwdg.mainifacewidget.qgiscanvas.pointEmitter
        )

    def _picknearestnode(self, point):

        debug = True
        typenode = False
        qgiscanvas = self.parentwdg.mainifacewidget.qgiscanvas
        dbase = self.parentwdg.dbase

        if self.picksender == "toolButton_pickam":
            editingnode = 1
        elif self.picksender == "toolButton_pickav":
            editingnode = 2

        if debug:
            logging.getLogger("Lamia").debug("edit mode %s", str(editingnode))

        # if self.toolwidgetmain.comboBox_branch.currentText()=='Faux' or editingnode == 1:
        if not self._isLateral() or editingnode == 1:
            nearestnodeid, distance = qgiscanvas.getNearestPk("node", point)
            # nearestnodefet = self.dbase.getLayerFeatureByPk('node', nearestnodeid)
            nearestnodefet = qgiscanvas.layers["node"]["layer"].getFeature(
                nearestnodeid
            )
            nearestnodepoint = nearestnodefet.geometry().asPoint()
            typenode = "NODE"
        else:
            nearestnodeid, distance = qgiscanvas.getNearestPk("edge", point)
            nearestnodeid2, distance2 = qgiscanvas.getNearestPk("node", point)

            if distance2 < distance * 1.1:
                nearestnodefet = qgiscanvas.layers["node"]["layer"].getFeature(
                    nearestnodeid2
                )
                nearestnodepoint = nearestnodefet.geometry().asPoint()
                typenode = "NODE"
            else:
                nearestnodefet = qgiscanvas.layers["edge"]["layer"].getFeature(
                    nearestnodeid
                )
                point = qgiscanvas.xformreverse.transform(point)
                nearestnodepoint = (
                    nearestnodefet.geometry()
                    .nearestPoint(qgis.core.QgsGeometry.fromPointXY(point))
                    .asPoint()
                )
                typenode = "INF"

        if typenode == "NODE":
            sql = "SELECT id_descriptionsystem FROM node_qgis WHERE pk_node = " + str(
                nearestnodefet.id()
            )
        elif typenode == "INF":
            sql = "SELECT id_descriptionsystem FROM edge_qgis WHERE pk_edge = " + str(
                nearestnodefet.id()
            )
        nearestnodeiddessys = dbase.query(sql)[0][0]

        if debug:
            logging.getLogger("Lamia").debug(
                "id,dist  %s %s", str(nearestnodeid), str(distance)
            )

        # gui things
        if editingnode == 1:
            self.spinBox_lk_noeud1.setValue(nearestnodeiddessys)
        elif editingnode == 2:
            self.spinBox_lk_noeud2.setValue(nearestnodeiddessys)

        # get the geometry before editing
        tempgeom = []
        if self.parentwdg.tempgeometry is not None:
            wkbtype = self.parentwdg.tempgeometry.wkbType()
            if wkbtype == qgis.core.QgsWkbTypes.LineString:
                tempgeom = self.parentwdg.tempgeometry.asPolyline()
            elif wkbtype == qgis.core.QgsWkbTypes.MultiLineString:
                tempgeom = self.parentwdg.tempgeometry.asMultiPolyline()[0]

        elif (
            self.parentwdg.currentFeaturePK is not None
            and self.parentwdg.tempgeometry is None
        ):
            tempfeat = qgiscanvas.layers[self.parentwdg.DBASETABLENAME][
                "layer"
            ].getFeature(self.parentwdg.currentFeaturePK)
            tempgeom = tempfeat.geometry().asPolyline()

        if debug:
            logging.getLogger("Lamia").debug("geombeforeediting %s", tempgeom)

        if len(tempgeom) >= 2:
            if editingnode == 1:
                tempgeom[0] = nearestnodepoint
            elif editingnode == 2:
                tempgeom[-1] = nearestnodepoint
        elif len(tempgeom) == 0:
            tempgeom.insert(-1, nearestnodepoint)
            tempgeom.insert(-1, nearestnodepoint)
        elif len(tempgeom) == 1:
            if editingnode == 1:
                tempgeom[0] = nearestnodepoint
            elif editingnode == 2:
                tempgeom.insert(-1, nearestnodepoint)

        if debug:
            logging.getLogger("Lamia").debug("geomafterediting %s", tempgeom)

        # update canvas
        qgiscanvas.createorresetRubberband(1)
        self.parentwdg.setTempGeometry(tempgeom, False)

        # disconnect all
        qgiscanvas.canvas.unsetMapTool(qgiscanvas.pointEmitter)
        self.picksender = None
        try:
            qgiscanvas.pointEmitter.canvasClicked.disconnect(self._picknearestnode)
        except:
            pass

