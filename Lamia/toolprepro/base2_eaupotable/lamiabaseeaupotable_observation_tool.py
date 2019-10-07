# -*- coding: utf-8 -*-

"""
This file is part of LAMIA.

    LAMIA is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    LAMIA is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Foobar.  If not, see <https://www.gnu.org/licenses/>.

"""
"""
  * Copyright (c) 2017-2020 ARTELIA Commit <lamia@arteliagroup.com>
  * 
  * SPDX-License-Identifier: GPL-3.0-or-later
  * License-Filename: LICENSING.md
 """




from qgis.PyQt import uic, QtCore

try:
    from qgis.PyQt.QtGui import (QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget)
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ..base2.lamiabase_observation_tool import BaseObservationTool
#from ..base.lamiabase_photo_tool import BasePhotoTool
from .lamiabaseeaupotable_photo_tool import BaseEaupotablePhotoTool as BasePhotoTool
from .lamiabaseeaupotable_croquis_tool import BaseEaupotableCroquisTool as BaseCroquisTool
import os
import datetime


class BaseEaupotableObservationTool(BaseObservationTool):


    def __init__(self, dbase, dialog=None, linkedtreewidget=None,gpsutil=None, parentwidget=None, parent=None):
        super(BaseEaupotableObservationTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)

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
                                             'widgets' : {
                                                        #general
                                                        'datetimeobservation' : self.userwdgfield.dateTimeEdit,
                                                        'gravite': self.userwdgfield.comboBox_urgence,

                                                         # infra
                                                          'nombre': self.userwdgfield.spinBox_nombre,
                                                          'evolution': self.userwdgfield.textEdit_evolution,
                                                        #noeud
                                                        'etattampon' : self.userwdgfield.comboBox_etattampon,
                                                       'etatregard': self.userwdgfield.comboBox_etatregard,

                                                        #equip
                                                          'etatgeneral': [self.userwdgfield.comboBox_etatgen,
                                                                          self.userwdgfield.comboBox_etatgen2],
                                                           'indexcompteur': self.userwdgfield.spinBox_indexcompteur,


                                                        #general
                                                        'typesuite': self.userwdgfield.comboBox_typesuite,
                                                        'commentairesuite': self.userwdgfield.textEdit_suite}},
                                'Objet' : {'linkfield' : 'id_objet',
                                          'widgets' : {'commentaire': self.userwdgfield.textEdit_comm}}}

            self.userwdgfield.toolButton_calc_nb.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.spinBox_nombre))

            self.userwdgfield.toolButton_indexcompteur.clicked.connect(
                lambda: self.windowdialog.showNumPad(self.userwdgfield.spinBox_indexcompteur))

            # ****************************************************************************************
            # child widgets
            self.dbasechildwdgfield=[]
            # if self.parentWidget is not None:
            if self.parentWidget is None or self.parentWidget is not None and self.parentWidget.dbasetablename == 'Desordre':
                self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(dbase=self.dbase,gpsutil=self.gpsutil, parentwidget=self)
                self.dbasechildwdgfield = [self.propertieswdgPHOTOGRAPHIE]
                self.propertieswdgCROQUIS = BaseCroquisTool(dbase=self.dbase, parentwidget=self)
                self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)


    def postInitFeatureProperties(self, feat):
        super(BaseEaupotableObservationTool, self).postInitFeatureProperties(feat)
        self.updateObservationStackedWidget()

    def updateObservationStackedWidget(self):

        if ('groupedesordre' in self.dbase.dbasetables['Desordre']['fields'].keys()  ):
            if self.parentWidget is not None and self.parentWidget.currentFeature is not None:
                grpdes = self.parentWidget.currentFeature['groupedesordre']
                grpdescst = [elem[1] for elem in self.dbase.dbasetables['Desordre']['fields']['groupedesordre']['Cst']]
                indexgrp = grpdescst.index(grpdes)
                try:
                    self.userwdgfield.stackedWidget.setCurrentIndex(indexgrp)
                except:
                    pass
                if grpdes == 'EQP' and self.parentWidget.parentWidget is not None and self.parentWidget.parentWidget.currentFeature is not None:
                    if self.parentWidget.parentWidget.dbasetablename == 'Equipement':
                        #typenoeud = self.parentWidget.parentWidget.currentFeature['typeOuvrageAss']
                        currenttext = self.parentWidget.parentWidget.userwdgfield.comboBox_cat.currentText()
                        # typenoeud = self.parentWidget.parentWidget.currentFeature['typeOuvrageAss']
                        typeeqp = self.dbase.getConstraintRawValueFromText('Equipement', 'categorie', currenttext)

                        if typeeqp in ['VEN', 'VAN', 'VID','REG','HYD','CHL','RPC','SPE','AUT','IND']:
                            self.userwdgfield.stackedWidget_2.setCurrentIndex(0)
                        elif typeeqp in ['COM', 'DEB']:
                            self.userwdgfield.stackedWidget_2.setCurrentIndex(1)
                        else:
                            self.userwdgfield.stackedWidget_2.setCurrentIndex(2)





                if grpdes == 'NOD' and self.parentWidget.parentWidget is not None and self.parentWidget.parentWidget.currentFeature is not None:
                    if self.parentWidget.parentWidget.dbasetablename == 'Noeud':
                        #typenoeud = self.parentWidget.parentWidget.currentFeature['typeOuvrageAss']
                        currenttext = self.parentWidget.parentWidget.userwdgfield.comboBox_typeouvrage.currentText()
                        # typenoeud = self.parentWidget.parentWidget.currentFeature['typeOuvrageAss']

                        typenoeud = self.dbase.getConstraintRawValueFromText('Noeud', 'type_ouvrage', currenttext)

                        if typenoeud in ['CHE']:
                            self.userwdgfield.stackedWidget_3.setCurrentIndex(0)
                        else:
                            self.userwdgfield.stackedWidget_3.setCurrentIndex(1)


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
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabaseeaupotable_observation_tool_ui.ui')
        uic.loadUi(uipath, self)
