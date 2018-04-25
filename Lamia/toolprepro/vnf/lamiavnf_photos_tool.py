# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore, QtGui
try:
    from qgis.PyQt.QtGui import (QWidget, QLabel, QFrame)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget, QLabel, QFrame)

#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..abstract.lamia_photos_tool import AbstractPhotosTool
import os
import datetime
import glob

import sqlite3


#FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), '..', 'dialog', 'InspectionDigue_propertieswidget.ui'))



class PhotosTool(AbstractPhotosTool):

    LOADFIRST = False
    dbasetablename = 'Photo'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None,gpsutil=None, parentwidget=None, parent=None):
        super(PhotosTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)

    """
    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Ressources'
        self.NAME = 'Photographies'
        self.dbasetablename = 'Photo'
        self.visualmode = [1, 2]
        self.PointENABLED = True
        # self.LineENABLED = True
        # self.PolygonEnabled = True
        self.magicfunctionENABLED = True
        self.linkagespec = {'Tcobjetressource' : {'tabletc' : 'Tcobjetressource',
                                              'idsource' : 'id_ressource',
                                            'idtcsource' : 'id_tcressource',
                                           'iddest' : 'id_objet',
                                           'idtcdest' : 'id_tcobjet',
                                           'desttable' : ['Infralineaire','Observation','Equipement']},
                            'Marche' :{'tabletc' : None,
                                              'idsource' : 'lk_marche',
                                            'idtcsource' : None,
                                           'iddest' : 'id_marche',
                                           'idtcdest' : None,
                                           'desttable' : ['Marche']} }
        # self.pickTable = None

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
            self.photowdg = Label()
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
        file, extension = self.qfiledlg.getOpenFileNameAndFilter(None, 'Choose the file', self.dbase.imagedirectory,
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

    """

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

        idphoto = self.currentFeature.id()

        sql = "UPDATE Photo SET id_objet = " + str(idobjet) + ",id_ressource = " + str(idres) + ",typephoto = 'PHO', content_type='JPG', list_photo=5, list_document=0  "
        sql += " WHERE id_photo = " + str(idphoto) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()

        if self.parentWidget is not None and self.parentWidget.currentFeature is not None:
            currentparentlinkfield = self.parentWidget.currentFeature['id_objet']
            sql = "INSERT INTO Tcobjetressource(id_tcobjet, id_tcressource) VALUES(" + str(currentparentlinkfield) + ", " + str(idres) + ");"
            query = self.dbase.query(sql)
            self.dbase.commit()






    def postSaveFeature(self, boolnewfeature):

        sql = "SELECT file FROM Ressource  WHERE id_ressource = " + str(self.currentFeature['id_ressource']) + ";"
        query = self.dbase.query(sql)
        result = [row[0] for row in query]
        # print('post',result)
        file = result[0]
        print(file)

        if file is not None and file != '':
            #self.showImageinLabelWidget(self.photowdg, self.userwdg.lineEdit_file.text())
            path_photo = self.dbase.completePathOfFile(file)
            print(path_photo)
            print(self.currentFeature.id())
            try:
                with open(path_photo, 'rb') as f:
                    ablob = f.read()
                    sql = '''UPDATE Photo SET file = ?  WHERE id_photo = ?;'''
                    args = [sqlite3.Binary(ablob),self.currentFeature.id() ]
                    query = self.dbase.query(sql, args)


            except Exception as e :
                print('error', e)



    """


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
            point.setX((size.width() - scaledPix.width())/2)
            point.setY((size.height() - scaledPix.height())/2)
            painter.drawPixmap(point, scaledPix)


    def setPixmap(self, img):
        self.pixmap = QtGui.QPixmap(img)
        self.repaint()

    def clear(self):
        self.pixmap = QtGui.QPixmap()
        self.repaint()

"""