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
from qgis.PyQt.QtWidgets import QWidget

from ...base3.qgswidgets.lamia_form_equipment import BaseEquipmentTool
from .lamia_form_camera import BaseUrbandrainageCameraTool
from .lamia_form_sketch import BaseUrbandrainageSketchTool
from .lamia_form_deficiency import BaseUrbandrainageDeficiencyTool


class BaseUrbandrainageEquipmentTool(BaseEquipmentTool):
    def __init__(self, **kwargs):
        super(BaseUrbandrainageEquipmentTool, self).__init__(**kwargs)

    def initMainToolWidget(self):

        if self.dbase.variante in [None, "Lamia", "2018_SNCF"]:
            self.toolwidgetmain = UserUI()
            self.formtoolwidgetconfdictmain = {
                "equipment": {
                    "linkfield": "id_equipment",
                    "widgets": {
                        "equipmentcategory": self.toolwidgetmain.comboBox_cat,
                        "sewertype": self.toolwidgetmain.comboBox_typeres,
                        "equipmenttype": self.toolwidgetmain.comboBox_typeapp,
                    },
                },
                "object": {
                    "linkfield": "id_object",
                    "widgets": {"comment": self.toolwidgetmain.textBrowser_comm},
                },
                "descriptionsystem": {
                    "linkfield": "id_descriptionsystem",
                    "widgets": {},
                },
            }
            self.toolwidgetmain.comboBox_cat.currentIndexChanged.connect(
                self.changeCategorie
            )

            # ****************************************************************************************
            # child widgets
            self.dbasechildwdgfield = []
            self.instancekwargs["parentwidget"] = self
            self.propertieswdgPHOTOGRAPHIE = BaseUrbandrainageCameraTool(
                **self.instancekwargs
            )
            self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)
            self.propertieswdgCROQUIS = BaseUrbandrainageSketchTool(
                **self.instancekwargs
            )
            self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)
        elif self.dbase.variante in ["CD41"]:
            # userui
            self.toolwidgetmain = UserUI_2()
            self.formtoolwidgetconfdictmain = {
                "equipment": {
                    "linkfield": "id_equipment",
                    "widgets": {
                        "equipmentcategory": self.toolwidgetmain.comboBox_cat,
                        "domain": self.toolwidgetmain.comboBox_domaine,
                        "location": self.toolwidgetmain.comboBox_implant,
                        "sewertype": self.toolwidgetmain.comboBox_typeres,
                        "equipmenttype": self.toolwidgetmain.comboBox_typeapp,
                        "accessibility": self.toolwidgetmain.comboBox_access,
                    },
                },
                "object": {
                    "linkfield": "id_object",
                    "widgets": {"comment": self.toolwidgetmain.textBrowser_comm},
                },
                "descriptionsystem": {
                    "linkfield": "id_descriptionsystem",
                    "widgets": {},
                },
            }
            self.toolwidgetmain.comboBox_cat.currentIndexChanged.connect(
                self.changeCategorie
            )

            # ****************************************************************************************
            # child widgets
            self.dbasechildwdgfield = []

            # self.propertieswdgDesordre = BaseAssainissementDesordreTool(dbase=self.dbase, gpsutil=self.gpsutil,
            #                                                            parentwidget=self)
            self.instancekwargs["parentwidget"] = self
            self.propertieswdgDesordre = BaseUrbandrainageDeficiencyTool(
                **self.instancekwargs
            )

            # self.propertieswdgDesordre.toolwidgetmain.frame_2.setParent(None)
            # self.propertieswdgDesordre.groupBox_elements.setParent(None)
            # self.propertieswdgDesordre.pushButton_addFeature.setEnabled(False)
            # self.propertieswdgDesordre.pushButton_delFeature.setEnabled(False)
            # self.propertieswdgDesordre.comboBox_featurelist.setEnabled(False)
            # self.propertieswdgDesordre.groupBox_geom.setParent(None)
            self.dbasechildwdgfield.append(self.propertieswdgDesordre)
            self.propertieswdgPHOTOGRAPHIE = BaseUrbandrainageCameraTool(
                **self.instancekwargs
            )
            self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)
            self.propertieswdgCROQUIS = BaseUrbandrainageSketchTool(
                **self.instancekwargs
            )
            self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

    # def postInitFeatureProperties(self, feat):
    def postSelectFeature(self):
        # if feat is None and self.comboBox_featurelist.currentText() == self.newentrytext :
        if self.currentFeaturePK is None:  # new feat
            if (
                self.parentWidget is not None
                and self.parentWidget.currentFeaturePK is not None
            ):
                if self.parentWidget.DBASETABLENAME == "node":
                    # get geom

                    noeudfetwkt = self.dbase.getValuesFromPk(
                        "node", "ST_AsText(geom)", self.parentWidget.currentFeaturePK
                    )
                    neudfetgeom = qgis.core.QgsGeometry.fromWkt(noeudfetwkt).asPoint()
                    # self.mainifacewidget.qgiscanvas.createorresetRubberband(1)
                    self.setTempGeometry([neudfetgeom, neudfetgeom], False, False)

    def postSaveFeature(self, savedfeaturepk=None):
        if self.dbase.variante in ["CD41"]:
            # save a disorder on first creation
            # if self.savingnewfeature and not self.savingnewfeatureVersion:
            if self.currentFeaturePK is None:  # very new equip, not newversion
                self.propertieswdgDesordre.toolbarNew()
                geomtext, iddessys = self.dbase.getValuesFromPk(
                    "equipment_qgis",
                    ["ST_AsText(geom)", "id_descriptionsystem"],
                    savedfeaturepk,
                )
                qgsgeom = qgis.core.QgsGeometry.fromWkt(geomtext).asPolyline()
                self.propertieswdgDesordre.setTempGeometry(qgsgeom)
                self.propertieswdgDesordre.parentWidget.currentFeaturePK = (
                    savedfeaturepk
                )
                self.propertieswdgDesordre.toolbarSave()
                pkdesordre = self.propertieswdgDesordre.currentFeaturePK
                sql = "UPDATE deficiency SET deficiencycategory = 'EQP' WHERE pk_deficiency = {}".format(
                    pkdesordre
                )
                self.dbase.query(sql)


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), "lamia_form_equipment_ui.ui")
        uic.loadUi(uipath, self)


class UserUI_2(QWidget):
    def __init__(self, parent=None):
        super(UserUI_2, self).__init__(parent=parent)
        uipath = os.path.join(
            os.path.dirname(__file__), "lamia_form_equipment_ui_CD41.ui"
        )
        uic.loadUi(uipath, self)
