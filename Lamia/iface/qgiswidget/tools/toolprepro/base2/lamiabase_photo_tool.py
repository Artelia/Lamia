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



import qgis, qgis.core
from qgis.PyQt import uic, QtCore, QtGui
try:
    from qgis.PyQt.QtGui import (QWidget, QLabel, QFrame)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget, QLabel, QFrame)
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ...lamia_abstractformtool import AbstractLamiaFormTool
import os
import datetime
import glob
from .lamiabase_photoviewer import PhotoViewer

prefixhoto = ''
numphoto = None
import sys


class BasePhotoTool(AbstractLamiaFormTool):


    DBASETABLENAME = 'Photo'
    LOADFIRST = False

    tooltreewidgetCAT = 'Ressources'
    tooltreewidgetSUBCAT = 'Photo'
    tooltreewidgetICONPATH = os.path.join(os.path.dirname(__file__), 'lamiabase_photo_tool_icon.svg')
    
    tempparentjoin = {}
    linkdict = {'colparent': 'id_objet',
                'colthistable': 'id_ressource',
                    'tctable': 'Tcobjetressource',
                    'tctablecolparent':'lid_objet',
                    'tctablecolthistable':'lid_ressource'}
    for tablename in ['Observation', 'Noeud', 'Infralineaire', 'Equipement']:
        tempparentjoin[tablename] = linkdict
    PARENTJOIN = tempparentjoin
    TABLEFILTERFIELD = {'typephoto': 'PHO' }


    def __init__(self, **kwargs):
        super(BasePhotoTool, self).__init__(**kwargs)

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
    """

    def initMainToolWidget(self):

        self.toolwidgetmain = UserUI()
        self.formtoolwidgetconfdictmain = {'Photo' : {'linkfield' : 'id_photo',
                                                            'widgets' : {}},
                                            'Objet' : {'linkfield' : 'id_objet',
                                                        'widgets' : {}},
                                            'Ressource' : {'linkfield' : 'id_ressource',
                                                        'widgets' : {'file': self.toolwidgetmain.lineEdit_file,
                                                                    'numressource': self.toolwidgetmain.spinBox_numphoto,
                                                                    'datetimeressource' : self.toolwidgetmain.dateTimeEdit_date}}}

        self.toolwidgetmain.stackedWidget.setCurrentIndex(0)
        self.toolwidgetmain.pushButton_chooseph.clicked.connect(self.choosePhoto)
        self.toolwidgetmain.pushButton_lastph.clicked.connect(self.lastPhoto)
        self.toolwidgetmain.pushButton_openph.clicked.connect(self.openPhoto)
        self.photowdg = PhotoViewer()
        self.toolwidgetmain.frame_ph.layout().addWidget(self.photowdg)

        self.toolwidgetmain.toolButton_photoplus.clicked.connect(self.changeNumPhoto)
        self.toolwidgetmain.toolButton_photomoins.clicked.connect(self.changeNumPhoto)
        self.toolwidgetmain.toolButton_calc.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.spinBox_numphoto))

    def changeNumPhoto(self):
        global numphoto
        if numphoto is None:
            numphoto = 0
        if self.sender() == self.toolwidgetmain.toolButton_photoplus:
            numphoto += 1
        elif self.sender() == self.toolwidgetmain.toolButton_photomoins:
            numphoto = numphoto -1
        self.toolwidgetmain.spinBox_numphoto.setValue(numphoto)

    """
    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass

    def postloadIds(self,sqlin):
        sqlin += " AND typephoto = 'PHO'"
        return sqlin
    """
    
    def magicFunction(self):
        self.featureSelected()
        self.lastPhoto()
        self.addGPSPoint()
        self.saveFeature()

    def setDefaultPhoto(self):
        if self.parentWidget.currentFeature is not None:
            idphoto = self.currentFeature['id_objet']
            idparentfeature=self.parentWidget.currentFeature['id_objet']
            # print('setDefaultPhoto',idphoto,idparentfeature)
            sql = "UPDATE " + str(self.parentWidget.dbasetablename) + " SET  lk_photo = " + str(idphoto) + " WHERE id_objet = " + str(idparentfeature) + ";"
            query = self.dbase.query(sql)
            self.dbase.commit()


    def choosePhoto(self):
        file = None
        file , extension= self.mainifacewidget.qfiledlg.getOpenFileName(None, 'Choose the file', self.mainifacewidget.imagedirectory,
                                                                    'Image (*.jpg)', '')
        if file:
            self.toolwidgetmain.lineEdit_file.setText(os.path.normpath(file))
            self.formutils.showImageinLabelWidget(self.photowdg , self.toolwidgetmain.lineEdit_file.text())


    def lastPhoto(self):
        if self.mainifacewidget.imagedirectory is not None:
            list_of_files = glob.glob(self.mainifacewidget.imagedirectory + "//*.jpg")
            try :
                latest_file = max(list_of_files, key=os.path.getctime)
                self.toolwidgetmain.lineEdit_file.setText(os.path.normpath(latest_file))
                self.showImageinLabelWidget(self.photowdg , self.toolwidgetmain.lineEdit_file.text())
                datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                self.toolwidgetmain.dateTimeEdit_date.setDateTime(QtCore.QDateTime.fromString(datecreation, 'yyyy-MM-dd hh:mm:ss'))

            except ValueError:
                pass

    def openPhoto(self):
        filepath = self.dbase.completePathOfFile(self.toolwidgetmain.lineEdit_file.text())

        if os.path.isfile(filepath ):
            os.startfile(filepath)
        else:
            possiblethumbnail, ext = os.path.splitext(filepath)
            if os.path.isfile(possiblethumbnail + "_thumbnail.png"):
                os.startfile(possiblethumbnail + "_thumbnail.png")


    #def postInitFeatureProperties(self, feat):
    def postSelectFeature(self):
        global numphoto

        if self.currentFeaturePK is None:   #first creation
            #datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
            datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            #self.initFeatureProperties(feat, 'Ressource', 'datetimeressource', datecreation)
            self.formutils.applyResultDict({'datetimeressource' : datecreation},checkifinforgottenfield=False)

            if numphoto is not None:
                self.toolwidgetmain.spinBox_numphoto.setValue(numphoto)

            # geom if parent is node
            if self.parentWidget is not None and self.parentWidget.currentFeaturePK is not None:
                if self.parentWidget.DBASETABLENAME == 'Noeud':

                    # get geom
                    #noeudfet = self.dbase.getLayerFeatureByPk('Noeud', self.parentWidget.currentFeature.id())
                    #neudfetgeom = noeudfet.geometry().asPoint()
                    noeudfetwkt = self.dbase.getValuesFromPk('Noeud',
                                                            'ST_AsText(geom)',
                                                            self.parentWidget.currentFeaturePK)
                    neudfetgeom = qgis.core.QgsGeometry.fromWkt(noeudfetwkt).asPoint()
                    self.mainifacewidget.qgiscanvas.createorresetRubberband(1)
                    self.setTempGeometry([neudfetgeom], False,False)

            self.photowdg.clear()

        else:
            sql = "SELECT file FROM photo_qgis  WHERE pk_photo = " + str(self.currentFeaturePK)
            file = self.dbase.query(sql)[0][0]
            if file is not None and file != '':
                self.formutils.showImageinLabelWidget(self.photowdg, self.toolwidgetmain.lineEdit_file.text())
            else:
                self.photowdg.clear()


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
    """



    def postSaveFeature(self, boolnewfeature):

        global numphoto
        if self.currentFeaturePK is None:
            if self.toolwidgetmain.spinBox_numphoto.value() == -1 :
                numphoto = None
            elif numphoto == self.toolwidgetmain.spinBox_numphoto.value():
                numphoto += 1
            else:
                numphoto = self.toolwidgetmain.spinBox_numphoto.value() + 1



    """
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


        query = self.dbase.query(sql)
        self.dbase.commit()

        return True
    """



class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabase_photo_tool_ui.ui')
        uic.loadUi(uipath, self)

