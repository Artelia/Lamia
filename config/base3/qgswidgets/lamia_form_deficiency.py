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

from qgis.PyQt import uic, QtCore
from qgis.PyQt.QtWidgets import QWidget

from Lamia.qgisiface.iface.qgiswidget.tools.lamia_abstractformtool import (
    AbstractLamiaFormTool,
)
from .lamia_form_observation import BaseObservationTool

base3 = QtCore.QObject()


class BaseDeficiencyTool(AbstractLamiaFormTool):

    PREPROTOOLNAME = "deficiency"
    DBASETABLENAME = "deficiency"
    LOADFIRST = True

    tooltreewidgetCAT = QtCore.QCoreApplication.translate("base3", "Condition")
    tooltreewidgetSUBCAT = QtCore.QCoreApplication.translate("base3", "Deficiency")
    tooltreewidgetICONPATH = os.path.join(
        os.path.dirname(__file__), "lamia_form_deficiency_icon.png"
    )

    tempparentjoin = {}
    linkdict = {
        "colparent": "id_descriptionsystem",
        "colthistable": "lid_descriptionsystem",
        "tctable": None,
        "tctablecolparent": None,
        "tctablecolthistable": None,
    }
    for tablename in ["node", "edge", "equipment", "surface"]:
        tempparentjoin[tablename] = linkdict
    PARENTJOIN = dict(tempparentjoin)

    def __init__(self, **kwargs):
        super(BaseDeficiencyTool, self).__init__(**kwargs)
        self.instancekwargs = kwargs

    def initMainToolWidget(self):

        self.toolwidgetmain = UserUI()

        self.formtoolwidgetconfdictmain = {
            "deficiency": {
                "linkfield": "id_deficiency",
                "widgets": {
                    "deficiencycategory": self.toolwidgetmain.comboBox_groupedes
                },
            },
            "Objet": {"linkfield": "id_objet", "widgets": {}},
        }

        self.toolwidgetmain.comboBox_groupedes.currentIndexChanged.connect(
            self.changeGroupe
        )

        # ****************************************************************************************
        # child widgets
        self.dbasechildwdgfield = []
        self.instancekwargs["parentwidget"] = self
        # if self.parentWidget is None :

        self.propertieswdgOBSERVATION = BaseObservationTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgOBSERVATION)

    def magicFunction(self):
        self.featureSelected()
        self.addGPSPoint()
        self.saveFeature()
        self.propertieswdgOBSERVATION2.featureSelected()
        self.propertieswdgOBSERVATION2.saveFeature()

    def postSelectFeature(self):
        if self.currentFeaturePK is not None:
            self.toolwidgetmain.comboBox_groupedes.setEnabled(False)

        else:
            self.toolwidgetmain.comboBox_groupedes.setEnabled(True)

        self._checkSameGeomAsParentNode()

    def _checkSameGeomAsParentNode(self):
        if self.currentFeaturePK is not None and self.parentWidget is not None:
            thisgeom = None
            if self.parentWidget.DBASETABLENAME in ["node"]:
                parentgeom = self.dbase.getWktGeomFromPk(
                    "node", self.parentWidget.currentFeaturePK
                )
                qgsgeom = qgis.core.QgsGeometry.fromWkt(parentgeom).asPoint()
                thisgeom = [qgsgeom, qgsgeom]
            elif self.parentWidget.DBASETABLENAME in ["equipment"]:
                parentgeom = self.dbase.getWktGeomFromPk(
                    "equipment", self.parentWidget.currentFeaturePK
                )
                qgsgeom = qgis.core.QgsGeometry.fromWkt(parentgeom).asPolyline()
                if len(qgsgeom) == 2 and qgsgeom[0] == qgsgeom[1]:
                    thisgeom = qgsgeom
            if thisgeom:
                self.setTempGeometry(thisgeom, False, False)
                self.formutils.setGeometryToFeature(self.currentFeaturePK)

    def changeGroupe(self, intcat):
        self.toolwidget.stackedWidget.setCurrentIndex(intcat)

    def postSaveFeature(self, savedfeaturepk=None):
        pass


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), "lamia_form_deficiency_ui.ui")
        uic.loadUi(uipath, self)
