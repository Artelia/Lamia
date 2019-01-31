# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore

try:
    from qgis.PyQt.QtGui import (QWidget, QPushButton)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget, QPushButton)
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ...toolabstract.Lamia_abstract_tool import AbstractLamiaTool

import os
import datetime
from .lamiabase_photo_tool import BasePhotoTool
from .lamiabase_croquis_tool import BaseCroquisTool




class BaseNoeudTool(AbstractLamiaTool):

    LOADFIRST = True
    dbasetablename = 'Noeud'
    specialfieldui = []

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(BaseNoeudTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)
        
    def initTool(self):
        # ****************************************************************************************
        # Main spec

        self.CAT = 'Description'
        self.NAME = 'Noeud'
        self.dbasetablename = 'Noeud'
        self.visualmode = [0, 1, 2]
        self.PointENABLED = True
        # self.LineENABLED = False
        # self.PolygonENABLED = True
        # self.magicfunctionENABLED = True
        # self.linkagespec = None
        # self.pickTable = None
        self.iconpath = os.path.join(os.path.dirname(__file__), 'lamiabase_noeud_tool_icon.svg')
        self.qtreewidgetfields = ['lpk_revision_begin']

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
            self.linkuserwdgfield = {'Noeud' : {'linkfield' : 'id_noeud',
                                             'widgets' : {}},
                                'Objet' : {'linkfield' : 'id_objet',
                                          'widgets' : {'libelle': self.userwdgfield.lineEdit_libelle}},
                                'Descriptionsystem' : {'linkfield' : 'id_descriptionsystem',
                                          'widgets' : {}}}



            # ****************************************************************************************
            # child widgets

            self.dbasechildwdgfield = []

            if self.parentWidget is None:
                self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(dbase=self.dbase, gpsutil=self.gpsutil, parentwidget=self)
                self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)


                self.propertieswdgCROQUIS = BaseCroquisTool(dbase=self.dbase, parentwidget=self)
                self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)




    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass



    def postInitFeatureProperties(self, feat):
        pass

    def createParentFeature(self):
        pkobjet = self.dbase.createNewObjet()

        if False:
            # lastrevision = self.dbase.maxrevision
            #datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
            datecreation =  str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            lastobjetid = self.dbase.getLastId('Objet') + 1
            sql = "INSERT INTO Objet (id_objet, lpk_revision_begin, datetimecreation ) "
            sql += "VALUES(" + str(lastobjetid ) + "," + str(self.dbase.maxrevision) +  ",'" + datecreation + "');"
            query = self.dbase.query(sql)
            self.dbase.commit()
            pkobjet = self.dbase.getLastRowId('Objet')



        #sql = "INSERT INTO Descriptionsystem (id_objet) VALUES(" + str(idobjet) + ");"
        lastdescriptionsystemid = self.dbase.getLastId('Descriptionsystem') + 1
        sql = "INSERT INTO Descriptionsystem (id_descriptionsystem, lpk_objet) "
        sql += "VALUES(" + str(lastdescriptionsystemid) +   "," + str(pkobjet) + ");"
        query = self.dbase.query(sql)
        self.dbase.commit()
        pksys = self.dbase.getLastRowId('Descriptionsystem')

        #idnoeud = self.currentFeature.id()
        pknoeud = self.currentFeaturePK
        lastidnoeud = self.dbase.getLastId('Noeud') + 1
        sql = "UPDATE Noeud SET id_noeud = " + str(lastidnoeud)  + ","
        sql += "lpk_descriptionsystem = " + str(pksys)
        sql += " WHERE pk_noeud = " + str(pknoeud) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()




    def postSaveFeature(self, boolnewfeature):
        pass


    def postDeleteFeature(self):
        pass

    def deleteParentFeature(self):

        sql = "SELECT pk_objet, pk_descriptionsystem FROM Noeud_qgis WHERE pk_noeud = " + str(self.currentFeaturePK)
        pkobjet, pkdes = self.dbase.query(sql)[0]
        #idobjet = self.currentFeature['id_objet']
        #idressource = self.currentFeature['id_ressource']

        sql = "DELETE FROM Objet WHERE pk_objet = " + str(pkobjet)
        query = self.dbase.query(sql)
        self.dbase.commit()

        sql = "DELETE FROM Descriptionsystem WHERE pk_descriptionsystem = " + str(pkdes)
        query = self.dbase.query(sql)
        self.dbase.commit()


        if False:
            idobjet = self.currentFeature['id_objet']
            # idnoeud= self.currentFeature['id_noeud']


            sql = "DELETE FROM Objet WHERE id_objet = " + str(idobjet) + ";"
            query = self.dbase.query(sql)
            self.dbase.commit()

            sql = "DELETE FROM Descriptionsystem WHERE id_objet = " + str(idobjet) + ";"
            query = self.dbase.query(sql)
            self.dbase.commit()


        return True


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabase_noeud_tool_ui.ui')
        uic.loadUi(uipath, self)