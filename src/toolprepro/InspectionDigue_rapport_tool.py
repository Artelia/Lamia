# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore, QtGui
try:
    from qgis.PyQt.QtGui import (QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget)
from ..toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
import os
import datetime




class RapportTool(AbstractInspectionDigueTool):
    
    def __init__(self, dbase, dialog=None, linkedtreewidget=None,gpsutil=None, parentwidget=None, parent=None):
        super(RapportTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil,parentwidget, parent=parent)

    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Ressources'
        self.NAME = 'Rapport'
        self.dbasetablename = 'Rapport'
        self.visualmode = [1, 2]
        # self.PointENABLED = True
        # self.LineENABLED = True
        self.PolygonENABLED = True
        # self.magicfunctionENABLED = True
        self.linkagespec = {'Tcobjetressource' : {'tabletc' : 'Tcobjetressource',
                                           'idsource' : 'id_ressource',
                                       'idtcsource' : 'id_tcressource',
                                           'iddest' : 'id_objet',
                                       'idtcdest' : 'id_tcoobjet',
                                           'desttable' : ['Infralineaire','Equipement']},
                            'Marche': {'tabletc': None,
                                           'idsource': 'lk_marche',
                                           'idtcsource': None,
                                           'iddest': 'id_marche',
                                           'idtcdest': None,
                                           'desttable': ['Marche']}}

        # ****************************************************************************************
        #properties ui


        # ****************************************************************************************
        # userui
        self.userwdg = UserUI()
        self.userwdg.pushButton_chooseph.clicked.connect(self.choosePhoto)
        self.userwdg.pushButton_openph.clicked.connect(self.openFile)

        self.linkuserwdg = {'Rapport' : {'linkfield' : 'id_rapport',
                                         'widgets' : {}},
                            'Objet' : {'linkfield' : 'id_objet',
                                      'widgets' : {}},
                            'Ressource' : {'linkfield' : 'id_ressource',
                                      'widgets' : {'file': self.userwdg.lineEdit_file,
                                                    'description': self.userwdg.lineEdit_nom,
                                                    'dateressource': self.userwdg.dateEdit}}}

        # ****************************************************************************************
        # child widgets



    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass

    def openFile(self):
        filepath = self.completePathOfFile(self.userwdg.lineEdit_file.text())
        if filepath != '':
            os.startfile(filepath)


    def choosePhoto(self):
        file, extension = self.qfiledlg.getOpenFileNameAndFilter(None, 'Choose the file', self.dbase.imagedirectory,
                                                                 'All (*.*)', '')
        if file:
            self.userwdg.lineEdit_file.setText(os.path.normpath(file))


    def postInitFeatureProperties(self, feat):
        if self.currentFeature is None:
            datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
            self.initFeatureProperties(feat, 'Ressource', 'dateressource', datecreation)



    def createParentFeature(self):
        datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
        sql = "INSERT INTO Objet (datecreation) VALUES('" + datecreation + "');"
        query = self.dbase.query(sql)
        self.dbase.commit()
        idobjet = self.dbase.getLastRowId('Objet')

        sql = "INSERT INTO Ressource (id_objet) VALUES(" + str(idobjet) + ");"
        query = self.dbase.query(sql)
        self.dbase.commit()
        idres = self.dbase.getLastRowId('Ressource')

        idrapport = self.currentFeature.id()

        sql = "UPDATE Rapport SET id_objet = " + str(idobjet) + ",id_ressource = " + str(idres) + " WHERE id_rapport = " + str( idrapport) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()

        self.initLinkageFromGeometry('Tcobjetressource',idres)

        """
        if self.parentWidget is not None and self.parentWidget.currentFeature is not None:
            if self.parentWidget.dbasetablename == 'Prestation':
                # print(self.parentWidget.currentFeature.attributes())
                currentparentlinkfield = self.parentWidget.currentFeature['id_prestation']
                sql = "UPDATE Ressource SET lk_prestation = " + str(currentparentlinkfield) + " WHERE id_ressource = " + str(idres) + ";"
                query = self.dbase.query(sql)
                self.dbase.commit()
        """




    def postSaveFeature(self, boolnewfeature):
        pass



class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'RapportToolUser.ui')
        uic.loadUi(uipath, self)