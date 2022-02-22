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
import os
import qgis
import sys, datetime
from collections import OrderedDict

from qgis.PyQt import uic, QtCore
from qgis.PyQt.QtWidgets import QWidget, QPushButton
from ...base3.qgswidgets.lamia_form_node import BaseNodeTool

from .lamia_form_camera import BaseUrbandrainageCameraTool
from .lamia_form_sketch import BaseUrbandrainageSketchTool
from .lamia_form_deficiency import BaseUrbandrainageDeficiencyTool
from .lamia_form_equipment import BaseUrbandrainageEquipmentTool
from .lamia_form_graph import BaseUrbandrainageGraphTool

from Lamia.qgisiface.iface.qgiswidget.tools.form_subwidgets.subwidget_lidchooser import (
    LidChooserWidget,
)

# from Lamia.qgisiface.iface.qgiswidget.tools.form_subwidgets.subwidget_topologicnode import (
#     TopologicNodeWidget,
# )

# from Lamia.qgisiface.iface.qgiswidget.tools.form_subwidgets.subwidget_createsubfeature import (
#     CreateSubFeatureWidget,
# )
from Lamia.qgisiface.iface.qgiswidget.tools.form_subwidgets.subwidget_gpsvalues import (
    GpsValuesWidget,
)


class BaseUrbandrainageNodeTool(BaseNodeTool):
    def __init__(self, **kwargs):
        super(BaseUrbandrainageNodeTool, self).__init__(**kwargs)

    def initMainToolWidget(self):

        if self.dbase.variante in [None, "Lamia"]:
            self._initMainToolWidgetLamia()

        elif self.dbase.variante in ["2018_SNCF"]:
            self._initMainToolWidgetSNCF()

        elif self.dbase.variante in ["CD41"]:
            self._initMainToolWidgetCD41()

        # * childwdg
        self.propertieswdgDesordre = BaseUrbandrainageDeficiencyTool(
            **self.instancekwargsforchildwdg
        )
        self.propertieswdgDesordre.SKIP_LOADING_UI = True
        self.propertieswdgDesordre.initMainToolWidget()
        # self.propertieswdgDesordre.formtoolwidgetconfdictmain["deficiency"]["widgets"][
        #     "deficiencycategory"
        # ] = "NOD"
        self.propertieswdgDesordre.TABLEFILTERFIELD = {"deficiencycategory": "NOD"}
        self.dbasechildwdgfield.append(self.propertieswdgDesordre)

        self.propertieswdgEquipement = BaseUrbandrainageEquipmentTool(
            **self.instancekwargsforchildwdg
        )
        self.dbasechildwdgfield.append(self.propertieswdgEquipement)

        self.propertieswdgPHOTOGRAPHIE = BaseUrbandrainageCameraTool(
            **self.instancekwargsforchildwdg
        )
        self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)
        self.propertieswdgCROQUIS = BaseUrbandrainageSketchTool(
            **self.instancekwargsforchildwdg
        )
        self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

        if self.dbase.variante in [None, "Lamia"]:
            self.propertieswdgGRAPH = BaseUrbandrainageGraphTool(
                **self.instancekwargsforchildwdg
            )
            self.dbasechildwdgfield.append(self.propertieswdgGRAPH)

        # * lamiawdg
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

    def _initMainToolWidgetLamia(self):
        self.toolwidgetmain = UserUI()
        self.formtoolwidgetconfdictmain = {
            "node": {
                "linkfield": "id_node",
                "widgets": {
                    "location": self.toolwidgetmain.location,
                    "nodetype": self.toolwidgetmain.nodetype,
                    "nodesubtype": self.toolwidgetmain.nodesubtype,
                    "manholecovershape": self.toolwidgetmain.manholecovershape,
                    "accessibility": self.toolwidgetmain.accessibility,
                    # regard
                    "presencesteps": self.toolwidgetmain.presencesteps,
                    "presencehandle": self.toolwidgetmain.presencehandle,
                    "presencelowflowchannel": self.toolwidgetmain.presencelowflowchannel,
                    "manholeshape": self.toolwidgetmain.manholeshape,
                    "manholematerial": self.toolwidgetmain.manholematerial,
                    # branchement
                    "presencesiphoidpartition": self.toolwidgetmain.presencesiphoidpartition,
                    "presencelid": self.toolwidgetmain.presencelid,
                    "lateralusercategory": self.toolwidgetmain.lateralusercategory,
                    # avaloir
                    "sedimenttrap": self.toolwidgetmain.sedimenttrap,
                    # PR
                    "psfence": self.toolwidgetmain.psfence,
                    "pslocked": self.toolwidgetmain.pslocked,
                    "psh2streatment": self.toolwidgetmain.psh2streatment,
                    "pseleccabinet": self.toolwidgetmain.pseleccabinet,
                    "pseleccabinetlocked": self.toolwidgetmain.pseleccabinetlocked,
                    "psremotemonitoring": [
                        self.toolwidgetmain.psremotemonitoring,
                        self.toolwidgetmain.psremotemonitoring_2,
                    ],
                    "psremotemonitoringcomment": self.toolwidgetmain.psremotemonitoringcomment,
                    "pspumpswitchingcontroller": self.toolwidgetmain.pspumpswitchingcontroller,
                    "psmaterial": [
                        self.toolwidgetmain.psmaterial,
                        self.toolwidgetmain.psmaterial_2,
                    ],
                    "psfallprotectiongratings": self.toolwidgetmain.psfallprotectiongratings,
                    "psinletscreen": self.toolwidgetmain.psinletscreen,
                    "pspumpswitchingcontrollertype": self.toolwidgetmain.pspumpswitchingcontrollertype,
                    "psnominalcapacity": self.toolwidgetmain.psnominalcapacity,
                    "pspumphead": self.toolwidgetmain.pspumphead,
                    "psfloatnumber": self.toolwidgetmain.psfloatnumber,
                    "psoverflow": self.toolwidgetmain.psoverflow,
                    "psguiderail": self.toolwidgetmain.psguiderail,
                    "pspumpliftingchain": self.toolwidgetmain.pspumpliftingchain,
                    "pspumpnumber": self.toolwidgetmain.pspumpnumber,
                    "psdrawdownheight": self.toolwidgetmain.psdrawdownheight,
                    "psdrawdownvolume": self.toolwidgetmain.psdrawdownvolume,
                    "pscheckvalve": self.toolwidgetmain.pscheckvalve,
                    "psgatevalve": self.toolwidgetmain.psgatevalve,
                    "pspressureport": self.toolwidgetmain.pspressureport,
                    # DSH
                    # DSH materiau : self.toolwidgetmain_2.comboBox_DSH_materiau cf PR
                    #'DSHpresencealarme': self.toolwidgetmain_2.comboBox_DSHalarme,
                    "presencecontroller": self.toolwidgetmain.presencecontroller,
                    "brandname": [
                        self.toolwidgetmain.brandname,
                        self.toolwidgetmain.brandname_2,
                    ],
                    "brandref": self.toolwidgetmain.brandref,
                    "nodetechclass": self.toolwidgetmain.nodetechclass,
                    "inletdiameter": [
                        self.toolwidgetmain.inletdiameter,
                        self.toolwidgetmain.inletdiameter_2,
                        self.toolwidgetmain.inletdiameter_3,
                    ],
                    "outletdiameter": [
                        self.toolwidgetmain.outletdiameter,
                        self.toolwidgetmain.outletdiameter_2,
                        self.toolwidgetmain.outletdiameter_3,
                    ],
                    "airing": self.toolwidgetmain.airing,
                    # cso
                    "csoweirheight": self.toolwidgetmain.csoweirheight,
                    "scoweirlenght": self.toolwidgetmain.scoweirlenght,
                    "scoweirthickness": self.toolwidgetmain.scoweirthickness,
                    "receivingenvironmentcomment": [
                        self.toolwidgetmain.receivingenvironmentcomment,
                        self.toolwidgetmain.receivingenvironmentcomment_2,
                        self.toolwidgetmain.receivingenvironmentcomment_3,
                        self.toolwidgetmain.receivingenvironmentcomment_4,
                        ],
                    # septic tank
                    "receivingenvironment": [
                        self.toolwidgetmain.receivingenvironment,
                        self.toolwidgetmain.receivingenvironment_2,
                        self.toolwidgetmain.receivingenvironment_3,
                        self.toolwidgetmain.receivingenvironment_4,
                        ],
                    # autre
                    "depthinvert": self.toolwidgetmain.depthinvert,
                    "width": self.toolwidgetmain.width,
                    "lenght": self.toolwidgetmain.lenght,
                    "x": self.toolwidgetmain.x,
                    "dx": self.toolwidgetmain.dx,
                    "y": self.toolwidgetmain.y,
                    "dy": self.toolwidgetmain.dy,
                    "z": self.toolwidgetmain.z,
                    "dz": self.toolwidgetmain.dz,
                },
            },
            "object": {
                "linkfield": "id_object",
                "widgets": {
                    "name": self.toolwidgetmain.name,
                    "comment": self.toolwidgetmain.comment,
                },
            },
            "descriptionsystem": {
                "linkfield": "id_descriptionsystem",
                "widgets": {
                    "networktype": self.toolwidgetmain.networktype,
                    "flowconditionupstream": self.toolwidgetmain.flowconditionupstream,
                    "flowconditiondownstream": self.toolwidgetmain.flowconditiondownstream,
                    "systemfunction": self.toolwidgetmain.systemfunction,
                    "city": self.toolwidgetmain.city,
                    "streetname": self.toolwidgetmain.streetname,
                    "structuralstate": self.toolwidgetmain.structuralstate,
                },
            },
        }

        self.toolwidgetmain.toolButton_longueur.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.lenght)
        )
        self.toolwidgetmain.toolButton_largeur.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.width)
        )
        self.toolwidgetmain.toolButton_calc.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.depthinvert)
        )
        self.toolwidgetmain.toolButton_poires.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.psfloatnumber)
        )
        self.toolwidgetmain.toolButton_pompes.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.pspumpnumber)
        )

        self.toolwidgetmain.toolButton_scoweirlenght.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.scoweirlenght)
        )
        self.toolwidgetmain.toolButton_csoweirheight.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.csoweirheight)
        )
        self.toolwidgetmain.toolButton_scoweirthickness.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.scoweirthickness)
        )

        self.toolwidgetmain.toolButton_inletdiameter.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.inletdiameter)
        )
        self.toolwidgetmain.toolButton_outletdiameter.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.outletdiameter)
        )
        self.toolwidgetmain.toolButton_inletdiameter_2.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.inletdiameter_2)
        )
        self.toolwidgetmain.toolButton_outletdiameter_2.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.outletdiameter_2)
        )
        self.toolwidgetmain.toolButton_inletdiameter_3.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.inletdiameter_3)
        )
        self.toolwidgetmain.toolButton_outletdiameter_3.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.outletdiameter_3)
        )
        self.toolwidgetmain.toolbutton_psnominalcapacity.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.psnominalcapacity)
        )
        self.toolwidgetmain.toolbutton_pspumphead.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.pspumphead)
        )

        self.toolwidgetmain.toolButton_psdrawdownheight.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.psdrawdownheight)
        )
        self.toolwidgetmain.toolButton_psdrawdownvolume.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.psdrawdownvolume)
        )

        self.toolwidgetmain.nodetype.currentIndexChanged.connect(
            self.fielduiTypeOhChanged
        )
        self.toolwidgetmain.pushButton_getGPS.clicked.connect(self.getGPSValue)

        self.ownerwdg = LidChooserWidget(
            parentwdg=self,
            parentlidfield="lid_actor_1",
            parentframe=self.toolwidgetmain.frame_owner,
            searchdbase="actor",
            searchfieldtoshow=["actorname"],
        )
        self.lamiawidgets.append(self.ownerwdg)
        self.operatorwdg = LidChooserWidget(
            parentwdg=self,
            parentlidfield="lid_actor_2",
            parentframe=self.toolwidgetmain.frame_operator,
            searchdbase="actor",
            searchfieldtoshow=["actorname"],
        )
        self.lamiawidgets.append(self.operatorwdg)

    def _initMainToolWidgetSNCF(self):
        """Same as default, but :
            * secondary properties come from specific widget (lamia_form_node_ui_2018SNCF_secondarypropertiestab.ui)
            * remove manage tab
        """
        self.toolwidgetmain = UserUI()

        # changing secondary properties tab
        secondarypropertiestab = UserUI_2()
        self.toolwidgetmain.tabWidget_node.removeTab(1)
        self.toolwidgetmain.tabWidget_node.insertTab(
            1, secondarypropertiestab, r"Secondary\nproperties"
        )
        self.formutils.mergeQtWidgets(self.toolwidgetmain, secondarypropertiestab)

        # remove manage tab
        self.toolwidgetmain.tabWidget_node.removeTab(4)

        # conf
        self.formtoolwidgetconfdictmain = {
            "node": {
                "linkfield": "id_node",
                "widgets": {
                    "location": self.toolwidgetmain.location,
                    "nodetype": self.toolwidgetmain.nodetype,
                    "nodesubtype": self.toolwidgetmain.nodesubtype,
                    "manholecovershape": self.toolwidgetmain.manholecovershape,
                    "accessibility": self.toolwidgetmain.accessibility,
                    # regard
                    "presencesteps": self.toolwidgetmain.presencesteps,
                    "presencehandle": self.toolwidgetmain.presencehandle,
                    # 'presencecunette': self.toolwidgetmain.comboBox_cunette,
                    "manholeshape": self.toolwidgetmain.manholeshape,
                    # 'formeregard': self.toolwidgetmain.comboBox_formeregard,
                    # branchement
                    # 'cloisonsiphoide': self.toolwidgetmain.comboBox_cloisonsiphoide,
                    # 'couvercle': self.toolwidgetmain.comboBox_couvercle,
                    # PR
                    # 'PRcloture': self.toolwidgetmain.comboBox_cloture,
                    # 'PRverouille': self.toolwidgetmain.comboBox_verouille,
                    "pseleccabinet": self.toolwidgetmain.pseleccabinet,
                    # 'PRarmoireelecverouillee': self.toolwidgetmain.comboBox_armoire_verouille,
                    "psremotemonitoring": [
                        self.toolwidgetmain.psremotemonitoring,
                        self.toolwidgetmain.psremotemonitoring_2,
                    ],
                    "psremotemonitoringcomment": self.toolwidgetmain.psremotemonitoringcomment,
                    # 'PRpermutautopompe': self.toolwidgetmain.comboBox_permut_pompes,
                    "psmaterial": [
                        self.toolwidgetmain.psmaterial,
                        self.toolwidgetmain.psmaterial_2,
                    ],
                    # 'PRgrilleantichute': self.toolwidgetmain.comboBox_antichute,
                    # 'PRpanierdegrilleur': self.toolwidgetmain.comboBox_panierdegrileur,
                    "pspumpswitchingcontrollertype": self.toolwidgetmain.pspumpswitchingcontrollertype,
                    "psnominalcapacity": self.toolwidgetmain.psnominalcapacity,
                    "pspumphead": self.toolwidgetmain.pspumphead,
                    "psfloatnumber": self.toolwidgetmain.psfloatnumber,
                    "psoverflow": self.toolwidgetmain.psoverflow,
                    "psdrawdownheight": self.toolwidgetmain.psdrawdownheight,
                    "psdrawdownvolume": self.toolwidgetmain.psdrawdownvolume,
                    # 'PRpompebarreguidage': self.toolwidgetmain.comboBox_barrresguidage,
                    # 'PRpompechainerelevage': self.toolwidgetmain.comboBox_pompe_relevage,
                    "pspumpnumber": self.toolwidgetmain.pspumpnumber,
                    # 'PRclapet': self.toolwidgetmain.comboBox_vanne_clapet,
                    # 'PRvannes': self.toolwidgetmain.comboBox_vanne_vanne,
                    # 'PRprisepression': self.toolwidgetmain.comboBox_vanne_prisepression,
                    # DSH
                    # DSH materiau : self.toolwidgetmain.comboBox_DSH_materiau cf PR
                    # 'DSHpresencealarme': self.toolwidgetmain.comboBox_DSHalarme,
                    "presencecontroller": self.toolwidgetmain.presencecontroller,
                    "brandname": [
                        self.toolwidgetmain.brandname,
                        self.toolwidgetmain.brandname_2,
                    ],
                    "brandref": self.toolwidgetmain.brandref,
                    "nodetechclass": self.toolwidgetmain.nodetechclass,
                    "inletdiameter": [
                        self.toolwidgetmain.inletdiameter,
                        self.toolwidgetmain.inletdiameter_2,
                        self.toolwidgetmain.inletdiameter_3,
                    ],
                    "outletdiameter": [
                        self.toolwidgetmain.outletdiameter,
                        self.toolwidgetmain.outletdiameter_2,
                        self.toolwidgetmain.outletdiameter_3,
                    ],
                    "airing": self.toolwidgetmain.airing,
                    # septic tank
                    "receivingenvironment": self.toolwidgetmain.receivingenvironment,
                    # cso
                    "csoweirheight": self.toolwidgetmain.csoweirheight,
                    "scoweirlenght": self.toolwidgetmain.scoweirlenght,
                    "scoweirthickness": self.toolwidgetmain.scoweirthickness,
                    "receivingenvironmentcomment": self.toolwidgetmain.receivingenvironmentcomment,
                    # autre
                    "depthinvert": self.toolwidgetmain.depthinvert,
                    "width": self.toolwidgetmain.width,
                    "lenght": self.toolwidgetmain.lenght,
                    "x": self.toolwidgetmain.x,
                    "dx": self.toolwidgetmain.dx,
                    "y": self.toolwidgetmain.y,
                    "dy": self.toolwidgetmain.dy,
                    "z": self.toolwidgetmain.z,
                    "dz": self.toolwidgetmain.dz,
                },
            },
            "object": {
                "linkfield": "id_object",
                "widgets": {
                    "name": self.toolwidgetmain.name,
                    "comment": self.toolwidgetmain.comment,
                },
            },
            "descriptionsystem": {
                "linkfield": "id_descriptionsystem",
                "widgets": {
                    "networktype": self.toolwidgetmain.networktype,
                    "flowconditionupstream": self.toolwidgetmain.flowconditionupstream,
                    "flowconditiondownstream": self.toolwidgetmain.flowconditiondownstream,
                    "systemfunction": self.toolwidgetmain.systemfunction,
                    # "city": self.toolwidgetmain.city,
                    # "streetname": self.toolwidgetmain.streetname,
                    "structuralstate": self.toolwidgetmain.structuralstate,
                },
            },
        }

        self.toolwidgetmain.toolButton_longueur.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.lenght)
        )
        self.toolwidgetmain.toolButton_largeur.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.width)
        )
        self.toolwidgetmain.toolButton_calc.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.depthinvert)
        )
        self.toolwidgetmain.toolButton_poires.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.psfloatnumber)
        )
        self.toolwidgetmain.toolButton_pompes.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.pspumpnumber)
        )

        self.toolwidgetmain.toolButton_scoweirlenght.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.scoweirlenght)
        )
        self.toolwidgetmain.toolButton_csoweirheight.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.csoweirheight)
        )
        self.toolwidgetmain.toolButton_scoweirthickness.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.scoweirthickness)
        )

        self.toolwidgetmain.toolButton_inletdiameter.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.inletdiameter)
        )
        self.toolwidgetmain.toolButton_outletdiameter.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.outletdiameter)
        )
        self.toolwidgetmain.toolButton_inletdiameter_2.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.inletdiameter_2)
        )
        self.toolwidgetmain.toolButton_outletdiameter_2.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.outletdiameter_2)
        )
        self.toolwidgetmain.toolButton_inletdiameter_3.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.inletdiameter_3)
        )
        self.toolwidgetmain.toolButton_outletdiameter_3.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.outletdiameter_3)
        )

        self.toolwidgetmain.toolbutton_psnominalcapacity.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.psnominalcapacity)
        )
        self.toolwidgetmain.toolbutton_pspumphead.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.pspumphead)
        )

        self.toolwidgetmain.toolButton_psdrawdownheight.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.psdrawdownheight)
        )
        self.toolwidgetmain.toolButton_psdrawdownvolume.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.psdrawdownvolume)
        )

        self.toolwidgetmain.nodetype.currentIndexChanged.connect(
            self.fielduiTypeOhChanged
        )

    def _initMainToolWidgetCD41(self):
        self.toolwidgetmain = UserUI_3()
        self.formtoolwidgetconfdictmain = {
            "node": {
                "linkfield": "id_noeud",
                "widgets": {
                    "domain": self.toolwidgetmain.domain,
                    # "sewertype": self.toolwidgetmain.comboBox_typeReseau,
                    "location": self.toolwidgetmain.location,
                    "nodetype": self.toolwidgetmain.nodetype,
                    "nodesubtype": self.toolwidgetmain.nodesubtype,
                    # regard
                    "accessibility": [
                        self.toolwidgetmain.accessibility,
                        self.toolwidgetmain.accessibility_2,
                    ],
                    "manholematerial": self.toolwidgetmain.manholematerial,
                    # diam_regard : longeur
                    "manholecovertype": self.toolwidgetmain.manholecovertype,
                    "manholecoverdiameter": self.toolwidgetmain.manholecoverdiameter,
                    "presencesteps": self.toolwidgetmain.presencesteps,
                    # Equipement
                    # ouvrage de regul
                    "psremotemonitoring": self.toolwidgetmain.psremotemonitoring,
                    "depth1": self.toolwidgetmain.depth1,
                    # PR
                    "psnominalcapacity": self.toolwidgetmain.psnominalcapacity,
                    # "pspumphead": self.toolwidgetmain.pspumphead,
                    "pspumpnumber": self.toolwidgetmain.pspumpnumber,
                    "psh2streatment": self.toolwidgetmain.psh2streatment,
                    "psoverflow": self.toolwidgetmain.psoverflow,
                    # avaloir
                    "sedimenttrap": self.toolwidgetmain.sedimenttrap,
                    # dimgrille : longeur
                    # autre
                    "depthinvert": self.toolwidgetmain.depthinvert,
                    "width": self.toolwidgetmain.width,
                    "lenght": self.toolwidgetmain.lenght,
                    "x": self.toolwidgetmain.x,
                    "dx": self.toolwidgetmain.dx,
                    "y": self.toolwidgetmain.y,
                    "dy": self.toolwidgetmain.dy,
                    "z": self.toolwidgetmain.z,
                    "dz": self.toolwidgetmain.dz,
                },
            },
            "object": {
                "linkfield": "id_object",
                "widgets": {"comment": self.toolwidgetmain.comment},
            },
            "descriptionsystem": {
                "linkfield": "id_descriptionsystem",
                "widgets": {"networktype": self.toolwidgetmain.networktype,},
            },
        }

        self.toolwidgetmain.toolButton_longueur.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.lenght)
        )
        self.toolwidgetmain.toolButton_diamtampon.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.manholecoverdiameter)
        )
        self.toolwidgetmain.toolButton_profsurverse.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.depth1)
        )
        self.toolwidgetmain.toolButton_capanom.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.psnominalcapacity)
        )
        self.toolwidgetmain.toolButton_pompes2.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.pspumpnumber)
        )
        self.toolwidgetmain.toolButton_largeur.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.width)
        )
        self.toolwidgetmain.toolButton_calc.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.depthinvert)
        )

        self.toolwidgetmain.pushButton_getGPS.clicked.connect(self.getGPSValue)

        self.toolwidgetmain.nodetype.currentIndexChanged.connect(
            self.fieldui3TypeOhChanged
        )

    def fielduiTypeOhChanged(self, comboindex):
        # print(self.toolwidgetmain.nodetype.currentText())
        currenttext = self.toolwidgetmain.nodetype.currentText()
        currentvalue = self.dbase.getConstraintRawValueFromText(
            "node", "nodetype", currenttext
        )

        if currentvalue in ["60", "62"]:  # Manhole simple or mixt
            self.toolwidgetmain.stackedWidget_node.setCurrentIndex(0)
        elif currentvalue in ["61"]:  # lateral
            self.toolwidgetmain.stackedWidget_node.setCurrentIndex(1)
        elif currentvalue in ["10"]:  # pumping station
            self.toolwidgetmain.stackedWidget_node.setCurrentIndex(2)
        elif currentvalue in ["21"]:  # deshuileur
            self.toolwidgetmain.stackedWidget_node.setCurrentIndex(3)
        elif currentvalue in [
            "70",
            "71",
            "72",
        ]:  # "Avaloir", "Grille", "Grille avaloir"
            self.toolwidgetmain.stackedWidget_node.setCurrentIndex(4)
        elif currentvalue in ["40"]:  # deversoir orage
            self.toolwidgetmain.stackedWidget_node.setCurrentIndex(5)
        elif currentvalue in ["24"]:  # septictank
            self.toolwidgetmain.stackedWidget_node.setCurrentIndex(6)
        elif currentvalue in ["50", "51", "52"]:  # outlet
            self.toolwidgetmain.stackedWidget_node.setCurrentIndex(7)
        else:
            self.toolwidgetmain.stackedWidget_node.setCurrentIndex(8)
        self.propertieswdgDesordre.propertieswdgOBSERVATION.updateObservationStackedWidget()

    def fieldui3TypeOhChanged(self, comboindex):
        # print(self.toolwidgetmain_2.nodetype.currentText())
        currenttext = self.toolwidgetmain.nodetype.currentText()
        if currenttext in ["Regard"]:
            self.toolwidgetmain.stackedWidget_node.setCurrentIndex(0)
        elif currenttext in [""]:
            self.toolwidgetmain.stackedWidget_node.setCurrentIndex(1)
        elif currenttext in ["Ouvrage de régulation"]:
            self.toolwidgetmain.stackedWidget_node.setCurrentIndex(2)
        elif currenttext in ["Poste de refoulement"]:
            self.toolwidgetmain.stackedWidget_node.setCurrentIndex(3)
        elif currenttext in ["Avaloir"]:
            self.toolwidgetmain.stackedWidget_node.setCurrentIndex(4)
        else:
            self.toolwidgetmain.stackedWidget_node.setCurrentIndex(5)

        # self.propertieswdgDesordre.propertieswdgOBSERVATION2.updateObservationStackedWidget()
        self.propertieswdgDesordre.propertieswdgOBSERVATION.updateObservationStackedWidget()

    def toolbarMagic(self):
        self.mainifacewidget.toolbarNew()
        self.toolbarGeomAddGPS()
        self.getGPSValue()
        self.mainifacewidget.toolbarSave()

    def magicFunction(self):
        self.featureSelected()
        self.toolbarGeomAddGPS()
        self.toolbarSave()

    def getGPSValue(self):
        self.assignValue(self.gpswidget.label_X, self.toolwidgetmain.x)
        self.assignValue(self.gpswidget.label_dX, self.toolwidgetmain.dx)
        self.assignValue(self.gpswidget.label_Y, self.toolwidgetmain.y)
        self.assignValue(self.gpswidget.label_dY, self.toolwidgetmain.dy)
        self.assignValue(self.gpswidget.label_Z, self.toolwidgetmain.z)
        self.assignValue(self.gpswidget.label_dZ, self.toolwidgetmain.dz)

    def assignValue(self, wdgfrom, wdgto):
        if self.isfloat(wdgfrom.text()):
            wdgto.setValue(float(wdgfrom.text()))

    def isfloat(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    # def postSaveFeature(self, boolnewfeature):
    def postSaveFeature(self, savedfeaturepk=None):

        if self.currentFeaturePK is not None and self.dbase.variante in ["2018_SNCF"]:
            libelle = ""
            sql = (
                "SELECT nodetype, networktype ,id_node  FROM node_qgis WHERE pk_node = "
                + str(self.currentFeaturePK)
            )
            typeouvrage, typereseau, idnoeud = self.dbase.query(sql)[0]
            if typeouvrage in ["60", "70", "71"]:
                libelle += "R"
                if typereseau == "PLU":
                    libelle += "P"
                elif typereseau == "USE":
                    libelle += "V"
                elif typereseau == "UNI":
                    libelle += "U"
                elif typereseau == "IND":
                    libelle += "I"
            elif typeouvrage in ["10"]:
                libelle += "POR"
            elif typeouvrage in ["22"]:
                libelle += "FOS"
            elif typeouvrage in ["51"]:
                libelle += "PUI"
            elif typeouvrage in ["21"]:
                libelle += "DSH"
            elif typeouvrage in ["40"]:
                libelle += "DOR"
            else:
                libelle += "DIV"

            libelle += "_" + str(
                self.dbase.getValuesFromPk(
                    "node_qgis", "id_node", self.currentFeaturePK
                )
            )

            pkobjet = self.dbase.getValuesFromPk(
                "node_qgis", "pk_object", self.currentFeaturePK
            )

            sql = (
                "UPDATE object SET name = '"
                + libelle
                + "' WHERE pk_object = "
                + str(pkobjet)
            )
            self.dbase.query(sql)
            self.toolwidgetmain.name.setText(libelle)


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), "lamia_form_node_ui.ui")
        uic.loadUi(uipath, self)


class UserUI_2(QWidget):
    def __init__(self, parent=None):
        super(UserUI_2, self).__init__(parent=parent)
        uipath = os.path.join(
            os.path.dirname(__file__),
            "lamia_form_node_ui_2018SNCF_secondarypropertiestab.ui",
        )
        uic.loadUi(uipath, self)


class UserUI_3(QWidget):
    def __init__(self, parent=None):
        super(UserUI_3, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), "lamia_form_node_ui_CD41.ui")
        uic.loadUi(uipath, self)
