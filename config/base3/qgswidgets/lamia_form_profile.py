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

from Lamia.qgisiface.iface.qgiswidget.tools.lamia_abstractformtool import (
    AbstractLamiaFormTool,
)
from .lamia_form_camera import BaseCameraTool
from .lamia_form_sketch import BaseSketchTool
from .lamia_form_graph import BaseGraphTool


class BaseProfileTool(AbstractLamiaFormTool):

    PREPROTOOLNAME = "profile"
    DBASETABLENAME = "profile"
    LOADFIRST = True

    tooltreewidgetCAT = QtCore.QCoreApplication.translate("base3", "Facilities")
    tooltreewidgetSUBCAT = QtCore.QCoreApplication.translate("base3", "Profile")
    tooltreewidgetICONPATH = os.path.join(
        os.path.dirname(__file__), "lamia_form_profile_icon.svg"
    )

    PARENTJOIN = {
        "edge": {
            "colparent": "id_descriptionsystem",
            "colthistable": "lid_descriptionsystem",
            "tctable": None,
            "tctablecolparent": None,
            "tctablecolthistable": None,
        }
    }

    def __init__(self, **kwargs):
        super(BaseProfileTool, self).__init__(**kwargs)
        self.instancekwargs = kwargs

    """
    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Description'
        self.NAME = 'Profil'
        self.dbasetablename = 'Profil'
        self.visualmode = [1, 2]
        # self.PointEnabled = True
        self.LineENABLED = True
        # self.PolygonEnabled = True

        self.linkagespec = {'Infralineaire' : {'tabletc' : None,
                                              'idsource' : 'lid_descriptionsystem',
                                            'idtcsource' : None,
                                           'iddest' : 'id_descriptionsystem',
                                           'idtcdest' : None,
                                           'desttable' : ['Infralineaire']} }
        # self.pickTable = None
        self.iconpath = os.path.join(os.path.dirname(__file__), 'lamiabase_profil_tool_icon.svg')
        # ****************************************************************************************
        #properties ui
        pass
        """

    def initMainToolWidget(self):

        self.toolwidgetmain = UserUI()
        self.formtoolwidgetconfdictmain = {
            "profile": {
                "linkfield": "id_profile",
                "widgets": {
                    "dateprofile": self.toolwidgetmain.dateEdit,
                    "profiletype": self.toolwidgetmain.comboBox_type,
                },
            },
            "object": {"linkfield": "id_object", "widgets": {}},
            "descriptionsystem": {"linkfield": "id_descriptionsystem", "widgets": {}},
        }

        # child widgets
        self.dbasechildwdgfield = []
        self.instancekwargs["parentwidget"] = self

        self.propertieswdgGRAPH = BaseGraphTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgGRAPH)

        self.propertieswdgCROQUIS = BaseSketchTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

        self.propertieswdgPHOTO = BaseCameraTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgPHOTO)

    def postSelectFeature(self):
        if self.currentFeaturePK is None:

            datecreation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            self.formutils.applyResultDict(
                {"dateprofil": datecreation}, checkifinforgottenfield=False
            )

        # if self.parentWidget is None:
        #     self.toolwidgetmain.pushButton_setasdefault.setEnabled(False)
        # else:
        #     self.toolwidgetmain.pushButton_setasdefault.setEnabled(True)

        # if self.parentWidget is not None:
        #    if self.parentWidget.DBASETABLENAME == 'Infralineaire' and self.parentWidget.currentFeaturePK is not None:
        #        #parent id_dessys
        #        sql = "SELECT id_descriptionsystem FROM Infralineaire_qgis WHERE pk_infralineaire = " + str(self.parentWidget.currentFeaturePK)
        #        pkdessys = self.dbase.query(sql)[0][0]
        #        # TODO
        #        self.initFeatureProperties(self.currentFeature,'Profil', 'lid_descriptionsystem', pkdessys)
        #        #self.formutils.applyResultDict({'date' : datecreation},checkifinforgottenfield=False)

    def postSaveFeature(self, savedfeaturepk=None):
        self.setAsDefault()

    def setAsDefault(self):
        if self.parentWidget and self.parentWidget.currentFeaturePK is not None:

            mainprofiletype = self.toolwidgetmain.comboBox_type.currentText()
            rawval = self.dbase.getConstraintRawValueFromText(
                "profile", "profiletype", mainprofiletype
            )
            if rawval == "GRA":
                wdg = self.propertieswdgGRAPH
                tbl = "graph"
            elif rawval == "CRO":
                wdg = self.propertieswdgCROQUIS
                tbl = "media"
            elif rawval == "PHO":
                wdg = self.propertieswdgPHOTO
                tbl = "media"

            resourcepk = wdg.currentFeaturePK
            if resourcepk is None:
                idresource = "NULL"
            else:
                idresource = self.dbase.getValuesFromPk(
                    f"{tbl}_qgis", "id_resource", resourcepk
                )

            sql = f"UPDATE {self.parentWidget.DBASETABLENAME} \
                    SET  lid_resource_4 = {idresource} \
                    WHERE pk_{self.parentWidget.DBASETABLENAME} = {self.parentWidget.currentFeaturePK}"
            self.dbase.query(sql)


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), "lamia_form_profile_ui.ui")
        uic.loadUi(uipath, self)
