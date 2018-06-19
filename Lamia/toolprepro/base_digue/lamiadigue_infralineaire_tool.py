# -*- coding: utf-8 -*-
"""


import datetime
import logging
import time
debugtime = False
"""

from qgis.PyQt import uic, QtCore, QtGui

try:
    from qgis.PyQt.QtGui import (QWidget, QLabel, QFrame)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget, QLabel, QFrame)
import os
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..default.lamiadefault_infralineaire_tool import DefaultInfraLineaireTool

from ..default.lamiadefault_photos_tool import DefaultPhotosTool
from ..default.lamiadefault_croquis_tool import DefaultCroquisTool




class DefaultBaseInfraLineaireTool(DefaultInfraLineaireTool):


    LOADFIRST = True
    dbasetablename = 'Infralineaire'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(DefaultInfraLineaireTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)

    """
    def initTool(self):
        # ****************************************************************************************
        # Main spec
        timestart = time.clock()
        if debugtime: logging.getLogger('Lamia').debug('Start init %s',str(round(time.clock() - timestart, 3)))

        self.CAT = 'Description'
        self.NAME = 'Troncon'
        self.dbasetablename = 'Infralineaire'
        # self.visualmode = [0, 1, 2]
        # self.PointEnabled = True
        self.LineENABLED = True
        # self.PolygonEnabled = True
        # self.magicfunctionENABLED = True
        self.linkagespec = {'Tcobjetintervenant' : {'tabletc' : 'Tcobjetintervenant',
                                              'idsource' : 'id_objet',
                                            'idtcsource' : 'id_tcobjet',
                                           'iddest' : 'id_intervenant',
                                           'idtcdest' : 'id_tcintervenant',
                                           'desttable' : ['Intervenant']}
                                            }
        self.pickTable = {'LkZoneGeo': {'ZONEGEO': 'ID'}}
        self.debug = False
        self.qtreewidgetfields = ['revisionbegin']

        self.iconpath = os.path.join(os.path.dirname(__file__), 'lamiadefault_infralineaire_tool_icon.svg')


        # ****************************************************************************************
        #properties ui
        pass


    
    """
    def initFieldUI(self):
        # ****************************************************************************************
        #   userui Field
        if self.userwdgfield is None:
            self.userwdgfield = UserUIField()

            self.linkuserwdgfield = {'Infralineaire': {'linkfield': 'id_infralineaire',
                                                       'widgets': {'infracommentaire':self.userwdgfield.textBrowser_commentaire}},
                                     'Objet': {'linkfield': 'id_objet',
                                               'widgets': {'libelle': self.userwdgfield.lineEdit_nom}},
                                     'Descriptionsystem': {'linkfield': 'id_descriptionsystem',
                                                           'widgets': {}}}

            self.dbasechildwdgfield = []

            self.propertieswdgPHOTOGRAPHIE = DefaultPhotosTool(dbase=self.dbase, gpsutil=self.gpsutil, parentwidget=self)
            self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)


            self.propertieswdgCROQUIS = DefaultCroquisTool(dbase=self.dbase, parentwidget=self)
            self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)
    """
    
    
    

    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass

    def postloadIds(self,sqlin):
        strid = 'id_' + self.dbasetablename.lower()
        sqlin += ' ORDER BY ' + strid
        return sqlin



    def postInitFeatureProperties(self, feat):
        debug = False
        if debug: logging.getLogger("Lamia").debug('Start ')

        pass


    def createParentFeature(self):
        lastrevision = self.dbase.getLastPk('Revision')
        datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
        lastobjetid = self.dbase.getLastId('Objet') + 1
        sql = "INSERT INTO Objet (id_objet, id_revisionbegin, datecreation ) "
        sql += "VALUES(" + str(lastobjetid ) + "," + str(lastrevision) +  ",'" + datecreation + "');"
        query = self.dbase.query(sql)
        self.dbase.commit()
        #idobjet = self.dbase.getLastRowId('Objet')



        #sql = "INSERT INTO Descriptionsystem (id_objet) VALUES(" + str(idobjet) + ");"
        lastdescriptionsystemid = self.dbase.getLastId('Descriptionsystem') + 1
        sql = "INSERT INTO Descriptionsystem (id_descriptionsystem, id_revisionbegin, id_objet) "
        sql += "VALUES(" + str(lastdescriptionsystemid) + "," + str(lastrevision) +  "," + str(lastobjetid) + ");"
        query = self.dbase.query(sql)
        self.dbase.commit()
        #idsys = self.dbase.getLastRowId('Descriptionsystem')

        idtroncon = self.currentFeature.id()
        lastidinfralineaire = self.dbase.getLastId('Infralineaire') + 1



        sql = "UPDATE Infralineaire SET id_objet = " + str(lastobjetid)  + ","
        sql += "id_descriptionsystem = " + str(lastdescriptionsystemid)   + ","
        sql += "id_infralineaire = " + str(lastidinfralineaire)  + ","
        sql += "id_revisionbegin = " + str(lastrevision)
        sql += " WHERE pk_infralineaire = " + str(idtroncon) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()


    def deleteParentFeature(self):
        idobjet = self.currentFeature['id_objet']
        idinfralin= self.currentFeature['id_infralineaire']


        sql = "DELETE FROM Objet WHERE id_objet = " + str(idobjet) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()

        sql = "DELETE FROM Descriptionsystem WHERE id_objet = " + str(idobjet) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()

        sql = "DELETE FROM Infralinemprise WHERE lk_infralineaire = " + str(idinfralin) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()

        return True

    """


class UserUIField(QWidget):
    def __init__(self, parent=None):
        super(UserUIField, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiadigue_infralineaire_tool_ui.ui')
        uic.loadUi(uipath, self)

