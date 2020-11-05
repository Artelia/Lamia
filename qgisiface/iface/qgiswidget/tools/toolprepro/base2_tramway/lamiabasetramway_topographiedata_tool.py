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

from qgis.PyQt import uic, QtCore
from qgis.PyQt.QtWidgets import (QWidget)

from ..base2.lamiabase_topographiedata_tool import BaseTopographiedataTool


class BaseTramwayTopographiedataTool(BasePointtopoTool):


    def __init__(self, **kwargs):
        super(BaseTramwayTopographiedataTool, self).__init__(**kwargs)


    def initMainToolWidget(self):

        self.toolwidgetmain = UserUI()

        self.formtoolwidgetconfdictmain = {'Pointtopo' : {'linkfield' : 'id_pointtopo',
                                                    'widgets' : {'typepointtopo': self.toolwidgetmain.comboBox_position,
                                                                'valeur1': self.toolwidgetmain.doubleSpinBox_valeur1,
                                                                'valeur2': self.toolwidgetmain.doubleSpinBox_valeur2,

                                                                'x': self.toolwidgetmain.doubleSpinBox_X,
                                                                'y': self.toolwidgetmain.doubleSpinBox_Y,
                                                                'zmngf': self.toolwidgetmain.doubleSpinBox_Zngf,
                                                                'dx': self.toolwidgetmain.doubleSpinBox_dX,
                                                                'dy': self.toolwidgetmain.doubleSpinBox_dY,
                                                                'dz': self.toolwidgetmain.doubleSpinBox_dZ,
                                                                'zwgs84': self.toolwidgetmain.doubleSpinBox_Zwgs84,
                                                                'zgps': self.toolwidgetmain.doubleSpinBox_Zgps,
                                                                'raf09': self.toolwidgetmain.doubleSpinBox_raf09,
                                                                'hauteurperche': self.toolwidgetmain.doubleSpinBox_hautperche}}
                                                                }
        #if self.parentWidget is not None and self.parentWidget.DBASETABLENAME == 'Topographie':
        #    self.pushButton_addFeature.setEnabled(True)
        #else:
        #    self.pushButton_addFeature.setEnabled(False)

        self.toolwidgetmain.pushButton_catchvalues.clicked.connect(self.getGPSValues)

        self.gpswidget = {'x' : {'widget' : self.toolwidgetmain.label_X,
                                    'gga' : 'Xcrs'},
                            'y': {'widget': self.toolwidgetmain.label_Y,
                                'gga': 'Ycrs'},
                            'zmngf': {'widget': self.toolwidgetmain.label_Z,
                                'gga': 'zmNGF'},
                            'dx': {'widget': self.toolwidgetmain.label_dX,
                                'gst': 'xprecision'},
                            'dy': {'widget': self.toolwidgetmain.label_dY,
                                'gst': 'yprecision'},
                            'dz': {'widget': self.toolwidgetmain.label_dZ,
                                'gst': 'zprecision'},
                            'zgps': {'widget': self.toolwidgetmain.label_zgps,
                                    'gga': 'elevation'},
                            'zwgs84': {'widget': self.toolwidgetmain.label_zwgs84,
                                    'gga': 'deltageoid'},
                            'raf09': {'widget': self.toolwidgetmain.label_raf09,
                                    'gga': 'RAF09'},
                            'hauteurperche': {'widget': self.toolwidgetmain.label_hautperche,
                                    'gga': 'hauteurperche'}
                            }


        
class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabasetramway_topographiedata_tool_ui.ui')
        uic.loadUi(uipath, self)