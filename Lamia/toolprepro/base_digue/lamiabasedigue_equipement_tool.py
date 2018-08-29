# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore

try:
    from qgis.PyQt.QtGui import (QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget)
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..base.lamiabase_equipement_tool import BaseEquipementTool

from .lamiabasedigue_photo_tool import BaseDiguePhotoTool as BasePhotoTool
from ..base.lamiabase_croquis_tool import BaseCroquisTool
from .lamiabasedigue_desordre_tool import BaseDigueDesordreTool


import os
import datetime


class BaseDigueEquipementTool(BaseEquipementTool):

    LOADFIRST = True
    dbasetablename = 'Equipement'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(BaseDigueEquipementTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)

    """
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
        self.iconpath = os.path.join(os.path.dirname(__file__), 'lamiadefault_equipement_tool_icon.svg')

        # ****************************************************************************************
        #properties ui
        pass
    """

    def initFieldUI(self):
        # ****************************************************************************************
        #   userui Field
        if self.userwdgfield is None:
            # ****************************************************************************************
            # userui
            self.userwdgfield = UserUI()
            self.linkuserwdgfield = {'Equipement' : {'linkfield' : 'id_equipement',
                                             'widgets' : {'categorie': self.userwdgfield.comboBox_cat,
                                                          'cote': self.userwdgfield.comboBox_cote,
                                                          'position': self.userwdgfield.comboBox_position,
                                                          'typeequipement': self.userwdgfield.comboBox_type,
                                                          'implantation': self.userwdgfield.comboBox_implantation,
                                                          'ecoulement': self.userwdgfield.comboBox_ecoulement,
                                                          'utilisation': self.userwdgfield.comboBox_utilisation,
                                                          'dimverti': self.userwdgfield.doubleSpinBox_dimvert,
                                                          'dimhori': self.userwdgfield.doubleSpinBox_dimhoriz,
                                                          'securite': self.userwdgfield.comboBox_securite
                                                          }},
                                'Objet' : {'linkfield' : 'id_objet',
                                          'widgets' : {'commentaire': self.userwdgfield.textBrowser_comm}},
                                'Descriptionsystem' : {'linkfield' : 'id_descriptionsystem',
                                          'widgets' : {}}}
            self.userwdgfield.comboBox_cat.currentIndexChanged.connect(self.changeCategorie)
            self.userwdgfield.toolButton_calch.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_dimvert))
            self.userwdgfield.toolButton__calcv.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_dimhoriz))


            # ****************************************************************************************
            # child widgets

            self.dbasechildwdgfield = []

            self.propertieswdgDesordre = BaseDigueDesordreTool(dbase=self.dbase, gpsutil=self.gpsutil, parentwidget=self)
            self.propertieswdgDesordre.userwdgfield.frame_2.setParent(None)
            self.propertieswdgDesordre.pushButton_addFeature.setEnabled(False)
            self.propertieswdgDesordre.pushButton_delFeature.setEnabled(False)
            self.propertieswdgDesordre.comboBox_featurelist.setEnabled(False)
            self.propertieswdgDesordre.groupBox_geom.setParent(None)
            self.dbasechildwdgfield.append(self.propertieswdgDesordre)




            if self.parentWidget is None:
                self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(dbase=self.dbase, gpsutil=self.gpsutil, parentwidget=self)
                self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)

                self.propertieswdgCROQUIS = BaseCroquisTool(dbase=self.dbase, parentwidget=self)
                self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)




                #parentwdg = self.dbase.dbasetables['Equipement']['widget']
                self.propertieswdgEQUIPEMENT = BaseDigueEquipementTool(dbase=self.dbase, parentwidget=self)
                self.dbasechildwdgfield.append(self.propertieswdgEQUIPEMENT)






    def postSaveFeature(self, boolnewfeature):

        if boolnewfeature :

            if self.currentFeature['categorie'] == 'OUH':
                self.propertieswdgDesordre.featureSelected()
                combocrtindex = self.propertieswdgDesordre.userwdgfield.comboBox_groupedes.findText('Equipement')
                self.propertieswdgDesordre.userwdgfield.comboBox_groupedes.setCurrentIndex(combocrtindex)
                self.propertieswdgDesordre.tempgeometry = self.currentFeature.geometry()
                self.propertieswdgDesordre.saveFeature()

            if self.parentWidget is not None and self.parentWidget.dbasetablename == 'Equipement':
                self.parentWidget.loadFeaturesinTreeWdg()
                # self.parentWidget.onActivationRaw(self.parentWidget.qtreewidgetitem, self.parentWidget.qtreewidgetitem)
                self.parentWidget.onActivationRaw(self.parentWidget.qtreewidgetitem)





    def changeCategorie(self,intcat):
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


    def postInitFeatureProperties(self, feat):
        pass
        if False:
            print(self.propertieswdgDesordre.comboBox_featurelist.count())
            if feat is not None and self.currentFeature['categorie'] == 'OUH' and self.propertieswdgDesordre.comboBox_featurelist.count() == 0:
                print('tt')
                self.propertieswdgDesordre.pushButton_addFeature.setEnabled(True)
            else:
                print('ff')
                self.propertieswdgDesordre.pushButton_addFeature.setEnabled(False)




    """
    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass





    def createParentFeature(self):

        lastrevision = self.dbase.getLastPk('Revision')
        datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
        lastobjetid = self.dbase.getLastId('Objet') + 1
        sql = "INSERT INTO Objet (id_objet, id_revisionbegin, datecreation ) "
        sql += "VALUES(" + str(lastobjetid) + "," + str(lastrevision) + ",'" + datecreation + "');"
        query = self.dbase.query(sql)
        self.dbase.commit()
        # idobjet = self.dbase.getLastRowId('Objet')

        # sql = "INSERT INTO Descriptionsystem (id_objet) VALUES(" + str(idobjet) + ");"
        lastdescriptionsystemid = self.dbase.getLastId('Descriptionsystem') + 1
        sql = "INSERT INTO Descriptionsystem (id_descriptionsystem, id_revisionbegin, id_objet) "
        sql += "VALUES(" + str(lastdescriptionsystemid) + "," + str(lastrevision) + "," + str(lastobjetid) + ");"
        query = self.dbase.query(sql)
        self.dbase.commit()
        # idsys = self.dbase.getLastRowId('Descriptionsystem')

        pkequip = self.currentFeature.id()
        lastidequip = self.dbase.getLastId('Equipement') + 1

        sql = "UPDATE Equipement SET id_objet = " + str(lastobjetid) + ","
        sql += "id_descriptionsystem = " + str(lastdescriptionsystemid) + ","
        sql += "id_equipement = " + str(lastidequip) + ","
        sql += "id_revisionbegin = " + str(lastrevision)
        sql += " WHERE pk_equipement = " + str(pkequip) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()


        if self.parentWidget is not None and self.parentWidget.currentFeature is not None:
            currentparentlinkfield = self.parentWidget.currentFeature['id_descriptionsystem']
            sql = "UPDATE Equipement SET lk_descriptionsystem = " + str(currentparentlinkfield)
            sql += " WHERE pk_equipement = " + str(pkequip)
            self.dbase.query(sql)
            self.dbase.commit()





    def deleteParentFeature(self):
        idobjet = self.currentFeature['id_objet']

        sql = "DELETE FROM Objet WHERE id_objet = " + str(idobjet) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()

        sql = "DELETE FROM Descriptionsystem WHERE id_objet = " + str(idobjet) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()

        return True


    """


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabasedigue_equipement_tool_ui.ui')
        uic.loadUi(uipath, self)