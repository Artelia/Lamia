# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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

import sys
from collections import OrderedDict
import datetime
import os

import qgis
from qgis.PyQt import uic, QtCore
from qgis.PyQt.QtWidgets import QWidget, QPushButton

from ...base3.qgswidgets.lamia_form_node import BaseNodeTool
from .lamia_form_camera import BaseWaterdistributionCameraTool
from .lamia_form_sketch import BaseWaterdistributionSketchTool
from .lamia_form_deficiency import BaseWaterdistributionDeficiencyTool

# from Lamia.qgisiface.iface.qgiswidget.tools.form_subwidgets.subwidget_topologicnode import (
#     TopologicNodeWidget,
# )
from Lamia.qgisiface.iface.qgiswidget.tools.form_subwidgets.subwidget_gpsvalues import (
    GpsValuesWidget,
)

# from Lamia.qgisiface.iface.qgiswidget.tools.form_subwidgets.subwidget_createsubfeature import (
#     CreateSubFeatureWidget,
# )


class BaseWaterdistributionNodeTool(BaseNodeTool):
    PARENTJOIN = {
        "equipment": {
            "colparent": "id_descriptionsystem",
            "colthistable": "lid_descriptionsystem_1",
            "tctable": None,
            "tctablecolparent": None,
            "tctablecolthistable": None,
        }
    }

    def __init__(self, **kwargs):
        super(BaseWaterdistributionNodeTool, self).__init__(**kwargs)

    def initMainToolWidget(self):

        self.toolwidgetmain = UserUI()
        self.formtoolwidgetconfdictmain = {
            "node": {
                "linkfield": "id_node",
                "widgets": {
                    "nodetype": self.toolwidgetmain.nodetype,
                    "nodefunction": self.toolwidgetmain.nodefunction,
                    "nodesubtype": self.toolwidgetmain.nodesubtype,
                    "access": self.toolwidgetmain.access,
                    "accessshape": self.toolwidgetmain.accessshape,
                    "diameterinlet": self.toolwidgetmain.diameterinlet,
                    "diameteroutlet": self.toolwidgetmain.diameteroutlet,
                    "nodedepth": self.toolwidgetmain.nodedepth,
                    "presencestep": self.toolwidgetmain.presencestep,
                    # ventouse
                    "nodeelevation": self.toolwidgetmain.nodeelevation,
                    # vanne
                    "localisation": [
                        self.toolwidgetmain.localisation,
                        self.toolwidgetmain.localisation_2,
                    ],
                    "accessibility": [
                        self.toolwidgetmain.accessibility,
                        self.toolwidgetmain.accessibility_2,
                    ],
                    "manipulability": self.toolwidgetmain.manipulability,
                    "nodeposition": self.toolwidgetmain.nodeposition,
                    # vidange
                    "presenceoutlet": self.toolwidgetmain.presenceoutlet,
                    # reg pression
                    "valvedownstreamsetting": self.toolwidgetmain.valvedownstreamsetting,
                    "valveupstreamsetting": self.toolwidgetmain.valveupstreamsetting,
                    # hydrant
                    "hydrantfiredepartmentid": self.toolwidgetmain.hydrantfiredepartmentid,
                    "brandname": [
                        self.toolwidgetmain.brandname,
                        self.toolwidgetmain.brandname_2,
                    ],
                    "brandref": [
                        self.toolwidgetmain.brandref,
                        self.toolwidgetmain.brandref_2,
                    ],
                    "hydrantconformity": self.toolwidgetmain.hydrantconformity,
                    # compteur"
                    "nodesize": self.toolwidgetmain.nodesize,
                    "nodeemitter": self.toolwidgetmain.nodeemitter,
                    "nodecountervalue": self.toolwidgetmain.nodecountervalue,
                    "retrofitable": self.toolwidgetmain.retrofitable,
                    "serialnumber": self.toolwidgetmain.serialnumber,
                    #'localisation': self.toolwidgetmain.comboBox_localisation2,
                    #'accessibilite': self.toolwidgetmain.comboBox_accessibilite2,
                    # 'marque': self.toolwidgetmain.lineEdit_marque2,
                    # 'type': self.toolwidgetmain.lineEdit_type2,
                    "maintenancefirm": [
                        self.toolwidgetmain.maintenancefirm,
                        self.toolwidgetmain.maintenancefirm_2,
                    ],
                    "remotemonitoring": [
                        self.toolwidgetmain.remotemonitoring,
                        self.toolwidgetmain.remotemonitoring_2,
                    ],
                    "linkedfacilities": self.toolwidgetmain.linkedfacilities,
                    # chloration
                    #'entreprise': self.toolwidgetmain.lineEdit_entreprise2,
                    #'telerelevage': self.toolwidgetmain.comboBox_telerelevage2,
                    # robinet de prise en charge
                    "clamp": self.toolwidgetmain.clamp,
                    "X": self.toolwidgetmain.X,
                    "dX": self.toolwidgetmain.dX,
                    "Y": self.toolwidgetmain.Y,
                    "dY": self.toolwidgetmain.dY,
                    "Z": self.toolwidgetmain.Z,
                    "dZ": self.toolwidgetmain.dZ,
                },
            },
            "object": {
                "linkfield": "id_object",
                "widgets": {"comment": self.toolwidgetmain.comment},
            },
            "descriptionsystem": {
                "linkfield": "id_descriptionsystem",
                "widgets": {
                    "operational": self.toolwidgetmain.operational,
                    "dateoperationalcreation": self.toolwidgetmain.dateoperationalcreation,
                    "networktype": self.toolwidgetmain.networktype,
                },
            },
        }

        self.toolwidgetmain.toolButton_diam.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.diameterinlet)
        )
        self.toolwidgetmain.toolButton_diamsor.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.diameteroutlet)
        )
        self.toolwidgetmain.toolButton_prof.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.nodedepth)
        )

        self.toolwidgetmain.toolButton_idsdis.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.hydrantfiredepartmentid)
        )

        self.toolwidgetmain.toolButton_altim.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.nodeelevation)
        )

        self.toolwidgetmain.toolButton_cons_am.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.valveupstreamsetting)
        )
        self.toolwidgetmain.toolButton_cons_av.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.valvedownstreamsetting)
        )

        self.toolwidgetmain.toolButton_nodesize.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.nodesize)
        )
        self.toolwidgetmain.toolButton_nodecountervalue.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.nodecountervalue)
        )

        self.toolwidgetmain.nodetype.currentIndexChanged.connect(self.changeCategorie)
        self.toolwidgetmain.pushButton_getGPS.clicked.connect(self.getGPSValue)

        self.allaccessfields = OrderedDict(
            self.dbase.dbasetables[self.DBASETABLENAME]["fields"]["access"]
        )

        # ****************************************************************************************
        # child widgets
        self.dbasechildwdgfield = []
        self.instancekwargs["parentwidget"] = self

        self.propertieswdgDesordre = BaseWaterdistributionDeficiencyTool(
            **self.instancekwargs
        )
        # self.propertieswdgDesordre.NAME = None
        # self.propertieswdgDesordre.userwdgfield.frame_2.setParent(None)
        # self.propertieswdgDesordre.userwdgfield.stackedWidget.setVisible(False)
        # self.propertieswdgDesordre.groupBox_elements.setParent(None)
        # self.propertieswdgDesordre.pushButton_addFeature.setEnabled(False)
        # self.propertieswdgDesordre.pushButton_delFeature.setEnabled(False)
        # self.propertieswdgDesordre.comboBox_featurelist.setEnabled(False)
        # self.propertieswdgDesordre.groupBox_geom.setParent(None)
        # self.propertieswdgDesordre.frame_editing.setVisible(False)
        # self.toolwidgetmain.tabWidget_2.widget(2).layout().addWidget(self.propertieswdgDesordre)
        self.propertieswdgDesordre.SKIP_LOADING_UI = True
        self.propertieswdgDesordre.TABLEFILTERFIELD = {"deficiencycategory": "NOD"}
        # self.propertieswdgDesordre.initMainToolWidget()
        # self.propertieswdgDesordre.formtoolwidgetconfdictmain['deficiency']['widgets']['deficiencycategory'] = 'NOD'
        self.dbasechildwdgfield.append(self.propertieswdgDesordre)

        self.propertieswdgPHOTOGRAPHIE = BaseWaterdistributionCameraTool(
            **self.instancekwargs
        )
        self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)

        self.propertieswdgCROQUIS = BaseWaterdistributionSketchTool(
            **self.instancekwargs
        )
        self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

        # self.topologicnode = TopologicNodeWidget(self)
        # self.lamiawidgets.append(self.topologicnode)
        # self.createdeficiencywdg = CreateSubFeatureWidget(
        #     self, self.propertieswdgDesordre
        # )
        # self.lamiawidgets.append(self.createdeficiencywdg)
        # * gpswidget
        self.gpswidget = GpsValuesWidget(
            parentwdg=self, parentframe=self.toolwidgetmain.frame_gps
        )
        self.lamiawidgets.append(self.gpswidget)

    # def postInitFeatureProperties(self, feat):
    def postSelectFeature(self):
        dbasetable = self.dbase.dbasetables["node"]
        if self.currentFeaturePK is not None:
            lid_dessys = self.dbase.getValuesFromPk(
                "node_qgis", ["lid_descriptionsystem_1"], self.currentFeaturePK
            )
            if lid_dessys is not None:
                self.toolwidgetmain.access.setEnabled(False)
            else:
                self.toolwidgetmain.access.setEnabled(True)
        else:
            self.toolwidgetmain.access.setEnabled(True)
        if (
            self.parentWidget is not None
            and self.parentWidget.currentFeaturePK is not None
            and self.parentWidget.DBASETABLENAME == "equipment"
        ):

            type_ouvrage = self.dbase.getValuesFromPk(
                "equipment_qgis", ["equipmenttype"], self.parentWidget.currentFeaturePK
            )

            if type_ouvrage == "CHE":
                # dbasetable['fields']['acces'] = OrderedDict([('PGtype', 'VARCHAR(255'),('ParFldCst','categorie'),('Cst',[[u'Chambre enterrée/regard', 'CHE',['','VEN','VAN','VID','REG','HYD','COM','CHL','RPC','SPE']]])])
                #                                                                                                                                              #  ['','VEN','VAN','VID','REG','HYD','COM','DEB','CHL','RPC','SPE','AUT','IND']
                rawval = [elem[1] for elem in dbasetable["fields"]["access"]["Cst"]]
                cheindex = rawval.index("CHE")
                dbasetable["fields"]["access"]["Cst"][cheindex][2] = [
                    "",
                    "VEN",
                    "VAN",
                    "VID",
                    "REG",
                    "HYD",
                    "COM",
                    "CHL",
                    "RPC",
                    "SPE",
                ]

                self.toolwidgetmain.nodetype.currentIndexChanged.emit(
                    self.toolwidgetmain.nodetype.currentIndex()
                )
                self.toolwidgetmain.access.setEnabled(False)

            else:
                if dbasetable["fields"]["access"] != self.allaccessfields:
                    dbasetable["fields"]["access"] = self.allaccessfields
                    self.toolwidgetmain.nodetype.currentIndexChanged.emit(
                        self.toolwidgetmain.nodetype.currentIndex()
                    )
        else:
            if dbasetable["fields"]["access"] != self.allaccessfields:
                dbasetable["fields"]["access"] = self.allaccessfields
                self.toolwidgetmain.nodetype.currentIndexChanged.emit(
                    self.toolwidgetmain.nodetype.currentIndex()
                )

    def postSaveFeature(self, savedfeaturepk=None):
        pass
        """
        if self.currentFeaturePK is None:
            self.propertieswdgDesordre.toolbarNew()
            geomtext = self.dbase.getValuesFromPk('node_qgis',
                                            'ST_AsText(geom)',
                                            savedfeaturepk)

            qgsgeom = qgis.core.QgsGeometry.fromWkt(geomtext).asPoint()
            qgsgeomfordesordre = [qgsgeom,qgsgeom]

            self.propertieswdgDesordre.setTempGeometry(qgsgeomfordesordre)

            self.currentFeaturePK = savedfeaturepk
            self.propertieswdgDesordre.toolbarSave()
            pkdesordre = self.propertieswdgDesordre.currentFeaturePK
            # sql = "UPDATE deficiency SET deficiencycategory = 'NOD' WHERE pk_deficiency = {}".format(pkdesordre)
            # self.dbase.query(sql)
        """

    def changeCategorie(self, intcat):
        typeeqt = self.toolwidgetmain.nodetype.itemText(intcat)
        rawtypeeqt = self.dbase.getConstraintRawValueFromText(
            "node", "nodetype", typeeqt
        )
        pagecount = self.toolwidgetmain.stackedWidget.count()
        for pageindex in range(pagecount):
            wdgname = self.toolwidgetmain.stackedWidget.widget(pageindex).objectName()
            if wdgname == rawtypeeqt:
                self.toolwidgetmain.stackedWidget.setCurrentIndex(pageindex)
                return
        self.toolwidgetmain.stackedWidget.setCurrentIndex(pagecount)

    def toolbarMagic(self):
        self.mainifacewidget.toolbarNew()
        self.toolbarGeomAddGPS()
        self.getGPSValue()
        self.mainifacewidget.toolbarSave()

        # self.featureSelected()
        # #self.lastPhoto()
        # self.addGPSPoint()
        # self.saveFeature()

    def addGPSPoint(self):
        if self.gpsutil is None:
            return
        if self.gpsutil.currentpoint is None:
            self.windowdialog.errorMessage("GPS non connecte")
            return

        self.createorresetRubberband(0)

        layerpoint = self.gpsutil.currentpoint
        self.setTempGeometry([layerpoint], False)

        self.getGPSValue()

    def getGPSValue(self):
        self.assignValue(self.gpswidget.label_X, self.toolwidgetmain.X)
        self.assignValue(self.gpswidget.label_dX, self.toolwidgetmain.dX)
        self.assignValue(self.gpswidget.label_Y, self.toolwidgetmain.Y)
        self.assignValue(self.gpswidget.label_dY, self.toolwidgetmain.dY)
        self.assignValue(self.gpswidget.label_Z, self.toolwidgetmain.Z)
        self.assignValue(self.gpswidget.label_dZ, self.toolwidgetmain.dZ)

    def assignValue(self, wdgfrom, wdgto):
        if self.isfloat(wdgfrom.text()):
            wdgto.setValue(float(wdgfrom.text()))

    def isfloat(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), "lamia_form_node_ui.ui")
        uic.loadUi(uipath, self)
