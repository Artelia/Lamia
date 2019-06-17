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
from ...toolabstract.Lamia_abstract_tool import AbstractLamiaTool
import os
import datetime



class BaseRasterTool(AbstractLamiaTool):

    LOADFIRST = True
    dbasetablename = 'Rasters'
    specialfieldui = []

    def __init__(self, dbase, dialog=None, linkedtreewidget=None,gpsutil=None, parentwidget=None, parent=None):
        super(BaseRasterTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil,parentwidget, parent=parent)


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
        self.iconpath = os.path.join(os.path.dirname(__file__), 'lamiabase_raster_tool_icon.png')
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
                                          'widgets' : {'libelle' : self.userwdgfield.lineEdit_libelle}},
                                'Ressource' : {'linkfield' : 'id_ressource',
                                          'widgets' : {'file': self.userwdgfield.lineEdit_file,
                                                     'datetimeressource': self.userwdgfield.dateTimeEdit}}}
            self.userwdgfield.pushButton_chooseph.clicked.connect(self.chooseFile)
            self.userwdgfield.pushButton_loadraster.clicked.connect(self.loadRaster)


    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass


    def loadRaster(self,feat = None):
        libelle = self.userwdgfield.lineEdit_libelle.text()
        rlayer = self.createMapLayer()

        if True:
            if int(str(self.dbase.qgisversion_int)[0:3]) < 220:
                qgis.core.QgsMapLayerRegistry.instance().addMapLayer(rlayer, False)
            else:
                qgis.core.QgsProject.instance().addMapLayer(rlayer, False)
        if False:
            root = qgis.core.QgsProject.instance().layerTreeRoot()
            lamialegendgroup =  root.findGroup('Lamia')
            lamialegendgroup.insertLayer(-1, rlayer)
        if self.windowdialog.qgislegendnode is not None:
            self.windowdialog.qgislegendnode.insertLayer(-1, rlayer)



    def createMapLayer(self,libelle = None):

        typefonddeplan = None
        if libelle is None:
            if self.currentFeature is not None:
                #sql = "SELECT file FROM Ressource WHERE id_ressource = " + str(self.currentFeature['id_ressource'])
                sql = "SELECT file FROM Rasters_qgis WHERE pk_rasters = " + str(self.currentFeaturePK)
                query = self.dbase.query(sql)
                filetemp = [row[0] for row in query][0]
                layfile = self.dbase.completePathOfFile(filetemp)
            else:
                return
        else:
            sql = "SELECT typeraster, file FROM Rasters_qgis WHERE libelle = '" + str(libelle) + "'"
            query = self.dbase.query(sql)
            typefonddeplan, filetemp = query[0]
            layfile = self.dbase.completePathOfFile(filetemp)

        if False:
            if feat is None or  isinstance(feat,bool):
                if self.currentFeature is not None:
                    #sql = "SELECT file FROM Ressource WHERE id_ressource = " + str(self.currentFeature['id_ressource'])
                    sql = "SELECT file FROM Rasters_qgis WHERE pk_rasters = " + str(self.currentFeaturePK)
                    query = self.dbase.query(sql)
                    filetemp = [row[0] for row in query][0]
                    file = self.dbase.completePathOfFile(filetemp)
                else:
                    return
            else:
                #file = self.dbase.completePathOfFile(feat['file'])
                # sql = "SELECT file FROM Ressource WHERE id_ressource = " + str(self.currentFeature['id_ressource'])
                sql = "SELECT file FROM Rasters_qgis WHERE pk_rasters = " + str(self.currentFeaturePK)
                query = self.dbase.query(sql)
                filetemp = [row[0] for row in query][0]
                file = self.dbase.completePathOfFile(filetemp)

        basename = os.path.basename(layfile).split('.')[0]

        rlayer = None

        if libelle is not None:
            layername = libelle
            if typefonddeplan == 'SHP':
                rlayer = qgis.core.QgsVectorLayer(layfile, 'test' , "ogr")
                qmlfile = os.path.splitext(layfile)[0] + '.qml'
                if os.path.isfile(qmlfile):
                    rlayer.loadNamedStyle(qmlfile)

        else:
            currentmaplayertype = self.userwdgfield.comboBox_type.currentText()
            if currentmaplayertype.split('-')[0] == 'Raster' :
                rlayer = qgis.core.QgsRasterLayer(layfile, basename)
            elif currentmaplayertype.split('-')[0] == 'Vecteur' :
                if self.userwdgfield.lineEdit_libelle.text() == '':
                    layername = basename
                else:
                    layername = self.userwdgfield.lineEdit_libelle.text()

                if currentmaplayertype.split('-')[1] == 'Shapefile' :
                    rlayer = qgis.core.QgsVectorLayer(layfile, layername ,"ogr")
                    qmlfile = os.path.splitext(layfile)[0] + '.qml'
                    if os.path.isfile(qmlfile):
                        rlayer.loadNamedStyle(qmlfile)

        return rlayer





    def chooseFile(self):
        file, extension = self.windowdialog.qfiledlg.getOpenFileNameAndFilter(None, 'Choose the file', self.dbase.imagedirectory,
                                                                 'All (*.*)', '')
        if file:
            self.userwdg.lineEdit_file.setText(os.path.normpath(file))




    def postInitFeatureProperties(self, feat):

        if self.currentFeature is None:
            if False:
                datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
                #self.initFeatureProperties(feat, 'dateressource', datecreation)
                self.initFeatureProperties(feat, None , 'dateressource', datecreation)

            datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            self.initFeatureProperties(feat, 'Ressource', 'datetimeressource', datecreation)


    def createParentFeature(self):
        pkobjet = self.dbase.createNewObjet()

        if False:


            # lastrevision = self.dbase.maxrevision
            datecreation =  str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            lastobjetid = self.dbase.getLastId('Objet') + 1
            sql = "INSERT INTO Objet (id_objet, lpk_revision_begin, datetimecreation ) "
            sql += "VALUES(" + str(lastobjetid ) + "," + str(self.dbase.maxrevision) +  ",'" + datecreation + "');"
            query = self.dbase.query(sql)
            self.dbase.commit()
            pkobjet = self.dbase.getLastRowId('Objet')

        lastressourceid = self.dbase.getLastId('Ressource') + 1
        sql = "INSERT INTO Ressource (id_ressource, lpk_objet) "
        sql += "VALUES(" + str(lastressourceid) +   "," + str(pkobjet) + ");"
        query = self.dbase.query(sql)
        self.dbase.commit()
        pkres = self.dbase.getLastRowId('Ressource')

        pkraster = self.currentFeaturePK
        lastidraster = self.dbase.getLastId('Rasters') + 1
        sql = "UPDATE Rasters SET id_rasters = " + str(lastidraster)  + ","
        sql += "lpk_ressource = " + str(pkres)
        sql += " WHERE pk_rasters = " + str(pkraster) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()



    def postSaveFeature(self, boolnewfeature):
        pass

    def deleteParentFeature(self):

        sql = "SELECT pk_objet, pk_ressource, id_ressource FROM Rasters_qgis WHERE pk_rasters = " + str(self.currentFeaturePK)
        pkobjet, pkressource, idressource = self.dbase.query(sql)[0]
        #idobjet = self.currentFeature['id_objet']
        #idressource = self.currentFeature['id_ressource']

        sql = "DELETE FROM Objet WHERE pk_objet = " + str(pkobjet)
        query = self.dbase.query(sql)
        self.dbase.commit()

        sql = "DELETE FROM Ressource WHERE pk_ressource = " + str(pkressource)
        query = self.dbase.query(sql)
        self.dbase.commit()


        return True



class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabase_raster_tool_ui.ui')
        uic.loadUi(uipath, self)
