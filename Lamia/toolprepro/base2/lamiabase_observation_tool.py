# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtCore

try:
    from qgis.PyQt.QtGui import (QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget)
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ...toolabstract.Lamia_abstract_tool import AbstractLamiaTool

from .lamiabase_photo_tool import BasePhotoTool
from .lamiabase_croquis_tool import BaseCroquisTool
import os
import datetime


class BaseObservationTool(AbstractLamiaTool):


    def __init__(self, dbase, dialog=None, linkedtreewidget=None,gpsutil=None, parentwidget=None, parent=None):
        super(BaseObservationTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)
        
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
                                           'idsource' : 'lid_desordre',
                                       'idtcsource' : None,
                                           'iddest' : 'id_desordre',
                                       'idtcdest' : None,
                                           'desttable' : ['Desordre']},
                            'Marche' :{'tabletc' : None,
                                              'idsource' : 'lid_marche',
                                            'idtcsource' : None,
                                           'iddest' : 'id_marche',
                                           'idtcdest' : None,
                                           'desttable' : ['Marche']} }
        self.iconpath = os.path.join(os.path.dirname(__file__), 'lamiabase_observation_tool_icon.png')

        # ****************************************************************************************
        #properties ui
        pass

    def initFieldUI(self):
        # ****************************************************************************************
        # userui Desktop
        if self.userwdgfield is None:
            # ****************************************************************************************
            # userui
            self.userwdgfield = UserUI()
            self.linkuserwdgfield = {'Observation' : {'linkfield' : 'id_observation',
                                             'widgets' : {'datetimeobservation' : self.userwdgfield.dateTimeEdit,
                                                          'nombre' : self.userwdgfield.spinBox_nombre,
                                                        'gravite': self.userwdgfield.comboBox_urgence,
                                                        'evolution': self.userwdgfield.textEdit_evolution,
                                                        'typesuite': self.userwdgfield.comboBox_typesuite,
                                                        'commentairesuite': self.userwdgfield.textEdit_suite}},
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


    def postOnActivation(self):
            pass

    def postOnDesactivation(self):
        pass

    def postloadIds(self,sqlin):
        if self.parentWidget is not None and self.parentWidget.dbasetablename == 'Desordre':
            sqlin += " ORDER BY datetimeobservation DESC"
        return sqlin


    def postInitFeatureProperties(self, feat):

        if self.currentFeature is None:

            if self.parentWidget is not None and self.parentWidget.currentFeature is not None:  #copy last obs text
                #parent iddesordre
                sql = " SELECT id_desordre FROM Desordre WHERE pk_desordre = " + str(self.parentWidget.currentFeaturePK)
                iddesordre = self.dbase.query(sql)[0][0]

                # SELECT pk_observation FROM Observation WHERE lk_desordre = 1 AND dateobservation = (SELECT MAX(dateobservation) FROM Observation WHERE lk_desordre = 1)
                sql = "SELECT pk_observation FROM Observation_qgis WHERE lid_desordre = " + str(iddesordre)
                sql += " AND datetimeobservation = (SELECT MAX(datetimeobservation) FROM Observation WHERE lid_desordre = " + str(iddesordre)
                sql += " )"
                sql += " AND "
                sql += self.dbase.dateVersionConstraintSQL()
                # print(sql)
                query = self.dbase.query(sql)
                result = [row[0] for row in query]
                if len(result)>0:
                    pklastobservation = result[0]
                    featobs = self.dbase.getLayerFeatureByPk('Observation',pklastobservation )
                    #print(featobs.attributes())
                    self.initFeatureProperties(featobs)

            datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            #datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
            self.initFeatureProperties(feat, self.dbasetablename, 'datetimeobservation', datecreation)



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
        pkobjet = self.dbase.createNewObjet()

        if False:


            # lastrevision = self.dbase.maxrevision
            # datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
            datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            lastobjetid = self.dbase.getLastId('Objet') + 1
            sql = "INSERT INTO Objet (id_objet, lpk_revision_begin, datetimecreation ) "
            sql += "VALUES(" + str(lastobjetid) + "," + str(self.dbase.maxrevision) + ",'" + datecreation + "');"
            query = self.dbase.query(sql)
            self.dbase.commit()
            pkobjet = self.dbase.getLastRowId('Objet')


        # idnoeud = self.currentFeature.id()
        pkobs = self.currentFeaturePK
        lastidobs = self.dbase.getLastId('Observation') + 1
        sql = "UPDATE Observation SET id_observation = " + str(lastidobs) + ","
        sql += "lpk_objet = " + str(pkobjet)
        sql += " WHERE pk_observation = " + str(pkobs) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()

        if self.parentWidget is not None and self.parentWidget.currentFeature is not None:

            if self.parentWidget.dbasetablename == 'Desordre':
                #currentparentlinkfield = self.parentWidget.currentFeature['id_desordre']
                #parent iddesordre
                sql = " SELECT id_desordre FROM Desordre WHERE pk_desordre = " + str(self.parentWidget.currentFeaturePK)
                iddesordre = self.dbase.query(sql)[0][0]

                sql = "UPDATE Observation SET lid_desordre = " + str(iddesordre)
                sql += " WHERE pk_observation = " + str(self.currentFeaturePK)
                query = self.dbase.query(sql)
                self.dbase.commit()




    def postSaveFeature(self, boolnewfeature):
        pass



    def deleteParentFeature(self):


        sql = "SELECT pk_objet FROM Observation_qgis WHERE pk_observation = " + str(self.currentFeaturePK)
        pkobjet = self.dbase.query(sql)[0][0]
        #idobjet = self.currentFeature['id_objet']
        #idressource = self.currentFeature['id_ressource']

        sql = "DELETE FROM Objet WHERE pk_objet = " + str(pkobjet)
        query = self.dbase.query(sql)
        self.dbase.commit()


        return True



class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabase_observation_tool_ui.ui')
        uic.loadUi(uipath, self)