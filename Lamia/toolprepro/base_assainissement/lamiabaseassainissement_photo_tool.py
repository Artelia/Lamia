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
    from qgis.PyQt.QtGui import (QWidget, QLabel, QFrame)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget, QLabel, QFrame)
# from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..base.lamiabase_photo_tool import BasePhotoTool
import os
import datetime
import glob

class BaseAssainissementPhotoTool(BasePhotoTool):
    LOADFIRST = False
    dbasetablename = 'Photo'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None, parentwidget=None, parent=None):
        super(BaseAssainissementPhotoTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil, parentwidget,
                                                          parent=parent)

    def initFieldUI(self):
        # ret = super().initTool()
        super(BaseAssainissementPhotoTool, self).initFieldUI()

        if self.parentWidget is not None and self.parentWidget.dbasetablename in ['']:
            self.userwdgfield.pushButton_defaultphoto.clicked.connect(self.setDefaultPhoto)
        else:
            self.userwdgfield.pushButton_defaultphoto.setParent(None)

    """
    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Ressources'
        self.NAME = 'Photographies'
        self.dbasetablename = 'Photo'
        self.visualmode = [ 1, 2]
        self.PointENABLED = True
        # self.LineENABLED = True
        # self.PolygonEnabled = True
        self.magicfunctionENABLED = True
        self.linkagespec = {'Tcobjetressource' : {'tabletc' : 'Tcobjetressource',
                                              'idsource' : 'id_ressource',
                                            'idtcsource' : 'id_tcressource',
                                           'iddest' : 'id_objet',
                                           'idtcdest' : 'id_tcobjet',
                                           'desttable' : ['Infralineaire','Observation','Equipement','Noeud']},
                            'Marche' :{'tabletc' : None,
                                              'idsource' : 'lk_marche',
                                            'idtcsource' : None,
                                           'iddest' : 'id_marche',
                                           'idtcdest' : None,
                                           'desttable' : ['Marche']} }
        # self.pickTable = None
        self.iconpath = os.path.join(os.path.dirname(__file__), 'lamiabase_photo_tool_icon.svg')

        # ****************************************************************************************
        #properties ui


        # ****************************************************************************************
        # userui
    def initFieldUI(self):
        if self.userwdgfield is None:
            self.userwdgfield = UserUI()
            self.linkuserwdgfield = {'Photo' : {'linkfield' : 'id_photo',
                                             'widgets' : {}},
                                'Objet' : {'linkfield' : 'id_objet',
                                          'widgets' : {}},
                                'Ressource' : {'linkfield' : 'id_ressource',
                                          'widgets' : {'file': self.userwdgfield.lineEdit_file,
                                                        'dateressource' : self.userwdgfield.dateEdit}}}

            self.userwdgfield.stackedWidget.setCurrentIndex(0)
            self.userwdgfield.pushButton_chooseph.clicked.connect(self.choosePhoto)
            self.userwdgfield.pushButton_lastph.clicked.connect(self.lastPhoto)
            self.userwdgfield.pushButton_openph.clicked.connect(self.openPhoto)
            self.photowdg = PhotoViewer()
            self.userwdgfield.frame_ph.layout().addWidget(self.photowdg)

            # ****************************************************************************************
            # parent widgets
            if self.parentWidget is not None and 'lk_photo' in self.dbase.dbasetables[self.parentWidget.dbasetablename]['fields'].keys():
                self.userwdgfield.pushButton_defaultphoto.clicked.connect(self.setDefaultPhoto)
            else:
                self.userwdgfield.pushButton_defaultphoto.setParent(None)


            # ****************************************************************************************
            # child widgets
            pass



    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass

    def postloadIds(self,sqlin):
        sqlin += " AND typephoto = 'PHO'"
        return sqlin

    def magicFunction(self):
        self.featureSelected()
        self.lastPhoto()
        self.addGPSPoint()
        self.saveFeature()

    def setDefaultPhoto(self):
        # print('setDefaultPhoto', self.currentparentfeature)
        if self.parentWidget.currentFeature is not None:
            idphoto = self.currentFeature['id_objet']
            idparentfeature=self.parentWidget.currentFeature['id_objet']
            # print('setDefaultPhoto',idphoto,idparentfeature)
            sql = "UPDATE " + str(self.parentWidget.dbasetablename) + " SET  lk_photo = " + str(idphoto) + " WHERE id_objet = " + str(idparentfeature) + ";"
            query = self.dbase.query(sql)
            self.dbase.commit()


    def choosePhoto(self):
        file, extension = self.windowdialog.qfiledlg.getOpenFileNameAndFilter(None, 'Choose the file', self.dbase.imagedirectory,
                                                                 'Image (*.jpg)', '')
        if file:
            self.userwdg.lineEdit_file.setText(os.path.normpath(file))
            self.showImageinLabelWidget(self.photowdg , self.userwdg.lineEdit_file.text())


    def lastPhoto(self):
        if self.dbase.imagedirectory is not None:
            list_of_files = glob.glob(self.dbase.imagedirectory + "\*.jpg")
            try :
                latest_file = max(list_of_files, key=os.path.getctime)
                self.userwdg.lineEdit_file.setText(os.path.normpath(latest_file))
                self.showImageinLabelWidget(self.photowdg , self.userwdg.lineEdit_file.text())
            except ValueError:
                pass

    def openPhoto(self):
        filepath = self.dbase.completePathOfFile(self.userwdg.lineEdit_file.text())
        if os.path.isfile(filepath ):
            os.startfile(filepath)


    def postInitFeatureProperties(self, feat):
        if self.currentFeature is None:
            datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
            self.initFeatureProperties(feat, 'Ressource', 'dateressource', datecreation)



        if feat is not None:
            sql = "SELECT file FROM Ressource  WHERE id_ressource = " + str(feat['id_ressource']) + ";"
            query = self.dbase.query(sql)
            result = [row[0] for row in query]
            #print('post',result)
            file = result[0]
            if file is not None and file != '':
                self.showImageinLabelWidget(self.photowdg, self.userwdg.lineEdit_file.text())
            else:
                self.photowdg.clear()
        else:
            self.photowdg.clear()

    def createParentFeature(self):

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


        idphoto = self.currentFeature.id()
        lastidphoto = self.dbase.getLastId('Photo') + 1




        sql = "UPDATE Photo SET id_objet = " + str(lastobjetid)  + ","
        sql += "id_ressource = " + str(lastressourceid)   + ","
        sql += "id_photo = " + str(lastidphoto)  + ","
        sql += "id_revisionbegin = " + str(lastrevision) + ","
        sql += "typephoto = 'PHO' "
        sql += " WHERE pk_photo = " + str(idphoto) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()

        if self.parentWidget is not None and self.parentWidget.currentFeature is not None:
            currentparentlinkfield = self.parentWidget.currentFeature['id_objet']
            sql = "INSERT INTO Tcobjetressource(id_tcobjet, id_tcressource,id_revisionbegin) "
            sql += " VALUES(" + str(currentparentlinkfield) + ", " + str(lastressourceid) + "," + str(lastrevision) + ");"
            query = self.dbase.query(sql)
            self.dbase.commit()




    def postSaveFeature(self, boolnewfeature):
        pass


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


"""
class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabase_photo_tool_ui.ui')
        uic.loadUi(uipath, self)
"""
