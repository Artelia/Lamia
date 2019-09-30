# -*- coding: utf-8 -*-
import qgis, sys
from qgis.PyQt import uic, QtGui, QtCore
try:
    from qgis.PyQt.QtGui import (QWidget, QLabel, QFrame, QTreeWidgetItem, QHeaderView)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget, QLabel, QFrame, QTreeWidgetItem, QHeaderView)

# from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
import os
import io
import glob

from ..Base2.Lamia_import_tool import ImportTool

# ********************************************************************************************************************
# ********************************* Main Widget                *******************************************************
# ********************************************************************************************************************

class AssainissementImportTool(ImportTool):

    DBASES = ['digue','base_digue','base2_digue']
    TOOLNAME = 'IMPORT'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(AssainissementImportTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil,parentwidget, parent=parent)
        
        

    def postImport(self,layerfeat, pkobjet=None, pkdessys=None, pksubdessys=None):


        if self.importtable == 'Noeud':
            sql = 'SELECT id_descriptionsystem FROM Descriptionsystem WHERE pk_descriptionsystem = ' + str(pkdessys)
            iddescriptionsystem = self.dbase.query(sql)[0][0]

            featgeom = layerfeat.geometry()

            success = featgeom.transform(self.xform)
            if sys.version_info.major == 2:
                featgeomlinestring = qgis.core.QgsGeometry.fromPolyline([featgeom.asPoint(), featgeom.asPoint()])
                featgeomwkt = featgeomlinestring.exportToWkt()
            elif sys.version_info.major == 3:
                featgeomlinestring = qgis.core.QgsGeometry.fromPolylineXY([featgeom.asPoint(), featgeom.asPoint()])
                featgeomwkt = featgeomlinestring.asWkt()
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


        


