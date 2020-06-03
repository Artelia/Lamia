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
from ..base3.lamiabase_surface_tool import BaseSurfaceTool

from ..subwidgets.subwidget_getfromcatalog import CatalogWidget



class BaseFaunafloraSurfaceTool(BaseSurfaceTool):

    PREPROTOOLNAME = 'surface_flora'
    tooltreewidgetSUBCAT =QtCore.QCoreApplication.translate('base3','Flora')
    TABLEFILTERFIELD = {'surfacecategory': 'FLO' }

    def __init__(self, **kwargs):
        super(BaseFaunafloraSurfaceTool, self).__init__(**kwargs)



    def initMainToolWidget(self):
        
        self.toolwidgetmain = UserUI()
        self.formtoolwidgetconfdictmain = {'surface' : {'linkfield' : 'id_surface',
                                                    'widgets' : {

                                                                'number':self.toolwidgetmain.spinBox_number,


                                                    }},
                                    'object' : {'linkfield' : 'id_object',
                                                'widgets' : {
                                                    'comment': self.toolwidgetmain.textBrowser_comment,
                                                    }},
                                    'descriptionsystem' : {'linkfield' : 'id_descriptionsystem',
                                                'widgets' : {
                                                            # 'orderclass': self.toolwidgetmain.lineEdit_orderclass,
                                                            'commonname':self.toolwidgetmain.lineEdit_commonname,
                                                            'scientificname':self.toolwidgetmain.lineEdit_scientificcname,
                                                        
                                                        }}}
        self.toolwidgetmain.comboBox_category.currentIndexChanged.connect(self.changeCategory)
        self.toolwidgetmain.toolButton_number.clicked.connect(
            lambda: self.showNumPad(self.toolwidgetmain.spinBox_number))


        self.catalogfinder = CatalogWidget(parentwdg=self,
                                                  parentframe=self.toolwidgetmain.frame_catalog,
                                                  catalogtype='faunaflora',
                                                  catalogname = 'Liste_bota_2020',
                                                  catalogsheet='#Liste_Naopad_bota_2020',
                                                  coltoshow=['LB_NOM', 'NOM_VERN'],
                                                  sheetfield=None,
                                                  valuefield=["commonname",
                                                                'scientificname'])
        self.lamiawidgets.append(self.catalogfinder)

    def _widgetClicked_manageToolBar(self):
        super()._widgetClicked_manageToolBar()
        print('ok point')
        self.mainifacewidget.actiontoobargeomnewpoint.setEnabled(True)


    def postSaveFeature(self, savedfeaturepk=None):
        super().postSaveFeature(savedfeaturepk)




class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabase_ff_surface_tool_ui.ui')
        uic.loadUi(uipath, self)

