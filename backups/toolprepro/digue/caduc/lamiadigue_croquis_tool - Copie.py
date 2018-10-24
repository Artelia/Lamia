# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore, QtGui

try:
    from qgis.PyQt.QtGui import (QWidget, QMainWindow, QSpinBox, QAction, QDialog, QLabel, QFrame)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget,QMainWindow, QSpinBox, QAction, QDialog, QLabel, QFrame)
from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
import os
import qgis
import datetime


FORM_CLASS3, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'FreeHandEditorToolUser.ui'))


class CroquisTool(AbstractInspectionDigueTool):


    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None, parentwidget=None, parent=None):
        super(CroquisTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil, parentwidget, parent=parent)

    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Ressources'
        self.NAME = 'Croquis'
        self.dbasetablename = 'Photo'
        self.visualmode = [1, 2]
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
            self.photowdg = Label()
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
        if os.path.isfile(self.dbase.completePathOfFile(self.currentFeature['File'] )):
            filepath = self.dbase.completePathOfFile(self.currentFeature['File'])
            os.startfile(filepath)


    def createParentFeature(self):

        datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
        sql = "INSERT INTO Objet (datecreation) VALUES('" + datecreation + "');"
        query = self.dbase.query(sql)
        self.dbase.commit()
        idobjet = self.dbase.getLastRowId('Objet')

        sql = "INSERT INTO Ressource (id_objet) VALUES(" + str(idobjet) + ");"
        query = self.dbase.query(sql)
        self.dbase.commit()
        idres = self.dbase.getLastRowId('Ressource')

        idcroquis = self.currentFeature.id()

        fileimage = os.path.join('.', self.dbasetablename, ''.join(datecreation.split('-')),
                                 str(idcroquis) + '_croquis.png')
        if not os.path.exists(os.path.dirname(self.dbase.completePathOfFile(fileimage))):
            os.makedirs(os.path.dirname(self.dbase.completePathOfFile(fileimage)))
        self.editorwindow.saveImage(self.dbase.completePathOfFile(fileimage))


        sql = "UPDATE Photo SET id_objet = " + str(idobjet) + ",id_ressource = " + str(idres) + ",typephoto = 'CRO' "
        sql += " WHERE id_photo = " + str(idcroquis) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()
        sql = "UPDATE Ressource SET  file = '" + fileimage + "', dateressource = '" + datecreation + "'" + " WHERE id_ressource = " + str(idres) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()

        if self.parentWidget is not None and self.parentWidget.currentFeature is not None:
            currentparentlinkfield = self.parentWidget.currentFeature['id_objet']
            sql = "INSERT INTO Tcobjetressource(id_tcobjet, id_tcressource) VALUES(" + str(currentparentlinkfield) + ", " + str(idres) + ");"
            query = self.dbase.query(sql)
            self.dbase.commit()

            if False:
                if self.parentWidget.dbasetablename == 'Equipement':
                    currentparentlinkfield = self.parentWidget.currentFeature['id_objet']
                    sql = "INSERT INTO Tcobjetressource(id_tcobjet, id_tcressource) VALUES(" +  str(currentparentlinkfield) + ", " +  str(idres) + ");"
                    print('createparent',sql)
                    query = self.dbase.query(sql)
                    self.dbase.commit()

                elif self.parentWidget.dbasetablename == 'Observation':
                    currentparentlinkfield = self.parentWidget.currentFeature['id_objet']
                    #sql = "UPDATE PHOTO SET LkObjet = " + str(currentparentlinkfield) + " WHERE id = " + str(idphoto) + ";"
                    sql = "INSERT INTO Tcobjetressource(id_tcobjet, id_tcressource) VALUES(" + str(currentparentlinkfield) + ", " + str(idres) + ");"
                    query = self.dbase.query(sql)
                    self.dbase.commit()

                elif self.parentWidget.dbasetablename == 'Profil':
                    currentparentlinkfield = self.parentWidget.currentFeature['id_objet']
                    #sql = "UPDATE PHOTO SET LkObjet = " + str(currentparentlinkfield) + " WHERE id = " + str(idphoto) + ";"
                    sql = "INSERT INTO Tcobjetressource(id_tcobjet, id_tcressource) VALUES(" + str(currentparentlinkfield) + ", " + str(idres) + ");"
                    query = self.dbase.query(sql)
                    self.dbase.commit()


                if False and self.parentWidget.dbasetablename == 'PROFILTRAVERS':
                    currentparentlinkfield = self.parentWidget.currentFeature['IdObjet']
                    sql = "UPDATE CROQUIS SET LkObjet = " + str(currentparentlinkfield) + " WHERE id = " + str(
                        idcroquis) + ";"
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




