# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore

try:
    from qgis.PyQt.QtGui import (QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget)
from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from .lamiadigue_croquis_tool  import CroquisTool
from .lamiadigue_graphique_tool  import GraphiqueTool
import os
import datetime




class ProfilTool(AbstractInspectionDigueTool):

    LOADFIRST = False
    dbasetablename = 'Profil'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(ProfilTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)
        
    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Description'
        self.NAME = 'Profil'
        self.dbasetablename = 'Profil'
        self.visualmode = [1, 2]
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

    def initFieldUI(self):
        # ****************************************************************************************
        #   userui Field
        if self.userwdgfield is None:
            # ****************************************************************************************
            # userui

            self.userwdgfield = UserUI()
            self.linkuserwdgfield = {'Profil' : {'linkfield' : 'id_profil',
                                             'widgets' : {'date': self.userwdgfield.dateEdit,
                                                          'type': self.userwdgfield.comboBox_type}},
                                'Objet' : {'linkfield' : 'id_objet',
                                          'widgets' : {}},
                                'Descriptionsystem' : {'linkfield' : 'id_descriptionsystem',
                                          'widgets' : {}}}

            self.userwdgfield.comboBox_type.currentIndexChanged.connect(self.changeType)


            # ****************************************************************************************
            # parent widgets
            if self.parentWidget is not None and 'lk_profil' in self.dbase.dbasetables[self.parentWidget.dbasetablename]['fields'].keys():
                self.userwdgfield.pushButton_setasdefault.clicked.connect(self.setAsDefault)
            else:
                self.userwdgfield.pushButton_setasdefault.setParent(None)

            # ****************************************************************************************
            # child widgets
            self.dbasechildwdgfield = []

            if True:
                self.propertieswdgCROQUIS = CroquisTool(dbase=self.dbase, parentwidget=self)
                self.propertieswdgCROQUIS.NAME = None
                #self.userwdgfield.tabWidget.widget(0).layout().addWidget(self.propertieswdgCROQUIS)
                self.userwdgfield.frame_cr.layout().addWidget(self.propertieswdgCROQUIS)
                self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)



            if True:
                self.propertieswdgGRAPH = GraphiqueTool(dbase=self.dbase, parentwidget=self)
                self.propertieswdgGRAPH.NAME = None
                #self.userwdgfield.tabWidget.widget(0).layout().addWidget(self.propertieswdgCROQUIS)
                self.userwdgfield.frame_graph.layout().addWidget(self.propertieswdgGRAPH)
                self.dbasechildwdgfield.append(self.propertieswdgGRAPH)



    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass

    def setAsDefault(self):
        if self.parentWidget.currentFeature is not None:
            if self.userwdgfield.stackedWidget.currentIndex() == 0:
                currentwdg = self.propertieswdgCROQUIS
            elif self.userwdgfield.stackedWidget.currentIndex() == 1:
                currentwdg = self.propertieswdgGRAPH

            if currentwdg.currentFeature is not None:
                idressource = currentwdg.currentFeature['id_ressource']
                idparentfeature=self.parentWidget.currentFeature['id_objet']
                # print('setDefaultPhoto',idphoto,idparentfeature)
                sql = "UPDATE " + str(self.parentWidget.dbasetablename) + " SET  lk_profil = " + str(idressource) + " WHERE id_objet = " + str(idparentfeature) + ";"
                query = self.dbase.query(sql)
                self.dbase.commit()

    def changeType(self,comboint):
        if 'Croquis' in self.userwdgfield.comboBox_type.currentText():
            self.userwdgfield.stackedWidget.setCurrentIndex(0)
        elif 'Graphique' in self.userwdgfield.comboBox_type.currentText():
            self.userwdgfield.stackedWidget.setCurrentIndex(1)

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
