# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore

try:
    from qgis.PyQt.QtGui import (QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget)
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..abstract.lamia_desordre_tool import AbstractDesordreTool
from .lamiadigue_photos_tool import PhotosTool
from .lamiadigue_observation_tool import ObservationTool
from .lamiadigue_croquis_tool import CroquisTool
import os
import datetime
import qgis




class DesordreTool(AbstractDesordreTool):

    LOADFIRST = True
    dbasetablename = 'Desordre'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None, parentwidget=None, parent=None):
        super(DesordreTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)



    """
    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Desordre'
        self.NAME = 'Desordre'
        self.dbasetablename = 'Desordre'
        #self.visualmode = [1, 2]
        self.PointENABLED = True
        self.LineENABLED = True
        # self.PolygonEnabled = True
        self.magicfunctionENABLED = True

        self.linkagespec = {'Descriptionsystem' : {'tabletc' : None,
                                              'idsource' : 'lk_descriptionsystem',
                                            'idtcsource' : None,
                                           'iddest' : 'id_descriptionsystem',
                                           'idtcdest' : None,
                                           'desttable' : ['Infralineaire','Equipement']}}


        self.pickTable = {'LkDesSys': {'TRONCON': 'IdSys'}}

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

            self.linkuserwdgfield = {'Desordre' : {'linkfield' : 'id_desordre',
                                             'widgets' : {'cote': self.userwdgfield.comboBox_cote,
                                                        'position': self.userwdgfield.comboBox_position,
                                                          'catdes': self.userwdgfield.comboBox_des_cat,
                                                        'typedes': self.userwdgfield.comboBox_des_type}},
                                'Objet' : {'linkfield' : 'id_objet',
                                          'widgets' : {}}}


            # ****************************************************************************************
            # child widgets

            if True:
                self.dbasechildwdgfield = []
                self.propertieswdgOBSERVATION = ObservationTool(dbase=self.dbase, parentwidget=self)
                self.dbasechildwdgfield.append(self.propertieswdgOBSERVATION)


                self.propertieswdgOBSERVATION2 = ObservationTool(dbase=self.dbase, parentwidget=self)
                self.propertieswdgOBSERVATION2.NAME = None
                self.userwdgfield.tabWidget.widget(0).layout().addWidget(self.propertieswdgOBSERVATION2)
                self.dbasechildwdgfield.append(self.propertieswdgOBSERVATION2)

                self.propertieswdgPHOTOGRAPHIE = PhotosTool(dbase=self.dbase, gpsutil=self.gpsutil, parentwidget=self.propertieswdgOBSERVATION2)
                self.propertieswdgPHOTOGRAPHIE.NAME = None
                self.userwdgfield.tabWidget.widget(1).layout().addWidget(self.propertieswdgPHOTOGRAPHIE)

                self.propertieswdgCROQUIS = CroquisTool(dbase=self.dbase, gpsutil=self.gpsutil, parentwidget=self.propertieswdgOBSERVATION2)
                self.propertieswdgCROQUIS.NAME = None
                self.userwdgfield.tabWidget.widget(2).layout().addWidget(self.propertieswdgCROQUIS)

                self.propertieswdgOBSERVATION2.dbasechildwdgfield = [self.propertieswdgPHOTOGRAPHIE, self.propertieswdgCROQUIS]
                try:
                    self.propertieswdgOBSERVATION2.currentFeatureChanged.disconnect()
                except:
                    pass
                for childwdg in self.propertieswdgOBSERVATION2.dbasechildwdgfield:
                    self.propertieswdgOBSERVATION2.currentFeatureChanged.connect(childwdg.loadChildFeatureinWidget)

                #self.dbasechildwdg = [self.propertieswdgOBSERVATION, self.propertieswdgOBSERVATION2]


            if self.parentWidget is not None :
                self.pushButton_addFeature.setEnabled(True)
            else:
                self.pushButton_addFeature.setEnabled(False)




    """
    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass
    """
    def magicFunction(self):
        self.featureSelected()
        self.addGPSPoint()
        self.saveFeature()
        self.propertieswdgOBSERVATION2.featureSelected()
        self.propertieswdgOBSERVATION2.saveFeature()
    """
    def postInitFeatureProperties(self, feat):
        pass
    """

    def createParentFeature(self):

        datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
        #print(datecreation)
        sql = "INSERT INTO Objet (datecreation) VALUES('" + datecreation + "');"
        query = self.dbase.query(sql)
        self.dbase.commit()
        idobjet = self.dbase.getLastRowId('Objet')

        iddesordre = self.currentFeature.id()

        sql = "UPDATE Desordre SET id_objet = " + str(idobjet) + " WHERE id_desordre = " + str(iddesordre) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()

        if self.parentWidget is not None and self.parentWidget.currentFeature is not None:
            if self.parentWidget.dbasetablename in ['Equipement'] and self.parentWidget.currentFeature['categorie'] == 'OUH':
                currentparentlinkfield = self.parentWidget.currentFeature['id_descriptionsystem']
                sql = "UPDATE Desordre SET lk_descriptionsystem = " + str(currentparentlinkfield) + ','
                sql += "groupedesordre = 'OH'  WHERE id_desordre = " + str(iddesordre)
                #sql = "UPDATE Desordre SET lk_descriptionsystem = ?, groupedesordre = 'OH' WHERE id_desordre = ?"
                #params = [self.parentWidget.currentFeature['id_descriptionsystem'],iddesordre ]
                self.dbase.query(sql)
                self.dbase.commit()
            elif self.parentWidget.dbasetablename in ['Infralineaire']:
                currentparentlinkfield = self.parentWidget.currentFeature['id_descriptionsystem']
                sql = "UPDATE Desordre SET lk_descriptionsystem = " + str(currentparentlinkfield) + ','
                sql += "groupedesordre = 'INF'  WHERE id_desordre = " + str(iddesordre)
                self.dbase.query(sql)
                self.dbase.commit()

    """
                        
                        
                        

    def postSaveFeature(self, boolnewfeature):
        pass


    """


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiadigue_desordre_tool_ui.ui')
        uic.loadUi(uipath, self)
        

