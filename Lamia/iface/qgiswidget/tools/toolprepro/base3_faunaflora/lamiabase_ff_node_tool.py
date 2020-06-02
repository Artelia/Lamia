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
from ..base3.lamiabase_node_tool import BaseNodeTool

from ..subwidgets.subwidget_getfromcatalog import CatalogWidget



class BaseUrbandrainageNodeTool(BaseNodeTool):

    PREPROTOOLNAME = 'node_fauna'
    tooltreewidgetSUBCAT =QtCore.QCoreApplication.translate('base3','Fauna')
    TABLEFILTERFIELD = {'nodecategory': 'FAU' }

    def __init__(self, **kwargs):
        super(BaseUrbandrainageNodeTool, self).__init__(**kwargs)



    def initMainToolWidget(self):
        
        self.toolwidgetmain = UserUI()
        self.formtoolwidgetconfdictmain = {'node' : {'linkfield' : 'id_node',
                                                    'widgets' : {
                                                                'nodecategory':self.toolwidgetmain.comboBox_nodecategory,
                                                                'faunadevstage':self.toolwidgetmain.comboBox_faunadevstage,
                                                                'number':self.toolwidgetmain.spinBox_number,
                                                                'faunachar1':self.toolwidgetmain.comboBox_faunachar1,

                                                    }},
                                    'object' : {'linkfield' : 'id_object',
                                                'widgets' : {
                                                    'comment': self.toolwidgetmain.textBrowser_comment,
                                                    }},
                                    'descriptionsystem' : {'linkfield' : 'id_descriptionsystem',
                                                'widgets' : {
                                                            'orderclass': self.toolwidgetmain.lineEdit_orderclass,
                                                            'commonname':self.toolwidgetmain.lineEdit_commonname,
                                                            'scientificname':self.toolwidgetmain.lineEdit_scientificcname,
                                                        
                                                        }}}
        self.toolwidgetmain.comboBox_nodecategory.currentIndexChanged.connect(self.changeCategorie)
        self.toolwidgetmain.toolButton_number.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.spinBox_number))




        self.catalogfinder = CatalogWidget(parentwdg=self,
                                                  parentframe=self.toolwidgetmain.frame_catalog,
                                                  catalogtype='faunaflora',
                                                  catalogname = 'LISTE_faune_2019',
                                                  catalogsheet=None,
                                                  coltoshow=['Nom français', 'Nom latin'],
                                                  sheetfield='orderclass',
                                                  valuefield=["commonname",
                                                                'scientificname'])






    def postSaveFeature(self, savedfeaturepk=None):
        super().postSaveFeature(savedfeaturepk)




class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabase_ff_node_tool_ui.ui')
        uic.loadUi(uipath, self)

