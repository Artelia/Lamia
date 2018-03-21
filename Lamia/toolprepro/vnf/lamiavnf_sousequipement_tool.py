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

from .lamiavnf_photos_tool import PhotosTool
from .lamiavnf_croquis_tool import CroquisTool
import os
import datetime



class SousEquipementTool(AbstractInspectionDigueTool):

    LOADFIRST = False
    dbasetablename = 'Propriete_option'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(SousEquipementTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)
        
    def initTool(self):
        # ****************************************************************************************
        # Main spec

        self.CAT = 'Description'
        self.NAME = 'SousEquipement'
        self.dbasetablename = 'Propriete_option'
        self.visualmode = [1, 2]
        #self.PointENABLED = True
        #self.LineENABLED = True
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

        if False and self.linkedtreewidget is not None:
            #self.linkedtreewidget.currentItemChanged.connect(self.itemChanged)
            print('ok treew')
            self.connectIdsGui()

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
            self.linkuserwdgfield = {'Propriete_option' : {'linkfield' : 'id_propriete_option',
                                                         'widgets' : {
                                                                    #'propriete': self.userwdgfield.comboBox_propriete,
                                                                    'option': self.userwdgfield.comboBox_option,
                                                                     'valeur': self.userwdgfield.textBrowser
                                                                      }},
                                     'Objet': {'linkfield': 'id_objet',
                                               'widgets': {}},
                                     'Descriptionsystem': {'linkfield': 'id_descriptionsystem',
                                                           'widgets': {}}
                                     }


            #self.userwdgfield.comboBox_cat.currentIndexChanged.connect(self.changeCategorie)
            self.pushButton_addPoint.setEnabled(False)
            self.pushButton_addLine.setEnabled(False)

            if self.parentWidget is not None:
                self.comboBox_featurelist.setParent(None)
                self.pushButton_linkage.setParent(None)
                self.pushButton_goto.setParent(None)
                self.pushButton_magic.setParent(None)
                self.pushButton_delFeature.setParent(None)
                self.pushButton_addFeature.setParent(None)

            if False:
                self.propertieswdgPHOTOGRAPHIE = PhotosTool(dbase=self.dbase, gpsutil=self.gpsutil, parentwidget=self)
                #self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)
                self.userwdgfield.tabWidget.widget(1).layout().addWidget(self.propertieswdgPHOTOGRAPHIE)

                self.propertieswdgCROQUIS = CroquisTool(dbase=self.dbase, parentwidget=self)
                self.userwdgfield.tabWidget.widget(2).layout().addWidget(self.propertieswdgCROQUIS)

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





    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass



    def postInitFeatureProperties(self, feat):
        # print('postInitFeatureProperties')
        self.userwdgfield.comboBox_option.clear()

        if feat is not None:

            equipementpropriete = feat['equipementpropriete']
            disablecombo = True
            indextoset = None
            listcombo=['/']
            fetoption = feat['option']



            for val in  self.dbase.dbasetables['Propriete_option']['fields']['option']['Cst']:
                if equipementpropriete in val[2]:
                    listcombo.append(str(val[0]))
                    disablecombo = False
                    # print('list', val, listcombo)
                    if val[1].isnumeric() and fetoption == int(val[1]):
                        # print(fetoption,int(val[1]) , listcombo )
                        indextoset = len(listcombo)-1

            # print(listcombo)

            if disablecombo:
                self.userwdgfield.stackedWidget.setCurrentIndex(1)
            else:
                self.userwdgfield.stackedWidget.setCurrentIndex(0)
                self.userwdgfield.comboBox_option.addItems(listcombo)
                if indextoset:
                    self.userwdgfield.comboBox_option.setCurrentIndex(indextoset)

                # print('fetoption', fetoption,indextoset)



        if False:
            self.userwdgfield.comboBox_propriete.clear()
            equipementpropriete = feat['equipementpropriete']
            self.userwdgfield.comboBox_equipementpropriete.addItems([str(equipementpropriete)])
            self.userwdgfield.comboBox_equipementpropriete.currentIndexChanged.emit(0)
            print(equipementpropriete)




        if False:
            txtprop = self.userwdgfield.comboBox_propriete.currentText()
            #print(txtprop)
            fieldscst = self.dbase.dbasetables['Propriete_option']['fields']['propriete']['Cst']
            fieldscsttxt = [elem[0] for elem in fieldscst]
            #print(fieldscsttxt)
            try:
                indexfieldscsttxt = fieldscsttxt.index(txtprop)
            except ValueError as e:
                print(e)
                print(txtprop, fieldscsttxt)
            # print('fieldscst', fieldscst[indexfieldscsttxt][1])

            if fieldscst[indexfieldscsttxt][1].isnumeric():
                rawvaluefieldscsttxt = int(fieldscst[indexfieldscsttxt][1])

                # print('rawvaluefieldscsttxt', rawvaluefieldscsttxt)

                fieldscstoption = self.dbase.dbasetables['Propriete_option']['fields']['option']['Cst']
                disablecombo = True
                for optioncst in fieldscstoption[1:]:
                    #print(optioncst[2])
                    if rawvaluefieldscsttxt in optioncst[2]:
                        # print('find')
                        disablecombo = False
                        break

                # print('disablecombo',disablecombo)

                if disablecombo:
                    self.userwdgfield.stackedWidget.setCurrentIndex(1)
                    #self.userwdgfield.comboBox_option.setEnabled(False)
                    #self.userwdgfield.textBrowser.setEnabled(True)
                else:
                    self.userwdgfield.stackedWidget.setCurrentIndex(0)
                    #self.userwdgfield.comboBox_option.setEnabled(True)
                    #self.userwdgfield.textBrowser.setEnabled(False)
                # print('done')

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

        sql = "UPDATE Propriete_option SET id_objet = " + str(idobjet) + ",id_descriptionsystem = " + str(idsys) + " WHERE id_propriete_option = " + str(idreseaulin) + ";"
        # print(sql)
        query = self.dbase.query(sql)
        self.dbase.commit()

        if self.parentWidget is not None and self.parentWidget.parentWidget is not None and self.parentWidget.parentWidget.currentFeature is not None:
            if self.parentWidget.parentWidget.dbasetablename == 'Equipement':
                idequip = self.parentWidget.parentWidget.currentFeature['id_equipement']
                sql = "UPDATE Propriete_option SET lk_equipement = " + str(idequip) + " WHERE id_propriete_option = " + str(self.currentFeature['id_propriete_option']) + ";"
                # print(sql)
                query = self.dbase.query(sql)
                self.dbase.commit()


    def postSaveFeature(self, boolnewfeature):
        pass


    def deleteParentFeature(self):
        if False:
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
        uipath = os.path.join(os.path.dirname(__file__), 'lamiavnf_ssequipement_tool_ui.ui')
        uic.loadUi(uipath, self)