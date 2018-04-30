# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore

try:
    from qgis.PyQt.QtGui import (QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget)
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..abstract.lamia_observation_tool import AbstractObservationTool
from .lamiavnf_photos_tool import PhotosTool
#from .lamiavnf_croquis_tool import CroquisTool
import os
import datetime


class ObservationTool(AbstractObservationTool):

    LOADFIRST = False
    dbasetablename = 'Observation'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None,gpsutil=None, parentwidget=None, parent=None):
        super(ObservationTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)



    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Desordre'
        self.NAME = 'Observation'
        self.dbasetablename = 'Observation'
        self.visualmode = [1, 2]
        # self.PointENABLED = True
        # self.LineENABLED = True
        # self.PolygonENABLED = True
        # self.magicfunctionENABLED = True
        self.linkagespec = {'Desordre' : {'tabletc' : None,
                                           'idsource' : 'lk_desordre',
                                       'idtcsource' : None,
                                           'iddest' : 'id_desordre',
                                       'idtcdest' : None,
                                           'desttable' : ['Desordre']} }

        # ****************************************************************************************
        #properties ui
        pass



    def initFieldUI(self):
        # ****************************************************************************************
        # userui Desktop
        if self.userwdgfield is None:
            # ****************************************************************************************
            # userui
            self.userwdgfield = UserUI()
            self.linkuserwdgfield = {'Observation' : {'linkfield' : 'id_observation',
                                             'widgets' : {'dateobservation' : self.userwdgfield.dateEdit,
                                                          'magnitude' : self.userwdgfield.comboBox_ampleur,
                                                          'state_level' : self.userwdgfield.comboBox_gravite,
                                                        'description': self.userwdgfield.textEdit_description,
                                                        'travaux': self.userwdgfield.comboBox_travaux}},
                                'Objet' : {'linkfield' : 'id_objet',
                                          'widgets' : {}}}

            # ****************************************************************************************
            # child widgets
            self.dbasechildwdgfield=[]
            self.propertieswdgPHOTOGRAPHIE = PhotosTool(dbase=self.dbase, parentwidget=self)
            self.dbasechildwdgfield = [self.propertieswdgPHOTOGRAPHIE]
            #self.propertieswdgCROQUIS = CroquisTool(dbase=self.dbase, parentwidget=self)
            #self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

    """

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

    """
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
        """

    def postSaveFeature(self, boolnewfeature):
        pass

    """
class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiavnf_observation_tool_ui.ui')
        uic.loadUi(uipath, self)

