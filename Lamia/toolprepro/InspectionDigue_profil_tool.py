# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore

try:
    from qgis.PyQt.QtGui import (QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget)
from ..toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from .InspectionDigue_croquis_tool  import CroquisTool
from .InspectionDigue_graphique_tool  import GraphiqueTool
import os
import datetime




class ProfilTool(AbstractInspectionDigueTool):

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(ProfilTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)
        
    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Description'
        self.NAME = 'Profil'
        self.dbasetablename = 'Profil'
        self.visualmode = [0, 1, 2]
        # self.PointEnabled = True
        self.LineENABLED = True
        # self.PolygonEnabled = True
        self.linkagespec = {'Infralineaire' : {'tabletc' : None,
                                              'idsource' : 'lk_objet',
                                            'idtcsource' : None,
                                           'iddest' : 'id_objet',
                                           'idtcdest' : None,
                                           'desttable' : ['Infralineaire']} }
        # self.pickTable = None
        # ****************************************************************************************
        #properties ui
        pass

        # ****************************************************************************************
        # userui

        self.userwdg = UserUI()
        self.linkuserwdg = {'Profil' : {'linkfield' : 'id_profil',
                                         'widgets' : {'date': self.userwdg.dateEdit,
                                                      'type': self.userwdg.comboBox_type}},
                            'Objet' : {'linkfield' : 'id_objet',
                                      'widgets' : {}},
                            'Descriptionsystem' : {'linkfield' : 'id_descriptionsystem',
                                      'widgets' : {}}}

        self.userwdg.comboBox_type.currentIndexChanged.connect(self.changeType)

        # ****************************************************************************************
        # child widgets
        if True:
            self.propertieswdgCROQUIS = CroquisTool(dbase=self.dbase, parentwidget=self)
            self.propertieswdgCROQUIS.NAME = None
            #self.userwdg.tabWidget.widget(0).layout().addWidget(self.propertieswdgCROQUIS)
            self.userwdg.frame_cr.layout().addWidget(self.propertieswdgCROQUIS)
            self.dbasechildwdg.append(self.propertieswdgCROQUIS)

        if True:
            self.propertieswdgGRAPH = GraphiqueTool(dbase=self.dbase, parentwidget=self)
            self.propertieswdgGRAPH.NAME = None
            #self.userwdg.tabWidget.widget(0).layout().addWidget(self.propertieswdgCROQUIS)
            self.userwdg.frame_graph.layout().addWidget(self.propertieswdgGRAPH)
            self.dbasechildwdg.append(self.propertieswdgGRAPH)


        if False:
            self.propertieswdgPROFILTRAVERSR = ProfilTraversRTool(dbase=self.dbase, parentwidget=self)
            self.propertieswdgPROFILTRAVERSR.NAME = None
            self.userwdg.tabWidget.widget(1).layout().addWidget(self.propertieswdgPROFILTRAVERSR)

            self.dbasechildwdg = [self.propertieswdgCROQUIS,self.propertieswdgPROFILTRAVERSR]

            self.idstoload = {'TRONCON' : ['LkTroncon','ID' ]}

    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass

    def changeType(self,comboint):
        if 'Croquis' in self.userwdg.comboBox_type.currentText():
            self.userwdg.stackedWidget.setCurrentIndex(0)
        elif 'Graphique' in self.userwdg.comboBox_type.currentText():
            self.userwdg.stackedWidget.setCurrentIndex(1)

    def postInitFeatureProperties(self, feat):
        if self.currentFeature is None:
            datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
            self.initFeatureProperties(feat, 'Date', datecreation)

            if self.parentWidget is not None:
                if self.parentWidget.dbasetablename == 'TRONCON' and self.parentWidget.currentFeature is not None:
                    self.initFeatureProperties(self.currentFeature, 'LkTroncon', self.parentWidget.currentFeature.id())


    def createParentFeature(self):
        datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
        # print(datecreation)
        sql = "INSERT INTO Objet (datecreation) VALUES('" + datecreation + "');"
        query = self.dbase.query(sql)
        self.dbase.commit()
        idobjet = self.dbase.getLastRowId('OBJET')

        sql = "INSERT INTO Descriptionsystem (id_objet) VALUES(" + str(idobjet) + ");"
        query = self.dbase.query(sql)
        self.dbase.commit()
        idsys = self.dbase.getLastRowId('Descriptionsystem')

        idprofil = self.currentFeature.id()

        sql = "UPDATE Profil SET id_objet = " + str(idobjet) + ",id_descriptionsystem = " + str(idsys) + " WHERE id_profil = " + str(idprofil) + ";"
        # print(sql)
        query = self.dbase.query(sql)
        self.dbase.commit()

        if self.parentWidget is not None and self.parentWidget.currentFeature is not None:
            if self.parentWidget.dbasetablename == 'Infralineaire':
                # print(self.parentWidget.currentFeature.attributes())
                currentparentlinkfield = self.parentWidget.currentFeature['id_objet']
                sql = "UPDATE Profil SET lk_objet = " + str(currentparentlinkfield) + " WHERE id_profil = " + str(idprofil) + ";"
                query = self.dbase.query(sql)
                self.dbase.commit()


    def postSaveFeature(self, boolnewfeature):
        pass





class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'ProfilToolUser.ui')
        uic.loadUi(uipath, self)
