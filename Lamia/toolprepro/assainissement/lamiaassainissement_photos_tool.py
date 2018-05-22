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
from ..abstract.lamia_photoviewer import PhotoViewer

#FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), '..', 'dialog', 'InspectionDigue_propertieswidget.ui'))

prefixhoto = ''
numphoto = 0

class PhotosTool(AbstractPhotosTool):

    LOADFIRST = False
    dbasetablename = 'Photo'




    def __init__(self, dbase, dialog=None, linkedtreewidget=None,gpsutil=None, parentwidget=None, parent=None):
        super(PhotosTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)



    def initFieldUI(self):
        if self.userwdgfield is None:
            self.userwdgfield = UserUI()
            self.linkuserwdgfield = {'Photo' : {'linkfield' : 'id_photo',
                                             'widgets' : {'numphoto': self.userwdgfield.spinBox_numphoto}},
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

            self.userwdgfield.toolButton_photoplus.clicked.connect(self.changeNumPhoto)
            self.userwdgfield.toolButton_photomoins.clicked.connect(self.changeNumPhoto)

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

        global prefixhoto
        global numphoto

        if self.sender() == self.userwdgfield.toolButton_photoplus:
            numphoto += 1


        elif self.sender() == self.userwdgfield.toolButton_photomoins:
            numphoto = numphoto -1

        self.userwdgfield.spinBox_numphoto.setValue(numphoto)




    def postInitFeatureProperties(self, feat):

        global prefixhoto
        global numphoto

        if self.currentFeature is None:
            datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
            self.initFeatureProperties(feat, 'Ressource', 'dateressource', datecreation)

            self.userwdgfield.spinBox_numphoto.setValue(numphoto)

        """
        if self.parentWidget is not None and self.parentWidget.currentFeature is not None:
            if self.parentWidget.dbasetablename == 'TRONCON':
                self.initFeatureProperties(feat, 'LkObjet', self.parentWidget.currentFeature.id())
            elif self.parentWidget.dbasetablename == 'OBSERVATION':
                self.initFeatureProperties(feat, 'LkObjet', self.parentWidget.currentFeature.id())
        """

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

            #geom if parent is node
            if self.parentWidget is not None and self.parentWidget.currentFeature is not None:
                if self.parentWidget.dbasetablename == 'Noeud':
                    # get geom
                    noeudfet = self.dbase.getLayerFeatureById('Noeud', self.parentWidget.currentFeature.id())
                    neudfetgeom = noeudfet.geometry().asPoint()
                    self.createorresetRubberband(1)
                    self.setTempGeometry([neudfetgeom],False)


        else:
            self.photowdg.clear()




    def postSaveFeature(self, boolnewfeature):
        global prefixhoto
        global numphoto

        if numphoto == self.userwdgfield.spinBox_numphoto.value():
            numphoto += 1
        else:
            numphoto = self.userwdgfield.spinBox_numphoto.value() + 1




class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiaassainissement_photo_tool_ui.ui')
        uic.loadUi(uipath, self)