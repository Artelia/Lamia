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

import sys
import os
import datetime, platform
import subprocess
import glob
import tempfile

import qgis, qgis.core
from qgis.PyQt import uic, QtCore, QtGui

try:
    from qgis.PyQt.QtGui import QWidget, QLabel, QFrame
except ImportError:
    from qgis.PyQt.QtWidgets import QWidget, QLabel, QFrame

from Lamia.qgisiface.iface.qgiswidget.tools.lamia_abstractformtool import (
    AbstractLamiaFormTool,
)
from .lamia_form_pictureviewer import PictureViewer

prefixhoto = ""
numphoto = None
base3 = QtCore.QObject()


class BaseCameraTool(AbstractLamiaFormTool):

    PREPROTOOLNAME = "camera"
    DBASETABLENAME = "media"
    LOADFIRST = False

    tooltreewidgetCAT = QtCore.QCoreApplication.translate("base3", "Resources")
    tooltreewidgetSUBCAT = QtCore.QCoreApplication.translate("base3", "Camera")
    tooltreewidgetICONPATH = os.path.join(
        os.path.dirname(__file__), "lamia_form_camera_icon.svg"
    )

    tempparentjoin = {}
    linkdict = {
        "colparent": "id_object",
        "colthistable": "id_resource",
        "tctable": "tcobjectresource",
        "tctablecolparent": "lid_object",
        "tctablecolthistable": "lid_resource",
    }
    for tablename in [
        "observation",
        "node",
        "edge",
        "surface",
        "equipment",
        "facility",
    ]:
        tempparentjoin[tablename] = linkdict
    PARENTJOIN = tempparentjoin

    TABLEFILTERFIELD = {"typemedia": "PHO"}

    def __init__(self, **kwargs):
        super(BaseCameraTool, self).__init__(**kwargs)

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
        self.formtoolwidgetconfdictmain = {
            "media": {"linkfield": "id_media", "widgets": {}},
            "object": {
                "linkfield": "id_object",
                "widgets": {"comment": self.toolwidgetmain.comment,},
            },
            "resource": {
                "linkfield": "id_resource",
                "widgets": {
                    # "file": self.toolwidgetmain.lineEdit_file,
                    # "resourceindex": self.toolwidgetmain.spinBox_numphoto,
                    # "datetimeresource": self.toolwidgetmain.dateTimeEdit_date,
                    "file": self.toolwidgetmain.file,
                    "resourceindex": self.toolwidgetmain.resourceindex,
                    "datetimeresource": self.toolwidgetmain.datetimeresource,
                },
            },
        }

        self.toolwidgetmain.stackedWidget.setCurrentIndex(0)
        self.toolwidgetmain.pushButton_chooseph.clicked.connect(self.choosePhoto)
        self.toolwidgetmain.pushButton_lastph.clicked.connect(self.lastPhoto)
        self.toolwidgetmain.pushButton_openph.clicked.connect(self.openPhoto)
        self.photowdg = PictureViewer()
        self.toolwidgetmain.frame_ph.layout().addWidget(self.photowdg)

        self.toolwidgetmain.toolButton_photoplus.clicked.connect(self.changeNumPhoto)
        self.toolwidgetmain.toolButton_photomoins.clicked.connect(self.changeNumPhoto)
        self.toolwidgetmain.toolButton_calc.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.resourceindex)
        )

        self.toolwidgetmain.pushButton_pictureparent.clicked.connect(
            self.setPictureForParent
        )

    def changeNumPhoto(self):
        global numphoto
        if numphoto is None:
            numphoto = 0
        if self.sender() == self.toolwidgetmain.toolButton_photoplus:
            numphoto += 1
        elif self.sender() == self.toolwidgetmain.toolButton_photomoins:
            numphoto = numphoto - 1
        self.toolwidgetmain.resourceindex.setValue(numphoto)

    # def magicFunction(self):
    #     self.featureSelected()
    #     self.lastPhoto()
    #     self.addGPSPoint()
    #     self.saveFeature()

    def toolbarMagic(self):
        self.toolbarNew()
        self.lastPhoto()
        self.toolbarGeomAddGPS()
        self.toolbarSave()

    def setDefaultPhoto(self):
        if self.currentFeaturePK is None:
            self.mainifacewidget.errorMessage("Enregistrer d'abord la photo")
            return

        idresource = self.dbase.getValuesFromPk(
            "node", "id_resource", self.currentFeaturePK
        )

        sql = "UPDATE " + str(self.parentWidget.DBASETABLENAME)
        sql += " SET  lid_resource_1 = " + str(idphoto)
        sql += (
            " WHERE id_"
            + +str(self.parentWidget.DBASETABLENAME)
            + " = "
            + str(self.parentWidget.currentFeaturePK)
            + ";"
        )
        query = self.dbase.query(sql)

    def setPictureForParent(self):

        if not self.parentWidget and not self.parentWidget.parentWidget:
            return

        parentWidget = self.parentWidget.parentWidget
        while parentWidget and parentWidget.SKIP_LOADING_UI:
            parentWidget = parentWidget.parentWidget

        if (
            parentWidget is not None
            and parentWidget.currentFeaturePK is not None
            and self.currentFeaturePK is not None
        ):
            parentidobj = self.dbase.getValuesFromPk(
                parentWidget.DBASETABLENAME + "_qgis",
                "id_object",
                parentWidget.currentFeaturePK,
            )
            photores = self.dbase.getValuesFromPk(
                "media_qgis", "id_resource", self.currentFeaturePK
            )

            sql = f"""INSERT INTO tcobjectresource(lpk_revision_begin, lid_resource, lid_object) 
                VALUES ({self.dbase.maxrevision}, {photores}, {parentidobj})"""
            print(sql)
            self.dbase.query(sql)

    def choosePhoto(self):
        file = None
        file, extension = self.mainifacewidget.qfiledlg.getOpenFileName(
            None,
            "Choose the file",
            self.mainifacewidget.imagedirectory,
            "Image (*.jpg)",
            "",
        )
        if file:
            self.toolwidgetmain.file.setText(os.path.normpath(file))
            self.formutils.showImageinLabelWidget(
                self.photowdg, self.toolwidgetmain.file.text()
            )

    def lastPhoto(self):
        if self.mainifacewidget.imagedirectory is not None:
            list_of_files = glob.glob(self.mainifacewidget.imagedirectory + "//*.jpg")
            try:
                latest_file = max(list_of_files, key=os.path.getctime)
                self.toolwidgetmain.file.setText(os.path.normpath(latest_file))
                self.showImageinLabelWidget(
                    self.photowdg, self.toolwidgetmain.file.text()
                )
                datecreation = str(
                    datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                )
                self.toolwidgetmain.datetimeresource.setDateTime(
                    QtCore.QDateTime.fromString(datecreation, "yyyy-MM-dd hh:mm:ss")
                )

            except ValueError:
                pass

    def openPhoto(self):

        filepath = self.dbase.completePathOfFile(self.toolwidgetmain.file.text())

        if os.path.isfile(filepath):
            os.startfile(filepath)
        else:
            if self.currentFeaturePK and "thumbnail" in self.dbase.getColumns(
                "resource"
            ):
                sql = "SELECT thumbnail FROM media_qgis  WHERE pk_media = " + str(
                    self.currentFeaturePK
                )
                binimg = self.dbase.query(sql)[0][0]
                thumbpath = os.path.join(tempfile.gettempdir(), "lamiathumbnail.png")
                f = open(thumbpath, "wb")
                f.write(binimg)
                f.close()
                os.startfile(thumbpath)
            else:
                possiblethumbnail, ext = os.path.splitext(filepath)
                if os.path.isfile(possiblethumbnail + "_thumbnail.png"):
                    os.startfile(possiblethumbnail + "_thumbnail.png")

    # def postInitFeatureProperties(self, feat):
    def postSelectFeature(self):
        global numphoto
        self.photowdg.clear()

        if self.currentFeaturePK is None:  # first creation
            datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            self.formutils.applyResultDict(
                {"datetimeresource": datecreation}, checkifinforgottenfield=False
            )

            if numphoto is not None:
                self.toolwidgetmain.resourceindex.setValue(numphoto)

            # geom if parent is node
            if (
                self.parentWidget is not None
                and self.parentWidget.currentFeaturePK is not None
            ):
                if self.parentWidget.DBASETABLENAME == "node":
                    # get geom
                    noeudfetwkt = self.dbase.getValuesFromPk(
                        "node", "ST_AsText(geom)", self.parentWidget.currentFeaturePK
                    )
                    neudfetgeom = qgis.core.QgsGeometry.fromWkt(noeudfetwkt).asPoint()
                    # self.mainifacewidget.qgiscanvas.createorresetRubberband(1)
                    self.setTempGeometry([neudfetgeom], False, False)

            self.photowdg.clear()

        else:
            if "thumbnail" in self.dbase.getColumns("resource"):
                sql = "SELECT file, thumbnail FROM media_qgis  WHERE pk_media = " + str(
                    self.currentFeaturePK
                )
                file, thumbnail = self.dbase.query(sql)[0]
            else:
                sql = "SELECT file FROM media_qgis  WHERE pk_media = " + str(
                    self.currentFeaturePK
                )
                file, thumbnail = self.dbase.query(sql)[0][0], None

            if thumbnail:
                self.formutils.showImageinLabelWidget(self.photowdg, thumbnail)

            elif file is not None and file != "":
                self.formutils.showImageinLabelWidget(
                    self.photowdg, self.toolwidgetmain.file.text()
                )
            else:
                self.photowdg.clear()

    def postSaveFeature(self, boolnewfeature):

        global numphoto
        if self.currentFeaturePK is None:
            if self.toolwidgetmain.resourceindex.value() == -1:
                numphoto = None
            elif numphoto == self.toolwidgetmain.resourceindex.value():
                numphoto += 1
            else:
                numphoto = self.toolwidgetmain.resourceindex.value() + 1

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
        uipath = os.path.join(os.path.dirname(__file__), "lamia_form_camera_ui.ui")
        uic.loadUi(uipath, self)
