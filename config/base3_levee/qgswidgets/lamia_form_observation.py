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
from qgis.PyQt.QtWidgets import QWidget

from ...base3.qgswidgets.lamia_form_observation import BaseObservationTool
from .lamia_form_camera import BaseLeveeCameraTool
from .lamia_form_sketch import BaseLeveeSketchTool


class BaseLeveeObservationTool(BaseObservationTool):

    tooltreewidgetSUBCAT = None

    def __init__(self, **kwargs):
        super(BaseLeveeObservationTool, self).__init__(**kwargs)

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

    def initMainToolWidget(self):
        # ****************************************************************************************
        # userui Desktop
        self.toolwidgetmain = UserUI()
        self.formtoolwidgetconfdictmain = {
            "observation": {
                "linkfield": "id_observation",
                "widgets": {
                    "datetimeobservation": self.toolwidgetmain.datetimeobservation,
                    "number": self.toolwidgetmain.number,
                    "specificlenght": self.toolwidgetmain.specificlenght,
                    "gravity": self.toolwidgetmain.gravity,
                    "conditionglobal": self.toolwidgetmain.conditionglobal,
                    "conditionglobalcom": self.toolwidgetmain.conditionglobalcom,
                    "oh_etatvantellerie": self.toolwidgetmain.oh_etatvantellerie,
                    "oh_etatvantelleriecom": self.toolwidgetmain.oh_etatvantelleriecom,
                    "eqconditioncivilwork": [
                        self.toolwidgetmain.eqconditioncivilwork,
                        self.toolwidgetmain.eqconditioncivilwork_2,
                    ],
                    "eqconditioncivilworkcom": [
                        self.toolwidgetmain.eqconditioncivilworkcom,
                        self.toolwidgetmain.eqconditioncivilworkcom_2,
                    ],
                    "eqhandlingtest": self.toolwidgetmain.eqhandlingtest,
                    "eqhandlingtestcom": self.toolwidgetmain.eqhandlingtestcom,
                    "eqconditionsealing": self.toolwidgetmain.eqconditionsealing,
                    "eqconditionsealingcom": self.toolwidgetmain.eqconditionsealingcom,
                    "eqconditionsedimentation": [
                        self.toolwidgetmain.eqconditionsedimentation,
                        self.toolwidgetmain.eqconditionsedimentation_2,
                    ],
                    "eqconditionsedimentationcom": [
                        self.toolwidgetmain.eqconditionsedimentationcom,
                        self.toolwidgetmain.eqconditionsedimentationcom_2,
                    ],
                    "progression": self.toolwidgetmain.progression,
                    "nextactiontype": self.toolwidgetmain.nextactiontype,
                    "nextactioncomment": self.toolwidgetmain.nextactioncomment,
                },
            },
            "object": {
                "linkfield": "id_object",
                "widgets": {"comment": self.toolwidgetmain.comment},
            },
        }

        self.toolwidgetmain.toolButton_calc_nb.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.number)
        )
        self.toolwidgetmain.toolButton_longueur.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.specificlenght)
        )

        # ****************************************************************************************
        # child widgets
        self.dbasechildwdgfield = []
        self.instancekwargs["parentwidget"] = self
        # if self.parentWidget is not None:
        # if self.parentWidget is None or self.parentWidget is not None and self.parentWidget.dbasetablename == 'Desordre':
        self.propertieswdgPHOTOGRAPHIE = BaseLeveeCameraTool(**self.instancekwargs)
        self.dbasechildwdgfield = [self.propertieswdgPHOTOGRAPHIE]
        self.propertieswdgCROQUIS = BaseLeveeSketchTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

        if self.dbase.variante in ["SIRS"]:
            self.toolwidgetmain.toolButton_longueur.setEnabled(False)
            self.toolwidgetmain.specificlenght.setEnabled(False)
            self.toolwidgetmain.nextactiontype.setEnabled(False)
            self.toolwidgetmain.comment.setEnabled(False)

            """
            self.toolwidgetmain = UserUISirs()

            self.formtoolwidgetconfdictmain = {
                "observation": {
                    "linkfield": "id_observation",
                    "widgets": {
                        "datetimeobservation": self.toolwidgetmain.dateTimeEdit,
                        "number": self.toolwidgetmain.spinBox_nombre,
                        "gravity": self.toolwidgetmain.comboBox_urgence,
                        "oh_etatvantellerie": self.toolwidgetmain.comboBox_etatvantellerie,
                        "oh_etatvantelleriecom": self.toolwidgetmain.textBrowser_vanteleriecom,
                        "eqconditioncivilwork": self.toolwidgetmain.comboBox_etatGC,
                        "eqconditioncivilworkcom": self.toolwidgetmain.textBrowser_etatGC,
                        "eqhandlingtest": self.toolwidgetmain.comboBox_manoeuvre,
                        "eqhandlingtestcom": self.toolwidgetmain.textBrowser_manoeuvre,
                        "eqconditionsealing": self.toolwidgetmain.checkBox_etancheite,
                        "eqconditionsealingcom": self.toolwidgetmain.textBrowser__etancheite,
                        "progression": self.toolwidgetmain.textEdit_evolution,
                        "nextactiontype": self.toolwidgetmain.comboBox_typesuite,
                        "nextactioncomment": self.toolwidgetmain.textEdit_suite,
                    },
                },
                "object": {
                    "linkfield": "id_object",
                    "widgets": {"comment": self.toolwidgetmain.textEdit_comm},
                },
            }

            self.toolwidgetmain.toolButton_calc_nb.clicked.connect(
                lambda: self.showNumPad(self.toolwidgetmain.spinBox_nombre)
            )

            # ****************************************************************************************
            # child widgets
            self.dbasechildwdgfield = []
            self.instancekwargs["parentwidget"] = self
            # if self.parentWidget is not None:
            # if self.parentWidget is None or self.parentWidget is not None and self.parentWidget.dbasetablename == 'Desordre':
            self.propertieswdgPHOTOGRAPHIE = BaseLeveeCameraTool(**self.instancekwargs)
            self.dbasechildwdgfield = [self.propertieswdgPHOTOGRAPHIE]
            self.propertieswdgCROQUIS = BaseLeveeSketchTool(**self.instancekwargs)
            self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)
            """

    def equipementTypeChanged(self, currentindex):
        if self.toolwidgetmain is None:
            return
        currenttext = (
            self.parentWidget.parentWidget.toolwidgetmain.equipmenttype.currentText()
        )
        currentval = self.dbase.getConstraintRawValueFromText(
            "equipment", "equipmenttype", currenttext
        )

        if currentval in ["VAN", "CLA"]:
            self.toolwidgetmain.stackedWidget_2.setCurrentIndex(1)
        elif currentval in ["EXU"]:
            self.toolwidgetmain.stackedWidget_2.setCurrentIndex(2)
        else:
            self.toolwidgetmain.stackedWidget_2.setCurrentIndex(0)

    # def postInitFeatureProperties(self, feat):
    def postSelectFeature(self):
        super().postSelectFeature()
        if self.currentFeaturePK is not None:
            iddesordre = self.dbase.getValuesFromPk(
                "observation_qgis", "lid_deficiency", self.currentFeaturePK
            )
            if iddesordre is not None:
                sql = f"""
                        SELECT equipment_now.equipmenttype FROM equipment_now, deficiency_now 
                        WHERE deficiency_now.lid_descriptionsystem = equipment_now.id_descriptionsystem
                        AND deficiency_now.id_deficiency = {iddesordre}
                        """
                # sql+= str(iddesordre)
                sql = self.dbase.updateQueryTableNow(sql)
                res = self.dbase.query(sql)
                if res and len(res) > 0:
                    currenttext = res[0][0]
                    if currenttext in ["VAN", "CLA"]:
                        self.toolwidgetmain.stackedWidget_2.setCurrentIndex(1)
                    elif currenttext in ["EXU"]:
                        self.toolwidgetmain.stackedWidget_2.setCurrentIndex(2)
                    else:
                        self.toolwidgetmain.stackedWidget_2.setCurrentIndex(0)


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), "lamia_form_observation_ui.ui")
        uic.loadUi(uipath, self)


"""
class UserUISirs(QWidget):
    def __init__(self, parent=None):
        super(UserUISirs, self).__init__(parent=parent)
        uipath = os.path.join(
            os.path.dirname(__file__), "lamia_form_observation_ui_SIRS.ui"
        )
        uic.loadUi(uipath, self)
"""
