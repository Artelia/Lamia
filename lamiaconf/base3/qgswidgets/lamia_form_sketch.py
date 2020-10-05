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


import qgis, qgis.utils, os, datetime, PIL, platform

if platform.system() == "Windows":
    from PIL import ImageGrab
from PIL.ImageQt import ImageQt

from qgis.PyQt import uic, QtCore, QtGui
from qgis.PyQt.QtWidgets import QWidget, QMainWindow, QSpinBox, QAction, QDialog, QFrame

from Lamia.iface.qgiswidget.tools.lamia_abstractformtool import AbstractLamiaFormTool
from .lamia_form_pictureviewer import PictureViewer

base3 = QtCore.QObject()


class BaseSketchTool(AbstractLamiaFormTool):

    PREPROTOOLNAME = "sketch"
    DBASETABLENAME = "media"
    LOADFIRST = False

    tooltreewidgetCAT = QtCore.QCoreApplication.translate("base3", "Resources")
    tooltreewidgetSUBCAT = QtCore.QCoreApplication.translate("base3", "Sketches")

    tooltreewidgetICONPATH = os.path.join(
        os.path.dirname(__file__), "lamia_form_sketch_icon.png"
    )

    tempparentjoin = {}
    linkdict = {
        "colparent": "id_object",
        "colthistable": "id_resource",
        "tctable": "Tcobjectresource",
        "tctablecolparent": "lid_object",
        "tctablecolthistable": "lid_resource",
    }
    for tablename in ["observation", "node", "edge", "surface", "equipment", "facility"]:
        tempparentjoin[tablename] = linkdict
    PARENTJOIN = tempparentjoin

    TABLEFILTERFIELD = {"typemedia": "CRO"}
    GEOMETRYSKIP = True

    def __init__(self, **kwargs):
        super(BaseSketchTool, self).__init__(**kwargs)

    def initMainToolWidget(self):
        # ****************************************************************************************
        # userui
        self.toolwidgetmain = UserUI()
        self.formtoolwidgetconfdictmain = {
            "media": {"linkfield": "id_media", "widgets": {}},
            "object": {"linkfield": "id_object", "widgets": {}},
            "resource": {"linkfield": "id_ressource", "widgets": {}},
        }

        # self.groupBox_geom.setParent(None)
        # self.frame_editing.setVisible(False)
        self.toolwidgetmain.stackedWidget.setCurrentIndex(1)

        self.toolwidgetmain.pushButton_open.clicked.connect(self.openFile)
        self.toolwidgetmain.pushButton_edit.clicked.connect(self.editPhoto)
        self.toolwidgetmain.pushButton_getfromclipboard.clicked.connect(self.pasteImage)
        self.editorwindow = ScribbleMainWindow(parentwdg=self)
        self.photowdg = PictureViewer()
        self.toolwidgetmain.frame_cr.layout().addWidget(self.photowdg)

    def postSelectFeature(self):

        if self.currentFeaturePK is None:  # first time
            datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            self.formutils.applyResultDict(
                {"resource": {"datetimeresource": datecreation}}
            )
            self.editorwindow.reinitSize()
            self.editorwindow.clear()
            self.photowdg.clear()

        else:
            sql = "SELECT file FROM media_qgis  WHERE pk_media = " + str(
                self.currentFeaturePK
            )
            file = self.dbase.query(sql)[0][0]
            if (
                file is not None
                and file != ""
                and os.path.isfile(self.dbase.completePathOfFile(file))
            ):
                self.editorwindow.openImage(self.dbase.completePathOfFile(file))
                self.formutils.showImageinLabelWidget(
                    self.photowdg, self.dbase.completePathOfFile(file)
                )
            else:
                self.editorwindow.clear()
                self.photowdg.clear()

    def pasteImage(self):
        if platform.system() == "Windows":
            pilimage = PIL.ImageGrab.grabclipboard()
            if pilimage is not None:
                im = ImageQt(pilimage)
                self.editorwindow.setImage(im)
                self.photowdg.clear()
                self.photowdg.setPixmap(im)
                self.editPhoto()

    def editPhoto(self):
        if qgis.utils.iface is not None:
            self.editorwindow.show()
        else:
            self.editorwindow.setWindowModality(QtCore.Qt.ApplicationModal)
            self.editorwindow.show()

    def openFile(self):
        if self.currentFeaturePK is not None:
            sql = "SELECT file FROM media_qgis  WHERE pk_media = " + str(
                self.currentFeaturePK
            )
            query = self.dbase.query(sql)
            # result = [row[0] for row in query]
            resultfile = query[0][0]
            if os.path.isfile(self.dbase.completePathOfFile(resultfile)):
                filepath = self.dbase.completePathOfFile(resultfile)
                os.startfile(filepath)

    """
    def createParentFeature(self):
        pkobjet = self.dbase.createNewObjet()

        if False:
            # lastrevision = self.dbase.maxrevision
            datetimecreation =  str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            lastobjetid = self.dbase.getLastId('Objet') + 1
            sql = "INSERT INTO Objet (id_objet, lpk_revision_begin, datetimecreation ) "
            sql += "VALUES(" + str(lastobjetid ) + "," + str(self.dbase.maxrevision) +  ",'" + datetimecreation + "');"
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
        datecreation = datetime.datetime.now().strftime("%Y-%m-%d")
        datetimecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


        fileimage = os.path.join('.', self.dbasetablename, ''.join(datecreation.split('-')),
                                 str(lastidphoto) + '_croquis.png')
        if not os.path.exists(os.path.dirname(self.dbase.completePathOfFile(fileimage))):
            os.makedirs(os.path.dirname(self.dbase.completePathOfFile(fileimage)))
        self.editorwindow.saveImage(self.dbase.completePathOfFile(fileimage))


        sql = "UPDATE Photo SET id_photo = " + str(lastidphoto)  + ","
        sql += "lpk_ressource = " + str(pkres)
        sql += ", typephoto = 'CRO' "
        sql += " WHERE pk_photo = " + str(pkphoto) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()


        sql = "UPDATE Ressource SET  file = '" + fileimage + "', datetimeressource = '" + datetimecreation + "'"
        sql += " WHERE pk_ressource = " + str(pkres) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()

        if self.parentWidget is not None and self.parentWidget.currentFeature is not None:
            # self.linkagespec = {'Tcobjetressource'
            if 'Tcobjetressource' in self.linkagespec.keys():
                #get parent id_objet
                sql = " SELECT id_objet FROM " + self.parentWidget.dbasetablename.lower() + "_qgis"
                sql += " WHERE pk_" + self.parentWidget.dbasetablename.lower() + " = " + str(self.parentWidget.currentFeaturePK)
                currentparentlinkfield = self.dbase.query(sql)[0][0]

                #currentparentlinkfield = self.parentWidget.currentFeature['id_objet']
                sql = "INSERT INTO Tcobjetressource(lpk_revision_begin, lid_objet, lid_ressource) "
                sql += " VALUES(" + str(self.dbase.maxrevision) + "," + str(currentparentlinkfield) + ',' + str(lastressourceid) + ")"
                query = self.dbase.query(sql)
                self.dbase.commit()


        if False:
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
    """

    def postSaveFeature(self, savedfeaturepk=None):

        if self.currentFeaturePK is None:  # first creation
            idphoto, pkres = self.dbase.getValuesFromPk(
                self.DBASETABLENAME.lower() + "_qgis",
                ["id_" + self.DBASETABLENAME.lower(), "pk_resource"],
                savedfeaturepk,
            )
            datecreation = datetime.datetime.now().strftime("%Y-%m-%d")
            datetimecreation = str(
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )

            # sql = "UPDATE media SET  mediatype = 'CRO' WHERE pk_photo = {}".format(str(savedfeaturepk))
            # query = self.dbase.query(sql)

            fileimage = os.path.join(
                ".",
                self.DBASETABLENAME,
                "".join(datecreation.split("-")),
                str(idphoto) + "_sketch.png",
            )
            if not os.path.exists(
                os.path.dirname(self.dbase.completePathOfFile(fileimage))
            ):
                os.makedirs(os.path.dirname(self.dbase.completePathOfFile(fileimage)))

            sql = (
                "UPDATE resource SET  file = '"
                + fileimage
                + "', datetimeresource = '"
                + datetimecreation
                + "'"
            )
            sql += " WHERE pk_resource = " + str(pkres)
            query = self.dbase.query(sql)

        else:
            fileimage = self.dbase.getValuesFromPk(
                self.DBASETABLENAME + "_qgis", "file", self.currentFeaturePK
            )

        self.editorwindow.saveImage(self.dbase.completePathOfFile(fileimage))


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), "lamia_form_media_ui.ui")
        uic.loadUi(uipath, self)


