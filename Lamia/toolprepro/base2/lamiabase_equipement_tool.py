# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore

try:
    from qgis.PyQt.QtGui import (QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget)
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ...toolabstract.Lamia_abstract_tool import AbstractLamiaTool

from .lamiabase_photo_tool import BasePhotoTool
# from .lamiadigue_rapport_tool import RapportTool
# from .lamiadigue_tronconemprise_tool  import TronconEmpriseTool
from .lamiabase_croquis_tool import BaseCroquisTool
import os
import datetime



class BaseEquipementTool(AbstractLamiaTool):

    LOADFIRST = True
    dbasetablename = 'Equipement'
    specialfieldui = []

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(BaseEquipementTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)
        
    def initTool(self):
        # ****************************************************************************************
        # Main spec

        self.CAT = 'Description'
        self.NAME = 'Equipement'
        self.dbasetablename = 'Equipement'
        self.PointENABLED = True
        self.LineENABLED = True
        # self.PolygonENABLED = True
        # self.magicfunctionENABLED = True
        self.linkagespec = {'Equipement': {'tabletc': None,
                                           'idsource': 'lid_descriptionsystem_1',
                                           'idtcsource': None,
                                           'iddest': 'id_descriptionsystem',
                                           'idtcdest': None,
                                           'desttable': ['Equipement','Noeud','Infralineaire']}



                            }
        # self.pickTable = None
        self.debug = False
        self.iconpath = os.path.join(os.path.dirname(__file__), 'lamiabase_equipement_tool_icon.svg')

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
            self.linkuserwdgfield = {'Equipement' : {'linkfield' : 'id_equipement',
                                             'widgets' : {'categorie': self.userwdgfield.comboBox_cat}},
                                'Objet' : {'linkfield' : 'id_objet',
                                          'widgets' : {
                                                          'commentaire': self.userwdgfield.textBrowser_comm}},
                                'Descriptionsystem' : {'linkfield' : 'id_descriptionsystem',
                                          'widgets' : {}}}
            self.userwdgfield.comboBox_cat.currentIndexChanged.connect(self.changeCategorie)


            # ****************************************************************************************
            # child widgets
            self.dbasechildwdgfield = []

            if self.parentWidget is None:
                self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(dbase=self.dbase, gpsutil=self.gpsutil, parentwidget=self)
                self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)

                self.propertieswdgCROQUIS = BaseCroquisTool(dbase=self.dbase, parentwidget=self)
                self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)




    def changeCategorie(self,intcat):
        pagecount = self.userwdg.stackedWidget.count()
        if intcat >= pagecount -1 :
            self.userwdg.stackedWidget.setCurrentIndex(pagecount -1)
        else:
            self.userwdg.stackedWidget.setCurrentIndex(intcat)


    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass


    def postloadIds(self,sqlin):
        strid = 'id_' + self.dbasetablename.lower()
        sqlin += ' ORDER BY ' + strid
        return sqlin



    def postInitFeatureProperties(self, feat):
        pass

    def createParentFeature(self):
        pkobjet = self.dbase.createNewObjet()

        if False:

            # lastrevision = self.dbase.maxrevision
            # datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
            datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            lastobjetid = self.dbase.getLastId('Objet') + 1
            sql = "INSERT INTO Objet (id_objet, lpk_revision_begin, datetimecreation ) "
            sql += "VALUES(" + str(lastobjetid) + "," + str(self.dbase.maxrevision) + ",'" + datecreation + "');"
            query = self.dbase.query(sql)
            self.dbase.commit()
            pkobjet = self.dbase.getLastRowId('Objet')

        # sql = "INSERT INTO Descriptionsystem (id_objet) VALUES(" + str(idobjet) + ");"
        lastdescriptionsystemid = self.dbase.getLastId('Descriptionsystem') + 1
        sql = "INSERT INTO Descriptionsystem (id_descriptionsystem, lpk_objet) "
        sql += "VALUES(" + str(lastdescriptionsystemid) + "," + str(pkobjet) + ");"
        query = self.dbase.query(sql)
        self.dbase.commit()
        pksys = self.dbase.getLastRowId('Descriptionsystem')

        # idnoeud = self.currentFeature.id()
        pkequip = self.currentFeaturePK
        lastidequip = self.dbase.getLastId('Equipement') + 1
        sql = "UPDATE Equipement SET id_equipement = " + str(lastidequip) + ","
        sql += "lpk_descriptionsystem = " + str(pksys)
        sql += " WHERE pk_equipement = " + str(pkequip) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()

        if  self.parentWidget is not None and self.parentWidget.currentFeature is not None:
            # if "lid_descriptionsystem" in self.dbase.dbasetables[self.parentWidget.dbasetablename]['fields'].keys():
            if 'Descriptionsystem' in self.dbase.getParentTable(self.parentWidget.dbasetablename):

                #parentid
                sql = "SELECT id_descriptionsystem FROM " + self.parentWidget.dbasetablename.lower() + "_qgis"
                sql += " WHERE pk_" + self.parentWidget.dbasetablename.lower() + " = " + str(self.parentWidget.currentFeaturePK)
                parentid = self.dbase.query(sql)[0][0]
                #currentparentlinkfield = self.parentWidget.currentFeature['id_descriptionsystem']
                sql = "UPDATE Equipement SET lid_descriptionsystem_1 = " + str(parentid)
                sql += " WHERE pk_equipement = " + str(pkequip)
                self.dbase.query(sql)
                self.dbase.commit()







    def postSaveFeature(self, boolnewfeature):
        pass


    def deleteParentFeature(self):

        sql = "SELECT pk_objet, pk_descriptionsystem FROM Equipement_qgis WHERE pk_equipement = " + str(self.currentFeaturePK)
        pkobjet, pkdes = self.dbase.query(sql)[0]
        #idobjet = self.currentFeature['id_objet']
        #idressource = self.currentFeature['id_ressource']

        sql = "DELETE FROM Objet WHERE pk_objet = " + str(pkobjet)
        query = self.dbase.query(sql)
        self.dbase.commit()

        sql = "DELETE FROM Descriptionsystem WHERE pk_descriptionsystem = " + str(pkdes)
        query = self.dbase.query(sql)
        self.dbase.commit()


        return True



class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabase_equipement_tool_ui.ui')
        uic.loadUi(uipath, self)