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
from .lamiabasedigue_photo_tool import BaseDiguePhotoTool as BasePhotoTool
from .lamiabasedigue_croquis_tool import BaseCroquisTool
import os
import datetime


class BaseDigueObservationTool(BaseObservationTool):


    def __init__(self, dbase, dialog=None, linkedtreewidget=None,gpsutil=None, parentwidget=None, parent=None):
        super(BaseDigueObservationTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)

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
        if self.dbase.variante in [None, 'Lamia']:
            if self.userwdgfield is None:
                # ****************************************************************************************
                # userui
                self.userwdgfield = UserUI()
                self.linkuserwdgfield = {'Observation': {'linkfield': 'id_observation',
                                                         'widgets': {
                                                             'datetimeobservation': self.userwdgfield.dateTimeEdit,
                                                             'nombre': self.userwdgfield.spinBox_nombre,
                                                             'longueurdes': self.userwdgfield.doubleSpinBox_longueur,
                                                             'gravite': self.userwdgfield.comboBox_urgence,

                                                             'oh_etatgeneral': self.userwdgfield.comboBox_etatgen,
                                                             'oh_etatgeneralcom': self.userwdgfield.textBrowser_etatgencom,

                                                             'oh_etatvantellerie': self.userwdgfield.comboBox_etatvantellerie,
                                                             'oh_etatvantelleriecom': self.userwdgfield.textBrowser_vanteleriecom,
                                                             'oh_etatgeniecivil': [self.userwdgfield.comboBox_etatGC,
                                                                                   self.userwdgfield.comboBox_etatGC_2],
                                                             'oh_etatgeniecivilcom': [
                                                                 self.userwdgfield.textBrowser_etatGC,
                                                                 self.userwdgfield.textBrowser_etatGC_2],
                                                             'oh_testmanoeuvre': self.userwdgfield.comboBox_manoeuvre,
                                                             'oh_testmanoeuvrecom': self.userwdgfield.textBrowser_manoeuvre,
                                                             'oh_etancheite': self.userwdgfield.checkBox_etancheite,
                                                             'oh_etancheitecom': self.userwdgfield.textBrowser__etancheite,
                                                             'oh_ecoulement': [self.userwdgfield.comboBox_envas,
                                                                               self.userwdgfield.comboBox_envas2],
                                                             'oh_ecoulementcom': [
                                                                 self.userwdgfield.textBrowser_envascom,
                                                                 self.userwdgfield.textBrowser_envascom2],

                                                             'evolution': self.userwdgfield.textEdit_evolution,
                                                             'typesuite': self.userwdgfield.comboBox_typesuite,
                                                             'commentairesuite': self.userwdgfield.textEdit_suite}},
                                         'Objet': {'linkfield': 'id_objet',
                                                   'widgets': {'commentaire': self.userwdgfield.textEdit_comm}}}

                self.userwdgfield.toolButton_calc_nb.clicked.connect(
                    lambda: self.windowdialog.showNumPad(self.userwdgfield.spinBox_nombre))
                self.userwdgfield.toolButton_longueur.clicked.connect(
                    lambda: self.windowdialog.showNumPad(self.userwdgfield.doubleSpinBox_longueur))

                # ****************************************************************************************
                # child widgets
                self.dbasechildwdgfield=[]
                # if self.parentWidget is not None:
                if self.parentWidget is None or self.parentWidget is not None and self.parentWidget.dbasetablename == 'Desordre':
                    self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(dbase=self.dbase,gpsutil=self.gpsutil, parentwidget=self)
                    self.dbasechildwdgfield = [self.propertieswdgPHOTOGRAPHIE]
                    self.propertieswdgCROQUIS = BaseCroquisTool(dbase=self.dbase, parentwidget=self)
                    self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)







        elif self.dbase.variante in ['SIRS']:
            if self.userwdgfield is None:
                # ****************************************************************************************
                # userui
                self.userwdgfield = UserUISirs()

                self.linkuserwdgfield = {'Observation' : {'linkfield' : 'id_observation',
                                                 'widgets' : {'datetimeobservation' : self.userwdgfield.dateTimeEdit,
                                                              'nombre' : self.userwdgfield.spinBox_nombre,
                                                            'gravite': self.userwdgfield.comboBox_urgence,

                                                            'oh_etatvantellerie' : self.userwdgfield.comboBox_etatvantellerie,
                                                            'oh_etatvantelleriecom': self.userwdgfield.textBrowser_vanteleriecom,
                                                              'oh_etatgeniecivil': self.userwdgfield.comboBox_etatGC,
                                                              'oh_etatgeniecivilcom': self.userwdgfield.textBrowser_etatGC,
                                                              'oh_testmanoeuvre': self.userwdgfield.comboBox_manoeuvre,
                                                              'oh_testmanoeuvrecom': self.userwdgfield.textBrowser_manoeuvre,
                                                              'oh_etancheite': self.userwdgfield.checkBox_etancheite,
                                                              'oh_etancheitecom': self.userwdgfield.textBrowser__etancheite,


                                                            'evolution': self.userwdgfield.textEdit_evolution,
                                                            'typesuite': self.userwdgfield.comboBox_typesuite,
                                                            'commentairesuite': self.userwdgfield.textEdit_suite}},
                                    'Objet' : {'linkfield' : 'id_objet',
                                              'widgets' : {'commentaire': self.userwdgfield.textEdit_comm}}}


                self.userwdgfield.toolButton_calc_nb.clicked.connect(
                    lambda: self.windowdialog.showNumPad(self.userwdgfield.spinBox_nombre))

                # ****************************************************************************************
                # child widgets
                self.dbasechildwdgfield = []
                # if self.parentWidget is not None:
                if self.parentWidget is None or self.parentWidget is not None and self.parentWidget.dbasetablename == 'Desordre':
                    self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(dbase=self.dbase, gpsutil=self.gpsutil,
                                                                   parentwidget=self)
                    self.dbasechildwdgfield = [self.propertieswdgPHOTOGRAPHIE]
                    self.propertieswdgCROQUIS = BaseCroquisTool(dbase=self.dbase, parentwidget=self)
                    self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)




    def equipementTypeChanged(self, currentindex):
        currenttext = self.parentWidget.parentWidget.userwdgfield.comboBox_type.currentText()
        if currenttext in ['Vanne', 'Clapet']:
            self.userwdgfield.stackedWidget_2.setCurrentIndex(1)
        elif currenttext in ['Exutoire']:
            self.userwdgfield.stackedWidget_2.setCurrentIndex(2)
        else :
            self.userwdgfield.stackedWidget_2.setCurrentIndex(0)

    def postInitFeatureProperties(self, feat):
        super(BaseDigueObservationTool, self).postInitFeatureProperties(feat)
        iddesordre = self.dbase.getValuesFromPk('Observation_qgis', 'lid_desordre', self.currentFeaturePK)
        if iddesordre is not None:
            sql = """
                  SELECT Equipement_now.typeequipement FROM Equipement_now, Desordre_now 
                  WHERE Desordre_now.lid_descriptionsystem = Equipement_now.id_descriptionsystem
                  AND Desordre_now.id_desordre = 
                  """
            sql+= str(iddesordre)
            sql = self.dbase.updateQueryTableNow(sql)
            res = self.dbase.query(sql)
            if len(res)>0:
                currenttext = res[0][0]
                if currenttext in ['VAN', 'CLA']:
                    self.userwdgfield.stackedWidget_2.setCurrentIndex(1)
                elif currenttext in ['EXU']:
                    self.userwdgfield.stackedWidget_2.setCurrentIndex(2)
                else :
                    self.userwdgfield.stackedWidget_2.setCurrentIndex(0)





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
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabasedigue_observation_tool_ui.ui')
        uic.loadUi(uipath, self)

class UserUISirs(QWidget):
    def __init__(self, parent=None):
        super(UserUISirs, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabasedigue_observation_tool_ui_SIRS.ui')
        uic.loadUi(uipath, self)
