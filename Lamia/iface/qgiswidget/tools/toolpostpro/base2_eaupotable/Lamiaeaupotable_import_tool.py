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
from qgis.PyQt import uic, QtGui, QtCore
try:
    from qgis.PyQt.QtGui import (QWidget, QLabel, QFrame, QTreeWidgetItem, QHeaderView)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget, QLabel, QFrame, QTreeWidgetItem, QHeaderView)

# from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
import os
import io
import glob

from ..base2.Lamia_import_tool import ImportTool


class EaupotableImportTool(ImportTool):


    def __init__(self, **kwargs):
        super(EaupotableImportTool, self).__init__(**kwargs)
        
        

    def postImport(self,layerfeat, pkobjet=None, pkdessys=None, pksubdessys=None):


        if self.importtable in ['Noeud','Equipement']:
            sql = 'SELECT id_descriptionsystem FROM Descriptionsystem WHERE pk_descriptionsystem = ' + str(pkdessys)
            iddescriptionsystem = self.dbase.query(sql)[0][0]

            featgeom = layerfeat.geometry()

            success = featgeom.transform(self.xform)
            featgeomlinestring = qgis.core.QgsGeometry.fromPolyline([featgeom.asPoint(), featgeom.asPoint()])
            featgeomwkt = featgeomlinestring.exportToWkt()
            geomsql = "ST_GeomFromText('"
            geomsql += featgeomwkt
            geomsql += "', " + str(self.dbase.crsnumber) + ")"

            # create objet
            if False:
                lastrevision = self.dbase.maxrevision
                datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
                lastobjetid = self.dbase.getLastId('Objet') + 1
                sql = "INSERT INTO Objet (id_objet, id_revisionbegin, datecreation ) "
                sql += "VALUES(" + str(lastobjetid) + "," + str(lastrevision) + ",'" + datecreation + "');"
                query = self.dbase.query(sql)
                # self.dbase.commit()
                pkobjet = self.dbase.getLastRowId('Objet')
            pkobjet = self.dbase.createNewObjet()

            #createdesordre
            lastdesordreid = self.dbase.getLastId('Desordre') + 1
            if False:
                sql = "INSERT INTO Desordre (id_desordre, id_objet, id_revisionbegin, lk_descriptionsystem, groupedesordre, geom ) "
                sql += "VALUES(" + str(lastdesordreid) + ',' +  str(lastobjetid) + "," + str(lastrevision) + "," + str(iddescriptionsystem)
                sql += ",'NOD'," + geomsql + ");"


            sql = "INSERT INTO Desordre (id_desordre, lpk_objet,  lid_descriptionsystem, groupedesordre, geom ) "
            sql += "VALUES(" + str(lastdesordreid) + ',' + str(pkobjet) + "," + str(iddescriptionsystem)
            sql += ",'NOD'," + geomsql + ");"

            query = self.dbase.query(sql)


        


