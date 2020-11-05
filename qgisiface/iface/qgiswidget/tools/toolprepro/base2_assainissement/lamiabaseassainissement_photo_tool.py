# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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
# from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..base2.lamiabase_photo_tool import BasePhotoTool
from ..base2.lamiabase_photoviewer import PhotoViewer
import os
import datetime
import glob

numphoto = None



class BaseAssainissementPhotoTool(BasePhotoTool):


    def __init__(self, **kwargs):
        super(BaseAssainissementPhotoTool, self).__init__(**kwargs)

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



        # ****************************************************************************************
        # child widgets
        pass

        if True:
            self.toolwidgetmain.pushButton_vueensemble.clicked.connect(self.setDefaultPhoto)
            self.toolwidgetmain.pushButton_cuve.clicked.connect(self.setDefaultPhoto)
            self.toolwidgetmain.pushButton_poires.clicked.connect(self.setDefaultPhoto)
            self.toolwidgetmain.pushButton_vanne.clicked.connect(self.setDefaultPhoto)
            self.toolwidgetmain.pushButton_armoire.clicked.connect(self.setDefaultPhoto)


    def setDefaultPhoto(self):
        # print('setDefaultPhoto', self.currentparentfeature)

        if self.currentFeaturePK is None:
            self.mainifacewidget.errorMessage("Enregistrer d'abord la photo")
            return

        sendername = self.sender().objectName()


        if self.parentWidget.currentFeature is not None:
            sql = "SELECT id_ressource FROM Photo_qgis WHERE pk_photo = " + str(self.currentFeaturePK)
            idressource = self.dbase.query(sql)[0][0]
            pkparentfeature=self.parentWidget.currentFeaturePK

            if sendername == "pushButton_vueensemble":
                field = 'lid_ressource_1'
            elif sendername == "pushButton_cuve":
                field = 'lid_ressource_2'
            elif sendername == "pushButton_poires":
                field = 'lid_ressource_4'
            elif sendername == "pushButton_vanne":
                field = 'lid_ressource_5'
            elif sendername == "pushButton_armoire":
                field = 'lid_ressource_6'

            sql = "UPDATE " + str(self.parentWidget.dbasetablename) + " SET " + field +  " = " + str(idressource)
            # sql += " WHERE id_objet = " + str(idparentfeature) + ";"
            sql += " WHERE pk_" + self.parentWidget.dbasetablename.lower() + " = " + str(pkparentfeature)
            query = self.dbase.query(sql)
            self.dbase.commit()





    #def postInitFeatureProperties(self, feat):
    def postSelectFeature(self):

        global numphoto
        super(BaseAssainissementPhotoTool, self).postSelectFeature()
        """
        if self.currentFeature is None:
            #datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
            datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            self.initFeatureProperties(feat, 'Ressource', 'datetimeressource', datecreation)


            if numphoto is not None:
                self.toolwidgetmain.spinBox_numphoto.setValue(numphoto)
                print('numphoto2', numphoto)

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

        """
        if self.parentWidget is not None and self.parentWidget.currentFeaturePK is not None:
            if self.parentWidget.DBASETABLENAME == 'Noeud':
                typeouvrageass = self.dbase.getValuesFromPk(self.parentWidget.DBASETABLENAME + '_qgis',
                                                            'typeOuvrageAss',
                                                            self.parentWidget.currentFeaturePK)
                if typeouvrageass == '10':
                    self.toolwidgetmain.stackedWidget_2.setCurrentIndex(1)
                else:
                    self.toolwidgetmain.stackedWidget_2.setCurrentIndex(2)

    """
    def postSaveFeature(self, boolnewfeature):

        global numphoto

        if self.toolwidgetmain.spinBox_numphoto.value() == -1 :
            numphoto = None
        elif numphoto == self.toolwidgetmain.spinBox_numphoto.value():
            numphoto += 1
        else:
            numphoto = self.toolwidgetmain.spinBox_numphoto.value() + 1
    """


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabaseassainissement_photo_tool_ui.ui')
        uic.loadUi(uipath, self)