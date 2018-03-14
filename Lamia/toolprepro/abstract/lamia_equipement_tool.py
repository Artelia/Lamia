# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore

try:
    from qgis.PyQt.QtGui import (QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget)
from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from .lamia_photos_tool import AbstractPhotosTool
from .lamia_croquis_tool import AbstractCroquisTool
import os
import datetime



class AbstractEquipementTool(AbstractInspectionDigueTool):


    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(AbstractEquipementTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)
        
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
                                           'idsource': 'lk_equipement',
                                           'idtcsource': None,
                                           'iddest': 'id_equipement',
                                           'idtcdest': None,
                                           'desttable': ['Equipement']}}
        # self.pickTable = None
        self.debug = False


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
                                             'widgets' : {'cote': self.userwdgfield.comboBox_cote,
                                                          'position' : self.userwdgfield.comboBox_position,
                                                          'categorie': self.userwdgfield.comboBox_cat,
                                                          'typeequipement': self.userwdgfield.comboBox_type,
                                                          'implantation': self.userwdgfield.comboBox_implantation,
                                                          'ecoulement': self.userwdgfield.comboBox_ecoulement,
                                                          'utilisation': self.userwdgfield.comboBox_utilisation,
                                                          'dimverti': self.userwdgfield.doubleSpinBox_dimvert,
                                                          'dimhori': self.userwdgfield.doubleSpinBox_dimhoriz,
                                                          'securite' : self.userwdgfield.comboBox_securite,
                                                          'commentaires': self.userwdgfield.textBrowser_comm}},
                                'Objet' : {'linkfield' : 'id_objet',
                                          'widgets' : {}},
                                'Descriptionsystem' : {'linkfield' : 'id_descriptionsystem',
                                          'widgets' : {}}}
            self.userwdgfield.comboBox_cat.currentIndexChanged.connect(self.changeCategorie)
            self.pushButton_addPoint.setEnabled(False)
            self.pushButton_addLine.setEnabled(False)


            # ****************************************************************************************
            # child widgets
            self.dbasechildwdgfield = []
            self.propertieswdgPHOTOGRAPHIE = AbstractPhotosTool(dbase=self.dbase, gpsutil=self.gpsutil, parentwidget=self)
            self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)

            self.propertieswdgCROQUIS = AbstractCroquisTool(dbase=self.dbase, parentwidget=self)
            self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

            if self.parentWidget is None:
                #parentwdg = self.dbase.dbasetables['Equipement']['widget']
                self.propertieswdgEQUIPEMENT = AbstractEquipementTool(dbase=self.dbase, parentwidget=self)
                self.dbasechildwdgfield.append(self.propertieswdgEQUIPEMENT)

                try:
                    self.currentFeatureChanged.disconnect()
                except:
                    pass
                for childwdg in self.dbasechildwdgfield:
                    self.currentFeatureChanged.connect(childwdg.loadChildFeatureinWidget)


    def changeCategorie(self,int):
        if 'Ponctuel' in self.userwdg.comboBox_cat.currentText():
            self.userwdg.stackedWidget.setCurrentIndex(1)
            self.pushButton_addPoint.setEnabled(True)
            self.pushButton_addLine.setEnabled(False)
        elif 'Lineaire' in self.userwdg.comboBox_cat.currentText():
            self.userwdg.stackedWidget.setCurrentIndex(0)
            self.pushButton_addPoint.setEnabled(False)
            self.pushButton_addLine.setEnabled(True)
        else:
            self.pushButton_addPoint.setEnabled(False)
            self.pushButton_addLine.setEnabled(False)



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

        idreseaulin = self.currentFeature.id()

        sql = "UPDATE Equipement SET id_objet = " + str(idobjet) + ",id_descriptionsystem = " + str(idsys) + " WHERE id_equipement = " + str(idreseaulin) + ";"
        # print(sql)
        query = self.dbase.query(sql)
        self.dbase.commit()

        if self.parentWidget is not None and self.parentWidget.currentFeature is not None:
            if self.parentWidget.dbasetablename == 'Equipement':
                currentparentlinkfield = self.parentWidget.currentFeature['id_equipement']
                sql = "UPDATE Equipement SET lk_equipement = " + str(currentparentlinkfield) + " WHERE id_equipement = " + str(idreseaulin)
                self.dbase.query(sql)
                self.dbase.commit()


    def postSaveFeature(self, boolnewfeature):
        pass


    def deleteParentFeature(self):
        idobjet = self.currentFeature['id_objet']

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
        uipath = os.path.join(os.path.dirname(__file__), 'lamia_equipement_tool_ui.ui')
        uic.loadUi(uipath, self)