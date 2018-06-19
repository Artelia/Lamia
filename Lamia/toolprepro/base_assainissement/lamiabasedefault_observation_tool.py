# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore

try:
    from qgis.PyQt.QtGui import (QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget)
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..base.lamiabase_observation_tool import BaseObservationTool
from ..base.lamiabase_photo_tool import BasePhotoTool
from ..base.lamiabase_croquis_tool import BaseCroquisTool
import os
import datetime


class BaseDefaultObservationTool(BaseObservationTool):


    def __init__(self, dbase, dialog=None, linkedtreewidget=None,gpsutil=None, parentwidget=None, parent=None):
        super(BaseDefaultObservationTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)

    """
    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Desordre'
        self.NAME = 'Observation'
        self.dbasetablename = 'Observation'
        #self.visualmode = [1, 2]
        self.visualmode = []
        # self.PointENABLED = True
        # self.LineENABLED = True
        # self.PolygonENABLED = True
        # self.magicfunctionENABLED = True
        self.linkagespec = {'Desordre' : {'tabletc' : None,
                                           'idsource' : 'lk_desordre',
                                       'idtcsource' : None,
                                           'iddest' : 'id_desordre',
                                       'idtcdest' : None,
                                           'desttable' : ['Desordre']},
                            'Marche' :{'tabletc' : None,
                                              'idsource' : 'lk_marche',
                                            'idtcsource' : None,
                                           'iddest' : 'id_marche',
                                           'idtcdest' : None,
                                           'desttable' : ['Marche']} }
        self.iconpath = os.path.join(os.path.dirname(__file__), 'lamiadefault_observation_tool_icon.png')

        # ****************************************************************************************
        #properties ui
        pass
    
    """
    def initFieldUI(self):
        # ****************************************************************************************
        # userui Desktop
        if self.userwdgfield is None:
            # ****************************************************************************************
            # userui
            self.userwdgfield = UserUI()
            self.linkuserwdgfield = {'Observation' : {'linkfield' : 'id_observation',
                                             'widgets' : {'dateobservation' : self.userwdgfield.dateEdit,
                                                          #'nombre' : self.userwdgfield.spinBox_nombre,
                                                        'gravite': self.userwdgfield.comboBox_urgence,
                                                          'depots' : self.userwdgfield.comboBox_depot,

                                                        # 'evolution': self.userwdgfield.textEdit_evolution,
                                                        'commentaires': self.userwdgfield.textEdit_comm,
                                                        'suite': self.userwdgfield.textEdit_suite,
                                                          'typesuite': self.userwdgfield.comboBox_typesuite,
                                                          'precisionsuite': self.userwdgfield.comboBox_precisionsuite,

                                                          'ECPPdepuisbranchement': self.userwdgfield.checkBox_ecpp,
                                                          'gcdegrade': self.userwdgfield.checkBox_gcdegrade,
                                                          'infiltration': self.userwdgfield.checkBox_infiltration,
                                                          'intrusionracine': self.userwdgfield.checkBox_racines,
                                                          'miseencharge': self.userwdgfield.checkBox_charge,
                                                          'tamponendommage': self.userwdgfield.checkBox_tamponendommage
                                                          }},
                                'Objet' : {'linkfield' : 'id_objet',
                                          'widgets' : {'commentaire': self.userwdgfield.textEdit_comm}}}

            self.userwdgfield.toolButton_calc_nb.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.spinBox_nombre))

            # ****************************************************************************************
            # child widgets
            self.dbasechildwdgfield=[]
            if self.parentWidget is not None:
                self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(dbase=self.dbase, parentwidget=self)
                self.dbasechildwdgfield = [self.propertieswdgPHOTOGRAPHIE]
                self.propertieswdgCROQUIS = BaseCroquisTool(dbase=self.dbase, parentwidget=self)
                self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

    """
    def postOnActivation(self):
            pass

    def postOnDesactivation(self):
        pass

    def postloadIds(self,sqlin):
        if self.parentWidget is not None and self.parentWidget.dbasetablename == 'Desordre':
            sqlin += " ORDER BY dateobservation DESC"
        return sqlin


    def postInitFeatureProperties(self, feat):
        if self.currentFeature is None:
            datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
            self.initFeatureProperties(feat, self.dbasetablename, 'dateobservation', datecreation)

        if ('groupedesordre' in self.dbase.dbasetables['Desordre']['fields'].keys()  ):
            if self.parentWidget is not None and self.parentWidget.currentFeature is not None:
                grpdes = self.parentWidget.currentFeature['groupedesordre']
                grpdescst = [elem[1] for elem in self.dbase.dbasetables['Desordre']['fields']['groupedesordre']['Cst']]
                indexgrp = grpdescst.index(grpdes)
                try:
                    self.userwdgfield.stackedWidget.setCurrentIndex(indexgrp)
                except:
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

        pkobservation = self.currentFeature.id()
        lastidobservation = self.dbase.getLastId('Observation') + 1

        sql = "UPDATE Observation SET id_objet = " + str(lastobjetid)  + ","
        sql += "id_observation = " + str(lastidobservation) + ","
        sql += "id_revisionbegin = " + str(lastrevision)
        sql += " WHERE pk_observation = " + str(pkobservation) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()

        if self.parentWidget is not None and self.parentWidget.currentFeature is not None:
            if self.parentWidget.dbasetablename == 'Desordre':
                currentparentlinkfield = self.parentWidget.currentFeature['id_desordre']
                sql = "UPDATE Observation SET lk_desordre = " + str(currentparentlinkfield) + " WHERE pk_observation = " + str(pkobservation) + ";"
                query = self.dbase.query(sql)
                self.dbase.commit()



    def postSaveFeature(self, boolnewfeature):
        pass



    def deleteParentFeature(self):
        idobjet = self.currentFeature['id_objet']

        sql = "DELETE FROM Objet WHERE id_objet = " + str(idobjet) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()

        return True

    """

class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabasedefault_observation_tool_ui.ui')
        uic.loadUi(uipath, self)
