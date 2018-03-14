# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore

try:
    from qgis.PyQt.QtGui import (QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget)
from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool

from .lamiadigue_rapport_tool import RapportTool
from .lamiadigue_photos_tool import PhotosTool
from .lamiadigue_topographie_tool import TopographieTool
from .lamiadigue_ressource_tool import RessourceTool



import os
import datetime



class MarcheTool(AbstractInspectionDigueTool):

    LOADFIRST = False
    dbasetablename = 'Marche'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(MarcheTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)

    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Gestion'
        self.NAME = 'Marche'
        self.dbasetablename = 'Marche'
        # self.visualmode = [0, 1, 2]
        # self.PointENABLED = True
        # self.LineENABLED = True
        # self.PolygonENABLED = True
        # self.magicfunctionENABLED = True
        self.linkagespec = {'Tcobjetintervenant' : {'tabletc' : 'Tcobjetintervenant',
                                              'idsource' : 'id_objet',
                                            'idtcsource' : 'id_tcobjet',
                                           'iddest' : 'id_intervenant',
                                           'idtcdest' : 'id_tcintervenant',
                                           'desttable' : ['Intervenant']}
                                            }
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
            self.linkuserwdgfield = {'Marche' : {'linkfield' : 'id_marche',
                                             'widgets' : {'nom': self.userwdgfield.lineEdit_nom,
                                                          'datemarche' : self.userwdgfield.dateEdit_date}},
                                'Objet' : {'linkfield' : 'id_objet',
                                          'widgets' : {}}}
            self.userwdgfield.pushButton_currentPrestation.clicked.connect(self.defineCurrentPrestation)
            self.userwdgfield.pushButton_defineinter.clicked.connect(self.manageLinkage)

            # ****************************************************************************************
            # child widgets
            self.dbasechildwdgfield = []
            self.propertieswdgRAPPORT = RapportTool(dbase=self.dbase, parentwidget=self)
            self.dbasechildwdgfield.append(self.propertieswdgRAPPORT)

            if False:
                self.propertieswdgRessource= RessourceTool(dbase=self.dbase, parentwidget=self)
                self.dbasechildwdgfield.append(self.propertieswdgRessource)

            self.propertieswdgPHOTO = PhotosTool(dbase=self.dbase, parentwidget=self)
            self.dbasechildwdgfield.append(self.propertieswdgPHOTO)
            self.propertieswdgTOPOGRAPHIE = TopographieTool(dbase=self.dbase, parentwidget=self)
            self.dbasechildwdgfield.append(self.propertieswdgTOPOGRAPHIE)



    def defineCurrentPrestation(self):
        self.windowdialog.currentprestationlabel.setText('Prestation : ' + str(self.currentFeature.id()) + " - " +str(self.currentFeature['Nom'] ))
        self.dbase.currentprestationid = self.currentFeature.id()

    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass


    def postInitFeatureProperties(self, feat):
        if self.currentFeature is None:
            datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
            self.initFeatureProperties(feat, self.dbasetablename, 'datemarche', datecreation)
        else:
            sql = "SELECT Tcobjetintervenant.fonction, Intervenant.nom,Intervenant.societe  FROM Tcobjetintervenant "
            sql += " INNER JOIN Intervenant ON Tcobjetintervenant.id_tcintervenant = Intervenant.id_intervenant "
            sql += "WHERE id_tcobjet = " + str(self.currentFeature['id_objet'])
            query = self.dbase.query(sql)
            result = "\n".join([str(row) for row in query])
            self.userwdg.textBrowser_intervenants.clear()
            self.userwdg.textBrowser_intervenants.append(result)

    def createParentFeature(self):
        datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
        sql = "INSERT INTO Objet (datecreation) VALUES('" + datecreation + "');"
        query = self.dbase.query(sql)
        self.dbase.commit()
        idobjet = self.dbase.getLastRowId('Objet')

        idprestation = self.currentFeature.id()

        sql = "UPDATE Marche SET id_objet = " + str(idobjet) + " WHERE id_marche= " + str(idprestation) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()



    def postSaveFeature(self, boolnewfeature):
        pass


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'MarcheToolUser.ui')
        uic.loadUi(uipath, self)