class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'PhotoToolUser.ui')
        uic.loadUi(uipath, self)

class ScribbleMainWindow(QMainWindow):
    def __init__(self, parentwdg=None, parent=None):
        super(ScribbleMainWindow, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'FreeHandEditorToolUser.ui')
        uic.loadUi(uipath, self)
        self.parentwdg = parentwdg
        self.scribbleArea = ScribbleArea(parent=self)
        self.scribbleArea.clearImage()
        self.scribbleArea.mainWindow = self  # maybe not using this?

        self.scrollArea.setWidget(self.scribbleArea)

        self.toolbar = self.addToolBar('Color')
        if int(str(self.parentwdg.dbase.qgisversion_int)[0:3]) < 220:
            self.colorwdg = qgis.gui.QgsColorButtonV2()
        else:
            self.colorwdg = qgis.gui.QgsColorButton()
        self.colorwdg.setColor(QtCore.Qt.black)
        self.toolbar.addWidget(self.colorwdg)
        self.spinb = QSpinBox()
        self.spinb.setValue(3)
        self.toolbar.addWidget(self.spinb)

        self.spinb.valueChanged.connect(self.scribbleArea.setPenWidth)
        self.colorwdg.colorChanged.connect(self.scribbleArea.setPenColor)

        self.clearAction = QAction('Clear', self)
        self.clearAction.triggered.connect(self.scribbleArea.clearImage)
        self.toolbar.addAction(self.clearAction)


    def saveImage(self,file):
        self.scribbleArea.saveImage(file,"png")

    def clear(self):
        self.scribbleArea.clearImage()

    def openImage(self,file):
        self.scribbleArea.openImage(file)


class ScribbleArea(QWidget):
    """
      this scales the image but it's not good, too many refreshes really mess it up!!!
    """
    def __init__(self, larg=500,haut=500, parent=None):
        super(ScribbleArea, self).__init__(parent)



        #self.setAttribute(QtCore.Qt.WA_StaticContents)
        self.setFixedSize(larg, haut)
        self.modified = False
        self.scribbling = False
        self.myPenWidth = 3
        self.myPenColor = QtCore.Qt.black
        imageSize = QtCore.QSize(larg, haut)
#       self.image = QtGui.QImage()
        self.image = QtGui.QImage(imageSize, QtGui.QImage.Format_RGB32)
        self.lastPoint = QtCore.QPoint()

    def openImage(self, fileName):
        loadedImage = QtGui.QImage()
        if not loadedImage.load(fileName):
            return False

        w = loadedImage.width()
        h = loadedImage.height()
        self.mainWindow.resize(w, h)

