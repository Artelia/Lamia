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

from lamiaqgisiface.iface.qgiswidget.tools.lamia_abstractformtool import (
    AbstractLamiaFormTool,
)
from .lamia_form_camera import BaseCameraTool
from .lamia_form_sketch import BaseSketchTool
from .lamia_form_actor import BaseActorTool
from lamiaqgisiface.iface.qgiswidget.tools.form_subwidgets.subwidget_tcmanytomany import (
    TcmanytomanyChooserWidget,
)
from lamiaqgisiface.iface.qgiswidget.tools.form_subwidgets.subwidget_lidchooser import (
    LidChooserWidget,
)


class BaseFacilityTool(AbstractLamiaFormTool):

    PREPROTOOLNAME = "facility"
    DBASETABLENAME = "facility"
    LOADFIRST = True

    tooltreewidgetCAT = QtCore.QCoreApplication.translate("base3", "Facilities")
    tooltreewidgetSUBCAT = QtCore.QCoreApplication.translate("base3", "Facility")
    tooltreewidgetICONPATH = os.path.join(
        os.path.dirname(__file__), "lamia_form_facility_icon.png"
    )

    # tempparentjoin = {}
    # linkdict = {'colparent': 'id_descriptionsystem',
    #             'colthistable': 'lid_descriptionsystem_1',
    #                 'tctable': None,
    #                 'tctablecolparent':None,
    #                 'tctablecolthistable':None}
    # for tablename in ['node', 'edge', 'equipment']:
    #     tempparentjoin[tablename] = linkdict
    # PARENTJOIN = tempparentjoin

    def __init__(self, **kwargs):
        super(BaseFacilityTool, self).__init__(**kwargs)
        self.instancekwargs = kwargs  # depreciated
        self.instancekwargsforchildwdg = kwargs
        self.instancekwargsforchildwdg["parentwidget"] = self

    def initMainToolWidget(self):

        self.toolwidgetmain = UserUI()
        self.formtoolwidgetconfdictmain = {
            "facility": {
                "linkfield": "id_facility",
                "widgets": {
                    "facilitytype": self.toolwidgetmain.comboBox_type,
                    "facilityfunction": self.toolwidgetmain.facilityfunction,
                },
            },
            "object": {
                "linkfield": "id_object",
                "widgets": {
                    "name": self.toolwidgetmain.lineEdit_name,
                    "comment": self.toolwidgetmain.textBrowser_comm,
                },
            },
            "descriptionsystem": {
                "linkfield": "id_descriptionsystem",
                "widgets": {
                    "city": self.toolwidgetmain.city,
                    "streetname": self.toolwidgetmain.streetname,
                },
            },
        }

        # ****************************************************************************************
        # child widgets
        self.dbasechildwdgfield = []

        if self.parentWidget is None:
            self.instancekwargs["parentwidget"] = self

            self.propertieswdgPHOTOGRAPHIE = BaseCameraTool(**self.instancekwargs)
            self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)

            self.propertieswdgCROQUIS = BaseSketchTool(**self.instancekwargs)
            self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)

            # self.propertieswdgACTOR = BaseActorTool(**self.instancekwargs)
            # self.dbasechildwdgfield.append(self.propertieswdgACTOR)

            # self.tcsubwidget = TcmanytomanyChooserWidget(parentwdg=self ,
            #                                                 tcmanytomanyname='tcobjectactor',
            #                                                 childtablename='actor',
            #                                                 parentmanytomanyfield='id_object',
            #                                                 childmanytomanyfield='id_actor',
            #                                                 childdisplayfields=['actorname', 'society'],
            #                                                 tcmanytomanydisplayfields=['role'])
            # self.toolwidgetmain.frame_actor.layout().addWidget(self.tcsubwidget)
            # self.lamiawidgets.append(self.tcsubwidget)
            # frame_actor
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

    def postSelectFeature(self):
        pass

    def postSaveFeature(self, savedfeaturepk=None):
        pass


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), "lamia_form_facility_ui.ui")
        uic.loadUi(uipath, self)
