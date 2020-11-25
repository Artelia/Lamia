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

import os, inspect, datetime
from qgis.PyQt import uic, QtCore, QtGui
from qgis.PyQt.QtWidgets import QWidget

from ...base3.qgswidgets.lamia_form_deficiency import BaseDeficiencyTool
from .lamia_form_observation import BaseConstructionsiteObservationTool
from Lamia.api.libslamia.lamiareport.lamiareport import ReportCore

from Lamia.qgisiface.iface.qgiswidget.tools.form_subwidgets.subwidget_lidchooser import (
    LidChooserWidget,
)

# from Lamia.qgisiface.iface.qgiswidget.tools.form_subwidgets.subwidget_createsubfeature import (
#     CreateSubFeatureWidget,
# )


class BaseConstructionsiteDeficiencyTool(BaseDeficiencyTool):

    PREPROTOOLNAME = "deficiencypv"
    tooltreewidgetSUBCAT = QtCore.QCoreApplication.translate(
        "base3_cs", "Proces verbal"
    )

    def __init__(self, **kwargs):
        super(BaseConstructionsiteDeficiencyTool, self).__init__(**kwargs)

    def initMainToolWidget(self):
        if self.dbase.variante in [None, "Lamia"]:
            self.toolwidgetmain = UserUI()
            self.formtoolwidgetconfdictmain = {
                "deficiency": {
                    "linkfield": "id_deficiency",
                    "widgets": {
                        #'groupedesordre': self.toolwidgetmain.comboBox_groupedes,
                        # 'deficiencyobservatortype': self.toolwidgetmain.comboBox_detecteur,
                        # 'detecteur_com': self.toolwidgetmain.lineEdit_detecteur,
                    },
                },
                "object": {
                    "linkfield": "id_object",
                    "widgets": {
                        # 'comment': self.toolwidgetmain.lineEdit_detecteur,
                    },
                },
            }

            # self.tabWidget.removeTab(0)
            # self.SKIP_LOADING_UI = True
            self.TABLEFILTERFIELD = {"deficiencycategory": "PVE"}
            self.toolwidgetmain.stackedWidget.setCurrentIndex(1)
            self.dbasechildwdgfield = []
            self.instancekwargs["parentwidget"] = self
            self.temppropertieswdgOBSERVATION = BaseConstructionsiteObservationTool(
                **self.instancekwargs
            )
            self.temppropertieswdgOBSERVATION.TABLEFILTERFIELD = {
                "observationcategory": "PVA"
            }
            # self.temppropertieswdgOBSERVATION.SKIP_LOADING_UI = True
            self.temppropertieswdgOBSERVATION.tooltreewidgetSUBCAT = "Procès verbal"
            # temppropertieswdgOBSERVATION.tooltreewidgetSUBCAT = displayname
            # exec('self.propertieswdgOBSERVATION{} = temppropertieswdgOBSERVATION'.format(observationcategory))
            # exec('self.dbasechildwdgfield.append(self.propertieswdgOBSERVATION{} )'.format(observationcategory))
            self.dbasechildwdgfield.append(self.temppropertieswdgOBSERVATION)

            # # * lamiawdg
            # self.createobswdg = CreateSubFeatureWidget(
            #     self, self.temppropertieswdgOBSERVATION
            # )
            # self.lamiawidgets.append(self.createobswdg)

        else:
            self.unloadWidgetinToolTree()
            self.loadWidgetinToolTree = lambda: None
            # self.toolTreeWidgetCurrentItemChanged = lambda: None

    def magicFunction(self):
        self.featureSelected()
        self.addGPSPoint()
        self.saveFeature()
        for wdgobservation in self.dbasechildwdgfield:
            if hasattr(wdgobservation, "OBSTYPE") and wdgobservation.OBSTYPE == "NCA":
                wdgobservation.featureSelected()
                wdgobservation.saveFeature()

    # def postInitFeatureProperties(self, feat):
    def postSelectFeature(self):
        super().postSelectFeature()

    """
    def postSaveFeature(self, savedfeaturepk=None):
        self.formutils.createNewSubFeature(
            self.temppropertieswdgOBSERVATION, savedfeaturepk
        )
    """

    def printWidget(self):

        # create finelname
        pdfdirectory = os.path.join(self.dbase.dbaseressourcesdirectory, "Print")
        if not os.path.isdir(pdfdirectory):
            os.mkdir(pdfdirectory)

        currentid = self.dbase.getValuesFromPk(
            "deficiency", "id_deficiency", self.currentFeaturePK
        )

        date = str(datetime.datetime.now().strftime("%Y%m%d_%H%M%S"))

        filename = str(currentid) + "_deficiency_" + date + ".pdf"

        pdffilename = os.path.join(pdfdirectory, filename)

        # choose phaseA report or phase C report
        sql = (
            "SELECT observationcategory FROM  observation_now WHERE observation_now.lid_deficiency = "
            + str(currentid)
        )
        sql = self.dbase.updateQueryTableNow(sql)
        res = self.dbase.query(sql)

        if (
            res is not None
            and len(res) > 0
            and not self.dbase.utils.isAttributeNull(res[0][0])
        ):
            if res[0][0] == "PVA":
                reporttype = "TRAMprocesverbalmiseadisposition"
            """
            elif res[0][0][0:2] == "NC":
                sql = "SELECT id_observation FROM observation_now WHERE observation_now.typeobservation = 'NCB'"
                sql += " AND Observation_now.lid_desordre = " + str(currentid)
                sql = self.dbase.updateQueryTableNow(sql)
                res = self.dbase.query(sql)
                if self.dbase.variante in [None, "Lamia"]:
                    if (
                        res is not None
                        and len(res) > 0
                        and not self.dbase.utils.isAttributeNull(res[0][0])
                    ):
                        reportype = "TRAMnonconformite"
                    else:
                        reportype = "TRAMnonconformitephaseA"
                elif self.dbase.variante in ["Orange"]:
                    print("*********ORANGEnonconformitephaseA")
                    reportype = "ORANGEnonconformitephaseA"
            """
        else:
            return

        # run report
        self.reporttool = ReportCore(
            dbaseparser=self.dbase, messageinstance=self.mainifacewidget.connector
        )
        self.reporttool.runReport(
            destinationfile=pdffilename,
            reportconffilename=reporttype,
            pklist={0: [self.currentFeaturePK]},
        )


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), "lamia_form_deficiency_ui.ui")
        uic.loadUi(uipath, self)