class ScribbleMainWindow(QMainWindow):
    def __init__(self, parentwdg=None, parent=None):
        super(ScribbleMainWindow, self).__init__(parent=parent)
        uipath = os.path.join(
            os.path.dirname(__file__), "lamia_form_sketch_drawingwdg_ui.ui"
        )
        uic.loadUi(uipath, self)
        self.parentwdg = parentwdg
        self.scribbleArea = ScribbleArea(parent=self)
        self.scribbleArea.clearImage()
        self.scribbleArea.mainWindow = self  # maybe not using this?

        self.scrollArea.setWidget(self.scribbleArea)

        self.toolbar = self.addToolBar("Color")
        self.colorwdg = qgis.gui.QgsColorButton()
        self.colorwdg.setColor(QtCore.Qt.black)
        self.toolbar.addWidget(self.colorwdg)
        self.spinb = QSpinBox()
        self.spinb.setValue(3)
        self.toolbar.addWidget(self.spinb)

        self.spinb.valueChanged.connect(self.scribbleArea.setPenWidth)
        self.colorwdg.colorChanged.connect(self.scribbleArea.setPenColor)

        self.clearAction = QAction("Clear", self)
        self.clearAction.triggered.connect(self.scribbleArea.clearImage)
        self.toolbar.addAction(self.clearAction)

        self.reinitAction = QAction("reinit", self)
        self.reinitAction.triggered.connect(self.scribbleArea.reinit)
        self.toolbar.addAction(self.reinitAction)

    def reinitSize(self):
        self.scribbleArea.reinitSize()

    def saveImage(self, file):
        self.scribbleArea.saveImage(file, "png")

    def clear(self):
        self.scribbleArea.clearImage()

    def openImage(self, file):
        self.scribbleArea.openImage(file)

    def setImage(self, qimage):
        self.scribbleArea.setImage(qimage)

    def closeEvent(self, event):
        self.parentwdg.photowdg.clear()
        self.parentwdg.photowdg.setPixmap(self.scribbleArea.image)
        event.accept()


