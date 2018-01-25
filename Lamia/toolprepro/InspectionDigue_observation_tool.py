# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore

try:
    from qgis.PyQt.QtGui import (QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget)
from ..toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from .InspectionDigue_photos_tool import PhotosTool
from .InspectionDigue_croquis_tool  import CroquisTool
import os
import datetime


class ObservationTool(AbstractInspectionDigueTool):

    def __init__(self, dbase, dialog=None, linkedtreewidget=None,gpsutil=None, parentwidget=None, parent=None):
        super(ObservationTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)
        
    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Desordre'
        self.NAME = 'Observation'
        self.dbasetablename = 'Observation'
        #self.visualmode = [1, 2]
        # self.PointENABLED = True
        # self.LineENABLED = True
        # self.PolygonENABLED = True
        # self.magicfunctionENABLED = True
        self.linkagespec = {'Desordre' : {'tabletc' : None,
                                           'idsource' : 'lk_desordre',
                                       'idtcsource' : None,
                                           'iddest' : 'id_desordre',
                                       'idtcdest' : None,
                                           'desttable' : ['Desordre']},
                            'Marche' :{'tabletc' : None,
                                              'idsource' : 'lk_marche',
                                            'idtcsource' : None,
                                           'iddest' : 'id_marche',
                                           'idtcdest' : None,
                                           'desttable' : ['Marche']} }

        # ****************************************************************************************
        #properties ui
        pass

        # ****************************************************************************************
        # userui
        self.userwdg = UserUI()
        self.linkuserwdg = {'Observation' : {'linkfield' : 'id_observation',
                                         'widgets' : {'dateobservation' : self.userwdg.dateEdit,
                                                      'nombre' : self.userwdg.spinBox_nombre,
                                                    'gravite': self.userwdg.comboBox_urgence,
                                                    'evolution': self.userwdg.textEdit_evolution,
                                                    'commentaires': self.userwdg.textEdit_comm,
                                                    'suite': self.userwdg.textEdit_suite}},
                            'Objet' : {'linkfield' : 'id_objet',
                                      'widgets' : {}}}

        # ****************************************************************************************
        # child widgets

        self.propertieswdgPHOTOGRAPHIE = PhotosTool(dbase=self.dbase, parentwidget=self)
        self.dbasechildwdg = [self.propertieswdgPHOTOGRAPHIE]
        self.propertieswdgCROQUIS = CroquisTool(dbase=self.dbase, parentwidget=self)
        self.dbasechildwdg.append(self.propertieswdgCROQUIS)


    def postOnActivation(self):
            pass

    def postOnDesactivation(self):
        pass

    def postloadIds(self,sqlin):
        if self.parentWidget is not None and self.parentWidget.dbasetablename == 'Desordre':
            sqlin += " ORDER BY dateobservation DESC"
        return sqlin


    def postInitFeatureProperties(self, feat):
        if self.currentFeature is None:
            datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
            self.initFeatureProperties(feat, self.dbasetablename, 'dateobservation', datecreation)


    def createParentFeature(self):
        datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
        sql = "INSERT INTO Objet (datecreation) VALUES('" + datecreation + "');"
        query = self.dbase.query(sql)
        self.dbase.commit()
        idobjet = self.dbase.getLastRowId('OBJET')

        idobservation = self.currentFeature.id()

        sql = "UPDATE Observation SET id_objet = " + str(idobjet) + " WHERE id_observation = " + str(idobservation) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()

        idobservation = self.currentFeature.id()

        if self.parentWidget is not None and self.parentWidget.currentFeature is not None:
            if self.parentWidget.dbasetablename == 'Desordre':
                currentparentlinkfield = self.parentWidget.currentFeature['id_desordre']
                sql = "UPDATE Observation SET lk_desordre = " + str(currentparentlinkfield) + " WHERE id_observation = " + str(idobservation) + ";"
                query = self.dbase.query(sql)
                self.dbase.commit()


    def postSaveFeature(self, boolnewfeature):
        pass


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'ObservationToolUser.ui')
        uic.loadUi(uipath, self)