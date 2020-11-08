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
from Lamia.config.base3.dbase.base3_crud import LamiaORM as BaseLamiaORM


class LamiaORM(BaseLamiaORM):
    def __init__(self, dbase):
        super().__init__(dbase)

    # *********** ASSETS ********************

    class Node(BaseLamiaORM.AbstractTableOrm):
        def create(self, pk=None):
            savedfeaturepk = super().create(pk)
            # deficiency creation
            pkdef = self.orm.deficiency.create()
            nodegeom = self.read(savedfeaturepk)["geom"]
            self.orm.deficiency.update(
                pkdef, {"lid_descriptionsystem": 2, "geom": nodegeom}
            )
            return savedfeaturepk

        def update(self, pk, valuesdict):
            super().update(pk, valuesdict)
            nodeval = self.trigger.node.read(pk)
            nodedessys, nodegeom = nodeval["id_descriptionsystem"], nodeval["geom"]
            sql = f"SELECT pk_deficiency FROM deficiency_qgis WHERE lid_descriptionsystem = {nodedessys}\
                    AND lpk_revision_end IS NULL"
            defpks = self.dbase.query(sql)
            for defpk in defpks:
                self.trigger.deficiency.update(defpk, {"geom": nodegeom})

    # ********* RESOURCES***********

    # ********* MANAGEMENT***********

    # ************* STATE *************

