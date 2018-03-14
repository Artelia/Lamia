# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore

try:
    from qgis.PyQt.QtGui import (QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget)
from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
import os
import datetime





class RessourceTool(AbstractInspectionDigueTool):
    
    def __init__(self, dbase, dialog=None, linkedtreewidget=None,gpsutil=None, parentwidget=None, parent=None):
        super(RessourceTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil,parentwidget, parent=parent)

    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Ressources'
        self.NAME = 'Ressources'
        self.dbasetablename = 'Ressource'
        #self.visualmode = [2]
        # self.PointENABLED = True
        # self.LineENABLED = True
        #self.PolygonENABLED = True
        # self.magicfunctionENABLED = True
        self.linkagespec = {'Prestation': {'tabletc': None,
                                           'idsource': 'lk_prestation',
                                           'idtcsource': None,
                                           'iddest': 'id_prestation',
                                           'idtcdest': None,
                                           'desttable': ['Prestation']}}

        # ****************************************************************************************
        #properties ui

    def initDesktopUI(self):
        # ****************************************************************************************
        # userui Desktop
        if self.userwdgdesktop is None:
            # ****************************************************************************************
            # userui
            self.userwdgdesktop = UserUI()

            self.linkuserwdgdesktop = { 'Objet' : {'linkfield' : 'id_objet',
                                          'widgets' : {}},
                                'Ressource' : {'linkfield' : 'id_ressource',
                                          'widgets' : {}}}

        # ****************************************************************************************
        # child widgets



    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass



    def postInitFeatureProperties(self, feat):
        pass



    def createParentFeature(self):
        pass
        if False:
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

            sql = "UPDATE Rapport SET id_objet = " + str(idobjet) + ",id_ressource = " + str(idres) + " WHERE id_rapport = " + str( idrapport) + ";"
            query = self.dbase.query(sql)
            self.dbase.commit()

            if False:
                idslink = []
                for table in self.linkagespec['ObjetRessource']:
                    sql = "SELECT " + table + ".id_objet FROM " + table + "," + self.dbasetablename + "WHERE ST_Within(" + table + ".geom," +self.dbasetablename + ".geom);"
                    query = self.dbase.query(sql)
                    idstemp = [row[0] for row in query]
                    idslink += idstemp
                for id in idslink:
                    sql = "INSERT INTO " + self.linkagespec['tabletc']


            self.initLinkageFromGeometry('ObjetRessource',idres)


        if False:
            if self.parentWidget is not None and self.parentWidget.currentFeature is not None:
                if self.parentWidget.dbasetablename == 'Prestation':
                    # print(self.parentWidget.currentFeature.attributes())
                    currentparentlinkfield = self.parentWidget.currentFeature['ID']
                    sql = "UPDATE Rapport SET LkPrestation = " + str(currentparentlinkfield) + " WHERE id_rapport = " + str(
                        idrapport) + ";"
                    query = self.dbase.query(sql)
                    self.dbase.commit()





    def postSaveFeature(self, boolnewfeature):
        pass



class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'RessourcesToolUser.ui')
        uic.loadUi(uipath, self)