#       newSize = loadedImage.size().expandedTo(self.size())
#       self.resizeImage(loadedImage, newSize)
        self.image = loadedImage
        self.modified = False
        self.update()
        return True

    def saveImage(self, fileName, fileFormat):
        visibleImage = self.image
        #self.resizeImage(visibleImage, self.size())

        #fileName = 'C://test1.png'
        #fileFormat = "PNG"

        if visibleImage.save(fileName, fileFormat):
            self.modified = False
            return True
        else:
            return False

    def setPenColor(self, newColor):
        self.myPenColor = newColor

    def setPenWidth(self, newWidth):
        self.myPenWidth = newWidth

    def clearImage(self):
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
        painter.drawImage(event.rect(), self.image,event.rect())


    if False:
        def resizeEvent(self, event):
            #       print "resize event"
            #       print "event = %s" % event
            #       print "event.oldSize() = %s" % event.oldSize()
            #       print "event.size() = %s" % event.size()

            self.resizeImage(self.image, event.size())

            #       if self.width() > self.image.width() or self.height() > self.image.height():
            #           newWidth = max(self.width() + 128, self.image.width())
            #           newHeight = max(self.height() + 128, self.image.height())
            #           print "newWidth = %d, newHeight = %d" % (newWidth, newHeight)
            #           self.resizeImage(self.image, QtCore.QSize(newWidth, newHeight))
            #           self.update()

            super(ScribbleArea, self).resizeEvent(event)

    def drawLineTo(self, endPoint):
        painter = QtGui.QPainter(self.image)
        painter.setPen(QtGui.QPen(self.myPenColor, self.myPenWidth,
            QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
        painter.drawLine(self.lastPoint, endPoint)
        self.modified = True

        # rad = self.myPenWidth / 2 + 2
        # self.update(QtCore.QRect(self.lastPoint, endPoint).normalized().adjusted(-rad, -rad, +rad, +rad))
        self.update()
        self.lastPoint = QtCore.QPoint(endPoint)


    if False:
        def resizeImage(self, image, newSize):
            if image.size() == newSize:
                return

            #       print "image.size() = %s" % repr(image.size())
            #       print "newSize = %s" % newSize

            # this resizes the canvas without resampling the image
            newImage = QtGui.QImage(newSize, QtGui.QImage.Format_RGB32)
            newImage.fill(QtGui.qRgb(255, 255, 255))
            painter = QtGui.QPainter(newImage)
            painter.drawImage(QtCore.QPoint(0, 0), image)


            ##  this resampled the image but it gets messed up with so many events...
            ##      painter.setRenderHint(QtGui.QPainter.SmoothPixmapTransform, True)
            ##      painter.setRenderHint(QtGui.QPainter.HighQualityAntialiasing, True)
            #
            #       newImage = QtGui.QImage(newSize, QtGui.QImage.Format_RGB32)
            #       newImage.fill(QtGui.qRgb(255, 255, 255))
            #       painter = QtGui.QPainter(newImage)
            #       srcRect = QtCore.QRect(QtCore.QPoint(0,0), image.size())
            #       dstRect = QtCore.QRect(QtCore.QPoint(0,0), newSize)
            ##      print "srcRect = %s" % srcRect
            ##      print "dstRect = %s" % dstRect
            #       painter.drawImage(dstRect, image, srcRect)


            self.image = newImage

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


class Label(QLabel):
    def __init__(self, img = None):
        super(Label, self).__init__()
        self.setFrameStyle(QFrame.StyledPanel)
        self.pixmap = QtGui.QPixmap(img)

    def paintEvent(self, event):
        size = self.size()
        painter = QtGui.QPainter(self)
        point = QtCore.QPoint(0,0)
        if not self.pixmap.isNull() :
            scaledPix = self.pixmap.scaled(size, QtCore.Qt.KeepAspectRatio, transformMode = QtCore.Qt.SmoothTransformation)
            # start painting the label from left upper corner
            if True:
                point.setX((size.width() - scaledPix.width())/2)
                point.setY((size.height() - scaledPix.height())/2)
                #print point.x(), ' ', point.y()
                painter.drawPixmap(point, scaledPix)
            if False:
                painter.drawPixmap(point, scaledPix)

    def setPixmap(self, img):
        self.pixmap = QtGui.QPixmap(img)
        self.repaint()

    def clear(self):
        self.pixmap = QtGui.QPixmap()
        self.repaint()