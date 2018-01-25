# -*- coding: utf-8 -*-

import datetime
import os

from qgis.PyQt import uic, QtCore, QtGui

from InspectionDigueV2.src.toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from .InspectionDigue_croquis_tool import CroquisTool
from .InspectionDigue_profiltravers_R_tool import ProfilTraversRTool

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), '..', 'dialog', 'InspectionDigue_propertieswidget.ui'))
FORM_CLASS2, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'ProfilTraversToolUser.ui'))


class ProfilTraversTool(AbstractInspectionDigueTool, FORM_CLASS):

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(ProfilTraversTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)
        
    def initTool(self):
        self.setupUi(self)
        self.CAT = 'Topographie'
        self.NAME = 'Profil en travers'
        self.dbasetablename = 'PROFILTRAVERS'
        self.visualmode = [1, 2]

        #self.qtreewidgetfields=['Nom']

        #self.propertieswdgPHOTOGRAPHIE = PhotosTool(dbase=self.dbase, parentwidget=self)
        #self.propertieswdgRAPPORT = RapportTool(dbase=self.dbase, parentwidget=self)
        #self.propertieswdgTRONCONEMPRISE = TronconEmpriseTool(dbase=self.dbase, parentwidget=self)


        #self.dbasechildwdg = [self.propertieswdgPHOTOGRAPHIE,self.propertieswdgRAPPORT,self.propertieswdgTRONCONEMPRISE]
        self.LineENABLED = True

        self.userwdg = UserUI()
        #self.linkuserwdg = {'Date': self.userwdg.dateEdit}

        self.linkuserwdg = {'PROFILTRAVERS' : {'linkfield' : 'ID',
                                         'widgets' : {'Date': self.userwdg.dateEdit}},
                            'OBJET' : {'linkfield' : 'IdObjet',
                                      'widgets' : {}},
                            'DESCRIPTIONSYSTEME' : {'linkfield' : 'IdSys',
                                      'widgets' : {}}}


        self.propertieswdgCROQUIS = CroquisTool(dbase=self.dbase, parentwidget=self)
        self.propertieswdgCROQUIS.NAME = None
        self.userwdg.tabWidget.widget(0).layout().addWidget(self.propertieswdgCROQUIS)

        self.propertieswdgPROFILTRAVERSR = ProfilTraversRTool(dbase=self.dbase, parentwidget=self)
        self.propertieswdgPROFILTRAVERSR.NAME = None
        self.userwdg.tabWidget.widget(1).layout().addWidget(self.propertieswdgPROFILTRAVERSR)

        self.dbasechildwdg = [self.propertieswdgCROQUIS,self.propertieswdgPROFILTRAVERSR]

        self.idstoload = {'TRONCON' : ['LkTroncon','ID' ]}

    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass



    def postInitFeatureProperties(self, feat):
        if self.currentFeature is None:
            datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
            self.initFeatureProperties(feat, 'Date', datecreation)

            if self.parentWidget is not None:
                if self.parentWidget.dbasetablename == 'TRONCON' and self.parentWidget.currentFeature is not None:
                    self.initFeatureProperties(self.currentFeature, 'LkTroncon', self.parentWidget.currentFeature.id())


    def createParentFeature(self):
        datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
        # print(datecreation)
        sql = "INSERT INTO OBJET (DateCreation) VALUES('" + datecreation + "');"
        query = self.dbase.query(sql)
        self.dbase.commit()
        idobjet = self.dbase.getLastRowId('OBJET')

        sql = "INSERT INTO DESCRIPTIONSYSTEME (IdObjet) VALUES(" + str(idobjet) + ");"
        query = self.dbase.query(sql)
        self.dbase.commit()
        idsys = self.dbase.getLastRowId('DESCRIPTIONSYSTEME')

        idprofiltravers = self.currentFeature.id()

        sql = "UPDATE PROFILTRAVERS SET IdObjet = " + str(idobjet) + ",IdSys = " + str(idsys) + " WHERE id = " + str(
            idprofiltravers) + ";"
        # print(sql)
        query = self.dbase.query(sql)
        self.dbase.commit()

        if self.parentWidget is not None and self.parentWidget.currentFeature is not None:
            if self.parentWidget.dbasetablename == 'TRONCON':
                # print(self.parentWidget.currentFeature.attributes())
                currentparentlinkfield = self.parentWidget.currentFeature['ID']
                sql = "UPDATE PROFILTRAVERS SET LkTroncon = " + str(currentparentlinkfield) + " WHERE id = " + str(
                    idprofiltravers) + ";"
                query = self.dbase.query(sql)
                self.dbase.commit()

    def postSaveFeature(self, boolnewfeature):
        pass
        if False:
            if boolnewfeature:
                datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
                # print(datecreation)
                sql = "INSERT INTO OBJET (DateCreation) VALUES('" + datecreation + "');"
                query = self.dbase.query(sql)
                self.dbase.commit()
                idobjet = self.dbase.getLastRowId('OBJET')

                sql = "INSERT INTO DESCRIPTIONSYSTEME (IdObjet) VALUES(" + str(idobjet) + ");"
                query = self.dbase.query(sql)
                self.dbase.commit()
                idsys = self.dbase.getLastRowId('DESCRIPTIONSYSTEME')

                idprofiltravers = self.currentFeature.id()

                sql = "UPDATE PROFILTRAVERS SET IdObjet = " + str(idobjet) +",IdSys = " + str(idsys) + " WHERE id = " + str(idprofiltravers) + ";"
                # print(sql)
                query = self.dbase.query(sql)
                self.dbase.commit()

                if self.parentWidget is not None and self.parentWidget.currentFeature is not None :
                    if self.parentWidget.dbasetablename == 'TRONCON':
                        #print(self.parentWidget.currentFeature.attributes())
                        currentparentlinkfield = self.parentWidget.currentFeature['ID']
                        sql = "UPDATE PROFILTRAVERS SET LkTroncon = " + str(currentparentlinkfield) + " WHERE id = " + str(idprofiltravers) + ";"
                        query = self.dbase.query(sql)
                        self.dbase.commit()



class UserUI(QtGui.QWidget, FORM_CLASS2):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        self.setupUi(self)
