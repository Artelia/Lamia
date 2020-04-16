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


import os
import datetime
import glob
import sys

from qgis.PyQt import uic, QtCore, QtGui
from qgis.PyQt.QtWidgets import (QWidget, QLabel, QFrame)

from ..base2.lamiabase_photo_tool import BasePhotoTool
from ..base2.lamiabase_photoviewer import PhotoViewer

numphoto = None



class BaseDiguePhotoTool(BasePhotoTool):



    def __init__(self, **kwargs):
        super(BaseDiguePhotoTool, self).__init__(**kwargs)




    def initMainToolWidget(self):


        self.toolwidgetmain = UserUI()
        self.formtoolwidgetconfdictmain = {'Photo': {'linkfield': 'id_photo',
                                            'widgets': {}},
                                    'Objet': {'linkfield': 'id_objet',
                                            'widgets': {}},
                                    'Ressource': {'linkfield': 'id_ressource',
                                                'widgets': {'file': self.toolwidgetmain.lineEdit_file,
                                                            'numressource': self.toolwidgetmain.spinBox_numphoto,
                                                            'datetimeressource': self.toolwidgetmain.dateTimeEdit_date}}}
        
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

        self.toolwidgetmain.pushButton_eau.clicked.connect(self.setDefaultPhoto)
        self.toolwidgetmain.pushButton_crete.clicked.connect(self.setDefaultPhoto)
        self.toolwidgetmain.pushButton_terre.clicked.connect(self.setDefaultPhoto)
        self.toolwidgetmain.pushButton_defaultphoto.clicked.connect(self.setDefaultPhoto)


    """
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


    def setDefaultPhoto(self):
        # print('setDefaultPhoto', self.currentparentfeature)

        if self.currentFeaturePK is None:
            self.windowdialog.errorMessage("Enregistrer d'abord la photo")
            return

        sendername = self.sender().objectName()

        if self.parentWidget.currentFeature is not None:
            sql = "SELECT id_ressource FROM Photo_qgis WHERE pk_photo = " + str(self.currentFeaturePK)
            idressource = self.dbase.query(sql)[0][0]
            pkparentfeature=self.parentWidget.currentFeaturePK
            # print('setDefaultPhoto',idphoto,idparentfeature)


            if sendername == "pushButton_eau":
                field = 'lid_ressource_1'
            elif sendername == "pushButton_crete":
                field = 'lid_ressource_2'
            elif sendername == "pushButton_terre":
                field = 'lid_ressource_3'
            elif sendername == "pushButton_defaultphoto":
                field = 'lid_ressource_1'

            sql = "UPDATE " + str(self.parentWidget.DBASETABLENAME) + " SET " + field +  " = " + str(idressource)
            # sql += " WHERE id_objet = " + str(idparentfeature) + ";"
            sql += " WHERE pk_" + self.parentWidget.DBASETABLENAME.lower() + " = " + str(pkparentfeature)
            query = self.dbase.query(sql)
            self.dbase.commit()



    #def postInitFeatureProperties(self, feat):
    def postSelectFeature(self):
        super(BaseDiguePhotoTool, self).postSelectFeature()
        """
        global numphoto

        if self.currentFeature is None:
            #datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
            datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            self.initFeatureProperties(feat, 'Ressource', 'datetimeressource', datecreation)


            if numphoto is not None:
                self.toolwidgetmain.spinBox_numphoto.setValue(numphoto)
                print('numphoto2', numphoto)

            # geom if parent is node
            if self.parentWidget is not None and self.parentWidget.currentFeature is not None:
                if self.parentWidget.DBASETABLENAME == 'Noeud':

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
        """

        if self.parentWidget is not None and self.parentWidget.currentFeaturePK is not None:
            if self.parentWidget.DBASETABLENAME in ['Equipement']:
                self.toolwidgetmain.stackedWidget_2.setCurrentIndex(0)
            elif self.parentWidget.DBASETABLENAME in ['Infralineaire']:
                self.toolwidgetmain.stackedWidget_2.setCurrentIndex(1)
            else:
                self.toolwidgetmain.stackedWidget_2.setCurrentIndex(2)






    def setDefaultPhotobackup(self):
        # print('setDefaultPhoto', self.currentparentfeature)
        if self.parentWidget.currentFeature is not None and self.parentWidget.DBASETABLENAME == 'Infralineaire':
            idressourcephoto = self.currentFeature['id_ressource']
            idparentfeature=self.parentWidget.currentFeature['id_objet']
            # print('setDefaultPhoto',idphoto,idparentfeature)
            sql = "UPDATE " + str(self.parentWidget.DBASETABLENAME) + " SET  lk_ressource_2 = " + str(idressourcephoto)
            sql += " WHERE id_objet = " + str(idparentfeature) + ";"
            query = self.dbase.query(sql)
            self.dbase.commit()



    def postSaveFeature(self, boolnewfeature):

        global numphoto

        if self.toolwidgetmain.spinBox_numphoto.value() == -1 :
            numphoto = None
        elif numphoto == self.toolwidgetmain.spinBox_numphoto.value():
            numphoto += 1
        else:
            numphoto = self.toolwidgetmain.spinBox_numphoto.value() + 1





class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabasedigue_photo_tool_ui.ui')
        uic.loadUi(uipath, self)
