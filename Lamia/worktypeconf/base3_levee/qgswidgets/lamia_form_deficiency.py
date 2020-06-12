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
import qgis
from collections import OrderedDict


from qgis.PyQt import uic, QtCore
from qgis.PyQt.QtWidgets import QWidget


from ...base3.qgswidgets.lamia_form_deficiency import BaseDeficiencyTool
from .lamia_form_observation import BaseLeveeObservationTool


class BaseLeveeDeficiencyTool(BaseDeficiencyTool):
    def __init__(self, **kwargs):
        super(BaseLeveeDeficiencyTool, self).__init__(**kwargs)

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

    def initMainToolWidget(self):

        self.toolwidgetmain = UserUI()

        self.formtoolwidgetconfdictmain = {
            "deficiency": {
                "linkfield": "id_deficiency",
                "widgets": OrderedDict(
                    [
                        ("deficiencycategory", self.toolwidgetmain.comboBox_groupedes),
                        ("side", self.toolwidgetmain.comboBox_cote),
                        ("position", self.toolwidgetmain.comboBox_position),
                        ("deficiencytype", self.toolwidgetmain.comboBox_des_cat),
                        ("deficiencysubtype", self.toolwidgetmain.comboBox_des_type),
                        (
                            "deficiencysubsubtype",
                            self.toolwidgetmain.comboBox_sstypedes,
                        ),
                    ]
                ),
            },
            "object": {"linkfield": "id_object", "widgets": {}},
        }

        self.toolwidgetmain.comboBox_groupedes.currentIndexChanged.connect(
            self.changeGroupe
        )
        # ****************************************************************************************
        # child widgets
        self.dbasechildwdgfield = []
        self.instancekwargs["parentwidget"] = self

        # if self.parentWidget is None :
        self.propertieswdgOBSERVATION = BaseLeveeObservationTool(**self.instancekwargs)
        self.propertieswdgOBSERVATION.tooltreewidgetSUBCAT = "Observation"
        self.dbasechildwdgfield.append(self.propertieswdgOBSERVATION)

        # self.propertieswdgOBSERVATION2 = BaseDigueObservationTool(dbase=self.dbase, gpsutil=self.gpsutil, parentwidget=self)
        # self.propertieswdgOBSERVATION2.NAME = None
        # self.toolwidgetmain.tabWidget.widget(0).layout().addWidget(self.propertieswdgOBSERVATION2)
        # self.dbasechildwdgfield.append(self.propertieswdgOBSERVATION2)

        # self.toolwidgetmain.tabWidget.widget(1).layout().addWidget(self.propertieswdgOBSERVATION2.propertieswdgPHOTOGRAPHIE)
        # self.toolwidgetmain.tabWidget.widget(2).layout().addWidget(self.propertieswdgOBSERVATION2.propertieswdgCROQUIS)

    # def postInitFeatureProperties(self, feat):
    def postSelectFeature(self):
        super().postSelectFeature()

        if False:
            if self.currentFeaturePK is None:
                if (
                    self.parentWidget is not None
                    and self.parentWidget.DBASETABLENAME == "Equipement"
                ):
                    combocrtindex = self.toolwidgetmain.comboBox_groupedes.findText(
                        "Equipement"
                    )
                    self.toolwidgetmain.comboBox_groupedes.setCurrentIndex(
                        combocrtindex
                    )

            if (
                self.parentWidget is not None
                and self.parentWidget.DBASETABLENAME == "Equipement"
            ):
                pass
                # categorie
                """ TODO
                if self.parentWidget.currentFeaturePK is not None :
                    sql = "SELECT Categorie FROM Equipement WHERE pk_equipement = " + str(self.parentWidget.currentFeaturePK)
                    categ = self.dbase.query(sql)[0][0]
                    if (categ == 'OUH' and self.comboBox_featurelist.count() == 0):
                        self.pushButton_addFeature.setEnabled(True)
                        pass
                    else:
                        self.pushButton_addFeature.setEnabled(False)
                        pass
                else:
                    self.pushButton_addFeature.setEnabled(False)
                    pass
                """

    def postSaveFeature(self, savedfeaturepk=None):
        # if self.savingnewfeature:
        if self.currentFeaturePK is None:
            if (
                self.parentWidget is not None
                and self.parentWidget.DBASETABLENAME == "Equipement"
            ):
                pass
                ## categorie
                # if self.parentWidget.currentFeaturePK is not None:
                #    sql = "SELECT Categorie FROM Equipement WHERE pk_equipement = " + str(self.parentWidget.currentFeaturePK)
                #    categ = self.dbase.query(sql)[0][0]
                #    if (categ == 'OUH'):
                #        #geomparent
                #        sql = " SELECT ST_AsText(geom) FROM Equipement WHERE pk_equipement = " + str()
                #        geomtxt = self.dbase.getValuesFromPk('Equipement', 'ST_AsText(geom)', str(self.parentWidget.currentFeaturePK))
                #        sql = self.dbase.createSetValueSentence('UPDATE',
                #                                              'Desordre',
                #                                              ['geom'],
                #                                              [geomtxt])
                #        sql += " WHERE pk_desordre = " + str(self.currentFeaturePK)
                #        self.dbase.query(sql)


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), "lamia_form_deficiency_ui.ui")
        uic.loadUi(uipath, self)
