# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore, QtGui
try:
    from qgis.PyQt.QtGui import (QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget)
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ...toolabstract.Lamia_abstract_tool import AbstractLamiaTool
import os
import datetime




class BaseRapportTool(AbstractLamiaTool):

    LOADFIRST = False
    dbasetablename = 'Rapport'
    specialfieldui = []

    def __init__(self, dbase, dialog=None, linkedtreewidget=None,gpsutil=None, parentwidget=None, parent=None):
        super(BaseRapportTool, self).__init__(dbase, dialog, linkedtreewidget, gpsutil,parentwidget, parent=parent)

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
                                       'idtcdest' : 'id_tcobjet',
                                           'desttable' : ['Infralineaire','Equipement']},
                            'Marche': {'tabletc': None,
                                           'idsource': 'lk_marche',
                                           'idtcsource': None,
                                           'iddest': 'id_marche',
                                           'idtcdest': None,
                                           'desttable': ['Marche']}}

        # ****************************************************************************************
        #properties ui
        self.iconpath = os.path.join(os.path.dirname(__file__), 'lamiabase_rapport_tool_icon.png')
        self.qtreewidgetfields = ['libelle']

    def initDesktopUI(self):
        # ****************************************************************************************
        # userui Desktop
        if self.userwdgdesktop is None:
            # ****************************************************************************************
            # userui
            self.userwdgdesktop = UserUI()
            self.userwdgdesktop.pushButton_chooseph.clicked.connect(self.choosePhoto)
            self.userwdgdesktop.pushButton_openph.clicked.connect(self.openFile)

            self.linkuserwdgdesktop = {'Rapport' : {'linkfield' : 'id_rapport',
                                             'widgets' : { }},
                                'Objet' : {'linkfield' : 'id_objet',
                                          'widgets' : {'libelle' : self.userwdgdesktop.lineEdit_nom}},
                                'Ressource' : {'linkfield' : 'id_ressource',
                                          'widgets' : {'file': self.userwdgdesktop.lineEdit_file,
                                                        'description': self.userwdgdesktop.lineEdit_description,
                                                        'dateressource': self.userwdgdesktop.dateEdit}}}

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
        file, extension = self.windowdialog.qfiledlg.getOpenFileNameAndFilter(None, 'Choose the file', self.dbase.imagedirectory,
                                                                 'All (*.*)', '')
        if file:
            self.userwdg.lineEdit_file.setText(os.path.normpath(file))


    def postInitFeatureProperties(self, feat):
        if self.currentFeature is None:
            datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
            self.initFeatureProperties(feat, 'Ressource', 'dateressource', datecreation)



    def createParentFeature(self):
        pkobjet = self.dbase.createNewObjet()

        if False:



            # lastrevision = self.dbase.maxrevision
            datecreation =  str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            lastobjetid = self.dbase.getLastId('Objet') + 1
            sql = "INSERT INTO Objet (id_objet, lpk_revision_begin, datetimecreation ) "
            sql += "VALUES(" + str(lastobjetid ) + "," + str(self.dbase.maxrevision) +  ",'" + datecreation + "');"
            query = self.dbase.query(sql)
            self.dbase.commit()
            pkobjet = self.dbase.getLastRowId('Objet')

        lastressourceid = self.dbase.getLastId('Ressource') + 1
        sql = "INSERT INTO Ressource (id_ressource, lpk_objet) "
        sql += "VALUES(" + str(lastressourceid) +   "," + str(pkobjet) + ");"
        query = self.dbase.query(sql)
        self.dbase.commit()
        pkres = self.dbase.getLastRowId('Ressource')

        pkrapport = self.currentFeaturePK
        lastidrapport = self.dbase.getLastId('Rapport') + 1
        sql = "UPDATE Rapport SET id_rapport = " + str(lastidrapport)  + ","
        sql += "lpk_ressource = " + str(pkres)
        sql += " WHERE pk_rapport = " + str(pkrapport)
        query = self.dbase.query(sql)
        self.dbase.commit()









    def postSaveFeature(self, boolnewfeature):
        pass



class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabase_rapport_tool_ui.ui')
        uic.loadUi(uipath, self)