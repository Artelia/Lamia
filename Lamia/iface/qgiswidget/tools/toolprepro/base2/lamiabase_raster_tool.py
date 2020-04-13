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


import os, sys
import datetime

import qgis
from qgis.PyQt import uic, QtCore
from qgis.PyQt.QtWidgets import (QWidget)

from ...lamia_abstractformtool import AbstractLamiaFormTool


class BaseRasterTool(AbstractLamiaFormTool):

    DBASETABLENAME = 'Rasters'
    LOADFIRST = True

    tooltreewidgetCAT = 'Ressources'
    tooltreewidgetSUBCAT = 'Fonds de plan'
    tooltreewidgetICONPATH = os.path.join(os.path.dirname(__file__), 'lamiabase_raster_tool_icon.png')

    def __init__(self, **kwargs):
        super(BaseRasterTool, self).__init__(**kwargs)

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
        self.iconpath = os.path.join(os.path.dirname(__file__), 'lamiabase_raster_tool_icon.png')
        self.qtreewidgetfields = ['typeraster']
        # ****************************************************************************************
        #properties ui
        pass
    """

    def initMainToolWidget(self):

        self.toolwidgetmain = UserUI()
        self.formtoolwidgetconfdictmain = {'Rasters' : {'linkfield' : 'id_rasters',
                                                            'widgets' : {
                                                        'typeraster' : self.toolwidgetmain.comboBox_type}},
                                            'Objet' : {'linkfield' : 'id_objet',
                                                        'widgets' : {'libelle' : self.toolwidgetmain.lineEdit_libelle}},
                                            'Ressource' : {'linkfield' : 'id_ressource',
                                                        'widgets' : {'file': self.toolwidgetmain.lineEdit_file,
                                                                    'datetimeressource': self.toolwidgetmain.dateTimeEdit}}}
        self.toolwidgetmain.pushButton_chooseph.clicked.connect(self.chooseFile)
        self.toolwidgetmain.pushButton_loadraster.clicked.connect(self.loadRaster)


    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass


    def loadRaster(self,feat = None):
        libelle = self.toolwidgetmain.lineEdit_libelle.text()
        rlayer = self.createMapLayer()

        qgis.core.QgsProject.instance().addMapLayer(rlayer, False)

        if self.mainifacewidget.qgiscanvas.qgislegendnode is not None:
            self.mainifacewidget.qgiscanvas.qgislegendnode.insertLayer(-1, rlayer)



    def createMapLayer(self,libelle = None):

        typefonddeplan = None
        if libelle is None:
            if self.currentFeaturePK is not None:
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
            currentmaplayertype = self.toolwidgetmain.comboBox_type.currentText()
            if currentmaplayertype.split('-')[0] == 'Raster' :
                rlayer = qgis.core.QgsRasterLayer(layfile, basename)
            elif currentmaplayertype.split('-')[0] == 'Vecteur' :
                if self.toolwidgetmain.lineEdit_libelle.text() == '':
                    layername = basename
                else:
                    layername = self.toolwidgetmain.lineEdit_libelle.text()

                if currentmaplayertype.split('-')[1] == 'Shapefile' :
                    rlayer = qgis.core.QgsVectorLayer(layfile, layername ,"ogr")
                    qmlfile = os.path.splitext(layfile)[0] + '.qml'
                    if os.path.isfile(qmlfile):
                        rlayer.loadNamedStyle(qmlfile)

        return rlayer





    def chooseFile(self):

        file, extension = self.mainifacewidget.qfiledlg.getOpenFileName(None, 'Choose the file', self.mainifacewidget.imagedirectory,
                                                                    'All (*.*)', '')
        if file:
            self.toolwidget.lineEdit_file.setText(os.path.normpath(file))




    def postSelectFeature(self):

        if self.currentFeaturePK is None:
            datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            # self.initFeatureProperties(feat, 'Ressource', 'datetimeressource', datecreation)
            self.formutils.applyResultDict({'datetimeressource': datecreation}, False)

    """
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
    """


    def postSaveFeature(self, savedfeaturepk=None):
        pass

    """
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
    """


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabase_raster_tool_ui.ui')
        uic.loadUi(uipath, self)
