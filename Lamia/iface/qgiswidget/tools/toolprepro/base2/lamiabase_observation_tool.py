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

from ...lamia_abstractformtool import AbstractLamiaFormTool

from .lamiabase_photo_tool import BasePhotoTool
from .lamiabase_croquis_tool import BaseCroquisTool
import os
import datetime


class BaseObservationTool(AbstractLamiaFormTool):

    DBASETABLENAME = 'Observation'
    # LOADFIRST = True

    tooltreewidgetCAT = 'Etat'
    tooltreewidgetSUBCAT = 'Obervation'
    tooltreewidgetICONPATH = os.path.join(os.path.dirname(__file__), 'lamiabase_observation_tool_icon.png')

    PARENTJOIN = {'Desordre' : {'colparent': 'id_desordre',
                                'colthistable': 'lid_desordre',
                                 'tctable': None,
                                 'tctablecolparent':None,
                                 'tctablecolthistable':None}
                 }
    CHOOSERTREEWDG_COLSHOW = ['datetimeobservation']

    def __init__(self, **kwargs):
        super(BaseObservationTool, self).__init__(**kwargs)
        self.instancekwargs = kwargs
    
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
    """

    def initMainToolWidget(self):

        self.toolwidgetmain = UserUI()
        self.formtoolwidgetconfdictmain = {'Observation' : {'linkfield' : 'id_observation',
                                                            'widgets' : {'datetimeobservation' : self.toolwidgetmain.dateTimeEdit,
                                                                        'nombre' : self.toolwidgetmain.spinBox_nombre,
                                                                    'gravite': self.toolwidgetmain.comboBox_urgence,
                                                                    'evolution': self.toolwidgetmain.textEdit_evolution,
                                                                    'typesuite': self.toolwidgetmain.comboBox_typesuite,
                                                                    'commentairesuite': self.toolwidgetmain.textEdit_suite}},
                                            'Objet' : {'linkfield' : 'id_objet',
                                                        'widgets' : {'commentaire': self.toolwidgetmain.textEdit_comm}}}

        self.toolwidgetmain.toolButton_calc_nb.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.spinBox_nombre))

        # ****************************************************************************************
        # child widgets
        self.dbasechildwdgfield=[]
        self.instancekwargs['parentwidget'] = self
        #if self.parentWidget is not None:
        self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(**self.instancekwargs)
        self.dbasechildwdgfield = [self.propertieswdgPHOTOGRAPHIE]
        self.propertieswdgCROQUIS = BaseCroquisTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

    """
    def postOnActivation(self):
            pass

    def postOnDesactivation(self):
        pass

    def postloadIds(self,sqlin):
        if self.parentWidget is not None and self.parentWidget.dbasetablename == 'Desordre':
            sqlin += " ORDER BY datetimeobservation DESC"
        return sqlin
    """

    # def postInitFeatureProperties(self, feat):
    def postSelectFeature(self):

        if self.currentFeaturePK is None:

            if self.parentWidget is not None and self.parentWidget.currentFeaturePK is not None:  #copy last obs text
                #parent iddesordre
                #sql = " SELECT id_desordre FROM Desordre WHERE pk_desordre = " + str(self.parentWidget.currentFeaturePK)
                #iddesordre = self.dbase.query(sql)[0][0]
                iddesordre = self.dbase.getValuesFromPk('Desordre',
                                                       'id_desordre',
                                                        self.parentWidget.currentFeaturePK)


                # SELECT pk_observation FROM Observation WHERE lk_desordre = 1 AND dateobservation = (SELECT MAX(dateobservation) FROM Observation WHERE lk_desordre = 1)
                #sql = "SELECT pk_observation FROM Observation_qgis WHERE lid_desordre = " + str(iddesordre)
                #sql += " AND datetimeobservation = (SELECT MAX(datetimeobservation) FROM Observation WHERE lid_desordre = " + str(iddesordre)
                #sql += " )"
                #sql += " AND "
                #sql += self.dbase.dateVersionConstraintSQL()
                # print(sql)
                sql = "SELECT pk_observation FROM Observation_now WHERE lid_desordre = {iddesordre}" \
                       " AND datetimeobservation = (SELECT MAX(datetimeobservation) FROM Observation_now WHERE lid_desordre = {iddesordre} )" .format(iddesordre=iddesordre)

                sql = self.dbase.sqlNow(sql)
                query = self.dbase.query(sql)
                if query:
                    result = [row[0] for row in query]
                    if len(result)>0:
                        pklastobservation = result[0]
                        dictvalues = self.formutils.getDictValuesForWidget(featurepk=pklastobservation)
                        #featobs = self.dbase.getLayerFeatureByPk('Observation',pklastobservation )
                        #print(featobs.attributes())
                        #self.initFeatureProperties(featobs)
                        self.formutils.applyResultDict(dictvalues)

            #datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            ##datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
            #self.initFeatureProperties(feat, self.dbasetablename, 'datetimeobservation', datecreation)
            datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            # self.initFeatureProperties(feat, self.dbasetablename, 'datetimeobservation', datecreation)
            self.formutils.applyResultDict({'datetimeobservation': datecreation}, checkifinforgottenfield=False)
            #applyResultDict(self, resultdict, checkifinforgottenfield=True):



        if ('groupedesordre' in self.dbase.dbasetables['Desordre']['fields'].keys()  ):
            if self.parentWidget is not None and self.parentWidget.currentFeaturePK is not None:
                #grpdes = self.parentWidget.currentFeature['groupedesordre']
                grpdes = self.dbase.getValuesFromPk(self.parentWidget.DBASETABLENAME,
                                                    'groupedesordre',
                                                    self.parentWidget.currentFeaturePK)
                if grpdes is not None:
                    grpdescst = [elem[1] for elem in self.dbase.dbasetables['Desordre']['fields']['groupedesordre']['Cst']]
                    indexgrp = grpdescst.index(grpdes)
                    try:
                        self.toolwidgetmain.stackedWidget.setCurrentIndex(indexgrp)
                    except:
                        pass


    """
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
    """



    def postSaveFeature(self, savedfeaturepk=None):
        if self.currentFeaturePK is None:   #new feature
            # Case when a observation is defined in the past
            pk_objet, datetimecreation , datetimeobservation = self.dbase.getValuesFromPk('Observation_qgis',
                                                            ['pk_objet','datetimecreation','datetimeobservation'],
                                                            savedfeaturepk)
            if isinstance(datetimecreation, str):
                datetimecreation = QtCore.QDateTime.fromString(datetimecreation, 'yyyy-MM-dd hh:mm:ss')
                datetimeobservation = QtCore.QDateTime.fromString(datetimeobservation, 'yyyy-MM-dd hh:mm:ss')
            if datetimecreation > datetimeobservation:
                sql = "UPDATE Objet SET datetimecreation = '" + str(datetimeobservation) + "'"
                sql += " WHERE pk_objet = " + str(pk_objet)
                self.dbase.query(sql)

            if self.parentWidget is not None and self.parentWidget.currentFeaturePK is not None:
                if self.parentWidget.DBASETABLENAME == 'Desordre':
                    pk_objet, datetimecreation = self.dbase.getValuesFromPk('Desordre_qgis',
                                                                                 ['pk_objet', 'datetimecreation'],
                                                                                 self.parentWidget.currentFeaturePK)
                    if isinstance(datetimecreation, str):
                        datetimecreation = QtCore.QDateTime.fromString(datetimecreation, 'yyyy-MM-dd hh:mm:ss')
                    if datetimecreation > datetimeobservation:
                        sql = "UPDATE Objet SET datetimecreation = '" + str(datetimeobservation) + "'"
                        sql += " WHERE pk_objet = " + str(pk_objet)
                        self.dbase.query(sql)


    """
    def deleteParentFeature(self):

        sql = "SELECT pk_objet FROM Observation_qgis WHERE pk_observation = " + str(self.currentFeaturePK)
        pkobjet = self.dbase.query(sql)[0][0]
        #idobjet = self.currentFeature['id_objet']
        #idressource = self.currentFeature['id_ressource']

        sql = "DELETE FROM Objet WHERE pk_objet = " + str(pkobjet)
        query = self.dbase.query(sql)
        self.dbase.commit()


        return True
    """


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabase_observation_tool_ui.ui')
        uic.loadUi(uipath, self)