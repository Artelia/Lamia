# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore

try:
    from qgis.PyQt.QtGui import (QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget)
from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
import os
import datetime

from .lamia_pointtopo_tool import AbstractPointtopoTool

"""
ne permettre de la renseigner qu en etant une classe fille de leve topo - sinon pas de datecreation
ca fout la merde....

"""


class AbstractTopographieTool(AbstractInspectionDigueTool):


    def __init__(self, dbase, dialog=None, linkedtreewidget=None,gpsutil=None, parentwidget=None, parent=None):
        super(AbstractTopographieTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil,parentwidget, parent=parent)

    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Ressources'
        self.NAME = 'Leves topographiques'
        self.dbasetablename = 'Topographie'
        # self.visualmode = [0, 1, 2]
        # self.PointENABLED = True
        # self.LineENABLED = True
        # self.PolygonEnabled = True
        # self.magicfunctionENABLED = True
        self.linkagespec = {'Tcobjetressource' : {'tabletc' : 'Tcobjetressource',
                                           'idsource' : 'id_ressource',
                                       'idtcsource' : 'id_tcressource',
                                           'iddest' : 'id_objet',
                                       'idtcdest' : 'id_tcobjet',
                                           'desttable' : ['Infralineaire']},
                            'Marche': {'tabletc': None,
                                           'idsource': 'lk_marche',
                                           'idtcsource': None,
                                           'iddest': 'id_marche',
                                           'idtcdest': None,
                                           'desttable': ['Marche']}}
        # self.pickTable = None


        # ****************************************************************************************
        #properties ui

    def initFieldUI(self):
        # ****************************************************************************************
        #   userui Field
        if self.userwdgfield is None:

            # ****************************************************************************************
            # userui
            self.userwdgfield = UserUI()
            self.linkuserwdgfield = {'Topographie' : {'linkfield' : 'id_topographie',
                                             'widgets' : {}},
                                'Objet' : {'linkfield' : 'id_objet',
                                          'widgets' : {}},
                                'Ressource' : {'linkfield' : 'id_ressource',
                                          'widgets' : {'file': self.userwdgfield.lineEdit_file,
                                                        'description': self.userwdgfield.lineEdit_nom,
                                                        'dateressource': self.userwdgfield.dateEdit_date}}}
            self.userwdgfield.pushButton_chooseph.clicked.connect(self.choosePhoto)
            self.userwdgfield.pushButton_open.clicked.connect(self.openFile)
            self.userwdgfield.pushButton_ajoutpointGPS.clicked.connect(self.ajoutPointGPS)
            self.userwdgfield.pushButton_importer.clicked.connect(self.importer)

            typpointlist = [elem[0] for elem in self.dbase.dbasetables['Pointtopo']['fields']['typepointtopo']['Cst']]
            self.userwdgfield.comboBox_typepoints.addItems(typpointlist)


            self.gpswidget = {'x' : {'widget' : self.userwdgfield.label_X,
                                     'gga' : 'Xcrs'},
                              'y': {'widget': self.userwdgfield.label_Y,
                                    'gga': 'Ycrs'},
                              'zmngf': {'widget': self.userwdgfield.label_Z,
                                    'gga': 'zmNGF'},
                              'dx': {'widget': self.userwdgfield.label_dX,
                                    'gst': 'xprecision'},
                              'dy': {'widget': self.userwdgfield.label_dY,
                                    'gst': 'yprecision'},
                              'dz': {'widget': self.userwdgfield.label_dZ,
                                    'gst': 'zprecision'},
                              'zgps': {'widget': self.userwdgfield.label_zgps,
                                     'gga': 'elevation'},
                              'zwgs84': {'widget': self.userwdgfield.label_zwgs84,
                                       'gga': 'deltageoid'},
                              'raf09': {'widget': self.userwdgfield.label_raf09,
                                       'gga': 'RAF09'},
                              'hauteurperche': {'widget': self.userwdgfield.label_hautperche,
                                        'gga': 'hauteurperche'}
                              }


            # ****************************************************************************************
            # child widgets
            self.dbasechildwdgfield = []
            self.propertieswdgPOINTTOPO= AbstractPointtopoTool(dbase=self.dbase,gpsutil=self.gpsutil, parentwidget=self)
            self.dbasechildwdgfield.append(self.propertieswdgPOINTTOPO)


    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass

    def openFile(self):
        filepath = self.completePathOfFile(self.userwdg.lineEdit_file.text())
        if filepath != '':
            os.startfile(filepath)

    def ajoutPointGPS(self):
        #self.propertieswdgPOINTTOPO.magicFunction()
        self.propertieswdgPOINTTOPO.featureSelected()
        #self.propertieswdgPOINTTOPO.userwdg.comboBox_position.setCurrentIndex(self.userwdg.comboBox_position.findText('Crete'))
        self.propertieswdgPOINTTOPO.userwdg.comboBox_position.setCurrentIndex(self.userwdg.comboBox_typepoints.currentIndex())
        success = self.propertieswdgPOINTTOPO.getGPSValues()
        if success:
            self.propertieswdgPOINTTOPO.saveFeature()

    def importer(self):
        pass

    def choosePhoto(self):
        file, extension = self.qfiledlg.getOpenFileNameAndFilter(None, 'Choose the file', self.dbase.imagedirectory,
                                                                 'All (*.*)', '')
        if file:
            self.userwdg.lineEdit_file.setText(os.path.normpath(file))


    def postInitFeatureProperties(self, feat):
        if self.currentFeature is None:
            datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
            self.initFeatureProperties(feat, 'Ressource', 'dateressource', datecreation)



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

        idrapport = self.currentFeature.id()

        sql = "UPDATE Topographie SET id_objet = " + str(idobjet) + ",id_ressource = " + str(idres) + " WHERE id_topographie = " + str( idrapport) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()

        if self.parentWidget is not None and self.parentWidget.currentFeature is not None:
            if self.parentWidget.dbasetablename == 'Marche':
                # print(self.parentWidget.currentFeature.attributes())
                currentparentlinkfield = self.parentWidget.currentFeature['id_marche']
                sql = "UPDATE Ressource SET lk_marche = " + str(currentparentlinkfield) + " WHERE id_ressource = " + str(idres) + ";"
                query = self.dbase.query(sql)
                self.dbase.commit()


    def postSaveFeature(self, boolnewfeature):
        pass



class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamia_topographie_tool_ui.ui')
        uic.loadUi(uipath, self)
