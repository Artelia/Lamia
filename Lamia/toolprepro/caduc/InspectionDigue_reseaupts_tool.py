# -*- coding: utf-8 -*-

import datetime
import os

from qgis.PyQt import uic, QtCore, QtGui

from InspectionDigueV2.src.toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from .InspectionDigue_photos_tool import PhotosTool
from .InspectionDigue_profiltravers_tool import ProfilTraversTool
from .InspectionDigue_rapport_tool import RapportTool
from .InspectionDigue_tronconemprise_tool import TronconEmpriseTool

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), '..', 'dialog', 'InspectionDigue_propertieswidget.ui'))
FORM_CLASS2, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'ReseauPtsToolUser.ui'))


class ReseauPtsTool(AbstractInspectionDigueTool, FORM_CLASS):

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(ReseauPtsTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)
        
    def initTool(self):
        self.setupUi(self)
        self.CAT = 'Description'
        self.NAME = 'Reseau ponctuel'
        self.dbasetablename = 'RESEAUPTS'

        #self.qtreewidgetfields=['Nom']
        if False:
            self.propertieswdgPHOTOGRAPHIE = PhotosTool(dbase=self.dbase, parentwidget=self)
            self.dbasechildwdg.append(self.propertieswdgPHOTOGRAPHIE)
            self.propertieswdgRAPPORT = RapportTool(dbase=self.dbase, parentwidget=self)
            self.dbasechildwdg.append(self.propertieswdgRAPPORT)
            self.propertieswdgTRONCONEMPRISE = TronconEmpriseTool(dbase=self.dbase, parentwidget=self)
            self.dbasechildwdg.append(self.propertieswdgTRONCONEMPRISE)
            if True:
                self.propertieswdgPROFILTRAVERS = ProfilTraversTool(dbase=self.dbase, parentwidget=self)
                self.dbasechildwdg.append(self.propertieswdgPROFILTRAVERS)

        #self.dbasechildwdg = [self.propertieswdgPHOTOGRAPHIE,self.propertieswdgRAPPORT,self.propertieswdgTRONCONEMPRISE,self.propertieswdgPROFILTRAVERS]
        self.PointENABLED = True

        self.userwdg = UserUI()
        """
        self.linkuserwdg = {'Nom': self.userwdg.lineEdit_nom,
                            'OBJET.DateCreation' : self.userwdg.lineEdit_test}
        """
        
        self.linkuserwdg = {'RESEAUPTS' : {'linkfield' : 'ID',
                                         'widgets' : {'COTE': self.userwdg.comboBox_cote,
                                                      'POSITION' : self.userwdg.comboBox_position,
                                                      'CATEGORIE': self.userwdg.comboBox_cat,
                                                      'TYPE': self.userwdg.comboBox_type,
                                                      'SECURITE': self.userwdg.comboBox_securite,
                                                      'COMMENTAIRE': self.userwdg.textBrowser_comm}},
                            'OBJET' : {'linkfield' : 'IdObjet',
                                      'widgets' : {}},
                            'DESCRIPTIONSYSTEME' : {'linkfield' : 'IdSys',
                                      'widgets' : {}}}
                            


        #self.pickTable = {'LkZoneGeo': {'ZONEGEO': 'ID'}}


    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass

    if False:
        def loadIds(self):
            ids = []
            if self.parentWidget is None:
                fieldlen = len(self.qtreewidgetfields)
                if fieldlen == 0:
                    sql = "SELECT ID FROM " + self.dbasetablename
                else :
                    sql = "SELECT ID, " + ','.join(self.qtreewidgetfields) + " FROM " + self.dbasetablename
                    # print(sql)
                query = self.dbase.query(sql)
                # print(query)
                ids = [row[0:fieldlen+1] for row in query]
                if False:
                    while query.next():
                        ids.append(query.value(0))
            else:
                pass
            # print('ids',ids)
            return ids

    def postInitFeatureProperties(self, feat):
        pass

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

        idreseaupts = self.currentFeature.id()

        sql = "UPDATE RESEAUPTS SET IdObjet = " + str(idobjet) + ",IdSys = " + str(idsys) + " WHERE id = " + str(idreseaupts) + ";"
        # print(sql)
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

                idtroncon = self.currentFeature.id()

                sql = "UPDATE TRONCON SET IdObjet = " + str(idobjet) +",IdSys = " + str(idsys) + " WHERE id = " + str(idtroncon) + ";"
                # print(sql)
                query = self.dbase.query(sql)
                self.dbase.commit()

                geom = self.currentFeature.geometry().buffer(10.0,12)
                geom.convertToMultiType()
                geombase = geom.exportToWkt()
                #print('buffer',geombase)
                crs = self.dbasetable['layer'].crs().authid().split(':')[1]
                sql  = "INSERT INTO TRONCONEMPRISE (LkTroncon,geom) VALUES(" + str(idtroncon) + ",ST_GeomFromText('" + geombase + "'," + crs  + "));"
                # print(sql)
                query = self.dbase.query(sql)
                self.dbase.commit()

    def postDeleteFeature(self):
        idobjet = self.currentFeature['IdObjet']
        datesuppr = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
        sql = "UPDATE OBJET SET DateDestruction = '" + datesuppr + "'  WHERE id = " + str(idobjet) + ";"
        # print(sql)
        query = self.dbase.query(sql)
        self.dbase.commit()


class UserUI(QtGui.QWidget, FORM_CLASS2):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        self.setupUi(self)
