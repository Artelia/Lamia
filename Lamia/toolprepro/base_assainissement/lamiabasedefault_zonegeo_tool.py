# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore

try:
    from qgis.PyQt.QtGui import (QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget)
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..base.lamiabase_zonegeo_tool import BaseZonegeoTool
import os
import datetime



class BaseDefaultZonegeoTool(BaseZonegeoTool):

    LOADFIRST = False
    dbasetablename = 'Zonegeo'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(BaseDefaultZonegeoTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil,parentwidget, parent=parent)

    """
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
        self.iconpath = os.path.join(os.path.dirname(__file__), 'lamiadefault_zonegeo_tool_icon.svg')
        self.qtreewidgetfields = ['nom']
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

        lastrevision = self.dbase.getLastPk('Revision')
        datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
        lastobjetid = self.dbase.getLastId('Objet') + 1
        sql = "INSERT INTO Objet (id_objet, id_revisionbegin, datecreation ) "
        sql += "VALUES(" + str(lastobjetid ) + "," + str(lastrevision) +  ",'" + datecreation + "');"
        query = self.dbase.query(sql)
        self.dbase.commit()

        pkzonegeo = self.currentFeature.id()
        lastidzonegeo = self.dbase.getLastId('Zonegeo') + 1

        sql = "UPDATE Zonegeo SET id_objet = " + str(lastobjetid)  + ","
        sql += "id_zonegeo = " + str(lastidzonegeo) + ","
        sql += "id_revisionbegin = " + str(lastrevision)
        sql += " WHERE pk_zonegeo = " + str(pkzonegeo) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()


        #self.initLinkageFromGeometry('Tcobjetzonegeo', pkzonegeo)

    def postSaveFeature(self, boolnewfeature):
        pass

    """
"""

class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiadefault_zonegeo_tool_ui.ui')
        uic.loadUi(uipath, self)
"""