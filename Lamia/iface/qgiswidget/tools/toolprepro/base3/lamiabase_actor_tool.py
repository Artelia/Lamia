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
from qgis.PyQt.QtWidgets import (QWidget, QInputDialog)

from ...lamia_abstractformtool import AbstractLamiaFormTool


def tr(msg):
    return QtCore.QCoreApplication.translate('BaseActorTool',msg)

class BaseActorTool(AbstractLamiaFormTool):


    DBASETABLENAME = 'actor'
    LOADFIRST = False

    tooltreewidgetCAT = tr('Management')
    tooltreewidgetSUBCAT = tr('Actors')
    tooltreewidgetICONPATH = os.path.join(os.path.dirname(__file__), 'lamiabase_actor_tool_icon.png')

    tempparentjoin = {}
    linkdict = {'colparent': 'id_object',
                'colthistable': 'id_actor',
                    'tctable': 'Tcobjectactor',
                    'tctablecolparent':'lid_object',
                    'tctablecolthistable':'lid_actor'}
    for tablename in ['edge','delivery']:
        tempparentjoin[tablename] = linkdict
    PARENTJOIN = tempparentjoin
    #CHOOSERTREEWDG_COLSHOW = ['societe', 'nom']
    CHOOSERTREEWDGSPEC = {'colshow': ['society', 'actorname']}

    def __init__(self, **kwargs):
        super(BaseActorTool, self).__init__(**kwargs)

  

    def initMainToolWidget(self):

        self.toolwidgetmain = UserUI()

        self.formtoolwidgetconfdictmain = {'actor': {'linkfield': 'id_actor',
                                                        'widgets': {'actorname' : self.toolwidgetmain.lineEdit_nom,
                                                                    'society': self.toolwidgetmain.lineEdit_societe,
                                                                    'role': self.toolwidgetmain.lineEdit_fonction,
                                                                    'adress': self.toolwidgetmain.lineEdit_adresse,
                                                                    'phone': self.toolwidgetmain.lineEdit_tel,
                                                                    'mail': self.toolwidgetmain.lineEdit_mail,
                                                                    'fax': self.toolwidgetmain.lineEdit_fax,
                                                                    }},
                                    'object': {'linkfield': 'id_objet',
                                                'widgets': {}}}



    def postSelectFeature(self):
        pass



    def postSaveFeature(self, savedfeaturepk=None):
        pass


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabase_actor_tool_ui.ui')
        uic.loadUi(uipath, self)