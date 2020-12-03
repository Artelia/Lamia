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

# from Lamia.api.dbasemanager.dbaseparserabstract import AbstractDBaseParser
from Lamia.config.base3.dbase.base3_crud_topologic import TopologicLamiaORM
import qgis.core


class LamiaORM(TopologicLamiaORM):
    def __init__(self, dbase):
        super().__init__(dbase)

    # *********** ASSETS ********************

    class Node(TopologicLamiaORM.Node):
        def update(self, pk, valuesdict):
            super().update(pk, valuesdict)
            self.orm._manageLinkedDeficiency(pk, valuesdict, "node")

    class Surface(TopologicLamiaORM.AbstractTableOrm):
        def update(self, pk, valuesdict):
            super().update(pk, valuesdict)
            self.orm._manageLinkedDeficiency(pk, valuesdict, "polygon")

    def _manageLinkedDeficiency(self, pk, valuesdict, geomtype):
        if geomtype == "node":
            valsnode = self.node.read(pk)
            res = self.deficiency[
                f"lid_descriptionsystem = {valsnode['id_descriptionsystem']} AND lpk_revision_end IS NULL"
            ]
            if not res:
                self._createNewNodeDeficiency(valsnode)
            else:
                newgeom = self._wktPointToLine(valsnode["geom"])
                pkdef = res[0]["pk_deficiency"]
                self.deficiency.update(pkdef, {"geom": newgeom})
        elif geomtype == "polygon":
            valsnode = self.surface.read(pk)
            res = self.deficiency[
                f"lid_descriptionsystem = {valsnode['id_descriptionsystem']} AND lpk_revision_end IS NULL"
            ]
            if not res:
                self._createNewSurfaceDeficiency(valsnode)
            else:
                newgeom = self._wktPolygonToLine(valsnode["geom"])
                pkdef = res[0]["pk_deficiency"]
                self.deficiency.update(pkdef, {"geom": newgeom})

    def _createNewNodeDeficiency(self, nodevals):
        pkdef = self.deficiency.create()
        newgeom = self._wktPointToLine(nodevals["geom"])
        self.deficiency.update(
            pkdef,
            {
                "deficiencycategory": "NOD",
                "lid_descriptionsystem": nodevals["id_descriptionsystem"],
                "geom": newgeom,
            },
        )

    def _createNewSurfaceDeficiency(self, nodevals):
        pkdef = self.deficiency.create()
        newgeom = self._wktPolygonToLine(nodevals["geom"])
        self.deficiency.update(
            pkdef,
            {
                "deficiencycategory": "SUR",
                "lid_descriptionsystem": nodevals["id_descriptionsystem"],
                "geom": newgeom,
            },
        )

    def _wktPointToLine(self, wktstr):
        qgisgeompoint = qgis.core.QgsGeometry.fromWkt(wktstr).asPoint()
        finalgeom = qgis.core.QgsGeometry.fromPolylineXY(
            [qgisgeompoint, qgisgeompoint]
        ).asWkt()
        return finalgeom

    def _wktPolygonToLine(self, wktstr):
        qgisgeompoint = qgis.core.QgsGeometry.fromWkt(wktstr).asPolygon()[0]
        finalgeom = qgis.core.QgsGeometry.fromPolylineXY(qgisgeompoint).asWkt()
        return finalgeom

    # ********* RESOURCES***********

    # ********* MANAGEMENT***********

    # ************* STATE *************

