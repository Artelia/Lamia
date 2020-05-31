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



import os
import datetime

from qgis.PyQt import uic, QtCore
import qgis
from qgis.PyQt.QtWidgets import (QWidget)

from ..base3.lamiabase_equipment_tool import BaseEquipmentTool
from .lamiabase_levee_camera_tool import BaseLeveeCameraTool 
from .lamiabase_levee_sketch_tool import BaseLeveeSketchTool
from .lamiabase_levee_deficiency_tool import BaseLeveeDeficiencyTool
from ..subwidgets.subwidget_createsubfeature import CreateSubFeatureWidget


class BaseLeveeEquipmentTool(BaseEquipmentTool):


    def __init__(self, **kwargs):
        super(BaseLeveeEquipmentTool, self).__init__(**kwargs)



    """
    def initTool(self):
        super(BaseDigueEquipementTool,self).initTool()
        self.linkedgeom = [['Desordre', 'lid_descriptionsystem']]
    """


    def initMainToolWidget(self):

        if self.dbase.variante in [None, 'Lamia']:
            self.initMainToolWidgetLamia()
            
        elif self.dbase.variante in ['SIRS']:
            self.initMainToolWidgetSirs()
            


        self.dbasechildwdgfield = []
        self.instancekwargs['parentwidget'] = self

        self.propertieswdgDesordre = BaseLeveeDeficiencyTool(**self.instancekwargs)
        #self.propertieswdgDesordre.userwdgfield.frame_2.setParent(None)
        #self.propertieswdgDesordre.pushButton_addFeature.setEnabled(False)
        #self.propertieswdgDesordre.pushButton_delFeature.setEnabled(False)
        #self.propertieswdgDesordre.comboBox_featurelist.setEnabled(False)
        #self.propertieswdgDesordre.groupBox_geom.setParent(None)
        self.propertieswdgDesordre.SKIP_LOADING_UI = True
        self.propertieswdgDesordre.TABLEFILTERFIELD = {'deficiencycategory': 'EQP' }
        self.propertieswdgDesordre.initMainToolWidget()
        self.toolwidgetmain.comboBox_type.currentIndexChanged.connect(self.propertieswdgDesordre.propertieswdgOBSERVATION.equipementTypeChanged)
        self.dbasechildwdgfield.append(self.propertieswdgDesordre)

        self.propertieswdgPHOTOGRAPHIE = BaseLeveeCameraTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)

        self.propertieswdgCROQUIS = BaseLeveeSketchTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

        if self.parentWidget is None:
            self.propertieswdgEQUIPEMENT = BaseLeveeEquipmentTool(**self.instancekwargs)
            #self.propertieswdgEQUIPEMENT.initMainToolWidget()
            #if self.parentWidget is not None and self.parentWidget.DBASETABLENAME == 'Equipement':
            #    self.propertieswdgEQUIPEMENT.dbasechildwdgfield.remove(self.propertieswdgEQUIPEMENT.propertieswdgEQUIPEMENT)
            self.dbasechildwdgfield.append(self.propertieswdgEQUIPEMENT)

        self.createdeficiencywdg = CreateSubFeatureWidget(self,
                                                          self.propertieswdgDesordre,
                                                          condition="equipmentcategory='OUH'")
        self.lamiawidgets.append(self.createdeficiencywdg)


    def initMainToolWidgetLamia(self):
        self.toolwidgetmain = UserUI()
        self.formtoolwidgetconfdictmain = {'equipment' : {'linkfield' : 'id_equipement',
                                                        'widgets' : {'equipmentcategory': self.toolwidgetmain.comboBox_cat,
                                                                    'side': self.toolwidgetmain.comboBox_cote,
                                                                    'position': self.toolwidgetmain.comboBox_position,
                                                                    'equipmenttype': self.toolwidgetmain.comboBox_type,
                                                                    'location': self.toolwidgetmain.comboBox_implantation,
                                                                    'flowtype': self.toolwidgetmain.comboBox_ecoulement,
                                                                    'usage': self.toolwidgetmain.comboBox_utilisation,
                                                                    'height': [self.toolwidgetmain.doubleSpinBox_dimvert,
                                                                                self.toolwidgetmain.doubleSpinBox_dimvert_2],
                                                                    'width': [self.toolwidgetmain.doubleSpinBox_dimhoriz,
                                                                                self.toolwidgetmain.doubleSpinBox_dimhoriz2],

                                                                    'equipmentsubtype': self.toolwidgetmain.comboBox_soustype,
                                                                    'invert': self.toolwidgetmain.doubleSpinBox_fildeau,
                                                                    'safety': self.toolwidgetmain.comboBox_securite,


                                                                    }},
                                        'object' : {'linkfield' : 'id_object',
                                                    'widgets' : {'comment': self.toolwidgetmain.textBrowser_comm}},
                                        'descriptionsystem' : {'linkfield' : 'id_descriptionsystem',
                                                    'widgets' : {}}}

        self.toolwidgetmain.comboBox_cat.currentIndexChanged.connect(self.changeCategorie)

        self.toolwidgetmain.toolButton_calch.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_dimvert))
        self.toolwidgetmain.toolButton__calcv.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_dimhoriz))
        self.toolwidgetmain.toolButton_calch_2.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_dimvert_2))
        self.toolwidgetmain.toolButton_dimhoriz2.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_dimhoriz2))
        self.toolwidgetmain.toolButton_fildeau.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_fildeau))

        self.toolwidgetmain.comboBox_type.currentIndexChanged.connect(self.typeponctuelChanged)

    def initMainToolWidgetSirs(self):
        self.toolwidgetmain = UserUISirs()
        self.formtoolwidgetconfdictmain = {'equipment': {'linkfield': 'id_equipment',
                                                            'widgets': {'equipmentcategory': self.toolwidgetmain.comboBox_cat,
                                                                        'side': self.toolwidgetmain.comboBox_cote,
                                                                        'position': self.toolwidgetmain.comboBox_position,
                                                                        'equipmenttype': self.toolwidgetmain.comboBox_type,
                                                                        'location': self.toolwidgetmain.comboBox_implantation,
                                                                        'flowtype': self.toolwidgetmain.comboBox_ecoulement,
                                                                        'usage': self.toolwidgetmain.comboBox_utilisation,
                                                                        'height': self.toolwidgetmain.doubleSpinBox_dimvert,
                                                                        'width': self.toolwidgetmain.doubleSpinBox_dimhoriz,
                                                                        'safety': self.toolwidgetmain.comboBox_securite
                                                                        }},
                                                'object': {'linkfield': 'id_object',
                                                        'widgets': {'comment': self.toolwidgetmain.textBrowser_comm}},
                                                'descriptionsystem': {'linkfield': 'id_descriptionsystem',
                                                                    'widgets': {}}}

        self.toolwidgetmain.comboBox_cat.currentIndexChanged.connect(self.changeCategorie)

        self.toolwidgetmain.toolButton_calch.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_dimvert))
        self.toolwidgetmain.toolButton__calcv.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.doubleSpinBox_dimhoriz))

    def postSaveFeature(self, savedfeaturepk=None):

        # save a disorder on first creation
        #if self.savingnewfeature and self.savingnewfeatureVersion == False:
        if False and self.currentFeaturePK is None:
            # categorie
            #sql = "SELECT Categorie FROM Equipement WHERE pk_equipement = " + str(self.currentFeaturePK)
            #categ = self.dbase.query(sql)[0][0]
            categ = self.dbase.getValuesFromPk('Equipement',
                                                'Categorie',
                                                savedfeaturepk)

            if categ == 'OUH':
                self.propertieswdgDesordre.toolbarNew()
                geomtext = self.dbase.getValuesFromPk('Equipement_qgis',
                                                'ST_AsText(geom)',
                                                savedfeaturepk)
                try:
                    qgsgeom = qgis.core.QgsGeometry.fromWkt(geomtext).asPoint()
                    qgsgeomfordesordre = [qgsgeom,qgsgeom]
                except TypeError:
                    qgsgeom = qgis.core.QgsGeometry.fromWkt(geomtext).asPolyline()
                    qgsgeomfordesordre = qgsgeom
                self.propertieswdgDesordre.setTempGeometry(qgsgeomfordesordre)

                # self.currentFeaturePK = savedfeaturepk
                # self.propertieswdgDesordre.toolbarSave()
                # pkdesordre = self.propertieswdgDesordre.currentFeaturePK
                # sql = "UPDATE Desordre SET groupedesordre = 'EQP' WHERE pk_desordre = {}".format(pkdesordre)
                # self.dbase.query(sql)


                """
                pkobjet = self.dbase.createNewObjet()
                lastiddesordre = self.dbase.getLastId('Desordre') + 1
                geomtext, iddessys = self.dbase.getValuesFromPk('Equipement_qgis',
                                                                ['ST_AsText(geom)', 'id_descriptionsystem'],
                                                                self.currentFeaturePK)
                sql = self.dbase.createSetValueSentence(type='INSERT',
                                                        tablename='Desordre',
                                                        listoffields=['id_desordre', 'lpk_objet', 'groupedesordre',
                                                                      'lid_descriptionsystem', 'geom'],
                                                        listofrawvalues=[lastiddesordre, pkobjet, 'EQP', iddessys,
                                                                         geomtext])
                self.dbase.query(sql)
                """

    def typeponctuelChanged(self, comboindex):
        if self.toolwidgetmain.comboBox_type.currentText() in ['Clapet', 'Vanne', 'Exutoire']:
            self.toolwidgetmain.stackedWidget_2.setCurrentIndex(0)
        else:
            self.toolwidgetmain.stackedWidget_2.setCurrentIndex(1)

    def changeCategorie(self,intcat):
        if 'Ponctuel' in self.toolwidget.comboBox_cat.currentText():
            self.toolwidget.stackedWidget.setCurrentIndex(1)
            #self.pushButton_addPoint.setEnabled(True)
            #self.pushButton_addLine.setEnabled(False)




        elif 'Lineaire' in self.toolwidget.comboBox_cat.currentText():
            self.toolwidget.stackedWidget.setCurrentIndex(0)
            #self.pushButton_addPoint.setEnabled(False)
            #self.pushButton_addLine.setEnabled(True)
        else:
            pass
            #self.pushButton_addPoint.setEnabled(False)
            #self.pushButton_addLine.setEnabled(False)


    """
    def postInitFeatureProperties(self, feat):
        pass
        if False:
            print(self.propertieswdgDesordre.comboBox_featurelist.count())
            if feat is not None and self.currentFeature['categorie'] == 'OUH' and self.propertieswdgDesordre.comboBox_featurelist.count() == 0:
                print('tt')
                self.propertieswdgDesordre.pushButton_addFeature.setEnabled(True)
            else:
                print('ff')
                self.propertieswdgDesordre.pushButton_addFeature.setEnabled(False)
    """



    """
    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
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
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabase_levee_equipment_tool_ui.ui')
        uic.loadUi(uipath, self)

class UserUISirs(QWidget):
    def __init__(self, parent=None):
        super(UserUISirs, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabase_levee_equipment_tool_ui_SIRS.ui')
        uic.loadUi(uipath, self)