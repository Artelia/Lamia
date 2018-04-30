# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore

try:
    from qgis.PyQt.QtGui import (QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget)
from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
"""
from .lamiadigue_photos_tool import PhotosTool
from .lamiadigue_croquis_tool import CroquisTool
"""

from .lamiavnf_ssequipementmain_tool  import EquipementMainTool
from .lamiavnf_photos_tool import PhotosTool
from .lamiavnf_croquis_tool import CroquisTool
from .lamiavnf_desordre_tool import DesordreTool

import os
import datetime



class EquipementTool(AbstractInspectionDigueTool):

    LOADFIRST = True
    dbasetablename = 'Equipement'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(EquipementTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)
        
    def initTool(self):
        # ****************************************************************************************
        # Main spec

        self.CAT = 'Description'
        self.NAME = 'Equipement'
        self.dbasetablename = 'Equipement'
        # self.PointENABLED = True
        self.LineENABLED = True
        # self.PolygonENABLED = True
        # self.visualmode = []
        # self.magicfunctionENABLED = True

        self.linkagespec = {'Infralineaire': {'tabletc': None,
                                           'idsource': 'lk_infralineaire',
                                           'idtcsource': None,
                                           'iddest': 'id_infralineaire',
                                           'idtcdest': None,
                                           'desttable': ['Infralineaire']}}

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
                                             'widgets' : {'note_ief': self.userwdgfield.spinBox_note_ief,
                                                          'forcage_ree': self.userwdgfield.spinBox_forcage_ree,
                                                          'typepk' : self.userwdgfield.comboBox_typepk,
                                                          'pk_debut': self.userwdgfield.doubleSpinBox_pk_debut,
                                                          'pk_fin': self.userwdgfield.doubleSpinBox_pk_fin,
                                                          'pr_debut': self.userwdgfield.spinBox_pr_debut,
                                                          'pr_fin': self.userwdgfield.spinBox_pr_fin,
                                                          'abs_debut': self.userwdgfield.spinBox_abs_debut,
                                                          'abs_fin': self.userwdgfield.spinBox_abs_fin,
                                                          'is_modified': self.userwdgfield.comboBox_is_modified,
                                                          #'ouvrage': self.userwdgfield.spinBox_ouvrage,
                                                          'partie': self.userwdgfield.comboBox_partie,
                                                          'equipement': self.userwdgfield.comboBox_equipement

                                                          }},
                                'Objet' : {'linkfield' : 'id_objet',
                                          'widgets' : {}},
                                'Descriptionsystem' : {'linkfield' : 'id_descriptionsystem',
                                          'widgets' : {}}}
            #self.userwdgfield.comboBox_cat.currentIndexChanged.connect(self.changeCategorie)
            # self.pushButton_addPoint.setEnabled(False)
            # self.pushButton_addLine.setEnabled(False)

            # ****************************************************************************************
            # child widgets
            self.dbasechildwdgfield = []
            self.propertieswdgEquipement = EquipementMainTool(dbase=self.dbase, gpsutil=self.gpsutil, parentwidget=self)
            self.dbasechildwdgfield.append(self.propertieswdgEquipement)

            self.propertieswdgDesordre = DesordreTool(dbase=self.dbase, gpsutil=self.gpsutil, parentwidget=self)
            self.dbasechildwdgfield.append(self.propertieswdgDesordre)


            if True:
                self.propertieswdgPHOTOGRAPHIE = PhotosTool(dbase=self.dbase, gpsutil=self.gpsutil, parentwidget=self)
                self.propertieswdgPHOTOGRAPHIE.NAME = None
                self.userwdgfield.tabWidget.widget(2).layout().addWidget(self.propertieswdgPHOTOGRAPHIE)
                self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)


                #self.propertieswdgCROQUIS = CroquisTool(dbase=self.dbase, parentwidget=self)
                #self.userwdgfield.tabWidget.widget(2).layout().addWidget(self.propertieswdgCROQUIS)


            if self.parentWidget is not None and self.parentWidget.dbasetablename == 'Infralineaire':
                self.pushButton_addFeature.setEnabled(True)
            else:
                self.pushButton_addFeature.setEnabled(False)




            """
            # ****************************************************************************************
            # child widgets
            self.dbasechildwdgfield = []
            self.propertieswdgPHOTOGRAPHIE = PhotosTool(dbase=self.dbase, gpsutil=self.gpsutil, parentwidget=self)
            self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)

            self.propertieswdgCROQUIS = CroquisTool(dbase=self.dbase, parentwidget=self)
            self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

            if self.parentWidget is None:
                #parentwdg = self.dbase.dbasetables['Equipement']['widget']
                self.propertieswdgEQUIPEMENT = EquipementTool(dbase=self.dbase, parentwidget=self)
                self.dbasechildwdgfield.append(self.propertieswdgEQUIPEMENT)

                try:
                    self.currentFeatureChanged.disconnect()
                except:
                    pass
                for childwdg in self.dbasechildwdgfield:
                    self.currentFeatureChanged.connect(childwdg.loadChildFeatureinWidget)
            """

    """
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
    """


    def postOnActivation(self):
        pass

        self.propertieswdgEquipement.postOnActivation()

    def postOnDesactivation(self):
        pass



    def postInitFeatureProperties(self, feat):
        if self.currentFeature is None:
            self.userwdgfield.comboBox_partie.setEnabled(True)
            self.userwdgfield.comboBox_equipement.setEnabled(True)
        else:
            self.userwdgfield.comboBox_partie.setEnabled(False)
            self.userwdgfield.comboBox_equipement.setEnabled(False)



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

        # print('*********************************')
        #create options
        self.propertieswdgEquipement.disconnectIdsGui()

        typeequiptxt = self.userwdgfield.comboBox_equipement.currentText()
        typequiplist = [elem[0] for elem in self.dbase.dbasetables['Equipement']['fields']['equipement']['Cst']]
        # print('*********************************')
        # print(typeequiptxt)
        # print(typequiplist)
        typeequipindex = typequiplist.index(typeequiptxt)
        typeequip = int(self.dbase.dbasetables['Equipement']['fields']['equipement']['Cst'][typeequipindex][1])
        # print('typeequip', typeequip)
        #typeequip = self.dbase.dbasetables['Equipement']['fields']['equipement']['Cst'][typeequipindex][0]
        #print('typeequip', typeequip)
        #typeequip = self.userwdgfield.comboBox_equipement.currentIndex() + 1
        #print('typeequip', typeequip)
        for constraint in self.dbase.dbasetables['Propriete_option']['fields']['propriete']['Cst']:
            #field = self.dbase.dbasetables['Propriete_option']['fields']['propriete'][proprietekey]
            # print(typeequip, constraint[2])
            if typeequip in constraint[2]:
                # print(constraint)
                self.propertieswdgEquipement.propertieswdgPropriete.featureSelected(None)

                self.propertieswdgEquipement.propertieswdgPropriete.saveFeature(showsavemessage=False)
                sql = "UPDATE Propriete_option SET equipementpropriete = " + str(typeequip) + str(constraint[1]) + ", "
                sql += "propriete = " + str(constraint[1])
                sql += " WHERE id_propriete_option = " + str(self.propertieswdgEquipement.propertieswdgPropriete.currentFeature['id_propriete_option'])
                # print(sql)
                self.dbase.query(sql)
                #self.propertieswdgEquipement.propertieswdgPropriete.currentFeature['equipement'] = typeequip
                #self.propertieswdgEquipement.propertieswdgPropriete.currentFeature['propriete'] = constraint[1]
                #self.propertieswdgEquipement.propertieswdgPropriete.saveFeature()

        self.propertieswdgEquipement.connectIdsGui()



        if self.parentWidget is not None and self.parentWidget.currentFeature is not None:
            if self.parentWidget.dbasetablename == 'Infralineaire':
                currentparentlinkfield = self.parentWidget.currentFeature['id_infralineaire']
                sql = "UPDATE Equipement SET lk_infralineaire = " + str(currentparentlinkfield) + " WHERE id_equipement = " + str(idreseaulin)
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



    """
    def postDeleteFeature(self):
        idobjet = self.currentFeature['IdObjet']
        datesuppr = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
        sql = "UPDATE Objet SET datedestruction = '" + datesuppr + "'  WHERE id_objet = " + str(idobjet) + ";"
        # print(sql)
        query = self.dbase.query(sql)
        self.dbase.commit()
    """


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiavnf_equipement_tool_ui.ui')
        uic.loadUi(uipath, self)