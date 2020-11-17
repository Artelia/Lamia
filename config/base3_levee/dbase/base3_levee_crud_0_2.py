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

from Lamia.api.dbasemanager.dbaseparserabstract import AbstractDBaseParser
from Lamia.config.base3.dbase.base3_crud import LamiaORM as BaseLamiaORM


class LamiaORM(BaseLamiaORM):
    def __init__(self, dbase):
        super().__init__(dbase)

    # *********** ASSETS ********************
    class Equipment(BaseLamiaORM.AbstractTableOrm):
        def update(self, pk, valuesdict):
            super().update(pk, valuesdict)

            valseqp = self.orm.equipment.read(pk)
            res = self.orm.deficiency[
                f"lid_descriptionsystem = {valseqp['id_descriptionsystem']} AND lpk_revision_end IS NULL"
            ]
            if not valseqp["equipmentcategory"] in ["OUH"]:
                return
            if not res:
                self._createNewEquipmentDeficiency(valseqp)
            else:
                pkdef = res[0]["pk_deficiency"]
                self.orm.deficiency.update(pkdef, {"geom": valseqp["geom"]})

        def _createNewEquipmentDeficiency(self, eqpvals):
            pkdef = self.orm.deficiency.create()
            self.orm.deficiency.update(
                pkdef,
                {
                    "deficiencycategory": "EQP",
                    "lid_descriptionsystem": eqpvals["id_descriptionsystem"],
                    "geom": eqpvals["geom"],
                },
            )

    # ********* RESOURCES***********

    # ********* MANAGEMENT***********

    # ************* STATE *************

