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


# -*- coding: utf-8 -*-
import qgis
from qgis.PyQt import uic, QtCore
try:
    from qgis.PyQt.QtGui import (QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget)
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..base.lamiabase_raster_tool import BaseRasterTool
import os
import datetime



class BaseAssainissementRasterTool(BaseRasterTool):

    LOADFIRST = True
    dbasetablename = 'Rasters'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None,gpsutil=None, parentwidget=None, parent=None):
        super(BaseAssainissementRasterTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil,parentwidget, parent=parent)

    """
    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Ressources'
        self.NAME = 'Fonds de plan'
        self.dbasetablename = 'Rasters'
        self.visualmode = [0, 1, 2]
        # self.PointENABLED = True
        # self.LineENABLED = True
        # self.PolygonENABLED = True
        # self.magicfunctionENABLED = True
        # self.linkagespec = None
        # self.pickTable = None
        self.iconpath = os.path.join(os.path.dirname(__file__), 'lamiadefault_raster_tool_icon.png')
        self.qtreewidgetfields = ['typeraster']
        # ****************************************************************************************
        #properties ui
        pass

    def initFieldUI(self):
        # ****************************************************************************************
        #   userui Field
        if self.userwdgfield is None:

            # ****************************************************************************************
            # userui
            self.userwdgfield = UserUI()
            self.linkuserwdgfield = {'Rasters' : {'linkfield' : 'id_rasters',
                                             'widgets' : {
                                            'typeraster' : self.userwdgfield.comboBox_type}},
                                'Objet' : {'linkfield' : 'id_objet',
                                          'widgets' : {}},
                                'Ressource' : {'linkfield' : 'id_ressource',
                                          'widgets' : {'file': self.userwdgfield.lineEdit_file,
                                                     'dateressource': self.userwdgfield.dateEdit}}}
            self.userwdgfield.pushButton_chooseph.clicked.connect(self.chooseFile)
            self.userwdgfield.pushButton_loadraster.clicked.connect(self.loadRaster)


    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass

    def loadRaster(self,feat = None):
        if feat is None or  isinstance(feat,bool):
            if self.currentFeature is not None:
                sql = "SELECT file FROM Ressource WHERE id_ressource = " + str(self.currentFeature['id_ressource'])
                query = self.dbase.query(sql)
                filetemp = [row[0] for row in query][0]
                file = self.dbase.completePathOfFile(filetemp)
            else:
                return
        else:
            #file = self.dbase.completePathOfFile(feat['file'])
            sql = "SELECT file FROM Ressource WHERE id_ressource = " + str(self.currentFeature['id_ressource'])
            query = self.dbase.query(sql)
            filetemp = [row[0] for row in query][0]
            file = self.dbase.completePathOfFile(filetemp)

        basename = os.path.basename(file).split('.')[0]
        rlayer = qgis.core.QgsRasterLayer(file, basename)




        if True:
            if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                qgis.core.QgsMapLayerRegistry.instance().addMapLayer(rlayer, False)
            else:
                qgis.core.QgsProject.instance().addMapLayer(rlayer, False)

        root = qgis.core.QgsProject.instance().layerTreeRoot()
        lamialegendgroup =  root.findGroup('Lamia')
        lamialegendgroup.insertLayer(-1, rlayer)

    def chooseFile(self):
        file, extension = self.windowdialog.qfiledlg.getOpenFileNameAndFilter(None, 'Choose the file', self.dbase.imagedirectory,
                                                                 'All (*.*)', '')
        if file:
            self.userwdg.lineEdit_file.setText(os.path.normpath(file))


    def postInitFeatureProperties(self, feat):
        if self.currentFeature is None:
            datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
            self.initFeatureProperties(feat, 'Date', datecreation)


    def createParentFeature(self):



        lastrevision = self.dbase.getLastPk('Revision')
        datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
        lastobjetid = self.dbase.getLastId('Objet') + 1
        sql = "INSERT INTO Objet (id_objet, id_revisionbegin, datecreation ) "
        sql += "VALUES(" + str(lastobjetid ) + "," + str(lastrevision) +  ",'" + datecreation + "');"
        query = self.dbase.query(sql)
        self.dbase.commit()
        #idobjet = self.dbase.getLastRowId('Objet')


        lastressourceid = self.dbase.getLastId('Ressource') + 1
        sql = "INSERT INTO Ressource (id_ressource, id_revisionbegin, id_objet) "
        sql += "VALUES(" + str(lastressourceid) + "," + str(lastrevision) +  "," + str(lastobjetid) + ");"
        query = self.dbase.query(sql)
        self.dbase.commit()


        idraster = self.currentFeature.id()
        lastidraster  = self.dbase.getLastId('Rasters') + 1




        sql = "UPDATE Rasters SET id_objet = " + str(lastobjetid)  + ","
        sql += "id_ressource = " + str(lastressourceid)   + ","
        sql += "id_rasters = " + str(lastidraster)  + ","
        sql += "id_revisionbegin = " + str(lastrevision)
        sql += " WHERE pk_rasters = " + str(idraster) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()



    def postSaveFeature(self, boolnewfeature):
        pass
    """
"""
class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiadefault_raster_tool_ui.ui')
        uic.loadUi(uipath, self)
"""