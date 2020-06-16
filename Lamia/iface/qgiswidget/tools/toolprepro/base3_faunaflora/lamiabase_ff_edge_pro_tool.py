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
import os, csv
import qgis
import sys, datetime
from collections import OrderedDict

from qgis.PyQt import uic, QtCore, QtGui
from qgis.PyQt.QtWidgets import (QWidget, QPushButton)
from ..base3.lamiabase_edge_tool import BaseEdgeTool

from .lamiabase_ff_camera_tool import BaseFaunafloraCameraTool
from .lamiabase_ff_sketch_tool import BaseFaunafloraSketchTool



class BaseFaunafloraEdgeTool(BaseEdgeTool):

    PREPROTOOLNAME = 'edge_protocol'
    tooltreewidgetCAT =QtCore.QCoreApplication.translate('base3','Inventory')
    tooltreewidgetSUBCAT =QtCore.QCoreApplication.translate('base3','Protocol')
    TABLEFILTERFIELD = {'edgecategory': 'PRO' }
    tooltreewidgetICONPATH = os.path.join(os.path.dirname(__file__), 'protocol.png')

    def __init__(self, **kwargs):
        super(BaseFaunafloraEdgeTool, self).__init__(**kwargs)



    def initMainToolWidget(self):
        
        self.toolwidgetmain = UserUI()
        self.formtoolwidgetconfdictmain = {'edge' : {'linkfield' : 'id_surface',
                                                    'widgets' : {
                                                                'edgecategory': self.toolwidgetmain.comboBox_category,
                                                                'edgetype':self.toolwidgetmain.comboBox_edgetype,


                                                    }},
                                    'object' : {'linkfield' : 'id_object',
                                                'widgets' : {
                                                    'comment': self.toolwidgetmain.textBrowser_comment,
                                                    }},
                                    'descriptionsystem' : {'linkfield' : 'id_descriptionsystem',
                                                'widgets' : {
                                                        
                                                        }}}
        self.toolwidgetmain.comboBox_category.currentIndexChanged.connect(self.changeCategory)
        # self.toolwidgetmain.toolButton_number.clicked.connect(
        #     lambda: self.showNumPad(self.toolwidgetmain.spinBox_number))


        self.dbasechildwdgfield = []
        self.instancekwargs['parentwidget'] = self
        self.propertieswdgPHOTOGRAPHIE = BaseFaunafloraCameraTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgPHOTOGRAPHIE)
        self.propertieswdgCROQUIS = BaseFaunafloraSketchTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgCROQUIS)


    def _widgetClicked_manageToolBar(self):
        super()._widgetClicked_manageToolBar()
        self.mainifacewidget.actiontoobargeomnewpoint.setEnabled(True)


class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabase_ff_edge_tool_ui.ui')
        uic.loadUi(uipath, self)
