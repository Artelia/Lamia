# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore

try:
    from qgis.PyQt.QtGui import (QWidget, QPushButton)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget, QPushButton)
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..abstract.lamia_noeud_tool import AbstractNoeudTool

import os
import datetime




class NoeudTool(AbstractNoeudTool):

    LOADFIRST = False
    dbasetablename = 'Noeud'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(NoeudTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)

"""
    def initTool(self):
        # ****************************************************************************************
        # Main spec

        self.CAT = 'Description'
        self.NAME = 'Noeud'
        self.dbasetablename = 'Noeud'
        self.visualmode = [1, 2]
        self.PointENABLED = True
        # self.LineENABLED = False
        # self.PolygonENABLED = True
        # self.magicfunctionENABLED = True
        # self.linkagespec = None
        # self.pickTable = None



        # ****************************************************************************************
        #properties ui
        pass

    def initDesktopUI(self):
        # ****************************************************************************************
        # userui Desktop
        if self.userwdgdesktop is None:

            # ****************************************************************************************
            # userui
            self.userwdgdesktop = UserUI()
            self.linkuserwdgdesktop = {'Noeud' : {'linkfield' : 'id_noeud',
                                             'widgets' : {}},
                                'Objet' : {'linkfield' : 'id_objet',
                                          'widgets' : {}},
                                'Descriptionsystem' : {'linkfield' : 'id_descriptionsystem',
                                          'widgets' : {}}}



            # ****************************************************************************************
            # child widgets

    pass



    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass



    def postInitFeatureProperties(self, feat):
        pass

    def createParentFeature(self):
        datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
        # print(datecreation)
        sql = "INSERT INTO Objet (datecreation) VALUES('" + datecreation + "');"
        query = self.dbase.query(sql)
        self.dbase.commit()
        idobjet = self.dbase.getLastRowId('Objet')

        sql = "INSERT INTO Descriptionsystem (id_objet) VALUES(" + str(idobjet) + ");"
        query = self.dbase.query(sql)
        self.dbase.commit()
        idsys = self.dbase.getLastRowId('Descriptionsystem')

        idnoeud = self.currentFeature.id()

        sql = "UPDATE Noeud SET id_objet = " + str(idobjet) + ",id_descriptionsystem = " + str(idsys) + " WHERE id_noeud = " + str(idnoeud) + ";"
        # print(sql)
        query = self.dbase.query(sql)
        self.dbase.commit()




    def postSaveFeature(self, boolnewfeature):
        pass


    def postDeleteFeature(self):
        pass


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'NoeudToolUser.ui')
        uic.loadUi(uipath, self)


"""