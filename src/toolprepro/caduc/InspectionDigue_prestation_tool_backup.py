# -*- coding: utf-8 -*-

import datetime
import os

from qgis.PyQt import uic, QtCore, QtGui

from InspectionDigueV2.src.toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from .InspectionDigue_desordre_tool import DesordreTool
from .InspectionDigue_topographie_tool import TopographieTool

FORM_CLASS, _ = uic.loadUiType(
    os.path.join(os.path.dirname(__file__), '..', 'dialog', 'InspectionDigue_propertieswidget.ui'))
FORM_CLASS2, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'PrestationToolUser.ui'))

class PrestationTool(AbstractInspectionDigueTool, FORM_CLASS):
    def __init__(self, dbase, dialog=None, linkedtreewidget=None, parentwidget=None, parent=None):
        super(PrestationTool, self).__init__(dbase, dialog, linkedtreewidget, parentwidget, parent=parent)

    def initTool(self):
        self.setupUi(self)
        self.CAT = 'Prestation'
        self.NAME = 'Prestation'
        self.dbasetablename = 'PRESTATION'




        self.userwdg = UserUI()
        self.linkuserwdg = {'Nom': self.userwdg.lineEdit_nom,'Date' : self.userwdg.dateEdit_date}

        self.propertieswdgDESORDRE = DesordreTool(dbase=self.dbase, parentwidget=self)
        self.propertieswdgTOPO= TopographieTool(dbase=self.dbase, parentwidget=self)
        self.dbasechildwdg = [self.propertieswdgDESORDRE,self.propertieswdgTOPO ]



    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass

    def loadIds(self):
        ids = []
        if self.parentWidget is None:
            sql = "SELECT ID FROM " + self.dbasetablename
            query = self.dbase.query(sql)
            ids = [row[0:1] for row in query]
            """
            while query.next:
                ids.append(query[0])
            """
        else:
            pass
        return ids

    def postInitFeatureProperties(self, feat):
        pass

    def postSaveFeature(self, boolnewfeature):
        if boolnewfeature:
            datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
            print(datecreation)
            sql = "INSERT INTO OBJET (DateCreation) VALUES('" + datecreation + "');"
            query = self.dbase.query(sql)
            self.dbase.commit()
            if False:
                sql = 'SELECT last_insert_rowid()'
                query = self.dbase.query(sql)
                idobjet = [row[0] for row in query][0]
            idobjet = self.dbase.getLastRowId('OBJET')

            idprestation = self.currentFeature.id()

            #sql = "UPDATE TOPOGRAPHIE SET IdObjet = " + str(idobjet) + " WHERE id = " + str(idtopo) + ";"
            sql = "UPDATE PRESTATION SET IdObjet = " + str(idobjet)  + " WHERE id = " + str(idprestation) + ";"
            query = self.dbase.query(sql)
            self.dbase.commit()


class UserUI(QtGui.QWidget, FORM_CLASS2):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        self.setupUi(self)
