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

import qgis
from qgis.PyQt import QtCore
from qgis.PyQt.QtWidgets import (QWidget)

class TopologicNodeWidget(QtCore.QObject):

    def __init__(self, parentwdg):
        super(TopologicNodeWidget, self).__init__()
        self.parentwdg = parentwdg
        self.dbase = parentwdg.dbase
        self.formutils = parentwdg.formutils
        self.mainifacewidget = parentwdg.mainifacewidget

    def postSelectFeature(self):
        pass

    def postSaveFeature(self, parentfeaturepk=None):
        self._moveLinkedTopologicalEdge(parentfeaturepk)
   
    def _moveLinkedTopologicalEdge(self, parentfeaturepk):
        # self.currentFeaturePK = parentfeaturepk

        if parentfeaturepk is not None:
            nodeiddessys = self.dbase.getValuesFromPk('node_qgis',['id_descriptionsystem'],parentfeaturepk )
            nodegeom = self.formutils.getQgsGeomFromPk(parentfeaturepk).asPoint()

            # iterate on lid_descriptionsystem_1 and lid_descriptionsystem_2
            valuetoiterate = [1, 2]
            for indexnode in valuetoiterate:
                sql = "SELECT pk_edge, id_edge FROM edge_now "\
                      "WHERE lid_descriptionsystem_{} = {} ".format(str(indexnode ),
                                                                    str(nodeiddessys))
                sql = self.dbase.sqlNow(sql)
                result = self.dbase.query(sql)
                if indexnode == 1 :
                    indexgeom = 0
                elif indexnode == 2:
                    indexgeom = -1

                for fetpk, fetid in result:
                    geomtext = self.dbase.getValuesFromPk('edge',
                                'ST_AsText(geom)',
                                fetpk)
                    infrafetgeom = qgis.core.QgsGeometry.fromWkt(geomtext).asPolyline()

                    if not self.dbase.utils.areNodesEquals(infrafetgeom[indexgeom], nodegeom):
                        # fetpk = self.mainifacewidget.toolwidgets['toolprepro']['Troncon'][0].formutils.manageFeatureCreationOrUpdate(fetpk)
                        fetpk = self.dbase.manageFeatureCreationOrUpdate('edge', fetpk)

                        infrafetgeom[indexgeom] = nodegeom
                        newgeom = qgis.core.QgsGeometry.fromPolylineXY(infrafetgeom)

                        sql = "UPDATE edge SET geom = ST_GeomFromText('{}',{}) "\
                              " WHERE pk_edge = {}".format(newgeom.asWkt(),
                                                                    self.dbase.crsnumber,
                                                                    fetpk)
                        self.dbase.query(sql)

                        # move laterals
                        self._moveLaterals(fetpk, newgeom)

        self.mainifacewidget.qgiscanvas.layers['edge']['layerqgis'].triggerRepaint()

    def _moveLaterals(self, pkinfralin, newgeom):

        fetiddessys = self.dbase.getValuesFromPk('edge_qgis', 'id_descriptionsystem', pkinfralin)
        dbasetablelayer = self.mainifacewidget.qgiscanvas.layers['edge']['layer']
        sql = "SELECT pk_edge, id_edge FROM edge_now "\
              " WHERE lid_descriptionsystem_2 = {} ".format( str(fetiddessys))
        sql = self.dbase.sqlNow(sql)
        result2 = self.dbase.query(sql)
        for fetpk, fetid in result2:
            edgepk = self.dbase.manageFeatureCreationOrUpdate('edge', fetpk)
            geomtext = self.dbase.getValuesFromPk('edge',
                        'ST_AsText(geom)',
                        edgepk)
            infrafetgeom = qgis.core.QgsGeometry.fromWkt(geomtext).asPolyline()
            infrafetpoint1 = qgis.core.QgsGeometry().fromPointXY(infrafetgeom[0])
            newgeom2 = infrafetpoint1.shortestLine(newgeom)

            sql = "UPDATE edge SET geom = ST_GeomFromText('{}',{}) "\
                    " WHERE pk_edge = {}".format(newgeom2.asWkt(),
                                                        self.dbase.crsnumber,
                                                        edgepk)
            self.dbase.query(sql)

