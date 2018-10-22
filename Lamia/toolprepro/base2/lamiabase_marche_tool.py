# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore

try:
    from qgis.PyQt.QtGui import (QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget)
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ...toolabstract.Lamia_abstract_tool import AbstractLamiaTool


from .lamiabase_rapport_tool import BaseRapportTool
from .lamiabase_photo_tool import BasePhotoTool
from .lamiabase_topographie_tool import BaseTopographieTool
# from .lamia_ressource_tool import AbstractRessourceTool



import os
import datetime



class BaseMarcheTool(AbstractLamiaTool):

    LOADFIRST = False
    dbasetablename = 'Marche'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(BaseMarcheTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)

    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Gestion'
        self.NAME = 'Marche'
        self.dbasetablename = 'Marche'
        # self.visualmode = [0, 1, 2]
        # self.PointENABLED = True
        # self.LineENABLED = True
        # self.PolygonENABLED = True
        # self.magicfunctionENABLED = True
        self.linkagespec = {'Tcobjetintervenant' : {'tabletc' : 'Tcobjetintervenant',
                                              'idsource' : 'id_objet',
                                            'idtcsource' : 'id_tcobjet',
                                           'iddest' : 'id_intervenant',
                                           'idtcdest' : 'id_tcintervenant',
                                           'desttable' : ['Intervenant']}
                                            }
        # self.pickTable = None
        self.iconpath = os.path.join(os.path.dirname(__file__), 'lamiabase_marche_tool_icon.png')

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
            self.linkuserwdgfield = {'Marche' : {'linkfield' : 'id_marche',
                                             'widgets' : {
                                                          'datemarche' : self.userwdgfield.dateEdit_date}},
                                'Objet' : {'linkfield' : 'id_objet',
                                          'widgets' : {'libelle': self.userwdgfield.lineEdit_nom}}}
            self.userwdgfield.pushButton_currentPrestation.clicked.connect(self.defineCurrentPrestation)
            self.userwdgfield.pushButton_defineinter.clicked.connect(self.manageLinkage)

            # ****************************************************************************************
            # child widgets
            self.dbasechildwdgfield = []
            self.propertieswdgRAPPORT = BaseRapportTool(dbase=self.dbase, parentwidget=self)
            self.dbasechildwdgfield.append(self.propertieswdgRAPPORT)

            self.propertieswdgPHOTO = BasePhotoTool(dbase=self.dbase, parentwidget=self)
            self.dbasechildwdgfield.append(self.propertieswdgPHOTO)

            self.propertieswdgTOPOGRAPHIE = BaseTopographieTool(dbase=self.dbase, parentwidget=self)
            self.dbasechildwdgfield.append(self.propertieswdgTOPOGRAPHIE)



    def defineCurrentPrestation(self):
        self.windowdialog.currentprestationlabel.setText('Prestation : ' + str(self.currentFeature.id()) + " - " +str(self.currentFeature['nommarche'] ))
        self.dbase.currentprestationid = self.currentFeature.id()



    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass


    def postInitFeatureProperties(self, feat):
        if self.currentFeature is None:
            datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
            self.initFeatureProperties(feat, self.dbasetablename, 'datemarche', datecreation)
        else:
            sql = "SELECT Tcobjetintervenant.fonction, Intervenant.nom,Intervenant.societe  FROM Tcobjetintervenant "
            sql += " INNER JOIN Intervenant ON Tcobjetintervenant.id_tcintervenant = Intervenant.id_intervenant "
            sql += "WHERE id_tcobjet = " + str(self.currentFeature['id_objet'])
            query = self.dbase.query(sql)
            result = "\n".join([str(row) for row in query])
            self.userwdg.textBrowser_intervenants.clear()
            self.userwdg.textBrowser_intervenants.append(result)


    def createParentFeature(self):
        pkobjet = self.dbase.createNewObjet()

        if False:


            datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            lastobjetid = self.dbase.getLastId('Objet') + 1
            sql = "INSERT INTO Objet (id_objet, lpk_revision_begin, datetimecreation ) "
            sql += "VALUES(" + str(lastobjetid) + "," + str(self.dbase.maxrevision) + ",'" + datecreation + "');"
            query = self.dbase.query(sql)
            self.dbase.commit()
            pkobjet = self.dbase.getLastRowId('Objet')



        pkmarche= self.currentFeaturePK
        lastidmarche = self.dbase.getLastId('Marche') + 1


        sql = "UPDATE Marche SET id_marche = " + str(lastidmarche) + ","
        sql += "lpk_objet = " + str(pkobjet)
        sql += " WHERE pk_marche = " + str(pkmarche) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()






    def postSaveFeature(self, boolnewfeature):
        pass


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabase_marche_tool_ui.ui')
        uic.loadUi(uipath, self)