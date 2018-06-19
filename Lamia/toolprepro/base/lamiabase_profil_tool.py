# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore

try:
    from qgis.PyQt.QtGui import (QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget)
from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from .lamiabase_photo_tool import BasePhotoTool
from .lamiabase_croquis_tool import BaseCroquisTool
from .lamiabase_graphique_tool import BaseGraphiqueTool

import os
import datetime




class BaseProfilTool(AbstractInspectionDigueTool):

    LOADFIRST = False
    dbasetablename = 'Profil'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(BaseProfilTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)
        
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
        # self.iconpath = os.path.join(os.path.dirname(__file__), 'lamiabase_photo_tool_icon.svg')
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
                self.propertieswdgGRAPH = BaseGraphiqueTool(dbase=self.dbase, parentwidget=self)
                self.propertieswdgGRAPH.NAME = None
                #self.userwdgfield.tabWidget.widget(0).layout().addWidget(self.propertieswdgCROQUIS)
                #self.userwdgfield.frame_graph.layout().addWidget(self.propertieswdgGRAPH)
                self.userwdgfield.stackedWidget.widget(0).layout().addWidget(self.propertieswdgGRAPH)
                self.dbasechildwdgfield.append(self.propertieswdgGRAPH)



            if True:
                self.propertieswdgCROQUIS = BaseCroquisTool(dbase=self.dbase, parentwidget=self)
                self.propertieswdgCROQUIS.NAME = None
                #self.userwdgfield.tabWidget.widget(0).layout().addWidget(self.propertieswdgCROQUIS)
                #self.userwdgfield.frame_cr.layout().addWidget(self.propertieswdgCROQUIS)
                self.userwdgfield.stackedWidget.widget(1).layout().addWidget(self.propertieswdgCROQUIS)
                self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

            if True:
                self.propertieswdgPHOTO = BasePhotoTool(dbase=self.dbase, parentwidget=self)
                self.propertieswdgPHOTO.NAME = None
                #self.userwdgfield.tabWidget.widget(0).layout().addWidget(self.propertieswdgCROQUIS)
                #self.userwdgfield.frame_cr.layout().addWidget(self.propertieswdgPHOTO)
                self.userwdgfield.stackedWidget.widget(2).layout().addWidget(self.propertieswdgPHOTO)
                self.dbasechildwdgfield.append(self.propertieswdgPHOTO)





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
        self.userwdgfield.stackedWidget.setCurrentIndex(comboint)


    def postInitFeatureProperties(self, feat):
        if self.currentFeature is None:
            datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
            self.initFeatureProperties(feat, 'Date', datecreation)

            if self.parentWidget is not None:
                if self.parentWidget.dbasetablename == 'Infralineaire' and self.parentWidget.currentFeature is not None:
                    self.initFeatureProperties(self.currentFeature, 'LkTroncon', self.parentWidget.currentFeature.id())


    def createParentFeature(self):

        lastrevision = self.dbase.maxrevision
        datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
        lastobjetid = self.dbase.getLastId('Objet') + 1
        sql = "INSERT INTO Objet (id_objet, id_revisionbegin, datecreation ) "
        sql += "VALUES(" + str(lastobjetid ) + "," + str(lastrevision) +  ",'" + datecreation + "');"
        query = self.dbase.query(sql)
        self.dbase.commit()
        #idobjet = self.dbase.getLastRowId('Objet')



        #sql = "INSERT INTO Descriptionsystem (id_objet) VALUES(" + str(idobjet) + ");"
        lastdescriptionsystemid = self.dbase.getLastId('Descriptionsystem') + 1
        sql = "INSERT INTO Descriptionsystem (id_descriptionsystem, id_revisionbegin, id_objet) "
        sql += "VALUES(" + str(lastdescriptionsystemid) + "," + str(lastrevision) +  "," + str(lastobjetid) + ");"
        query = self.dbase.query(sql)
        self.dbase.commit()
        #idsys = self.dbase.getLastRowId('Descriptionsystem')

        idprofil = self.currentFeature.id()
        lastidprofil = self.dbase.getLastId('Profil') + 1


        sql = "UPDATE Profil SET id_objet = " + str(lastobjetid)  + ","
        sql += "id_descriptionsystem = " + str(lastdescriptionsystemid)   + ","
        sql += "id_profil = " + str(lastidprofil)  + ","
        sql += "id_revisionbegin = " + str(lastrevision)
        sql += " WHERE pk_profil = " + str(idprofil) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()



        if self.parentWidget is not None and self.parentWidget.currentFeature is not None:
            if self.parentWidget.dbasetablename == 'Infralineaire':
                # print(self.parentWidget.currentFeature.attributes())
                currentparentlinkfield = self.parentWidget.currentFeature['id_objet']
                sql = "UPDATE Profil SET lk_objet = " + str(currentparentlinkfield) + " WHERE pk_profil = " + str(idprofil) + ";"
                query = self.dbase.query(sql)
                self.dbase.commit()





    def postSaveFeature(self, boolnewfeature):
        pass





class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabase_profil_tool_ui.ui')
        uic.loadUi(uipath, self)
