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

import os
import datetime
import glob


from qgis.PyQt import uic, QtCore, QtGui
from qgis.PyQt.QtWidgets import QWidget, QLabel, QFrame

from ...base3.qgswidgets.lamia_form_camera import BaseCameraTool

# from ..base3.lamiabase_pictureviewer import PictureViewer


numphoto = None


class BaseLeveeCameraTool(BaseCameraTool):
    def __init__(self, **kwargs):
        super(BaseLeveeCameraTool, self).__init__(**kwargs)

    def initMainToolWidget(self):
        super(BaseLeveeCameraTool, self).initMainToolWidget()

        defaultbuttons = DefaultButtons()
        self.toolwidgetmain.stackedWidget_2.removeWidget(
            self.toolwidgetmain.stackedWidget_2.widget(1)
        )
        self.toolwidgetmain.stackedWidget_2.insertWidget(1, defaultbuttons)

        self.toolwidgetmain.pushButton_defaultphoto.clicked.connect(
            self.setDefaultPhoto
        )
        self.formutils.mergeQtWidgets(self.toolwidgetmain, defaultbuttons)

        self.toolwidgetmain.pushButton_water.clicked.connect(self.setDefaultPhoto)
        self.toolwidgetmain.pushButton_crest.clicked.connect(self.setDefaultPhoto)
        self.toolwidgetmain.pushButton_land.clicked.connect(self.setDefaultPhoto)

    def setDefaultPhoto(self):

        if self.currentFeaturePK is None:
            self.mainifacewidget.errorMessage("Enregistrer d'abord la photo")
            return
        sendername = self.sender().objectName()

        if (
            self.parentWidget is not None
            and self.parentWidget.currentFeaturePK is not None
        ):
            sql = "SELECT id_resource FROM media_qgis WHERE pk_media = " + str(
                self.currentFeaturePK
            )
            idressource = self.dbase.query(sql)[0][0]
            pkparentfeature = self.parentWidget.currentFeaturePK

            if sendername in ["pushButton_water", "pushButton_defaultphoto"]:
                field = "lid_resource_1"
            elif sendername == "pushButton_crest":
                field = "lid_resource_2"
            elif sendername == "pushButton_land":
                field = "lid_resource_3"

            # sql = (
            #     "UPDATE "
            #     + str(self.parentWidget.DBASETABLENAME)
            #     + " SET "
            #     + field
            #     + " = "
            #     + str(idressource)
            # )
            # sql += (
            #     " WHERE pk_"
            #     + self.parentWidget.DBASETABLENAME.lower()
            #     + " = "
            #     + str(pkparentfeature)
            # )
            # query = self.dbase.query(sql)

            self.dbase.lamiaorm[self.parentWidget.DBASETABLENAME].update(
                pkparentfeature, {field: idressource}
            )

    # def postInitFeatureProperties(self, feat):
    def postSelectFeature(self):

        global numphoto
        super().postSelectFeature()

        if (
            self.parentWidget is not None
            and self.parentWidget.currentFeaturePK is not None
        ):
            if self.parentWidget.DBASETABLENAME == "edge":
                self.toolwidgetmain.stackedWidget_2.setCurrentIndex(1)
            else:
                self.toolwidgetmain.stackedWidget_2.setCurrentIndex(0)

    def toolbarMagic(self):
        self.mainifacewidget.toolbarNew()
        self.lastPhoto()
        self.toolbarGeomAddGPS()
        self.mainifacewidget.toolbarSave()


class DefaultButtons(QWidget):
    def __init__(self, parent=None):
        super(DefaultButtons, self).__init__(parent=parent)
        uipath = os.path.join(
            os.path.dirname(__file__), "lamia_form_camera_defaultbuttons_ui.ui",
        )
        uic.loadUi(uipath, self)