class ScribbleArea(QWidget):
    """
      this scales the image but it's not good, too many refreshes really mess it up!!!
    """

    def __init__(self, larg=500, haut=500, parent=None):
        super(ScribbleArea, self).__init__(parent)
        # self.setAttribute(QtCore.Qt.WA_StaticContents)
        self.setFixedSize(larg, haut)
        self.modified = False
        self.scribbling = False
        self.myPenWidth = 3
        self.myPenColor = QtCore.Qt.black
        imageSize = QtCore.QSize(larg, haut)
        #       self.image = QtGui.QImage()
        self.image = QtGui.QImage(imageSize, QtGui.QImage.Format_RGB32)
        self.lastPoint = QtCore.QPoint()

        self.currentfilename = None

    def openImage(self, fileName=None):
        loadedImage = QtGui.QImage()
        if not loadedImage.load(fileName):
            return False
        self.currentfilename = fileName
        return self.setImage(loadedImage)

    def reinit(self):
        if self.currentfilename is not None:
            self.openImage(self.currentfilename)

    def reinitSize(self):
        self.setFixedSize(500, 500)
        self.mainWindow.resize(500, 500)
        imageSize = QtCore.QSize(500, 500)
        self.image = QtGui.QImage(imageSize, QtGui.QImage.Format_RGB32)

    def setImage(self, loadedImage):
        w = loadedImage.width()
        h = loadedImage.height()
        self.setFixedSize(w, h)
        self.mainWindow.resize(w, h)

        #       newSize = loadedImage.size().expandedTo(self.size())
        #       self.resizeImage(loadedImage, newSize)
        self.image = loadedImage
        self.modified = False
        self.update()
        return True

    def saveImage(self, fileName, fileFormat):
        if self.image.save(fileName, fileFormat):
            self.modified = False
            return True
        else:
            return False

    def setPenColor(self, newColor):
        self.myPenColor = newColor

    def setPenWidth(self, newWidth):
        self.myPenWidth = newWidth

    def clearImage(self):
        # print('celar')
        self.image.fill(QtGui.qRgb(255, 255, 255))
        self.modified = True
        self.update()

    def mousePressEvent(self, event):
        #       print "self.image.width() = %d" % self.image.width()
        #       print "self.image.height() = %d" % self.image.height()
        #       print "self.image.size() = %s" % self.image.size()
        #       print "self.size() = %s" % self.size()
        #       print "event.pos() = %s" % event.pos()
        if event.button() == QtCore.Qt.LeftButton:
            self.lastPoint = event.pos()
            self.scribbling = True

    def mouseMoveEvent(self, event):
        if (event.buttons() & QtCore.Qt.LeftButton) and self.scribbling:
            self.drawLineTo(event.pos())

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and self.scribbling:
            self.drawLineTo(event.pos())
            self.scribbling = False

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawImage(event.rect(), self.image, event.rect())

    def drawLineTo(self, endPoint):
        painter = QtGui.QPainter(self.image)
        painter.setPen(
            QtGui.QPen(
                self.myPenColor,
                self.myPenWidth,
                QtCore.Qt.SolidLine,
                QtCore.Qt.RoundCap,
                QtCore.Qt.RoundJoin,
            )
        )
        painter.drawLine(self.lastPoint, endPoint)
        self.modified = True

        # rad = self.myPenWidth / 2 + 2
        # self.update(QtCore.QRect(self.lastPoint, endPoint).normalized().adjusted(-rad, -rad, +rad, +rad))
        self.update()
        self.lastPoint = QtCore.QPoint(endPoint)

    def print_(self):
        printer = QtGui.QPrinter(QtGui.QPrinter.HighResolution)

        printDialog = QtGui.QPrintDialog(printer, self)
        if printDialog.exec_() == QDialog.Accepted:
            painter = QtGui.QPainter(printer)
            rect = painter.viewport()
            size = self.image.size()
            size.scale(rect.size(), QtCore.Qt.KeepAspectRatio)
            painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
            painter.setWindow(self.image.rect())
            painter.drawImage(0, 0, self.image)
            painter.end()

    def isModified(self):
        return self.modified

    def penColor(self):
        return self.myPenColor

    def penWidth(self):
        return self.myPenWidth
