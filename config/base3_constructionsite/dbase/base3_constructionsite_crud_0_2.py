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

    # ********* RESOURCES***********

    # ********* MANAGEMENT***********

    # ************* STATE *************
    class Deficiency(BaseLamiaORM.AbstractTableOrm):
        def update(self, pk, valuesdict):
            super().update(pk, valuesdict)
            self.orm._manageLinkedObservation(pk, valuesdict)
            
            
    def _manageLinkedObservation(self, pk, valuesdict):

        valsdef = self.deficiency.read(pk)
        res = self.observation[
            f"lid_deficiency = {valsdef['id_deficiency']} AND lpk_revision_end IS NULL"
        ]
        if not res:
            # self._createNewNodeDeficiency(valsnode)
            pkdef = self.observation.create()
            # newgeom = self._wktPointToLine(nodevals["geom"])
            self.observation.update(
                pkdef,
                {
                    "observationcategory": "PVA",
                    "lid_deficiency": valsdef["id_deficiency"],
                },
            )
            
            
