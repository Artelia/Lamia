# -*- coding: utf-8 -*-

import qgis
import os
# from ..toolabstract.inspectiondigue_abstractworker import AbstractWorker
from qgis.PyQt import QtGui, uic, QtCore, QtXml
from collections import OrderedDict
import datetime
import decimal
import numpy as np
import glob

#from .tools.Lamia_exportshpdialog import ExportShapefileDialog
from ..base.Lamiabase_import import importShapefileBaseWorker

#class exportShapefileWorker(AbstractWorker):


class importShapefileAssainissementWorker(importShapefileBaseWorker):


    def __init__(self, dbase=None, windowdialog=None):
        # AbstractWorker.__init__(self)

        super(importShapefileAssainissementWorker, self).__init__(dbase, windowdialog)


    def postImport(self,layerfeat, pkobjet=None, pkdessys=None, pksubdessys=None):


        if self.importtable == 'Noeud':
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
            lastrevision = self.dbase.maxrevision
            datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
            lastobjetid = self.dbase.getLastId('Objet') + 1
            sql = "INSERT INTO Objet (id_objet, id_revisionbegin, datecreation ) "
            sql += "VALUES(" + str(lastobjetid) + "," + str(lastrevision) + ",'" + datecreation + "');"
            query = self.dbase.query(sql)
            # self.dbase.commit()
            pkobjet = self.dbase.getLastRowId('Objet')

            #createdesordre
            lastdesordreid = self.dbase.getLastId('Desordre') + 1
            sql = "INSERT INTO Desordre (id_desordre, id_objet, id_revisionbegin, lk_descriptionsystem, groupedesordre, geom ) "
            sql += "VALUES(" + str(lastdesordreid) + ',' +  str(lastobjetid) + "," + str(lastrevision) + "," + str(iddescriptionsystem)
            sql += ",'NOD'," + geomsql + ");"
            query = self.dbase.query(sql)


