# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore

try:
    from qgis.PyQt.QtGui import (QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget)



from ..base.lamiabase_desordre_tool import BaseDesordreTool
from .lamiabaseassainissement_observation_tool import BaseAssainissementObservationTool


import os
import datetime
import qgis




class BaseAssainissementDesordreTool(BaseDesordreTool):

    LOADFIRST = True
    dbasetablename = 'Desordre'

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None, parentwidget=None, parent=None):
        super(BaseAssainissementDesordreTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)

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
                                           'desttable' : ['Infralineaire','Equipement','Noeud']}}


        self.pickTable = {'LkDesSys': {'TRONCON': 'IdSys'}}
        self.iconpath = os.path.join(os.path.dirname(__file__), 'lamiadefault_desordre_tool_icon.png')

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
                                             'widgets' : {'groupedesordre': self.userwdgfield.comboBox_groupedes
                                                          }},
                                'Objet' : {'linkfield' : 'id_objet',
                                          'widgets' : {}}}

            self.userwdgfield.comboBox_groupedes.currentIndexChanged.connect(self.changeGroupe)
            # ****************************************************************************************
            # child widgets
            self.dbasechildwdgfield = []
            if True:
                if self.parentWidget is None :

                    self.propertieswdgOBSERVATION = BaseAssainissementObservationTool(dbase=self.dbase, parentwidget=self)
                    self.dbasechildwdgfield.append(self.propertieswdgOBSERVATION)


                self.propertieswdgOBSERVATION2 = BaseAssainissementObservationTool(dbase=self.dbase, parentwidget=self)
                self.propertieswdgOBSERVATION2.NAME = None
                self.userwdgfield.tabWidget.widget(0).layout().addWidget(self.propertieswdgOBSERVATION2)
                self.dbasechildwdgfield.append(self.propertieswdgOBSERVATION2)

                self.userwdgfield.tabWidget.widget(1).layout().addWidget(self.propertieswdgOBSERVATION2.propertieswdgPHOTOGRAPHIE)
                self.userwdgfield.tabWidget.widget(2).layout().addWidget(self.propertieswdgOBSERVATION2.propertieswdgCROQUIS)


    """
    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass

    def magicFunction(self):
        self.featureSelected()
        self.addGPSPoint()
        self.saveFeature()
        self.propertieswdgOBSERVATION2.featureSelected()
        self.propertieswdgOBSERVATION2.saveFeature()

    def postInitFeatureProperties(self, feat):
        if feat is not None:
            self.userwdgfield.comboBox_groupedes.setEnabled(False)
        else:
            self.userwdgfield.comboBox_groupedes.setEnabled(True)


    def createParentFeature(self):
        lastrevision = self.dbase.getLastPk('Revision')
        datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
        lastobjetid = self.dbase.getLastId('Objet') + 1
        sql = "INSERT INTO Objet (id_objet, id_revisionbegin, datecreation ) "
        sql += "VALUES(" + str(lastobjetid ) + "," + str(lastrevision) +  ",'" + datecreation + "');"
        query = self.dbase.query(sql)
        self.dbase.commit()

        pkdesordre = self.currentFeature.id()
        lastiddesordre = self.dbase.getLastId('Desordre') + 1

        sql = "UPDATE Desordre SET id_objet = " + str(lastobjetid)  + ","
        sql += "id_desordre = " + str(lastiddesordre) + ","
        sql += "id_revisionbegin = " + str(lastrevision)
        sql += " WHERE pk_desordre = " + str(pkdesordre) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()

        if self.parentWidget is not None and self.parentWidget.currentFeature is not None:

            currentparentlinkfield = self.parentWidget.currentFeature['id_descriptionsystem']
            sql = "UPDATE Desordre SET lk_descriptionsystem = " + str(currentparentlinkfield)

            if self.parentWidget.dbasetablename in ['Infralineaire']:
                sql += ',groupedesordre = INF'
            elif self.parentWidget.dbasetablename in ['Noeud']:
                sql += ',groupedesordre = NOD'
            elif self.parentWidget.dbasetablename in ['Equipement']:
                sql += ',groupedesordre = EQP'
            else:
                sql += ',groupedesordre = INF'
            sql += " WHERE pk_desordre = " + str(pkdesordre)
            self.dbase.query(sql)
            self.dbase.commit()

        else:
            sql = "UPDATE Desordre SET groupedesordre = 'INF'  WHERE pk_desordre = " + str(pkdesordre)
            self.dbase.query(sql)
            self.dbase.commit()



    def postSaveFeature(self, boolnewfeature):
        pass

    """

class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabaseassainissement_desordre_tool_ui.ui')
        uic.loadUi(uipath, self)
