# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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



class BaseEaupotablePhotoTool(BasePhotoTool):
    LOADFIRST = False
    dbasetablename = 'Photo'


    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None, parentwidget=None, parent=None):
        super(BaseEaupotablePhotoTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil, parentwidget,
                                                          parent=parent)

    def initFieldUI(self):
        if self.userwdgfield is None:
            self.userwdgfield = UserUI()
            self.linkuserwdgfield = {'Photo' : {'linkfield' : 'id_photo',
                                             'widgets' : {'numphoto': self.userwdgfield.spinBox_numphoto}},
                                'Objet' : {'linkfield' : 'id_objet',
                                          'widgets' : {}},
                                'Ressource' : {'linkfield' : 'id_ressource',
                                          'widgets' : {'file': self.userwdgfield.lineEdit_file,
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



            # ****************************************************************************************
            # child widgets
            pass
            if False:
                if self.parentWidget is not None and self.parentWidget.dbasetablename in ['']:
                    self.userwdgfield.pushButton_defaultphoto.clicked.connect(self.setDefaultPhoto)
                else:
                    self.userwdgfield.pushButton_defaultphoto.setParent(None)

            if True:
                self.userwdgfield.pushButton_vueensemble.clicked.connect(self.setDefaultPhoto)
                self.userwdgfield.pushButton_cuve.clicked.connect(self.setDefaultPhoto)
                self.userwdgfield.pushButton_poires.clicked.connect(self.setDefaultPhoto)
                self.userwdgfield.pushButton_vanne.clicked.connect(self.setDefaultPhoto)
                self.userwdgfield.pushButton_armoire.clicked.connect(self.setDefaultPhoto)



    def changeNumPhoto(self):

        global numphoto

        if numphoto is None:
            numphoto = 0

        if self.sender() == self.userwdgfield.toolButton_photoplus:
            numphoto += 1
        elif self.sender() == self.userwdgfield.toolButton_photomoins:
            numphoto = numphoto -1
        self.userwdgfield.spinBox_numphoto.setValue(numphoto)




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





    def postInitFeatureProperties(self, feat):

        global numphoto

        if self.currentFeature is None:
            #datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
            datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            self.initFeatureProperties(feat, 'Ressource', 'datetimeressource', datecreation)


            if numphoto is not None:
                self.userwdgfield.spinBox_numphoto.setValue(numphoto)
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


        if self.parentWidget is not None and self.parentWidget.currentFeature is not None:
            if self.parentWidget.dbasetablename == 'Noeud':
                pass
                if False:
                    if self.parentWidget.currentFeature['typeOuvrageAss'] == '10':
                        self.userwdgfield.stackedWidget_2.setCurrentIndex(1)
                    else:
                        self.userwdgfield.stackedWidget_2.setCurrentIndex(2)


    def postSaveFeature(self, boolnewfeature):

        global numphoto

        if self.userwdgfield.spinBox_numphoto.value() == -1 :
            numphoto = None
        elif numphoto == self.userwdgfield.spinBox_numphoto.value():
            numphoto += 1
        else:
            numphoto = self.userwdgfield.spinBox_numphoto.value() + 1



class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabaseeaupotable_photo_tool_ui.ui')
        uic.loadUi(uipath, self)