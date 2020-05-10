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




from qgis.PyQt import uic, QtCore, QtGui
try:
    from qgis.PyQt.QtGui import (QWidget, QLabel, QFrame)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget, QLabel, QFrame)
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ...toolabstract.Lamia_abstract_tool import AbstractLamiaTool
import os
import datetime
import glob
from .lamiabase_photoviewer import PhotoViewer

prefixhoto = ''
numphoto = None
import sys


class BasePhotoTool(AbstractLamiaTool):

    LOADFIRST = False
    dbasetablename = 'Photo'
    specialfieldui = []


    def __init__(self, dbase, dialog=None, linkedtreewidget=None,gpsutil=None, parentwidget=None, parent=None):
        super(BasePhotoTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)

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
                                            'idtcsource' : 'lid_ressource',
                                           'iddest' : 'id_objet',
                                           'idtcdest' : 'lid_objet',
                                           'desttable' : ['Infralineaire','Observation','Equipement','Noeud','Profil']} }
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
                                                       'numressource': self.userwdgfield.spinBox_numphoto,
                                                        'datetimeressource' : self.userwdgfield.dateTimeEdit_date}}}

            self.userwdgfield.stackedWidget.setCurrentIndex(0)
            self.userwdgfield.pushButton_chooseph.clicked.connect(self.choosePhoto)
            self.userwdgfield.pushButton_lastph.clicked.connect(self.lastPhoto)
            self.userwdgfield.pushButton_openph.clicked.connect(self.openPhoto)
            self.photowdg = PhotoViewer()
            self.userwdgfield.frame_ph.layout().addWidget(self.photowdg)

            self.userwdgfield.toolButton_photoplus.clicked.connect(self.changeNumPhoto)
            self.userwdgfield.toolButton_photomoins.clicked.connect(self.changeNumPhoto)
            self.userwdgfield.toolButton_calc.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.spinBox_numphoto))


            if False:
                # ****************************************************************************************
                # parent widgets
                if self.parentWidget is not None and 'lk_photo' in self.dbase.dbasetables[self.parentWidget.dbasetablename]['fields'].keys():
                    self.userwdgfield.pushButton_defaultphoto.clicked.connect(self.setDefaultPhoto)
                else:
                    self.userwdgfield.pushButton_defaultphoto.setParent(None)


            # ****************************************************************************************
            # child widgets
            pass


    def changeNumPhoto(self):

        global numphoto

        if numphoto is None:
            numphoto = 0

        if self.sender() == self.userwdgfield.toolButton_photoplus:
            numphoto += 1
        elif self.sender() == self.userwdgfield.toolButton_photomoins:
            numphoto = numphoto -1
        self.userwdgfield.spinBox_numphoto.setValue(numphoto)





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

        file = None
        if sys.version_info.major == 2:
            file, extension = self.windowdialog.qfiledlg.getOpenFileNameAndFilter(None, 'Choose the file', self.dbase.imagedirectory,
                                                                     'Image (*.jpg)', '')
        elif sys.version_info.major == 3:
            file , extension= self.windowdialog.qfiledlg.getOpenFileName(None, 'Choose the file', self.dbase.imagedirectory,
                                                                     'Image (*.jpg)', '')


        if file:
            self.userwdg.lineEdit_file.setText(os.path.normpath(file))
            self.showImageinLabelWidget(self.photowdg , self.userwdg.lineEdit_file.text())


    def lastPhoto(self):
        if self.dbase.imagedirectory is not None:
            list_of_files = glob.glob(self.dbase.imagedirectory + "//*.jpg")
            try :
                latest_file = max(list_of_files, key=os.path.getctime)
                self.userwdg.lineEdit_file.setText(os.path.normpath(latest_file))
                self.showImageinLabelWidget(self.photowdg , self.userwdg.lineEdit_file.text())
                datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                self.userwdg.dateTimeEdit_date.setDateTime(QtCore.QDateTime.fromString(datecreation, 'yyyy-MM-dd hh:mm:ss'))

            except ValueError:
                pass

    def openPhoto(self):
        filepath = self.dbase.completePathOfFile(self.userwdg.lineEdit_file.text())

        if os.path.isfile(filepath ):
            os.startfile(filepath)
        else:
            possiblethumbnail, ext = os.path.splitext(filepath)
            if os.path.isfile(possiblethumbnail + "_thumbnail.png"):
                os.startfile(possiblethumbnail + "_thumbnail.png")


    def postInitFeatureProperties(self, feat):

        global numphoto

        if self.currentFeature is None:
            datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
            #datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            self.initFeatureProperties(feat, 'Ressource', 'datetimeressource', datecreation)

            if numphoto is not None:
                self.userwdgfield.spinBox_numphoto.setValue(numphoto)

            # geom if parent is node
            if self.parentWidget is not None and self.parentWidget.currentFeature is not None:
                if self.parentWidget.dbasetablename == 'Noeud':

                    # get geom
                    noeudfet = self.dbase.getLayerFeatureByPk('Noeud', self.parentWidget.currentFeature.id())
                    neudfetgeom = noeudfet.geometry().asPoint()
                    self.createorresetRubberband(1)
                    self.setTempGeometry([neudfetgeom], False,False)

            self.photowdg.clear()

        else:
            sql = "SELECT file FROM photo_qgis  WHERE pk_photo = " + str(self.currentFeaturePK)
            file = self.dbase.query(sql)[0][0]
            if file is not None and file != '':
                self.showImageinLabelWidget(self.photowdg, self.userwdg.lineEdit_file.text())
            else:
                self.photowdg.clear()



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

        pkphoto = self.currentFeaturePK
        lastidphoto = self.dbase.getLastId('Photo') + 1
        sql = "UPDATE Photo SET id_photo = " + str(lastidphoto)  + ","
        sql += "lpk_ressource = " + str(pkres)
        sql += ", typephoto = 'PHO' "
        sql += " WHERE pk_photo = " + str(pkphoto) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()

        if self.parentWidget is not None and self.parentWidget.currentFeature is not None:

            #get parent id_objet
            sql = " SELECT id_objet FROM " + self.parentWidget.dbasetablename.lower() + "_qgis"
            sql += " WHERE pk_" + self.parentWidget.dbasetablename.lower() + " = " + str(self.parentWidget.currentFeaturePK)
            currentparentlinkfield = self.dbase.query(sql)[0][0]

            #currentparentlinkfield = self.parentWidget.currentFeature['id_objet']
            sql = "INSERT INTO Tcobjetressource(lpk_revision_begin, lid_objet, lid_ressource) "
            sql += " VALUES(" + str(self.dbase.maxrevision) + "," + str(currentparentlinkfield) + ',' + str(lastressourceid) + ")"
            query = self.dbase.query(sql)
            self.dbase.commit()




    def postSaveFeature(self, boolnewfeature):

        global numphoto
        if self.userwdgfield.spinBox_numphoto.value() == -1 :
            numphoto = None
        elif numphoto == self.userwdgfield.spinBox_numphoto.value():
            numphoto += 1
        else:
            numphoto = self.userwdgfield.spinBox_numphoto.value() + 1


    def deleteParentFeature(self):

        sql = "SELECT pk_objet, pk_ressource, id_ressource FROM Photo_qgis WHERE pk_photo = " + str(self.currentFeaturePK)
        pkobjet, pkressource, idressource = self.dbase.query(sql)[0]
        #idobjet = self.currentFeature['id_objet']
        #idressource = self.currentFeature['id_ressource']

        sql = "DELETE FROM Objet WHERE pk_objet = " + str(pkobjet)
        query = self.dbase.query(sql)
        self.dbase.commit()

        sql = "DELETE FROM Ressource WHERE pk_ressource = " + str(pkressource)
        query = self.dbase.query(sql)
        self.dbase.commit()

        sql = "DELETE FROM Tcobjetressource WHERE id_tcressource = " + str(idressource)
        sql += " AND lpk_revision_begin <= " + str(self.dbase.maxrevision)
        sql += " AND lpk_revision_end IS  NULL "

        """
        if self.dbase.dbasetype == 'postgis':
            sql += " AND CASE WHEN lpk_revision_end IS NOT NULL THEN "
            sql += " lpk_revision_end > " + str(self.currentrevision)
            sql += " ELSE TRUE END "
        elif self.dbase.dbasetype == 'spatialite':
            sql += " AND CASE WHEN lpk_revision_end IS NOT NULL THEN "
            sql += " lpk_revision_end > " + str(self.currentrevision)
            sql += " ELSE 1 END"
        """
        query = self.dbase.query(sql)
        self.dbase.commit()

        return True




class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabase_photo_tool_ui.ui')
        uic.loadUi(uipath, self)

