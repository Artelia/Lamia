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

from qgis.PyQt import uic, QtCore, QtGui

try:
    from qgis.PyQt.QtGui import (QWidget, QMainWindow, QSpinBox, QAction, QDialog, QFrame)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget,QMainWindow, QSpinBox, QAction, QDialog, QFrame)
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..base.lamiabase_croquis_tool import BaseCroquisTool
import os
import qgis
import datetime
#from .lamiabase_photoviewer import PhotoViewer


# FORM_CLASS3, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'FreeHandEditorToolUser.ui'))


class BaseAssainissementCroquisTool(BaseCroquisTool):

    LOADFIRST = False
    dbasetablename = 'Photo'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None, parentwidget=None, parent=None):
        super(BaseAssainissementCroquisTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil, parentwidget, parent=parent)

    """
    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Ressources'
        self.NAME = 'Croquis'
        self.dbasetablename = 'Photo'
        self.visualmode = [ 1, 2]
        # self.PointENABLED = True
        # self.LineENABLED = True
        # self.PolygonEnabled = True
        # self.magicfunctionENABLED = True
        self.linkagespec = {'Tcobjetressource' : {'tabletc' : 'Tcobjetressource',
                                              'idsource' : 'id_ressource',
                                            'idtcsource' : 'id_tcressource',
                                           'iddest' : 'id_objet',
                                           'idtcdest' : 'id_tcobjet',
                                           'desttable' : ['Profil','Infralineaire','Observation','Equipement']} }
        # self.pickTable = None
        self.iconpath = os.path.join(os.path.dirname(__file__), 'lamiabase_croquis_tool_icon.png')


        # ****************************************************************************************
        #properties ui
        pass

    def initFieldUI(self):
        # ****************************************************************************************
        # userui
        if self.userwdgfield is None:
            self.userwdgfield = UserUI()
            self.linkuserwdgfield = {'Photo' : {'linkfield' : 'id_photo',
                                             'widgets' : {}},
                                'Objet' : {'linkfield' : 'id_objet',
                                          'widgets' : {}},
                                'Ressource' : {'linkfield' : 'id_ressource',
                                          'widgets' : {}}}

            self.groupBox_geom.setParent(None)
            self.userwdgfield.stackedWidget.setCurrentIndex(1)

            self.userwdgfield.pushButton_open.clicked.connect(self.openPhoto)
            self.userwdgfield.pushButton_edit.clicked.connect(self.editPhoto)
            self.editorwindow = ScribbleMainWindow(parentwdg=self)
            self.photowdg = PhotoViewer()
            self.userwdgfield.frame_cr.layout().addWidget(self.photowdg)


    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass

    def postloadIds(self,sqlin):
        sqlin += " AND typephoto = 'CRO'"
        return sqlin

    def postInitFeatureProperties(self, feat):
        if self.currentFeature is None:
            datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
            self.initFeatureProperties(feat, 'Ressource', 'dateressource', datecreation)

        if feat is not None :
            sql = "SELECT file FROM Ressource  WHERE id_ressource = " + str(feat['id_ressource']) + ";"
            query = self.dbase.query(sql)
            result = [row[0] for row in query]
            file = result[0]
            if os.path.isfile(self.dbase.completePathOfFile(file)):
                self.editorwindow.openImage(self.dbase.completePathOfFile(file))
                self.showImageinLabelWidget(self.photowdg, self.dbase.completePathOfFile(file))
        else:
            self.editorwindow.clear()
            self.photowdg.clear()

    def editPhoto(self):
        self.editorwindow.show()

    def openPhoto(self):
        if False:
            if os.path.isfile(self.dbase.completePathOfFile(self.currentFeature['File'] )):
                filepath = self.dbase.completePathOfFile(self.currentFeature['File'])
                os.startfile(filepath)

        if True:
            sql = "SELECT file FROM Ressource  WHERE id_ressource = " + str(self.currentFeature['id_ressource']) + ";"
            query = self.dbase.query(sql)
            result = [row[0] for row in query]
            resultfile = result[0]
            if os.path.isfile(self.dbase.completePathOfFile(resultfile)):
                filepath = self.dbase.completePathOfFile(resultfile)
                os.startfile(filepath)

    def createParentFeature(self):

        #lastrevision = self.dbase.getLastPk('Revision')
        lastrevision = self.dbase.maxrevision
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
        lastressourcepk = self.dbase.getLastRowId('Ressource')


        pkcroquis = self.currentFeature.id()
        lastidcroquis = self.dbase.getLastId('Photo') + 1

        fileimage = os.path.join('.', self.dbasetablename, ''.join(datecreation.split('-')),
                                 str(lastidcroquis) + '_croquis.png')
        if not os.path.exists(os.path.dirname(self.dbase.completePathOfFile(fileimage))):
            os.makedirs(os.path.dirname(self.dbase.completePathOfFile(fileimage)))
        self.editorwindow.saveImage(self.dbase.completePathOfFile(fileimage))



        sql = "UPDATE Photo SET id_objet = " + str(lastobjetid)  + ","
        sql += "id_ressource = " + str(lastressourceid)   + ","
        sql += "id_photo = " + str(lastidcroquis)  + ","
        sql += "id_revisionbegin = " + str(lastrevision) + ","
        sql += "typephoto = 'CRO' "
        sql += " WHERE pk_photo = " + str(pkcroquis) + ";"
        print(sql)
        query = self.dbase.query(sql)
        self.dbase.commit()

        sql = "UPDATE Ressource SET  file = '" + fileimage + "', dateressource = '" + datecreation + "'"
        sql += " WHERE pk_ressource = " + str( lastressourcepk) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()



        if self.parentWidget is not None and self.parentWidget.currentFeature is not None:
            currentparentlinkfield = self.parentWidget.currentFeature['id_objet']
            sql = "INSERT INTO Tcobjetressource(id_tcobjet, id_tcressource,id_revisionbegin) "
            sql += " VALUES(" + str(currentparentlinkfield) + ", " + str(lastressourceid) + "," + str(lastrevision) + ");"
            query = self.dbase.query(sql)
            self.dbase.commit()



    def postSaveFeature(self, boolnewfeature):
        if self.currentFeature is not None:
            sql = "SELECT file FROM Ressource WHERE id_ressource = " + str(self.currentFeature['id_ressource'])
            query = self.dbase.query(sql)
            fileimage = [row[0] for row in query][0]
            self.editorwindow.saveImage(self.dbase.completePathOfFile(fileimage))




    def deleteParentFeature(self):
        idobjet = self.currentFeature['id_objet']
        idressource = self.currentFeature['id_ressource']

        sql = "DELETE FROM Objet WHERE id_objet = " + str(idobjet) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()

        sql = "DELETE FROM Ressource WHERE id_objet = " + str(idobjet) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()

        sql = "DELETE FROM Tcobjetressource WHERE id_tcressource = " + str(idressource) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()

        return True

    """


