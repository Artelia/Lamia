# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore

try:
    from qgis.PyQt.QtGui import (QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget)
from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
import os
import datetime



class AbstractZonegeoTool(AbstractInspectionDigueTool):


    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(AbstractZonegeoTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil,parentwidget, parent=parent)

    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Gestion'
        self.NAME = 'Zone geographique'
        self.dbasetablename = 'Zonegeo'
        self.visualmode = [ 1, 2]
        # self.PointENABLED = True
        # self.LineENABLED = True
        self.PolygonENABLED = True
        # self.magicfunctionENABLED = True
        self.linkagespec = {'Tcobjetzonegeo' : {'tabletc' : 'Tcobjetzonegeo',
                                              'idsource' : 'id_zonegeo',
                                            'idtcsource' : 'id_tczonegeo',
                                           'iddest' : 'id_objet',
                                           'idtcdest' : 'id_tcobjet',
                                           'desttable' : ['Infralineaire']}}
        # self.pickTable = None

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
            self.linkuserwdgfield = {'Zonegeo' : {'linkfield' : 'id_zonegeo',
                                             'widgets' : {'nom' : self.userwdgfield.lineEdit_nom,
                                                          'type_zonegeo':self.userwdgfield.comboBox_type }},
                                'Objet' : {'linkfield' : 'id_objet',
                                          'widgets' : {}}}


    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass


    def postInitFeatureProperties(self, feat):
        pass

    def createParentFeature(self):
        datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
        print(datecreation)
        sql = "INSERT INTO Objet (datecreation) VALUES('" + datecreation + "');"
        query = self.dbase.query(sql)
        self.dbase.commit()

        idobjet = self.dbase.getLastRowId('Objet')

        idzonegeo = self.currentFeature.id()

        sql = "UPDATE Zonegeo SET id_objet = " + str(idobjet) + " WHERE id_zonegeo = " + str(idzonegeo) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()

        self.initLinkageFromGeometry('Tcobjetzonegeo', idzonegeo)

    def postSaveFeature(self, boolnewfeature):
        pass

class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamia_zonegeo_tool_ui.ui')
        uic.loadUi(uipath, self)