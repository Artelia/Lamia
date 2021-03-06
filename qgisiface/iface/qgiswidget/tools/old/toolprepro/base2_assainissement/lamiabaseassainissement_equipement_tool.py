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
import qgis
try:
    from qgis.PyQt.QtGui import (QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget)

from ..base2.lamiabase_equipement_tool import BaseEquipementTool
from .lamiabaseassainissement_photo_tool import BaseAssainissementPhotoTool as BasePhotoTool
from .lamiabaseassainissement_croquis_tool import BaseAssainissementCroquisTool as BaseCroquisTool
from .lamiabaseassainissement_desordre_tool import BaseAssainissementDesordreTool

import os
import datetime


class BaseAssainissementEquipementTool(BaseEquipementTool):


    def __init__(self, **kwargs):
        super(BaseAssainissementEquipementTool, self).__init__(**kwargs)

    """
    def initTool(self):
        super(BaseAssainissementEquipementTool, self).initTool()
        self.LineENABLED = False
    """

    """
    def initTool(self):
        # ****************************************************************************************
        # Main spec

        self.CAT = 'Description'
        self.NAME = 'Equipement'
        self.dbasetablename = 'Equipement'
        self.PointENABLED = True
        self.LineENABLED = True
        # self.PolygonENABLED = True
        # self.magicfunctionENABLED = True
        self.linkagespec = {'Equipement': {'tabletc': None,
                                           'idsource': 'lk_equipement',
                                           'idtcsource': None,
                                           'iddest': 'id_equipement',
                                           'idtcdest': None,
                                           'desttable': ['Equipement']}}
        # self.pickTable = None
        self.debug = False
        self.iconpath = os.path.join(os.path.dirname(__file__), 'lamiadefault_equipement_tool_icon.svg')

        # ****************************************************************************************
        #properties ui
        pass
    """

    def initMainToolWidget(self):

        if self.dbase.variante in [None, 'Lamia','2018_SNCF']:
            self.toolwidgetmain = UserUI()
            self.formtoolwidgetconfdictmain = {'Equipement' : {'linkfield' : 'id_equipement',
                                                                'widgets' : {'categorie': self.toolwidgetmain.comboBox_cat,
                                                                            'typeReseau': self.toolwidgetmain.comboBox_typeres,
                                                                            'typeAppAss': self.toolwidgetmain.comboBox_typeapp
                                                                            }},
                                                'Objet' : {'linkfield' : 'id_objet',
                                                            'widgets' : {'commentaire': self.toolwidgetmain.textBrowser_comm}},
                                                'Descriptionsystem' : {'linkfield' : 'id_descriptionsystem',
                                                            'widgets' : {}}}
            self.toolwidgetmain.comboBox_cat.currentIndexChanged.connect(self.changeCategorie)


            # ****************************************************************************************
            # child widgets
            self.dbasechildwdgfield = []
            self.instancekwargs['parentwidget'] = self
            self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(**self.instancekwargs)
            self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)

            self.propertieswdgCROQUIS = BaseCroquisTool(**self.instancekwargs)
            self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

            #if self.parentWidget is None:
            #    self.pushButton_addFeature.setEnabled(False)

        elif self.dbase.variante in ['CD41']:
            # userui
            self.toolwidgetmain = UserUI_2()
            self.formtoolwidgetconfdictmain = {'Equipement': {'linkfield': 'id_equipement',
                                                    'widgets': {
                                                                'categorie': self.toolwidgetmain.comboBox_cat,
                                                                'domaine': self.toolwidgetmain.comboBox_domaine,
                                                                'environnement': self.toolwidgetmain.comboBox_implant,


                                                                'typeReseau': self.toolwidgetmain.comboBox_typeres,
                                                                'typeAppAss': self.toolwidgetmain.comboBox_typeapp,

                                                                'accessibilite': self.toolwidgetmain.comboBox_access

                                                                }},
                                     'Objet': {'linkfield': 'id_objet',
                                               'widgets': {'commentaire': self.toolwidgetmain.textBrowser_comm}},
                                     'Descriptionsystem': {'linkfield': 'id_descriptionsystem',
                                                           'widgets': {}}}
            self.toolwidgetmain.comboBox_cat.currentIndexChanged.connect(self.changeCategorie)

            # ****************************************************************************************
            # child widgets
            self.dbasechildwdgfield = []

            #self.propertieswdgDesordre = BaseAssainissementDesordreTool(dbase=self.dbase, gpsutil=self.gpsutil,
            #                                                            parentwidget=self)
            self.instancekwargs['parentwidget'] = self
            self.propertieswdgDesordre = BaseAssainissementDesordreTool(**self.instancekwargs)

            #self.propertieswdgDesordre.toolwidgetmain.frame_2.setParent(None)
            #self.propertieswdgDesordre.groupBox_elements.setParent(None)
            #self.propertieswdgDesordre.pushButton_addFeature.setEnabled(False)
            #self.propertieswdgDesordre.pushButton_delFeature.setEnabled(False)
            #self.propertieswdgDesordre.comboBox_featurelist.setEnabled(False)
            #self.propertieswdgDesordre.groupBox_geom.setParent(None)
            self.dbasechildwdgfield.append(self.propertieswdgDesordre)


            self.propertieswdgPHOTOGRAPHIE = BasePhotoTool(**self.instancekwargs)
            self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)

            self.propertieswdgCROQUIS = BaseCroquisTool(**self.instancekwargs)
            self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)



    # def postInitFeatureProperties(self, feat):
    def postSelectFeature(self):
        #if feat is None and self.comboBox_featurelist.currentText() == self.newentrytext :
        if self.currentFeaturePK is None : #new feat
            if self.parentWidget is not None and self.parentWidget.currentFeaturePK is not None:
                if self.parentWidget.DBASETABLENAME == 'Noeud':
                    # get geom
                    """
                    noeudfet = self.dbase.getLayerFeatureByPk('Noeud', self.parentWidget.currentFeaturePK)
                    neudfetgeom = noeudfet.geometry().asPoint()
                    self.createorresetRubberband(1)
                    self.setTempGeometry([neudfetgeom,neudfetgeom],False)
                    """
                    noeudfetwkt = self.dbase.getValuesFromPk('Noeud',
                                                            'ST_AsText(geom)',
                                                            self.parentWidget.currentFeaturePK)
                    neudfetgeom = qgis.core.QgsGeometry.fromWkt(noeudfetwkt).asPoint()
                    #self.mainifacewidget.qgiscanvas.createorresetRubberband(1)
                    self.setTempGeometry([neudfetgeom,neudfetgeom], False,False)

    def postSaveFeature(self, savedfeaturepk=None):
        if self.dbase.variante in ['CD41']:
            # save a disorder on first creation
            #if self.savingnewfeature and not self.savingnewfeatureVersion:
            if self.currentFeaturePK is None :  #very new equip, not newversion
                self.propertieswdgDesordre.toolbarNew()
                geomtext, iddessys = self.dbase.getValuesFromPk('Equipement_qgis',
                                                ['ST_AsText(geom)', 'id_descriptionsystem'],
                                                savedfeaturepk)
                qgsgeom = qgis.core.QgsGeometry.fromWkt(geomtext).asPolyline()
                self.propertieswdgDesordre.setTempGeometry(qgsgeom)
                self.propertieswdgDesordre.parentWidget.currentFeaturePK = savedfeaturepk
                self.propertieswdgDesordre.toolbarSave()
                pkdesordre = self.propertieswdgDesordre.currentFeaturePK
                sql = "UPDATE Desordre SET groupedesordre = 'EQP' WHERE pk_desordre = {}".format(pkdesordre)
                self.dbase.query(sql)
                if False:
                    pkobjet = self.dbase.createNewObjet()
                    lastiddesordre = self.dbase.getLastId('Desordre') + 1
                    geomtext, iddessys = self.dbase.getValuesFromPk('Equipement_qgis',
                                                                    ['ST_AsText(geom)', 'id_descriptionsystem'],
                                                                    savedfeaturepk)
                    qgsgeom = qgis.core.QgsGeometry.fromWkt(geomtext)
                    newgeom = qgis.core.QgsGeometry(qgsgeom)
                    newgeomwkt = newgeom.asWkt()

                    sql = self.dbase.createSetValueSentence(type='INSERT',
                                                            tablename='Desordre',
                                                            listoffields=['id_desordre', 'lpk_objet', 'groupedesordre',
                                                                        'lid_descriptionsystem', 'geom'],
                                                            listofrawvalues=[lastiddesordre, pkobjet, 'EQP',
                                                                            iddessys, newgeomwkt])
                    self.dbase.query(sql)



    """
    def changeCategorie(self,intcat):
        self.userwdg.stackedWidget.setCurrentIndex(intcat)


    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass



    def postInitFeatureProperties(self, feat):
        pass

    def createParentFeature(self):

        lastrevision = self.dbase.getLastPk('Revision')
        datecreation = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
        lastobjetid = self.dbase.getLastId('Objet') + 1
        sql = "INSERT INTO Objet (id_objet, id_revisionbegin, datecreation ) "
        sql += "VALUES(" + str(lastobjetid) + "," + str(lastrevision) + ",'" + datecreation + "');"
        query = self.dbase.query(sql)
        self.dbase.commit()
        # idobjet = self.dbase.getLastRowId('Objet')

        # sql = "INSERT INTO Descriptionsystem (id_objet) VALUES(" + str(idobjet) + ");"
        lastdescriptionsystemid = self.dbase.getLastId('Descriptionsystem') + 1
        sql = "INSERT INTO Descriptionsystem (id_descriptionsystem, id_revisionbegin, id_objet) "
        sql += "VALUES(" + str(lastdescriptionsystemid) + "," + str(lastrevision) + "," + str(lastobjetid) + ");"
        query = self.dbase.query(sql)
        self.dbase.commit()
        # idsys = self.dbase.getLastRowId('Descriptionsystem')

        pkequip = self.currentFeature.id()
        lastidequip = self.dbase.getLastId('Equipement') + 1

        sql = "UPDATE Equipement SET id_objet = " + str(lastobjetid) + ","
        sql += "id_descriptionsystem = " + str(lastdescriptionsystemid) + ","
        sql += "id_equipement = " + str(lastidequip) + ","
        sql += "id_revisionbegin = " + str(lastrevision)
        sql += " WHERE pk_equipement = " + str(pkequip) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()


        if self.parentWidget is not None and self.parentWidget.currentFeature is not None:
            currentparentlinkfield = self.parentWidget.currentFeature['id_descriptionsystem']
            sql = "UPDATE Equipement SET lk_descriptionsystem = " + str(currentparentlinkfield)
            sql += " WHERE pk_equipement = " + str(pkequip)
            self.dbase.query(sql)
            self.dbase.commit()


    def postSaveFeature(self, boolnewfeature):
        pass


    def deleteParentFeature(self):
        idobjet = self.currentFeature['id_objet']

        sql = "DELETE FROM Objet WHERE id_objet = " + str(idobjet) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()

        sql = "DELETE FROM Descriptionsystem WHERE id_objet = " + str(idobjet) + ";"
        query = self.dbase.query(sql)
        self.dbase.commit()

        return True


    """


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabaseassainissement_equipement_tool_ui.ui')
        uic.loadUi(uipath, self)

class UserUI_2(QWidget):
    def __init__(self, parent=None):
        super(UserUI_2, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabaseassainissement_equipement_tool_ui_CD41.ui')
        uic.loadUi(uipath, self)